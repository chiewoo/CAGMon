import numpy as np


###
#
#  Merging Matrix Files
#
###

print 'Merging the splitted data...'

l=[]
for k in range(50):
    l.append(k*25)

for i in l:
    f=open('CorrMatrix_MIC_1250_959126400_GlitchDataNoise_MIC_'+str(i)+'_'+str(i+25)+'.txt','r')
    print 'Reading the %d-th data...' %(i)
    g=open('CorrMatrix_MIC_1250_959126400_GlitchDataNoise_MIC_Merged.txt','a')
    print 'Writing the %d-th data...' %(i)
    while 1:
        data=f.readline()
        if not data: break
        g.write(str(data))
        g.write('\n')
    g.close()
    f.close()

###
# Checking the Merged Data
##

print 'Checking the merged data...'

f=np.loadtxt('CorrMatrix_MIC_1250_959126400_GlitchDataNoise_MIC_Merged.txt')
print 'Dimension of the Matrix=(%d, %d)' %(len(f), len(f.T))

print 'All Jobs Done!'
