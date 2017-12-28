import datetime
import calendar
import time
from customer import Customer
from hotel import Hotel
import operator


class HotelReservation:

    booked_room_details = {}

    def store_hotel_details(self, hotelsDetails):
        hotels_details = {}
        for hotelDetails in hotelsDetails:
            hotelName = hotelDetails["hotelName"]
            hotelDetails.pop("hotelName", None)
            hotels_details[hotelName] = hotelDetails   
        return hotels_details

    def user_input(self, customers_details):
        user_dates = []
        user_name = raw_input("Enter username")
        if user_name in customers_details:
            days_to_stay=int(raw_input("How many days you want to stay \n"))
            for i in range(0,days_to_stay):
                dates=raw_input("Enter date in the format dd/mm/yy")
                user_dates.append(dates)
        else:
            print "Sorry the entered user name is not valid, enter valid"
        return  user_name, user_dates

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
            page.user_input()   
        return user_booking_days

    def split_booking_days(self,user_booking_days):
        user_week_days=[]
        user_week_ends=[]
        days=list(calendar.day_name)
        if len(user_booking_days) == 1:
            if days.index(user_booking_days[0]) <= 4:
                user_week_days.append(user_booking_days[0])
            else:
                user_week_ends.append(user_booking_days[0])
        else:
            for i in range(0,len(user_booking_days)):
                if days.index(user_booking_days[i]) <=4:
                    user_week_days.append(user_booking_days[i])
                else:
                    user_week_ends.append(user_booking_days[i])          
        return  user_week_days, user_week_ends

    def get_customer_type(self, user_name, customers_details):
        customer_type = customers_details[user_name]
        return customer_type

    def each_hotel_amount(self,customer_type, hotels_details, user_week_days, user_week_ends):
        hotels_amount = []
        for key, value in hotels_details.iteritems():
            if customer_type == "Regular":
                amount = ((value["regular_weekday_Price"] * len(user_week_days)) + (value["regular_weekend_price"] * len(user_week_ends)))
                hotels_amount.append([key, amount]) 
            elif customer_type == "Rewards":
                amount = ((value["reward_weekday_price"] * len(user_week_days)) + (value["reward_weekend_price"] * len(user_week_ends)))
                hotels_amount.append([key, amount])
        return hotels_amount

    def display_hotel(self, hotels_amount, hotels_details):
        print "df", hotels_amount
        hotels_amount = sorted(hotels_amount, key = operator.itemgetter(1))
        count = 1
        for i in range(0, len(hotels_amount)-1):
            if hotels_amount[i][count] == hotels_amount[i+1][count]:
                if hotels_details[hotels_amount[i]][rating] > hotels_details[hotels_amount[i+1][rating]]:
                    print "Available hotel is:", hotels_details[hotels_amount[i]]
                else:
                    print "available hotel is:", hotels_details[hotels_amount[i+1]]
            else:
                print "available Hotel is:", hotels_amount[i]
            break                                                    

    
cutomerOne = Customer("Naga", "Regular")
cutomerOne.get_customer_details(cutomerOne)
customerTwo = Customer("Rani", "Rewards")
customerTwo.get_customer_details(customerTwo)
customerThree = Customer("Raja", "Regular")
customerThree.get_customer_details(customerThree)
customerFour = Customer("Nithya", "Rewards")
customerFour.get_customer_details(customerFour)
customerFive = Customer("Raveena", "Regular")
customers_details = customerFive.get_customer_details(customerFive)
print "fgjkh", customers_details

hotel = Hotel()
hotel.add_hotel_name("Lakewood")
hotel.add_room_Details(2, 3)
hotel.add_regular_price_details(110, 90)
hotel.add_reward_price_details(80, 80)
hotelOneDetails = hotel.hotels_details
    
hotelTwoDetails = Hotel()
hotelTwoDetails.add_hotel_name("Bridgewood")
hotelTwoDetails.add_room_Details(3, 4)
hotelTwoDetails.add_regular_price_details(160, 60)
hotelTwoDetails.add_reward_price_details(110, 50)
hotelTwoDetails = hotelTwoDetails.hotels_details

hotelThreeDetails = Hotel()
hotelThreeDetails.add_hotel_name("Ridgewood")
hotelThreeDetails.add_room_Details(4, 5)
hotelThreeDetails.add_regular_price_details(220, 150)
hotelThreeDetails.add_reward_price_details(110, 40)
hotelThreeDetails = hotelThreeDetails.hotels_details

reservation = HotelReservation()
hotels_details = reservation.store_hotel_details([hotelOneDetails, hotelTwoDetails, hotelThreeDetails])
user_name, user_dates = reservation.user_input(customers_details)
user_booking_days = reservation.convert_dates_to_days(user_dates)
user_week_days,user_week_ends = reservation.split_booking_days(user_booking_days)
customer_type = reservation.get_customer_type(user_name, customers_details)
hotels_amount = reservation.each_hotel_amount(customer_type, hotels_details, user_week_days, user_week_ends)
reservation.display_hotel(hotels_amount, hotels_details)
##Type = reservation.get_cutomer_type(user_name, customer_types)
##amount_details = reservation.get_amount(Type, user_week_days, user_week_ends, regular_price_details, reward_price_details)

