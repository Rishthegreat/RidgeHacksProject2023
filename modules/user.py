import random
import sqlite3
import hashlib

# user class
class User:
    def __init__(self, uuid, email, username, password_hash, first_name, last_name, state):
        self.uuid = uuid
        self.email = email
        self.username = username
        self.password_hash = password_hash
        self.first_name = first_name
        self.last_name = last_name
        self.state = state
        self.requests = []
        self.matches = []

    # Add user to database
    def add_to_database(self):
        con = sqlite3.connect('database.db')
        cur = con.cursor()
        cur.execute(
                'INSERT INTO users VALUES (?, ?, ?, ?, ?, ?, ?)',
                (self.uuid, self.email, self.username, self.password_hash, self.first_name, self.last_name, self.state)
            )
        con.commit()
        con.close()    

    def update_user(self):
        con = sqlite3.connect('database.db')
        cur = con.cursor()
        cur.execute(
                'UPDATE users SET email = ?, username = ?, password_hash = ?, first_name = ?, last_name = ?, state = ? WHERE users_uuid = ?',
                (self.email, self.username, self.password_hash, self.first_name, self.last_name, self.state, self.uuid)
            )
        con.commit()
        con.close()

    def add_request(self, request):
        self.requests.append(request)

    def add_match(self, match):
        self.matches.append(match)

    def get_requests(self):
        return self.requests
    
    def get_matches(self):
        return self.matches
    
def create_account(email, username, password, first_name, last_name, state) -> User:
    #generate a random 15 digit integer
    while True:
        uuid = random.randint(100000000000000, 999999999999999)

        # check if uuid is already in database, if so generate a new one
        if get_user_by_uuid(uuid) is None:
            break



    # hash the password
    password_hash = hashlib.sha256((str(uuid) + password).encode('utf-8')).hexdigest()

    # create user object
    user = User(uuid, email, username, password_hash, first_name, last_name, state)
    return user

def get_user_by_uuid(uuid):
    # Search database for user with uuid
    con = sqlite3.connect('database.db')
    cur = con.cursor()
    cur.execute('SELECT * FROM users WHERE users_uuid = ?', (uuid,))
    user_attributes = cur.fetchone()
    con.close()
    
    # If user is not found, return None
    # Else, return user object
    if user_attributes is None:
        return None
    else:
        uuid, email, username, password_hash, first_name, last_name, state = user_attributes
        user = User(uuid, email, username, password_hash, first_name, last_name, state)
        return user
    
def get_user_by_username(username):
    # Search database for user with username
    con = sqlite3.connect('database.db')
    cur = con.cursor()
    cur.execute('SELECT * FROM users WHERE username = ?', (username,))
    user_attributes = cur.fetchone()
    con.close()
    
    # If user is not found, return None
    # Else, return user object
    if user_attributes is None:
        return None
    else:
        uuid, email, username, password_hash, first_name, last_name, state = user_attributes
        user = User(uuid, email, username, password_hash, first_name, last_name, state)
        return user
    
def get_user_by_email(email):
    # Search database for user with email
    con = sqlite3.connect('database.db')
    cur = con.cursor()
    cur.execute('SELECT * FROM users WHERE email = ?', (email,))
    user_attributes = cur.fetchone()
    con.close()
    
    # If user is not found, return None
    # Else, return user object
    if user_attributes is None:
        return None
    else:
        uuid, email, username, password_hash, first_name, last_name, state = user_attributes
        user = User(uuid, email, username, password_hash, first_name, last_name, state)
        return user
    
def check_login(username, password):
    # search database for user with username

    user = get_user_by_username(username)
    if user is None:
        return 'username_not_found'
    
    # check if password is correct
    if user.password_hash == hashlib.sha256((str(user.uuid) + password).encode('utf-8')).hexdigest():
        return 'success'
    
    return 'incorrect_password'