# Jaysen Hippensteel
#from menu import *
from tkinter import *
import random, time

#Window Init
window = Tk()
window.wm_attributes('-fullscreen', True)
screenwidth = window.winfo_screenwidth()
screenheight = window.winfo_screenheight()

team_var = StringVar()
name_var = StringVar()
###---FUNCS---###
def add_spec():
  def sub():
    name = name_var.get()
    team = team_var.get()
    teams[team].append(name)
  for widget in entryframe.winfo_children():
    widget.destroy()
  name_label = Label(entryframe, text="Name: ", bg="white")
  name_entry = Entry(entryframe, textvariable=name_var, font=('calibre',10,'normal'))
  team_label = Label(entryframe, text="Team Name (e.g red, green, blue): ", bg="white")
  team_entry = Entry(entryframe, textvariable=team_var, font=('calibre',10,'normal'))
  sub_btn = Button(entryframe, text = 'Submit', command=sub)
  name_label.grid(row=0,column=0)
  name_entry.grid(row=0,column=1)
  team_label.grid(row=1,column=0)
  team_entry.grid(row=1,column=1)
  sub_btn.grid(row=2,column=1)

def add_rand():
  def sub():
    name = name_var.get()
    teams[team].append(name)
  team = random.choice(list(teams.keys()))
  for widget in entryframe.winfo_children():
    widget.destroy()
  name_label=Label(entryframe, text="Name: ", bg="white")
  name_entry = Entry(entryframe, textvariable=name_var, font=('calibre',10,'normal'))
  sub_btn = Button(entryframe, text = 'Submit', command=sub)
  name_label.grid(row=0,column=0)
  name_entry.grid(row=0,column=1)
  sub_btn.grid(row=1,column=1)
  
def move_student():
  def sub():
    name = name_var.get()
    team = team_var.get()
    for k, v in teams.items():
      if(name in v):
        del teams[k][teams[k].index(name)]
        teams[team].append(name)
  for widget in entryframe.winfo_children():
    widget.destroy()
  name_label = Label(entryframe, text="Name: ", bg="white")
  name_entry = Entry(entryframe, textvariable=name_var, font=('calibre',10,'normal'))
  team_label = Label(entryframe, text="Team Name (e.g red, green, blue): ", bg="white")
  team_entry = Entry(entryframe, textvariable=team_var, font=('calibre',10,'normal'))
  sub_btn = Button(entryframe, text = 'Submit', command=sub)
  name_label.grid(row=0,column=0)
  name_entry.grid(row=0,column=1)
  team_label.grid(row=1,column=0)
  team_entry.grid(row=1,column=1)
  sub_btn.grid(row=2,column=1)

  
def del_student():
  def sub():
    name = name_var.get()
    for k, v in teams.items():
      if(name in v):
        del teams[k][teams[k].index(name)]
  for widget in entryframe.winfo_children():
    widget.destroy()
  name_label = Label(entryframe, text="Name: ", bg="white")
  name_entry = Entry(entryframe, font=('calibre',10,'normal'), textvariable=name_var)
  sub_btn = Button(entryframe, text="Submit", command=sub)
  name_label.grid(row=0,column=0)
  name_entry.grid(row=0,column=1)
  sub_btn.grid(row=1,column=1)

  
def rand_student():
  def sub():
    team = team_var.get()
    rando = random.choice(teams[team])
    display_lab = Label(entryframe, text=rando, font=('calibre',15,'normal'), bg="white")
    display_lab.grid(row=2,column=0)
  for widget in entryframe.winfo_children():
    widget.destroy()
  team_label = Label(entryframe, text="Team: ", bg="white")
  team_entry = Entry(entryframe, font=('calibre',10,'normal'), textvariable=team_var)
  sub_btn = Button(entryframe, text="Submit", command=sub)
  team_label.grid(row=0,column=0)
  team_entry.grid(row=0,column=1)
  sub_btn.grid(row=1,column=1)
  
def rand_studteam():
  for widget in entryframe.winfo_children():
    widget.destroy()
  team = random.choice(list(teams.keys()))
  name = random.choice(teams[team])
  display_lab = Label(entryframe, text=f"Student: {name}", font=('calibre',15,'normal'), padx=95, bg="white")
  display_lab.pack()
  
def rand_pair():
  for widget in entryframe.winfo_children():
    widget.destroy()
  captains = {}
  for k, v in teams.items():
    captains[k] = random.sample(v, k=2)
  cocaps = list(captains.values())
  display_lab = Label(entryframe, text=f"{cocaps[0][0]} and {cocaps[0][1]}\n{cocaps[1][0]} and {cocaps[1][1]}\n{cocaps[2][0]} and {cocaps[2][1]}", font=('calibre',15,'normal'), padx=95, bg="white")
  display_lab.pack()
  
def print_len():
  for widget in entryframe.winfo_children():
    widget.destroy()
  team_lens = {}
  for k, v in teams.items():
    team_lens[k] = len(v)
  for i in range(3):
    display_lab = Label(entryframe, text=f"{list(teams.keys())[i].title()}: {team_lens[list(teams.keys())[i]]}", font=('calibre',15,'normal'), padx=95, bg="white")
    display_lab.pack()
