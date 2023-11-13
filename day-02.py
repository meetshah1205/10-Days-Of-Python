#Welcome to Day-02 of my python course.
#Did I mention that this course will teach you everything you need to know to be dangerous in Python?
#We are going to talk abouut one of the most important and fundamental topics of Python.
#VARIABELS
#Variables are cointainers of data.
#Like you would have conatiners in your home, you store things in it.
#Here the container is variable and the things are data.
#Lets code robot for our coffee shop.
#First we want to name it, I don't want to refer it as robot everytime.
#Lets call him Envixy.
#First we want Envixy to greet the customer(user)
#To do that we will use print.
print("Hello, Welcome to Envixstar coffee shop.")
#Now Envixy is trained enough to say Hello to customers.
#Lets ask the customer for their name to write on the cup.
#print("What is you name?")
#Now Envixy can talk but how will he know the name of the user.
#Think about it.
#if you said inputs, very well done.
#NEW FUNCTIOn TIME
#The input function.
#Do I even need to explain the input function.
#Lets ask the customer about their name.
#input()
#You can also do input("Name goes here") or anything else.But I decided to be simple.
#This input function is designed to take inputs fro mthe user.
#CAUTION: The input fucntion converts the user input into a string even if its not a string. We will talk about it when its important later.
#You can also delete the print function for the name(line 16).
#Now run the code and see.
#After you enter the name, what happens is a bit anti-climatic because it does nothing with our inputs.
#We can also do print our input.
#like this
#print(input("What is your name?"))
#The input function is inside the print function.
#This code prints the input we gave it.
#CAUTION: Never use this if you are using inputs for important things like passwords or you are using it for a calculator.
#Its useless for our cafe waiter Envixy. Because can you imagine you go in a cafe and:
# Envixy: What is you name?
# You: Bob
# Envxy: BOB
#The function(s) on line 33 was just to demonstrate that you can a function inside a function.
#Now we wnat the waiter to greet us after knowing our name.
#So we can do this:
#print("Hello....... Thank you visiting today.")
#Now I can jus treplace the ........ with a name but its not garenteed that the person whose name I give will come.
#The person coming could be anyone.
#To Do what we are intending we are going to use VARIABLES.
#First lets create a variable.
# name = "Envixy" #Replace Envixy with your name.
#Nwo lets print the variable.
# print(name)#No quotes because we are printng a variable
#Now if we run this code we can see the name inside name.
#Variables can change accordiing to our code
#For example lets change name to Iron Man
# name = "Iron Man"
#Lets print name again
# print(name)
#Now we want Envixy to remenber the customer's name
#So we can do this:
name = input("What is you name?\n")
#Now lets print name
# print(name)
#We can use the concept of concatenation which we learnt in DAY-01.
#Lets do it quickly
print("Hello " + name + ",Thank you for visiting today.")
#Now let's make it show a menu after this is printed
print("We have a variety of things. Please choose your order from what we server")
menu = """
1.Esprsso
2.Cappuccino 
3.Black Coffee
4.Latte
5.Milk Coffee
6.Indian Tea
"""
print(menu)
#Let the user choose their order.
order = input("Choose your order.")
#Now let's print the order.
print("So " + name + ", If I am not mistaken, you ordered a " + order + ".")

