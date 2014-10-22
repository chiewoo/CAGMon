import numpy as np

attrib=5
work_dir='CorrMapMic'

f=np.loadtxt(work_dir+'/'+'CorrMatrixNMicG_1250.txt').reshape([1250,1250,])

for i in range(0,len(f)/attrib):
    for j in range(0,len(f)/attrib):
        F=f[attrib*i:attrib*i+attrib, attrib*j:attrib*j+attrib]
        k=open(work_dir+'/'+'MaxRedMatrixNMICG.txt','a')
        MaxMIC=np.max(F)
        if j == len(f)/attrib-1:
            k.write(str(MaxMIC))
            k.write('\n')
        else:
            k.write(str(MaxMIC))
            k.write(' ')
        k.close()
print 'ALL JOBS DONE!'
