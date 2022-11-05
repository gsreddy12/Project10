#to check whether the given number is Armstrong or not

x=int(input("Enter Any Number:"))
num=x
sum=0
y=len(str(x))
p=y
for i in range(y):
    while(x!=0):
        m=x%10
        sum=sum+m**p
        x=x//10
if num==sum:
    print('Armstrong Number')
else:
    print('Not Armstrong Number')