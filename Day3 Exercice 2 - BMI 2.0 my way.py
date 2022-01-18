# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
weight_as_float = (weight)
height_as_float = (height)

bmi = weight_as_float / (height_as_float * height_as_float)
bmi_as_float = str(round(bmi, 1))

if bmi < 18.5:
    print("Your BMI is " + (bmi_as_float) + ", you are underweight")
elif bmi > 18.5 and bmi < 25:
              print("Your BMI is " + (bmi_as_float) +", you have a normal weight.")
elif bmi > 25 and bmi < 30:
              print("Your BMI is " + (bmi_as_float) +", you are slightly overweight.")
elif bmi > 30 and bmi < 35:
              print("Your BMI is " + (bmi_as_float) + ", you are obese.")
else:
    print("Your BMI is " + (bmi_as_float) + ", you are clinically obese.")




