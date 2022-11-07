import sys

args=sys.argv[1: ]
print(args)

sum=0
for i in args:
    x = int(input('enter a number'))
    if x%2==0:
        sum+=x
print('sum of evens=', sum)
