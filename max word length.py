lst=['aaa','bbbb','ccccc']
lenlst=[]
for i,v in enumerate(lst):
    lenlst.append(len(v))
# print(lenlst)
maxlen=max(lenlst)
print(maxlen)
print(lst[lenlst.index((maxlen))])