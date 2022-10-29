#Nested if else

#1
x=int(input("Enter any Number:"))
if x!=0:
    if x>0:
        print("+ve Number")
    else:
        print("-ve Number")
else:
    print("Zero")

#2
if x<=0:
    if x<0:
        print('-ve Number')
    else:
        print('Zero')
else:
    print('+ve Number')

#3
if x>=0:
    if x>0:
        print('+ve Number')
    else:
        print('Zero')
else:
    print('-ve Number')

#4
if x==0:
    print('Zero')
else:
    if x>0:
        print('+ve Number')
    else:
        print('-ve Number')

#5
if x>0 and x!=0:
    print('+ve Number')
else:
    if x<0:
        print('-ve Number')
    else:
        print('Zero')
