#DATA TYPES

#STRING (string is when you use something in a bracket
#Put out the "index" or "position" of the character we want
#In this case if you put 0 (0 is the first number not 1) then computer prints "H"
print ("Hello"[0])

#INTERGER (number without decimal places) interger is the coding lingo for whole numbers
#It then really counts 123+345 and will print 468
print(123 + 345)

#FLOAT (number with decimal that can be moved) short for floating point number
3.14159

#BOOTLEAN (only true or false with big T and big F)
True
False

#CALCULATIONS

#PEMDAS
#Parentheses ()
#Exponents **
#Multiplication or Division ** or /
#Addition or Substraction + or -
3 + 5
3 - 5
3 * 5
3 / 5
** (exponent) 2 ** 3 = 2 x 2 x 2
# what it is (2 to the power of 3)
#several calculation in a line of code - order of calculation :
()
 **
 * or /
 + or -
 for example: print  (3 * 3 + 3 / 3 - 3)
#can change priority using ()
 
#number with exact decimals (it alwauys appears as a floating point number)
print (8/3)

#if you convert to an interger (it goes to closest decimal)
print (int(8/3))
# or can also do
print (8//3)
 #but can also do this
 #round number to higher or lower closest decimal
 print (round(8/3))
 
 #Can go one step further to precise which number you want to round it to (e.g. 2 decimal places)
 print (round(8/3, 2))
 #result is 2.67
 print (2.666667, 2)
 # result is 2.67
 
 # Also can make float into interger by
 print (8 //3)
 #result is 2
 
 #when using a variable (e.g.below) can continue the calcluation
 result = 4/2
 result /= 2
 Print (result)
 #result is 1
 
 #in a game if you want to add up score
 score = 0
 
 #user scores a point
 score+= 1
 
 print (score)
 #result is 1
 
 #F-STRINGS (to simplify the code)
 
 #BASIC WAY
 score = 0
 
print ("your score is " + str(score))
#result: Your score is 0

#Alternative when incorporating many data types
#1interger2.float3.boolean
score=0
height=1.8
isWinning = True
print(f"your score is {score}, your height is {height}, you are winning is {isWinning}")


 
 