"""Intro to Python - Part 1 - Hands-On Exercise."""


import math
import random


# TODO: Write a print statement that displays both the type and value of `pi`
pi = math.pi
print ("pi is a {} and has a value of {}".format(type(pi), pi))



# TODO: Write a conditional to print out if `i` is less than or greater than 50
i = random.randint(0, 100)
if i <50:
    print("i is less than 50")
elif i == 50:
    print ("i is equal to 50")
elif i > 50:
    print("i is greater than 50")


# TODO: Write a conditional that prints the color of the picked fruit
picked_fruit = random.choice(['orange', 'strawberry', 'banana'])
if picked_fruit == 'orange':
    print("The fruit is orange")
elif picked_fruit == 'strawberry':
    print("The fruit is red")
elif picked_fruit == 'banana':
    print("The fruit is yellow")


# TODO: Write a function that multiplies two numbers and returns the result
# Define the function here.
def multiply(num1, num2):
    result = num1 * num2
    return result


# TODO: Now call the function a few times to calculate the following answers

print ("22 x 44 =", multiply(22, 44))

print ("58 x 99 =", multiply(58, 99))

print ("252525 x 232323 =", multiply(252525, 232323))
