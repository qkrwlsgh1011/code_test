
def view_count(_building):
    count = 0
    for i in range(len(_building)):
        for j in range(255):
            if i == 0 and i == 1 and i == len(_building) - 1 and i == len(_building) - 2:
                continue
            elif _building[i][j] == 1:      #있는 집일 때
                if _building[i-2][j] == 0 and _building[i-1][j] == 0 and _building[i+1][j] == 0 and _building[i+2][j] == 0:
                    count = count + 1
    return count


for s in range (10):
    build_num = int(input())            #빌딩 갯수
    building = [[0 for i in range(255)] for j in range(build_num)]
    build_height = list(map(int, input().split()))
    for t in range(build_num):
        temp = build_height[t]          #빌딩 높이
        if temp == 0:
            continue
        else:
            for u in range(temp):
                building[t][u] = 1
    print(f"#{s+1} {view_count(building)}")
    


    del building