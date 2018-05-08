#  

import os 
import datetime
ts = datetime.datetime.now() 

INPFILE="UniqueLabels.txt" 
OUTFOL = "SplittedFiles"  


def split_by(infile,outfolder,chunksize):    
    partFileName = 0 
    SOURCEFL = open(infile,'r')
    isLinesThere = True 
    while isLinesThere:
        partFileName = partFileName + 1         
        #print "Processing Part   "+ str(partFileName)
        tempfilename = os.path.join(outfolder,(infile[:-4]+"_"+str(partFileName)+".txt"))
      
        with open(tempfilename,'w') as tfl:
             for lineNumber in xrange(chunksize):
                 try:
                     aRawLine=SOURCEFL.next()
                     tfl.write(aRawLine)                                  
                 except StopIteration:
                     isLinesThere = False  
                     lineNumber = chunksize 
    SOURCEFL.close()
    print("File Chunking is done ")


split_by(INPFILE,OUTFOL,chunksize=2) 
te = datetime.datetime.now() 
print 'Elapsed Time  :  ' + str(te-ts)

