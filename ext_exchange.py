import os

path = input("PATH:")
from_extension = '.bmp'
to_extension = '.jpg'
count=0

print (path)
listing = os.listdir(path)
for filename in listing:
    if not ( from_extension in filename or from_extension.upper() in filename):
        pass
    else:
        #print ("current file is: " + filename)
        newname=filename.replace(from_extension,to_extension)
        newname = filename.replace(from_extension.upper(), to_extension)
        #print (newname)
        os.rename(path+'\\'+filename,path+'\\'+newname)
        count=count+1;

print ("FILE CONVERTED : "+str(count));