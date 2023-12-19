import random

random_number = random.randrange(0, 100, 10)

# Will give an integer in [0, 100] but will start with 0 and will only print after 10 steps of zero
# Like it will randomly print 0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100
print(random_number)