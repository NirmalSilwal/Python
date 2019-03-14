with open('hello.txt','r+') as ip:
    # print('file name is :', ip.name)
    # singleline=ip.readline()
    # print(singleline)

    for x in ip:
        print(x)
