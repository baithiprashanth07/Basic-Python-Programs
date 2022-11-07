x=[]
print('how many elements?', end='')
n= int(input())
for i in range(n): 
     print('enter element:', end='')
     x.append(int(input()))
print('the list is:',x)
y=int(input('enter elemnets to count:'))
c=0
for i in  x:
    if(y==i):
        c+=1
print('{} is found {} times.'.format(y,c))
