import operator

class Hotel:

    def __init__(self, name, rating):
        self.name =  name
        self.rating = rating
        self.price_details = []
        self.hotel_rate = ""

    def add_price_details(self, regular_weekday, regular_weekend, reward_weekday, reward_weekend):
        self.price_details.append(regular_weekday)
        self.price_details.append(regular_weekend)
        self.price_details.append(reward_weekday)
        self.price_details.append(reward_weekend)

    def get_hotel_rate(self, customer_type, week_days, week_ends):
        if customer_type == "Regular":
            self.hotel_rate = ((self.price_details[0] * len(week_days)) + (self.price_details[1] * len(week_ends)))
        else:
            self.hotel_rate = ((self.price_details[2] * len(week_days)) + (self.price_details[3] * len(week_ends))) 
