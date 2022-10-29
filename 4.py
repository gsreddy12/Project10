#To print even or odd numbers in between the given numbers

#Even numbers

x=int(input("Enter the numbers you want to display:"))
y=int(input("Enter the numbers you want to display:"))
count=0
evensum=0
for i in range(x,y+1):
    if i%2==0:
        print('Number %d is Even'%(i))
        count+=1
        evensum+=i
print("The Even numbers in between {} and {} is {}".format(x,y,count))
print('The sum of Even Numbers in between {} and {} is {}'.format(x,y,evensum))

#Odd Numbers
count=0
oddsum=0
for i in range(x,y):
    if (i+1)%2==0:
        print('Number %d is Odd'%(i))
        count+=1
        oddsum+=i
print('The Odd numbers in between {} and {} is {}'.format(x,y,count))
print('The sum of Odd Numbers in between {} and {} is {}'.format(x,y,oddsum))