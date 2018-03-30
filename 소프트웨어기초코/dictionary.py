# 딕셔너리
print("1","-"*50)
a = {1: 'hi'}
print(a)
print(a[1])
a = {'a': [1,2,3]}
print(a)
print("\n")

# 딕셔너리 쌍 추가
print("2","-"*50)
a =  {1: 'a'}
print(a)
a[2] = 'b'
print(a)
a['name'] = 'pey'
print(a)
a[3] = [1,2,3]
print(a)
print(a[3][2])
print("\n")

# 딕셔너리 요소 삭제하기
print("3","-"*50)
del a[1] # 키값이 1인 딕셔너리 요소를 삭제한다.
print(a)
a[1] = 'a'
print(a)
a.pop(1) # pop 함수도 인식된다.
print(a)
print("\n")

# 중복값 무시
print("4","-"*50)
a = {1:'a',1:'b',1:'c'}
print(a) # 중복되는 값이 있으면 가장 마지막의 key 값을 사용한다.
print("\n")

# 딕셔너리에서는 리스트는 사용할수 없다.
# a = {[1,2]:'a'}
# print(a)  오류가 난다.

# 딕셔너리 키 리스트 만들기
print("5","-"*50)
a = {'name':'shin', 'num':'010', 'birth':'1999'}
print(a.keys())  # 딕셔너리에 있는 모든 키를 출력한다.
for a in a.keys():  # 이런식으로도 출력가능
    print(a)
print("\n")

# 딕셔너리 키값들을 모아서 리스트로 만든다.
a = {1:1.1, 2:2.2, 3:3.3}
print(list(a.keys()))
print("\n")

# 딕셔너리 value 리스트 만들기
a = {1:1.1, 2:2.2, 3:3.3}
print(a.values())
print("\n")

# key,value쌍 얻기
print("6","-"*50)
a = {1:1.1, 2:2.2, 3:3.3}
print(a.items())
print("\n")

# 쌍 모두 지우기
a.clear()
print(a)
print("\n")

# key 로 value 얻기
print("7","-"*50)
a = {'name':'pey', 'phone':'0119993323', 'birth': '1118'}
print(a.get('name'))  # 동일한 결과
print(a['name'])      # 동일한 결과
print("\n")

# 해당 key가 딕셔너리 안에 있는지 조사하기
print("8","-"*50)
a = {'name':'pey', 'phone':'0119993323', 'birth': '1118'}
print('name' in a)
print('pey' in a)  # 키값은 인식되지 않는다.
print('phone' in a)