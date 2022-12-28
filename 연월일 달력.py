T = int(input())

def classify_month(n):
    month = n[4] * 10 + n[5]
    if month > 0 and month <= 9:
        return  "0" + str(month)
    elif month>=10 and month<=12:
        return str(month)
    else:
        return -1

def classify_day(n):
    odd = ["01","03","05","07","08","10","12"]
    even = ["04","06","09","11"]
    special = ["02"]
    if classify_month(n) in odd:
        day = n[6]*10 + n[7]
        if day > 0 and day <= 9:
            return "0" + str(day)
        elif day>=10 and day<=31:
            return str(day)
        else:
            return -1
    elif classify_month(n) in even:
        day = n[6]*10 + n[7]
        if day > 0 and day <= 9:
            return "0" + str(day)
        elif day>=10 and day<=30:
            return str(day)
        else:
            return -1
    elif classify_month(n) in special:
        day = n[6]*10 + n[7]
        if day > 0 and day <= 9:
            return "0" + str(day)
        elif day>=10 and day<=28:
            return str(day)
        else:
            return -1
    else:
        return -1

def is_possible(n):
    if classify_month(n) == -1 or classify_day(n) == -1:
        return -1

for i in range(0,T):
    N = input()
    int_N = []
    for j in N:
        int_N.append(int(j))
    if is_possible(int_N) == -1:
        print(f"#{i+1} -1")
    else:
        print(f"#{i+1} {N[0:4]}/{classify_month(int_N)}/{classify_day(int_N)}")
    T = T - 1