data=['nirmal','silwal','sagar','raju']

def find_longest_word(lst):
    wordmax=''
    maxlength=0
    index=0
    for i,data in enumerate(lst):
        if len(lst[i])>maxlength:
            maxlength=len(lst[i])
            index=i

    wordmax=lst[index]
    return wordmax
print(find_longest_word(data))
