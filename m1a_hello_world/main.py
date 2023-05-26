import sys
from termcolor import colored, cprint

print("Hello, World!")
my_name = "Jaysen"
print("My name is",my_name)

my_day = "2/6/2006"
print("My birthday is on",my_day)
my_name = "Barry"
print("I sometimes wish my name was", my_name)
favorite_cream = "Moose Tracks"
etown_furthest = "Virginia"
house_number = "171 Hillsdale Road"
new_line = "                   "
print(new_line)
print("My favorite Ice Cream is", favorite_cream, ".")
print()
print("The furthest I have been from Etown is", etown_furthest, ".")
print()
print("My house number is", house_number, ".")
last_name_letter = "hip"
first_name_letter = "ja"
middle_name_letter = "ro"
town_letters = "her"
force = last_name_letter + first_name_letter + " " + middle_name_letter + town_letters
print()
print(force)
import progress.bar
import time

b = progress.bar.Bar('Waiting', max = 100)

for i in range(100):
    b.next()
    time.sleep(0.1)
    
b.finish()

my_age = 15
my_moms_age = 48
age_of_death = 86
parent_age_diff = my_moms_age - my_age
print("My mom and I are", parent_age_diff, "years apart in age")
div = my_moms_age // my_age
remainder = my_moms_age % my_age
print("You have lived", div, "of my lifetimes, plus an additional", remainder, "years!")