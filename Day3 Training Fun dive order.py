# 🚨 Don't change the code below 👇
print("Welcome to WIE Divers!")
dive = input("How many dives you want to do? 1, 2, or 3: ")
equipment_rental = input("Do you need to rent equipment? Y or N: ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

bill = 0

if dive == "1":
  bill += 450
elif dive == "2":
  bill += 550
else:
  bill += 650

if equipment_rental == "Y":
  bill += 450
else:
  bill += 0


print(f"Your final bill is HK${bill}")






