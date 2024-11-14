#8.Simple Search
Names=["Jake","Zac","Ian","Ron","Sam","Dave"] #Create a list with the listed names
check=input("Enter a name:").capitalize() #Ask the user to input the name they are searching for and it capitalizses the name

if check.lower() in (name.lower() for name in Names): #To check if the person is there in the list and made it case insensitive
    print(check,"is there in the list") #If the person is there in the list, then you will see this in the terminal
else: 
    print(check,"is not there in the list") #if the person is not there in the list, this statement will be printed