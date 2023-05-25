from tkinter import *

#window init
window = Tk()
window.wm_attributes('-fullscreen', True)
screenwidth = window.winfo_screenwidth()
screenheight = window.winfo_screenheight()

#style vars
bg_color = '#ffb35e'
game_area_bg = "#dd5521"

titleframe = LabelFrame(master=window, width = screenwidth, bg=bg_color)
titleframe.place(relx=.5,rely=.05,anchor="n")
titleframe.pack(fill="both", expand="yes")
title = Label(master=titleframe, text="Nonary Nonsense", bg=bg_color, font=("Ariel", 20, "bold"))
title.pack()

act_var=StringVar()
mes_var=StringVar()
def submit():
  action = act_var.get()
  message = mes_var.get()
  if(action == 'ENCRYPT'):
    encrypted_message = ''
    for v in message:
      nonary_v = []
      ordinal = ord(v)
      for i in range(3,-1,-1):
        nonary_v.append(ordinal // 9**i)
        ordinal = ordinal % 9**i
      for s, d in enumerate(nonary_v):
        nonary_v[s] = str(d)
      nonary_v = "".join(nonary_v)
      nonary_v = int(nonary_v)
      encrypted_message += chr(nonary_v)
    outputframe = Frame(window, bg="black")
    outputframe.pack(fill="both", expand="yes")
    output=Label(outputframe, text=f"{encrypted_message}", font=("Researcher", 10, "bold"), bg="black", fg="green")
    output.pack()
  
  if(action == 'DECRYPT'):
    decrypted_message = ''
    for v in message:
      ordinal_v = ord(v)
      new_ordinal = int(str(ordinal_v), 9)
      decrypted_message += chr(new_ordinal)
    outputframe = Frame(window, bg="black")
    outputframe.pack(fill="both", expand="yes")
    output=Label(outputframe, text=f"{decrypted_message}", font=("Researcher", 10, "bold"), bg="black", fg="green")
    output.pack()
    
    




entryframe = Frame(window, padx=15)
entryframe.pack()
action_label = Label(entryframe, text="Action: ", font=('calibre',10,'normal'))
action_entry = Entry(entryframe, textvariable = act_var, font=('calibre',10,'normal'))
message_label = Label(entryframe, text="Message: ", font=('calibre',10,'normal'))
message_entry = Entry(entryframe, textvariable = mes_var, font=('calibre',10,'normal'))
sub_btn = Button(entryframe, text="Submit", command = submit)
action_label.grid(row=0,column=0)
action_entry.grid(row=0,column=1)
message_label.grid(row=1, column=0)
message_entry.grid(row=1, column=1)
sub_btn.grid(row=1, column=3)

while True:
  window.update()
