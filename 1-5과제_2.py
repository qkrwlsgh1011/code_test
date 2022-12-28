sub_list = []
point_list = []

def cal(lst):                                                                       #평균 계산 (점수 list를 인자로 받음)
    lst_sum = 0                                                                     #초기화
    for i in range(len(lst)):                                                       #입력한 과목 수 만큼 실행
        lst_sum += lst[i]       
    return lst_sum/len(lst)                                                         #과목 점수 총합 / 과목 수 = 과목 평균

while True:
    select = int(input("점수를 입력하시려면 1번, 종료하시려면 2번을 눌러주세요 : "))    #1번을 누르면 입력 2번 누르면 결과 출력 후 프로그램 종료
    if select == 1:
        subject = input("과목 : ")
        point = int(input("점수 : "))
        confirm = (input("추가 하실 건가요?\n\t 예 or 아니오 : "))
        if confirm == "예":
            sub_list.append(subject)
            point_list.append(point)                                                #예를 눌러 과목명과 점수를 입력
        elif confirm == "아니오":                                                     
            continue
    elif select == 2:
        break
for i in range(len(sub_list)):                                                      #과목 수 만큼 결과 값 출력 실행
    print(f"{sub_list[i]} : {point_list[i]}")
print(f"평균 : {cal(point_list)}")                                                  #point_list 점수 list를 인자로 넣어 평균값 계산