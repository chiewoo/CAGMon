import numpy as np

th=0.8
M=np.loadtxt('MaxRedMatrixNMICG.txt')
f=open('MaxRedMatrixNMICG_th'+str(th)+'.txt','a')
for i in range(len(M)):
    for j in range(len(M)):
        if j==len(M)-1:
            if M[i][j]>th:
                f.write(str(M[i][j]))
                f.write('\n')
            else:
                f.write('0.0')
                f.write('\n')
        else:
            if M[i][j]>th:
                f.write(str(M[i][j]))
                f.write(' ')
            else:
                f.write('0.0')
                f.write(' ')
f.close()
print 'ALL Jobs Done!'
