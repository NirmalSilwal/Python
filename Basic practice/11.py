dict1 ={1:'one',2:'two'}
print(dict1)
print(dict1.keys())

for i in dict1.keys():
    print(i,dict1.get(i))


for k,v in dict1.items():
    print(k,v)

print(dict1[1])
dict1[4] ='four'
print(dict1)

dict2 ={5:'five'}
dict1.update(dict2)
print(dict1)


