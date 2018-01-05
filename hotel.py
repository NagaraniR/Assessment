class Hotel:

    def __init__(self):
        self.hotels_details = {}
        self.name = ""
        self.rating = ""
    def add_hotel_name(self, hotelName):
        self.hotels_details["hotelName"] = hotelName
        self.name = hotelName
        return self.name
        
    def add_room_Details(self, rooms, rating):
        self.rating = rating
        self.hotels_details["rooms"] = rooms
        self.hotels_details["rating"] = rating

    def add_regular_price_details(self, regular_weekday_Price, regular_weekend_price):
        self.hotels_details["regular_weekday_Price"] = regular_weekday_Price
        self.hotels_details["regular_weekend_price"] = regular_weekend_price
    
    def add_reward_price_details(self, reward_weekday_price,reward_weekend_price):
        self.hotels_details["reward_weekday_price"] = reward_weekday_price
        self.hotels_details["reward_weekend_price"] = reward_weekend_price
