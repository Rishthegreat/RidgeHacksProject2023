#schema = list[option: (text: str, outcome: str or recursive list)]
schema = [
    ("I need a part", ),
    ("I have a part", ),
    ("I have a device", ),
    ("I need a device", )
]        

# chat class
class Chat:
    def __init__(self, user_id):
        self.user_id = user_id

    def start_chat(self):    