str=input('enter the main string')
sub=input('enter the sub string ')
n=str.find(sub,0,len(str))
if n==-1:
    print('sub string not found')
else:
    print('sub string find the position"', n+1)
    
