##a=int(input('enter first number: '))
##b=int(input('enter second number: '))
##c=int(input('enter third number: '))
##if a>b:
##    if a>c:
##        print(a, "is highest")
##    else:
##        print(c, "is highest")
##else:
##    if b>c:
##        print(b, "is highest")
##    else:
##        print(c, "is highest")
##    
##    


lst=[]
print(lst)
n=int(input('Enter total elements in the list: '))
for i in range(n):
    number = int(input('enter number '))
    lst.append(number)
    print(lst)
print(lst)
max=lst[0]

for k in range(1,n,1):
    if lst[k]>max:
        max=lst[k]
print('largest number is ', max)

    ##print(lst[j])
##lst.sort
##c=lst.count
##print(c)
