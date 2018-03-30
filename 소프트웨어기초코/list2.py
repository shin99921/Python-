# 리스트에 요소추가
print("1","-"*50)
a = [1,2,3]
a.append(4)  # 한번에 하나씩만 가능한듯 하다.
a.append([1,2,3,4])
print(a)
print("\n")

# 리스트 정렬
print("2","-"*50)
a = [3,2,5,3,4,1]
print(a)
a.sort()  # 적은 숫자부터 차례로 나열한다.
print(a)

a = ['c','d','b','a']
print(a)
a.sort() # 역시 알파벳 순서대로 나열한다.
print(a)
print("\n")

# 리스트 뒤집기
print("3","-"*50)
a = [1,2,3,4,5]
print(a)
a.reverse() # 리스트 순서를 숫자 알파벳 모두 뒤집어 버린다.
print(a)
a.reverse() # 한번더 뒤집으면 원래대로 돌아온다.
print(a)
print("\n")

# 위치 반환
print("4","-"*50)
a = [1,2,3]
print(a.index(3),a.index(1)) # 리스트에 있는 x의 위치를 알려준다.
print("\n")

# 리스트의 요소 삽입
print("5","-"*50)
a = [1,2,3,4]
a.insert(0,0) # 0번째 위치에 0을 대입한다.
a.insert(1,45)
print(a)

# 리스트 요소 제거 (remove함수는 요소만을 삭제한다.)
#  리스트 요소 제거에는 remove함수, pop함수, del을 이용하는 방법이 있다.
print("6","-"*50)
a = [1,2,3,1,2,3]
a.remove(3) # 리스트안에 있는 3 하나를 삭제한다.
print(a)
a.remove(3)
print(a)
print("\n")

# 리스트 요소 끄집어내기 (pop은 인덱스로만 지울수 있다.)
print("7","-"*50)
a = [1,2,3,4,5]
print(a.pop()) # 맨 마지막 리스트를 뽑고 a 에 있는 맨 마지막 리스트를 삭제.
print(a)
print(a.pop(0))
print(a) # 0번째 리스트를 뽑고 리스트 0번재 있는 수를 제거.
print("\n")

# 리스트 개수 세기
print("8","-"*50)
a = [1,2,3,1]
print(a.count(1)) # 리스트에 있는 1들의 수를 센다.
print("\n")

# 리스트 확장
print("9","-"*50)
a = [1,2,3]
a.extend([1,2,3,'g']) # []안에 있는 모든 요소들이 리스트에 추가된다.
a = a+[4,5] # 이렇게도 추가할수 있다.
print(a)
a = [1,2,3]
b = [4,5]
c = 6
a.extend(b)
#a.extend(c) # 리스트가 아니면 추가되지 않는다.
print(a)
print("\n")

# del도 remove처럼 리스트 요소를 삭제하는 함수이므로 인덱스만 가능하다.