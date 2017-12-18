import MySQLdb as database
import re
import datetime
import calendar
import time
import sys

 

class NagaWebPage:

    def db_connection(self):
        con=database.connect(host='localhost',user='root',passwd="root",db="naga_customers")
        cur=con.cursor()
        return con,cur
    
    def login_page(self,con,cur):
        key=int(raw_input("""Press one to signup for new account in NagaWebPage
Press two to login \n"""))
        if key==1:
           user_dates,user_mail = page.signUp(con,cur) 
        elif key==2:
            user_mail,user_dates = page.login_account(cur)
        else:
            print "The entered key is not valid.Please re-enter correct key"
            page.login_page()
        return user_mail,user_dates  

    def signUp(self,con,cur):
        username=raw_input("Enter Username for signUp \n")
        mailid=raw_input("Give valid mail id signUp \n")
        password=raw_input("Set password signUp \n")
        mobno=raw_input("Enter mobno signUp \n")
        if re.search("[@.]", mailid) is None:
            print "Sorry the entered mailID not valid .Please valid password"
        else:    
            if re.match(r'[A-Za-z0-9@#$%^&+=]{8,}', password):
                try:
                    cur.execute("""insert into customer_details(Username,Password,mailID,mobNO) values (%s,%s,%s,%s) \n
""",(username,password,mailid,mobno))
                    con.commit()
                    print "Successfully SignUp"
                    user_dates=page.user_input()
                except Exception as exception:
                    print exception
            else:
                print "Sorry the entered password not valid .Please valid password"
        return user_dates,mailid
                
    def login_account(self,cur):
        user_mail = raw_input("Enter mailID or username for login \n")
        password = raw_input("Enter password for login \n")
        query = "select Username from customer_details where mailID='"+user_mail+"'"
        check = cur.execute(str(query))
        if check >= 1:
            query = "select Password from customer_details where Password = '"+ password + "' and mailID = '"+user_mail+"'"
            check_again=cur.execute(str(query))
            if check_again == 1:
                user_dates=page.user_input()
            else:
                print "Sorry the entered password not valid"
        else:
            print "Sorry the enterd email id not valid"
        return user_mail,user_dates

    def user_input(self):
        user_dates = []
        days_to_stay=int(raw_input("How many days you want to stay \n"))
        for i in range(0,days_to_stay):
            dates=raw_input("Enter date in the format dd/mm/yy")
            user_dates.append(dates)  
        return user_dates

    def check_dates(slef,user_dates):
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

    def check_booking_days(self,user_booking_days):
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
        return  user_week_days,user_week_ends

    def check_customer_inLakewood(self,user_mail):
        Lakewood_reward_customer = ""
        Lakewood_reg_customer = ""
        queryOne = "select cusName from Lakewood_reward_customers where emailid = '" + user_mail +"'"
        cur.execute(str(queryOne))
        result=cur.fetchone()
        if result is not None:
            Lakewood_reward_customer=result[0]
        else:
            queryTwo ="select cusName from Lakewood_reg_customers where emailid = '" + user_mail +"'"
            cur.execute(str(queryTwo))
            result = cur.fetchone()
            if result is not None:
                Lakewood_reg_customer = result[0]
            else:
                queryThree = "select Username from customer_details where mailID = '" + user_mail +"'"
                cur.execute(str(queryThree))
                user_name= cur.fetchone() 
                Lakewood_reg_customer=user_name
                try:
                    cur.execute("insert into Lakewood_reg_customers values (%s,%s,%s)",(user_name,user_mail,0))
                    con.commit()
                except Exception as exception:
                    print exception
        return Lakewood_reg_customer, Lakewood_reward_customer

    def check_customer_inBridgewood(self,user_mail):
        Bridgewood_reward_customer = ""
        Bridgewood_reg_customer = ""
        queryOne = "select cusName from Bridgewood_reward_customers where emailid = '" + user_mail +"'"
        cur.execute(str(queryOne))
        result=cur.fetchone()
        if result is not None:
            Bridgewood_reward_customer = result[0]
        else:
            queryTwo ="select cusName from Bridgewood_reg_customers where emailid = '" + user_mail +"'"
            cur.execute(str(queryTwo))
            result = cur.fetchone()
            if result is not None:
                Bridgewood_reg_customer = result[0]
            else:
                queryThree = "select Username from customer_details where mailID = '" + user_mail +"'"
                cur.execute(str(queryThree))
                user_name = cur.fetchone() 
                Bridgewood_reg_customer=user_name
                try:
                    cur.execute("insert into Bridgewood_reg_customers values (%s,%s,%s)",(user_name,user_mail,0))
                    con.commit()
                except Exception as exception:
                    print exception
        return Bridgewood_reward_customer, Bridgewood_reg_customer

    def check_customer_inRidgewood(self,user_mail):
        Ridgewood_reward_customer = ""
        Ridgewood_reg_customer = ""
        queryOne = "select cusName from Ridgewood_reward_customers where emailid = '" + user_mail +"'"
        cur.execute(str(queryOne))
        result=cur.fetchone()
        if result is not None:
            Ridgewood_reward_customer = result[0]
        else:
            queryTwo ="select cusName from Ridgewood_reg_customers where emailid = '" + user_mail +"'"
            cur.execute(str(queryTwo))
            result = cur.fetchone()
            if result is not None:
                Ridgewood_reg_customer = result[0]
            else:
                queryThree = "select Username from customer_details where mailID = '" + user_mail +"'"
                cur.execute(str(queryThree))
                user_name = cur.fetchone() 
                Ridgewood_reg_customer=user_name
                try:
                    cur.execute("insert into Ridgewood_reg_customers values (%s,%s,%s)",(user_name,user_mail,0))
                    con.commit()
                except Exception as exception:
                    print exception
        return Ridgewood_reg_customer,Ridgewood_reward_customer

    def get_Lakewood_customer_amount(self,Lakewood_reg_customer, Lakewood_reward_customer,user_week_days,user_week_ends):
        if Lakewood_reg_customer:
            query="select ((reg_wk_price* %r) + (reg_we_price* %r)) as amount from price_details where hotelName='Lakewood'" %((len(user_week_days),len(user_week_ends)))
            cur.execute(str(query))
            amount=cur.fetchone()
            Lakewood_amount = amount[0]
        else:
            query="select ((rew_wk_price* %r) + (rew_we_price* %r)) as amount from price_details where hotelName='Lakewood'" %((len(user_week_days),len(user_week_ends)))
            cur.execute(str(query))
            amount=cur.fetchone()
            Lakewood_amount = amount[0]   
        return Lakewood_amount

    def get_Bridgewood_customer_amount(self,Bridgewood_reward_customer, Bridgewood_reg_customer,user_week_days,user_week_ends):
        if Bridgewood_reg_customer:
            query="select ((reg_wk_price* %r) + (reg_we_price* %r)) as amount from price_details where hotelName='Bridgewood'" %((len(user_week_days),len(user_week_ends)))
            cur.execute(str(query))
            amount=cur.fetchone()
            Bridgewood_amount=amount[0]
        else:
            query="select ((rew_wk_price* %r) + (rew_we_price* %r)) as amount from price_details where hotelName='Bridgewood'" %((len(user_week_days),len(user_week_ends)))
            cur.execute(str(query))
            amount=cur.fetchone()
            Bridgewood_amount=amount[0]   
        return Bridgewood_amount

    def get_Ridgewood_customer_amount(self,Ridgewood_reg_customer,Ridgewood_reward_customer,user_week_days,user_week_ends):
        if Ridgewood_reg_customer:
            query="select ((reg_wk_price* %r) + (reg_we_price* %r)) as amount from price_details where hotelName='Ridgewood'" %((len(user_week_days),len(user_week_ends)))
            cur.execute(str(query))
            amount=cur.fetchone()
            Ridgewood_amount=amount[0]
        else:
            query="select ((rew_wk_price* %r) + (rew_we_price* %r)) as amount from price_details where hotelName='Ridgewood'" %((len(user_week_days),len(user_week_ends)))
            cur.execute(str(query))
            amount=cur.fetchone()
            Ridgewood_amount=amount[0]   
        return Ridgewood_amount

    def check_cheepest_room(self,Lakewood_amount,Bridgewood_amount,Ridgewood_amount):
        available_hotel = ""
        if Lakewood_amount < Bridgewood_amount and Lakewood_amount< Ridgewood_amount:
            available_hotel = "Lakewood"
        elif  Bridgewood_amount < Lakewood_amount and  Bridgewood_amount <  Ridgewood_amount:
            available_hotel = "Bridgewood"
        elif Ridgewood_amount <  Lakewood_amount and  Ridgewood_amount <  Bridgewood_amount:
            available_hotel = "Ridgewood"
        else:
            available_hotel = page.get_available_room(Lakewood_amount,Bridgewood_amount,Ridgewood_amount)
        print "The cheepest price hotel is: \n" ,available_hotel    
        page.reserve()

    def get_available_room(self,Lakewood_amount,Bridgewood_amount,Ridgewood_amount):
        if Lakewood_amount != Bridgewood_amount:
            if Bridgewood_amount != Ridgewood_amount:
                if Lakewood_amount == Ridgewood_amount and Lakewood_amount < Bridgewood_amount:
                    query = "select hotelName from price_details where ratings = (select max(ratings) from price_details where hotelName in ('Lakewood','Ridgewood'))"
                    cur.execute(str(query))
                    result = cur.fetchone()
                    available_hotel = result[0]
                else:
                    available_hotel = Bridgewood_amount
            elif Bridgewood_amount < Lakewood_amount or Ridgewood_amount < Lakewood_amount:
                query = "select hotelName from price_details where ratings = (select max(ratings) from price_details where hotelName in ('Lakewood','Bridgewood'))"
                cur.execute(str(query))
                result = cur.fetchone()
                available_hotel = result[0]
            else:
                print Lakewood_amount
        elif  Lakewood_amount <  Ridgewood_amount or  Bridgewood_amount <  Ridgewood_amount:
            query = "select hotelName from price_details where ratings = (select max(ratings) from price_details where hotelName in ('Lakewood','Bridgewood'))"
            cur.execute(str(query))
            result = cur.fetchone()
            available_hotel = result[0]
        else:
            available_hotel = Ridgewood_amount
        return available_hotel
        
    def reserve(self):
        key = int(raw_input("Press 1 to book \nPress 2 to exit \n"))
        if key == 1:
            print "Room reserved successfully"
        elif key == 2:
            sys.exit()
        else:
            print "The enterd key is not valid"
        
           
page=NagaWebPage()
con,cur=page.db_connection()
user_mail,user_dates=page.login_page(con,cur)
user_booking_days = page.check_dates(user_dates)
user_week_days,user_week_ends=page.check_booking_days(user_booking_days)
Lakewood_reg_customer, Lakewood_reward_customer=page.check_customer_inLakewood(user_mail)
Bridgewood_reward_customer, Bridgewood_reg_customer=page.check_customer_inBridgewood(user_mail)
Ridgewood_reg_customer,Ridgewood_reward_customer=page.check_customer_inRidgewood(user_mail)
Lakewood_amount=page.get_Lakewood_customer_amount(Lakewood_reg_customer, Lakewood_reward_customer,user_week_days,user_week_ends)
Bridgewood_amount=page.get_Bridgewood_customer_amount(Bridgewood_reward_customer, Bridgewood_reg_customer,user_week_days,user_week_ends)
Ridgewood_amount=page.get_Ridgewood_customer_amount(Ridgewood_reg_customer,Ridgewood_reward_customer,user_week_days,user_week_ends)
page.check_cheepest_room(Lakewood_amount,Bridgewood_amount,Ridgewood_amount)
