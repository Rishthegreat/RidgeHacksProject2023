from flask import Flask, render_template, redirect, session
from flask import request
import modules.user as user
import modules.matcher as matcher

app = Flask(__name__)
app.secret_key = 'ThisIsSecret'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/signup', methods=['POST', 'GET'])
def signup():
    if request.method == 'POST':
        if (request.form['email'] != '' or request.form['username'] != '' or request.form['password'] != '' or request.form['fname'] != '' or request.form['lname'] != '' or request.form['state'] != ''):
            email = request.form['email']
            username = hash(request.form['username'])
            password = request.form['password']
            fname = request.form['fname']
            lname = request.form['lname']
            state = request.form['state']
            # Call the database to add the user
            if (user.username_exists(username) == False and user.email_exists(email) == False):
                user.create_account(email, username, password, fname, lname, state)
                return redirect('/login')
            elif (user.username_exists(username) == True):
                return redirect('/signup', error=True, error_message="Username is in use")
            else:
                return redirect('/signup', error=True, error_message="Email is in use")
        else:
            return redirect('/signup', error=True, error_message="Incomplete form")
    else:
        return render_template('signup.html')

@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':

        username = request.form['username']
        password = request.form['password']
        login_success = user.check_login(username, password)
        if login_success == 'success': # If the user is valid
            session['uuid'] = user.get_user_by_username(username).uuid
            session['username'] = username
            session['logged_in'] = True
            return redirect('/')
        elif login_success == 'username_not_found':
            return redirect('/login', error=True, error_message="Username not found")
        else:
            return redirect('/login', error=True, error_message="Incorrect password")
        # Call the database to validate the user
        return redirect('/')
    else:
        return render_template('login.html')


@app.route('/offer', methods=['POST', 'GET'])
def offer():
    if request.method == 'POST':

        brand = request.form['brand']
        part = request.form['part']
        if(brand == 'apple'):
            device = request.form['apple_device']
        elif (brand == 'samsung'):
            device = request.form['samsung_device']
        else:
            device = request.form['google_device']
        user.update_offers(brand, device, part)

    else:
        return render_template('offer.html')

@app.route('/logout')
def logout():
    session['logged_in'] = False
    session.pop('username', None)
    session.pop('uuid', None)
    return redirect('/')

@app.route('/getrequest', methods=['POST', 'GET'])
def getrequest():
    if request.method == 'POST':

        brand = request.form['brand']
        part = request.form['part']
        if(brand == 'apple'):
            device = request.form['apple_device']
        elif (brand == 'samsung'):
            device = request.form['samsung_device']
        else:
            device = request.form['google_device']

        user.add_request(brand, device, part)

    else:
        return render_template('getrequest.html')

@app.route('/update')
def update():
    if request.method == 'POST':

        match = matcher.search_for_match(session['uuid'])
        if match != None: # If the user is valid
            return redirect('/update', error=True, error_message="Match found! You can contact your offerer by emailing them at" + match.getOfferer.email)
        else:
            return redirect('/update', error=True, error_message="We weren't able to find an offer for you, please try again later")
        # Call the database to validate the user
    else:
        return render_template('update.html')




#background process happening without any refreshing
@app.route('/background_process_test')
def background_process_test():
    print("Hello")
    return (matcher.search_for_match(session['uuid']))

if __name__ == '__main__':
    app.run(debug=True)