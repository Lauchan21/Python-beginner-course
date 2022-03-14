################### Scope ####################

enemies = 1

def increase_enemies():
  enemies = 2
  print(f"enemies inside function: {enemies}")

increase_enemies()
print(f"enemies outside function: {enemies}")

######## Local scope (only use inside a function - careful about indentation)##########
def drink_potion():
  potion_strength = 2
  print(potion_strength) #here it will give me 2 inside the function

drink_potion()
#if I print it outside of the function it will give me an error
print(potion_strength) #because it is not in the function: NameError: Name "portion_strength" is not defined

########Global scope# to access it outside of the function#################### 
player_health = 10

def drink_potion():
  potion_strength = 2
  print(player_health)

drink_potion()
print(player_health)

#### There is no Block Scope  ################
game_level= 3
enemies = ["Skeleton", "Zombie", "Alien"]
if game_level < 5:
  new_enemy = enemies[0]

print(new_enemy) #this works perfectly well

#But then if you embedd it in a function there is an error (there is a local scope within the function)
#so need to do like this:
game_level= 3
def create_enemy():
  enemies = ["Skeleton", "Zombie", "Alien"]
  if game_level < 5:
    new_enemy = enemies[0]

  print(new_enemy)
  

################### Modifying Global Scope ####################

enemies = 1

def increase_enemies():
  enemies = 2 #deperate from initial ennemies, its set as 2 and it prints 2
  print(f"enemies inside function: {enemies}")

increase_enemies()
print(f"enemies outside function: {enemies}") #it referes back to initial enemies so its 1

#to make it more understandable
enemies = "Skeleton"

def increase_enemies():
  enemies = "Zombie" #it prints zombie
  print(f"enemies inside function: {enemies}")

increase_enemies()
print(f"enemies outside function: {enemies}") #it prints Skeleton

#if you want to change the amount within the function, you could as follow
enemies = 1

def increase_enemies():
  print(f"enemies inside function: {enemies}")
  return enemies + 1

enemies = increase_enemies()
print(f"enemies outside function: {enemies}")

######## Global Constants ##########
#constant that you will never change with variable that will liekly change
#the consensus in Python is tu put it all uppercase
pi = 3.14159
#Write PI in uppercase
PI = 3.14159
URL = "https://www.google.com"
TWITTER HANDLE = "@Lauchan21"
#helps you not to modify it in your code
                  