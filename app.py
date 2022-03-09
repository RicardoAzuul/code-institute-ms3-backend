import os
import re
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)

# function from https://www.geeksforgeeks.org/how-to-validate-image-file-extension-using-regular-expression/
def imageFile(str):
 
    # Regex to check valid image file extension.
    regex = "([^\\s]+(\\.(?i)(jpe?g|png|gif|bmp))$)"     
    p = re.compile(regex)

    if(re.search(p, str)):
        return True
    else:
        return False


@app.route("/")
@app.route("/get_books")
def get_books():
    books = mongo.db.books.find()
    return render_template("books.html", books=books)


@app.route("/get_book/<book_id>")
def get_book(book_id):
    book = mongo.db.books.find_one({"_id": ObjectId(book_id)})
    # We need to get the reviews dictionary element: this contains the ids for reviews, if there are any
    review_ids = book.get("reviews")
    review_documents = [] 
    # if there are reviews, variable reviews is type list
    if type(review_ids) is list:
        for review_id in review_ids:
            review_document = mongo.db.reviews.find_one({"_id": ObjectId(review_id)})
            review_documents.append(review_document)
    return render_template("book.html", book=book, review_documents=review_documents)


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        user_exists = mongo.db.users.find_one({"username": request.form.get("username").lower()})

        if user_exists:
            flash("Sorry, your username has already been taken!")
            return redirect(url_for("register"))
        
        user_to_register = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password"))
        }
        mongo.db.users.insert_one(user_to_register)

        session["user"] = request.form.get("username").lower()
        flash("Congratulations, you've been registered!")
        return redirect(url_for("profile", username=session["user"]))
        
    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        user_exists = mongo.db.users.find_one({"username": request.form.get("username").lower()})

        if user_exists:
            if check_password_hash(user_exists["password"], request.form.get("password")):
                session["user"] = request.form.get("username").lower()
                flash("Welcome back, {}!".format(request.form.get("username")))
                return redirect(url_for("profile", username=session["user"]))
            else:
                flash("Incorrect username and/or password")
                return redirect(url_for("login"))

        else:
            flash("Incorrect username and/or password")
            return redirect(url_for("login")) 

    return render_template("login.html")


@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    user = mongo.db.users.find_one({"username": session["user"]})
    username = user.get("username")
    # We want to add the titles of books added to the profile page, and also pass through the id of the books, for use with the buttons
    # We want to add the titles of books that are reviewed to the profile page, and also pass through the id of the reviews, for use with the buttons
    books_added = user.get("booksAdded")
    books = []
    if type(books_added) is list:
        for book_id in books_added:
            book_document = mongo.db.books.find_one({"_id": ObjectId(book_id)})
            books.append(book_document)
    reviews_added = user.get("reviewsAdded")
    reviews = []
    if type(reviews_added) is list:
        for review_id in reviews_added:
            review_document = mongo.db.reviews.find_one({"_id": ObjectId(review_id)})
            reviews.append(review_document)

    if session["user"]:
        return render_template("profile.html", username=username, books=books, reviews=reviews)

    return redirect(url_for("login"))


@app.route("/logout")
def logout():
    flash("You have been successfully logged out.")
    session.pop("user")
    return redirect(url_for("login"))


@app.route("/delete_profile")
def delete_profile():
    # TODO: Add code that updates the addedByUser field on the book document, from username to objectID
    # TODO: Add session.pop, like logout?
    user = mongo.db.users.find_one({"username": session["user"]})
    username = user.get("username")
    user_id = user.get("_id")
    reviews_by_user = user.get("reviewsAdded")
    if reviews_by_user != None:
        for review in reviews_by_user:
            print("[PRINT] review", review)
            review_to_delete = mongo.db.reviews.find_one({'_id': ObjectId(review)})
            print("[PRINT] review_to_delete", review_to_delete)
            book_title = review_to_delete.get("booktitle")
            book = mongo.db.books.find_one({"title": book_title})
            mongo.db.books.update_one(book, {'$pull': {'reviews': review}})
            mongo.db.reviews.find_one_and_delete({'_id': ObjectId(review)})  
    mongo.db.users.find_one_and_delete({'username': username})
    flash("Your profile has been deleted.")
    return redirect(url_for("get_books"))


# IMPROVE: this can be done with fewer lines of code
@app.route("/delete_book/<book_id>")
def delete_book(book_id):
    book_to_delete = mongo.db.books.find_one({'_id': ObjectId(book_id)})
    user = mongo.db.users.find_one({"username": session["user"]})
    mongo.db.users.find_one_and_update(user, {'$pull': {'booksAdded': ObjectId(book_id)}})
    reviews_of_book = book_to_delete.get("reviews")
    mongo.db.books.delete_one(book_to_delete)
    if reviews_of_book != None:
        for review in reviews_of_book:
            mongo.db.reviews.find_one_and_delete(review)   
    flash("Book has been deleted.")
    return redirect(url_for("get_books"))

