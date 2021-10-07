# 1번 문제 : 변수 2개를 입력받아 그 곱을 구하는 함수를 만드시오.

## 전역 변수 선언 ##
c = 0

## 함수 선언 부분 ##
def multiply(a,b) :
    c = a * b
    return c


## 메인 코드 부분 ##
hello1 = int(input("첫번째 값을 입력해주세요 : "))
hello2 = int(input("두번째 값을 입력해주세요 :"))
d = multiply(hello1, hello2)
print(d)