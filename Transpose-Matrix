 
R = int(input("Enter the number of rows:"))
C = int(input("Enter the number of columns:"))
  
# Initialize matrix
matrix = []
print("Enter the entries row-wise:")
  
# For user input
for i in range(R):          # a for loop for row entries
    a =[]
    for j in range(C):      # a for loop for column entries
         a.append(int(input()))
    matrix.append(a)
  
# # For printing the matrix
# for i in range(R):
#     for j in range(C):
#         print(matrix[i][j], end = " ")
#     print()


result = [[0,0],
     [0,0]]

# iterate through rows
for i in range(len(matrix)):
   # iterate through columns
   for j in range(len(matrix[0])):
       result[j][i] = matrix[i][j]

for r in result:
   print(r)
