# Write your code below this line 👇
#PRINT FUNCTION - e.g HOW TO WRITE "HELLO WORLD"
print("Hello World!")

#print HOW TO MAKE SAME TEXT ON SEVERAL COLUMS
print("i am the best\ni am the best")

#print STRING MANUPILUATION 3 types on how to write (Concatenation is done with the "+" sign.")
print("Hello " + "Angela")
print("Hello" + " Angela")
print("Hello" + " " + "Angela")

#INPUT FUNCTION - will get user input in console to give user something to work with
#Then print() will print the word "Hello" and the user input
input("What is your name?")

#You can the combine print and input in 1 like
print("Hello "+ input("What is your name?") + "!")

#number of characters in a user Name or character
print( len( input("What is your name?")))

#VARIABLES
name = input ("What is your name?")
print (name)
print ("hello " + (name))

#name is the variable here
name = input("What is your name?")
print(name)

name= "Jack"
print(name)

#if you ad same variable, a 2nd time it will use the 2nd one for 2nd time
name= "Jack"
print(name)
name= "Angela"
print(name)

#From exercice 3
print ( len( input("what is your name?")))
#You could do
name = input("What is your name?")
lenght = len(name)
print(lenght)

#Changes variables between 2 (tech create a third variable to switch the 2 first ones)
c = a
a = b
b = c

#NAMING VARIABLES - YOU CAN CALL THEM PRETTY MUCH WHAT YOU WANT
#FOR EXAMPLE
name = input("What is your name?")
lenght = len(name)
print(lenght)
#COULD ALSO BE
n = input("What is your name?")
l = len(n)
print(l)
#Important is to keep the code readable if you come back after 6 months "l" "n" you might forget

#use underscore "_" when naming something for example "user_name"
#Synthax error if you start with a number for example "1name"
#\n also brings you back to a new line (makes the code look better) for example:
pet = input ("What is the name of your pet?\n")