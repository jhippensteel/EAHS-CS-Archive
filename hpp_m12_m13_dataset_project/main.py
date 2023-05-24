import csv
import funcs
from choices import *

with open("energy.csv") as file:
  contents = list(csv.reader(file))

choices(contents)