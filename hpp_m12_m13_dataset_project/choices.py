import funcs
from funcs import *
def choices(contents):
  choice = ""
  
  while (choice != 0):
    print("\n0) Quit the program\n1) Search For Record In State\n2) Print Data By Year And State\n3) Total Any Field For Year\n4) Average Any Field For A Year\n5)Find State With Highest In Field")
    choice = int(input("--> "))
    print("\033c")
    if choice == 0:
      exit("Bye!")
  
    if choice == 1:
      funcs.searchStateInfo(contents)
  
    if choice == 2:
      funcs.searchDateInfo(contents)
      
    if choice == 3:
      funcs.totalForYear(contents)
  
    if choice == 4:
      funcs.averageForYear(contents)
  
    if choice == 5:
      funcs.maximumState(contents)