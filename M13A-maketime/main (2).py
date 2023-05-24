#Jaysen Hippensteel. M13A project
import sys, os, time, random
from termcolor import colored, cprint

cprint("Welcome to MasterMind: Easy to Learn, Easy to play, Not so Easy to Win", attrs = ["bold", "underline"])#Introduction
help = str(input("\nDo you need directions (yes/no): "))#User decides whether or not to read directions

help = help[0].lower()

if(help == "y"):#outputs directions if user indicates
  print()
  print("When You start the game, the computer will randomly devise a code. How many digits or weather there are repeats in that code will depend on what skill level you choose (if you are reading these directions we reccomend you choose Novice)")#prints directions
  print()
  print("Your job is to guess that code in a certain amount of tries (amount of tries once again depend on skill level)")
  print()
  

  print("When you input a guess, the computer will output several K's or W's, a K represents a right digit in the wrong place, while a W represents a right digit in the right place.")
  print()
  print("When you choose novice, prompts will guide you along as you play")
  print()

  end_help = str(input("Ready to start: "))#aks user if they are ready to start game
  end_help[0].lower()

  if(end_help == "y"):
    os.system("clear")#clears screen if user starts game

  else:
    print("#"*60)

    time.sleep(1)

    print("Here, we will show you an example.")
    print()#outputs an example to user

    help_ex_1 = "Here is the computer's secret code:"
    help_ex_code_1 = "3 4 6 5"

    time.sleep(1)
    print(help_ex_1.ljust(45), help_ex_code_1)
    
    print("_"*60)
    
    print()

    help_ex_2 = "And here is what the code-breaker guessed:"
    help_ex_code_2 = "4 2 6 8"
    
    print(help_ex_2.ljust(45), help_ex_code_2)

    time.sleep(2)
    
    print()
    print("This is the computer's response: W K")
    print()

    time.sleep(1)
    
    print("This means that code-breaker got one correct digit that was in the wrong place (the 4 was corect, but it should have been the second digit) and the code breaker got one correct digit in the correct place (the 6 was in exactly the right spot)")
    
    time.sleep(1.5)#adds delay between directions for organization

    print()
    print("If the code-breaker's response was 3 4 6 5, then the computer's response would be K K K K because the code-breaker got all the correct digits in the correct location")

    time.sleep(1.5)

    print()
    print("If the codebreaker's response was 5 6 4 3, then the computer's response would be W W W W, because the code-breaker got all the correct digits in all the wrong places.")

    print()

    end_help_2 = str(input("Ready now (Y or N): "))

    if(end_help_2 == "Y"):
      time.sleep(1)
      os.system("clear")

    if(end_help_2 == "N"):
      print()
      print("Error: No more directions!")

      time.sleep(10)
      os.system("clear")
else:
  os.system("clear")

game_set = int(input("How many games would you like to play: "))
wins = 0

