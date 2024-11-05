#3. Biography
information = {"Name":"Jisa Johnson",
               "Hometown":"Fujairah",
               "Age":21}
print(*information.items(),sep='\n')

def personal_details():
    name=input("What is your name?")
    hometown=input("Where is your hometown?")
    age=input(str("what is your age?"))
    print("Name:{}\nHometown:{}\nAge:{}".format(name,hometown,age))
personal_details()