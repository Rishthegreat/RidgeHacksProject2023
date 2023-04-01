from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = 'ThisIsSecret'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/signup', methods=['POST', 'GET'])
def signup():
    if request.method == 'POST':
        email = request.form['email']
        username = hash(request.form['username'])
        password = request.form['password']
        fname = request.form['fname']
        lname = request.form['lname']
        state = request.form['state']
        # Call the database to add the user
        user.create_account(email, username, password, fname, lname, state)
        return redirect('/login')
    else:
        return render_template('signup.html')

@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        session['username'] = request.form['username']
        session['password'] = request.form['password']
        # Call the database to validate the user
        return redirect('/')
    else:
        return render_template('login.html')


@app.route('/mission')
def mission():
    return render_template('mission.html')

if __name__ == '__main__':
    app.run(debug=True)