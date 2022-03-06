#FUNCTIONS WITH OUTPUTS
# Function with output
#simply by printing this
def format_name(f_name, l_name):
  print(f_name.title())
  print(l_name.title())

format_name("laurent", "LAURENT")
  
  #capture inside a variable
def format_name(f_name, l_name):
  formated_f_name = f_name.title()
  formated_l_name = l_name.title()

  print(f"{formated_f_name} {formated_l_name}")

format_name("laurent", "STIEGER")

#instead of printing out we can also return it (now this format string becomes the output)
#this replace the output where the function was called (format_name("laurent", "STIEGER"))
def format_name(f_name, l_name):
  formated_f_name = f_name.title()
  formated_l_name = l_name.title()
  return f"{formated_f_name} {formated_l_name}"

formated_string = format_name("laurent", "STIEGER")

#or could simply do (same)
def format_name(f_name, l_name):
  formated_f_name = f_name.title()
  formated_l_name = l_name.title()
  return f"{formated_f_name} {formated_l_name}"

print(format_name("laurent", "STIEGER"))

#//////////////////////////////////
#multiple return values
#return indicates that return is the end of the function and u should excit function
#so whatever you type after it will not take place
def format_name(f_name, l_name):
  if f_name == "" or l_name == "":
    return "You didn't provide valid input."
  formated_f_name = f_name.title()
  formated_l_name = l_name.title()
  return f"{formated_f_name} {formated_l_name}"

print(format_name(input("What is your first name?"), input("What is your first name?")))
      
     
#////////////////////////////////////////////////////////////////////////////////////////
#doc string (a way to add documentation along your coding (functions or block of codes)
#it comes after def line and use 3 quotation marks """   """
def format_name(f_name, l_name):
    """Take a first and last name and format it to return the title case version of the name."""  
  if f_name == "" or l_name == "":
    return "You didn't provide valid input."
  formated_f_name = f_name.title()
  formated_l_name = l_name.title()
  return f"{formated_f_name} {formated_l_name}"

                  