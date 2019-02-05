from flask import Flask, request, redirect, render_template
import cgi

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/")
def index():
    return render_template('index.html')

def is_filled(val):
    if val != "":
        return True
    else:
        return False

def no_whitespace(val):
    whitespace = " "
    if whitespace not in val:
        return True
    else:
        return False

def validate_email(val):
    valid_email = re.compile("[a-zA-Z0-9_]+{a-z]+\.[a-z]+")
    if valid_email.match(val):
        return True
    else:
        return False


@app.route("/", methods = ['GET', 'POST'])
def user_signup():
    username=request.form['username']
    password=request.form['password']
    verify=request.form['verify']
    email=request.form['email']

    username_error = ''
    password_error = ''
    verify_error = ''
    email_error = ''

    if len(username) < 3 or len(username) > 20:
        username_error = "Enter a valid username"

    if len(password) < 3 or len(password) > 20:
        password_error = "Enter a valid password"

    if verify != password:
        verify_error = "Passwords must match"
 
    if len(email) < 3 or len(email) > 20:
        email_error = "Enter a valid email"
        if ' ' in email or '@' not in email or '.' not in email:
             email_error = "Enter a valid email"

    if not username_error and not password_error and not verify_error and not email_error:
        return render_template("welcome.html", username=username)
    else:
         return render_template("index.html",
         username=username,
         email=email,
         username_error=username_error, password_error=password_error, verify_error=verify_error, email_error=email_error)

@app.route("/welcome", methods = ['POST'])
def welcome():    
    username = request.args.get('username')
    return render_template("welcome.html", username = username)
         

    

app.run()