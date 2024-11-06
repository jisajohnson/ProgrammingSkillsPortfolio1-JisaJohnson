#5. Days of the Month
months={1:31,
        2:29,
        3:31,
        4:30,
        5:31,
        6:30,
        7:31,
        8:31,
        9:30,
        10:31,
        11:30,
        12:31}

month_number=int(input("Enter a Month number from 1-12:"))

if 1 <= month_number or 12>= month_number:
    print("There are",months[month_number],"Months in month",month_number)
else:
    print("Error! Enter a valid month number")

#Advanced Requirements

leapyearcheck=input("Is it leap year? (yes/no)")
leapyear="Yes"

if leapyearcheck.lower() == "yes":
    print("February has 29 days in leap year.")
else:
    print("February has 28 days in non-leap year")