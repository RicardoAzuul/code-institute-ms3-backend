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


@app.route("/new_book")
def new_book():
    return render_template("new_book.html")


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)