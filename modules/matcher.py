import sqlite3
import modules.user as user

class Match:
    def __init__(self, requester_uuid, offerer_uuid, request_uuid, offer_uuid, part_id):
        self.requester_uuid = requester_uuid
        self.offerer_uuid = offerer_uuid
        self.request_uuid = request_uuid
        self.offer_uuid = offer_uuid
        self.part_id = part_id

    def get_offerer(self):
        return user.get_user_by_uuid(self.offerer_uuid)
    
    def get_requester(self):
        return user.get_user_by_uuid(self.requester_uuid)

# update match for a single user
# used on refresh
def search_for_match(user_uuid) -> Match:
    requester = user.get_user_by_uuid(user_uuid)

    # get all requests for user
    con = sqlite3.connect('database.db')
    cur = con.cursor()
    #cur.execute('SELECT part_id FROM requests WHERE user_uuid = ?', (user_uuid,))
    # search where user is in state of request, and part is in status of pending
    cur.execute('SELECT part_id, uuid FROM requests WHERE user_uuid = ? AND status = ?', (user_uuid, 'pending'))
    requests = cur.fetchone() # tuple of part id and request uuid
    con.close()
    if requests is None:
        return None
    
    part_id, request_uuid = requests

    # get all users with matching part offers
    con = sqlite3.connect('database.db')
    cur = con.cursor()
    cur.execute('SELECT user_uuid, uuid FROM offers WHERE part_id = ? AND status = ? AND state = ?', (part_id, 'pending', requester.state))
    offer = cur.fetchone() # list of tuples of user uuid and offer uuid

    if offer is None:
        return None
    
    offerer_uuid, offer_uuid = offer
    offererer = user.get_user_by_uuid(offerer_uuid)

    # create match
    match = Match(requester.uuid, offerer_uuid, request_uuid, offer_uuid, part_id)
    return match    