T = int(input())
for i in range(1,T+1):
    P = int(input())
    i_list = list(map(int, input().split()))
    grade = [0] * 101
    max_idx = 0
    for g in i_list:
        grade[g] += 1
        if grade[g] >= grade[max_idx]:
            max_idx = g

    print(f"#{i} {max_idx}")