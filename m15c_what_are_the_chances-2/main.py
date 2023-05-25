#Jaysen Hippensteel. Lottery

import sys, random, time
import os

lucky_numbers = []
payout = 0
wins = 0

lucky_numbers.append(str(input("Lucky Number 1 >> ")))
lucky_numbers.append(str(input("Lucky Number 2 >> ")))
lucky_numbers.append(str(input("Lucky Number 3 >> ")))
lucky_numbers.append(str(input("Lucky Number 4 >> ")))
lucky_numbers.append(str(input("Lucky Number 5 >> ")))
lucky_numbers.append(str(input("Lucky Number 6 >> ")))
lucky_numbers.append(str(input("Lucky Number 7 >> ")))
lucky_numbers.append(str(input("Lucky Number 8 >> ")))
lucky_numbers.append(str(input("Lucky Number 9 >> ")))
lucky_numbers.append(str(input("Lucky Number 10 >> ")))
lucky_numbers.append(str(input("Lucky Number 11 >> ")))
lucky_numbers.append(str(input("Lucky Number 12 >> ")))
lucky_numbers.append(str(input("Lucky Number 13 >> ")))
lucky_numbers.append(str(input("Lucky Number 14 >> ")))
lucky_numbers.append(str(input("Lucky Number 15 >> ")))
c = 0

import time

calc_list = []
iterations = 0
class timer:
  def start_timer(duration):
    global end_time
    global start_time
    global continue_flag
    end_time = duration
    start_time = time.time()
  def continue_timer():
    global calc
    global start_time
    global iterations
    global calc_list
    global c
    timer = time.time() - start_time
    if timer>=end_time:
      calc_list.append(c)
      c = 0
      iterations+=1
      start_time = time.time()
      if iterations > 60:
        for i,v in enumerate(calc_list):
          print(f'Calculations per {end_time} seconds: '+str(calc_list[i]))
        exit()


timer.start_timer(duration=60)
while True:
  c += 1
  pick_numbers = []
  payout -= 1
  for i in range(15):
    pick_numbers.append(str(random.randint(0, 9)))
  if(lucky_numbers != pick_numbers):
    timer.continue_timer()
    print("Day", c, ":", *pick_numbers, "  ", len(str(c)),'  ')    
  if(lucky_numbers == pick_numbers):
    print("Day " + str(c) + " : " + str(pick_numbers), "green")
    payout += 50000
    wins += 1
    break
    time.sleep(1.99)
print("You won: $", payout)
print(wins)


