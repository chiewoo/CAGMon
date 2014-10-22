import numpy as np

thrshd=0.8
M=np.loadtxt('MaxRedMatrixNMICG.txt')
f=open('GetIndexThrshd_'+str(thrshd)+'.txt','a')
for i in range(len(M)):
    for j in range(len(M)):
        if i==j:
            pass
        else:
            if M[i][j] > thrshd:
                f.write(str(i))
                f.write(' ')
                f.write(str(j))
                f.write(' ')
                f.write(str(M[i][j]))
                f.write('\n')
            else:
                pass
f.close()
print 'ALL JOBS DONE!'
