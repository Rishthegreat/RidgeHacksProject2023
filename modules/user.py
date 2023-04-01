import random
import sqlite3
import hashlib
import modules.part as part

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
                'UPDATE users SET email = ?, username = ?, password_hash = ?, first_name = ?, last_name = ?, state = ? WHERE uuid = ?',
                (self.email, self.username, self.password_hash, self.first_name, self.last_name, self.state, self.uuid)
            )
        con.commit()
        con.close()

    def add_request(self, requested_part: part.Part) -> None:
        # create uuid for request
        while True:
            uuid = random.randint(100000000000000, 999999999999999)

            # check if uuid is already in database, if so generate a new one
            con = sqlite3.connect('database.db')
            cur = con.cursor()
            cur.execute('SELECT * FROM requests WHERE uuid = ?', (uuid,))
            if cur.fetchone() is None:
                break

        # add request to database
        con = sqlite3.connect('database.db')
        cur = con.cursor()
        cur.execute('INSERT INTO requests VALUES (?, ?, ?, ?, ?)', (uuid, self.uuid, requested_part.part_id, self.state, 'pending'))
        con.commit()
        con.close()

    def add_offer(self, offered_part: part.Part) -> None:
        # create uuid for offer
        while True:
            uuid = random.randint(100000000000000, 999999999999999)

            # check if uuid is already in database, if so generate a new one
            con = sqlite3.connect('database.db')
            cur = con.cursor()
            cur.execute('SELECT * FROM offers WHERE uuid = ?', (uuid,))
            if cur.fetchone() is None:
                break

        # add offer to database
        con = sqlite3.connect('database.db')
        cur = con.cursor()
        cur.execute('INSERT INTO offers VALUES (?, ?, ?, ?, ?)', (uuid, self.uuid, offered_part.part_id, self.state, 'pending'))
        con.commit()
        con.close()
    
def create_account(email, username, password, first_name, last_name, state) -> User:
    #generate a random 15 digit integer
    while True:
        uuid = random.randint(100000000000000, 999999999999999)

        # check if uuid is already in database, if so generate a new one
        if not uuid_exists(uuid):
            break

    # TODO: check if email or username is already in database

    # hash the password
    password_hash = hashlib.sha256((str(uuid) + password).encode('utf-8')).hexdigest()

    # create user object
    user = User(uuid, email, username, password_hash, first_name, last_name, state)
    return user

def get_user_by(request_type, request, return_type='object') -> User | bool:
    # Search database for user with request
    con = sqlite3.connect('database.db')
    cur = con.cursor()
    cur.execute(f'SELECT * FROM users WHERE {request_type} = ?', (request,))
    user_attributes = cur.fetchone()
    con.close()

    # return user object or boolean
    if user_attributes is None:
        if return_type == 'boolean':
            return False
        else:
            return None
    else:
        if return_type == 'boolean':
            return True
        else:
            uuid, email, username, password_hash, first_name, last_name, state = user_attributes
            user = User(uuid, email, username, password_hash, first_name, last_name, state)
            return user

def get_user_by_uuid(uuid) -> User:
    return get_user_by('uuid', uuid)

def get_user_by_email(email) -> User:
    return get_user_by('email', email)

def get_user_by_username(username) -> User:
    return get_user_by('username', username)

def uuid_exists(uuid) -> bool:
    return get_user_by('uuid', uuid, return_type='boolean')

def email_exists(email) -> bool:
    return get_user_by('email', email, return_type='boolean')

def username_exists(username) -> bool:
    return get_user_by('username', username, return_type='boolean')
    
def check_login(username, password) -> str: # success, username_not_found, incorrect_password
    # search database for user with username

    user = get_user_by_username(username)
    if user is None:
        return 'username_not_found'
    
    # check if password is correct
    if user.password_hash == hashlib.sha256((str(user.uuid) + password).encode('utf-8')).hexdigest():
        return 'success'
    
    return 'incorrect_password'