# This is the mail file for the app

from src.flask_app import app as application

application.env="development"

if __name__ == "__main__":
    application.run(debug=True)
    