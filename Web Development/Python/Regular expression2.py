import re


def multi_find(patterns, phrase):

    for expression in patterns:
        print(f'searching for pattern {expression}')
        print(re.findall(expression, phrase))
        # print('\n')


test_text = 'sdsd..sssddd..sdddsddd...dsds...dssssss...sddddd'

print('s followed by zero or more d')
test_pattern = ['sd*']
multi_find(test_pattern, test_text)

print('s followed by one or more d')
multi_find(['sd+'], test_text)

print('\n s followed by 2d:')
multi_find(['sd{2}'], test_text)

print('\n s followed by 1 or 3 d:')
multi_find(['sd{1,3}'], test_text)

print('\n s followed by 1 or more s OR 1 or more d:')
multi_find(['sd[sd]+'], test_text)

multi_find(['[a-z]+'],'I am lower case charaCTER being Checked!')
multi_find(['[A-Z]+'],'I am upper case charaCTER being Checked!')

multi_find([r'\d'], 'i am sentence containing digits 89 and numbers 1234 here for test for digits')
multi_find([r'\d+'], 'i am sentence containing digits 89 and numbers 1234 here for test for digits+')

multi_find([r'\D+'], 'i am sentence containing digits and numbers 1234 here for test for non-digits')