for c in range(game_set):

  level = str(input("\nWhat skill level are you (Novice, Skilled, or Mastermind): "))
  level = level[0].lower()


  ####################################################################################################################


  if(level == "n"):#Novice Level
    tries = 0
    w = 0
    k = 0

    random_number = [c for c in range(1, 10)]#finds non-repetitive numbers between 1 and 10 not including 10
    random.shuffle(random_number) #shuffles list of random numbers

    digit_1 = str(random_number[0])
    digit_2 = str(random_number[1])
    digit_3 = str(random_number[2])
    digit_4 = str(random_number[3])
    code = digit_1 + " " + digit_2 + " " + digit_3 + " " + digit_4
    
    output = ""

    #print(code)
    text = colored("This code must be a four digit number, no repeats, and all positive integers between 1 and 9 (including 9)\n", "blue")
    dotted_line = ("."*80)
    log = text + dotted_line
    print(log)


    while(w < 4):#begins a loop
      guess = str(input("\nWhat is your guess: "))
      guess_mod = guess.replace(" ", "")
      
      log = log + "\n\nWhat is your guess: " + guess
      tries += 1
      w = 0
      k = 0
      output = ""

      if(digit_1 == guess_mod[0]):
        w += 1
        output = output + "W"

        guess_mod = list(guess_mod)
        guess_mod[0] = "#"
        guess_mod = str(guess_mod[0] + guess_mod[1] + guess_mod[2] + guess_mod[3])
      
      if(digit_2 == guess_mod[1]):
        w += 1
        output = output + "W"

        guess_mod = list(guess_mod)
        guess_mod[1] = "#"
        guess_mod = str(guess_mod[0] + guess_mod[1] + guess_mod[2] + guess_mod[3])
      
      if(digit_3 == guess_mod[2]):
        w += 1
        output = output + "W"

        guess_mod = list(guess_mod)
        guess_mod[2] = "#"
        guess_mod = str(guess_mod[0] + guess_mod[1] + guess_mod[2] + guess_mod[3])
      
      if(digit_4 == guess_mod[3]):
        w += 1
        output = output + "W"

        guess_mod = list(guess_mod)
        guess_mod[3] = "#"
        guess_mod = str(guess_mod[0] + guess_mod[1] + guess_mod[2] + guess_mod[3])

      if(w == 4):
        print("\nCongradulations, you cracked the code in", tries, "tries")
        #break#breaks loop if user cracks code

      if(digit_1 == guess_mod[1]):
        output = output + "K"
        k += 1

        guess_mod = list(guess_mod)
        guess_mod[1] = "#"
        guess_mod = str(guess_mod[0] + guess_mod[1] + guess_mod[2] + guess_mod[3])
      
      if(digit_1 == guess_mod[2]):
        output = output + "K"
        k += 1

        guess_mod = list(guess_mod)
        guess_mod[2] = "#"
        guess_mod = str(guess_mod[0] + guess_mod[1] + guess_mod[2] + guess_mod[3])
      
      if(digit_1 == guess_mod[3]):
        output = output + "K"
        k += 1
        
        guess_mod = list(guess_mod)
        guess_mod[3] = "#"
        guess_mod = str(guess_mod[0] + guess_mod[1] + guess_mod[2] + guess_mod[3])
      if(digit_2 == guess_mod[0]):
        output = output + "K"
        k += 1

        guess_mod = list(guess_mod)
        guess_mod[0] = "#"
        guess_mod = str(guess_mod[0] + guess_mod[1] + guess_mod[2] + guess_mod[3])
      if(digit_2 == guess_mod[2]):
        output = output + "K"
        k += 1

        guess_mod = list(guess_mod)
        guess_mod[2] = "#"
        guess_mod = str(guess_mod[0] + guess_mod[1] + guess_mod[2] + guess_mod[3])
      if(digit_2 == guess_mod[3]):
        output = output + "K"
        k += 1

        guess_mod = list(guess_mod)
        guess_mod[3] = "#"
        guess_mod = str(guess_mod[0] + guess_mod[1] + guess_mod[2] + guess_mod[3])

      if(digit_3 == guess_mod[0]):
        output = output + "K"
        k += 1

        guess_mod = list(guess_mod)
        guess_mod[0] = "#"
        guess_mod = str(guess_mod[0] + guess_mod[1] + guess_mod[2] + guess_mod[3])
      if(digit_3 == guess_mod[1]):
        output = output + "K"
        k += 1

        guess_mod = list(guess_mod)
        guess_mod[1] = "#"
        guess_mod = str(guess_mod[0] + guess_mod[1] + guess_mod[2] + guess_mod[3])
      if(digit_3 == guess_mod[3]):
        output = output + "K"
        k += 1

        guess_mod = list(guess_mod)
        guess_mod[3] = "#"
        guess_mod = str(guess_mod[0] + guess_mod[1] + guess_mod[2] + guess_mod[3])

      if(digit_4 == guess_mod[0]):
        output = output + "K"
        k += 1

        guess_mod = list(guess_mod)
        guess_mod[0] = "#"
        guess_mod = str(guess_mod[0] + guess_mod[1] + guess_mod[2] + guess_mod[3])
      if(digit_4 == guess_mod[1]):
        output = output + "K"
        k += 1

        guess_mod = list(guess_mod)
        guess_mod[1] = "#"
        guess_mod = str(guess_mod[0] + guess_mod[1] + guess_mod[2] + guess_mod[3])
      if(digit_4 == guess_mod[2]):
        output = output + "K"
        k += 1

        guess_mod = list(guess_mod)
        guess_mod[2] = "#"
        guess_mod = str(guess_mod[0] + guess_mod[1] + guess_mod[2] + guess_mod[3])
      
      log = log + " | " + output
      os.system("clear")
      print(log)
      
      if(k == 0 and w == 0 and tries > 1):
        log_2 = log + "\n\nTry using a whole new set of numbers"

        os.system("clear")
        print(log_2)

      elif(k == 4 and tries > 1):
        log_2 = log + "\n\nTry shuffling your code"

        os.sytem("clear")
        print(log_2)
      
      
      if(tries >= 20):
        bad_exit = "\nThis is Novice level, come on man, you ran out of tries! The code was " + str(code)
        cprint(bad_exit, "red")
        break#breaks loop if user runs out of tries
      if(w >= 4):
        cprint("\nCongradulations, you broke the code! Maybe you should move on to the Skilled level.", "green")
        wins += 1
        break
      if(tries == 1 and w < 4):
        log_2 = log + "\n\nYou have 19 more tries\n\nIf you have many K's, you might want to try shuffling your digits, and you might want to try completely new numbers one digit at a time"

        os.system("clear")
        print(log_2)
      

  if(level == "s"):#Skilled Level
    tries = 0
    w = 0
    k = 0

    digit_1 = str(random.randint(1, 9))
    digit_2 = str(random.randint(1, 9))
    digit_3 = str(random.randint(1, 9))
    digit_4 = str(random.randint(1, 9))
    #'''
    code = digit_1 + " " + digit_2 + " " + digit_3 + " " + digit_4
    # '''
    digit_1b = digit_1#creates a copy of computer code
    digit_2b = digit_2
    digit_3b = digit_3
    digit_4b = digit_4

    user_note1 = colored("\nThis code has a possibility of repeat digits that are integers from 1 to 9.\n\nIf you repeat a number in your guess, a K will only be output if each the digit in your guess corresponds with a digit in the code", "blue")#note to user
    dotted_line = ("."*80)
    log = user_note1 + "\n" + dotted_line
    os.system("clear")
    print(log)

    
    while(w < 4):
      guess = str(input("\nWhat is your guess: "))
      guess_mod = guess.replace(" ", "")

      log = log + "\n\nWhat is your guess: " + guess
      w = 0
      k = 0
      tries += 1
      output = ""

      digit_1b = digit_1
      digit_2b = digit_2
      digit_3b = digit_3
      digit_4b = digit_4

      if(digit_1 == guess_mod[0]):#tests first digit of user's guess against computer code
        w += 1#adds 1 to "w" counter
        digit_1b = "*"#makes copy of digit 1 become void of test criteria/ prevents repeat k's
        
        guess_mod = list(guess_mod)
        guess_mod[0] = "#"
        guess_mod = str(guess_mod[0] + guess_mod[1] + guess_mod[2] + guess_mod[3])
        
        output = output + "W"#adds w to output string
      
      
      if(digit_2 == guess_mod[1]):
        w += 1
        digit_2b = "*"
        
        guess_mod = list(guess_mod)
        guess_mod[1] = "#"
        guess_mod = str(guess_mod[0] + guess_mod[1] + guess_mod[2] + guess_mod[3])
        
        output = output + "W"
      
      
      if(digit_3 == guess_mod[2]):
        w += 1
        digit_3b = "*"

        guess_mod = list(guess_mod)
        guess_mod[2] = "#"
        guess_mod = str(guess_mod[0] + guess_mod[1] + guess_mod[2] + guess_mod[3])
        
        output = output + "W"
      
      
      if(digit_4 == guess_mod[3]):
        w += 1
        digit_4b = "*"
        
        guess_mod = list(guess_mod)
        guess_mod[3] = "#"
        guess_mod = str(guess_mod[0] + guess_mod[1] + guess_mod[2] + guess_mod[3])
        
        output = output + "W"
      
      ###End of direct placement testing###
      
      if(digit_2b == guess_mod[0]):#priority testing
        output = output + "K"#adds k to output
        digit_2b = "*"#makes copy of digit 2 become void

        guess_mod = list(guess_mod)
        guess_mod[0] = "#"
        guess_mod = str(guess_mod[0] + guess_mod[1] + guess_mod[2] + guess_mod[3])
        
        k += 1#adds 1 to "k" counter
      
      
      elif(digit_3b == guess_mod[0]):
        output = output + "K"
        digit_3b = "*"

        guess_mod = list(guess_mod)
        guess_mod[0] = "#"
        guess_mod = str(guess_mod[0] + guess_mod[1] + guess_mod[2] + guess_mod[3])
        
        k += 1
      
      
      elif(digit_4b == guess_mod[0]):
        output = output + "K"
        digit_4b = "*"

        guess_mod = list(guess_mod)
        guess_mod[0] = "#"
        guess_mod = str(guess_mod[0] + guess_mod[1] + guess_mod[2] + guess_mod[3])
        
        k += 1
      
      ###End of first guess digit testing###

      if(digit_1b == guess_mod[1]):
        output = output + "K"
        digit_1b = "*"

        guess_mod = list(guess_mod)
        guess_mod[1] = "#"
        guess_mod = str(guess_mod[0] + guess_mod[1] + guess_mod[2] + guess_mod[3])
        
        k += 1
      
      elif(digit_3b == guess_mod[1]):
        output = output + "K"
        digit_3b = "*"
        
        guess_mod = list(guess_mod)
        guess_mod[1] = "#"
        guess_mod = str(guess_mod[0] + guess_mod[1] + guess_mod[2] + guess_mod[3])
        
        k += 1
      
      elif(digit_4b == guess_mod[1]):
        output = output + "K"
        digit_4b = "*"

        guess_mod = list(guess_mod)
        guess_mod[1] = "#"
        guess_mod = str(guess_mod[0] + guess_mod[1] + guess_mod[2] + guess_mod[3])
        
        k += 1

      ###End of second guess digit testing###

      if(digit_1b == guess_mod[2]):
        output = output + "K"
        digit_1b = "*"

        guess_mod = list(guess_mod)
        guess_mod[2] = "#"
        guess_mod = str(guess_mod[0] + guess_mod[1] + guess_mod[2] + guess_mod[3])
        
        k += 1
      
      elif(digit_2b == guess_mod[2]):
        output = output + "K"
        digit_2b = "*"

        guess_mod = list(guess_mod)
        guess_mod[2] = "#"
        guess_mod = str(guess_mod[0] + guess_mod[1] + guess_mod[2] + guess_mod[3])
        
        k += 1
      
      elif(digit_4b == guess_mod[2]):
        output = output + "K"
        digit_4b = "*"

        guess_mod = list(guess_mod)
        guess_mod[2] = "#"
        guess_mod = str(guess_mod[0] + guess_mod[1] + guess_mod[2] + guess_mod[3])
        
        k += 1

      ###End of third digit testing###

      if(digit_1b == guess_mod[3]):
        output = output + "K"
        digit_1b = "*"

        guess_mod = list(guess_mod)
        guess_mod[3] = "#"
        guess_mod = str(guess_mod[0] + guess_mod[1] + guess_mod[2] + guess_mod[3])
        
        k += 1
      
      elif(digit_2b == guess_mod[3]):
        output = output + "K"
        digit_2b = "*"

        guess_mod = list(guess_mod)
        guess_mod[2] = "#"
        guess_mod = str(guess_mod[0] + guess_mod[1] + guess_mod[2] + guess_mod[3])
        
        k += 1
      
      elif(digit_3b == guess_mod[3]):
        output = output + "K"
        digit_3b = "*"

        guess_mod = list(guess_mod)
        guess_mod[2] = "#"
        guess_mod = str(guess_mod[0] + guess_mod[1] + guess_mod[2] + guess_mod[3])
        k += 1

      ###End of fourth digit testing###
      ###End of testing###

      sorted_characters = sorted(output)
      output = " ".join(sorted_characters)
      log = log + " | " + output

      os.system("clear")
      print(log)
        
      if(w >= 4):
        good_exit = "\nCongradulations, you cracked the code in " + str(tries) + " tries"
        cprint(good_exit, "green")
        wins += 1
        break#ends loop if user repeats code
      if(tries >= 15):
        bad_exit = "Sorry, you ran out of tries! The code was " + str(code)
        cprint(bad_exit, "red")

        break#breaks loop if user runs out of tries

  if(level == "m"):#Mastermind Level
    tries = 0
    w = 0
    k = 0
    output = ""

    digit_1 = str(random.randint(0, 9))
    digit_2 = str(random.randint(0, 9))
    digit_3 = str(random.randint(0, 9))
    digit_4 = str(random.randint(0, 9))
    digit_5 = str(random.randint(0, 9))
    digit_6 = str(random.randint(0, 9))
    digit_7 = str(random.randint(0, 9))
    digit_8 = str(random.randint(0, 9))
    #'''
    code = digit_1 + " " + digit_2 + " " + digit_3 + " " + digit_4 + " " + digit_5 + " " + digit_6 + " " + digit_7 + " " + digit_8
    # '''
    digit_1b = digit_1#creates a copy of computer code
    digit_2b = digit_2
    digit_3b = digit_3
    digit_4b = digit_4
    digit_5b = digit_5
    digit_6b = digit_6
    digit_7b = digit_7
    digit_8b = digit_8

    user_note1 = colored("This code has a possibility of repeat digits that are integers from 0 to 9.\n\nIf you repeat a number in your guess, a K will only be output if each the digit in your guess corresponds with a digit in the code. There are 8 digits in this code.", "blue")#note to user
    dotted_line = ("."*80)

    log = "\n" + user_note1 + "\n" + dotted_line
    os.system("clear")
    print(log)

    while(w < 8):

      guess = str(input("\nWhat is your guess: "))
      guess_mod = guess.replace(" ", "")
      w = 0
      k = 0
      tries += 1
      output = ""
      log = log + "\n\n" + "What is your guess: " + guess

      digit_1b = digit_1#creates a copy of computer code
      digit_2b = digit_2
      digit_3b = digit_3
      digit_4b = digit_4
      digit_5b = digit_5
      digit_6b = digit_6
      digit_7b = digit_7
      digit_8b = digit_8

      if(digit_1 == guess_mod[0]):#tests first digit of user's guess against computer code
        w += 1#adds 1 to "w" counter
        digit_1b = "*"#makes copy of digit 1 become void of test criteria/ prevents repeat k's

        guess_mod = list(guess_mod)
        guess_mod[0] = "#"
        guess_mod = str(guess_mod[0] + guess_mod[1] + guess_mod[2] + guess_mod[3] + guess_mod[4] + guess_mod[5] + guess_mod[6] + guess_mod[7])

        output = output + "W"#adds w to output string
      elif(digit_2b == guess_mod[0]):#priority testing
        output = output + "K"#adds k to output
        digit_2b = "*"#makes copy of digit 2 become void

        guess_mod = list(guess_mod)
        guess_mod[0] = "#"
        guess_mod = str(guess_mod[0] + guess_mod[1] + guess_mod[2] + guess_mod[3] + guess_mod[4] + guess_mod[5] + guess_mod[6] + guess_mod[7])
        
        k += 1#adds 1 to "k" counter
      elif(digit_3b == guess_mod[0]):
        output = output + "K"
        digit_3b = "*"

        guess_mod = list(guess_mod)
        guess_mod[0] = "#"
        guess_mod = str(guess_mod[0] + guess_mod[1] + guess_mod[2] + guess_mod[3] + guess_mod[4] + guess_mod[5] + guess_mod[6] + guess_mod[7])
        
        k += 1
      elif(digit_4b == guess_mod[0]):
        output = output + "K"
        digit_4b = "*"

        guess_mod = list(guess_mod)
        guess_mod[0] = "#"
        guess_mod = str(guess_mod[0] + guess_mod[1] + guess_mod[2] + guess_mod[3] + guess_mod[4] + guess_mod[5] + guess_mod[6] + guess_mod[7])
        
        k += 1
      elif(digit_5b == guess_mod[0]):
        output = output + "K"
        digit_5b = "*"

        guess_mod = list(guess_mod)
        guess_mod[0] = "#"
        guess_mod = str(guess_mod[0] + guess_mod[1] + guess_mod[2] + guess_mod[3] + guess_mod[4] + guess_mod[5] + guess_mod[6] + guess_mod[7])
        
        k += 1
      elif(digit_6b == guess_mod[0]):
        output = output + "K"
        digit_6b = "*"

        guess_mod = list(guess_mod)
        guess_mod[0] = "#"
        guess_mod = str(guess_mod[0] + guess_mod[1] + guess_mod[2] + guess_mod[3] + guess_mod[4] + guess_mod[5] + guess_mod[6] + guess_mod[7])
        
        k += 1
      elif(digit_7b == guess_mod[0]):
        output = output + "K"
        digit_7b = "*"

        guess_mod = list(guess_mod)
        guess_mod[0] = "#"
        guess_mod = str(guess_mod[0] + guess_mod[1] + guess_mod[2] + guess_mod[3] + guess_mod[4] + guess_mod[5] + guess_mod[6] + guess_mod[7])
        
        k += 1
      elif(digit_8b == guess_mod[0]):
        output = output + "K"
        digit_8b = "*"

        guess_mod = list(guess_mod)
        guess_mod[0] = "#"
        guess_mod = str(guess_mod[0] + guess_mod[1] + guess_mod[2] + guess_mod[3] + guess_mod[4] + guess_mod[5] + guess_mod[6] + guess_mod[7])
        
        k += 1

      if(digit_2 == guess_mod[1]):
        w += 1
        digit_2b = "*"

        guess_mod = list(guess_mod)
        guess_mod[1] = "#"
        guess_mod = str(guess_mod[0] + guess_mod[1] + guess_mod[2] + guess_mod[3] + guess_mod[4] + guess_mod[5] + guess_mod[6] + guess_mod[7])
        
        output = output + "W"
      elif(digit_1b == guess_mod[1]):
        output = output + "K"
        digit_1b = "*"

        guess_mod = list(guess_mod)
        guess_mod[1] = "#"
        guess_mod = str(guess_mod[0] + guess_mod[1] + guess_mod[2] + guess_mod[3] + guess_mod[4] + guess_mod[5] + guess_mod[6] + guess_mod[7])
        
        k += 1
      elif(digit_3b == guess_mod[1]):
        output = output + "K"
        digit_3b = "*"

        guess_mod = list(guess_mod)
        guess_mod[1] = "#"
        guess_mod = str(guess_mod[0] + guess_mod[1] + guess_mod[2] + guess_mod[3] + guess_mod[4] + guess_mod[5] + guess_mod[6] + guess_mod[7])
        
        k += 1
      elif(digit_4b == guess_mod[1]):
        output = output + "K"
        digit_4b = "*"

        guess_mod = list(guess_mod)
        guess_mod[1] = "#"
        guess_mod = str(guess_mod[0] + guess_mod[1] + guess_mod[2] + guess_mod[3] + guess_mod[4] + guess_mod[5] + guess_mod[6] + guess_mod[7])
        
        k += 1
      elif(digit_5b == guess_mod[1]):
        output = output + "K"
        digit_5b = "*"

        guess_mod = list(guess_mod)
        guess_mod[1] = "#"
        guess_mod = str(guess_mod[0] + guess_mod[1] + guess_mod[2] + guess_mod[3] + guess_mod[4] + guess_mod[5] + guess_mod[6] + guess_mod[7])
      
        k += 1
      elif(digit_6b == guess_mod[1]):
        output = output + "K"
        digit_6b = "*"

        guess_mod = list(guess_mod)
        guess_mod[1] = "#"
        guess_mod = str(guess_mod[0] + guess_mod[1] + guess_mod[2] + guess_mod[3] + guess_mod[4] + guess_mod[5] + guess_mod[6] + guess_mod[7])
        
        k += 1
      elif(digit_7b == guess_mod[1]):
        output = output + "K"
        digit_7b = "*"

        guess_mod = list(guess_mod)
        guess_mod[1] = "#"
        guess_mod = str(guess_mod[0] + guess_mod[1] + guess_mod[2] + guess_mod[3] + guess_mod[4] + guess_mod[5] + guess_mod[6] + guess_mod[7])
      
        k += 1
      elif(digit_8b == guess_mod[1]):
        output = output + "K"
        digit_8b = "*"

        guess_mod = list(guess_mod)
        guess_mod[1] = "#"
        guess_mod = str(guess_mod[0] + guess_mod[1] + guess_mod[2] + guess_mod[3] + guess_mod[4] + guess_mod[5] + guess_mod[6] + guess_mod[7])
        
        k += 1

      if(digit_3 == guess_mod[2]):
        w += 1
        digit_3b = "*"

        guess_mod = list(guess_mod)
        guess_mod[2] = "#"
        guess_mod = str(guess_mod[0] + guess_mod[1] + guess_mod[2] + guess_mod[3] + guess_mod[4] + guess_mod[5] + guess_mod[6] + guess_mod[7])
        
        output = output + "W"
      elif(digit_1b == guess_mod[2]):
        output = output + "K"

        guess_mod = list(guess_mod)
        guess_mod[2] = "#"
        guess_mod = str(guess_mod[0] + guess_mod[1] + guess_mod[2] + guess_mod[3] + guess_mod[4] + guess_mod[5] + guess_mod[6] + guess_mod[7])
        
        digit_1b = "*"
        k += 1
      elif(digit_2b == guess_mod[2]):
        output = output + "K"
        digit_2b = "*"

        guess_mod = list(guess_mod)
        guess_mod[2] = "#"
        guess_mod = str(guess_mod[0] + guess_mod[1] + guess_mod[2] + guess_mod[3] + guess_mod[4] + guess_mod[5] + guess_mod[6] + guess_mod[7])
        
        k += 1
      elif(digit_4b == guess_mod[2]):
        output = output + "K"
        digit_4b = "*"

        guess_mod = list(guess_mod)
        guess_mod[2] = "#"
        guess_mod = str(guess_mod[0] + guess_mod[1] + guess_mod[2] + guess_mod[3] + guess_mod[4] + guess_mod[5] + guess_mod[6] + guess_mod[7])
        
        k += 1
      elif(digit_5b == guess_mod[2]):
        output = output + "K"
        digit_5b = "*"

        guess_mod = list(guess_mod)
        guess_mod[2] = "#"
        guess_mod = str(guess_mod[0] + guess_mod[1] + guess_mod[2] + guess_mod[3] + guess_mod[4] + guess_mod[5] + guess_mod[6] + guess_mod[7])
        
        k += 1
      elif(digit_6b == guess_mod[2]):
        output = output + "K"
        digit_6b = "*"

        guess_mod = list(guess_mod)
        guess_mod[2] = "#"
        guess_mod = str(guess_mod[0] + guess_mod[1] + guess_mod[2] + guess_mod[3] + guess_mod[4] + guess_mod[5] + guess_mod[6] + guess_mod[7])
        
        k += 1
      elif(digit_7b == guess_mod[2]):
        output = output + "K"
        digit_7b = "*"

        guess_mod = list(guess_mod)
        guess_mod[2] = "#"
        guess_mod = str(guess_mod[0] + guess_mod[1] + guess_mod[2] + guess_mod[3] + guess_mod[4] + guess_mod[5] + guess_mod[6] + guess_mod[7])
        
        k += 1
      elif(digit_8b == guess_mod[2]):
        output = output + "K"
        digit_8b = "*"

        guess_mod = list(guess_mod)
        guess_mod[2] = "#"
        guess_mod = str(guess_mod[0] + guess_mod[1] + guess_mod[2] + guess_mod[3] + guess_mod[4] + guess_mod[5] + guess_mod[6] + guess_mod[7])
        
        k += 1
      
      if(digit_4 == guess_mod[3]):
        w += 1
        digit_2b = "*"

        guess_mod = list(guess_mod)
        guess_mod[3] = "#"
        guess_mod = str(guess_mod[0] + guess_mod[1] + guess_mod[2] + guess_mod[3] + guess_mod[4] + guess_mod[5] + guess_mod[6] + guess_mod[7])
        
        output = output + "W"
      elif(digit_1b == guess_mod[3]):
        output = output + "K"
        digit_1b = "*"

        guess_mod = list(guess_mod)
        guess_mod[3] = "#"
        guess_mod = str(guess_mod[0] + guess_mod[1] + guess_mod[2] + guess_mod[3] + guess_mod[4] + guess_mod[5] + guess_mod[6] + guess_mod[7])
        
        k += 1
      elif(digit_2b == guess_mod[3]):
        output = output + "K"
        digit_2b = "*"

        guess_mod = list(guess_mod)
        guess_mod[3] = "#"
        guess_mod = str(guess_mod[0] + guess_mod[1] + guess_mod[2] + guess_mod[3] + guess_mod[4] + guess_mod[5] + guess_mod[6] + guess_mod[7])
        
        k += 1
      elif(digit_3b == guess_mod[3]):
        output = output + "K"
        digit_3b = "*"

        guess_mod = list(guess_mod)
        guess_mod[3] = "#"
        guess_mod = str(guess_mod[0] + guess_mod[1] + guess_mod[2] + guess_mod[3] + guess_mod[4] + guess_mod[5] + guess_mod[6] + guess_mod[7])
        
        k += 1
      elif(digit_5b == guess_mod[3]):
        output = output + "K"
        digit_5b = "*"

        guess_mod = list(guess_mod)
        guess_mod[3] = "#"
        guess_mod = str(guess_mod[0] + guess_mod[1] + guess_mod[2] + guess_mod[3] + guess_mod[4] + guess_mod[5] + guess_mod[6] + guess_mod[7])
        
        k += 1
      elif(digit_6b == guess_mod[3]):
        output = output + "K"
        digit_6b = "*"

        guess_mod = list(guess_mod)
        guess_mod[3] = "#"
        guess_mod = str(guess_mod[0] + guess_mod[1] + guess_mod[2] + guess_mod[3] + guess_mod[4] + guess_mod[5] + guess_mod[6] + guess_mod[7])
        
        k += 1
      elif(digit_7b == guess_mod[3]):
        output = output + "K"
        digit_7b = "*"

        guess_mod = list(guess_mod)
        guess_mod[3] = "#"
        guess_mod = str(guess_mod[0] + guess_mod[1] + guess_mod[2] + guess_mod[3] + guess_mod[4] + guess_mod[5] + guess_mod[6] + guess_mod[7])
        
        k += 1
      elif(digit_8b == guess_mod[3]):
        output = output + "K"
        digit_8b = "*"

        guess_mod = list(guess_mod)
        guess_mod[3] = "#"
        guess_mod = str(guess_mod[0] + guess_mod[1] + guess_mod[2] + guess_mod[3] + guess_mod[4] + guess_mod[5] + guess_mod[6] + guess_mod[7])
        
        k += 1
      
      if(digit_5 == guess_mod[4]):
        w += 1
        digit_5b = "*"

        guess_mod = list(guess_mod)
        guess_mod[4] = "#"
        guess_mod = str(guess_mod[0] + guess_mod[1] + guess_mod[2] + guess_mod[3] + guess_mod[4] + guess_mod[5] + guess_mod[6] + guess_mod[7])
        
        output = output + "W"
      elif(digit_1b == guess_mod[4]):
        output = output + "K"
        digit_1b = "*"

        guess_mod = list(guess_mod)
        guess_mod[4] = "#"
        guess_mod = str(guess_mod[0] + guess_mod[1] + guess_mod[2] + guess_mod[3] + guess_mod[4] + guess_mod[5] + guess_mod[6] + guess_mod[7])
        
        k += 1
      elif(digit_2b == guess_mod[4]):
        output = output + "K"
        digit_2b = "*"

        guess_mod = list(guess_mod)
        guess_mod[4] = "#"
        guess_mod = str(guess_mod[0] + guess_mod[1] + guess_mod[2] + guess_mod[3] + guess_mod[4] + guess_mod[5] + guess_mod[6] + guess_mod[7])
        
        k += 1
      elif(digit_3b == guess_mod[4]):
        output = output + "K"
        digit_3b = "*"

        guess_mod = list(guess_mod)
        guess_mod[4] = "#"
        guess_mod = str(guess_mod[0] + guess_mod[1] + guess_mod[2] + guess_mod[3] + guess_mod[4] + guess_mod[5] + guess_mod[6] + guess_mod[7])
        
        k += 1
      elif(digit_4b == guess_mod[4]):
        output = output + "K"
        digit_4b = "*"

        guess_mod = list(guess_mod)
        guess_mod[4] = "#"
        guess_mod = str(guess_mod[0] + guess_mod[1] + guess_mod[2] + guess_mod[3] + guess_mod[4] + guess_mod[5] + guess_mod[6] + guess_mod[7])
        
        k += 1
      elif(digit_6b == guess_mod[4]):
        output = output + "K"
        digit_6b = "*"

        guess_mod = list(guess_mod)
        guess_mod[4] = "#"
        guess_mod = str(guess_mod[0] + guess_mod[1] + guess_mod[2] + guess_mod[3] + guess_mod[4] + guess_mod[5] + guess_mod[6] + guess_mod[7])
        
        k += 1
      elif(digit_7b == guess_mod[4]):
        output = output + "K"
        digit_7b = "*"

        guess_mod = list(guess_mod)
        guess_mod[4] = "#"
        guess_mod = str(guess_mod[0] + guess_mod[1] + guess_mod[2] + guess_mod[3] + guess_mod[4] + guess_mod[5] + guess_mod[6] + guess_mod[7])
        
        k += 1
      elif(digit_8b == guess_mod[4]):
        output = output + "K"
        digit_8b = "*"

        guess_mod = list(guess_mod)
        guess_mod[4] = "#"
        guess_mod = str(guess_mod[0] + guess_mod[1] + guess_mod[2] + guess_mod[3] + guess_mod[4] + guess_mod[5] + guess_mod[6] + guess_mod[7])
        
        k += 1

      if(digit_6 == guess_mod[5]):
        w += 1
        digit_6b = "*"

        guess_mod = list(guess_mod)
        guess_mod[5] = "#"
        guess_mod = str(guess_mod[0] + guess_mod[1] + guess_mod[2] + guess_mod[3] + guess_mod[4] + guess_mod[5] + guess_mod[6] + guess_mod[7])
        
        output = output + "W"
      elif(digit_1b == guess_mod[5]):
        output = output + "K"
        digit_1b = "*"

        guess_mod = list(guess_mod)
        guess_mod[5] = "#"
        guess_mod = str(guess_mod[0] + guess_mod[1] + guess_mod[2] + guess_mod[3] + guess_mod[4] + guess_mod[5] + guess_mod[6] + guess_mod[7])
        
        k += 1
      elif(digit_2b == guess_mod[5]):
        output = output + "K"
        digit_2b = "*"

        guess_mod = list(guess_mod)
        guess_mod[5] = "#"
        guess_mod = str(guess_mod[0] + guess_mod[1] + guess_mod[2] + guess_mod[3] + guess_mod[4] + guess_mod[5] + guess_mod[6] + guess_mod[7])
        
        k += 1
      elif(digit_3b == guess_mod[5]):
        output = output + "K"
        digit_3b = "*"

        guess_mod = list(guess_mod)
        guess_mod[5] = "#"
        guess_mod = str(guess_mod[0] + guess_mod[1] + guess_mod[2] + guess_mod[3] + guess_mod[4] + guess_mod[5] + guess_mod[6] + guess_mod[7])
        
        k += 1
      elif(digit_4b == guess_mod[5]):
        output = output + "K"
        digit_4b = "*"

        guess_mod = list(guess_mod)
        guess_mod[5] = "#"
        guess_mod = str(guess_mod[0] + guess_mod[1] + guess_mod[2] + guess_mod[3] + guess_mod[4] + guess_mod[5] + guess_mod[6] + guess_mod[7])
        
        k += 1
      elif(digit_5b == guess_mod[5]):
        output = output + "K"
        digit_5b = "*"

        guess_mod = list(guess_mod)
        guess_mod[5] = "#"
        guess_mod = str(guess_mod[0] + guess_mod[1] + guess_mod[2] + guess_mod[3] + guess_mod[4] + guess_mod[5] + guess_mod[6] + guess_mod[7])
        
        k += 1
      elif(digit_7b == guess_mod[5]):
        output = output + "K"
        digit_7b = "*"

        guess_mod = list(guess_mod)
        guess_mod[5] = "#"
        guess_mod = str(guess_mod[0] + guess_mod[1] + guess_mod[2] + guess_mod[3] + guess_mod[4] + guess_mod[5] + guess_mod[6] + guess_mod[7])
        
        k += 1
      elif(digit_8b == guess_mod[5]):
        output = output + "K"
        digit_8b = "*"

        guess_mod = list(guess_mod)
        guess_mod[5] = "#"
        guess_mod = str(guess_mod[0] + guess_mod[1] + guess_mod[2] + guess_mod[3] + guess_mod[4] + guess_mod[5] + guess_mod[6] + guess_mod[7])
        
        k += 1
      
      if(digit_7 == guess_mod[6]):
        w += 1
        digit_7b = "*"

        guess_mod = list(guess_mod)
        guess_mod[6] = "#"
        guess_mod = str(guess_mod[0] + guess_mod[1] + guess_mod[2] + guess_mod[3] + guess_mod[4] + guess_mod[5] + guess_mod[6] + guess_mod[7])
        
        output = output + "W"
      elif(digit_1b == guess_mod[6]):
        output = output + "K"
        digit_1b = "*"

        guess_mod = list(guess_mod)
        guess_mod[6] = "#"
        guess_mod = str(guess_mod[0] + guess_mod[1] + guess_mod[2] + guess_mod[3] + guess_mod[4] + guess_mod[5] + guess_mod[6] + guess_mod[7])
        
        k += 1
      elif(digit_2b == guess_mod[6]):
        output = output + "K"
        digit_2b = "*"

        guess_mod = list(guess_mod)
        guess_mod[6] = "#"
        guess_mod = str(guess_mod[0] + guess_mod[1] + guess_mod[2] + guess_mod[3] + guess_mod[4] + guess_mod[5] + guess_mod[6] + guess_mod[7])
        
        k += 1
      elif(digit_3b == guess_mod[6]):
        output = output + "K"
        digit_3b = "*"

        guess_mod = list(guess_mod)
        guess_mod[6] = "#"
        guess_mod = str(guess_mod[0] + guess_mod[1] + guess_mod[2] + guess_mod[3] + guess_mod[4] + guess_mod[5] + guess_mod[6] + guess_mod[7])
        
        k += 1
      elif(digit_4b == guess_mod[6]):
        output = output + "K"
        digit_4b = "*"

        guess_mod = list(guess_mod)
        guess_mod[6] = "#"
        guess_mod = str(guess_mod[0] + guess_mod[1] + guess_mod[2] + guess_mod[3] + guess_mod[4] + guess_mod[5] + guess_mod[6] + guess_mod[7])
        
        k += 1
      elif(digit_5b == guess_mod[6]):
        output = output + "K"
        digit_5b = "*"

        guess_mod = list(guess_mod)
        guess_mod[6] = "#"
        guess_mod = str(guess_mod[0] + guess_mod[1] + guess_mod[2] + guess_mod[3] + guess_mod[4] + guess_mod[5] + guess_mod[6] + guess_mod[7])
        
        k += 1
      elif(digit_6b == guess_mod[6]):
        output = output + "K"
        digit_6b = "*"

        guess_mod = list(guess_mod)
        guess_mod[6] = "#"
        guess_mod = str(guess_mod[0] + guess_mod[1] + guess_mod[2] + guess_mod[3] + guess_mod[4] + guess_mod[5] + guess_mod[6] + guess_mod[7])
        
        k += 1
      elif(digit_8b == guess_mod[6]):
        output = output + "K"
        digit_8b = "*"

        guess_mod = list(guess_mod)
        guess_mod[6] = "#"
        guess_mod = str(guess_mod[0] + guess_mod[1] + guess_mod[2] + guess_mod[3] + guess_mod[4] + guess_mod[5] + guess_mod[6] + guess_mod[7])
        
        k += 1

      if(digit_8 == guess_mod[7]):
        w += 1
        digit_8b = "*"

        guess_mod = list(guess_mod)
        guess_mod[7] = "#"
        guess_mod = str(guess_mod[0] + guess_mod[1] + guess_mod[2] + guess_mod[3] + guess_mod[4] + guess_mod[5] + guess_mod[6] + guess_mod[7])
        
        output = output + "W"
      elif(digit_1b == guess_mod[7]):
        output = output + "K"
        digit_1b = "*"

        guess_mod = list(guess_mod)
        guess_mod[7] = "#"
        guess_mod = str(guess_mod[0] + guess_mod[1] + guess_mod[2] + guess_mod[3] + guess_mod[4] + guess_mod[5] + guess_mod[6] + guess_mod[7])
        
        k += 1
      elif(digit_2b == guess_mod[7]):
        output = output + "K"
        digit_2b = "*"

        guess_mod = list(guess_mod)
        guess_mod[7] = "#"
        guess_mod = str(guess_mod[0] + guess_mod[1] + guess_mod[2] + guess_mod[3] + guess_mod[4] + guess_mod[5] + guess_mod[6] + guess_mod[7])
        
        k += 1
      elif(digit_3b == guess_mod[7]):
        output = output + "K"
        digit_3b = "*"

        guess_mod = list(guess_mod)
        guess_mod[7] = "#"
        guess_mod = str(guess_mod[0] + guess_mod[1] + guess_mod[2] + guess_mod[3] + guess_mod[4] + guess_mod[5] + guess_mod[6] + guess_mod[7])
        
        k += 1
      elif(digit_4b == guess_mod[7]):
        output = output + "K"
        digit_4b = "*"

        guess_mod = list(guess_mod)
        guess_mod[7] = "#"
        guess_mod = str(guess_mod[0] + guess_mod[1] + guess_mod[2] + guess_mod[3] + guess_mod[4] + guess_mod[5] + guess_mod[6] + guess_mod[7])
        
        k += 1
      elif(digit_5b == guess_mod[7]):
        output = output + "K"
        digit_5b = "*"

        guess_mod = list(guess_mod)
        guess_mod[7] = "#"
        guess_mod = str(guess_mod[0] + guess_mod[1] + guess_mod[2] + guess_mod[3] + guess_mod[4] + guess_mod[5] + guess_mod[6] + guess_mod[7])
        
        k += 1
      elif(digit_6b == guess_mod[7]):
        output = output + "K"
        digit_6b = "*"

        guess_mod = list(guess_mod)
        guess_mod[7] = "#"
        guess_mod = str(guess_mod[0] + guess_mod[1] + guess_mod[2] + guess_mod[3] + guess_mod[4] + guess_mod[5] + guess_mod[6] + guess_mod[7])
        
        k += 1
      elif(digit_7b == guess_mod[7]):
        output = output + "K"
        digit_7b = "*"

        guess_mod = list(guess_mod)
        guess_mod[7] = "#"
        guess_mod = str(guess_mod[0] + guess_mod[1] + guess_mod[2] + guess_mod[3] + guess_mod[4] + guess_mod[5] + guess_mod[6] + guess_mod[7])
        
        k += 1

      sorted_characters = sorted(output)
      output = " ".join(sorted_characters)
      log = log + " | " + output
      os.system("clear")
      print(log)

      if(w >= 8):
          good_exit = "\nCongradulations, you cracked the code in " + str(tries) + " tries! You really are a mastermind!"
          cprint(good_exit, "green", attrs = ["bold"])
          wins += 1
          break#ends loop if user repeats code
      if(tries >= 15):
          bad_exit = "Sorry, you ran out of tries! The code was " + str(code)
          cprint(bad_exit, "red")
          break#breaks loop if user runs out of tries

final_exit = "Wow! You won " + str(wins) + " out of " + str(game_set) + " games!"
cprint(final_exit, "yellow", attrs = ["bold", "underline"])