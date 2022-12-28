for i in range (1,11):
    pwd_len, pwds= input().split()
    pwds = list(pwds)
    tmp = True
    while tmp:
        for j in range(1,len(pwds)+1):
            if pwds[j] == pwds[j-1]:
                del pwds[j]
                del pwds[j-1]
                break
            if j == len(pwds)-1:
                tmp = False
                break
    pwds = ''.join(pwds)
    print(f"#{i} {pwds}")