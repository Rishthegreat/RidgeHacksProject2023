import random
import sqlite3

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
        con = sqlite3.connect("database.db")
        cur = con.cursor()
        cur.execute(
                "INSERT INTO users VALUES (?, ?, ?, ?, ?, ?, ?)",
                (self.uuid, self.email, self.username, self.password_hash, self.first_name, self.last_name, self.state)
            )
        con.commit()
        con.close()    

    def update_user(self):
        con = sqlite3.connect("database.db")
        cur = con.cursor()
        cur.execute(
                "UPDATE users SET email = ?, username = ?, password_hash = ?, first_name = ?, last_name = ?, state = ? WHERE users_uuid = ?",
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
        # check if id is unique; if it is, break.
        # TODO: implement this
        break

    # hash the password
    password_hash = hash(str(uuid) + password)

    # create user object
    user = User(uuid, email, username, password_hash, first_name, last_name, state)
    return user

def get_user_by_id(id):
    # search database for user with id
    # return all user data in user object
    # TODO: implement this
    user = None
    return user