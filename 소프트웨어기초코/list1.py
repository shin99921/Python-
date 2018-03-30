# 리스트 인덱싱
print("1","-"*50)
a = [1,2,3,4]
print(a)
print(a[0],a[1],a[2],a[3])
print(a[0],a[2])
print(a[-1],a[-3])
print("\n")

# 리스트로 사칙연산도 가능
print("2","-"*50)
print(a[0]+a[2])
print(a[2]-a[0])
print(a[3]*a[2])
print(a[3]/a[2])
print("\n")

# 리스트 안이 리스트
print("3","-"*50)
b = [1,2,3,['a','b','c']]
print(b[0],b[-1])
# 리스트중의 리스트를 출력하려면 밑과 갗이 하면 된다
print(b[-1][0],b[-1][1])
print("\n")

# 리스트 슬라이싱
# a[start:end:step]
print("4","-"*50)
a = [1,2,3,4,5]
print(a[0:2])
print(a[0::2])
print(a[:3])
print("\n")

# 중첩된 리스트 슬라이딩
print("5","-"*50)
a = [1,2,3,['a','b','c','d'],4,5,6]
print(a[2:5])
print(a[3][1:])
print(a[3][:2])
print("\n")

# 리스트 연산자
print("6","-"*50)
a = [1,2,3]
b = [4,5,6]
print(a+b)
print(a*9)
print("\n")
# 리스트의 수정, 변경과 삭제

# 리스트 수정
print("7","-"*50)
a = [1,2,3]
a[1] = 4
print(a[0:])
a[1:2] = ['a','b','c']
print(a[0:])
a[1] = ['a','b']
print(a[0:])
print("\n")

# 리스트 삭제
print("8","-"*50)
a = [1,2,3,4,5]
print(a[0:])
a[1:2] = []
print(a[0:])
print("\n")

# del 함수 사용해서 리스트 삭제
print("9","-"*50)
a = [1,2,3,4,5]
print(a[0:])
del a[0]
print(a[0:])
del a[0:]
print(a[0:])
print("\n")


