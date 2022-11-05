#to find lcm and hcd of a given numbers

x=int(input("Enter the numbers you want to find LCM:"))
y=int(input("Enter the numbers you want to find LCM:"))
max=x if x>y else y
for i in range(1,max+1):
        if x%i==0 and y%i==0:
                gcd=i
lcd=(x*y)//gcd
print("The Lcd of a given numbers are %d"%(lcd))
print("The Gcd of a given numbers are %d"%(gcd))