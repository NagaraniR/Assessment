class Hotel:

    def __init__(self, name):
        self.name =  name
        self.room_details = {}
        self.price_details = {}

    def add_room_details(self, rooms, rating):
        self.room_details["rooms"] = rooms
        self.room_details["rating"] = rating

    def add_price_details(self, regular_weekday, regular_weekend, reward_weekday, reward_weekend):
        self.price_details["regular_weekday_price"] = regular_weekday
        self.price_details["regular_weekend_price"] = regular_weekend
        self.price_details["reward_weekday_price"] = reward_weekday
        self.price_details["reward_weekend_price"] = reward_weekend
