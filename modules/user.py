import random
from part_request import PartRequest

# user class
class User:
    def __init__(self, email, username, password_hash, firstname, lastname, location, uuid):
        self.email = email
        self.username = username
        self.password_hash = password_hash
        self.firstname = firstname
        self.lastname = lastname
        self.location = location
        self.uuid = uuid
        self.requests = []
        self.matches = []

    def add_to_database(self):
        # add user to database
        # TODO: implement this
        pass

    def update_user(self):
        # update user in database
        # TODO: implement this
        pass

    def add_request(self, request: PartRequest):
        self.requests.append(request)

    def add_match(self, match):
        self.matches.append(match)

    def get_requests(self):
        return self.requests
    
    def get_matches(self):
        return self.matches
    
def create_new_account(email, username, password, firstname, lastname, address) -> User:
    #generate a random 15 digit integer
    while True:
        uuid = random.randint(100000000000000, 999999999999999)
        # check if id is unique; if it is, break.
        # TODO: implement this
        break

    # hash the password
    password_hash = hash(str(uuid) + password)

    # convert address to lat/long
    # TODO: implement this
    latitute = 0
    longitude = 0

    # create user object
    user = User(email, username, password_hash, firstname, lastname, address, uuid, latitute, longitude)
    return user

def get_user_by_id(id):
    # search database for user with id
    # return all user data in user object
    # TODO: implement this
    user = None
    return user