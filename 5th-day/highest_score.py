student_scores=input("Enter score of every students separated ").split()


for n in range(0,len(student_scores)):
  student_scores[n]=int(student_scores[n])
print(student_scores)

highest_score=0
for score in student_scores:
  if score > highest_score:
    highest_score=score

print(f"The highest score in the calss is : {highest_score}")



# print(max(student_scores))
# print(min(student_scores))