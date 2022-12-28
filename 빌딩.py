for T in range(10) :
    N = int(input())
    building = list(map(int, input().split()))

    count = 0
    for i in range(2, N-2) :
        sub_2 = building[i] - building[i-2]
        sub_1 = building[i] - building[i-1]
        add_1 = building[i] - building[i+1]
        add_2 = building[i] - building[i+2]
        if sub_2 > 0 and sub_1 > 0 and add_1 > 0 and add_2 > 0 :
            count = min(sub_2, sub_1, add_1, add_2) + count

    print(f"#{T+1} {count}")