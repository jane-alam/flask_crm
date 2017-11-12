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
    projectss = db.relationship("ProjectsDB", backref="client", lazy="dynamic")


class ProjectsDB(db.Model):
    __tablename__ = 'projects'
    id = db.Column(db.INTEGER, primary_key=True)
    pr_name = db.Column(db.String(200))
    client_id = db.Column(db.INTEGER, db.ForeignKey('clients.id'))


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
    cl_list = ClientsDB.query.all()
    return render_template("clients.html", form=form, cl_list=cl_list)


if __name__ == "__main__":
    app.run()
