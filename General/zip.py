countries={'uk','usa'}
curr={'pound','dollar'}
a=(zip(countries,curr))
# for i in a:
#     print(i)
d={}
for k,v in a:
    d[k]=v
print(d)