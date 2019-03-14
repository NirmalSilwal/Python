lst=['M','T','W','T','F','S','S']
total=int(input('enter total days of month: '))
startday=int(input('enter start day: '))
dic={}

for i in range(0,7,1):
    dic[i]=[]
# print(dic)
day=startday
for i in range(1,total+1,1):
    dic[day].append(i)
    if day<6:
        day=day+1

    else:
        day=0
# print(dic)

for k,v in dic.items():
    print(lst[k]+":"+str(v))