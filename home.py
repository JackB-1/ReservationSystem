from reservation import Reservation
from schedule import *
from file import File
import time

class Home():
    customer_list = []
    Rooms = Schedule()
    call = ""
    while call != "0":
        print("\tWELCOME TO HOTEL KAARL\n")
        print("\tWe offer you three fine rooms to stay at!\n")
        print("\t 1 Booking\n")
        print("\t 2 Customers\n")
        print("\t 3 Record\n")
        print("\t 4 Load file\n")
        print("\t 5 Save file\n")
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
        elif call == "4":
            customer_list1, customer_names, customer_phones, Rooms1 = File.load_file()
            customer_list = Reservation.create_customers_from_lists(customer_names, customer_phones)
            Rooms = File.final_load(customer_list, customer_list1, Rooms1)
            print("\tFile successfully loaded.\n")
        elif call == "5":
            customer_names, customer_phones = Reservation.make_customer_lists(customer_list)
            File.save_file(customer_list, customer_names, customer_phones, Rooms)
    print("\n\tThank you for choosing HOTEL KAARL, welcome back!\n")


