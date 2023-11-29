from flask import Blueprint, render_template

# using Blueprint create crud application
crud = Blueprint(
    "crud",
    __name__,
    template_folder = "templates",
    static_folder="static",
)

# create index endpoint and return index.html
@crud.route("/")
def index():
    return render_template("crud/index.html")