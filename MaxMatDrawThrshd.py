import numpy as np
import matplotlib.pyplot as plt
from pylab import *

mla='PCC'
Mdim=1250
attrib=5
nfilename='GlitchDataNoise_'+mla
GPS=959126400
thv=0.8
output_dir='.'
chan_input='/data/ligo/home/john.oh/MIC/Data/ALL_S6_FullChannelNamesOnly'

# =============================================================================                                                       
#                                                                                                                                     
#                    Select Max_value among all atrributes                                                                            
#                           & Generate reduced matrix                                                                                 
#                                                                                                                                     
# =============================================================================                                                      
 

f=np.loadtxt('CorrMatrix_'+mla+'_'+str(Mdim)+'_'+str(GPS)+'_'+nfilename+'.txt')
print 'Selecting maximum values and generating reduced matrix...'
for i in range(0,len(f)/attrib):
    for j in range(0,len(f)/attrib):
        F=f[attrib*i:attrib*i+attrib, attrib*j:attrib*j+attrib]
        k=open(output_dir+'/'+'MaxRedMatrix_'+mla+'_'+str(GPS)+'_'+nfilename+'.txt','a')
        MaxMIC=np.max(F)
        if j == len(f)/attrib-1:
            k.write(str(MaxMIC))
            k.write('\n')
        else:
            k.write(str(MaxMIC))
            k.write(' ')
        k.close()

# =============================================================================                                         
#                                                                                                                       
#                    Select Max_value among all atrributes                                                              
#                           & Generate reduced matrix                                                                   
#                                                                                
# =============================================================================  

if thv == 0.0 :
    pass
else:
    M=np.loadtxt(output_dir+'/'+'MaxRedMatrix_'+mla+'_'+str(GPS)+'_'+nfilename+'.txt')
    f=open(output_dir+'/'+'MaxRedMatrix_'+mla+'_'+str(GPS)+'_'+nfilename+'_th'+str(thv)+'.txt','a')
    for i in range(len(M)):
        for j in range(len(M)):
            if j==len(M)-1:
                if M[i][j]>thv:
                    f.write(str(M[i][j]))
                    f.write('\n')
                else:
                    f.write('0.0')
                    f.write('\n')
            else:
                if M[i][j]>thv:
                    f.write(str(M[i][j]))
                    f.write(' ')
                else:
                    f.write('0.0')
                    f.write(' ')
    f.close()
# =============================================================================                                               
#                                                                                                                             
#                            Draw Correlation Matrix                                                                          
#                                                                                                                             
# =============================================================================  


print 'Drawing correlation matrix map...'

if thv == 0.0:
    dat = np.loadtxt(output_dir+'/'+'MaxRedMatrix_'+mla+'_'+str(GPS)+'_'+nfilename+'.txt')
else:
    dat = np.loadtxt(output_dir+'/'+'MaxRedMatrix_'+mla+'_'+str(GPS)+'_'+nfilename+'_th'+str(thv)+'.txt')





###                                                                                                                                   
# if NaN appears, set to be zero                                                                                                      
###                                                                                                                                  
                                                                                                                                      
#dat2= np.nan_to_num(dat)                                                                                                             
#data=(dat2-np.min(dat2))/np.max(dat2-np.min(dat2))                                                                                   
#data=abs(dat)/np.max(abs(dat))                                                                                                       
                                                                                                                                   

rows, cols = np.indices((Mdim/attrib, Mdim/attrib))
#dat[np.diag(rows, k=0), np.diag(cols, k=0)]=0                                                                                       
 
if mla == 'MIC':
    data = (dat-np.min(dat))/np.max(dat-np.min(dat))
elif mla == 'PCC':
    dat2=np.nan_to_num(dat)
    data=abs(dat2)/np.max(abs(dat2))
elif mla == 'Ktau':
    data=abs(dat)/np.max(abs(dat))

colors = [('white')] + [(cm.jet(i)) for i in xrange(1,256)]
new_map = matplotlib.colors.LinearSegmentedColormap.from_list('new_map', colors, N=256)

lbs=open(chan_input+'.txt','r')
lbsdat=lbs.readlines()

column_labels = lbsdat
row_labels = lbsdat

if Mdim/attrib > 50:
    egc='k'
else:
    egc='None'

fig, ax = plt.subplots()
fig.set_size_inches(24,20)
heatmap = pcolor(data, cmap=new_map,edgecolors=egc)
colorbar()

ftsize=int(round(-0.05*(Mdim/attrib - 250)+3))

ax.set_xticks(np.arange(data.shape[0])+0.5, minor=False)
ax.set_yticks(np.arange(data.shape[1])+0.5, minor=False)
mpl.rc('text', usetex=False)
#fig.suptitle('Correlation Matrix via '+mla+' between SEI and GW channels of CLIO', fontsize=25, fontweight='bold')                  

fig.suptitle('Correlation Matrix via '+mla+' between Auxiliary channels of S6', fontsize=25, fontweight='bold')

ax.invert_yaxis()
ax.xaxis.tick_top()
plt.ylabel(str(GPS)+'_AuX_'+nfilename, fontsize=20)
plt.xlabel(str(GPS)+'_AuX_'+nfilename, fontsize=20)
plt.xticks(rotation=90)
ax.set_xticklabels(row_labels, minor=False, fontsize=ftsize)
ax.set_yticklabels(column_labels, minor=False, fontsize=ftsize)
#fig.savefig(output_dir+'/'+'CMatrix_'+mla+'_SEI_GW_CLIO_'+str(GPS)+'_'+nfilename+'.png',dpi=256)                                     
fig.savefig(output_dir+'/'+'CMatrix_'+mla+'_S6_Aux_'+str(GPS)+'_'+nfilename+'.png',dpi=256)
#plt.show()                                                                                                                          
 

print 'ALL JOBS DONE!'
