# 2번 문제 : 사용자로부터 숫자를 3개 입력하고
# 입력한 숫자의 합계를 구하는 코드를 for문으로 완성하시오

total = 0

for i in range (0,3) :
    p = int(input("값을 입력해주세요 :"))
    total = total + p

# 첫번째 루프에서 total이 0에서 1로 수정
# 두번째 루프에서 total이 1에서 3으로 수정

print(total)
