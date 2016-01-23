#!/usr/bin/python

# This utility extracts the text from SubRip files (extention: .srt) into a plain text files.
#
# author: joseph.k.j@gatech.edu

import os
import inspect
import re

# sourceDirectory : refers to the directory in which you have all the srt files
sourceDirectory = '/Users/josephkj/Desktop/Subtitles'

# consolidatedFile : the file name of the output file
consolidatedFile = 'Consolidated.txt'

# readAndParseFile() : Reads the contents of each file and parses it, to retain only the necessary lines
def readAndParseFile(filename):
    finalFile.write('\r\n\r\n'+filename[:-4]+'\r\n\r\n\r\n')
    with open(sourceDirectory+filename) as f:
        content = f.readlines()
    for line in content:
        if re.search('[a-zA-Z]', line) != None :
            finalFile.write(line.replace('\r\n',' '))

# Some sanity check on the sourceDirectory variable
if not sourceDirectory.endswith('/'):
    sourceDirectory = sourceDirectory + '/'
consolidatedFile = sourceDirectory + consolidatedFile

# Reading each file form the directory
scriptFile = inspect.getfile(inspect.currentframe())
finalFile = open(consolidatedFile,'w')
for filename in os.listdir(sourceDirectory):
    if(filename.find('srt') > 0):
        readAndParseFile(filename)
finalFile.close();
