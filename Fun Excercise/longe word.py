# lst=['hello','fello','galloer','damna','meriammoini']
# n = float(input('enter min word length: '))
#
# filterlambda = lambda x: len(x)>n
# lst1=[]
# for value in filter(filterlambda,lst):
#     lst1.append(value)
# print(lst1)

                          #ANOTHER WAY

filterlambda = lambda a: len(a)>n
def filter_long_words(lst,n):
    for value in filter(filterlambda,lst):
        print(value)

lst=['hello','fello','galloer','damna','meriammoini']
n = float(input('enter min word length: '))
filter_long_words(lst,n)
