from hotelModel import Hotel
from customerModel import Customer
import datetime
import calendar
import operator

class Controller(Hotel):
    def __init__(self):
        self.customers_details = {}
        self.hotels_details = {}

    def user_input(self):
        user_dates = []
        username = raw_input("Enter username")
        if username in self.customers_details:
            days_to_stay=int(raw_input("How many days you want to stay \n"))
            for i in range(0,days_to_stay):
                user_date=raw_input("Enter date in the format dd/mm/yy")
                user_dates.append(user_date)
        else:
            print "Sorry the entered user name is not valid, enter valid"
        return username, user_dates

    def convert_dates_to_days(self,user_dates):
        try:
            user_booking_days=[]
            for index in range(0,len(user_dates)):
                day,month,year=user_dates[index].split("/")
                user_date=datetime.date(int(year),int(month),int(day))
                day=user_date.strftime("%A")
                user_booking_days.append(day)
        except Exception as exception:
            print exception
            username, user_dates = controller.user_input()
            user_booking_days = controller.convert_dates_to_days(user_dates)    
        return user_booking_days
    
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
        customer_type = self.customers_details[user_name]
        return customer_type

    def get_each_hotel_rate(self, customer_type, week_days, week_ends):
        hotels_rate = controller.each_hotel_rate(customer_type, week_days, week_ends)
        return hotels_rate

    def display(self, hotels_rate):
        available_hotel = controller.cheepest_hotel(hotels_rate)
        print "The available hotel is \n", available_hotel
        return available_hotel
    

if __name__ == "__main__":
    controller = Controller()
    customer1 = Customer("Naga", "Regular")
    controller.customers_details[customer1.name] = customer1.cutomer_type
    customer2 = Customer("Rani", "Reward")
    controller.customers_details[customer2.name] = customer2.cutomer_type
    customer3 = Customer("Raja", "Regular")
    controller.customers_details[customer3.name] = customer3.cutomer_type
    customer4 = Customer("raveena", "Reward")
    controller.customers_details[customer4.name] = customer4.cutomer_type
    customer5 = Customer("Nithya", "Regular")
    controller.customers_details[customer5.name] = customer5.cutomer_type

    Lakewood = Hotel("Lakewood")
    Lakewood.add_room_details(4,3)
    Lakewood.add_price_details(110, 90, 80, 80)
    controller.hotels_details[Lakewood.name] = dict(Lakewood.room_details.items() + Lakewood.price_details.items())


    Bridgewood = Hotel("Bridgewood")
    Bridgewood.add_room_details(2, 4)
    Bridgewood.add_price_details(160, 60, 110, 50)
    controller.hotels_details[Bridgewood.name] = dict(Bridgewood.room_details.items() + Bridgewood.price_details.items())

    Ridgewood = Hotel("Ridgewood")
    Ridgewood.add_room_details(5, 5)
    Ridgewood.add_price_details(220, 150, 110, 40)
    controller.hotels_details[Ridgewood.name] = dict(Ridgewood.room_details.items() + Ridgewood.price_details.items())

    username, user_dates = controller.user_input()
    user_booking_days = controller.convert_dates_to_days(user_dates)
    week_days, week_ends = controller.seperate_days(user_booking_days)
    customer_type = controller.get_customer_type(username)
    
    hotels_rate = controller.get_each_hotel_rate(customer_type, week_days, week_ends)
    controller.display(hotels_rate)
