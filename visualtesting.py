from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = 'ThisIsSecret'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/signup', methods=['POST', 'GET'])
def signup():
    return render_template('signup.html')

@app.route('/login', methods=['POST', 'GET'])
def login():
    return render_template('login.html')

@app.route('/offer', methods=['POST', 'GET'])
def offer():
    return render_template('offer.html')

@app.route('/update')
def update():
    return render_template('update.html')

#background process happening without any refreshing
@app.route('/background_process_test')
def background_process_test():
    print("Hello")
    return (matcher.search_for_match(session['uuid']))

if __name__ == '__main__':
    app.run(debug=True)