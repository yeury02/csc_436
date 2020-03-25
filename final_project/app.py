from flask import Flask, render_template,request,flash, url_for, redirect
from passlib.hash import sha256_crypt
from flask_mysqldb import MySQL, MySQLdb
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

        if name == username:
            flash ("name and username must be different", "danger")
            return render_template('register.html')
        
        elif password == confirm:
            if len(password) and len(confirm) > 7:
                cur = mysql.connection.cursor()
                cur.execute("INSERT INTO users(name,username,password) VALUES(%s, %s, %s)", (name, username, password))
                mysql.connection.commit() 
                cur.close()
                flash("you are registered and can login", "success")
                return redirect(url_for('login'))
            else:
                flash ("Password is too short!!", "danger")
                return render_template('register.html')
        else:
            flash("password does not match", "danger")
            return render_template('register.html')
    return render_template('register.html')

@app.route('/login', methods=["GET", "POST"])
def login():
    # Output message if something goes wrong...
    msg = ''
    # Check if "username" and "password" POST requests exist (user submitted form)
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
        # Create variables for easy access
        username = request.form['username']
        password = request.form['password']
        flash(username, password)
        # Check if account exists using MySQL
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM accounts WHERE username = %s AND password = %s', (username, password))
        # Fetch one record and return result
        account = cursor.fetchone()
        # If account exists in accounts table in out database
        if account:
            # Create session data, we can access this data in other routes
            session['loggedin'] = True
            session['id'] = account['id']
            session['username'] = account['username']
            # Redirect to home page
            return 'Logged in successfully!'
        else:
            # Account doesnt exist or username/password incorrect
            msg = 'Incorrect username/password!'
    # Show the login form with message (if any)
    return render_template('login.html', msg=msg)

# # http://localhost:5000/python/logout - this will be the logout page
# @app.route('/pythonlogin/logout')
# def logout():
#     # Remove session data, this will log the user out
#    session.pop('loggedin', None)
#    session.pop('id', None)
#    session.pop('username', None)
#    # Redirect to login page
#    return redirect(url_for('login'))

if __name__ == '__main__':
    app.secret_key = "1234567csc436finalproject"
    app.run(debug=True)