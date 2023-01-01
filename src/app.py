from flask import Flask, render_template, request, redirect, url_for, session
from .models import Resume
from .parser import Parser

# Generate and add secret key
app = Flask(__name__)
app.config["SECRET_KEY"] = "secret"


@app.route("/", methods=["GET", "POST"])
def home():

    # Get all available tags from master
    master = Resume.parse_file("db/master.json")
    all_tags = master.get_tags()

    # Get selected tags from session
    selected_tags = set(session.get("selected_tags", []))

    # Get available tags
    available_tags = all_tags - selected_tags

    if request.method == "POST":


        # Get selected tags from request
        selected_tags = set(request.form.getlist("selected-tags"))

        # Get job description and extract tags from it
        job_description = request.form["job-description"]
        selected_tags |= Parser.from_text(job_description) & all_tags

        # Save selected tags to session
        session["selected_tags"] = list(selected_tags)

        return redirect(url_for("home"))

    return render_template(
        "home.html",
        tags= [
            (tag, (tag in selected_tags))
            for tag in all_tags
        ]
    )


@app.route("/render/")
def render():

    # Load master resume
    master = Resume.parse_file("db/master.json")
    tags = set(session.get("selected_tags", []))
    resume = master.render(tags)

    return render_template("render.html", **resume.dict())
