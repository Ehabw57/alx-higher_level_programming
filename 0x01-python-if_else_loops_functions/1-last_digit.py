#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
print(f"Last digit of {number} is", end="")
if number < 0:
    Lastdig = -number % 10
    Lastdig *= -1
else:
    Lastdig = number % 10
print(f" {Lastdig}", end="")
if Lastdig > 5:
    print(f" and is greater than 5", end="")
if Lastdig == 0:
    print(f" and is 0", end="")
if Lastdig < 6 and Lastdig != 0:
    print(" and is less than 6 and not 0", end="")
print("")
