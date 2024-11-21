#4. Primitive Quiz
question=input("What is the capital of France?") #Asks the user the question and they need to type it in
answer="Paris" #This is the answer to the question

if question.lower()==answer.lower(): #lower.() is used to make the input case insensitive
    print("Correct! Congratulations!",answer,"is the right answer") #If the answer is correct it shows this message
else:
    print("Wrong! The answer is",answer) #if the answer is wrong this message will be shown

#Advanced Requirements
print("Capitals of European Countries Quiz!")
score=0 #it is used to check how many questions the user has answered correctly
print("Question 1")
question1=input("What is the Capital of Germany?")
answer1="Berlin"

if question1.lower()==answer1.lower():
    print("Correct!",answer1,"is the right answer!")
    score += 1 #If the answer is correct user gets 1 point
else:
    print("Wrong answer! The correct answer is",answer1)

print("Question 2")
question2=input("What is the capital of Spain?")
answer2="Madrid"

if question2.lower()==answer2.lower():
    print("Correct!",answer2,"is the right answer!")
    score += 1
else:
    print("Wrong answer! The correct answer is",answer2)

print("Question 3")
question3=input("What is the capital of Norway?")
answer3="Oslo"

if question3.lower()==answer3.lower():
    print("Correct!",answer3,"is the right answer!")
    score += 1
else:
    print("Wrong answer! The correct answer is",answer3)

print("Question 4")
question4=input("What is the capital of Finland?")
answer4="Helsinki"

if question4.lower()==answer4.lower():
    print("Correct!",answer4,"is the right answer!")
    score += 1
else:
    print("Wrong answer! The correct answer is",answer4)

print("Question 5")
question5=input("What is the capital of Denmark?")
answer5="Coppenhagen"

if question5.lower()==answer5.lower():
    print("Correct!",answer5,"is the right answer!")
    score += 1
else:
    print("Wrong answer! The correct answer is",answer5)

print("Question 6")
question6=input("What is the capital of Portugal?")
answer6="Lisbon"

if question6.lower()==answer6.lower():
    print("Correct!",answer6,"is the right answer!")
    score += 1
else:
    print("Wrong answer! The correct answer is",answer6)

print("Question 7")
question7=input("What is the capital of Poland?")
answer7="Warsaw"

if question7.lower()==answer7.lower():
    print("Correct!",answer7,"is the right answer!")
    score += 1
else:
    print("Wrong answer! The correct answer is",answer7)

print("Question 8")
question8=input("What is the capital of Sweden?")
answer8="Stockholm"

if question8.lower()==answer8.lower():
    print("Correct!",answer8,"is the right answer!")
    score += 1
else:
    print("Wrong answer! The correct answer is",answer8)

print("Question 9")
question9=input("What is the capital of Slovakia?")
answer9="Bratislava"

if question9.lower()==answer9.lower():
    print("Correct!",answer9,"is the right answer!")
    score += 1
else:
    print("Wrong answer! The correct answer is",answer9)

print("Question 10")
question10=input("What is the capital of Ukraine?")
answer10="Kyiv"

if question10.lower()==answer10.lower():
    print("Correct!",answer10,"is the right answer!")
    score += 1
else:
    print("Wrong answer! The correct answer is",answer10)

if score >= 6: #the pass mark for this quiz is 6 or above
    print("Congratulations! You have passed the quiz. Your total score is",score,"out of 10 questions.") #if they got 6 or more they have passed the test
else:
    print("Oh no! You have not passed the quiz, better luck next time. Your total score is",score,"out of 10 questions.") #if not, they have failed the test and need to do better next time