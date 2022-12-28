letters = ["a","b","c"]

# Add
letters.append("d") #Insert at the end of the list
letters.insert(0,"-") #Insert at specific index
print(letters)

# Remove
letters.pop(0) #Remove at certain index
letters.remove("b") #Remove FIRST OCCURANCE
del letters[0:3] #Remove by range
letters.clear() #Clears the list
print(letters)