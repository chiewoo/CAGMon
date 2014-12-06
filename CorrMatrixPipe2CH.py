#!/usr/bin/env python
#
# Copyright (C) 2014 Korean Gravitational Wave Group (KGWG)            
#
# This program is free software; you can redistribute it and/or modify it
# under the terms of the GNU General Public License as published by the
# Free Software Foundation; either version 2 of the License, or (at your
# option) any later version.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General
# Public License for more details.
#
# You should have received a copy of the GNU General Public License along
# with this program; if not, write to the Free Software Foundation, Inc.,
# 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.
#
#
#          CorrMatrixPipe2CH.py
#              : An Integrated Pipeline Code for
#                a) Read Trigger Input with 2 different channel data
#                b) Compute Mutual Information Correlation
#                c) Select Max Value among Atrributes
#                d) Generate Correlation Matrix
#                e) List Correlated Channel Names
#                f) Draw Correlation Matrix Map
#
#                 Author : John J. Oh (KGWG - NIMS)
#                     Version: 2.0
#
#
# =============================================================================
#
#                                   Preamble
#
# =============================================================================
#

__author__ = "John J. Oh <john.oh@ligo.org>"
__version__ = "2.000"
__date__ = "December 2014"

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
from sklearn.metrics.cluster import normalized_mutual_info_score
from sklearn.metrics.cluster import mutual_info_score
from data_process import feat_remover
from data_process import file_splitter
from data_process import null_remover
from data_process import file_merger

from os import makedirs
from os.path import isdir, exists
from sys import exit
from optparse import *

#                                                                             
# =============================================================================                                                      
#                                                                             
#                          Log, Option, and Profile 
#              
# =============================================================================
#                                                                                                                                                           

class Log:
    def __init__(self, stdout, logpath):
        self.stdout = stdout
        self.logfile = open(logpath, 'w')
    def write(self, s):
        self.stdout.write(s)
        self.logfile.write(s)

parser=OptionParser(usage="Computing MIC and generating correlation matrix with a given data", version="1.000")
parser.add_option("-f","--fname1", action="store", type="string", default="NoFile", help="First input data file; Default is NoFile")
parser.add_option("-e","--fname2", action="store", type="string", default="NoFile", help="Second input data file: Default is NoFIle")
parser.add_option("-o","--output-dir", action="store", type="string", default="output", help="Output directory; Default is output")
parser.add_option("-i","--input-dir", action="store", type="string", default=".", help="Input directory; 2CH Data should be located in the same input directory: Default is .")
parser.add_option("-l", "--log-dir", action="store", type="string", default="log_dir", help="Log-file directory; Default is log_dir")
parser.add_option("-d", "--cinput-dir", action="store", type="string", default=".", help="directory where the channel list file locates")
parser.add_option("-c", "--chan-file", action="store", type="string", default="NoFile", help="Channel List Filename")
parser.add_option("-n", "--number-channels", action="store", type="int", default="35", help="Number of Channels")
parser.add_option("-a", "--number-attribute", action="store", type="int", default="5", help="NUmber of Attribute")
parser.add_option("-t", "--threshold", action="store", type="float", default="0.0", help="Threshold value of Correlation between 0.0 and 1.0")
parser.add_option("-g", "--gps-time", action="store", type="int", default="00000", help="GPS time")

(opts,files)=parser.parse_args()
filename1   = '.'.join(((opts.fname1.split('/'))[-1].split('.'))[:-1])
filename2   = '.'.join(((opts.fname2.split('/'))[-1].split('.'))[:-1])
input_dir = opts.input_dir
input_file1 = input_dir+'/'+opts.fname1
input_file2 = input_dir+'/'+opts.fname2
output_dir = opts.output_dir
log_dir = opts.log_dir
cinput_dir = opts.cinput_dir
chan_input = cinput_dir+'/'+opts.chan_file
num_chan=opts.number_channels
attrib = opts.number_attribute
thv = opts.threshold
GPS = opts.gps_time

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

sys.stdout = Log(sys.stdout, output_dir+'/'+'MIC_Report.log')

profile_filename=log_dir+'/'+"Profiling.result"
prof=hotshot.Profile(profile_filename)
prof.start()


f1=np.loadtxt(input_file1+'.txt')
f2=np.loadtxt(input_file2+'.txt')

Mdim=len(f1)
mic=np.zeros((Mdim, Mdim))

# =============================================================================
#
#                               Compute MIC
#                      & Generate Correlation Matrix
#
# =============================================================================
print 'Computing mutual information indices and generating correlation matrix...'
for i in range(Mdim):
#    sys.stdout.write(".")
    for j in range(Mdim):
        mic[i][j] = normalized_mutual_info_score(f1[i],f2[j])
