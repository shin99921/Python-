"""
사용자에게 태어난 년도를 입력받아 그 해의 띠를 출력하는 프로그램을 작성해 주세요.
"""
# HINT : 입력받은 년도를 12로 나눈 나머지를 사용합니다.

year = int(input("input year : "))
y = year % 12   # 띠 구하는 공식을 y로 받음


if y == 0:
    print("원숭이띠 입니다.")
elif y == 1:
    print("닭띠 입니다.")
elif y == 2:
    print("개띠 입니다.")
elif y == 3:
    print("돼지띠 입니다.")
elif y == 4:
    print("쥐띠 입니다.")
elif y == 5:
    print("소띠 입니다.")
elif y == 6:
    print("범띠 입니다.")
elif y == 7:
    print("토끼띠 입니다.")
elif y == 8:
    print("용띠 입니다.")
elif y == 9:
    print("뱀띠 입니다.")
elif y == 10:
    print("말띠 입니다.")
else:
    print("양띠 입니다.")