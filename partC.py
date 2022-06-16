# functions
def sayHi(name):
    print("Hi " + name)
sayHi("Becca")

def cube(num):
    return pow(num, 3)
print(cube(2))

# if statements
guess = 10
if guess != 0 and guess < 10:
    print("Lower than 10")
elif guess != 0 and guess > 10:
    print("Higher than 10")
else:
    print("10")

# while loops
# for-loops
for letter in "Rebecca":
    print(letter)

friends = ["Abby", "Becca", "Cassie"]
for friend in friends:
    print(friend)
for i in range(len(friends)):
    print(friends[i])

for i in range(10):
    print(i) # 0-9

for i in range(3,10):
    print(i) # 3-9

# 2D Lists and Nested Loops
number_grid = [
    [1,2,3],
    [4,5,6],
    [7,8,9],
    [0]
]

print(number_grid[0][1]) # row, column

for row in number_grid:
    for col in row:
        print(col)

