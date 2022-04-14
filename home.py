import datetime
from reservation import *
from schedule import *
from customer import *

class Home():
    room_1 = Schedule.__init__("Room_1")
    print("\tWELCOME TO HOTEL KAARL\n")
    print("\t 1 Booking\n")
    print("\t 2 Record\n")
    print("\t 0 Exit\n")
    input = input()
    if input == "1":
        reservation_date = Reservation.Booking()
        print(reservation_date)
        print("jajja")
    elif input == "2":
        Schedule()
    elif input == "0":
        exit()


Home()