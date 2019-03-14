text = input('enter any text: ')

def translate(line):
    result=[]
    for x in line.lower():
        if x in ['a','e','i','o','u']:
            result.append(x)
        else:
            result.append(x)
            result.append('o')
            result.append(x)
    return result

print("".join(translate(text)))