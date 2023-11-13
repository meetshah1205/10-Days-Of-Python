#WELCOME TO MY PYTHON COURSE!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#This is a comment.
#A comment in an programming language is ignored by the computer.
#Comments are used to explain what your code does.
#String are basically words in Python.
#To write a string you use either Double quotes("") or Sngle Quotes('').
#You can also use Triple quotes.
#A function
#A function is a command you give to your computer to execute something in a specific way.
#There are some built-in functions in Python.
#We will later on learn how to create our own funtions.
print("This is a single line string in Python.")
#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#This statement is used to print a single line string.
#The print function is used to print things on the screen(console).
#In this case we used the print funtion to tell our compiler.
#Compiler is machine which is used to run our code. 
# In this case we used the compiler to print what we told it to.
#In this case its"I this case its "This is a single line string in Python"
#We can ofcource print multiple times.
#For example:
print("This is a line.")
print("This is another line.")
print("And one more.")
print("So by nnow you should have understood how to use print function.")
#But what is you had to print multiple lines.
#Would you do it like this:
print("I am Iron Man.")
print("No, I am Tony Strak.")
print("THE ONE PIECE IS REAL!!!!")
print("I have no idea how the above statements' context is related. ")
#If you are a complete begginer, this would be logical.
#But there is a way to do this with only 1 print satement.
#You can use Triple Quotes as I mentioned earlier.
#Like this:
print("""I am Iron Man.
No, I am Tony Stark
THE ONE PIECE IS REAL!!!!
I have no idea how teh above statements' context is related""")
#Here in the above example ou used jsut 1 print statements to do the work of 4 print statements.
#NOW THAT IS CALLED 4 TIEMS IMPROVEMENT!!!
#And ofcource I don't need to mention that you use as much space as you want between lines.
#But if you want to add spaces between line you use /n
#For example
print("I am Iron Man\n" "Now I am not going to write the sentences over and over again.")
#Great thing about python is that the syntax(the way you write the code) is really easy.
#As you progress the you realise that the syntax just looks like simple English.
#Now lets learn another way to add multiple strings.
#We use the addition operator(+) to add things in Python just like real life.
#For example:
print("I am Iron Man" + "No, I am Tony Stark" + "THE ONE PIECE IS Real!!!")
#This is called concatening(I have no idea I spelled it correctlly)
#But you might have seen that after running the code, trhere is a problem in the concaneted string.
#The problem is that the compiler is treating it just like a thing to separate the strings.
#But how do we fix it?
#Well. You have the right doubt. becuase I have no idea how.
#Ok just kidding here is how you fix it.
#We use somethng called an empty string (" ")
#An empty string is just quotes with space in-between.
#Here is an updated version of concaneted string:
print("I am Iron Man" + " " "No, I am Tony Stark" + " " + "Think the ahed by yourself")
#Now the compiler still treats the + sign as a spearator but it adds the empty string after it.
#Now don't think that you fooled the compiler because this is just basic things.
#What we did was treated by the compiler like this:
#print("I am Iron Man" + " " "No, I am Tony Stark" + " " + "Think the ahed by yourself")
#what the compiler understood was:
#print I am Iron Man(empty string space)No, I am Tony Stark(empty string space)Think the ahed by yourself.
#But instead of empty string space  it printed nothing( )
#Now lets say wanted to print something 100 or 10000 times.
#Will youu write or copy-paste that many print statements?
#Or do this:
print("THE ONE PIECE IS REAL!!!" * 100)
#ofcource the second one is better but what if you wanted each one in a new line.
#Well simple, use the new line \n command.
#Like this:
print("THE ONE PIECE IS REAL!!!\n" *100)
#This prints THE ONE PIECE IS REAL!! 100 times. Each in a new line.
#Woah we learnt a lot today.
#lets keep today only until here.
#Practise, Revise and Play with the concepts we learnt today.
#Not to scare you but its just the surface of python development. Python goes a lot deeper than this.