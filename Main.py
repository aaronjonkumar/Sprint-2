__author__ = "Aaron J. Kumar"
# COP 1500
# Integration Project
"""My project will consist of a combination of all my programming exercises"""
print("Welcome to my project!")
# This is called a string literal
print("This is a big combination of all my programming exercises")
age = input("How old are you? ")
print("You are", age + " years old.")
# "age" is a variable that was created to store data entered by the user
twenty = 20
num1 = int(age)
num2 = int(twenty)
# I converted the variables into integers
addition = num1 + num2
print("In 20 years, you will be", addition, "years old")
# I then created an equation to add 20 to whatever was inputted
print("I am now going to add 2+2, subtract 2-2, multiply 2*2, and divide 2/2")
yes = input("Click enter when you are ready to proceed ")
print(2 + 2)
print(2 - 2)
print(2 * 2)
print(2 // 2)
print("I will now find the remainder in 7/3")
print(7 % 3)
print("I will now calculate 5 to the 2nd power")
print(5 ** 2)
# This is how you can output different math equations
# I am now going output a phrase several times
phrase = "Welcome to my project! " * 4
print(phrase)
# Next, I will create a code below to find out your textbooks cost
num_textbooks = input("How many textbooks do you need? ")
textbooks_cost = input("How much do they cost? ")
num3 = int(num_textbooks)
num4 = int(textbooks_cost)
total_cost = num3 * num4
print("Your textbooks will cost: $", format(total_cost, '.2f'))
# Above, that is where we learned how to format the display of variables
a = 10
b = 20
c = 30
# I will now create boolean expressions from the variables above
print("a=10, b=20, c=30")
print("a < b")
print(a < b)
print("c < a")
print(c < a)
# I will now use logical operators in this expression
print("Is a < b and b < c?")
print((a < b) and (b < c))
randomNumber = input("Click any button to generate random number up to 1000: ")
import random
# Importing random will allow for you to computer generate a number
# RNG (Random number generator)

print(random.randint(1, 1000))
# IF statements are used to do something based of a condition
tired = input("Are you tired? Type Yes or No: ")
if tired == 'Yes':
    print("You are tired, get some rest. ")
elif tired == 'No':
    print("Great!")
year = int(input("How old are you? "))
if year >= 65:
    print("According to the CDC, you are at an increased risk for COVID 19.")
# else statements are for everything the if statement is not
else:
    print("You are not at an increased risk for COVID 19.")
# This is a if-elif statement below
day = input("What day of the week is it: ")
if day == 'Friday' or "Saturday":
    print("Have a good weekend! ")
elif day != 'Friday' or "Saturday":
    print("Sorry to hear that. ")
number = int(input("Enter a number between -5 and 5 "))
if number > 0:
    print("You have entered a positive number")
elif number == 0:
    print("You have entered zero")
else:
    print("You have entered a negative number")
# This was a if-elif-else statement above
# They are used to set certain conditions onto something
total = 0
# for loops can have something loop until a condition has been met
for x in range(4):
    num4 = int(input("Enter a number: "))
    total += num4
# In this for loop it is adding all the numbers together
print("The total is:", total)
# The variable 'total' is an accumulator
name = input("Enter your name and it will print your name based off age ")
x = 0
while x < num1:
    print(name)
    x += 1
# With this while loop it prints you name 10 times if your 10 etc etc
cars = ['Toyota', 'Volkswagen', 'Chevrolet', 'Ford', 'BMW', 'Audi', 'Lexus']
print(cars)
# This is how I print a list
print("The best car manufacturer in this list is", cars[2])


# In the above print statement you can take just one part of a list to print
# This is where I created a function
def addIntegers(num5, num6):
    """This function adds two number together.

    :param num5:
    :param num6:
    """
    # addIntegers has parameters in the parentheses
    print(num5, "+", num6, "=", num5 + num6)


# I defined the function 'addIntegers' above
def main():
    """ This is the main function.

    """
    first_num = int(input("Enter a positive number: "))
    second_num = int(input("Enter another positive number: "))
    addIntegers(first_num, second_num)


# The line above is the function I defined earlier
# Have to call to main below
main()
# This program will calculate the percentage of credits earned
credit = int(input("Enter how many credits you have earned: "))
percentage = credit / 120
percentage *= 100
print("You have earned", percentage, '%', 'of the 120 credits needed.')
print("Enter 3 numbers below to find the largest number")
# Not the best variable names but they work
num10 = float(input("Enter number: "))
num11 = float(input("Enter number: "))
num12 = float(input("Enter number: "))
if (num10 >= num11) and (num10 >= num12):
    large = num10
elif (num11 >= num10) and (num11 >= num12):
    large = num11
else:
    large = num12
print("The largest number is", large)
# Above, I used a simple if, elif, else statement

print("This is the end of my integration project.")
print("This is an accumulation of everything I learned in COP 1500.")
print("Thank you for using my program.")
print("Have a great rest of your day!")
