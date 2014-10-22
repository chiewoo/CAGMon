#/usr/bin/env python

import numpy as np

f=open('S6/ALL_S6_full_set_0_evaluation.pat','r')
k=0
while 1:
    data = f.readline()
    if k < 1:
        pass
    elif k == 1:
        g=open('S6/ALL_S6_full_ch_names.txt','a')
        for i in range(4,1254):
            ch_names='_'.join(data.split(' ')[i].split('_')[:]).strip()
            g.write(ch_names)
            g.write('\n')
        g.close()
    elif k > 1:
        break
    k+=1
f.close()
