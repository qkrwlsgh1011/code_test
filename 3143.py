T = int(input())

def length(dest, _string):
    s_length = len(dest)
    freq = dest.count(_string)
    return s_length - (freq * len(_string)) + freq


for i in range(0,T):
    s_string, temp = input().split()      #검사할 문자열 A,B
    print(f'#{i+1} {length(s_string,temp)}')
    