import datetime
from reservation import *
from schedule import *
from customer import *

class Home():
    room_1 = Schedule.__init__("Room_1")
    print("\tWELCOME TO HOTEL KAARL\n")
    print("\t 1 Booking\n")
    print("\t 2 Customers\n")
    print("\t 3 Record\n")
    print("\t 0 Exit\n")
    call = input()
    if call == "1":
        reservation_date = Reservation.Booking()
        print(reservation_date)
        print("jajja")
    elif call == "2":
        Customers()
    elif call == "3":
        Schedule()
    elif call == "0":
        exit()
    elif call != "1" or call != "2" or call != "3" or call != "0":




Home()