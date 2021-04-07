class Student:
    roll=int(input('Enter your Roll Number \n'))
    name=input('Enter your Name \n')
    age=int(input('Enter your Age \n'))
    gender=input('Enter your Gender \n')
    print("")
    class address: #Inner Class
        print ("-------------Inner Class--------------")
        print ("This is Inner class")
        def disp(self):
            print("I am inner")
    @staticmethod #Static method
    def statmeth():
        print ("This is Static method")
    def display_record(self):
        print ("Your Roll number is",self.roll)
        print ("Your Name is",self.name)
        print ("Your Age is",self.age)
        print ("Your Gender is",self.gender)
s=Student() #Main class object
a=s.address()
print("")
print ("-------------Static Method--------------")
Student.statmeth() #calling static method
print("")
print ("-------------Details of Student are--------------")
s.display_record() #Calling class method
a.disp()
