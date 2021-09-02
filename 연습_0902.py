#1
import turtle

myT = None

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
result3 = pow(int(p),int(q))

print(result1, result2, result3)