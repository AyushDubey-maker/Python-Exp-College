print("--Operations on Tuple using built-in functions--")
my_tuple = ()#Empty Tuple
print(my_tuple)


my_tuple = (1, 2, 3)# Tuple having integers
print(my_tuple)


my_tuple = (1, "Hello", 3.4)# tuple with mixed datatypes
print(my_tuple)


my_tuple = ("mouse", [8, 4, 6], (1, 2, 3))# nested tuple
print(my_tuple)

print("Accessing tuple elements using indexing")
# Accessing tuple elements using indexing
my_tuple = ('p','e','r','m','i','t')

print(my_tuple[0])   # 'p' 
print(my_tuple[5])   # 't'


# nested tuple
n_tuple = ("mouse", [8, 4, 6], (1, 2, 3))

# nested index
print(n_tuple[0][3])       # 's'
print(n_tuple[1][1])       # 4

# Negative indexing for accessing tuple elements
my_tuple = ('p', 'e', 'r', 'm', 'i', 't')

# Output: 't'
print(my_tuple[-1])

print("Accessing tuple elements using slicing")
# Accessing tuple elements using slicing
my_tuple = ('p','r','o','g','r','a','m','i','z')
print(my_tuple[1:4])# elements 2nd to 4th
print(my_tuple[:-7])# elements beginning to 2nd
print(my_tuple[7:])# elements 8th to end
print(my_tuple[:]) #elements beginning to end

print((1, 2, 3) + (4, 5, 6))# Concatenation
print(("Repeat",) * 3)# Repeat

del my_tuple
#print(my_tuple)

my_tuple = ('a', 'p', 'p', 'l', 'e',)
print(my_tuple.count('p'))  # Output: 2
print(my_tuple.index('l'))  # Output: 3

# Membership test in tuple
my_tuple = ('a', 'p', 'p', 'l', 'e',)

# In operation
print('a' in my_tuple)
print('b' in my_tuple)

# Not in operation
print('g' not in my_tuple)
