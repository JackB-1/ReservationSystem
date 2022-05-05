import time
from customer import *

class Schedule:
    def __init__(self):
        self.Reservations1 = []
        self.CustomersRoom1 = []
        self.Reservations2 = []
        self.CustomersRoom2 = []
        self.Reservations3 = []
        self.CustomersRoom3 = []


    def insert_schedule(Rooms, reservation_date, booking_customer):
        if reservation_date not in Rooms.Reservations1:
            Rooms.Reservations1.append(reservation_date)
            Rooms.CustomersRoom1.append(booking_customer)
            return 1
        else:
            if reservation_date not in Rooms.Reservations2:
                Rooms.Reservations2.append(reservation_date)
                Rooms.CustomersRoom2.append(booking_customer)
                return 2
            else:
                if reservation_date not in Rooms.Reservations3:
                    Rooms.Reservations3.append(reservation_date)
                    Rooms.CustomersRoom3.append(booking_customer)
                    return 3
                else:
                    return 0


    def print_schedule(Rooms):
        print("\n\tRoom 1 dates reserved:\n\n")
        print("\t{:12s}  {:25s}\n".format("Booked date", "Customer"))
        for i in range(len(Rooms.Reservations1)):
            customer_name, customer_phone = Customer.get_customer_info(Rooms.CustomersRoom1[i])
            print("\t{:12s}  {:25s}\n".format(Rooms.Reservations1[i], customer_name))
        print("\n\tRoom 2 dates reserved:\n\n")
        print("\t{:12s}  {:25s}\n".format("Booked date", "Customer"))
        for i in range(len(Rooms.Reservations2)):
            customer_name, customer_phone = Customer.get_customer_info(Rooms.CustomersRoom2[i])
            print("\t{:12s}  {:25s}\n".format(Rooms.Reservations2[i], customer_name))
        print("\n\tRoom 3 dates reserved:\n\n")
        print("\t{:12s}  {:25s}\n".format("Booked date", "Customer"))
        for i in range(len(Rooms.Reservations3)):
            customer_name, customer_phone = Customer.get_customer_info(Rooms.CustomersRoom3[i])
            print("\t{:12s}  {:25s}\n".format(Rooms.Reservations3[i], customer_name))
        time.sleep(7)
