#test
a=input("input: ")
print(a,type(a),len(a))

cnt = 0
for i in range(len(a)):
         cnt = cnt+1

print(cnt)

for i, t in enumerate(a):
    print(i, t)

print(i+1)

for i,t in enumerate("abcd"):
    print(i,t)


temp = ["Abc", "d", "E"]

for i, t in enumerate(temp):
    print(i, t)

for i in range(len(temp)):
    print(temp[i])
