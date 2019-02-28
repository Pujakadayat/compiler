"""
simple script to test the compiler on all of the current sample programs
prints which sample programs pass and which fail
"""
import glob
#glob is basically grep
#finds files & directories with given pattern

fileNames = sorted(glob.glob('../samples/*.c'))
fileNames = fileNames[0:15]
#sort & list the file names in alphabetical order

for i in fileNames:
#loop through testing files
#test with main_grammar
    print(i)
