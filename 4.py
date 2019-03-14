ran = int(input('Enter range'))
a = range(ran)
for i in a:
    print(i)

for index in a:
    print(index,a[index])

num =[1,3,5,7,9]

for n in num:
    if n %2 == 0:
        print('Even present')
        break;
else:
    print('Only odd')
