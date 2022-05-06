# ReservationSystem

## Checkpoint2

## Current properties

What properties have you already implemented into your project? What can be done with the program at this point?

My program is done. The project is made according to the level "Easy". This means all easy requirements are 
available;
1. Ability to check if a date/time is reserved and to make a reservation for a chosen time.
2. The program prevents concurrent reservations and, if needed, informs the user about the resource already being reserved at the given point of time.
3. The program marks the chosen resource as reserved for the given points of time.
4. The program can be used to save information on customers (name, phone number) and to connect it to a reservation.
5. The reservations can be saved into and loaded from separate text files.

## Instructions

 - Is it possible to run the program already? (yes/no)
 It is possible to run the program. 

  - How is the program executed?

 The program main function is in the home.py file. When the program is started the user is shown the menu:
        
 "      WELCOME TO HOTEL KAARL

        We offer you three fine rooms to stay at!

         1 Booking

         2 Customers

         3 Record

         4 Load file

         5 Save file

         0 Exit

 "       Please choose from our menu the option that suits you best:
         
         The reservation system is made for a hotel that has 3 rooms. The duration of a booking is always 1 day. The program always
         tries to book for the first room, but if it's already booked it tries for the second and third room, if none is available
         the user is shown a message which says the hotel is fully booked that day.
         A list called "customer_list" and a class object called "Rooms" are created in the 2 first lines of the program. The customer_list
         is a normal list while "Rooms" is a object created through the class "Schedule". "Rooms" object contains 6 lists which are a 
         "reserved dates" and who the customer is that booked it that date, 2 lists for each hotel room so therefore 6 lists.
         
         By typing "1" the user is redirected to reservation class. Then the user is asked for input for one's name. If it's a new 
         customer one is asked to input phone number, if the customer is already a registered customer there is no need for 
         phone number as it is already in the system. The customer fetch/creation happens through customer class where a customer
         is either fetched from the system or created. The customer class creates an object that has "name" and "phone number"
         properties. All customers are stored in the "customer_list". After the customer is fetched, the user is asked
         to input date of the stay at the hotel. Then the customer object and reservation_date is returned 
         to home class where it is fetched to "Schedule" class. There the booking is reserved through "insert_schedule" function into the hotel schedule, if there is
         available rooms that date.The function returns a value to "Home" class depending on this, where the customer is informed whether the booking was successful
         and what room was booked.

         By typing "2" the user gets a print of what customers is/has been at the hotel, the customer name and phone number is shown. This happens through
         "Reservation" and "Customer" classes. 

         By typing "3" the user is shown a record of all bookings on the hotel, both past and future. The record shows "Booked date" and "Customer". This happens 
         through "print_schedule" function in class "Schedule".

         By typing "4" the user can load a textfile containing a record of customers and bookings. After loading the file the user can see everything that
         was booked and all customers on the file. The loading happens through the Class "File" and function "load_file" and "final_load".

         By typing "5" the user can save a textfile containing all records, bookings and customers, that have been made. The savinf happens through 
         the Class "File" and function "save_file".

         The saving and loading is implemented by writing and reading a textfile that contains the information from all 6 lists in "Rooms", customer_list,
         customer_name and customer_phonenumber. The loading of said textfile was challenging to implement. The saving of a file uses the classes
         "Reservation" and "File" while loading the file uses all 5 classes.

         By typing "0" the program is exited and the customer is shown "Thank you for choosing HOTEL KAARL, welcome back!"



## Schedule

 - How much time have you spent making the project this far?

 I have spent approximately 25h.

 - Have you made changes to the schedule of your project plan?

 I implemented a delay function from the "Time" package to give the user a smoother experience.
 I also added a class called "File" where the saving and loading of files are done. This made the process 
 more clear and a cleaner code.

## Other

 - Have you faced any specific problems?

 Small problems when passing very many variables with different types.
