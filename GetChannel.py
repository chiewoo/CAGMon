#!/usr/bin/env python

f=open('hchannels.txt')
g=open('S6/35ch2/hveto35channellist.txt','a')
attrib = ['signif', 'dt']

while 1:
    chlist=f.readline()
    if not chlist: break
    for i in range(len(attrib)):
        newlist = chlist.strip()+'_'+attrib[i]
        g.write(newlist)
        g.write('\n')
g.close()
f.close()
