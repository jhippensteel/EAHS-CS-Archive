# Jaysen Hippensteel
from tkinter import *
import time, statistics, random

#Window Init
window = Tk()
window.wm_attributes("-fullscreen", True)
screenwidth = window.winfo_screenwidth()
screenheight = window.winfo_screenheight()
window.configure(bg="#ff9b3d")
bg_color = "#ff9b3d"
#gui
#title
container = LabelFrame(master=window, relief="flat", bg=bg_color)
container.place(relx=.5,rely=.5,anchor="c")
title = Label(master=container, text="Taco Typer", font=("Ariel", 15, "bold"), padx=0, pady =10, bg=bg_color)
title.pack()
hint = Label(master=container, text="Turn On Volume To Hear ACII Bells", font=("Ariel",7), anchor="c", bg=bg_color, pady=0)
hint.pack()
player = "Player One"
player_lab = Label(master=container, text = f"{player}'s Turn", font=("Ariel", 7), anchor="c", bg=bg_color)
player_lab.pack()

def check_ans():
  if(response == words[chirps]):
    z = y-x
    player_one_score.append(round(z,1))
  else:
    mistakes += 1 
    for a in range(100):
      print("\a")
      time.sleep(0.01)
    if(mistakes < 3):
      time.sleep(2)
def taco_com():
  global y, response
  y = time.time()
  response = "Taco"
  check_ans()
def nacho_com():
  global y, response
  y = time.time()
  response = "Nacho"
  check_ans()
def churro_com():
  global y, response
  y = time.time()
  response = "Churro"
  check_ans()

player_one_score = []
player_two_score = []
words = ['Taco', 'Nacho', 'Churro']
mistakes = 0
while(mistakes < 3):
  chirps = random.randint(0,2)
  for i in range(chirps + 1):
    print("\a")
    time.sleep(0.25)
  x = time.time()
  player = "Player Two"
  window.update()

'''
print("Player Two's Turn:")
mistakes = 0


while(mistakes < 3):
  chirps = random.randint(0,2)
  for i in range(chirps + 1):
    print("\a")
    print("\n"*(3-(chirps+1)))
    time.sleep(0.25)
  x = time.time()
  response = str(input(">"))
  y=time.time()
  if(response == words[chirps]):
    z = y-x
    player_two_score.append(round(z,1))
  else:
    mistakes += 1 
    for a in range(100):
      print("\a")
      print(".")
      time.sleep(0.01)
    if(mistakes < 3):
      time.sleep(2)
if((len(player_one_score) < 2) and(len(player_two_score) < 2)):
  raise Exception("You both Suck And We're not even going to show your depressing score breakdown. Visit kindtiskewl.cf, and come back when you actually know how to play!!! You both lose")
elif (player_one_score == []):
  raise Exception("You Suck And We're not even going to show your depressing score breakdown. Visit kindtiskewl.cf, and come back when you actually know how to play!!!The other player wins.")
elif(player_two_score == []):
  raise Exception("You Suck And We're not even going to show your depressing score breakdown. Visit kindtiskewl.cf, and come back when you actually know how to play!!! The other player wins.")
player_one_points = len(player_one_score)
player_two_points = len(player_two_score)

player_one_min = min(player_one_score)
player_two_min = min(player_two_score)
if(player_one_min < player_two_min):
  player_one_points += 3
  player_one_min_points = 3
  player_two_min_points = 0
else:
  player_two_points += 3
  player_two_min_points = 3
  player_one_min_points = 0

player_one_max = max(player_one_score)
player_two_max = max(player_two_score)
if(player_one_max < player_two_max):
  player_one_points += 3
  player_one_max_points = 3
  player_two_max_points = 0
else:
  player_two_points += 3
  player_two_max_points = 3
  player_one_max_points = 0

player_one_mean = statistics.mean(player_one_score)
player_two_mean = statistics.mean(player_two_score)
if(player_one_mean < player_two_mean):
  player_one_points += 5
  player_one_mean_points = 3
  player_two_mean_points = 0
else:
  player_two_points += 5
  player_one_mean_points = 0
  player_two_mean_points = 3

player_one_median = statistics.median(player_one_score)
player_two_median = statistics.median(player_two_score)
if(player_one_median < player_two_median):
  player_one_points += 5
  player_one_median_points = 5
  player_two_median_points = 0
else:
  player_two_points += 5
  player_one_median_points = 0
  player_two_median_points = 5

player_one_dev = statistics.stdev(player_one_score)
player_two_dev = statistics.stdev(player_two_score)
if(player_one_dev < player_two_dev):
  player_one_points += 5
  player_one_dev_points = 5
  player_two_dev_points = 0
else:
  player_two_points += 5
  player_one_dev_points = 0
  player_two_dev_points = 5
player_one_mode = statistics.mode(player_one_score)
player_two_mode = statistics.mode(player_two_score)
player_one_mode = player_one_score.count(player_one_mode)
player_two_mode = player_two_score.count(player_two_mode)
if(player_one_mode != player_two_mode):
  if(player_one_mode < player_two_mode):
    player_one_points += 5
    player_one_mode_points = 5
    player_two_mode_points = 0
  else:
    player_two_points += 5
    player_one_mode_points = 0
    player_two_mode_points = 5
else:
  player_one_mode_points = 0
  player_two_mode_points = 0
print(f"Here's your score breakdown.\n\nPlayer 1:\nWords Correct: {len(player_one_score)} | Points Awarded: {len(player_one_score)}\nFastest Single Time: {player_one_min} | Points Awarded: {player_one_min_points}\nSlowest Time: {player_one_max} | Points Awarded: {player_one_max_points}\nAverage: {player_one_mean} | Points Awarded: {player_one_mean_points}\nMedian Score: {player_one_median} | Points Awarded: {player_one_median_points}\nConsistancy: {player_one_dev} | Points Awarded: {player_one_dev_points}\nMode Count: {player_one_mode} | Points Awarded: {player_one_mode_points}")
print()
print(f"Here's your score breakdown.\n\nPlayer 2:\nWords Correct: {len(player_two_score)} | Points Awarded: {len(player_two_score)}\nFastest Single Time: {player_two_min} | Points Awarded: {player_two_min_points}\nSlowest Time: {player_two_max} | Points Awarded: {player_two_max_points}\nAverage: {player_two_mean} | Points Awarded: {player_two_mean_points}\nMedian Score: {player_two_median} | Points Awarded: {player_two_median_points}\nConsistancy: {player_two_dev} | Points Awarded: {player_two_dev_points}\nMode Count: {player_two_mode} | Points Awarded: {player_two_mode_points}")

if(player_one_points == player_two_points):
  print("Congratulations, you both Win!")
elif(player_one_points > player_two_points):
  print("Congratulations player one, you win! Sorry player two.")
elif(player_two_points > player_one_points):
  print("Congratulations player two, you win! Sorry player one.")
'''