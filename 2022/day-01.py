import os;

file_name = "{dir}/data/day-01.txt".format(dir=os.path.dirname(__file__))

def calorie_amounts():
  with open(file_name, "rt") as file:
    items = file.read().splitlines()
  amount = 0;
  for item in items:
    if item.isdigit():
      amount += int(item)
    else:
      yield amount
      amount = 0
  if amount > 0:
    yield amount

def max_number_per_group():
  max = 0
  for amount in calorie_amounts():
    if amount > max:
      max = amount
  
  return max

def top_three_per_group():
  groups = list(calorie_amounts())
  groups.sort(reverse=True)
  return groups[0] + groups[1] + groups[2]

print(max_number_per_group())
print(top_three_per_group())

