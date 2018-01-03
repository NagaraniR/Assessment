from hotel import Hotel
from customer import Customer
import datetime
import calendar
import operator

class Controller():

    def __init__(self):
        self.customers_details = []
        self.hotels_details = []

    def user_input(self):
        user_dates = []
        username = raw_input("Enter username")
        for cutomer in self.customers_details:
            if username == cutomer.name:
                days_to_stay=int(raw_input("How many days you want to stay \n"))
                for i in range(0,days_to_stay):
                    user_date=raw_input("Enter date in the format dd/mm/yy")
                    user_dates.append(user_date)
                break    
        else:
            print "Sorry the entered user name is not valid, enter valid"
        return username, user_dates

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
        return customer_type

    def get_hotels_rate(self, customer_type, week_days, week_ends):
        for hotel_details in self.hotels_details:
            hotel_details.get_hotel_rate(customer_type,week_days, week_ends)

    #import pdb;pdb.set_trace()
    def cheepest_hotel(self):
        cheepest_hotel = ""
        cheepest_rate = self.hotels_details[0].hotel_rate
        for hotels_detail in self.hotels_details:
            if hotels_detail.hotel_rate < cheepest_rate:
                cheepest_rate = hotels_detail.hotel_rate
                cheepest_hotel = hotels_detail.name
            else:
                cheepest_hotel = self.hotels_details[0].name
        print "Available hotel is ", cheepest_hotel
        return cheepest_hotel
            
if __name__ == "__main__":
    controller = Controller()
    
    customer1 = Customer("Naga", "Regular")
    controller.customers_details.append(customer1)
    customer2 = Customer("Rani", "Reward")
    controller.customers_details.append(customer2)
    customer3 = Customer("Raja", "Regular")
    controller.customers_details.append(customer3)
    customer4 = Customer("raveena", "Reward")
    controller.customers_details.append(customer4)
    customer5 = Customer("Nithya", "Regular")
    controller.customers_details.append(customer5)
    
    Lakewood = Hotel("Lakewood", 3)
    Lakewood.add_price_details(110, 90, 80, 80)
    controller.hotels_details.append(Lakewood)

    Bridgewood = Hotel("Bridgewood", 4)
    Bridgewood.add_price_details(160, 60, 110, 50)
    controller.hotels_details.append(Bridgewood)

    Ridgewood = Hotel("Ridgewood", 5)
    Ridgewood.add_price_details(220, 150, 110, 40)
    controller.hotels_details.append(Ridgewood)

    username, user_dates = controller.user_input()
    result, user_booking_days = controller.convert_dates_to_days(user_dates)
    week_days, week_ends = controller.seperate_days(user_booking_days)
    customer_type = controller.get_customer_type(username)
    
    hotels_rate = controller.get_hotels_rate(customer_type, week_days, week_ends)
    controller.cheepest_hotel()
