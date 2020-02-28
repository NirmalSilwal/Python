import string
sen = input('enter sentence')
alphabets = list(string.ascii_lowercase)
# count = [0]*len(alphabets)
alphacounter={}

for i in alphabets:
    alphacounter[i]=0

for val in sen.lower():
    if val.isalpha():
        c=alphacounter.get(val)
        alphacounter[val]=c+1

if all(v>0 for k,v in alphacounter.items()):
    print('panagram')
else:
    print('not panagram')