import matplotlib
from pylab import *
import matplotlib.pyplot as plt
import numpy as np


#Create new colormap, with white for zero                                                                                                                      
#(can also take RGB values, like (255,255,255):                                                                                                                

dat = np.loadtxt('MaxRedMatrixNMICG.txt')
#dat2= np.nan_to_num(dat)                                                                                                                                      
#data=(dat2-np.min(dat2))/np.max(dat2-np.min(dat2))                                                                                                            
#data = abs(dat)/np.max(abs(dat))                                                                                                                              

rows, cols = np.indices((250, 250))
dat[np.diag(rows, k=0), np.diag(cols, k=0)]=0
data = (dat-np.min(dat))/np.max(dat-np.min(dat))

colors = [('white')] + [(cm.jet(i)) for i in xrange(1,256)]
new_map = matplotlib.colors.LinearSegmentedColormap.from_list('new_map', colors, N=256)

lbs=open('../S6/ALL_S6_FullChannelNamesOnly.txt','r')
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
.png',dpi=500)                                                                                                                                                 
#plt.show()                                                                                                                                                    
print 'All Jobs Done!'                                                                                                                                         
                                                                                                                                                               
#pcolor(data, cmap=new_map)                                                                                                                                    
#colorbar()                                                                                                                                                    
#savefig('map.png')                                                                                                                                            
#show()                                                                                                                                                        
