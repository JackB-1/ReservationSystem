from schedule import Schedule

class File():

    def save_file(customer_list, customer_names, customer_phones, Rooms):
        print("\tPlease input name of save file:\n")
        textfile = input(str("\t"))
        with open(textfile, "w") as file:
            for objekt in customer_list:
                file.write(str(objekt) + "\n")
            file.write("END0\n")
            for objekt in customer_names:
                file.write(str(objekt) + "\n")
            file.write("END1\n")
            for objekt in customer_phones:
                file.write(str(objekt) + "\n")
            file.write("END2\n")
            for objekt in Rooms.Reservations1:
                file.write(str(objekt) + "\n")
            file.write("ROOM1\n")
            for objekt in Rooms.Reservations2:
                file.write(str(objekt) + "\n")
            file.write("ROOM2\n")
            for objekt in Rooms.Reservations3:
                file.write(str(objekt) + "\n")
            file.write("ROOM3\n")
            for objekt in Rooms.CustomersRoom1:
                file.write(str(objekt) + "\n")
            file.write("CUSTOM1\n")
            for objekt in Rooms.CustomersRoom2:
                file.write(str(objekt) + "\n")
            file.write("CUSTOM2\n")
            for objekt in Rooms.CustomersRoom3:
                file.write(str(objekt) + "\n")
            file.write("CUSTOM3\n")
        print("\tFile successfully saved.\n")

    def load_file():
        loaded_list = []
        customer_list1 = []
        customer_names = []
        customer_phones = []
        room1 = []
        room2 = []
        room3 = []
        custom1 = []
        custom2 = []
        custom3 = []
        counter = 0
        print("\tPlease input name of file to load:\n")
        textfile = input(str("\t"))
        with open(textfile, "r") as file:
            for line in file:
                if line == "END0\n":
                    counter +=1
                elif line != "END0\n" and counter == 0:
                    customer_list1.append(str(line.strip("\n")))
                elif line != "END1\n" and counter == 1:
                    customer_names.append(str(line.strip("\n")))
                elif line == "END1\n":
                    counter +=1
                elif line != "END2\n" and counter == 2:
                    customer_phones.append(str(line.strip("\n")))
                elif line == "END2\n":
                    counter +=1
                elif line != "ROOM1\n" and counter == 3:
                    room1.append(str(line.strip("\n")))
                elif line == "ROOM1\n":
                    counter +=1
                elif line != "ROOM2\n" and counter == 4:
                    room2.append(str(line.strip("\n")))
                elif line == "ROOM2\n":
                    counter +=1
                elif line != "ROOM3\n" and counter == 5:
                    room3.append(str(line.strip("\n")))
                elif line == "ROOM3\n":
                    counter +=1
                elif line != "CUSTOM1\n" and counter == 6:
                    custom1.append(str(line.strip("\n")))
                elif line == "CUSTOM1\n":
                    counter +=1
                elif line != "CUSTOM2\n" and counter == 7:
                    custom2.append(str(line.strip("\n")))
                elif line == "CUSTOM2\n":
                    counter +=1
                elif line != "CUSTOM3\n" and counter == 8:
                    custom3.append(str(line.strip("\n")))
                elif line == "CUSTOM3\n":
                    counter +=1
        Rooms1 = Schedule()
        Rooms1.Reservations1 = room1
        Rooms1.Reservations2 = room2
        Rooms1.Reservations3 = room3
        Rooms1.CustomersRoom1 = custom1
        for i in custom2:
            Rooms1.CustomersRoom2.append(i)
        for i in custom3:
            Rooms1.CustomersRoom3.append(i)
        return customer_list1, customer_names, customer_phones, Rooms1

    def final_load(customer_list, customer_list1, Rooms1):
        Rooms = Schedule()
        for i in range(len(Rooms1.Reservations1)):
            Rooms.Reservations1.append(Rooms1.Reservations1[i])
        for i in range(len(Rooms1.Reservations2)):
            Rooms.Reservations2.append(Rooms1.Reservations2[i])
        for i in range(len(Rooms1.Reservations3)):
            Rooms.Reservations3.append(Rooms1.Reservations3[i])
        for i in range(len(Rooms1.CustomersRoom1)):
            old = Rooms1.CustomersRoom1[i]
            for j in range(len(customer_list1)):
                if customer_list1[j] == old:
                    Rooms.CustomersRoom1.append(customer_list[j])
        for i in range(len(Rooms1.CustomersRoom2)):
            old = Rooms1.CustomersRoom2[i]
            for j in range(len(customer_list1)):
                if customer_list1[j] == old:
                    Rooms.CustomersRoom2.append(customer_list[j])
        for i in range(len(Rooms1.CustomersRoom3)):
            old = Rooms1.CustomersRoom3[i]
            for j in range(len(customer_list1)):
                if customer_list1[j] == old:
                    Rooms.CustomersRoom3.append(customer_list[j])
        return Rooms