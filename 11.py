#to pring fibonacci series

a=0
b=1
x=int(input('Enter the number you want:'))
for i in range(1,x+1):
  print(a,end='\t')
  c=a+b
  a=b
  b=c