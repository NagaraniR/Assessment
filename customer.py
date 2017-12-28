class Customer:

    customer_details = {}
    def __init__(self, name, customer_type):
        customer_details = {}
        self.name = name
        self.customer_type = customer_type

    def get_customer_details(self, customer):
        self.customer_details[customer.name] = customer.customer_type
        return self.customer_details
