# 1.for 문을 이용하여 리스트[1,3,5,7,9]의 원소들의 합을 순서대로 다음과 같이 출력해 보자.
print("1","-"*50)

li = [1,3,5,7,9]
a = 0
for i in li:
    a += i
    print(i,a)

print()





# 2.for문을 이용해서 subject 리스트["국어","영어","수학","과학","한국사"] 의 원소를 순서대로 출력해 보자.
print("2","-"*50)

li = ["국어","영어","수학","과학","한국사"]

for i in li:
    print(i,end=" ")

print("\n")





# 3. for 문을 이용해서 name 리스트 ["홍길동","임꺽정"]과 subject 리스트 ["국어","영어","수학"]의 원소를 교차 반복 출력해 보자.
print("3","-"*50)

name = ["홍길동","임꺽정"]
subject = ["국어","영어","수학"]

for i in name:
    for j in subject:
        print(i,j)

print()





# 4. for 문과 range()함수를 이용하여 1부터 100까지의 모든 수의 합을 출력해 보자.
print("4","-"*50)

a = 0

for i in range(0,101):
    a += i
print(a)

print()






# 5.for 문과 range()함수를 이용해서 1부터 100까지의 모든 홀수의 합과 짝수의 합을 각각 계산하여 출력해 보자.
print("5","-"*50)

a = 0
b = 0

for i in range(0,101):
    if (i % 2 == 0):
        a += i
    else:
        b += i

print("짝수의 합:",a)
print("홀수의 합:",b)

print()






# 6.for 문과 range()함수를 사용하여 3부터 -3까지의 모든 수를 한 줄에 나열하여 출력하고, 모든 수의 합을 계산하여 출력 해보자.
print("6","-"*50)

a = 0

for i in range(3,-4,-1):
    a += i
    print(i,end=" ")

print()
print(a)
print()





# 7.for 문을 이용하여 반복하면서 num 리스트 [8,7,3,2,9,4,1,6,5] 의 원소중 가장 큰 수와 가장 작은 수로 출력 해보자.
print("7","-"*50)

import sys

a = sys.maxsize
b = -sys.maxsize
li = [8,7,3,2,9,4,1,6,5]

for i in li:
    if b < i:
        b = i

for i in li:
    if a < i:
        a = i

print("최댓값:",b)
print("최솟값:",a)

print()





# 8.두 개의 for 문을 중첩하여 반복하면서 다음 모양을 출력 해보자.
print("8","-"*50)

a = ["*","*","*","*","*"]
b = ["*","*","*"]

for i in a:
    print(i,end="")
    for j in b:
        print(j,end="")
    print()

print()






# 9.바깥쪽 한개의 for문과 안쪽 두개의 for문을 사용해서 반복하면서 다음 모양을 출력해보자.
print("9","-"*50)

for i in range(1,6):
    for j in range(1,i+1):
        print("*",end="")
    print()

print()






# 10.두개의 for문을 충첩시켜서 다음 모양을 출력해 보자.
print("10","-"*50)

for i in range(1,6):
    for j in range(1,6-i):
        print(" ",end="")
    for k in range(1,i+1):
        print("*",end="")
    print()

print()






# 11.바깥쪽 한개의 for문과 안쪽 새게의 for 문을 중촙시켜서 반복하면서 다음 모양을 출력해 보자.
print("11","-"*50)

for i in range(1,6):
    for j in range(1,6-i):
        print(" ",end="")
    for k in range(1,i+1):
        print("*",end="")
    for l in range(1,i):
        print("*",end="")
    print()

print()






# 12.while 문을 이용하여 반복하면서 정수를 입력받아 입력되 모든수의 합을 출력해 보자. 단 입력한 정수의 값이 0이 아니라면 반복을 계속 진행하고 0 이변 반복을 종료한다.
print("12","-"*50)

total = 0
n = int(input("input: "))

while(n != 0):
    total += n
    n = int(input("input: "))
print("합:",total)

print()







# 13.while 문을 이용하여 비밀번호를 입력받아 "pwpass"가 아닐경우 계속 비밀번호를 입력받고 "pwpass"가 입력될 경우 "LogIn Pass"를 출력해 보자.
print("13","-"*50)

password = input("input: ")

while (password != "pwpass"):
    password = input("input: ")

print("LogIn Pass!!")

print()







# 14.while문을 이용하여 무한반복을 하면서 정수를 입력받아 합을 계산해 보자. 단 입력한 정수값이 양수이면 합을 구하고 음수이면
# 합을 구하지 말고 계속 반복을 진행한다. 단 0인경우 반복을 종료하고 합을 출력한다.
print("14","-"*50)

n = 0
total = 0

while(True):
    n = int(input("input: "))
    if n < 0:
        continue
    total += n

    if n == 0:
        break
print(total)

print()






# 15.종이를 한번 접으면 원래 두께의 2배로 두꺼워진다 이렇게 접은 종이를 또 다시 접으면 종이 두께는 원래 종이 둒의 4배가 된다. 또 다시 접으면 8배가 된다.
# n번을 접으면 원래 두께에 2n을 곱한 수만큼 두께가 커지게 된다. 이런 과정을 계속해서 접은 두께가 100m(100000mm)를 넘으려면 두꼐가 1mm인 종이를 볓번 접어야 할지 계산 해보자.
print("15","-"*50)

n = 2
cnt = 0
total = 0

while (True):
    cnt += 1
    total = n**cnt
    print(cnt,"번 접으면",total,"mm")

    if total >= 100000:
        break

print("횟수:",cnt,"두께:",total)

print()