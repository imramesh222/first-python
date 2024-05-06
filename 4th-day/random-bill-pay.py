import random

all_persons = input("Enter names of persons separated by comma: ")
single_person = all_persons.split(",")

# print(single_person)
# print(len(single_person))
# print(single_person[0])
# op = random.randint(0, len(single_person)-1)
# print(single_person[op])

person_who_wil_pay=random.choice(single_person)
print(person_who_wil_pay)