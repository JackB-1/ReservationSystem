class Reservation(object):


    def Booking():
        print("\t Welcome to the Reservation page.\n")
        print("\t Please input year of the reservation:\n")
        year = int(input())
        while year < 2022 or year > 2099:
            print("Not a valid year, please input year of reservation.")
            year = int(input())
        month = int(input())
        while month < 1 or month > 12 :
            print("Not a valid month, please input month of reservation.")
            month = int(input())
        day = int(input())
        while day < 1 or day > 31 :
            print("Not a valid day, please input day of reservation.")
            day = int(input())
        reservation_date = str(str(year) + "." + str(month) + "." + str(day))
        return reservation_date
