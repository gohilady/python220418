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

