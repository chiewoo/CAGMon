import numpy as np

f=open('S6/ALL_S6_full_ch_names.txt','r')
k=0
while 1:
    data=f.readline()
    if not data: break
    if np.mod(k,5)==0:
        g=open('S6/ALL_S6_FullChannelNamesOnly.txt','a')
        ndat='_'.join(data.split('_')[:-1])
        g.write(ndat)
        g.write('\n')
        g.close()
    k+=1
    print k
f.close()
