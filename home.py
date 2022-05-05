from reservation import Reservation
from schedule import *

import time

class Home():
    customer_list = Reservation.make_customer_list()
    Rooms = Schedule()
    call = ""
    while call != "0":
        print("\tWELCOME TO HOTEL KAARL\n")
        print("\tWe offer you three fine rooms to stay at!\n")
        print("\t 1 Booking\n")
        print("\t 2 Customers\n")
        print("\t 3 Record\n")
        print("\t 0 Exit\n")
        call = input("\tPlease choose from our menu the option that suits you best:\n\t")
        if call == "1":
            booking_customer, reservation_date = Reservation.Booking(customer_list)
            success = Schedule.insert_schedule(Rooms, reservation_date, booking_customer)
            if success == 1:
                print("\tRoom 1 was successfully booked!\n")
                time.sleep(2)
            elif success == 2:
                print("\tRoom 2 was successfully booked!\n")
                time.sleep(2)
            elif success == 3:
                print("\tRoom 3 was successfully booked!\n")
                time.sleep(2)
            else:
                print("\tUnfortunately we don't have any rooms available for this date.\n")
                time.sleep(2)
        elif call == "2":
            Reservation.print_customers(customer_list)
        elif call == "3":
            Schedule.print_schedule(Rooms)
        elif call == "0":
            exit()





Home()