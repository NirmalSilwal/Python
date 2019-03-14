fname=input('enter name of file: ')
content= input('enter content: ')
o = open("input",'w')
o.write(content)
o.close()

ip=open("input",'r')
# print(ip.read(5))
lst=ip.readlines()
# print(lst)
# print("".join(lst))

# nl=[]
# for index,data in enumerate(lst):
#     nl.append(data.replace("\n"," "))
# print(nl)