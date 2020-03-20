from flask import Flask, render_template,request,flash, url_for, redirect
from passlib.hash import sha256_crypt
from flask_mysqldb import MySQL
import yaml

app = Flask(__name__)

#configure db

db = yaml.load(open('db.yaml'))
app.config['MYSQL_HOST'] = db['mysql_host']
app.config['MYSQL_USER'] = db['mysql_user']
app.config['MYSQL_PASSWORD'] = db['mysql_password']
app.config['MYSQL_DB'] = db['mysql_db']


mysql = MySQL(app)


@app.route('/')
# @app.route('/home')
def home():
    return render_template('home.html')

@app.route('/register', methods=["GET", "POST"])
def register():
    if request.method == "POST":
        name = request.form.get("name")
        username = request.form.get("username")
        password = request.form.get("password")
        confirm = request.form.get("confirm")
        secure_password = sha256_crypt.encrypt(str(password))
        
        if password == confirm:
            cur = mysql.connection.cursor()
            cur.execute("INSERT INTO users(name,username,password) VALUES(%s, %s, %s)", (name, username, password))
            mysql.connection.commit() 
            cur.close()
            flash("you are registered and can login", "success")
            return redirect(url_for('login'))
        else:
            flash("password does not match", "danger")
            return render_template('register.html')
    return render_template('register.html')

@app.route('/login')
def login():
    return render_template('login.html')



if __name__ == '__main__':
    app.secret_key = "1234567csc436finalproject"
    app.run(debug=True)