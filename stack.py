list_a = []

def push(x):
  list_a.append(x)

def pop():
  if len(list_a) == 0:
    return -1
  else:
    return list_a.pop()

def size():
  return list_a.len()

def empty():

  if len(list_a) == 0:
    return 1
  else:
    return 0

def top():
  if len(list_a) == 0:
    return -1
  else:
    return list_a[len(list_a)-1]

temp = int(input())
while temp !=0:
  select = input()
  if select[0] == 'p':
    a,b = select.split()
    push(b)
  elif select[0] == 'p':
    print(pop())
  elif select[0] == 's':
    print(size())
  elif select[0] == 'e':
    print(empty())
  elif select[0] == 't':
    print(top())
  temp -= 1