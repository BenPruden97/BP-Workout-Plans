import os
from flask import (
    Flask, flash, render_template, redirect, request, session, url_for)
from flask_pymongo import PyMongo, DESCENDING
from flask_paginate import Pagination, get_page_args
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


# ----- Page Pagination -----

PER_PAGE = 6


def paginated(workout_plans):
    page, per_page, offset = get_page_args(
        page_parameter='page', per_page_parameter='per_page')
    offset = page * PER_PAGE - PER_PAGE

    return workout_plans[offset: offset + PER_PAGE]


def pagination_args(workout_plans):
    page, per_page, offset = get_page_args(
        page_parameter='page', per_page_parameter='per_page')

    total = len(workout_plans)

    return Pagination(page=page, per_page=PER_PAGE,
                      css_framework='bootstrap4', total=total)


# ----- Home Page -----


@app.route("/")
@app.route("/home")
def home():
    """
    The home page which displays 6 workout plans created by members
    """

    workout_plans = mongo.db.workout_plans.find().sort(
        "_id", DESCENDING).limit(6)
    workout_difficulties = mongo.db.workout_difficulties.find()
    workout_categories = mongo.db.workout_categories.find()
    return render_template(
        "index.html", workout_plans=workout_plans,
        workout_difficulties=workout_difficulties,
        workout_categories=workout_categories
    )


# ----- Search Input -----


@app.route("/search")
def search():
    """
    This is the search query to allow users/members
    to search for workout plans by category and difficulty
    """

    query = request.args.get('query')

    workout_plans = list(
        mongo.db.workout_plans.find({"$text": {"$search": query}}))
    workout_difficulties = mongo.db.workout_difficulties.find()
    workout_categories = mongo.db.workout_categories.find()

    workout_plans_paginated = paginated(workout_plans)
    pagination = pagination_args(workout_plans)

    return render_template(
        "find_workouts.html", workout_plans=workout_plans_paginated,
        workout_difficulties=workout_difficulties,
        workout_categories=workout_categories, pagination=pagination
    )


# ----- Find Workouts Page -----


@app.route("/find_workouts")
def find_workouts():
    """
    The find workouts page which allows users/ members
    to find different workout plans created by members
    """

    workout_plans = list(mongo.db.workout_plans.find().sort(
        "_id", DESCENDING))
    workout_difficulties = mongo.db.workout_difficulties.find()
    workout_categories = mongo.db.workout_categories.find()

    workout_plans_paginated = paginated(workout_plans)
    pagination = pagination_args(workout_plans)

    return render_template(
        "find_workouts.html", workout_plans=workout_plans_paginated,
        workout_difficulties=workout_difficulties,
        workout_categories=workout_categories, pagination=pagination
    )


# ----- Workout Plan Page -----


@app.route("/workout_plan/<workout_plan_id>")
def workout_plan(workout_plan_id):
    """
    The workout plan page which displays the members
    workout plan for users/ members to see
    """

    workout_plan = mongo.db.workout_plans.find_one(
        {"_id": ObjectId(workout_plan_id)})
    workout_difficulties = mongo.db.workout_difficulties.find()
    workout_categories = mongo.db.workout_categories.find()
    return render_template(
        "workout_plan.html", workout_plan=workout_plan,
        workout_difficulties=workout_difficulties,
        workout_categories=workout_categories
    )


# ----- Sign Up Page -----


@app.route("/sign_up", methods=["GET", "POST"])
def sign_up():
    """
    The sign up page to allow the user to sign up to
    BP Workout Plans and become a member
    """

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
        flash("Welcome to the community {}".format(
            request.form.get("username")))

        return redirect(url_for("profile", username=session["member"]))

    return render_template("sign_up.html")


# ----- Log In Page -----


@app.route("/log_in", methods=["GET", "POST"])
def log_in():
    """
    The log in page to allow the user to log into their account
    using the username and password fields
    """

    if request.method == "POST":
        existing_member = mongo.db.members.find_one(
            {"username": request.form.get("username").lower()})

        if existing_member:

            if check_password_hash(
                existing_member["password"],
                    request.form.get("password")):
                session["member"] = request.form.get("username").lower()
                flash("Welcome Back {}!".format(
                    request.form.get("username")))
                return redirect(url_for(
                    "profile", username=session["member"]))
            else:
                flash(
                    """
                    Incorrect Username and/or
                    Password Entered, please try again
                    """
                    )
                return redirect(url_for("log_in"))

        else:
            flash(
                """
                Username Does Not Exist,
                please try again
                """
                )
            return redirect(url_for("log_in"))

    return render_template("log_in.html")


# ----- Contact Page -----


@app.route("/contact", methods=["GET", "POST"])
def contact():
    """
    Contact page to allow the user to contact the developer/
    site owner
    """

    return render_template("contact.html")


