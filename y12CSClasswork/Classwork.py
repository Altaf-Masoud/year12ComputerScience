# displays full name using variables
# firstname = ("Altaf")
# lastname = ("Masoud")

# print(firstname, lastname)

# pi = (3.141592653)

# a = 5
# b = 10
# c = a+b
# print(c)

'''Casting to String
⭐

Challenge: 
Write a program to demonstrate casting an integer to a string data type
 
e.g cast 42 into a string and output the result
 
use str( )'''


# # displays name in terminal
# print ("Altaf")
# # displays saying in terminal
# print("Hello world")
# # displays age in terminal
# print("The number 16")
# # displays the sum in terminal
# print(0+4)
# # displays difference in terminal
# print(2-1)
# # displays multiplication result in terminal
# print(9*8)
# # displays division result in terminal
# print(4/2)
# # displays DIV in terminal. DIV is interger division
# print(9//2)
# # displays MOD in terminal. Modulus is the remainder
# print(9%2) 
# # displays the root of the number in terminal
# print(2**6)
# # simple bidmas
# print( 5+2*(10-5)+2 )

# print ("This is a Pounds to Kilogram converter")
# pounds = float(input("Enter your weight in pounds... "))
# kg = round(pounds / 2.205, 2)
# print(kg, "kg")

# print ("This is a Kilograms to Pounds converter")
# kilograms = float(input("Enter your weight in Kilograms... "))
# lbs = round(kilograms * 2.205, 2)
# print(lbs, "lbs")

# num = str(42)
# print(num)
# print("6"==str(6))

# number = int(input("Enter a three digit number... "))
# print("The number you have entered is...", number)
# hundreds = number // 100
# tens = number // 10 % 10
# units = number % 10

# print("Hundreds Column =", hundreds, "\nTens Column =", tens, "\nUnits Column =", units)

'''
 Positive Integer Checker

 Take a number as input from the user 
 
 and print whether it's a positive integer or not.

 Maintainable Code: Nested If Statement Indentation
⭐⭐⭐⭐

Challenge: 
Write a program that asks for a number and prints "Positive" if the number is greater than zero, "Negative" if the number is less than zero, and "Zero" if the number is zero. Use nested if statements with correct indentation.
 
 number = int(input("Enter a number: "))if number > 0:print("Positive")else:if number < 0:print("Negative")else:print("Zero") '''

# number = int(input("Type in a number: "))

# if number>0:
#     print("Your number is positive.")
# elif number==0:
#     print("Your number is neither positive nor negative and is 0")
# else:
#     print("Your number is negative.")


''' Even and odd checker'''

# num = int(input("Type in a integer: "))

# if num%2==0:
#     print("Your number is even")
# else:
#     print("Your number is odd")

'''Comments: Inline - Boolean Operators and Assignment
⭐⭐⭐⭐

Challenge: 
convert this code to python
 
 add inline comments to explain what is happening
 
 x = True
 y = False
 z = x AND y
 output(z)'''

# x = True
# y = False
# z = x and y
# print(z)

# x = True
# y = False
# z = x , y
# print(z)



''''''
# number = int(input("Type in a number: "))

# if number>0 and number%2==0:
#     print("Your number is positive and even.")
# elif number<0 and number%2!=0:
#     print("Your number is negative and odd")
# elif number>0 and number%2!=0:
#     print("Your number is positive and odd.")
# else:
#     print("Your number is negative and even")

'''Maintainable Code: Comments: Inline - combination of concepts
⭐⭐⭐

Challenge: 
convert this code to python
 
 add inline comments to explain what is happening
 a = 5
 b = 3
 if a > b
  c = a - b
 else
  c = b - a
 output ( c )'''

# a = 5
# b = 10
# if a>b:
#     c = a - b
# else:
#     d = b - a
# print(c)

'''Maintainable Code: Comments: Inline - Nested If Statements
⭐⭐⭐⭐

Challenge: 
convert this code to python
 
 add inline comments to explain what is happening
 number = input()
 if number > 0
  if number % 2 == 0
  output("Positive even")
  else
  output("Positive odd")
 else
  output("Non-positive")'''

# number = int(input("Enter a number... "))
# if number>0:
#     if number%2 == 0:
#         print("Your numnber is positive even")
#     else:
#         print("Your numnber is positive odd")
# elif number<0:
#     if number%2 == 0:
#         print("Your number is negative and even.")
#     else:
#         print("Your number is negative and odd.")
# else:
#     print("Your numnber is Zero")

'''Positive Integer Checker'''

# number = int(input("Enter a number... "))
# if number>0:
#   print("Positive Number")
# else:
#   print("non-positive")

'''Positive or Negative Number
⭐⭐

Challenge: 
Take a number as input from the user and print whether it's positive, negative, or zero.'''

# number = int(input("Enter a number... "))
# if number>0:
#   print("Positive Number")
# elif number<0:
#   print("Negative Number")
# else:
#   print("Number = Zero")

'''Passing Marks
⭐⭐

Challenge: 
Take a student's score as input from the user and print whether they passed or failed (passing score is 50).'''

# score = int(input("Please enter your score... "))

# if score>50:
#     print("You have passed.")
# else:
#     print("You have failed.")

'''Greater Number
⭐⭐

Challenge: 
Take two numbers as input from the user and print which one is greater.'''

# num1 = int(input("Please enter your first number... "))
# num2 = int(input("Please enter your second number... "))

