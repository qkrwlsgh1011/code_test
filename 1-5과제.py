def add_city():
    pass

def output_city():
    pass

list_city = []
temp = 0
while True:
    temp = int(input("종료 값을 입력하세요 : "))
    if temp == 2:
        break
    elif temp == 1:
        city = input("도시를 영어로 입력하세요 : ")
        store_city = city[0:3]
        list_city.append(store_city)
        print("도시를 추가")
        print("추가 완료")
    else:
        print("숫자를 다시 입력하세요")
print(f"{list_city} 종료")
    

