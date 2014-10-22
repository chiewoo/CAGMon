import numpy as np
import scipy as sp
import math
from sklearn.metrics.cluster import normalized_mutual_info_score
from sklearn.metrics.cluster import mutual_info_score
#from data_process import file_splitter                                                                                                
from os import makedirs
from os.path import isdir, exists
from sys import exit

#in_file='ALL_S6_full_100ms_Unorm_combined.ann'                                                                                        
filename='GlitchData'
#in_dir='/Users/johnoh/MyMLA/AuX/S6/100msUnormFull'                                                                                    
work_dir='CorrMapMic'

if isdir(work_dir):
    print "Directory exists:", work_dir
else:
    print "Creating directory:", work_dir
    makedirs(work_dir)

#file_splitter(in_dir+'/'+in_file, filename, work_dir)                                                                                 

f=np.loadtxt(filename+'.txt')
mic=np.zeros((1250,1250))

for i in range(len(f.T)):
    for j in range(len(f.T)):
        mic[i][j] = normalized_mutual_info_score(f.T[i],f.T[j])
        print mic[i][j]
        g=open(work_dir+'/'+'CorrMatrixNMicG_1250.txt','a')
        if j==len(f.T):
            g.write(str(mic[i][j]))
            g.write('\n')
        else:
            g.write(str(mic[i][j]))
            g.write(' ')
        g.close()
print 'ALL JOBS DONE!'
