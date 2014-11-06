import numpy as np
import scipy as sp
import math
import os
import glob
import hotshot, hotshot.stats
import sys
import matplotlib as mpl
import matplotlib.pyplot as plt

from pylab import *

print 'Drawing correlation matrix map...'


##### Parameter Setup ######

Mdim=1250
attrib=5
output_dir='../MIC/MICBack'
chan_dir='../Pearsons/S6'
in_file='MaxRedMatrixNMIC.txt'
chan_name='ALL_S6_FullChannelNamesOnly.txt'
fig_name='CMapNMICBack.png'

dat = np.loadtxt(output_dir+'/'+in_file)

###                                                                                                                                                       
# if NaN appears, set to be zero                                                                                                                          
###                                                                                                                                                       
#                                                                                                                                                         
#dat2= np.nan_to_num(dat)                                                                                                                                 
#data=(dat2-np.min(dat2))/np.max(dat2-np.min(dat2))                                                                                                       
#data=abs(dat)/np.max(abs(dat))                                                                                                                          

##### Drawing Correlation Matrix ###########

rows, cols = np.indices((Mdim/attrib, Mdim/attrib))
dat[np.diag(rows, k=0), np.diag(cols, k=0)]=0
data = (dat-np.min(dat))/np.max(dat-np.min(dat))

colors = [('white')] + [(cm.jet(i)) for i in xrange(1,256)]
new_map = matplotlib.colors.LinearSegmentedColormap.from_list('new_map', colors, N=256)

lbs=open(chan_dir+'/'+chan_name,'r')
lbsdat=lbs.readlines()

column_labels = lbsdat
row_labels = lbsdat

fig, ax = plt.subplots()
fig.set_size_inches(24,20)
heatmap = pcolor(data, cmap=new_map)
colorbar()

ax.set_xticks(np.arange(data.shape[0])+0.5, minor=False)
ax.set_yticks(np.arange(data.shape[1])+0.5, minor=False)
mpl.rc('text', usetex=False)
fig.suptitle('Correlation Map via Mutual Information Coefficient between 250 Auxiliary Channels', fontsize=25, fontweight='bold')
ax.invert_yaxis()
ax.xaxis.tick_top()
plt.xticks(rotation=90)
ax.set_xticklabels(row_labels, minor=False, fontsize=3)
ax.set_yticklabels(column_labels, minor=False, fontsize=3)
fig.savefig(output_dir+'/'+fig_name, dpi=1024)
#plt.show()                                                                                                                                                

print 'ALL JOBS DONE!'
