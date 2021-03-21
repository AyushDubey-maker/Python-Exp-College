print ("---------------COMMENTS-----------------")
print ('Single Line "#"')
print ('Multi Line ("""---""")')
print ("Multi Line ('''---''')")
print ("")

print ("--Datatypes,Expressions,Output Statement & Conversions-")
a=16 #int datatype
a1="abc" #string datatype
b=23.32 #Float datatype
c=2.3+3.2j #Complex datatype
d=1.2-2.8j #Complex datatype
e=c+d #expression
e1=a*b #expression
e2=a**3
print("Exponential is",e2)#exponential
print ("Sum is",e )#Output statement
print ('Multiplication is ', e1) #Output statement

f=float(a) #Converting int to float
print ('Int to Float', f)
g=complex(b) #Converting float to complex
print ('Float to Complex', g)
h=oct(a) #Decimal to octal
print ('Decimal to Octal', h)
i=bin(a) #Decimal to binary
print ('Decimal to Binary', i)
j=hex(a) #Decimal to hexadecimal
print ('Decimal to Hexadecimal',j)
print ("")

print ("------INPUT STATEMENT---------")
k=input('What is your name? using raw input ') #ask & returns string of data
print ('Your name is ' + k)
l=input('Enter value of x ')
print ('Entered value of x using String Function is ' + str(l)) #Printing Output in String Format
print ('Entered value of x using format function is {0}'.format(l)) #Printing Formatted Output
print ("accept integer input",int(input())) #Accept Integer Input
print ("")

print ("-------Knowing the datatype------")
a=12
print (type(a))
b="str"
print (type(b))
c=1.2+4j
print (type(c))

print("----Identity operator---")
x=5
y=6
print(type(x) is type(y))
print(type(x) is not type(y))

print("---membership operator---")
print("Hi" in "Hello World" )
print ("Hi" not in "Hello world")

print("---Logical operator---")
x=True
y=False
print('x and y is',x and y)
print('x or y is',x or y)
print('not x is',not x)

print("---Bitwise Operator---")
x=10
y= 4
print("x &y",x&y)
print("x | y",x|y)
print("~x",~x)
print("x^y",x^y)
print("Right shift",x>>2)
print("Left shift ",x<<2)
