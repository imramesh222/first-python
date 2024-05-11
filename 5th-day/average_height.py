students_heights=input("Enter a list of students height ").split()
for n in range(0, len(students_heights)):
  students_heights[n]=int(students_heights[n])
print(students_heights)



#Write code here

# using for loop
total_height=0
for height in students_heights:
  total_height += height
print(total_height)


no_of_students=0
for student in students_heights:
  no_of_students += 1
print(no_of_students)

average_height = round(total_height / no_of_students)
print(average_height)

# print(len(students_heights))
# print(sum(students_heights))

# total_heights = sum(students_heights)
# no_of_students=len(students_heights)
# average_height = round(total_heights / no_of_students)
# print(average_height)

