#3. Biography
information={"Name":"Jisa Johnson",
             "Hometown":"Fujairah",
             "Age":21} #creating a dictionary with personal details
for key, value in information.items(): #Using for function with key-values to show in separate line
    print(f"{key}:{value}") #Prints the information in separate lines

#Advanced Requirements
name=input("What is your name?") #Asks the user to type their name
hometown=input("Where is your hometown?") #Asks the user their hometown
age=input(str("what is your age?")) #Asks the user their age and in case it is written in string it accepts that as well

personal_details={"Name":name,
                  "Hometown":hometown,
                  "age":age} #The overall dictionary of the user's input data
for key, value in personal_details.items(): #to ensure it comes in separate lines
    print(f"{key}:{value}") #prints the personal_details in separate lines