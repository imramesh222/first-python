import random
all_name= input("Enter all the names saperated by comma")
single_name=all_name.split(",")
# print(single_name)
# ap=len(single_name)

# person_who_will_pay=random.randint(0,ap-1)

# op=single_name[person_who_will_pay]
# print(f"{op} should pay all the bill")

np=random.choice(single_name)
print(f"{np} should pay all the bill")