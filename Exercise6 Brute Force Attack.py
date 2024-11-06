#6. Brute Force Attack
correctpassword=12345
attempts=0

while attempts<5:
    password=int(input("Enter the password:"))

    if password == correctpassword:
        print("Access Granted. You have logged in successfully")
        break
    else:
        attempts += 1
        attemptsleft = 5-attempts
        print("Access Denied, Try again. You have", attemptsleft, "attempts remaining!")

if attempts == 5:
    ("Access Denied! The maximum number of attempts is reached. The Authorities have been alerted ")