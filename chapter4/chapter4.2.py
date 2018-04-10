# 딕셔너리



# 딕셔너리 선언하기
print("1","="*50)

dic = {                    # 딕셔너리 선언
    "name":"shin",
    "age":20,
    "home":"gimhea"
}

print(dic)      # 딕셔너리 출력 은 랜덤으로 되는것 같다.
print()




# 딕셔너리 요소접근
print("2","="*50)

print(dic["name"])    # 딕셔너리 안에있는 name키의 value 값을 출력한다.
print(type(dic["name"]))     # 딕셔너리 안에 있는 value 값이 문자열이기 때문에 key값 name의 type은 str이다.
print(type(dic["age"]))     # 딕셔너리 안에 있는 value 값이 정수형 이기때문에 key 값 age의 type은 int이다.

print()

# 딕셔너리 value값 변경

dic["name"] = "jihong"       # 딕셔너리 안에있는 key값 name의 value값을 jihong으로 바꾸어 주었다.
print(dic["name"])        # 바꾸면 key값 name의 value값은 jihong으로 바뀐다.

dic["home"] = [1,2,3,4,5,6,7]     # 딕셔너리의 value값에는 list도 들어간다.
print(dic["home"])
print(type(dic["home"]))      # 타입은 list가 출력된다.

print()




# 딕셔너리 요소 추가
print("3","="*50)

dic = {}

print(dic)     # 현제 딕셔너리 dic안에는 어떠한 요소도 들어가 있지 않다.

dic["name"] = "hong"     # 이렇게 비어있던 딕셔너리에 key값 name과 value값 hong을 추가해줄수 있다.
print(dic)

dic["empty"] = ""       # 딕셔너리 value값 에는 공백도 들어간다.
print(dic)

dic[""] = ""      # 키값에도 공백이 들어갌 있다.
print(dic)

print()




# 딕셔너리 요소 삭제
print("4","="*50)

dic = {
    "name":"shin",
    "type":"human"
       }

del dic["name"]    # 딕셔너리 안에 있는 key값 name 요소를 삭제 하였다.
print(dic)

print()

# del dic["type"] = "human"
# del dic["type:"human]         딕셔너리 안에있는 value값을 지우는 방법은 없는것같다 교체만 가능한듯 하다.




# 딕셔너리 내부 키값 찾기
print("5","="*50)

dic = {
    "a":1,
    "b":2,
    "c":3
}

print(dic["a"])
# print(dic["d"])         존재하제 읺는 key에 접근하면 오류가 난다.
# if 문을 사용해셔 오류를 막을수 있다.

print()





# 딕셔너리 get함수
print("6","="*50)

dic = {
    "a":"a",
    "b":"b",
    "c":"c"
}

a = dic.get("c")      # c에 있는 value값을 추출 하였다.
print(dic)       # 추출 했을 때 .pop 이랑 다르게 딕셔너리 요소가 사라지지는 않는다.

print()

print(a)       # a에 추출된 값 c가 들어가였다.

print()





# for문을 딕셔너리와 함께 사용하기
print("7","="*50)

dic = {
    "a":1,
    "b":2,
    "c":3,
    "d":4
}

for key in dic:
    print(key, ":",dic[key])      # dic 만큼 반복될동안 dic에있는 key를 출력하여라.

# 출력은 랜덤으로 된다.