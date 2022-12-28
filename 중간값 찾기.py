N = int(input())
int_list = list(map(int, input().split()))
int_list.sort()
print(int_list[N//2])