print("Highest score csaloculator")
student_scores=input("Enter score of every students \n" ).split()


for n in range(0,student_scores):
  student_scores[n]=int(student_scores[n])

highest_score=0
for score in student_scores:
  if score > highest_score:
    highest_score=score

print(f"The highest score in the calss is : {highest_score}")