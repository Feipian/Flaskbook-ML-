from email_validator import validate_email, EmailNotValidError
from flask import (Flask, render_template,
     url_for, current_app,
    g, request, redirect,
    flash,)

from flask_mail import Mail, Message
from dotenv import load_dotenv
import logging
from flask_debugtoolbar import DebugToolbarExtension
import os

from flask_mail import Mail


load_dotenv()

# create a instance
app = Flask(__name__)
# the toolbar is only enabled in debug mode:
app.debug = True

# add secret_key
app.config["SECRET_KEY"] = "2AZSMss3p5QPbcY2hBsJ"

# setting application in debugToolbarExtension
toolbar = DebugToolbarExtension(app)

# setting logger level
app.logger.setLevel(logging.DEBUG)
app.logger.critical("fatal error")
app.logger.error("error")
app.logger.warning("warning")
app.logger.info("info")
app.logger.debug("debug")

# avoid intercept redirects
app.config["DEBUG_TB_INTERCEPT_REDIRECTS"] = False

# add Mail type
app.config["MAIL_SERVER"] = os.environ.get("MAIL_SERVER")
app.config["MAIL_PORT"] = os.environ.get("MAIL_PORT")
app.config["MAIL_USE_TLS"] = os.environ.get("MAIL_USE_TLS")
app.config["MAIL_USERNAME"] = os.environ.get("MAIL_USERNAME")
app.config["MAIL_PASSWORD"] = os.environ.get("MAIL_PASSWORD")
app.config["MAIL_DEFAULT_SENDER"] = os.environ.get("MAIL_DEFAULT_SENDER")

# login flask-mail package
mail = Mail(app)


@app.route("/")
def index():
        return "Hello, Flaskbook!"

@app.route("/hello/<name>",
            methods=["GET","POST"])
def hello(name):
    return render_template("index.html", name=name)

@app.route("/name/<name>")
def show_name(name):
    return render_template("index.html", name=name)

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/contact/complete", methods=["GET", "POST"])
def contact_complete():
    if request.method == "POST":
        

        # using form get form attribute
        username = request.form["username"]
        email = request.form["email"]
        description = request.form["description"]



        # 輸入檢測
        is_valid = True

        if not username:
            flash("must write down username")
            is_valid = False
        
        if not email:
            flash("Must write email address")
            is_valid = False

        try:
            validate_email(email)
        except EmailNotValidError:
            flash("Please enter correct email address.")
            is_valid = False
        
        if not description:
            flash("Must to write some content.")
            is_valid = False

        if not is_valid:
            return redirect(url_for("contact"))
        # send mail
        send_email(
            email,
            "Thank your mail",
            "contact_mail",
            username=username,
            description = description,
        )

        # redirect contact endpoint
        flash("Thank for your feedback!")
        return redirect(url_for("contact_complete"))
    
    return render_template("contact_complate.html")

def send_email(to, subject, template, **kwargs):
    """
    send mail function
    """
    msg = Message(subject, recipients=[to])
    msg.body = render_template(template + ".txt", **kwargs)
    msg.html = render_template(template + ".html", **kwargs)
    mail.send(msg)


with app.test_request_context("/users?updated=true"):
    print(request.args.get("updated"))

# with app.test_request_context():
#     #/
#     print(url_for(index))
#     #/hello/world
#     print(url_for("hello-endpoint", name="world"))
#     # /name/ichiro?page=1
#     print(url_for("show_name", name="ichiro", page="1"))

