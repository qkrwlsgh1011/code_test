
for i in range(10):
    N = int(input())                        #암호문 길이
    src = list(map(int,input().split()))    #원본 암호문
    T = int(input())                        #명령어 개수
    adj = input().split()                   #명령어
    for j in range(0,len(adj)):
        if adj[j] =='I':                    #삽입
            idx = int(adj[j+1])             #x의 위치
            much = int(adj[j+2])            #몇개 들어갈지
            add_list = []                   #추가할 암호문들
            for k in range(much):
                add_list.append(int(adj[j+3+k]))    #추가할 암호문 list
            for s in range(much):
                src.insert(idx + s,add_list[s])     #암호 추가
        elif adj[j] == 'D':                 #삭제
            idx = int(adj[j+1])             #x의 위치
            much = int(adj[j+2])            #몇개 삭제할지
            del src[idx:idx+much]
        elif adj[j] == 'A':                 #추가
            much = int(adj[j+1])             #추가할 개수
            for k in range(much):
                src.append(adj[j+2+k])
    
    print("#{} {} {} {} {} {} {} {} {} {} {}".format(i+1, *src))
