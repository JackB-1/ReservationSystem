from customer import Customer

class Reservation():


    def Booking(customer_list):
        booking_customer = Customer.fedge_customer(customer_list)
        print("\tWelcome to the Reservation page.\n")
        print("\tPlease input year of the reservation:\n")
        year = int(input("\t"))
        while year < 2022 or year > 2099:
            print("\tNot a valid year, please input year of reservation.")
            year = int(input("\t"))
        print("\tPlease input month of the reservation:\n")
        month = int(input("\t"))
        while month < 1 or month > 12 :
            print("\tNot a valid month, please input month of reservation.")
            month = int(input("\t"))
        print("\tPlease input day of the reservation:\n")
        day = int(input("\t"))
        while day < 1 or day > 31 :
            print("\tNot a valid day, please input day of reservation.")
            day = int(input("\t"))
        reservation_date = str(str(year) + "." + str(month) + "." + str(day))
        return booking_customer, reservation_date

        
    def make_customer_list():
        customer_list = []
        return customer_list

    def print_customers(customer_list):
        Customer.print_customers(customer_list)