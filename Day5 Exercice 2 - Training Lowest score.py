# 🚨 Don't change the code below 👇
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)
# 🚨 Don't change the code above 👆

#Write your code below this row 👇
lowest_score = 100
for score in student_scores:
  if score < lowest_score:
    lowest_score = score
print(f"The lowest score in the class is: {lowest_score}")



