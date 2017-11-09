from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import Form
from wtforms import StringField

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)


class ClientsDB(db.Model):
    __tablename__ = 'clients'
    id = db.Column(db.INTEGER, primary_key=True)
    cl_name = db.Column(db.String(200))


class ClientsForm(Form):
    cl_name = StringField("Client Name")


@app.route("/")
def HomePage():
    return render_template("clients.html")


if __name__ == "__main__":
    app.run()