def display_rost():
  for widget in entryframe.winfo_children():
    widget.destroy()
  for k, v in teams.items():
    v2 = ", ".join(v)
    display_lab = Label(entryframe, text=f"{k.title()}: {v2}", font=('calibre',13,'normal'), padx=95, bg="white")
    display_lab.pack()
def quit_pro():
  entryframe.destroy()
  time.sleep(.25)
  radioframe.destroy()
  time.sleep(.25)
  window.destroy()
  time.sleep(.25)
  window2 = Tk()
  #Title Frame
  titleframe = LabelFrame(window2, bg=bg_color)
  titleframe.place(relx=.5, rely=.05, anchor="n")
  titleframe.pack(fill="both")
  #Title
  title = Label(titleframe, bg=bg_color, fg=txt_color, text="Goodbye!",font=("ariel",10,"bold"))
  title.pack()
  display_frame = LabelFrame(window2, bg="white")
  display_frame.pack(fill="both",expand="yes")
  for k, v in teams.items():
    v2 = ", ".join(v)
    display_lab = Label(display_frame, text=f"{k.title()}: {v2}", font=('calibre',6,'normal'), bg="white")
    display_lab.pack()
###---FUNCS---###



#Style Vars
bg_color = "blue"
txt_color = "white"

#Title Frame
titleframe = LabelFrame(window, bg=bg_color)
titleframe.place(relx=.5, rely=.05, anchor="n")
titleframe.pack(fill="both")
#Title
title = Label(titleframe, bg=bg_color, fg=txt_color, text="Hippie LMS",font=("ariel",25,"bold"))
title.pack()


flg = True
red_team = ["Allwein", "Bennett", "Campos", "D'Amour"]
blue_team = ["Enterline", "Ferris", "Gandel", "Harrison"]
green_team = ["Iriza", "Jankovich", "Kindt", "Lerch"]

teams = {
  "red":red_team, 
  "blue":blue_team, 
  "green":green_team
}

var = IntVar()
#Radio Buttons
topFrame = Frame(window, width=1350, height=500,bg="white")
topFrame.pack(side='top', fill=X, expand=1, anchor='n')

radioframe = Frame(topFrame, bd=5, bg="white")
radioframe.pack(side='left')
R1 = Radiobutton(radioframe, text="Add a new enrollment to a specific team", command=add_spec, bg="white", fg="blue", borderwidth=0, highlightthickness=0)
R2 = Radiobutton(radioframe, text="Add a new enrollment to a random team", command=add_rand, bg="white", fg="blue", borderwidth=0, highlightthickness=0)
R3 = Radiobutton(radioframe, text="Move a student from one team to another", command=move_student, bg="white", fg="blue", borderwidth=0, highlightthickness=0)
R4 = Radiobutton(radioframe, text="Remove/delete an athlete from the club completely", command=del_student, bg="white", fg="blue", borderwidth=0, highlightthickness=0)
R5 = Radiobutton(radioframe, text="Randomly select an athlete from a selected team", command = rand_student, bg="white", fg="blue", borderwidth=0, highlightthickness=0)
R6 = Radiobutton(radioframe, text="Randomly select an athlete from any team", command=rand_studteam, bg="white", fg="blue", borderwidth=0, highlightthickness=0)
R7 = Radiobutton(radioframe, text="Randomly select co-captains for all teams", command=rand_pair, bg="white", fg="blue", borderwidth=0, highlightthickness=0)
R8 = Radiobutton(radioframe, text="Display the number of students in each team", command=print_len, bg="white", fg="blue", borderwidth=0, highlightthickness=0)
R9 = Radiobutton(radioframe, text="Display team color and roster", command=display_rost, bg="white", fg="blue", borderwidth=0, highlightthickness=0)
R0 = Radiobutton(radioframe, text="Quit program and display team rosters", command=quit_pro, bg="white", fg="blue", borderwidth=0, highlightthickness=0)
R1.pack()
R2.pack()
R3.pack()
R4.pack()
R5.pack()
R6.pack()
R7.pack()
R8.pack()
R9.pack()
R0.pack()
entryframe = Frame(topFrame, width=500, height=100, bd=4, bg="white")
entryframe.pack(side='right')






'''
print("\033c")
if(action == 1):
  add_spec(teams)
if(action == 2):
  add_rand(teams, list(teams.keys()))
if(action == 3):
  move_student(teams)
if(action == 4):
  del_student(teams)
if(action == 5):
  print(rand_student(teams))
if(action == 6):
    print(rand_studteam(teams))
if(action == 7):
  print(*rand_pair(teams), sep = "\n")
if(action == 8):
  team_lens = {}
  print_len(teams, team_lens)
  for k, v in team_lens.items():
    print(k +":", v)
if(action == 9):
  for k, v in teams.items():
    print(k+": ",end="")
    print(*v,sep=", ")
if(action == 0 or action == 10):
  flg = False

for k, v in teams.items():
  print(k+": ",end="")
  print(*v,sep=", ")
'''
while True:
  window.mainloop()