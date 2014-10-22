import numpy as np

ColSize=1250
MtxSize=ColSize*ColSize
BmtxColSize=5

A=np.linspace(0,MtxSize-1,MtxSize).reshape([ColSize,ColSize,])
print 'Orginal Matrix:'
print A
print 'Decomposed Matrices with the size:', BmtxColSize
C=[]
for i in range(0,len(A)/BmtxColSize):
    for j in range(0,len(A)/BmtxColSize):
        B= A[BmtxColSize*i:BmtxColSize*i+BmtxColSize,BmtxColSize*j:BmtxColSize*j+BmtxColSize]
        print B
        f=open('MaxRedMatrix.txt','a')
        C=np.max(B)
        print 'max:', C
        if j == len(A)/BmtxColSize-1:
            f.write(str(C))
            f.write('\n')
        else:
            f.write(str(C))
            f.write(' ')
        f.close()
print 'ALL JOBS DONE!'
