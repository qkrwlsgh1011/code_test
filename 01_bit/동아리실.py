T = int(input())

for s in range(1,T+1):
    studs = input()
    stu_bit =[[0] * 16 for i in range(len(studs))]  #2차원 배열 [16][10000]
    for day in range(len(studs)):                   #날짜
        manage = 1 << (ord(studs[day]) - ord('A'))            #A : 1, B : 2, C : 4, D : 8
        for i in range(1,16):
            if day == 0:                            #첫날이면
                if i&manage != 0 and i&1 !=0:   #관리자와 A가 포함
                    stu_bit[day][i] = 1;
            else:
                if stu_bit[day-1][i]!=0:
                    for j in range(1,16):
                        if j&manage != 0 and i&j !=0:
                            stu_bit[day][j] += stu_bit[day-1][i]
                            stu_bit[day][j] %= 1000000007
    much = 0
    for i in range(1,16):
        much += stu_bit[len(studs)-1][i]
        much%=1000000007
    print(f"#{s} {much}")

