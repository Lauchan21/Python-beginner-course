#FUNCTION WITH INPUT (functions that allow them to give input)
#Simple function definition
def greet():
  print("Hello")
  print("How do you do?")
  print("Isn't the weather nice?")

greet()

#Add variable (have to add in the "()" ) to pass the value when you call the function
#function that allows for input
def greet_with_name(name):
  print(f"Hello {name}")
  print(f"How do you do {name}?")
  print("Isn't the weather nice?")

greet_with_name("Angela")
#"name" is generally refered to as the "parameter" -> Name of the data
#"Angela" as the "argument" -> The actual piece of data that is passed over to the function

#/////////////////////////////
#POSITIONAL vs KEYWORD ADJUSTMENT

#Functions with more than 1 input
#here parameters are Name and Location
#Here arguments are Jack bauer and Nowhere
def greet_with(name, location):
  print(f"Hello {name}")
  print(f"What is the weather like in {location}?")

greet_with("Jack Bauer", "Nowhere")

#to avoid mistyping you could add "Keyword Arguments" so it doesnt impact the order
def greet_with(name, location):
  print(f"Hello {name}")
  print(f"What is the weather like in {location}?")

greet_with(name="Jack Bauer", location="Nowhere")