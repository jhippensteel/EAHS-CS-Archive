#Jaysen Hippensteek. Five straight

score = 0 #setting variable

print("Question 1: ")#starts quiz
print('Which of the following will print "Hello World"?')#print question
print('(A): print(Hello World")\n(B): print("Hello World")\n(C): Print("Hello World")') #gives the user multiple options to choose

answer_1 = str(input("Please enter the letter (capital)of your choice: ")) #asks user for answer

if(answer_1 == "B"):#only moves on if answer is correct
  score += 1#adds 1 to variable

  print()
  print("Question 2")#Moves on to next question
  print("What type of variable has only two states")
  print("(A): A Boolean Variable\n(B): A numeric variable\n(C): A Lovelacean")
  
  answer_2 = str(input("What is your answer (capital letter): "))#Repeats

  if(answer_2 == "A"):
    score += 1

    print()
    print("Question 3")
    print('What function adds "accessories" to the language')
    print("(A): add\n(B): accessorize\n(C): import")

    answer_3 = str(input("What is your answer (Capital letter): "))

    if(answer_3 == "C"):
      score += 1

      print()
      print("Question 4")
      print("What will this line output: print(1 > 2")
      print("(A): True\n(B): False\n(C): 3")

      answer_4 = str(input("What is your answer (Capital letter): "))

      if(answer_4 == "B"):
        score += 1

        print()
        print("Question 5")
        print("What does the function // do")
        print("(A): It preforms division\n(B): It Rounds\n(C): It preforms floor or integer division")

        answer_5 = str(input("What is your answer (Capital letter): "))

        if(answer_5 == "C"):
          score += 1

          print()
          print("-"*50)
          print("Congratulations! You got all five answers correct")#congatulates user if they got all answers correct
          print("Your score was", score) #tells user their score


if(answer_1 != "B"):#Only does following if answer was wrong
  
  print()
  print("-"*50)
  print("Sorry, you were unseccessful")#infroms user that they were unseccessful
  print("Your score was", score)#tells user their score
  exit() #ends program

if(answer_2 != "A"):
  
  print()
  print("-"*50)
  print("Sorry, you were unseccessful")
  print("Your score was", score)
  exit()

if(answer_3 != "C"):
  
  print()
  print("-"*50)
  print("Sorry, you were unseccessful")
  print("Your score was", score)
  exit()

if(answer_4 != "B"):
  
  print()
  print("-"*50)
  print("Sorry, you were unseccessful")
  print("Your score was", score)
  exit()

if(answer_5 != "C"):
  
  print()
  print("-"*50)
  print("Sorry, you were unseccessful")
  print("Your score was", score)
  exit()

#! Not sure what directions mean by "use score in boolean test"