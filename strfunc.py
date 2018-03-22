a = "hobby"
print(a.count('b')) #산택한 문자가 한 문장에 몇가지가 있는지 알려준다.

a = "Python is very fun"
print(a.find('y'))
print(a.find('P'))
print(a.find('b')) #없는 문자는 거짓(-1)로 출력된다.

a = "Lief is too short"
print(a.index('t'))
#print(c.index('k')) #-1이 출력되지 않고 오류가 난다.

a = ","
print(a.join('abcd')) #문자 사이사이에 변수에있는 문자를 대입한다.

a = "hi"
print(a.upper()) #소문자를 대문자로 바꿔준다.

a = "HI"
print(a.lower()) #대문자를 소문자로 바꿔준다.

a = " hi "
print(a.lstrip()) #왼쪽 공백을 지운다.
print(a.rstrip()) #오른쪽 공백을 지운다.
print(a.strip()) #양쪽 공백을 지운다.

a = "Life is too short"
print(a.replace("Life","Your leg")) #문자를 바꿔준다.

a = "Life is too short"
print(a.split()) #아무것도 지정하지 않으면 공백으로 문장을 나눠주고.
a = "a:b:c:d"
print(a.split(':')) #지정해준 문자를 기준으로 문자열을 나눈다.