# ----- Profile Page -----


@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    """
    The profile page that displays the member's profile.
    The member can update or delete their account from this page
    """

    username = mongo.db.members.find_one(
        {"username": session["member"]})["username"]

    if session["member"]:
        return render_template("profile.html", username=username)

    return redirect("log_in")


# ----- Log Out Functionality -----


@app.route("/log_out")
def log_out():
    """
    Allows the member to log out of their account
    """

    flash("You have been logged out")
    session.pop("member")
    return redirect(url_for("log_in"))


# ----- Create A Workout Plan Page -----


@app.route("/create_workout", methods=["GET", "POST"])
def create_workout():
    """
    This page allows the member to create their own
    workout plan to share with the community
    """

    if request.method == "POST":
        workout_plan = {
            "workout_category": request.form.get("workout_category"),
            "workout_difficulty": request.form.get("workout_difficulty"),
            "workout_name": request.form.get("workout_name"),
            "workout_description": request.form.get("workout_description"),
            "exercise_name_1": request.form.get("exercise_name_1"),
            "number_of_sets_1": request.form.get("number_of_sets_1"),
            "number_of_reps_1": request.form.get("number_of_reps_1"),
            "rest_time_1": request.form.get("rest_time_1"),
            "weight_used_1": request.form.get("weight_used_1"),
            "exercise_name_2": request.form.get("exercise_name_2"),
            "number_of_sets_2": request.form.get("number_of_sets_2"),
            "number_of_reps_2": request.form.get("number_of_reps_2"),
            "rest_time_2": request.form.get("rest_time_2"),
            "weight_used_2": request.form.get("weight_used_2"),
            "exercise_name_3": request.form.get("exercise_name_3"),
            "number_of_sets_3": request.form.get("number_of_sets_3"),
            "number_of_reps_3": request.form.get("number_of_reps_3"),
            "rest_time_3": request.form.get("rest_time_3"),
            "weight_used_3": request.form.get("weight_used_3"),
            "exercise_name_4": request.form.get("exercise_name_4"),
            "number_of_sets_4": request.form.get("number_of_sets_4"),
            "number_of_reps_4": request.form.get("number_of_reps_4"),
            "rest_time_4": request.form.get("rest_time_4"),
            "weight_used_4": request.form.get("weight_used_4"),
            "exercise_name_5": request.form.get("exercise_name_5"),
            "number_of_sets_5": request.form.get("number_of_sets_5"),
            "number_of_reps_5": request.form.get("number_of_reps_5"),
            "rest_time_5": request.form.get("rest_time_5"),
            "weight_used_5": request.form.get("weight_used_5"),
            "exercise_name_6": request.form.get("exercise_name_6"),
            "number_of_sets_6": request.form.get("number_of_sets_6"),
            "number_of_reps_6": request.form.get("number_of_reps_6"),
            "rest_time_6": request.form.get("rest_time_6"),
            "weight_used_6": request.form.get("weight_used_6"),
            "total_workout_time": request.form.get("total_workout_time"),
            "created_by": session["member"]
        }
        mongo.db.workout_plans.insert_one(workout_plan)
        flash("Workout Plan Successfully Added")
        return redirect(url_for('find_workouts'))

    workout_plans = mongo.db.workout_plans.find()
    workout_difficulties = mongo.db.workout_difficulties.find()
    workout_categories = mongo.db.workout_categories.find()
    return render_template(
        "create_workout.html", workout_plans=workout_plans,
        workout_difficulties=workout_difficulties,
        workout_categories=workout_categories
    )


# ----- Edit Workout Plan Page -----


