# Using functions with lists in python. In python, lists is essnetial in storing information
lucky_numbers = [1, 4, 9, 16, 25, 36, 49]
friends = ["Kelechi", "Jide", "Mark","Jide", "Hunk", "Yale"]

print(friends.index("Mark")) # To determine whether a specific value is present in a list

print(friends.count("Jide")) # Count method is used to know how many times a value/element appear in a list

friends2 = friends.copy() # used to copy an exact replica of a list

friends.sort() # used to sort list in ascending order i.e alphabetical order

friends.reverse() #used to reverse the sequence of the values in the list

friends.extend(lucky_numbers) # Extend function allows to take a list and append another list to it

friends.append("Ural") # append is used to add individual values to the end of a list

friends.insert(2, "Tubu") # insert takes 2 parameters which are the index you want the value and secon is the value you want to add

friends.remove("Hunk") # remove is used a specific value from the list

friends.pop() # pop gets rid of the last element/value in a list

friends.clear() # clear is used to clean up a list giving an empty list

print(friends)