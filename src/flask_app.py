
from os import environ
from dotenv import load_dotenv
from flask import Flask, render_template, request
from flask_ckeditor import CKEditor
from src.db.db_obj import db
from src.routes.admin.blueprint import admin_blueprint
from src.routes.home.blueprint import home_blueprint
from werkzeug.utils import secure_filename
import sqlite3

#Load env variables
   
load_dotenv()

# Create application objects

app = Flask(__name__)

# Load the cnofig variables

app.config["SQLALCHEMY_DATABASE_URI"] = environ.get("DATABASE_URL")
print(environ.get("DATABASE_URL"))

app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]=True

UPLOAD_FOLDER = 'src/static/uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


# Init the appls

db.init_app(app)

#db.create_all(app=app)

ckeditor = CKEditor()

ckeditor.init_app(app)


app.register_blueprint(home_blueprint)

app.register_blueprint(admin_blueprint)





# to execute it from inside
if __name__ == '__main__':
    app.run(debug = True)