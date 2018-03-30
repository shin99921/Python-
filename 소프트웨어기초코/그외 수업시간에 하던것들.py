#1
a=9
b=a
c=a+b
print(c)

#2
a=b=c=d=1
print(a,b,c,d)

e,f=1,2
print(e,f)

#3
num=input("학번 : ")
name=input("이름 : ")
print("학번 :",num, "이름 :",name)

#4
x=3
y=4

print(x,y)

t=x
x=y
y=t

print(x,y)

a=1
b=2


a,b,=b,a
print(a,b)

#5
x=int(input("number : "))
y = x+1
print(y)

#6
x=int(input("num : "))
y=int(input("num : "))

print(x+y)

#7
num1=10
num2=21.3125673258
ch="shin"
print(num1,type(num1))
print(num2,type(num2))
print(ch,type(ch))


#8
x=True
y=False

print(x*2)
print(y*2)

#x는 참이라서 1이고 y는 거짓이라서 0이다.

#9
num1=int(input("input num1 : "))
num2=int(input("input num2 : "))

print(num1,"+",num2,"=",(num1+num2))
print(num1,"-",num2,"=",(num1-num2))
print(num1,"*",num2,"=",(num1*num2))
print(num1,"/",num2,"=",(num1/num2))
print(num1,"%",num2,"=",(num1%num2))
print(num1,"//",num2,"=",(num1//num2))

#10
a=int(input("input:"))
b=int(input("input:"))

print("%d+%d=%d"%(a,b,(a+b)))
print("%d-%d=%d"%(a,b,(a-b)))
print("%d*%d=%d"%(a,b,(a*b)))
print("%d/%d=%d"%(a,b,(a/b)))
print("%d//%d=%d"%(a,b,(a//b)))
print("%d% %%d=%d"%(a,b,(a%b)))
