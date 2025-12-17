#x=5
#y=3.14
#name="Semma"
#import datetime
#import math
#from math import factorial

#print(x)
#print(y)
#print("your name is "+name)

#name1 =  input("what is your name:")
#print("Hello, "+ name1)

#num1 = input("Enter the first number:")
#num2 = input("Enter the second number:")
#sum = int(num1) + int(num2)
#print("The sum is " + str(sum))

#num1 = int(input("Enter the first number:"))
#num2 = int(input("Enter the second number:"))
#sum = num1 + num2
#print("The sum is " + str(sum))
#age =15

#if age>=18:
#   print("you can vote")
#else:
#    print("you cannot vote")

#temp = float(input("Enter the temperature : "))

#if temp > 30 :
#   print("The temperature is greater than 30")
#elif temp >= 20 :
#    print("The temperature is greater than 20")
#elif temp >= 10 :
#    print("The temperature is greater than 10")
#else:
#    print("The temperature is less than 10")

#fruits =["mango", "cherry", "apple"]

#for fruit in fruits :
#    print(fruit)

#number=int(input("Enter a no. "))
#for i in range(1,11):
#    print(f"{number} x {i} = {number*i}")
#  5

#servers=["10.10.10.10" , "10.0.2.0"]
# for s in servers:
#    print("pinging:",s)

#count=1

#while count<10:
#    print(count)
#    count=count+1

#status="down"
#while status!="running":
#    print("trying to restart service ..")
 #   #systemctl restart httpd
#    status="running"

#numbers=[1,2,3,4,5,6]
#for num in numbers:
#    if num % 2 == 0:
#        print(f"{num} is even")
#    else:
#        print(f"{num} is odd")

#fruits = ["Apple", "Cherry", "Grapes"]
#print(fruits)
#fruits.append("Orange")
#fruits.remove("Cherry")
#print(fruits)
#fruits.insert(1, "Mango")
#print(fruits)

#colors=("red","blue","green")
#print(colors)
#print(len(colors))
#more_colors=("yellow","purple")
#all_colors=colors+more_colors
#print(all_colors)
#port(80,443)

#sports={"Soccer","Basketball","Tennis"}
#print(sports)
#sports.add("Cricket")
#sports.remove("Soccer")
#print(sports)

#capital={"India":"New Delhi","France":"Paris"}
#print(capital["France"])
#capital["Germany"]="Berlin"
#print(capital["Germany"])


#def greet(name):
#    print(f"Namaste..{name}!! Welcome to the python session")

#greet("Seema")
#greet("Amit")
#greet("Pooja")

#def add(a,b):
#    print(f"The sum of {a} and {b} = {a+b}")

#result = add(10,5)
#print(result)


#x=5
#def my_function():
#    global x
#    x=10
#    print(x)
#    print(x)

#my_function()
#print(x)


#result= math.sqrt(16)
#print(result)

#factorial_value= math.factorial(5)
#print(f"Factorial of 5 is {factorial_value}")

#current_time = datetime.datetime.now()
#print(current_time)

#today = datetime.date.today()
#print(today)

#time= datetime.datetime.now().time()
#print(time)


#import os
#cws= os.getcwd()
#print("Current Working Directory:",cws)


#items = os.listdir()
#print("Itema in this folder:",items)

#import numpy as np
#no=np.array([10,20,5,7])
#print("Max: ", np.max(no))
#print("Min: ", np.min(no))
#print("Sum: ", np.sum(no))

#import pandas
#import matplotlib.pyplot as plt
