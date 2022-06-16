from partG import partG

store_file = open("store.txt", "a")
store_file.write("\nMark - HR")
store_file.close()

store2_file = open("store2.txt", "w") # creates a new file
store2_file.write("\nMark - HR")
store2_file.close()

student1 = partG("A", "Math", 3.0, False)
print(student1.name)