@app.route("/edit_workout/<workout_plan_id>", methods=["GET", "POST"])
def edit_workout(workout_plan_id):
    """
    This page allows the member to edit any of
    their own workout plans to make changes
    """

    if request.method == "POST":
        submit = {
            "workout_category": request.form.get("workout_category"),
            "workout_difficulty": request.form.get("workout_difficulty"),
            "workout_name": request.form.get("workout_name"),
            "workout_description": request.form.get("workout_description"),
            "exercise_name_1": request.form.get("exercise_name_1"),
            "number_of_sets_1": request.form.get("number_of_sets_1"),
            "number_of_reps_1": request.form.get("number_of_reps_1"),
            "rest_time_1": request.form.get("rest_time_1"),
            "weight_used_1": request.form.get("weight_used_1"),
            "exercise_name_2": request.form.get("exercise_name_2"),
            "number_of_sets_2": request.form.get("number_of_sets_2"),
            "number_of_reps_2": request.form.get("number_of_reps_2"),
            "rest_time_2": request.form.get("rest_time_2"),
            "weight_used_2": request.form.get("weight_used_2"),
            "exercise_name_3": request.form.get("exercise_name_3"),
            "number_of_sets_3": request.form.get("number_of_sets_3"),
            "number_of_reps_3": request.form.get("number_of_reps_3"),
            "rest_time_3": request.form.get("rest_time_3"),
            "weight_used_3": request.form.get("weight_used_3"),
            "exercise_name_4": request.form.get("exercise_name_4"),
            "number_of_sets_4": request.form.get("number_of_sets_4"),
            "number_of_reps_4": request.form.get("number_of_reps_4"),
            "rest_time_4": request.form.get("rest_time_4"),
            "weight_used_4": request.form.get("weight_used_4"),
            "exercise_name_5": request.form.get("exercise_name_5"),
            "number_of_sets_5": request.form.get("number_of_sets_5"),
            "number_of_reps_5": request.form.get("number_of_reps_5"),
            "rest_time_5": request.form.get("rest_time_5"),
            "weight_used_5": request.form.get("weight_used_5"),
            "exercise_name_6": request.form.get("exercise_name_6"),
            "number_of_sets_6": request.form.get("number_of_sets_6"),
            "number_of_reps_6": request.form.get("number_of_reps_6"),
            "rest_time_6": request.form.get("rest_time_6"),
            "weight_used_6": request.form.get("weight_used_6"),
            "total_workout_time": request.form.get("total_workout_time"),
            "created_by": session["member"]
        }
        mongo.db.workout_plans.update(
            {"_id": ObjectId(workout_plan_id)}, submit)
        flash("Workout Plan Successfully Updated")

    workout_plan = mongo.db.workout_plans.find_one(
        {"_id": ObjectId(workout_plan_id)})
    workout_plans = mongo.db.workout_plans.find()
    workout_difficulties = mongo.db.workout_difficulties.find()
    workout_categories = mongo.db.workout_categories.find()
    return render_template(
        "edit_workout.html", workout_plan=workout_plan,
        workout_plans=workout_plans, workout_difficulties=workout_difficulties,
        workout_categories=workout_categories
    )


# ----- Delete Workout Plan Functionality -----


@app.route("/delete_workout/<workout_plan_id>")
def delete_workout(workout_plan_id):
    """
    Allows the member to delete any of their own
    workout plans if they no longer want them
    """

    mongo.db.workout_plans.remove(
        {"_id": ObjectId(workout_plan_id)})

    flash("Workout Plan Successfully Deleted")
    return redirect(url_for('find_workouts'))


# ----- Edit Account Page -----


@app.route("/edit_account/<username>", methods=["GET", "POST"])
def edit_account(username):
    """
    Allows the member to edit their account
    by changing their username
    """

    if request.method == "POST":

        mongo.db.members.update_one({"username": session['member']},
                                    {'$set': {
                                        "username": request.form.get(
                                            "username").lower(),
                                    }})
        flash("Your Username Has Been Updated")
        session.pop("member")

        return render_template("log_in.html")

    return render_template("edit_account.html")


# ----- Update Password Functionality -----


@app.route("/update_password/<username>", methods=["GET", "POST"])
def update_password(username):
    """
    Allows the member to edit their account
    by changing their password
    """

    if request.method == "POST":

        mongo.db.members.update_one({"username": session['member']},
                                    {'$set': {
                                        "password": generate_password_hash(
                                            request.form.get("password")),
                                    }})
        flash("Your Password Has Been Updated")
        session.pop("member")

        return render_template("log_in.html")

    return render_template("edit_account.html")


# Delete Member Functionality


@app.route("/delete_member/<username>")
def delete_member(username):
    """
    Allows the member to delete their account
    if they longer want to have one
    """

    mongo.db.members.remove({"username": username.lower()})
    flash("Your Profile Has Been Deleted")
    session.pop("member")

    return redirect(url_for('home'))


# ----- Member's Workout Plans Page -----


@app.route("/my_workouts/<username>", methods=["GET", "POST"])
def my_workouts(username):
    """
    This page will display all of the
    workout plans created by this member
    """

    username = mongo.db.members.find_one(
        {"username": session["member"]})["username"]

    workout_plans = list(mongo.db.workout_plans.find(
        {"created_by": username}).sort(
        "_id", DESCENDING))

    workout_plans_paginated = paginated(workout_plans)
    pagination = pagination_args(workout_plans)

    return render_template(
        "my_workouts.html", username=username,
        workout_plans=workout_plans_paginated, pagination=pagination
    )


# ----- Error Handler Pages -----
# ----- I used this website to help me with the error handler pages:
# https://flask.palletsprojects.com/en/1.1.x/errorhandling/

@app.errorhandler(404)
def page_error(e):

    return render_template("404.html"), 404


@app.errorhandler(500)
def server_error(e):

    return render_template("500.html"), 500


# ----- Declaration of Special Variables -----


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
