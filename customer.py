import time

class Customer():
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone


    def get_customer_list():
        customer_list = []
        return customer_list

    def fedge_customer(customer_list):
        name = str(input("\tPlease input your full name:\n\t"))
        for customer in customer_list:
            if customer.name == name:
                return customer
        print("\n\tWelcome new customer, please input your phone number:\n\t")
        phone = str(input("\t"))
        while len(phone) < 9 or len(phone) > 15:
            phone = str(input("\tPlease input valid phone number:\n\t"))
        new_customer = Customer(name, phone)
        customer_list.append(new_customer)
        return new_customer

    def get_customer_info(customer):
        return customer.name, customer.phone


    def print_customers(customer_list):
        print("\tCustomers at Hotel Kaarl:\n\n")
        for customer in customer_list:
            print("\tName: {:25s} Phone number: {:15s}\n\n".format(customer.name, customer.phone))
        time.sleep(4)