def overlapping(lis1,lis2):
    set1=set(lis1)
    set2=set(lis2)

    # if set1.isdisjoint(set2):
    #     return False
    # else:
    #     return True

    return not set1.isdisjoint(set2)

a=[1,2,3]
b=[2,3]
c=[44]

print('overlapping: ',overlapping(b,a))
