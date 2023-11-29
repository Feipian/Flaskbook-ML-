from flask import Flask
from pathlib import Path
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    # make a flask instance
    app = Flask(__name__)

    
    # setting application
    app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{Path(__file__).parent.parent / 'local.sqlite'}"
    app.config.from_mapping(
        SECRET_KEY="2AZSMss3p5QPbcY2hBsJ",
        SQLALCHEMY_TRACK_MODIFICATIONS=False
    )

    # connect SQLAlchemy and application
    db.init_app(app)
    # connect Migrate and application
    Migrate(app, db)

    # from crud package import views
    from apps.crud import views as crud_views

    app.register_blueprint(crud_views.crud, url_prefix="/crud")

    return app