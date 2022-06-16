store_file = open("store.txt", "r") # open and read (r) the file
# open("store.txt", "w") is open and write/change the file
# open("store.txt", "a") is open and appending to the file
# open("store.txt", "r+") is open, read, and write

print(store_file.readable()) # True
# print(store_file.read())
# print("------------")
# print(store_file.readlines()[1])

for employee in store_file.readlines():
    print(employee)



store_file.close()
