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
    def add_to_database(self) -> None:
        con = sqlite3.connect('database.db')
        cur = con.cursor()
        cur.execute(
                'INSERT INTO users VALUES (?, ?, ?, ?, ?, ?, ?)',
                (self.uuid, self.email, self.username, self.password_hash, self.first_name, self.last_name, self.state)
            )
        con.commit()
        con.close()    

    def update_user(self) -> None:
        con = sqlite3.connect('database.db')
        cur = con.cursor()
        cur.execute(
                'UPDATE users SET email = ?, username = ?, password_hash = ?, first_name = ?, last_name = ?, state = ? WHERE users_uuid = ?',
                (self.email, self.username, self.password_hash, self.first_name, self.last_name, self.state, self.uuid)
            )
        con.commit()
        con.close()

    def add_request(self, request) -> None:
        self.requests.append(request)

    def add_match(self, match) -> None:
        self.matches.append(match)

    def get_requests(self) -> list:
        return self.requests
    
    def get_matches(self) -> list:
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

def get_user_by(request_type, request, return_type='object') -> User | bool:
    # Search database for user with request
    con = sqlite3.connect('database.db')
    cur = con.cursor()
    cur.execute('SELECT * FROM users WHERE ? = ?', (request_type, request))
    user_attributes = cur.fetchone()
    con.close()

    # return user object or boolean
    if user_attributes is None:
        if return_type == 'object':
            return None
        elif return_type == 'boolean':
            return False
    else:
        if return_type == 'object':
            uuid, email, username, password_hash, first_name, last_name, state = user_attributes
            user = User(uuid, email, username, password_hash, first_name, last_name, state)
            return user
        elif return_type == 'boolean':
            return True

def get_user_by_uuid(uuid) -> User:
    return get_user_by('users_uuid', uuid)

def get_user_by_email(email) -> User:
    return get_user_by('email', email)

def get_user_by_username(username) -> User:
    return get_user_by('username', username)

def uuid_exists(uuid) -> bool:
    get_user_by('users_uuid', uuid, 'boolean')

def email_exists(email) -> bool:
    get_user_by('email', email, 'boolean')

def username_exists(username) -> bool:
    get_user_by('username', username, 'boolean')
    
def check_login(username, password) -> str: # success, username_not_found, incorrect_password
    # search database for user with username

    user = get_user_by_username(username)
    if user is None:
        return 'username_not_found'
    
    # check if password is correct
    if user.password_hash == hashlib.sha256((str(user.uuid) + password).encode('utf-8')).hexdigest():
        return 'success'
    
    return 'incorrect_password'