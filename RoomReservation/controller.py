from hotel import Hotel
from customer import Customer
import datetime
import calendar
import operator


class Controller():

    def __init__(self):
        self.customers_details = []
        self.hotels_details = []

    def add_customers_details(self, customer_details):
        self.customers_details.append(customer_details)

    def add_hotels_details(self, hotel_hotels):
        self.hotels_details.append(hotel_hotels)
        
    def user_input(self):
        result = True
        try:    
            username = raw_input("Enter username")
            for cutomer in self.customers_details:
                if username == cutomer.name:
                    user_dates = []
                    days_to_stay=int(raw_input("How many days you want to stay \n"))
                    for i in range(0,days_to_stay):
                        user_date=raw_input("Enter date in the format dd/mm/yy")
                        user_dates.append(user_date)
                    break
            else:
                print "Sorry the entered user name is not valid, enter valid"
        except Exception as exception:
            result = False
            print exception
        return result, username, user_dates

    def convert_dates_to_days(self,user_dates):
        result = True
        try:
            user_booking_days=[]
            for index in range(0,len(user_dates)):
                day,month,year=user_dates[index].split("/")
                user_date=datetime.date(int(year),int(month),int(day))
                day=user_date.strftime("%A")
                user_booking_days.append(day)
        except Exception as exception:
            result = False
            print exception
            username, user_dates = controller.user_input()
            user_booking_days = controller.convert_dates_to_days(user_dates)
        return result, user_booking_days
    
    def seperate_days(self, user_booking_days):
        week_days=[]
        week_ends=[]
        days=list(calendar.day_name)
        if len(user_booking_days) == 1:
            if days.index(user_booking_days[0]) <= 4:
                week_days.append(user_booking_days[0])
            else:
                week_ends.append(user_booking_days[0])
        else:
            for index in range(0,len(user_booking_days)):
                if days.index(user_booking_days[index]) <=4:
                    week_days.append(user_booking_days[index])
                else:
                    week_ends.append(user_booking_days[index])
        return  week_days, week_ends
    
    def get_customer_type(self, user_name):
        for customer in self.customers_details:
            if customer.name == user_name:
                customer_type = customer.cutomer_type
                break
        return customer

    def get_hotels_rate(self, customer, week_days, week_ends):
        result = True
        try:
            for hotel_details in self.hotels_details:
                hotel_details.get_hotel_rate(customer.cutomer_type,week_days, week_ends)
        except Exception as exception:
            result = False
            print exception
        return result    

    #import pdb;pdb.set_trace()
    def cheepest_hotel(self):
        result = True
        try:
            cheepest_hotel = ""
            cheepest_rate = self.hotels_details[0].hotel_rate
            for hotel_details in self.hotels_details:
                if hotel_details.hotel_rate < cheepest_rate:
                    cheepest_rate = hotel_details.hotel_rate
                    cheepest_hotel = hotel_details
                else:
                    cheepest_hotel = self.hotels_details[0]
        except Exception as exception:
            result = False
            print exception            
        return result, cheepest_hotel
    
    def get_available_hotel(self, cheepest_hotel):
        result = True
        try:
            available_hotel = ""
            for hotel_details in self.hotels_details:
                if hotel_details.hotel_rate == cheepest_hotel.hotel_rate:
                    if hotel_details.name != cheepest_hotel.name:
                        if hotel_details.rating > cheepest_hotel.rating:
                            available_hotel = hotel_details.name
                        else:
                            available_hotel = cheepest_hotel.name
                    else:
                        available_hotel = cheepest_hotel.name
            print  "available_hotel", available_hotel
        except Exception as exception:
            result = False
            print exception 
        return result

    
if __name__ == "__main__":
    controller = Controller()
    
    customer1 = Customer("Naga", "Regular")
    controller.add_customers_details(customer1)
    customer2 = Customer("Rani", "Reward")
    controller.add_customers_details(customer2)
    customer3 = Customer("Raja", "Regular")
    controller.add_customers_details(customer3)
    customer4 = Customer("raveena", "Reward")
    controller.add_customers_details(customer4)
    customer5 = Customer("Nithya", "Regular")
    controller.add_customers_details(customer5)
    
    Lakewood = Hotel("Lakewood", 3)
    Lakewood.add_price_details(110, 90, 80, 80)
    controller.add_hotels_details(Lakewood)

    Bridgewood = Hotel("Bridgewood", 4)
    Bridgewood.add_price_details(160, 60, 110, 50)
    controller.hotels_details.append(Bridgewood)

    Ridgewood = Hotel("Ridgewood", 5)
    Ridgewood.add_price_details(220, 150, 100, 40)
    controller.add_hotels_details(Ridgewood)

    result, username, user_dates = controller.user_input()
    result, user_booking_days = controller.convert_dates_to_days(user_dates)
    week_days, week_ends = controller.seperate_days(user_booking_days)
    customer = controller.get_customer_type(username)
    result = controller.get_hotels_rate(customer, week_days, week_ends)
    result, cheepest_hotel = controller.cheepest_hotel()
    controller.get_available_hotel(cheepest_hotel)
