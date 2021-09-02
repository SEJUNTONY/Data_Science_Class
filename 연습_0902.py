#1
import turtle

## 함수 선언 부분 ##

## 변수 선언 부분 ##
myT = None

## 메인 코드 부분 ##
turtle.shape('turtle')

turtle.forward(100)
turtle.right(240)
turtle.forward(100)
turtle.right(240)
turtle.forward(100)

turtle.done()


#2
p = input("숫자를 입력하세요")
q = input("숫자를 입력하세요")

result1 = int(p) + int(q)
result2 = int(p) * int(q)
result3 = int(p) ** int(q)

print(result1)
print(result2)
print(result3)
