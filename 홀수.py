turn = int(input())
temp = 1

while True:
    if turn == 0:
      break
    a = list(map(int,input().split()))
    print(f'#{temp} {max(a)}')
    temp = temp + 1
    turn = turn - 1
    