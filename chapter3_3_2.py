"""
다음 중첩 조건문에 논리 연산자를 적용해 하나의 if 조건문으로 만들어 주세요
"""
x = int(input("input number: "))

if x > 10:
    if x < 20:
        print("조건에 맞습니다.")

# 를 논리 연산자로 만들어 주면

if x > 10 and x < 20:
    print("조건에 맞습니다.")

# 이렇게 할수 있습니다.