from flask import Flask, render_template, request



app = Flask(__name__)


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
        secure_password = sha256_scrypt.encrypt(str(password))
        
        if password == confirm:
            # insert into database here!
    return render_template('register.html')

@app.route('/login')
def login():
    return render_template('login.html')



# @app.route('/about')
# def about():
#     return render_template('index.html')



if __name__ == '__main__':
    app.run(debug=True)