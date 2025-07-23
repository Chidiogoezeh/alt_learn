
friends = ["Kelechi", "Jide", "Mark", "Hunk", "Yale"] # Square brackets in python indicate objects or values stored in python lists. lists can contain strings, numbers, and boolean concurrently or separately

#How do you access the values inside the list? Counting index from the front starts with 0 to 1, while counting from the back starts with -1 to wards the first index
print(friends)
print(friends[-2])  # Any value can be accessed through it's index, either from the front or negatives from the back
print(friends[1:]) # To select values from a specific portion of the list use 1 colon:, it grabs values from the index and everything after
print(friends[2:4]) #Select values from specific index positions
friends[1] = "Tate" # Modify the list. this changes the second index value to Tate
