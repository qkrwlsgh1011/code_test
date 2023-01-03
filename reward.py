
T = int(input())

def exchange(_src,_div):
    for i in range(0,_div):
        if sorted(_src) == _src:    #정렬된 형태라면
            tmp = _src[-1]
            _src[-1] = _src[-2]
            _src[-2] = _src[-1]     #맨 뒷자리 스왑
        else:
            max_idx = _src.index(max(_src)) #최대값이 있는 위치



for i in range(1,T+1):
    src, div = input().split()
    div = int(div)
    src = list(map(int,src))