# if num1>num2:
#     print("First number entered is larger than the second number.")
# elif num1<num2:
#     print("Second number entered is larger than the first number.")
# else:
#     print("Your numbers are equal")

''''''
# evenNumberCheck = int(input("Please enter an even number to win the game: ")) # set condition

# while ((evenNumberCheck % 2) != 0) : # check the condition
#     print("You Lose, Odd Number") # actions
#     evenNumberCheck = int(input("Enter an even Number: ")) # reset the condition
    

# print("Well done you win")
# continues in sequence

'''Countdown: Condition Controlled
⭐⭐⭐

Challenge: 
Write a program that prints numbers from 10 to 1 in reverse order.'''


# countdown = 10

# while countdown>=0:
#     print(countdown)
#     countdown = countdown-1

'''Comments: Inline - Loop with Nested Conditional
⭐⭐⭐⭐

Challenge: 
convert this code to python
 
 add inline comments to explain what is happening
 for i = 1 to 5
  if i % 2 == 0
  output(i + " is even")
  else
  output(i + " is odd")'''

# num = 0
' code made whilst using while instead of for'
# while 100>=num:
#   if num%2==0 and num!=0:
#     print("The number ", num, "is even")
#   elif num==0:
#     print("0 is neither even nor odd")
#   else:
#     print("The number ", num, "is odd")
#   num = num+1

'''Multiplication Table: Condition Controlled
⭐⭐⭐

Challenge: 
Create a program that takes an input number and prints its multiplication table up to 10.'''

# num = int(input("Enter any number"))
# multiplier = 0

# while (10*num)>= num*multiplier:
#   print(num*multiplier)
#   multiplier = multiplier + 1

'''Even Numbers: Condition Controlled
⭐⭐⭐

Challenge: 
Print all even numbers between 1 and 20.'''

# num = 0

# while 20>=num:
#   if num%2==0 and num!=0:
#     print(num, "is an even number.")
#   elif num==0:
#     print("Your number is", 0)
#   else:
#     print(num, "is an odd number")
#   num = num + 1

'''For Statements'''

'''Comments: Inline - Loop with Nested Conditional
⭐⭐⭐⭐

Challenge: 
convert this code to python
 
 add inline comments to explain what is happening
 for i = 1 to 5
  if i % 2 == 0
  output(i + " is even")
  else
  output(i + " is odd")'''



# for i in range(1, 5):
#   if i % 2 == 0:
#     print(i, "is even")
#   else:
#     print(i, "is odd")

'''Maintainable Code: Count Controlled Indentation
⭐⭐⭐⭐

Challenge: 
Write a program that asks for a number and prints all numbers from 0 to that number (inclusive). Ensure the loop body is correctly indented.
 
 number = int(input("Enter a number: "))for i in range(number + 1):print(i)'''
 
# number = int(input("Enter a number: "))

# for i in range(number + 1):
#   print(i)

'''Print Numbers: Count Controlled
⭐⭐⭐

Challenge: 
Print the numbers from 1 to 10.'''

# for i in range(1,):
#   print(i)

# Write pseudocode for a program that prompts a user to enter their name. If the name is “Hazel” then output “Hello Hazel”.
# If the name is not Hazel, output “We haven’t met, ” name, “ pleased to meet you.” 					[4]

'''name = str(input("Please enter your name: ")) Question 1

if name == ("Hazel"):
  print("Hello Hazel")
else:
  print("We haven’t met",  name,  "pleased to meet you.")'''

# Complete the following pseudocode for a program that prompts the user to input a temperature reading and humidity reading. 
# If the temperature is greater than 25 or humidity is greater than 50% and window is closed, then output a message “Open the window”. 
# If the temperature is below 10, the humidity is below 50% and the window is not closed, output a message “Close the window”.

# 		temp = input(“Enter the temperature”)
# 		humidity = input(“Enter the humidity”)
# 		if window == “closed” then
# 		(add statements here)		

'''temp = int(input("Enter the temperature: "))
humidity = int(input("Enter the humidity: "))

if temp>25 and humidity>50:
  print("Please open your window if it is not already open.")
elif temp<10 and humidity<50:
  print("Please close your window if not already close.")'''

  
# A pseudocode program that measures pH levels is shown below. The pH scale runs from 0 to 14. 
# Read the code below and complete the trace tables with the values given.

# pH = 0
# pH = int(input("Enter pH level: "))
# if pH>0 and pH<7:
# 	print("pH is acidic")
# elif pH == 7:
# 	print("pH is neutral")
# elif pH>7 and pH <=14:
# 	print("pH is alkaline")
# else:
# 	print("Error... enter a number from 1 to 14")

num1 = int(input("Please enter your first number: "))
num2 = int(input("Please eneter your second number: "))
operation = str(input("Select one of the following options: \n Enter A for Multiplication: \n Enter B for Division:  \n Enter C for Addition: \n Enter D for Subtraction: \n Enter E for Remainder Division: \n "))

if operation == ("A"):
  print("The result of multiplication between both numbers is... ", num1 * num2)
elif operation == ("B"):
  print("The result of division between both numbers is... ", num1 / num2)
elif operation == ("C"):
  print("The sum of both numbers is... ", num1 + num2)
elif operation == ("D"):
  print("The difference between both numbers is... ", num1 - num2)
elif operation == ("E"):
  print("The result of remainder division between both numbers is... ", num1 % num2)
else:
  print("Error... You haven't chosen any of the suitable options. Please restart and try again.")