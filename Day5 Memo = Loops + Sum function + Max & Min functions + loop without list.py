#LOOPS
#for item in list_of_items:
    #Do something to each item

fruits = ["Apple", "Peach", "Pear"]
for fruit in fruits:
    print(fruit)
#it will print as below in that order (it takes it the order it is in the string:
#Apple
#Peach
#Pear
    
#You can add stuff with the print
fruits = ["Apple", "Peach", "Pear"]
for fruit in fruits:
    print(fruit)
    print(fruit + " Pie")
#it will print as below in that order (it takes it the order it is in the string:
#Apple
#Apple + Pie
#Peach
#Peach + Pie
#Pear
#Pear + Pie

#If you keep idented and put print(fruits) it will do the loop 3 times because there is 3 items
fruits = ["Apple", "Peach", "Pear"]
for fruit in fruits:
    print(fruit)
    print(fruit + " Pie")
    print (fruits)
#if you remove the indent it will print once bc its not in the loop (printed after the loop is done)
fruits = ["Apple", "Peach", "Pear"]
for fruit in fruits:
    print(fruit)
    print(fruit + " Pie")
print (fruits)

#SUM function (gives a total of all the amounts in a list)
print(sum(student_heights))

#MAX function (gives you the highest value)
print(max(student_score))

#MIN function (gives you the lowest value)
print(min(student_score))

#/////////////////////////////////////////////

#FOR LOOP INDEPENDANT OF A LIST (without a list)
#using FOR LOOP with RANGE function ()
for number in range (a, b):
    print(number)
#e.g.
for number in range(1, 10): #not including 10
    print(number)
#1
#2
#3
#4
#...until 9

#if you want to increase by any number other than 1 you need to add another ,
#at the end of it and specify how "large" you want the "step" to be
#e.g.
for number in range(1, 11, 3): #step is 3
    print(number)
#1
#4
#7
#10
    
#coming back at the pb for begining of the lesson
total = 0
for number in range (1, 101):
    total += number
print(total)

        