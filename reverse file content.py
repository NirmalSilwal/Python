ip = open("input.txt","r")

lst = ip.readlines()

lst.reverse()
lst.insert(1,'\n')

ip.close()

op = open("output.txt",'w')
op.write("".join(lst))
op.close()
