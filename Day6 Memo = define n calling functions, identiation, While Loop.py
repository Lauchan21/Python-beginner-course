#FUNCTIONS (built in function)
print("Hello")
num_char = len("Hello")
print(num_char)

#How to make your own function
#start with a key word and def (to define the function)

def my_function():
  print("Hello")
  print("Bye")
  #at this stage nothing happen, you first need to call the function as below
  my_function()
#so full code would be:
def my_function():
  print("Hello")
  print("Bye")

my_function()

#RECAP Defining and calling a function
#Defining function
def my_function():
    #Do this
    #Then do this
    #finally do this
#Caling function
my_function()
    
#Reeborg World (makes code much shorter and readable)
def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
#Reeborg World to do a square
#https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Alone&url=worlds%2Ftutorial_en%2Falone.json
#FUNCTIONS (built in function)
def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
turn_left()
move()
turn_right()
move()
turnn_right()
move()
turn_right()
move()

#Reeborg challenge could also add wen repeating tasks (to shorten code)
for step in range (6):
    jump()
    
#e.g.
def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
def jump():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()
    
for step in range(6):
    jump()

#//////////////////////////////////////////////////////////
#Identation could use TAB button instead of space (cant mix both! in same file)
# Use 4 spaces per indentation level!!!
#settings can change ident type to spaces and ident size to 4

#/////////////////////////////////////////////////////////////
#WHILE LOOPS

#For loop is
for item in list_of_items:
    #Do something to each item
    
for number in range (a, b):
    print(number)
    
#while loop is
while something_is_true:
    #Do something repeatedly
    
#E.g. in reeborg instead of for step in range(6):
#it could be
number_ofhurdles = 6
while number_of_hurdles > 0:
    jump()
    number_of_hurdles -= 1
    
#so what happens is
while something_is_true:
    #Do this
    #then do this
    #then do this
    #until it becomes false

#Reeborg challenge Hurdle2
def turn_right():
    turn_left()
    turn_left()
    turn_left()

def jump():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()
    
while not at_goal(): #not true (true until)
    jump()
    
#Could also have put (not true until)
while at_goal != True:
    jump
    
#When to use a for loop or a while loop
#For is when you make iteration and need to do things with each things iterating over for example a list of fruit, for each fruits in a list of fruits and want to say do something with each items in it)
#While is when you dont really care what items you go through a list and want to carry out functionality many times until a function you set
#While loop can be dangerous (for will stop until it is parameters, While will continue until it goes False so it can be infinite)
