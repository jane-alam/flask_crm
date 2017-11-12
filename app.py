from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import Form
from wtforms import StringField
from wtforms_sqlalchemy.fields import QuerySelectField

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)


class ClientsDB(db.Model):
    __tablename__ = 'clients'
    id = db.Column(db.INTEGER, primary_key=True)
    cl_name = db.Column(db.String(200))
    projectss = db.relationship("ProjectsDB", backref="client", lazy="dynamic")

    def __repr__(self):
        return '{}'.format(self.id)


class ProjectsDB(db.Model):
    __tablename__ = 'projects'
    id = db.Column(db.INTEGER, primary_key=True)
    pr_name = db.Column(db.String(200))
    client_id = db.Column(db.INTEGER, db.ForeignKey('clients.id'))


def ChoiceQuery():
    return ClientsDB.query


class ClientsForm(Form):
    cl_name = StringField("Client Name")


class ProjectsForm(Form):
    pr_name = StringField("Project Name")
    client_id = QuerySelectField(query_factory=ChoiceQuery, allow_blank=True, get_label='cl_name')


@app.route("/", methods=["POST", "GET"])
def HomePage():
    # Add Client Form
    form = ClientsForm()
    if form.validate_on_submit():
        new_cl = ClientsDB(
            cl_name=form.cl_name.data
        )
        db.session.add(new_cl)
        db.session.commit()
        return "New Client added successfully"

    # Show All Clients
    cl_list = ClientsDB.query.all()
    return render_template("clients.html", form=form, cl_list=cl_list)


@app.route("/projects", methods=["POST", "GET"])
def ProjectsDef():
    # Add Project Form
    form = ProjectsForm()
    if form.validate_on_submit():
        new_pr = ProjectsDB(
            pr_name = form.pr_name.data,
            client_id = form.client_id.data
        )
        db.session.add(new_pr)
        db.session.commit()
        return "New Project added successfully"

    # Show all Projects
    pr_list = ProjectsDB.query.all()
    return render_template("projects.html", form=form, pr_list=pr_list)

if __name__ == "__main__":
    app.run()
