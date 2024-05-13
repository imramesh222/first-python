import random

random_side=random.randint(0,1)
if random_side == 0:
  print("Tails")
else:
  print("Heads")

print(f"You got {random_side} after flipping dice")