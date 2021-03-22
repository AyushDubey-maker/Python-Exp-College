1.print ("--Finding MAX BETWEEN 3 Nos using IF-Else-Elif STATEMENT--")
a=input("Enter value of First element:")
b=input("Enter value of Second element:")
c=input("Enter value of Third element:")
if a>b and a>c:
    print (a,"is Greater")
elif b>c:
    print (b,"is Greater")
else:
    print (c,"is Greater")
print ("")

2.print ("-----Calculate Factorial using WHILE LOOP-----------")
num=int(input("Enter the number : "))
fact=1
i=1
while i <= num:
    fact=fact*i
    i=i+1
print("Factorial of",num," is :",fact)

3.print ("--Multiplication table using FOR loop--")
n=int(input("Enter the number:"))
for i in range(1,11):
    print (n,"X",i,"=",n*i)
print ("")
