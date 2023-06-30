from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    def __repr__(self):
        return '<User %r>' % self.username

@app.get("/", endpoint="index")
def hello_root():
        return render_template('index.html')

@app.get("/about/", endpoint="about")
def hello_about():
    return render_template('about.html')

@app.route("/create-add/", methods=['POST', 'GET'], endpoint="create-add")
def create_add():
    if request.method == "POST":
        name = request.form['name']
        email = request.form['email']

        user = User(username=name, email=email)

        try:
            db.session.add(user)
            db.session.commit()
            return redirect('/')
        except:
            return 'При добавлении произошла ошибка'
    else:
        return render_template("create-add.html")

@app.route("/viewpage/", endpoint="viewpage")
def create_add():
    return render_template("viewpage.html")

if __name__ == '__main__':
    app.run(debug=True)