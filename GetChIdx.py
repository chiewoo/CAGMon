import numpy as np

mla='PCC'
GPS=959126400
nfilename='GlitchDataNoise_'+mla
ths = 0.8

f=np.loadtxt('MaxRedMatrix_'+mla+'_'+str(GPS)+'_'+nfilename+'.txt')
g=np.loadtxt('../Data/ALL_S6_FullChannelNamesOnly.txt',dtype=np.str)
l=open('GetCorrelationChannels_'+mla+'_'+str(GPS)+'_'+'Th_'+str(ths)+'.txt','a')

print 'Correlation Threshold:', ths
l.write('Correlated Channels of AuxChannels of S6 by '+mla)
l.write('\n')
l.write(str(GPS)+'_threshold='+str(ths))
l.write('\n')
l.write('\n')
for i in range(len(f)):
    for j in range(i+1,len(f)):
        if f[i][j]> ths:
            print 'Channel 1:', g[i]
            print 'Channel 2:', g[j]
            print 'Correlation Value of '+mla+':', f[i][j]
            print '\n'
            
            l.write('Channel 1: '+g[i])
            l.write('\n')
            l.write('Channel 2: '+g[j])
            l.write('\n')
            l.write('Correlation Value of '+mla+': '+str(f[i][j]))
            l.write('\n')
            l.write('\n')
        
l.close()
