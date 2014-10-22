import numpy as np

ChannFile=open('S6/100msUnormFull/nmifs175/chan35list.txt','r')

NewChList=[]
ChannFile.readline()
while 1:
    Chlist=ChannFile.readline()
    if not Chlist: break
    LstChn='_'.join(Chlist.split(':')[1].strip().split('_')[:-1])
    if LstChn in NewChList:
        pass
    else:
        NewChList.append(LstChn)
ResCh=open('S6/100msUnormFull/nmifs175/ChannelAnalyzedResult35.txt','w')
ResCh.write('NMIFS Top 35 Channel List')
ResCh.write('\n')
for i in range(len(NewChList)):
    ResCh.write(NewChList[i])
    ResCh.write('\n')
ResCh.close()