# IMPROVE: this can be done with fewer lines of code
@app.route("/delete_review/<review_id>")
def delete_review(review_id):
    review_to_delete = mongo.db.reviews.find_one({'_id': ObjectId(review_id)})
    book_title = review_to_delete.get("booktitle")
    username = review_to_delete.get("addedByUser")
    book = mongo.db.books.find_one({"title": book_title})
    user = mongo.db.users.find_one({"username": username})
    mongo.db.books.update_one(book, {'$pull': {'reviews': ObjectId(review_id)}})
    mongo.db.users.update_one(user, {'$pull': {'reviewsAdded': ObjectId(review_id)}})
    mongo.db.reviews.delete_one(review_to_delete)

    flash("Review has been deleted.")
    return redirect(url_for("get_books"))


@app.route("/new_book", methods=["GET", "POST"])
def new_book():
    if request.method == "POST":
        # Do I want to lowercase titles?
        book_exists = mongo.db.books.find_one({"title": request.form.get("booktitle")})

        if book_exists:
            flash("This book is already in the database.")
            return redirect(url_for("new_book"))

        cover_image_input = request.form.get("cover-image")
        if imageFile(cover_image_input) == False:
            flash("The url you entered is not an image.")
            return redirect(url_for("new_book"))
        
        book_to_register = {
            "title": request.form.get("booktitle"),
            "authors": request.form.get("authors"),
            "genres": request.form.get("genres"),
            "coverImageURL": request.form.get("cover-image"),
            "blurb": request.form.get("blurb"),
            "upvotes": 0,
            "affiliateLink": "https://fake.affiliate.link",
            "addedByUser": session["user"]
        }
        mongo.db.books.insert_one(book_to_register)
        # When we register a book, we also register its id to the user document that added the book
        registered_book = mongo.db.books.find_one(book_to_register)
        book_id_to_register = registered_book.get("_id")
        user_to_update = mongo.db.users.find_one({"username": session["user"]})
        user_id = user_to_update.get("_id")
        mongo.db.users.update_one({"_id": ObjectId(user_id)}, { '$push': {'booksAdded': book_id_to_register}})

        flash("Book has been added to the database!")
        return redirect(url_for("get_books"))

    return render_template("new_book.html")


@app.route("/new_review/<book_id>", methods=["GET", "POST"])
def new_review(book_id):
    if request.method == "POST":
        book = mongo.db.books.find_one({"title": request.form.get("booktitle")})
       
        review_to_register = {
            "booktitle": request.form.get("booktitle"),
            "reviewtext": request.form.get("review"), 
            "addedByUser": session["user"]
        }
        mongo.db.reviews.insert_one(review_to_register)
        # When a new review is added, we retrieve it again, to insert the id on the book document and on the user document
        registered_review = mongo.db.reviews.find_one(review_to_register)
        review_id_to_register = registered_review.get("_id")
        book_id_to_update = book.get("_id")
        user_to_update = mongo.db.users.find_one({"username": session["user"]})
        user_id = user_to_update.get("_id")
        mongo.db.books.update_one({"_id": ObjectId(book_id_to_update)}, { '$push': {'reviews': review_id_to_register}})
        mongo.db.users.update_one({"_id": ObjectId(user_id)}, { '$push': {'reviewsAdded': review_id_to_register}})

        flash("Review has been added!")
        return redirect(url_for("get_books"))

    book = mongo.db.books.find_one({"_id": ObjectId(book_id)})

    return render_template("new_review.html", book=book)


@app.route("/edit_book/<book_id>", methods=["GET", "POST"])
def edit_book(book_id):
    if request.method == "POST":
        book_to_update_id = book_id   
        title_to_update = request.form.get("booktitle")
        authors_to_update = request.form.get("authors")
        genres_to_update = request.form.get("genres")
        coverImageURL_to_update = request.form.get("cover-image")
        blurb_to_update = request.form.get("blurb")

        if imageFile(coverImageURL_to_update) == False:
            flash("The url you entered is not an image.")
            return redirect(url_for("edit_book", book_id=book_to_update_id))

        mongo.db.books.update_one({"_id": ObjectId(book_id)}, { '$set': {'title': title_to_update, 'authors': authors_to_update, 'genres': genres_to_update, 'coverImageURL': coverImageURL_to_update, 'blurb': blurb_to_update}})

        flash("Book has been updated in the database!")
        return redirect(url_for("get_books"))

    book = mongo.db.books.find_one({"_id": ObjectId(book_id)})

    return render_template("edit_book.html", book=book)


@app.route("/edit_review/<review_id>", methods=["GET", "POST"])
def edit_review(review_id):
    if request.method == "POST":
        reviewtext_to_update = request.form.get("review")

        mongo.db.reviews.update_one({"_id": ObjectId(review_id)}, { '$set': {'reviewtext': reviewtext_to_update}})

        flash("Review has been updated in the database!")
        return redirect(url_for("get_books"))

    review = mongo.db.reviews.find_one({"_id": ObjectId(review_id)})

    return render_template("edit_review.html", review=review)


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)