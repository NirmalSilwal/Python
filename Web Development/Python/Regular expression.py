import re

patterns = ['term1', 'term2']

text = 'this is the string with term1, and not the other'

for pattern in patterns:
    print('I am searching for ', pattern)

    if re.search(pattern, text):
        print('MATCH')
    else:
        print('DID NOT MATCH')

# ===============================================================================================
# ===============================================================================================
text = 'test me'
match = re.search('test', text)
print(match)
print(match.start())
print(match.end())

# ===============================================================================================

split_term = '@'
mail = 'user@gmail.com'

match = re.split(split_term, mail)
print(match)

# ===============================================================================================

print(re.findall('match', 'i am tested for match string here'))
print(re.findall('match', 'i am tested for match string here, match me'))