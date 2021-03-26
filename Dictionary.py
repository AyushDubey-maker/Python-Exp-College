print("-----------Dictionary---------------")
a={"Name":"Abcdef","age":18,"address":"kalyan"}
print("Dictionary a",a)
print("Keys of Dictionary a",a.keys())
print("Values of Dictionary a",a.values())
print("Items of Dictionary a",a.items())
 
print("Length of a",len(a))
print("a[name]", a['Name'])
print("Get age ", a.get('age'))
 
a['tel']=322233
print("Adding tel",a)
c=a.clear()
print("Clearing a :",a)
 
 
a={'name':'bj','age':23,'contact':666555,'gender':'male'}
b={'name':'bj','age':23,'contact':666555,'ge':'male',"rank":1}
a.update(b)
print("Updating a with b : ",a)
 
my_dict = {'name':'Jack', 'age': 26}
print("New dictionary :: ",my_dict)
 
my_dict['age'] = 27
 
#Output: {'age': 27, 'name': 'Jack'}
print("Change age 26 to 27 :: ",my_dict)
 
# add item
my_dict['address'] = 'Downtown'  
 
# Output: {'address': 'Downtown', 'age': 27, 'name': 'Jack'}
print("Add new address field :: ",my_dict)
