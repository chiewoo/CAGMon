#/usr/bin/python

import numpy as np
import math
import os

f=open('ALL_S6_959126400_hveto_channels_signif_dt_set_0_training.ann','r')
while 1:
    data=f.readline()
    if not data: break
    g=open('transformed.txt','a')
    l=open('transformedres.txt','a')
    if len(data)<15 and data[1]==str(7):
        pass
    elif len(data)<15:
        l.write(data[0:-1])
        l.write('\n')
    else:
        g.write(data[0:-1])
        g.write('\n')
    g.close()
    l.close()
f.close()
