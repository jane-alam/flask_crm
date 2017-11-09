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


@app.route("/", methods=["POST", "GET"])
def HomePage():
    form = ClientsForm()
    if form.validate_on_submit():
        new_cl = ClientsDB(
            cl_name=form.cl_name.data
        )
        db.session.add(new_cl)
        db.session.commit()
        return "New Client added successfully"
    return render_template("clients.html", form=form)


if __name__ == "__main__":
    app.run()
