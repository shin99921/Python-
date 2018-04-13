# 3.정수를 입력받아 변수num에 대입한 후, 변수 num의 값이 100보다 적을경우 숫자를 출력해보자.
print("3","-"*50)

a = int(input("input: "))

if a < 100:
    print(a)

print()




# 4.정수를 입력받아 변수 num에 대입한 후, 변수 num의 값이 100 보다 적을경우 숫자를 출력해보자.
print("4","-"*50)

a = int(input("input: "))

if (a % 2 == 0):
    print("짝수")

print()




# 5.정수를 입력받아 변수 num 에 대입한 후 변수 num의 값이 짝수인 경우 "짝수"를 홀수일 경우 "홀수"를 출력해 보자.
print("5","-"*50)

a = int(input("input: "))

if (a % 2 == 0):
    print("짝수")
else:
    print("홀수")

print()




# 6.정수를 입력받아 변수 num에 대입한 후 변수 num의 값이 100 보다 작을경우 10%감소한 값을 그렇지 않으면 10% 증가한 값을 출력해 보자.
print("6","-"*50)

num = int(input("input: "))

if num < 100:
    print(num-(num*0.1))
else:
    print(num+(num*0.1))




# 7.두 정수를 입력받아 변수 a,b에 각각 대입하고, a+b-b**2의 계산 결과가 0 이거나 양수 이면 결과를 출력하고 음수이변 음수를 출력해보자.
print("7","-"*50)

a = int(input("input: "))
b = int(input("input: "))

if (a+b-b**2) >= 0:
    print(a+b-b**2)
else:
    print("음수")

print()




# 8.정수를 입력받아 변수 num에 대입한 후 변수의 값이 2와 3으로 나누어질 경우 "나누어짐" 을 출룍하고 그렇지 않으면 "나누어지지 않음" 이라고 출력해보자.
print("8","-"*50)

num = int(input("input: "))

if (num % 2 == 0) and (num % 3 == 0):
    print("나누어짐")
else:
    print("나누어지지 않음")

print()




# 9.a=5, b=3인경우 +,-,*,/중 한 문자를 입력받아 +이면 두 변수를 더하고 -이면 두 변수를 빼고 *이면 두변수를 곱하고 /이면 두변수를 나누는 연산을 하여 그 결과를 출력하라.
print("9","-"*50)

a = 5
b = 3
c = input("input +,-,*,/: ")

if c == "+":
    print(a+b)
elif c == "-":
    print(a-b)
elif c == "*":
    print(a*b)
elif c == "/":
    print(a/b)

print()





# 10.정수를 입력받아 다음 수소이온지수(ph) 범위 내의 숫자일 경우 해당 용액의 종류를 출력하자.
print("10","-"*50)

ph = int(input("input: "))

if 0 <= ph <=4:
    print("강산성")
elif ph <= 6:
    print("약산성")
elif ph == 7:
    print("중성")
elif ph <= 9:
    print("약염기성")
elif ph <= 14:
    print("강염기성")

print()






# 11.년도를 입력받아 윤년인지 평년인지 구분하여 출력해 보자.
print("11","-"*50)

year = int(input("input: "))

if (year % 4 == 0) and (year % 100 != 100) or (year % 400 == 0):
    print("윤년")
else:
    print("평년")

print()






# 12.키와 몸무게를 입력받아 체질량 지수를 계산하여 출력해 보자. BMI계산은 몸무게/키(m)**2 로 계산하며 BMI판정 기준은 다음과 같다.
print("12","-"*50)

kg = int(input("input: "))
tall = int(input("input: "))
bmi = kg/(tall*0.01)**2

if bmi < 18.5:
    print("저체중")
elif bmi < 23:
    print("정상")
elif bmi < 25:
    print("과체중")
elif bmi < 30:
    print("중등도비만")
elif bmi >= 35:
    print("고도비만")

print()