#        print mic[i][j]
        sys.stdout.write(".")
        g=open(output_dir+'/'+'CorrMatrixNMic_'+str(Mdim)+'_'+filename1+'_'+filename2+'.txt','a')
        if j==Mdim:
            g.write(str(mic[i][j]))
            g.write('\n')
        else:
            g.write(str(mic[i][j]))
            g.write(' ')
        g.close()

# =============================================================================
#                                                                                                                                                         
#                    Select Max_value among all atrributes
#                           & Generate reduced matrix
#                                                                                                                                
# =============================================================================
f=np.loadtxt(output_dir+'/'+'CorrMatrixNMic_'+str(Mdim)+'_'+filename1+'_'+filename2+'.txt').reshape([Mdim,Mdim,])
print 'Selecting maximum values and generating reduced matrix...'
for i in range(0,len(f)/attrib):
    for j in range(0,len(f)/attrib):
        F=f[attrib*i:attrib*i+attrib, attrib*j:attrib*j+attrib]
        k=open(output_dir+'/'+'MaxRedMatrixNMIC_'+filename1+'_'+filename2+'.txt','a')
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
#                         Threshold Triggered Matrix
#                               & Indices
#
# =============================================================================
if thv == 0.0 :
    pass
else:
    M=np.loadtxt(output_dir+'/'+'MaxRedMatrixNMIC_'+filename1+'_'+filename2+'.txt')
    f=open(output_dir+'/'+'MaxRedMatrixNMIC_'+filename1+'_'+filename2+'_th'+str(thv)+'.txt','a')
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
    g=open(output_dir+'/'+'GetIndexThrshd_'+filename1+'_'+filename2+'_th'+str(thv)+'.txt','a')
    for i in range(len(M)):
        for j in range(len(M)):
            if i==j:
                pass
            else:
                if M[i][j] > thv:
                    g.write(str(i))
                    g.write(' ')
                    g.write(str(j))
                    g.write(' ')
                    g.write(str(M[i][j]))
                    g.write('\n')
                else:
                    pass
    g.close()

# =============================================================================
#
#                            Draw Correlation Matrix
#
# =============================================================================

print 'Drawing correlation matrix map...'                                                    
                              
if thv == 0.0:
    dat = np.loadtxt(output_dir+'/'+'MaxRedMatrixNMIC_'+filename1+'_'+filename2+'.txt')
else:
    dat = np.loadtxt(output_dir+'/'+'MaxRedMatrixNMIC_'+filename1+'_'+filename2+'_th'+str(thv)+'.txt')

###
# if NaN appears, set to be zero
###
#
#dat2= np.nan_to_num(dat)
#data=(dat2-np.min(dat2))/np.max(dat2-np.min(dat2))                                                                                                       
#data=abs(dat)/np.max(abs(dat))                                                                                                                          
                                                                                                                                    
rows, cols = np.indices((Mdim/attrib, Mdim/attrib))
#dat[np.diag(rows, k=0), np.diag(cols, k=0)]=0
data = (dat-np.min(dat))/np.max(dat-np.min(dat))

colors = [('white')] + [(cm.jet(i)) for i in xrange(1,256)]
new_map = matplotlib.colors.LinearSegmentedColormap.from_list('new_map', colors, N=256)

lbs=open(chan_input+'.txt','r')
lbsdat=lbs.readlines()

column_labels = lbsdat
row_labels = lbsdat
                                                                                                                                                    
fig, ax = plt.subplots()
fig.set_size_inches(24,20)
heatmap = pcolor(data, cmap=new_map,edgecolors='k')
colorbar()
                                                                                                                                                    
ax.set_xticks(np.arange(data.shape[0])+0.5, minor=False)
ax.set_yticks(np.arange(data.shape[1])+0.5, minor=False)
mpl.rc('text', usetex=False)
fig.suptitle('Correlation Matrix via Mutual Information Coefficient between SEI and GW channels of CLIO', fontsize=25, fontweight='bold')
ax.invert_yaxis()
ax.xaxis.tick_top()
plt.ylabel(str(GPS)+'_GW_fs2048', fontsize=20)
plt.xlabel(str(GPS)+'_SEI_fs2048', fontsize=20)
plt.xticks(rotation=90)
ax.set_xticklabels(row_labels, minor=False, fontsize=15)
ax.set_yticklabels(column_labels, minor=False, fontsize=15)
fig.savefig(output_dir+'/'+'CMatrixNMICG_SEI_GW_CLIO_'+str(GPS)+'.png',dpi=256)
#plt.show()                            

print 'ALL JOBS DONE!'


# =============================================================================
#
#                                 Profiling Ends
#
# =============================================================================
prof.stop()
prof.close()
stats=hotshot.stats.load(profile_filename)
stats.strip_dirs()
stats.sort_stats('time','calls')
stats.print_stats(0)

