print("-----------String--------------")
str="Welcome to python"
print("String:",str)
print("Extract letter",str[2])
print("Extract last character ",str[-1])
 
print("Return range of charater",str[3:7])
print("Return all characters from indes 5",str[5:])
print('Retiurn all characters before index 6',str[:6])
 
print("Replace python with java",str.replace('python','java'))
print("In operator Checkin",'Wel'in str)
print("Not in Operator checking",'N' not in str)
 
print("To capitalize first charater",str.capitalize())
print("To convert all string to lowercase",str.lower())
print("To convert all string to uppercase",str.upper())
 
str1='o'
print("To count the occurence of letter o in str",str.count(str1))
 
print("To return the substring using split()",str.split())
print("To return the substring using split() till some limit",str.split(' ',1))
 
seq=('ab','bc','cd')
print("The string obtained by using join()",str.join(seq))
print("Length of String",len(str))

