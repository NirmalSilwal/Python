op=open("input","r")
lst=[]
lst=op.readlines()
# print(lst)
# for i in op:
#     # print(i)
#     lst.append(i)
# print(lst)

newlst=[]
for i in lst:
    newlst.append(int(i.replace("\n","")))
print(newlst)
newlst.sort()
print(max(newlst))
newlst.reverse()
print(newlst)
newlst.reverse()
print(newlst)
