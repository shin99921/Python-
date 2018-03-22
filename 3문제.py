# q1.다음 변수명중 올바른것과 올바르지 않은것을 구분하고 올바르지 않은경우 그 이유를 설명하시오.
# 1.abc 2.3ab 3.a b 4.import 5.import_var 6.test 7.temp# 8.k31

# 3ab는 숫자가 앞에오면 안됨
# a b 는 공백이 있으므로 안됨
# import 지정된 예약어라서 안됨
# temp# 는 특수문자가 포함되어서 지정불가
# 영문자와 숫자, 밑줄문자(_)로 이루어진다, 중간에 공백이 사용되면 안된다, 첫 글자는 반드시 영문자 또는 밑줄문자(_)이어야 아며 숫자로는 시작불가
# 대문자와 소분자는 구별된다.
# if,while,for 등의 파이썬 예약어는 사용불가.

# q2.다음 문장들 중 문제점이나 오류가 발생하는 것은 무엇인가? 또한 문제점이나 오류가 발생하는 이유는 무엇인지 확인해보라.
# a=3
# c=a+b+1
# a=3, c=a+b+1 에서 오류가 나는 이유는 변수b가 지정되지 않았기 때문이다.

# q3.다음 문장들을 실행한 후의 각 변수의 값은 무엇인지 확인해보자.
# a=3
# b=2
# c=1
# a=a+1
# b=b
# c=a+b
# c=c+1
a=3
b=2
c=1
a=a+1
b=b
c=a+b
c=c+1
print(a,b,c)

#4
subject=input("subject: ")
score=int(input("socre: "))
print("선호과목:",subject,"점수:",score)

#5
a=int(input("int1: "))
b=int(input("int2: "))
c=int(input("int3: "))
sum=a+b+c
print("a: ",a,"b: ",b,"c: ",c)
print("sum: ",(sum),"ave: ",(sum/3))

#6
a=int(input("int: "))
b=str(a)
print(a,type(a),b,type(b))

