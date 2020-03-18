import sys 
from guess import *
try:
    l = int(sys.argv[1])
    r = int(sys.argv[2])
    ans = setAnswer(l, r)
    startGame(ans, l, r)
except IndexError as ie:
    print('Out of range')
except ValueError as ve:
    print('Enter integer number')


    


