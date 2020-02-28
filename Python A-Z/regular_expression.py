import re

# my_string = 'this is search for this inside of this text!'

# print('search' in my_string)

# a = re.search('this',my_string)
# # print(a.span())
# print(a.group())
# print(a.start())
# print(a.end())

# pattern = re.compile('this')
# a = pattern.search(my_string)
# print(a)
#
# b = pattern.findall(my_string)
# print(b)

# c = pattern.fullmatch(my_string)
# print(c)
# pattern2 = re.compile('search this ')
# d = pattern2.fullmatch(my_string)
# print(d)

# e = pattern2.match(my_string)
# print(e)

# password checker

password = re.compile(r"[a-zA-X0-9@#$]{7,}[0-9]")

check = password.fullmatch('ssdhs9t@#$8')
print(check)