import matplotlib
from pylab import *
import matplotlib.pyplot as plt
import numpy as np


#Create new colormap, with white for zero 
#(can also take RGB values, like (255,255,255):
data = np.random.random_sample((250, 250))
rows, cols = np.indices((250, 250))
data[np.diag(rows, k=0), np.diag(cols, k=0)]=0
colors = [('white')] + [(cm.jet(i)) for i in xrange(1,256)]
new_map = matplotlib.colors.LinearSegmentedColormap.from_list('new_map', colors, N=256)

lbs=open('S6/ALL_S6_FullChannelNamesOnly.txt','r')
lbsdat=lbs.readlines()

column_labels = lbsdat
row_labels = lbsdat
#data = np.random.rand(20,20)
fig, ax = plt.subplots()
fig.set_size_inches(24,20)
heatmap = pcolor(data, cmap=new_map)
colorbar()

# put the major ticks at the middle of each cell
ax.set_xticks(np.arange(data.shape[0])+0.5, minor=False)
ax.set_yticks(np.arange(data.shape[1])+0.5, minor=False)

# want a more natural, table-like display
fig.suptitle('Correlation Map via Mutual Information Coefficient between 250 Auxiliary Channels', fontsize=25, fontweight='bold')
ax.invert_yaxis()
ax.xaxis.tick_top()
plt.xticks(rotation=90)
ax.set_xticklabels(row_labels, minor=False, fontsize=3)
ax.set_yticklabels(column_labels, minor=False, fontsize=3)
fig.savefig('CMapMIC.png',dpi=500)
plt.show()

#pcolor(data, cmap=new_map)
#colorbar()
#savefig('map.png')
#show()
