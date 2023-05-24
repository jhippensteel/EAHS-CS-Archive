def searchStateInfo(contents):
  states = set()
  for v in contents[1:]:
    states.add(v[0])
  print(*sorted(list(states)), sep=", ")
  state = str(input("STATE: "))
  print(*contents[0][1:], sep=", ")
  topic = str(input("TOPIC: "))
  for i, v in enumerate(contents[0][1:]):
    if(v == topic):
      index = i + 2
  for v in contents[1:]:
    if(v[0] == state):
      print(f"{v[1]}: {v[index]}")
def searchDateInfo(contents):
  dates = set()
  for v in contents[1:]:
    dates.add(v[1])
  print(*sorted(list(dates)), sep=", ")
  date = str(input("DATE: "))
  states = set()
  for v in contents[1:]:
    states.add(v[0])
  print(*sorted(list(states)), sep=", ")
  state = str(input("STATE: "))
  for v in contents[1:]:
    if(v[0] == state and v[1] == date):
      for i, c in enumerate(v):
        print(f"{contents[0][i]}: {c}")
def totalForYear(contents):
  total = 0
  dates = set()
  for v in contents[1:]:
    dates.add(v[1])
  print(*sorted(list(dates)), sep=", ")
  date = str(input("DATE: "))
  print("\033c")
  print(contents[0][2:])
  field = str(input("FIELD: "))
  print("\033c")
  for i, v in enumerate(contents[0][2:]):
    if v == field:
      index = i + 2
  for v in contents[1:]:
    if v[1] == date:
      total += float(v[index])
  print(f"Total: {round(total, 2)}")
def averageForYear(contents):
  total = 0
  count = 0
  dates = set()
  for v in contents[1:]:
    dates.add(v[1])
  print(*sorted(list(dates)), sep=", ")
  date = str(input("DATE: "))
  print("\033c")
  print(contents[0][2:])
  field = str(input("FIELD: "))
  print("\033c")
  for i, v in enumerate(contents[0][2:]):
    if v == field:
      index = i + 2
  for v in contents[1:]:
    if v[1] == date:
      total += float(v[index])
      count += 1
  average = total / count
  print(f"Average: {round(average, 2)}")
def maximumState(contents):
  field = str(input("FIELD: "))
  index = contents[0].index(field)
  print("\033c")
  data = []
  for v in contents[1:]:
    data.append(float(v[index]))
  for v in contents[1:]:
    if(float(v[index]) == max(data)):
      state = v[0]
  print(f"{state} has the largest data in the field")