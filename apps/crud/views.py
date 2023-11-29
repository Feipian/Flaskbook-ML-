from flask import Blueprint, render_template

# import db
from apps.app import db
#import user class
from apps.crud.models import User

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

@crud.route("/sql")
def sql():
    db.session.query(User).get(2)
    return "check log"