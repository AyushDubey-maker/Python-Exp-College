print("--------------Array using Numpy-------------------")
import numpy as np
a=np.array([1,2,3]) #single dimensional array
print(a)

b=np.array([(1,2,3),(4,5,6)]) #Multidimensional array
print(b)
print("Access 2nd element of 1st dim:",b[0,2])
print(b.ndim)#find the dimension of the array whether two or three dimensional

print("Array is of type",type(b))
print("Array stores element of type:",b.dtype)
print("size of array:",b.size)#printing size(total number of elements) of array

c=np.array([[1,2,3],[4,5,6],[7,8,9]])
print("before transpose:",end=" ")
print(c)
print("after transpose",c.transpose())#to form a transpose of array

arr=np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])#Accessing 3 di array element
print(arr[0,1,2])


d=np.full((3,3),6,dtype='complex')#Create a constant value array of complex type
print("An array intializes with all 6:",d)

e=np.zeros((3,4))#Creating a 3X4 array with all zeros
print("An array intizlized with all zero:",e)

f=np.arange(0,30,5)#Create a sequence of integers from 0 to 30 with steps of 5
print("A sequential array with step of 5:",f)

A = np.array([[2, 4], [5, -6]])
B = np.array([[9, -3], [3, 6]])
C = A + B      # element wise addition
print("Addition of matrix",C)

D=A.dot(B)
print("Multiplication of matrix:",D)

print("Access 2nd column of the matriox",A[:,1])
print("Accessn last colum of the matrix",A[:,-1])

