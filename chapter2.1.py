# 문자열의 추가적인 기능

# 대소문자 바꾸기
print("1","-"*50)
str_up = "hello python world"
str_low = "HELLO PYTHON WORLD"

str_up = str_up.upper()  # 모든 소문자가 대문자가 된다.
str_low = str_low.lower()  # 모든 대문자가 소문자가 된다.

print(str_up)
print(str_low)

print("\n")

# 문자열 공백제거
print("2","-"*50)
str_strip = "   Hello world    "
print(str_strip)
str_strip = str_strip.strip()  # 양쪽 공백을 제거(r은 오른쪽, l은 왼쪽)
print(str_strip)

print("\n")

# 문자열 찾기
print("3","-"*50)
str_find = "Hello World".find("H")
str_find2 = "Hello World".rfind("H")
print(str_find)  # 왼쪽에서부터 찾기
print(str_find2)  # 오른쪽에서부터 찾기

print("\n")

# in 연산자
print("4","-"*50)
print("He" in "Hellow world")
print("kk" in "Hellow world")

print("\n")

# 문자열 자르기
print("5","-"*50)
cut = "10 20 30 40 50"
print(cut.split(" "))  # 공백으로 나누겠다
cut = "10:20:30:40:50"
print(cut.split(":"))  # :으로 나누겠다
