# for 범위지정
print("1","="*50)

print(range(5))    # range 타입 범위를 5 까지 지정한다.
print(type(range(5)))      # range 의 타입은 range였다.

print()

print(list(range(5)))     # 리스트 범위를 5 까지 지정해준다.
print(type(list(range(5))))      # list(range(5))의 타입은 리스트 이다.

print()

print(range(3,8))              # 범위를 3~8까지 지정하였다. 중간부터도 범위 지정이 가능하다.
print(type(range(3,8)))          # 역시나 range의 타입은 range이다.

print()

print(list(range(5,20)))        # 리스트 범위를 5~20까지 지정 하였다. 범위 지정방식은 모든 파이썬에서는 맨 마지막 숫자에서 -1한 값까지가 범위이다.
print(type(list(range(5,20))))            # 리스트 타입은 역시나 리스트 이다.

print()

print(range(0,5,2))               # start end step 형식으로 range 범위를 지정 하였다.
print(type(range(0,5,2)))

print()

print(list(range(0,10,2)))           # list 형식으로 start end step 범위가 지정된다.
print(type(list(range(0,10,2))))

print()





# for 문 범위와 함께 사용하기
print("2","="*50)

for i in range(10):          # range 의 범위만큼 출력이 된다.
    print(i)


# for i in range(10,2):          # 큰 수가 앞에오면 아무것도 출력되지 않는다.
    # print(i)

print()

for i in range(0,10,2):            # start end step 형식으로 출력 하였다.
    print(i)

print()

for i in range(-20,0):           # -형식 으로도 출력이 가능하다.
    print(i)

print()

for i in range(-20,0,2):           # -형식에 start end step 적용
    print(i)

print()







# 리스트와 for 문 합성
print("3","="*50)

array = [10,20,2,45,75,99,34]           # 리스트를 지정하였다.
a = 0

for i in array:
    a+=1
    print(a,":",i)

print()

for i,t in enumerate(array):           # enumerate 함수를 사용해서 출력하는 방법이다.
    print(i,t)

print()

for i in reversed(range(10)):         # 10에서 -1을 한 값만큼 큰수부터 거꾸로 출력한다.
    print(i)

print()
