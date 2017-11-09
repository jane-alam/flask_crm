from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import Form
from wtforms import StringField

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)


@app.route("/")
def HomePage():
    return "HomePage"


if __name__ == "__main__":
    app.run()
