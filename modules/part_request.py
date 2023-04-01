# PartRequest class
class PartRequest:
    def __init__(self, user, type, brand, part, status, id = None):
        self.user = user
        self.type = type
        self.brand = brand
        self.part = part
        self.status = status
    
    def set_id(self, id):
        self.id = id