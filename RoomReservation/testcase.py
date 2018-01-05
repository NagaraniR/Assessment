import unittest
from customer import Customer
from hotel import Hotel
from controller import Controller

class Test(unittest.TestCase):

    def test_customer_init(self):
        self.cutomer1 = Customer("praburam", "Regular")
        self.customer2 = Customer("omprakash", "Reward")
        self.assertEqual(self.cutomer1.name, "praburam")
        self.assertEqual(self.customer2.name, "omprakash")
        self.assertNotEqual(self.cutomer1.cutomer_type, "Reward")
        self.assertEqual(self.customer2.cutomer_type, "Reward")

    def test_convert_dates_to_days(self):
        expected = ["Saturday", "Sunday", "Monday", "Tuesday"]
        user_dates = ["30/12/2017", "31/12/2017", "01/01/2018", "02/01/2018"]
        self.result = Controller()
        self.assertEqual(self.result.convert_dates_to_days(user_dates)[1], expected)
        self.assertNotEqual(self.result.convert_dates_to_days(["03/01/2018"])[1], "Friday")

    def test_seperate_days(self):
        self.result = Controller()
        self.assertEqual(self.result.seperate_days(["Sunday", "Friday"])[0], ["Friday"])
        self.assertNotEqual(self.result.seperate_days(["Sunday", "Friday"])[0], ["Sunday"])
        self.assertNotEqual(self.result.seperate_days(["Monday", "Friday"])[1], ["Friday"])

    def test_get_customer_type(self):
        self.result = Controller()
        self.customer1 = Customer("naren", "Regular")
        self.result.add_customers_details(self.customer1)
        self.customer2 = Customer("kala", "Reward")
        self.result.add_customers_details(self.customer2)
        self.assertEqual(self.result.get_customer_type("kala"), self.customer2)
        self.assertNotEqual(self.result.get_customer_type("naren"), self.customer2)

    def test_get_hotels_rate(self):
        self.result = Controller()
        self.balajibavan = Hotel("balajibavan", 3)
        self.balajibavan.add_price_details(200, 100, 90, 90)
        self.result.add_hotels_details(self.balajibavan)

        self.parsons = Hotel("parsons", 4)
        self.parsons.add_price_details(400, 300, 100, 70)
        self.result.add_hotels_details(self.parsons)

        self.vivera = Hotel("vivera", 5)
        self.vivera.add_price_details(400, 300, 90, 90)
        self.result.add_hotels_details(self.vivera)

        self.garden = Hotel("garden", "")
        self.garden.add_price_details(300, 100, 90, 90)
        self.result.add_hotels_details(self.garden)
        
        self.customer = Customer("kala", "Reward")
        self.result.get_hotels_rate(self.customer, ["Monday"], ["Sunday"])
        result, cheepest_hotel = self.result.cheepest_hotel()
        self.result.get_available_hotel(cheepest_hotel)

        self.result.get_hotels_rate(self.customer, ["Monday"], ["Sunday"])
        result, cheepest_hotel = self.result.cheepest_hotel()
        result = self.result.get_available_hotel(cheepest_hotel)
        self.assertTrue(result)
        self.assertNotEqual(result, False)
        

if __name__ == "__main__":
    unittest.main()
    
