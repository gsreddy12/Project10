#To print the prime numbers

#to check Prime or not

x=int(input("Enter the number to print the Prime numbers upto:"))
ct=0
for i in range(1,x+1):
    if x%i==0:
        ct+=1
if ct==2:
    print('The given number %d is Prime Number'%(x))
else:
    print('The given number %d is Not Prime Number' % (x))

#Set of Prime Numbers

a=int(input("Enter the number to print the Prime numbers upto:"))
b=int(input("Enter the number to print the Prime numbers upto:"))
print("The Prime Numbers are :")
value=0
for i in range(a,b+1):
    ct=0
    for j in range(1,i+1):
        if i%j==0:
            ct+=1
    if ct==2:
        print(i,end='\t')
        value+=1
    #else:
        #print("The given number %d is Not Prime Number"%(i))
print("\nThe Total number of Prime numbers in between %d and %d are %d"%(a,b,value))