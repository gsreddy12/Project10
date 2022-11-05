#to print the given number is polyndrom or not

number=input("Enter any number :")
for i in range(len(number)):
    if number[i]!=number[-1-i]:
        print('It is not a palindrome')
        break
else:
    print('It is a palindrome')


x=int(input("Enter Any Number:"))
num=x
sum=0
for i in range(len(str(x))):
    while(x!=0):
        m=x%10
        sum=sum*10+m
        x=x//10
if num==sum:
    print('Polyndrom')
else:
    print('Not Polyndrom')