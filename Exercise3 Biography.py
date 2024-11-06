#3. Biography
information={"Name":"Jisa Johnson",
             "Hometown":"Fujairah",
             "Age":20} #creating a dictionary with personal details
print(information,sep='\n') #Prints the information in separate lines

#Advanced Requirements 
def personal_details(): #define a function called personal details
    name=input("What is your name?") #Asks the user to type their name
    hometown=input("Where is your hometown?") #Asks the user their hometown
    age=input(str("what is your age?")) #Asks the user their age and in case it is written in string it accepts that as well
    print("Name:{}\nHometown:{}\nAge:{}".format(name,hometown,age)) #Prints the personal details separately as per given by the user
personal_details() #End of the define function