print("--Operations on List using built-in functions--")

my_list = []
# list of integers
my_list = [1, 2, 3]
# list with mixed data types
my_list = [1, "Hello", 3.4]
print(my_list)
# nested list
my_list = ["mouse", [8, 4, 6], ['a']]


my_list = ['p', 'r', 'o', 'b', 'e']
print(my_list[0])
print(my_list[2])
print(my_list[4])

# Nested List
n_list = ["Happy", [2, 0, 1, 5]]

# Nested indexing
print(n_list[0][0])
print(n_list[1][2])

#negative indexing
my_list = ['p','r','o','b','e']
print(my_list[-1])#negative indexing
print(my_list[-5])


# List slicing in Python
print("List Slicing: ")
my_list = ['p','r','o','g','r','a','m','i','z']
# elements 3rd to 5th
print(my_list[2:5])
# elements beginning to 4th
print(my_list[:-5])
# elements 6th to end
print(my_list[5:])
# elements beginning to end
print(my_list[:])


# add or update the element in list
odd = [2, 4, 6, 8]
# change the 1st item
odd[0] = 1
print(odd)
# change 2nd to 4th items
odd[1:4] = [3, 5, 7]
print(odd)

print("Appending and Extending lists: ")
# Appending and Extending lists in Python
odd = [1, 3, 5]
odd.append(7)
print(odd)
odd.extend([9, 11, 13])
print(odd)

# Concatenating and repeating lists
odd = [1, 3, 5]
print(odd + [9, 7, 5])#Concatenating  lists
print(odd * 3)# repeating lists


print("Insert elements in list: ")
# Demonstration of list insert() method
odd = [1, 9]
odd.insert(1,3)
print(odd)
odd[2:2] = [5, 7]
print(odd)

print("Delete elements from list:")
# Deleting list items
my_list = ['p', 'r', 'o', 'b', 'l', 'e', 'm']
del my_list[2]# delete one item
print(my_list)
del my_list[1:5]# delete multiple items
print(my_list)
del my_list# delete entire list
#print(my_list)# Error: List not defined

print("Remove elements from list: ")
#Remove list
my_list = ['p','r','o','b','l','e','m']
my_list.remove('p')
# Output: ['r', 'o', 'b', 'l', 'e', 'm']
print(my_list)
# Output: 'o'
print(my_list.pop(1))
# Output: ['r', 'b', 'l', 'e', 'm']
print(my_list)
# Output: 'm'
print(my_list.pop())
# Output: ['r', 'b', 'l', 'e']
print(my_list)
my_list.clear()
# Output: []
print(my_list)

# Python list methods
my_list = [3, 8, 1, 6, 0, 8, 4]
print(my_list.index(8)) # Using index method
print(my_list.count(8))  # Count method
my_list.sort() #sort method
print(my_list)
my_list.reverse()#reverse method
print(my_list)
