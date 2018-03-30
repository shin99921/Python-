# else 문
print("1","-"*50)

num = int(input("input number: "))

if num%2 == 0:
    print("{}는(은) 짝수 입니다.".format(num))
else:
    print("{}는(은) 홀수 입니다.".format(num))


print("\n")

# elif 구문
print("2","-"*50)
import datetime

now = datetime.datetime.now()
month = now.month

if 3 <= month <=5:
    print("지금은 봄")
elif 6 <= month <=8:
    print("지금은 여름")
elif 9 <= month <=11:
    print("지금은 가을")
else:
    print("지금은 겨울")

print("\n")

# 0과 빈문자열은 False 로 나온다.
print("3","-"*50)
if 0:
    print("0은 True로 변환됩니다. ")
else:
    print("0은 False로 변환됩니다.")

print()

if 0:
    print("빈 문자열은 True로 변환됩니다. ")
else:
    print("빈 문자열은 False로 변환됩니다.")

print("\n")

# 프로그램 중간에 pass 를 입력해 놓으면 그냥 지나간다.
print("4","-"*50)

number = int(input("input : "))

if number > 0:
    pass
else:
    pass

print("\n")

# raise 를 사용하면 강제로 오류를 발생시킨다.
print("5","-"*50)

number = int(input("input : "))

if number > 0:
    raise
else:
    raise

print("\n")
