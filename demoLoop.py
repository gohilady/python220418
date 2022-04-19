# demoLoop.py

#반복 구문
value = 5
while value > 0:
    print(value)
    value -= 1

print("전체 실행 종료")

lst = ["문자열" , 100, 3.14]
for item in lst:
    print(item, type(item))

print(len(lst))

lst = [1,2,3,4,5,6,7,8,9,10]
for i in lst:
    if i > 5:
        break
    print("item:{0}".format(i))

print("------continue구문")
for i in lst:
    if i % 2 == 0:
        continue
    print("item:{0}".format(i))

#수열함수 
print(list(range(10)))
print(list(range(1,11)))

# 메뉴얼하게 루프돌기
for i in range(10):
    print(i)

print(range(10))

#년도
print(list(range(2000,2023)))

#리스트 컴프리헨션(리스트 임베딩) : 한줄로 필터링, 루프, 가공까지 - 파이썬스럽다.
lst = list(range(1,11))
print([i**2 for i in lst if i >5])

#필터함수
lst = [20, 25, 30]

iterL = filter(None, lst)
for i in iterL:
    print("Item:{0}".format(i))

print("=----필터링====")

#필터링 함수 정의 (논리식에서 True면 포함)
def getBiggerThen20(i):
    return i >20 

#파이썬은 무조건 참조가 복사
iterL = filter(getBiggerThen20, lst)
for i in iterL:
    print("Item:{0}".format(i))

#람다함수를 정의
print("====람다함수===")

iterL = filter(lambda x:x>20, lst)
for i in iterL:
    print("Item:{0}".format(i))