# 덧셈 리컬시브
# def fac_sum(n):
#     if(n==0):
#         return 0
#     elif(n==1):
#         return 1
#     else:
#         return n+fac_sum(n-1)

# print(f"{fac_sum(5)}")

# 곱셈 리컬시브
# def fac_square(x,n):
#     if(n==0):
#         return 1
#     elif(n==1):
#         return x
#     else:
#         return x * fac_square(x,n-1)

# print(f"{fac_square(3,3)}")

#최대 공약수
# def gcd(n,m):
#     if n == 0:
#         return m
#     elif n < m:
#         temp = m
#         m = n
#         n = temp
#         return gcd(n,m)
#     elif n >= m:
#         temp = n%m
#         n = temp
#         return gcd(n,m)

# print(gcd(15,12))

# def fibo(n):
#     fib_list =[1,1]
#     if n==1 or n==2:
#         return 1
#     for i in range(2,n):
#         fib_list.append(fib_list[i-1] + fib_list[i-2])
#     return fib_list

# print(sum(fibo(5)))
# hanoi_list = {1:1}
# counter = 0
# def hanoi(n):   #하노이 원판개수
#     global counter
#     counter += 1
#     if n in hanoi_list:
#         return hanoi_list[n]
#     else:
#         output = 2 * hanoi(n-1) + 1
#         hanoi_list[n] = output
#         return output

# print(hanoi(5))

# name_1 = "JinHo"
# email_1 = "qkrwlsgh1011@naver.com"
# add_1 = "Incheon"

def print_business_card(name,email,add):
    print("-" * 20)
    print(f"Name : {name}")
    print(f"E-mail : {email}")
    print(f"address : {add}")
    print("-" * 20)
    
# print_business_card(name_1,email_1,add_1)

# name_2 = "dlwlrma"
# email_2 = "dlwlrma@kakao.com"
# add_2 = "Seoul"

# print_business_card(name_2,email_2,add_2)

class BusinessCard:
    def set_inform(self,_name,_email,_address):
        self._name = _name              #변수 값 대입 할당
        self._email = _email
        self._address = _address

    def print_business_card(self):
        print("=" * 20)
        print(f"Name : {self._name}")
        print(f"E-mail : {self._email}")
        print(f"Address : {self._address}")
        print("=" * 20)
        


# member_1 = BusinessCard()
# print(type(member_1))
# print(id(member_1))
# print(member_1)

# member_1.set_inform("JinHo","qkrwlsgh1011@naver.com","Incheon")
# print(member_1._email)
# print(member_1.get_name())

# member_3=BusinessCard()
# member_3.set_inform("user3","user3@gmail.com","seoul")
# member_3.print_business_card()


class ClassCard:
    # def set_info(self,_name,_korean,_math):
    #     self._name = _name              #변수 값 대입 할당
    #     self._korean = _korean
    #     self._math = _math

    def print_classcard(self):
        print("=" * 20)
        print(f"이름 : {self.name}")
        print(f"국어 : {self.korean}")
        print(f"수학 : {self.math}")
        print(f"총점 : {self.get_sum()}")
        print(f"총점 : {self.get_average()}")
        print("=" * 20)

    def get_sum(self):
        return self.korean + self.math

    def get_average(self):
        return self.get_sum()//2

    def input_info(self):
        self.name = input("이름을 입력해주세요 : ")
        self.korean = int(input("국어 점수를 입력해주세요 : "))
        self.math = int(input("수학 점수를 입력해주세요 : "))



student1 = ClassCard()
student1.input_info()
student1.print_classcard()
