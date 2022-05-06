# Reservation System
## A reservation system for a hotel. Customer and bokking data
## are handled and can be viewed as well as saved.

## File and directory structure
    
  - Root directory includes all code, and README files.
  - Documents includes project plan and Project document.
  - Test textfiles include text files that can be used to test the code.


## Installation instructions

  - Only library that has been used is the "Time" library, which is automatically built into python.

## User instructions

    The reservation system is made for a hotel that has 3 rooms. The duration of a booking is always 1 day. The program always
    tries to book for the first room, but if it's already booked it tries for the second and third room, if none is available
    the user is shown a message which says the hotel is fully booked that day.
    When starting the program the user is shown a menu that has 6 different options to choose from by pressing keys 0-5.

    By typing "1" the user is able to make a booking to the hotel.
    By typing "2" the user gets a print of what customers is/has been at the hotel, the customer name and phone number is shown.
    By typing "3" the user is shown a record of all bookings on the hotel, both past and future.
    By typing "4" the user can load a textfile containing a record of customers and bookings. After loading the file the user can see everything that
    was booked and all customers on the file.
    By typing "5" the user can save a textfile containing all records, bookings and customers, that have been made.
    By typing "0" the program is exited.
