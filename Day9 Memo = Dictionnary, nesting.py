#Dictionary in Python work like a normal dictionary.
#If you search "Code" you find the definition "program instruction...." called the "Key" and the "Value"
#Key Value
#Bug An error in....
#Dictionary_name = {"Bug": "An error in..."}
#If you have to seperate with a ","
#Dictionary_name = {"Bug": "An error in...", "Function": "A piece of code..."}

programming_dictionary = {
  "Bug": "An error in a program that prevents the program from running as expected.", 
  "Function": "A piece of code that you can easily call over and over again.",
}
#Here we have key so we can collect the needed info by typing the key (the string)
programming_dictionary["Bug"]

#For example to print it
print(programming_dictionary["Bug"])

#Adding new items to dictionnary
programming_dictionary["Loop"] = "The action of doing something over and over again."
#when printing
print(programming_dictionary) #the 3 keys are printed

#Create empty dictionnary at the beginning of your code is sometimes useful
empty_dictionary = {}

#Wipe an excisting dictionnary
programming_dictionary = {}
print(programming_dictionary) #it will be completely empty (to clear out user progress or game restarts)

#Edit an item in the dictionnary (The entry value will be edited)
programming_dictionary["Bug"] = "A moth in your computer."
print(programming_dictionary) #The value has been changed

#Loop through dictionnary
for thing in programming_dictionary:
  print(thing)  #it will print only Bug, Function & Loop

for key in programming_dictionary:
  print(key) #it will print Bug Function Loop
  print(programming_dictionary[key]) #it will print the value below each key

#/////////////////////////////////////////
#NESTING (put 1 inside the other)
= {
  "key": [list], 
  "key": "Value2",
}

#OR
= {
  "key": [list], 
  "key": {Dictionnary},
}

#Nesting Simple as seen before nesting for easy dictionnary
capitals = {
  "France": "Paris",
  "Germany": "Berlin",
}

#Nesting a List in a Dictionary (when becoming more complex)
#Each kkey only can have 1 value so u need to put in list []

travel_log = {
  "France": ["Paris", "Lille", "Dijon"],
  "Germany": ["Berlin", "Hamburg", "Stuttgart"],
}

#Nesting Dictionary in a Dictionary
#Can store mulitple data {key:[value], key2: value2}

travel_log = {
  "France": {"cities_visited": ["Paris", "Lille", "Dijon"], "total_visits": 12},
  "Germany": {"cities_visited": ["Berlin", "Hamburg", "Stuttgart"], "total_visits": 5},
}

#Nesting Dictionaries in Lists

travel_log = [
{
  "country": "France", 
  "cities_visited": ["Paris", "Lille", "Dijon"], 
  "total_visits": 12,
},
{
  "country": "Germany",
  "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
  "total_visits": 5,
},
]