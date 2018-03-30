# 파이썬 키워드
print("1","-"*50)
import keyword
print(keyword.kwlist)
print("\n")

# 식별자는 변수라고도 하는것같은데 키워드, 특수문자(_제외), 숫자시작, 공백포함을 할수없다.

# 앞이 대문자이면 스네이크 케이스, 앞이 대문자면 캐멀 케이스이다.

# print() = 함수
# list() = 함수
# soup.select() = 함수
# math.pi = (변수)
# math.e = (변수)
# class Animal = 클래스

# 이렇게 샵을 붙이는 것을 주석이라하고 프로그램의 영향을 주지 않는다.

# 출력
print("2","-"*50)
print("print 함수로 메시지를 출력할수 있다.")
print("\n")

# 문자열
print("3","-"*50)
print("큰 따옴표표로 출력가능",'작은 따옴표로도 출력가능')
print("\n")

# 이스케이프 문자
print("4","-"*50)
print("큰 따옴표안에 '작은따옴표' 가능")
print('작은 따옴표 "안에 큰" 따옴표 가능')
print("\'\"") # 이스케이프 문자
print("aaaa\taaaa") # 탭을 의미한다.
print("\n") # 줄바꿈이다.

# 문자열 연산자
print("5","-"*50)
print("adsd"+"asds") # 문자열과 문자열을 연결
print("문자열"*3) # 문자열 반복 연산자
print("\n")

# 문자열 선택 연산자
print("6","-"*50)
print("abcde"[0])
print("abcde"[1])
print("abcde"[2])
print("abcde"[3])
print("abcde"[-1]) # 뒤에서부터 선택
print("\n")

# 문자열 범위 선택 연산자
print("7","-"*50)
print("안녕하세요"[0:5])
print("안녕하세요"[4:])
print("안녕하세요"[:5])
print("\n")

# 문자열의 길이 구하기
print("8","-"*50)
print(len("안녕하세요"))
print("\n")

# 자료형 확인하기
print("9","-"*50)
print(type("안녕하세요"))
print(type(len("안녕하세요")))
print("\n")

# 숫자
print("10","-"*50)
print(type(10))
print(type(1.1))
print("\n")

# 숫자 연산자
print("11","-"*50)
print(6+4)
print(6-4)
print(6*4)
print(6/4)
print(6%4)
print(6//4)
print(6**4)
print("\n")

# 변수
print("12","-"*50)
a = 'asd'
b = 123
print(type(a))
print(type(b))
print("\n")

# 복합대입 연산자
print("13","-"*50)
a=1
a+=10 # 나머지 연산도 같다
print(a)
string = "hello"
string += "!"
string += "?"
print(string)
print("\n")

# 입력
print("14","-"*50)
string = input("input: ") # 숫자로 입력해도 문자열로 인식받는다
print(string)
print("\n")

# 문자열을 숫자로 바꾸기
print("15","-"*50)
a = input("input: ")
print(type(a))
a = int(a)
print(type(a))
print("\n")

# 숫자를 문자열로 바구기
print("16","-"*50)
a = int(input("input: "))
print(type(a))
a = str(a)
print(type(a))
print("\n")

# 문자열의 format()함수
print("17","-"*50)
format = "{}".format(52273)
print(type(format), format)
print("\n")

# 정수출력의 다양한 형태
print("18","-"*50)
a = "{:010}".format(52)  # 0포함 코드를 특정칸에 출력
print(a)
a = "{:10}".format(52)
print(a)
print("\n")