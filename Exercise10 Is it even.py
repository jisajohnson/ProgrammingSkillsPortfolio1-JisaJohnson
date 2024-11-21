#10. Is it even?
def even_or_odd(number):
    return f"The number {number} is even" if number%2==0 else f"The number {number} is odd" #To check if the code is even or odd

def main():
    number = int(input("Enter a number:")) #asks the user to input a number
    odd_or_even = even_or_odd(number) #to check if the number the user has inputted is odd or even
    print(odd_or_even) #it declares whether the number the user has given is odd or even

if __name__ == "__main__": #calls the main function and it is printed within the main function
    main()
