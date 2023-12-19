# Imports all functions, variables, classes available in the random module
from random import *

# choice - It will chselect any random element from list, tupple or string 

random_in_list = choice([1, 2, 3, 'Khateeb', 100, 200])
print(random_in_list);

random_in_tupple = choice(("Hello", "everyone", "good", "morning"))
print(random_in_tupple);

random_in_string = choice("Ignited minds")
print(random_in_string);