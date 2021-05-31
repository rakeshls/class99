import os
import shutil
source=input("Enter Source Folder:")
dest=input("Enter Destination Folder:")
source=source+'/'
dest=dest+'/'
lof=os.listdir(source)
for file in lof:
    shutil.copy((source+file),dest)