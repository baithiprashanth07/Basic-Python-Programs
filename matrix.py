mat=[[1,2,3],[4,5,6],[7,8,9]]
print('display the list is:')
print(mat)
print ('display the row by row',)
for r in mat:
    print(r)
print('display the each coloumn in row 0:')
for c in mat[0]:
    print(' %d' %c, end='')
print()
print('display the each coloumn in row 1:')
for c in mat[1]:
    print(' %d' %c, end='')
print()
print('display the each coloumn in row 2:')
for c in mat[2]:
    print(' %d' %c, end='')
print()
print('display the all elements for all:')
for r in mat:
    for c in r:
        print(c, end='')
    print()

print('display the all elememts using for:')
for i in range(len(mat)):
    for j in range(len(mat)):
        print('%d' %mat[i][j], end='')
    print()
