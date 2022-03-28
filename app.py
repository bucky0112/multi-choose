import random

a_choose = "選項A"
b_choose = "選項B"
options = [a_choose, b_choose]
pick_list = []
init_num = 0
end_num = 10

while init_num != end_num:
  init_num += 1
  pick_list.append(random.choice(options))

  if init_num == end_num:
    break
  else:
    continue  

def showOption(item):
  times = pick_list.count(item)
  return f"抽到 {item} 共 {times} 次"

print(showOption(a_choose))
print(showOption(b_choose))