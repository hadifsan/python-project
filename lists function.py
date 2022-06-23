
lucky_numbers = [4, 8, 15, 16, 23, 42]
friends = ["Syafiq", "Sued", "Ujin", "lin", "lin"]
#friends.extend(lucky_numbers) # extend the lists, combine the lists
friends.append("Creed") # add another item to the lists
friends.insert(1, "mao") # insert another item to the location number specified
#friends.remove("lin") # remove item from the lists
#friends.clear() # get rid of everything
friends.pop() # remove the last element of the lists
lucky_numbers.sort() # susun in ascending order
#lucky_numbers.reverse() # descending order
friends2 = friends.copy() # copy the lists from friends var

print(friends)
print(friends.index("Syafiq")) # to figure out the position of the specific element is inside of the lists
print(friends.count("Ujin")) # tell how many time the specific element show up inside of the lists
print(lucky_numbers)
print(friends2)


