#CONDITIONAL STATEMENT
#"if/else" STATEMENT
if condition:
do this
else:
do this

#ex: Baththub situation
water_level = 50
if water_level > 80:
    print("Drain water")
else:
    print("Continue")
    
#ex: Height of kid (make sure ELSE IS ALIGNED WITH IF)
if height > 120:
    print("You can ride the rollercoaster!")
else:
    print("Sorry, you have to grow taller")
#if you get identiation error its because you missaligned-indeted)
#if you want to include somebody that is 120 need to put >=
    
#/////////////////////////////////////////////////////////////////////////
    
#COMPARISON OPERATORS
# > Greater than
# < Less than
# >= Greater than or equal to
# <= Less than or equal to
# != Not equal to
# == Equal to - check equality (value on left and on right)

#///////////////////////////////////////////////////////////////////////////////

#MODULO OPERATIONS (using %)
#it will divide a number
#e.g.
#7 % 2 (gives the remainder of number)
# 2 + 2 + 2 + 1 (it can be divided 3 times and give a remainer of 1)
#7 % 3
# 3 + 3 + 1 (it will also give me 1)

#In the previous example, if you want a 2nd conditions for e.g. 1st is height 2nd is their age
# <= 18 $7
# >18 $12
#We called it a Nested if / else conditions
#Basically when 1 conditions passed we can check for a 2nd condition
if condition:
    if another condition:
        do this #for this to happen the 2 on top need to happen)
    else:
        do this #for this to happen 1st needs to happen 2nd NOT
else: do this #for this 1st one didnt happen
#e.gs below with height and age
if height >= 120:
    print("You can ride the rollercoaster!")
    age = int(input("What is your age? "))
    if age <= 18:
              print("Please pay $7.")
    else:
              print("Please pay $12.")
else:
    print("Sorry, you have to grow taller")
# Now lets say there are 3 prices <12 $5  12-18 $7 and >18 $12
#IF/ELIF/ELSE CONDITIONS ELIF stands for ELSEIF
if condition1:
      do A
elif condition2:
      do B
else:
      do this
#e.g. below
print ("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))    
           
if height >= 120:
    print("You can ride the rollercoaster!")
    age = int(input("What is your age? "))
    if age < 12:
        print("Please pay $5.")
    elif age <= 18:
        print("Please pay $7.")
    else:
        print("Please pay $12.")
else:
    print("Sorry, you have to grow taller")
    
#In the previous condition we actually really on checked 1 condition because we would by pass 2nd condition
#In the previous example if we want to ask them if they want to purchase a photo (not relevant to their age and ticket price)
#Several conditions will be carried out
if condition1:
    do A
if condition2:
    do B
if condition3:
    do C
#e.g. below

print ("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0
    
if height >= 120:
    print("You can ride the rollercoaster!")
    age = int(input("What is your age? "))
    if age < 12:
        bill = 5
        print("Child tickets are $5.")
    elif age <= 18:
        bill = 7
        print("Youth ticket are $7.")
    else:
        bill = 12
        print("Adult ticket are $12.")
              
    wants_photo = input("Do you want a photo taken? Y or N. ")
    if wants_photo == "Y":
        bill = bill + 3 #could write also bill += 3
    #no need to put else because No wouldnt affect the code
        
    print(f"Your final bill is ${bill}")
    
else:
    print("Sorry, you have to grow taller")
    
#/////////////////////////////////////////////////////////////////////////////////
    
#MULTIPLE CONDIIONS IN THE SAME LINE OF CODE
if condition1 & condition2 & condition3:
    do this
else:
    do this
#Logical Operators
# A and B (both have to be true both A and B)then True otherwise its False
# C or D (if one of them is true then its True if both are false then its False
#not E (it reverse a condition (if condition is false then its True, if condition is True then its False)

#A and B
# a= 12
# a > 15
# False
# a> 10
# True
# a>10 and a<13
# True
# a>15 and a<13
# False

# not E
# a =12
# not a >15
# True (bc 12 is less than 15)

#e.g. Add free ride for people aged 45-55 in the rollercoaster example
print ("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))  

if height >= 120:
    print("You can ride the rollercoaster!")
    age = int(input("What is your age? "))
    if age < 12:
        bill = 5
        print("Child tickets are $5.")
    elif age <= 18:
        bill = 7
        print("Youth ticket are $7.")
    elif age >=45 and age <=55:
        bill = 0
        print("Have a free ride on us!")
    else:
        bill = 12
        print("Adult ticket are $12.")
              
    wants_photo = input("Do you want a photo taken? Y or N. ")
    if wants_photo == "Y":
        bill = bill + 3 #could write also bill += 3
    #no need to put else because No wouldnt affect the code
        
    print(f"Your final bill is ${bill}")
    
else:
    print("Sorry, you have to grow taller")

#//////////////////////////////////////////////////////////////////////////////////////
#The lower () (change majuscule to lower character)
"Angela" .lower()
'angela'
#The count () (number of times a letter comes in a string)
"Angela" .count("a")
1

lower_case_name = "Angela" .lower()
lower_case_name.count("a")
2


    