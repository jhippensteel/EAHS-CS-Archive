import random, math
a = 0

poss_dig = ['1', '2', '3', '4', '5', '6']#, 7, 8, 9]
poss_guesses = []
code = []
s = []
guesses = {}

table = {
  'kkkk' : 0,
  'kkww' : 0,
  'kkkw' : 0,
  'www' : 0,
  'kww' : 0,
  'kkw' : 0,
  'kkk' : 0,
  'ww' : 0,
  'kw' : 0,
  'kk' : 0,
  'w' : 0,
  'k' : 0,
  '' : 0,
  'wwww' : 0
}

for i in range(4):
  code.append(random.choice(poss_dig))
s.append(code)

print('|', '#', '|')

#-------------Creating List of Possible Codes----------------#
while(code in s):
  code = []
  for i in range(4):
    code.append(random.choice(poss_dig))
  if(code not in s):
    a += 1
    print('|', '#' * math.ceil(a/60), '|')
    s.append(code)
  if(a == 1295):
    break
#-------------Creating List of Possible Codes----------------#

#-------------Creating Copies--------------#
s_copy = list(s)
t = list(s)
#-------------Creating Copies--------------#

#-------------First Guess-------------#
guess = ['1', '1', '2', '2']
print('1122')
t.remove(guess)
s.remove(guess)
#-------------First Guess-------------#

while(True):
  #----------------Resets Lists-----------------------#
  w_counted = []
  k_counted = []
  max_scores = []
  guesses = {}

  table = {
    'kkkk' : 0,
    'kkww' : 0,
    'kkkw' : 0,
    'www' : 0,
    'kww' : 0,
    'kkw' : 0,
    'kkk' : 0,
    'ww' : 0,
    'kw' : 0,
    'kk' : 0,
    'w' : 0,
    'k' : 0,
    '' : 0,
    'wwww' : 0
  }
  #-----------------------Resets Lists------------------#
  #--------------Counting W's and K's in response----------------#
  response = str(input(">>"))
  w_count = response.count('w')
  k_count = response.count('k')
  #--------------Counting W's and K's in response----------------#

  if(w_count == 4):
    exit()

  #------------------Removing any Possible Code that does not show the same response--------------------#
  for v in s:
    test_code = list(v)
    #----------------Second W and K count------------------------#
    w_count_2 = 0
    k_count_2 = 0
    #----------------Second W and K count------------------------#

    #----------------Runs through Digits of guesses in s----------------#
    for i in range(4):
      if(v[i] == guess[i]):
        w_count_2 += 1
        test_code[i] = '0'
        print(str(v[i]), str(guess[i]), v, w_count)
    for i in range(4):
      if(test_code[i] in guess) and (test_code[i] != guess[i]):
        k_count_2 += 1
        test_code[i] = '0'
    #----------------Runs through Digits of guesses in s----------------#

    #---------------Removes any item in s that does not fit paramiters---------------#
    if(w_count != w_count_2) or (k_count != k_count_2):
      s_copy.remove(v)

  #-----------------Resets W and K count-------------------#
  w_count = 0
  k_count = 0
  #-----------------Resets W and K count-------------------#

  #------------------Removing any Possible Code that does not show the same response--------------------#
  s_copy.sort()
  print(len(s_copy))
  print(*s_copy, sep = "\n")
  #--------------------Finding all untried guesses-----------------------#
  for untried in t:
    if(untried in t):
      #--------------------Finding all untried guesses-----------------------#
    
      #----Calculating the guess that would eliminate the most possible codes in a worst case situation---#
      for x in s_copy:
        test_code = list(x)
        w_counted = []
        k_counted = []
        for i in range(4):
          if(untried[i] == test_code[i]):
            w_count += 1
            w_counted.append(untried[i])
            test_code[i] = '0'
        for i in range(4):
          if(untried[i] in test_code) and (untried[i] != test_code[i]) and (untried[i] not in w_counted) and (untried[i] not in k_counted):
            k_count += 1
            test_code[i] = '0'
            k_counted.append(untried[i])

        search = (('k'*k_count) + ('w'*w_count))

        table[search] += 1
        k_count = 0
        w_count = 0

      min_elim = len(s_copy) - max(table.values())#The worth of the guess is only as valuable as the least number of codes it eliminated
      sg = "".join(untried)
      guesses[sg] = min_elim


  max_val  = max(guesses.values())#Find which guess has the best worst outcome  
  max_scores = []
  for item in guesses.items():
    if(item[1] == max_val):
      max_scores.append(item[0])
      #print(item[0])
      if(item[0] in s_copy):
        in_s = True
  max_scores.sort()
  print(max_scores)
  i = 0
  for guess in max_scores:
    i += 1
    if(list(guess) in s_copy):
      if(guess in t):
        break

  if(len(s_copy) == 1):
    print(*s_copy)
  else:
    print(guess)
    guess = list(guess)
    t.remove(guess)
    if(guess in s_copy):
      s.remove(guess)
      s_copy.remove(guess)