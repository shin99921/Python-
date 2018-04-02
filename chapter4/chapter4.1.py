# for
print("1","-"*50)
for i in range(10):  # i 가 10이 될때까지 출력한다.
    print("print")

print()



# list
print("2","-"*50)

array = [231,32,103,"str",True,False]  # 리스트를 선언한다.

print(array)  # 리스트 전체를 출력한다.

print()

print(array[0])   # 리스트 각 요소들을 출력한다.
print(array[1])
print(array[2])
print(array[1:4])  # 1부터 3까지 출력한다.
print(array[-1])   # 뒤에서 부터 1번째
print(array[-2])   # 뒤에서 2번째
print(array[-3])   # 위랑 같다.


array[0] = "change"   # 리스트 요소 0번째 를 change로 바꾼다.

print(array)

print()



# 리스트 연산자
print("3","-"*50)

# 리스트 선언
list_a = [1,2,3]
list_b = [4,5,6]

# 출력
print("list_a: ",list_a)
print("list_b: ",list_b)
print()

# 기본 리스트 연산자
print("list_a + list_b: ",list_a + list_b)
print("list_a*3: ",list_a*3)
print()

# 리스트 길이 구하는 함수
print("len(list_a): ",len(list_a))
print()




# 리스트에 요소 추가하기
print("4","-"*50)
array = [1,2,3]
array.append(4)   # 리스트 맨끝에 4를 추가한다.
array.append(5)   # 리스트 맨끝에 5추가
print(array)
print()

# 리스트 중간에 요소 추가하기
array.insert(0,0)   # 0번째에 0추가
print(array)
print()

# 리스트 extend 함수
list_1 = [1,2,3]
list_1.extend([4,5,6])   # 리스트에 4,5,6을 추가함
print(list_1)
print()

# 리스트 연결 연산자는 리스트 원본을 건들지 않는다.
# extend 함수는 원본을 바꾸어 보인다.
# append, insert, extend 함수들은 모두 원본에 영향을 준다.



# 리스트 요소 제거하기
print("5","-"*50)

# 인덱스로 제거하기
list_a = [1,2,3,4]
del list_a[1]
print(list_a)   # 1번의 리스트가 제거 되었다.
print()

# 인덱스로 여러개 한꺼번에 제거하기
list_a = [1,2,3,4,5,6,7,8]
del list_a[3:7]    # 3번째부터 6번째까지 삭제
print(list_a)
print()

# pop
list_a = [1,2,3,4]
print(list_a.pop(0))   # 0번째 요소를 뽑는다.
print(list_a)
a = list_a.pop(0)
print(a)
print()

# 값으로 제거하기
print("-"*50)

# remove
list_a = [1,2,3,4,5,1,2,3,4,5]
list_a.remove(1)    # 가장 앞쪽에 있는 1 이라는 값을 제거한다.
print(list_a)
print()

# clear
list_a = [1,2,3,4,5,6,7,8,9,10]
list_a.clear()   # 모든 요소 삭제하기
print(list_a)
print()



# 리스트 내부에 있는지 확인
print("6","-"*50)
array = [1,2,3,4,5]
print(1 in array)     # 1이 요소안에 있다.
print(123 in array)   # 123은 요소에 없다.
print()


# for 반복문 list와 함께 사용하기
print("7","-"*50)
array = [123,4234,5,2678,98534]

for i in array:   # array 요소를 모두 출력한다.
    print(i)

print()

for i in "abcdefg":
    print(i)


