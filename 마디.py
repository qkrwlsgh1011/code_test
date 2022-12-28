T = int(input())
for i in range(1,T+1):
    s_cases = input()
    tmp = ''
    for s_case in s_cases:
        tmp += s_case
        if tmp == s_cases[len(tmp):len(tmp) + len(tmp)]:
            break
    print(f"#{i} {len(tmp)}")

