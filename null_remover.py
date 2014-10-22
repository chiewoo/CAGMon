import numpy as np
import math
import os
import glob
import sys
from os import makedirs
from os.path import isdir, exists
from sys import exit
from optparse import *
from data_process import null_remover
from data_process import file_splitter
class Log:
    def __init__(self, stdout, logpath):
        self.stdout = stdout
        self.logfile = open(logpath, 'w')
    def write(self, s):
        self.stdout.write(s)
        self.logfile.write(s)
#    def close(self):                                                                                                                 #        self.logfile.close()                                                                                                          

parser=OptionParser(usage="Computing MIC with a given data", version="none")
parser.add_option("-f","--filename", action="store", type="string", default="NoFile", help="Input data file; Default is NoFile")
parser.add_option("-o","--output-dir", action="store", type="string", default="output", help="Output directory; Default is output")
parser.add_option("-i","--input-dir", action="store", type="string", default=".", help="Input directory; Default is .")
parser.add_option("-l", "--log-dir", action="store", type="string", default="log_dir", help="Log-file directory; Default is log_dir")


(opts,files)=parser.parse_args()
filename   = '.'.join(((opts.filename.split('/'))[-1].split('.'))[:-1])
input_dir = opts.input_dir
input_file = input_dir+'/'+opts.filename
output_dir = opts.output_dir
log_dir = opts.log_dir


print 'Splitting data...'
file_splitter(input_file, filename, output_dir)

print 'Removing null vectors...'
null_remover(filename, output_dir)

print 'All jobs done.'


