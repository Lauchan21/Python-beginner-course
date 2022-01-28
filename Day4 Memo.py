#RANDOMIZATION AND PYTHON LIST

#RANDOM NUMBERS/////////////
#askpython.com Searh Python random model
#show random inter, float etc...
#Need to import it in code to access it
import random
#now can use in python code
#so for example to have a random number between 1 and 10 (both included)
import random

random_integer = random.randint(1, 10)
print(random_integer)

#Random number is a Python Module (created by Python team)
#What is a module: Code can be so long so its hard to follow in a large piece of code, so spliting code
#in module each module is a function of your program. Some module could be colloabration with different ppl.
#Main.py is the main file that will be executed when we run our code
#If click on "Add file" create a new file (e.g.My Module") u can work on something else
#You can then import file in Main.py
import my_module

#RANDOM FLOATING NUMBER//////////
#so for example to have a random number between 0 and 1 (does not include 1)
import random

random_integer = random.randint(1, 10)
print(random_integer)

random_float = random.random()
print(random_float)

#how to create a random decimal between 0 and 5?
#need to multiply the random float
import random

random_integer = random.randint(1, 10)
print(random_integer)

random_float = random.random() * 5
print(random_float)

#True Love previously if you just want to generate a random number
love_score = random.randit(0, 100)
print(f"Your love score is {love_score}")



#DATA STRUCTURE (= organizing and storing data in Python) /////////////////////////////////////
#Useful when you want to store lots of datas (e.g. All the states in the US)
# States in the us (all states in the US store in the same variable)
#An order (e.g. people in the queue in the proper order 1st come etc...)
#LIST
fruits = ["item1", "item2"] #can store strings with numbers..Anything matter except syntax -> [  ,  , ]

#LIST EXAMPLE"
#in the past
state1 = "Delaware"
state2 = "Pennsylvania"
state3 = "New jersey"
#Now
states_of_america = ["delaware", "Pennsylvania","New Jersey"]
#IMPORTANT: The order is defined by the order in the list so for example in US first state was Delaware so it should be 1st in the list
#so in the full list of states if you want to see which one joined first you could do
print(states_of_america[0]) #remember 0 is the first number
#it will print delaware

#wenn you want to get hold of a particular piece of data stored inside a list you can get the name of the list and add into bracket
#e.g. i want to get Pennsylvania
 #Now this part of the code is equal to New Jersey
#you could then print it e.g.
print(states_of_america[1])
#You can also have negative index e.g.
print(states_of_america[-1]) #you would get New Jersey
#You can also change the spelling of an item in the list e.g.
states_of_america [1] = "Pencilvania"
#ADDING TO THE LIST You can also add an item in the list (e.g. adding a state joining in your country)
states_of_america.append("Guam")
print(states_of_america) #Guam will be added in the end
#EXTEND TO THE LIST You can also add a full list of items (need to use [])
states_of_america.extend(["Angelaland", "Laurentland"])
print(states_of_america) #the full list will be added in the end

#Indexerror "list index out of range"
#You get the error when what u print is out of the list for example there is 50 states and u search for 51
print(states_of_america[50])
#You get the index error message because its beyond hawaii

#List in a list = NESTED LIST (several lists in a list)
fruits = ["strawberries", "Nectarines", "Grapes", "Peaches", "Cherries", "Pears"]
vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]

dirty_dozen = [fruits, vegetables]

print(dirty_dozen)