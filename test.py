# class Person:
#     name = "Amar"
#     occupation = "Software Developer"
#     networth = 100
#     def info(self):
#         print(f"{self.name} is a {self.occupation} his networth {self.networth}")

# a = Person()
# b = Person()
# c = Person()

# a.name = "Ajay"
# a.occupation = "Accountant"
# a.networth = 2000
# b.name = "Nikita"
# b.occupation = "HR"
# b.networth = 1000
# #print(a.name, a.occupation)
# a.info()
# b.info()
# c.info()


# def run(fname = "" , lname = ""):
#     print(fname + " " + lname)

# run("Rahul" , "raj")
# run("Ajay" , "singh")

# def new(name , age , city):

#     print(f"Hello {name} your age  is {age} and your city is {city}")

# new("Anas", 19 ,"Lucknow")
# new("Amar", 18 , "Hardoi")
# new("Gautam", 20, "Sandila")

# # Default value argument:

# def new2(name = "John", age = 18, city = "Lucknow"):
#     print(f"Hello {name} your age  is {age} and your city is {city}")

# new2("Anas", 19 ,"Lucknow")
# new2("Ajay")

# def data(*names):
#     for name in names:
#         print(f"Hello {name}")

# data("Aman" ,"Anas")

# def add(a,b,c):
#     return a * b * c

# result = add(2,6,5)
# print(result)

# def calculate_sum():
#     value1 = int(input("Enter value1: "))
#     value2 = int(input("Enter value2: "))

#     return value1 * value2

# result = calculate_sum()
# print(result)

# # Variable-Length Arguments in Functions:
# def read(*args):
#     for x in args:
#         print(x)
# read(1,2,3,4,5,6)

# def sum_values():
#     v1 = int(input("v1: "))
#     v2 = int(input("v2: "))

#     return v1 + v2

# def subtract_values():
#     v1 = int(input("v1: "))
#     v2 = int(input("v2: "))
#     return v1 - v2

# result1 = sum_values()
# print(f"Sum result: {result1}")

# result2 = subtract_values()
# print(f"Sum result: {result2}")
# def append_to_list(val, my_list=[]):
#     my_list.append(val)
#     return my_list

# print(append_to_list(1))  # Output: [1]
# print(append_to_list(2))  # Output: [1, 2] (unexpected behavior)

# x = 10  # Global variable

# def my_function():
#     global x
#     x = 20  

# my_function()
# print(x)

# #average of 3 numbers:
# def average(a, b, c):
#     sum = a + b + c
#     avg = sum / 3
#     print(avg)
#     return avg

# average(1, 2, 3)

# fruits = ["apple", "banana", "cherry"]
# def print_len(list):
#     print(len(list))
# print_len(fruits)

# def cal_fact(n):
#     fact = 1
#     for i in range(1, n+1):
#         fact *= i
#     print(fact)
# cal_fact(6)

# def converter(usd_val):
#     inr_val = usd_val * 83
#     print(usd_val,"USD=",inr_val, "INR")

# converter(76)

# def even_odd(x):
#     if (x % 2 == 0) :
#         print("even")
#     else:
#         print("odd")
# even_odd(int(input("Enter no.")))

# def show(n):
#     if(n == 0):
#          return
#     print(n)
#     show(n-1)
#     print("End")
# show(3)

# # object oriented programming:

# class Car:
#     color = "blue"
#     brand = "mercedes"

# car1 = Car()
# print(car1.color)
# print(car1.brand)

# class Student():
   
#    def __init__(self,name, marks):
#         self.name = name
#         self.marks = marks
#         print("adding new student in Database...")

# s1 = Student("Aman", 96)
# print(s1.name, s1.marks)

# s2 = Student("Anas", 91)
# print(s2.name, s2.marks)

# class Student:
#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks

#     def get_avg(self):
#         sum = 0
#         for val in self.marks:
#             sum += val
#         print("hi", self.name, "your avg score is:", sum/3)

# s1 = Student("tony stark", [99, 98, 97])
# s1.get_avg()

# class Account:
#     def __init__(self, name, bal, acc):
#         self.name = name
#         self.balance = bal
#         self.account = acc

#     def debit(self, amount):
#         self.balance -= amount
#         print("Rs.", amount, "was debited")
#         print("Total blanace = ", self.get_balance())
    
    
#     def credit(self, amount):
#         self.balance += amount
#         print("Rs.", amount, "was credited")
#         print("Total blanace = ", self.get_balance())

#     def get_balance(self):
#         return self.balance
    

# acc1 = Account("Aman", 12000, 8520)
# acc1.debit(1000)
# acc1.credit(5000)
# acc1.credit(50000)

# class Fan:
#     def __init__(self,name, age, marks):
#         self.name = name 
#         self.age = age
#         self.marks = marks

# fan = Fan("Anas", 19, 95)
# print(fan.name, fan.age, fan.marks)

# class Person:
#     name = "Aman"
#     occupation = "Software Developer"
#     networth = 100
#     def info(self):
#         print

# a = Person()
# print(a.name, a.occupation)

# class Man():
#     def __init__(self, name,age, city):
#         self.name = name
#         self.age = age
#         self.city = city
    
#     def print(self):
#         print(self.name, self.age,self.city)
    
# f = Man("Aman", 25, "Lucknow")
# f.print()

# class Person:
#     def __init__(self, name, age ):
#         self.name = name
#         self.age = age

#     def print(self):
#         print("hello my name is " + self.name, self.age)

# a = Person("Anas", 21)
# b = Person("Aman", 23)
# c = Person("Amar", 20)
# a.print()
# b.print()
# c.print()


# class Man:
#     def __init__(self, name, id):
#         self.name = name
#         self.id = id

#     def showDetails(self):
#         print(f"The name of Man: {self.id} is {self.name}")

# class Son(Man):
#     def showLanguage(self):
#        print("The defalt language is python")

# m1 = Man("Rohan Das", 410)
# m1.showDetails()
# m2 = Son("Ajay",425)
# m2.showLanguage()

# class BankAccount:
#     def __init__(self,account_number,balance):
#         self._account_niumber = account_number
#         self._balance = balance

#     def get_balance(self):
#         return self._balance

#     def deposit(self,amount):
#         self._balance += amount

#     def withdraw(self,amount):
#         if amount > self._balance:
#             print("Insufficient balance")
#         else:
#             self._balance -= amount

# account = BankAccount("1234567890", 1000)
# print(account.get_balance())
# account.deposit(500)
# print(account.get_balance())
# account.withdraw(200)
# print(account.get_balance())


# #__str__method:
# class Student:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def __str__(self):
#         return f"The name is {self.name} and age {self.age}"
    
        
# a = Student("Aman", 15)
# print(a)
# __repr__mrthod:
# class That:
#     def __init__(self,name,marks,add):
#         self.name = name
#         self.marks = marks
#         self.add = add

#     def __repr__(self):
#         return f"The student is {self.name} his marks {self.marks} and add. {self.add}."

# n = That("Amar", 45, "Chandigarh")
# print(repr(n))

import calendar

y = int(input("Enter your year:"))
m = int(input("Enter your month:"))

print(calendar.month(y, m))



