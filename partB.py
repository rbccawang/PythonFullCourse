# lists
friends = ["Abby", "Becca", 2]
print(friends[1]) # Becca
print(friends[-1]) # 2
print(friends[-3]) # Abby
print(friends[1:2]) # Becca

friends[0] = "Abigail"
print(friends)

# list functions
authors = ["Fitz", "Fitz", "Gerald"]
''' authors.sort()
print(authors)
authors.reverse()
print(authors) '''

friends.extend(authors)
print(friends)
friends.append("Alicia")
friends.insert(0, "Abby")
friends.remove("Abigail")
print(friends) # ['Abby', 'Becca', 2, 'Fitz', 'Gerald', 'Alicia']
friends.pop() # removes last element
print(friends) # ['Abby', 'Becca', 2, 'Fitz', 'Gerald']
print(friends.index("Becca"))
print(friends.count("Fitz")) # 2 occurances

friends2 = friends.copy()
print(friends2)

friends.clear() # empty list
print(friends)

# tuples
immutable = (1,2)
print(immutable[1])

# list of tuples
coordinates = [(1,2), (3,4), (5,6)]
print(coordinates[2])

# dictionaries (key-value pairs)
monthConversions = {
    "Jan" : 1,
    "Feb" : "February",
    "Mar" : 3
}
print(monthConversions["Jan"]) # prints the key, 1
print(monthConversions.get("Mar")) # prints the key, 3
print(monthConversions.get("Dec", "Not a valid key"))