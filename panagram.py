import string

sen=input('enter sentence: ')

alphabets=list(string.ascii_lowercase)

count = [0]*len(alphabets)

alphacount={}

for i in alphabets:
    alphacount[i]=0

for x in sen.lower():
    if x.isalpha():
        c = alphacount.get(x)
        alphacount[x]=c+1

if all(v>0 for k,v in alphacount.items()):
    print('panagram')
else:
    print('not panagram')

# TEST CASE:
# "The quick brown fox jumps over the lazy dog." >> this is panagram
# 'i am learning programming' >> not panagram



