import os
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


@app.route("/")
@app.route("/get_books")
def get_books():
    books = mongo.db.books.find()
    return render_template("books.html", books=books)


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
    username = mongo.db.users.find_one({"username": session["user"]})["username"]

    if session["user"]:
        return render_template("profile.html", username=username)

    return redirect(url_for("login"))


@app.route("/logout")
def logout():
    flash("You have been successfully logged out.")
    session.pop("user")
    return redirect(url_for("login"))


@app.route("/delete_profile")
def delete_profile():
    username = mongo.db.users.find_one({"username": session["user"]})["username"]
    mongo.db.users.find_one_and_delete({'username': username})
    flash("Your profile has been deleted.")
    return redirect(url_for("get_books"))


@app.route("/delete_book/<book_id>")
def delete_book(book_id):    
    mongo.db.books.find_one_and_delete({'_id': ObjectId(book_id)})
    flash("Book has been deleted.")
    return redirect(url_for("get_books"))


@app.route("/new_book", methods=["GET", "POST"])
def new_book():
    if request.method == "POST":
        # Do I want to lowercase titles?
        book_exists = mongo.db.books.find_one({"title": request.form.get("booktitle")})

        if book_exists:
            flash("This book is already in the database.")
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

        flash("Book has been added to the database!")
        return redirect(url_for("get_books"))

    return render_template("new_book.html")


@app.route("/new_review", methods=["GET", "POST"])
def new_review():
    if request.method == "POST":
        book_exists = mongo.db.books.find_one({"title": request.form.get("booktitle")})

        if not book_exists:
            flash("There is no book with this title in the database.")
            return redirect(url_for("new_review"))
        
        review_to_register = {
            "title": request.form.get("booktitle"),
            "review": request.form.get("review"), 
            "addedByUser": session["user"]
        }
        mongo.db.reviews.insert_one(review_to_register)

        flash("Review has been added!")
        return redirect(url_for("get_books"))

    return render_template("new_review.html")


@app.route("/edit_book/<book_id>", methods=["GET", "POST"])
def edit_book(book_id):
    if request.method == "POST":      
        book_to_update = {
            "title": request.form.get("booktitle"),
            "authors": request.form.get("authors"),
            "genres": request.form.get("genres"),
            "coverImageURL": request.form.get("cover-image"),
            "blurb": request.form.get("blurb"),
            "upvotes": 0,
            "affiliateLink": "https://fake.affiliate.link",
            "addedByUser": session["user"]
        }
        mongo.db.books.update({"_id": ObjectId(book_id)}, book_to_update)

        flash("Book has been updated in the database!")
        return redirect(url_for("get_books"))

    book = mongo.db.books.find_one({"_id": ObjectId(book_id)})

    return render_template("edit_book.html", book=book)    


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)