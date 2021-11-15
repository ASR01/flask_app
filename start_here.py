# This is the mail file for the app

from src.flask_app import app

app.env="development"

if __name__ == "__main__":
    app.run(debug=True)
    