#To print table of a content

x=int(input("Enter the number you want to display the table:"))
for i in range(1,11):
    print("%d * %d = %d"%(x,i,x*i))

#To print the tables in between the numbers you want

a=int(input("Enter the number you want to display the table:"))
b=int(input("Enter the number you want to display the table:"))
for i in range(a,b+1):
    for j in range(1,11):
        print("%d * %d = %d"%(i,j,i*j))

#To print the Tables parallel

a=int(input("Enter the number you want to display the table:"))
b=int(input("Enter the number you want to display the table:"))
for j in range(1,11):
    for i in range(a,b+1):
        print("%d * %d = %d"%(i,j,i*j),end='\t')
    print('\n')

