# funtion1.py

#함수를 정의
def setValue(newValue):
    x = newValue
    print("함수내부:", x)

#호출
retValue = setValue(5)
print(retValue)

# 교집합 문자를 리턴하는 함수 
def intersect(perlist, postlist):
    #지역변수
    result = []
    for x in perlist:
        if x in postlist and x not in result:
            result.append(x)
    return result 

# 호출(중단점을 추가)
print(intersect("HAM","SPAM")
