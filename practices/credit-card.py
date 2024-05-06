import random
persons=input("Enter every person you want to saperated by comma ','")
single_person=persons.split(",")
print(single_person)
len(single_person)
person_who_pay=random.choice(single_person)
print(f"{person_who_pay} will pay the bill")
# person_who_pay=random.randint(0,len(single_person)-1)
# op=single_person[person_who_pay]
# print(f"{op} will pay the bill")