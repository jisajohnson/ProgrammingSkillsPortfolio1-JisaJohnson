#6. Brute Force Attack
correctpassword=12345 #The correct password set by us
attempts=0 #the number of attempts so far

while attempts<5: #when the attempts are less than 5 and the attempts is 0
    password=int(input("Enter the password:")) #this statement will be printed

    if password == correctpassword: #if the password is same as the correct password
        print("Access Granted. You have logged in successfully") #this statement will be printed
        break #to exit the loop since the condition is met
    else: #when the condition is not met, it will repeat again
        attempts += 1 #the number of attempts will be increased
        attemptsleft = 5-attempts #this shows the number of attempts left
        print("Access Denied, Try again. You have", attemptsleft, "attempts remaining!") #when the password is wrong this statement will be printed

if attempts == 5: #When the attempts is more than 5, the loop will be stopped
    ("Access Denied! The maximum number of attempts is reached. The Authorities have been alerted ") #this would be final statement since they couldn't crack the password