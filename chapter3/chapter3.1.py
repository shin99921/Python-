# if 문
print("1","-"*50)

num = int(input("input number: "))

if num > 0:
    print("+")
if num < 0:
    print("-")
if num == 0:
    print("0")

print("\n")



# 오전 오후 구분 프로그램
print("2","-"*50)
import datetime

now = datetime.datetime.now()

if now.hour < 12:
    print("{}시 이므로 오전".format(now.hour))
if now.hour >= 12:
    print("{}시 이므로 오후".format(now.hour))

print("\n")



# 계절 출력 프로그램
print("3","-"*50)
import datetime

now = datetime.datetime.now()
mon = now.month

if 3 <= mon <= 5:
    print("봄 입니다!")
if 6 <= mon <= 8:
    print("여름 입니다!")
if 9 <= mon <= 11:
    print("가을 입니다!")
if 12 == mon or 1 <= mon <=2:
    print("겨울 입니다 ㅠㅠ")

print("\n")



# 짝수 홀수 프로그램
print("4","-"*50)

num = int(input("input num: "))

if num % 2 == 0:
    print("짝수")
if num % 2 != 0:
    print("홀수")

