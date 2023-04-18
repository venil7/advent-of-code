import os;

file_name = "{dir}/data/day-01.txt".format(dir=os.path.dirname(__file__))

def max_number_per_group():
  max = 0
  with open(file_name, "rt") as file:
    items = file.read().splitlines()
    current = 0
    for item in items:
      if item == "":
        current = 0
      else:
        current += int(item)
        if current > max:
          max = current
    return max

def top_three_per_group():
  groups = []
  with open(file_name, "rt") as file:
    items = file.read().splitlines()
    current = 0
    for item in items:
      if item == "":
        groups.append(current)
        current = 0
      else:
        current += int(item)
    groups.append(current)

    groups.sort(reverse=True)
    return groups[0] + groups[1] + groups[2]

print(max_number_per_group())
print(top_three_per_group())

