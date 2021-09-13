import os
from flask import (
    Flask, flash, render_template, redirect, request, session, url_for)
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
@app.route("/home")
def home():
    return render_template("index.html")


@app.route("/find_workouts")
def find_workouts():
    return render_template("find_workouts.html")


@app.route("/sign_up", methods=["GET", "POST"])
def sign_up():
    if request.method == "POST":
        existing_member = mongo.db.members.find_one(
            {"username": request.form.get("username").lower()})

        if existing_member:
            flash("This username already exists, please try again")
            return redirect(url_for("sign_up"))

        sign_up = {
            "username": request.form.get("username").lower(),
            "email": request.form.get("email").lower(),
            "password": generate_password_hash(request.form.get("password")),
        }
        mongo.db.members.insert_one(sign_up)

        session["member"] = request.form.get("username").lower()
        flash("Welcome to the community {}".format(request.form.get("username")))
        return redirect(url_for("profile", username=session["member"]))

    return render_template("sign_up.html")


@app.route("/log_in", methods=["GET", "POST"])
def log_in():
    if request.method == "POST":
        existing_member = mongo.db.members.find_one(
            {"username": request.form.get("username").lower()})

        if existing_member:

            if check_password_hash(existing_member["password"], request.form.get("password")):
                session["member"] = request.form.get("username").lower()
                flash("Welcome Back {}!".format(
                    request.form.get("username")))
                return redirect(url_for(
                    "profile", username=session["member"]))
            else:
                flash("Incorrect Username and/or Password Entered, please try again")
                return redirect(url_for("log_in"))

        else:
            flash("Incorrect Username and/or Password Entered, please try again")
            return redirect(url_for("log_in"))

    return render_template("log_in.html")


@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    username = mongo.db.members.find_one(
        {"username": session["member"]})["username"]

    if session["member"]:
        return render_template("profile.html", username=username)

    return redirect("log_in")


@app.route("/log_out")
def log_out():
    flash("You have been logged out")
    session.pop("member")
    return redirect(url_for("log_in"))


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/create_workout")
def create_workout():
    workout_plans = mongo.db.workout_plans.find()
    workout_difficulties = mongo.db.workout_difficulties.find()
    workout_categories = mongo.db.workout_categories.find()
    return render_template("create_workout.html", workout_plans=workout_plans, workout_difficulties=workout_difficulties, workout_categories=workout_categories)


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
