from random import randint
import sys

start = int(input('enter start index: '))
end = int(input('enter last index: '))

random_number = randint(start, end)
sys.argv[0] = int(input('guess one number: '))
num_entered = sys.argv[0]
if num_entered == random_number:
    print('Correct! you are genius!')
else:
    while num_entered != random_number:
        sys.argv[0] = int(input('retry: '))
        num_entered = sys.argv[0]
    else:
        print('Correct! finally you did it!')


