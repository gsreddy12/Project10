#to check whether the given number is Armstrong or not

x=int(input("Enter Any Number:"))
act=0
nact=0
for i in range(0,x+1,1):
    num1=i
    #print(x,i)
    y = len(str(i))
    p = y
    #print(p,y)
    sum=0
    while(i>0):
        m=i%10
        sum=sum+m**p
        i=i//10
    if num1==sum:
        print('%d is Armstrong Number'%(num1))
        act+=1
    else:
        #print('%d is Not Armstrong Number'%(num1))
        nact+=1
print('Armstrong numbers in between 0 and %d is %d'%(x,act))
print('Not Armstrong numbers in between 0 and %d is %d'%(x,nact))