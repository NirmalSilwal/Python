sen=input('enter text: ')
def translate(txt):
    result=[]
    vowel=['a','e','i','o','u']
    for value in txt.lower():
        if value in vowel:
            result.append(value)
        else:
            result.append(value)
            result.append('o')
            result.append(value)
    return result
print("".join(translate(sen)))
# print(translate(sen))
