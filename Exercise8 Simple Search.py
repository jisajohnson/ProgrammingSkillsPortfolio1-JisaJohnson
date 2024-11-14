#8.Simple Search
Names=["Jake","Zac","Ian","Ron","Sam","Dave"]
check=input("Enter a name:").capitalize()

if check.lower() in (name.lower() for name in Names):
    print(check,"is there in the list")
else:
    print(check,"is not there in the list")