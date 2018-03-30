# 자료형 변환
print("1","-"*50)
# 1
x1=3.14
x2=float(x1)
x3=int(x2)
x4=str(x3)
print(x1,x2,x3,x4)
print("\n")
# 2
text=input("실수 형태 문자열: ")
fnum=float(text)
inum=int(fnum)
tstr=str(inum)
print(text,type(text), fnum,type(fnum))
print(inum, type(inum),tstr,type(tstr))
print("\n")

# 문자열 연산
print("2","-"*50)
head="Python"
tail=" is fun!"
print(head+tail)
print("\n")

# 문자열 콤마 사용법과 종류
print("3","-"*50)
print("Hello World.1")
print('Hello World.2')
print("""Hello World.3""")
print('''Hello World.4''')

a="Python 'is' fun"
print(a)

b='Python "is" fun'
print(b)

c="Python \'is\" fun"
print(c)

d="Python is\n fun"
print(d)

e="""Python
is
fun"""
print(e)

f='''Python
is
so
good'''
print(f)
print("\n")

# 문자열 관련 함수들
print("4","-"*50)
a = "hobby"
print(a.count('b')) # 산택한 문자가 한 문장에 몇가지가 있는지 알려준다.

a = "Python is very fun"
print(a.find('y'))
print(a.find('P'))
print(a.find('b')) # 없는 문자는 거짓(-1)로 출력된다.

a = "Lief is too short"
print(a.index('t'))
#print(c.index('k')) # -1이 출력되지 않고 오류가 난다.

a = ","
print(a.join('abcd')) # 문자 사이사이에 변수에있는 문자를 대입한다.

a = "hi"
print(a.upper()) # 소문자를 대문자로 바꿔준다.

a = "HI"
print(a.lower()) # 대문자를 소문자로 바꿔준다.

a = " hi "
print(a.lstrip()) # 왼쪽 공백을 지운다.
print(a.rstrip()) # 오른쪽 공백을 지운다.
print(a.strip()) # 양쪽 공백을 지운다.

a = "Life is too short"
print(a.replace("Life","Your leg")) # 문자를 바꿔준다.

a = "Life is too short"
print(a.split()) # 아무것도 지정하지 않으면 공백으로 문장을 나눠주고.
a = "a:b:c:d"
print(a.split(':')) # 지정해준 문자를 기준으로 문자열을 나눈다.
print("\n")

# 문자열 포멧
print("5","-"*50)
print("I eat %d apple!"%3)
print("I eat %s apple!"%"three")

number=5
print("I eat %d sushi"% number)
day="six"
print("I have %d book and %s pencil"% (number,day))

flo=3.234
print("This is float number test %d"% flo)
# %d는 정수형이라서 실수로 출력하려면 실수형 %f
print("This is float number test %f"% flo)

# %를 출력하고 싶으면 %%를 사용한다.
print("%f%%"% flo)
print("%15s"%"hello")
print("%0.9d"% 3)
print("%0.9s"%"hello")# 가능은 하지만 변화는 없다.
print("\n")

# 고급 문자열 포멧팅
print("6","-"*50)
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
print("\n")


