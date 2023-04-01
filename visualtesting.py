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


@app.route('/mission')
def mission():
    return render_template('mission.html')

if __name__ == '__main__':
    app.run(debug=True)