print("Function with no parameter")
def show():
          print("Welcome to SLRTCE College ")
show()

print("Function with parameter without return type")
def  sum(a,b):
          print("Addition of {0} and {1} is {2}".format(a,b,a+b))
x=int(input("Enter value of a : "))
y=int(input("Enter value of b : "))
sum(x,y)
  
print("Function with parameter with return type")
def  sub(a,b):
          return a-b
x=int(input("Enter value of a : "))
y=int(input("Enter value of b : "))
print("Substraction is",sub(x,y))





lam_fun=lambda x,y:x+y # making use of in bulit lambda function
print("output using lambda",lam_fun(2,3))

li = [5, 7, 22, 97, 54, 62, 77, 23, 73, 61] #making use of filter function
final_list = list(filter(lambda x: (x%2 != 0) , li)) 
print(final_list)

li = [5, 7, 22, 97, 54, 62, 77, 23, 73, 61] #making use of map function
final_list = list(map(lambda x: x*2, li)) 
print(final_list) 

from functools import reduce # making use of reduce() function
li = [5, 8, 10, 20, 50, 100] 
sum = reduce((lambda x, y: x + y), li) 
print (sum) 

import functools  
lis = [ 1 , 3, 5, 6, 2, ] # initializing list
print ("The maximum element of the list is : ",end="") # using reduce to compute maximum element from list   
print (functools.reduce(lambda a,b : a if a > b else b,lis)) 
