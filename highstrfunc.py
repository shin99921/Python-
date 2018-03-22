print("I eat {0} apples".format(3))
#숫자 바로 대입하기.

print("I eat {0} apples".format("five"))
#문자 바로 대입하기

number = 3
print("I have {0} book".format(number))
#변수 대입하기

a = 10
b = "ten"
c = 10.000
print("{0}=={1}=={2}".format(a,b,c))
#2개이상 값 넣기

print("{a},{b},{c}".format(a=1,b=2,c=3))
#이름으로 넣기

print("{0},{1},{a}".format(1,b,a=123))
#인덱스와 이름 혼용해서 넣기

print("{0:>10}".format("hi"))
print("{0:<10}".format("hello"))
print("{0:^10}".format("middle"))
#오른쪽 정렬과 왼쪽 정렬과 가운데 정렬

print("{0:=^10}".format("hi"))
print("{0:=<10}".format("hi"))
print("{0:=>10}".format("hi"))
#가운데,왼쪽,오른쪽 공백 채우기

y = 3.141592
print("{0:0.9f}".format(y))
print("{0:20.9}".format(y))
#소수점 표현하기

print("{{ and }}".format())
#{}와 문자 표현