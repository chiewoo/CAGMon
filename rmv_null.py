#/usr/bin/python

import numpy as np

data=np.loadtxt('transformed.txt')
cls=np.loadtxt('transformedres.txt')

for i in range(len(data)):
    temp=0
    f=open('rmvd_null.txt','a')
    g=open('rmvd_null_class.txt','a')
    for j in range(len(data[i])):
        temp+=data[i][j]
    if temp == 0:
        pass
    else:
        for k in range(len(data[i])):
            f.write(str(data[i][k]))
            f.write(' ')
        g.write(str(cls[i]))
        g.write('\n')
        f.write('\n')
    f.close()
    g.close()


    
