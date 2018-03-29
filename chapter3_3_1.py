"""
 다음 코드의 실행 결과를 예측해 주세요.
 아래의 코드는 모두 같고, 입력 결과가 다른 경우입니다.
"""

# 1
x = 2
y = 10

if x > 4:
    if y > 2:
        print(x*y)
else:
    print(x+y)

# x가 4를 넘지 않아서 x+y를 해서 12가 된다.


# 2
x = 1
y = 4

if x > 2:
    if y > 2:
        print(x*y)
else:
    print(x+y)

# x가 2를 넘지 않기 때문에 x+y를 하면 5이다.


# 3
x = 10
y = 2

if x > 4:
    if y > 2:
        print(x*y)
else:
    print(x+y)

# x는 4를 넘지만 y가 2를 넘지 않아서 아무것도 출력않됨.


