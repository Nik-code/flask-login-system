from flask import Flask, render_template, request, redirect, session
from database import *

app = Flask(__name__)
app.secret_key = '431fd96472605f491e83b1e0674944e6'


db = Database(DB_HOST, DB_USER, DB_PASSWORD, DB_NAME)


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        fullname = request.form['fullname']
        email = request.form['email']
        phone = request.form['phone']
        score = request.form['score']

        # Store the user information using the middle layer (Database class)
        db.insert_user(username, password, fullname, email, phone, score)

        return redirect('/')
    return render_template('signup.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Read the user information using the middle layer (Database class)
        user_data = db.get_user(username, password)

        if user_data:
            # Store the username in the session for later use
            session['username'] = username
            return redirect('/user')

        # Show a message if the username or password is incorrect
        message = 'Incorrect username or password'
        return render_template('login.html', message=message)

    message = ''
    return render_template('login.html', message=message)


@app.route('/user')
def user():
    # Get the username from the session
    username = session.get('username')

    if username:
        # Fetch the user data using the middle layer (Database class)
        user_data = db.get_user_by_username(username)

        if user_data:
            return render_template('user.html', user_data=user_data)

    return redirect('/login')


if __name__ == '__main__':
    app.run(debug=True)
