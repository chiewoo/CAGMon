#!/usr/bin/env python
#############
#         Normalizer.py : data normalizer feature by feature
#                 Author : John J. Oh (NIMS)
#                    2014. 5. 22 (Thur)
#                         v.1.0
############

import numpy as np
import math
import os
import glob
import sys
from os import makedirs
from os.path import isdir, exists
from sys import exit
from optparse import *
from data_process import file_splitter
from data_process import file_merger
from data_process import feat_normalize
from data_process import null_remover

parser=OptionParser(usage="Performing data normalization feature by feature", version="v.1.0")
parser.add_option("-f","--filename", action="store", type="string", default="NoFile", help="Input data file; Default is NoFile")
parser.add_option("-o","--output-dir", action="store", type="string", default="output", help="Output directory; Default is output")
parser.add_option("-i","--input-dir", action="store", type="string", default=".", help="Input directory; Default is .")
parser.add_option("-l", "--log-dir", action="store", type="string", default="log_dir", help="Log-file directory; Default is log_dir")
parser.add_option("-t", "--tag", action="store", type="string", help="User-defined tag")

(opts,files)=parser.parse_args()
filename   = '.'.join(((opts.filename.split('/'))[-1].split('.'))[:-1])
input_dir = opts.input_dir
input_file = input_dir+'/'+opts.filename
output_dir = opts.output_dir
log_dir = opts.log_dir
tag= opts.tag

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

print 'Input data splitting....'
file_splitter(input_file, filename, output_dir)

dat_input = output_dir+'/'+filename+'_dat.txt'
cls_input = output_dir+'/'+filename+'_cls.txt'

print 'Removing null vectors...'
null_remover(dat_input, filename, output_dir)

dinull_rmv = output_dir+'/'+filename+'_reduced_null_rmvd_dat.txt'
dinp = np.loadtxt(dinull_rmv)
cinput=np.loadtxt(cls_input)

print 'Performing Data normalization....'
norm=feat_normalize(dinp)

f=open(output_dir+'/'+filename+'_norm_temp.txt','a')
for i in range(len(norm)):
    for j in range(len(norm[i])):
        f.write(str(norm[i][j]))
        f.write(' ')
    f.write('\n')

datemp_input = output_dir+'/'+filename+'_norm_temp.txt'

print 'Generating normalized .ann file...'
f=open(datemp_input, 'r')
k=open(cls_input, 'r')
g=open(output_dir+'/'+tag+'_norm.ann','a')
g.write(str(len(dinp)))
g.write(' ')
g.write(str(len(dinp[0])))
g.write(' ')
g.write('1')
g.write('\n')
while 1:
    data=f.readline()
    clss=k.readline()
    if not data: break
    g.write(str(data[0:-1]))
    g.write('\n')
    g.write(str(clss[0:-1]))
    g.write('\n')
g.close()
k.close()
f.close()

print 'All processes done.'

