#!/usr/bin/env python                                                                                                  
##########
#                aux_file_combiner.py
#              File combiner for aux data 
#     - one training / one evaluation file merger
#            Author: John J. Oh (NIMS)
#                 2014. 5. 20 (Tue)
#                      v.1.0
###########
import numpy as np
import os
import hotshot, hotshot.stats
import glob

from os import makedirs
from os.path import isdir, exists
from sys import exit
from optparse import *
from data_process import file_splitter

parser=OptionParser(usage="Generating .ann input file with Combining ten RR files", version="NA")
parser.add_option("-e","--filename", action="store", type="string", default="NoFile", help="Input data file; Default is NoFile")
parser.add_option("-o","--output-dir", action="store", type="string", default="output", help="Output directory; Default is output")
parser.add_option("-i","--input-dir", action="store", type="string", default=".", help="Input directory; Default is .")
parser.add_option("-l", "--log-dir", action="store", type="string", default="log_dir", help="Log-file directory; Default is log_dir")
parser.add_option("-c", "--cfilename", action="store", type="string",default="NoFile", help="Combined Filename: Default is NoFile")
parser.add_option("-t", "--tag", action="store", type="string", default="none")

(opts,files)=parser.parse_args()
filename   = '.'.join(((opts.filename.split('/'))[-1].split('.'))[:-1])
cfilename = '.'.join(((opts.cfilename.split('/'))[-1].split('.'))[:-1])
input_dir = opts.input_dir
output_dir = opts.output_dir
log_dir = opts.log_dir
t_file = input_dir+'/'+opts.filename
e_file = input_dir+'/'+opts.cfilename
tag = opts.tag

if isdir(output_dir):
    print "Directory exists:", output_dir
else:
    print "Creating directory:", output_dir
    makedirs(output_dir)
if isdir(log_dir):
    logfiles=glob.glob('log_dir/*')
    print "Directory exists:", log_dir
    for f in logfiles:
        os.remove(f)
    print "Removing all log files..."
else:
    print "Creating directory:", log_dir
    makedirs(log_dir)

profile_filename=log_dir+'/'+"Profiling.result"
prof=hotshot.Profile(profile_filename)
prof.start()

file_splitter(filename, input_dir, t_file, output_dir)
file_splitter(cfilename, input_dir, e_file, output_dir)

tdat=np.loadtxt(output_dir+'/'+filename+'_dat.txt')
tcls=np.loadtxt(output_dir+'/'+filename+'_cls.txt')

edat=np.loadtxt(output_dir+'/'+cfilename+'_dat.txt')
ecls=np.loadtxt(output_dir+'/'+cfilename+'_cls.txt')

tfile=open(t_file,'r')
efile=open(e_file,'r')
f=open(output_dir+'/'+tag+'_full_combined.ann','a')
k=0
print 'Writing training files...'
while 1:
    tdata=tfile.readline()
    if not tdata: break
    if k==0:
        f.write(str(len(tdat)+len(edat)))
        f.write(' ')
        f.write(str(len(tdat[0])))
        f.write(' ')
        f.write('1')
        f.write('\n')
    else:
        f.write(tdata[0:-1])
        f.write('\n')
    k+=1
l=0
print 'Writing evaluation files...'
while 1:
    edata=efile.readline()
    if not edata: break
    if l==0:
        pass
    else:
        f.write(edata[0:-1])
        f.write('\n')
    l+=1
tfile.close()
efile.close()
f.close()

print 'Generating combined full data set...'
print 'All jobs done.'

prof.stop()
prof.close()
stats=hotshot.stats.load(profile_filename)
stats.strip_dirs()
stats.sort_stats('time','calls')
stats.print_stats(0)
