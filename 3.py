#to print n Natural Numbers

x=int(input("Enter the number you want to print:"))
for i in range(x):
    print(i+1)

#to print sum of n Natural Numbers
sum=0
for i in range(x):
    sum+=i+1
print('The sum of %d Natural numbers are %d'%(x,sum))
print('the sum of {} Natural Numbers are {}'.format(x,sum))
print('The sum of {0} Natural Numbers are {1}'.format(x,sum))
print('The sum of {c} Natural Numbers are {s}'.format(c=x,s=sum))
print('the sum of '+str(x)+' Natural Numbers are '+str(sum))