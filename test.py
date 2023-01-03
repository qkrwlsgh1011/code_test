for T in range(1,11):
    A,B = input().split()
    result = []
    for i in B:
        if result and result[-1] == i:
            result.pop()
        else:
            result.append(i)
    result = "".join(result)
    print(f"#{T} {result}")