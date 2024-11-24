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
        12:31} #creates a dictionary of the 12 months

month_number=int(input("Enter a Month number from 1-12:")) #Asks the user to input the month from 1 to 12

if 1 <= month_number or 12>= month_number:
    print("There are",months[month_number],"Months in month",month_number) #To ensure that the user types only a month from 1-12
else:
    print("Error! Enter a valid month number") #If any number other that 1-12 is given it would show error

#Advanced Requirements

leapyearcheck=input("Is it leap year?") #Asks the user if it's leap year
leapyearcheck1= "Yes"

if leapyearcheck.lower() == leapyearcheck1.lower():
    print("February has 29 days in leap year.") #if it's a leap year, this message will be shown
else:
    print("February has 28 days in non-leap year") #if it is not a leap year, then this messasge will be shown