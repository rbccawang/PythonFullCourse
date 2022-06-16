from math import *

# variables
name = "Mimi"
age = 10
print("There once was a bear named " + name)
print(f"She was {age} years old.")

# strings
print("Rebecca\nWang")
print("Rebecca\"Wang")
print("Rebecca\Wang")

phrase = "Rebecca Wang"
print(phrase.lower())
print(phrase.upper())
print(phrase.upper().isupper())
print(len(phrase)) # 12 (counts spaces/chars)
print(phrase[1]) # e
print(phrase.index("Reb")) # 0
print(phrase.replace("Reb", "Mim"))

# integers and doubles
print(-2 + 1) # -1
modR = 10 % 3
print(modR)
print(str(modR) + " is the remainder.")

mNum = -10
print(abs(mNum))
print(pow(2, 4)) # 2 to the power of 4; 16
print(max(2,4))
print(min(2,4))
print(round(3.5)) # 4, unlike Java
print(floor(3.7)) # 3 like Java
print(ceil(3.2)) # 4, always rounds the number up
print(sqrt(25)) # 5.0

# user input
name2 = input("Enter your name: ")
age2 = input("Enter your age: ")
print("Hello " + name2 + f". You are {age2} years old.")


