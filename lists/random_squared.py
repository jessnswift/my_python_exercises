import random

random_numbers = random.sample(range(0,49), 20)
print(random_numbers)

squared_number = [num*num for num in random_numbers]
print(squared_number)