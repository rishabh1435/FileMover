import shutil
import os
import random 

sourceF="C:\Code\PythonTest\SourceFile"
source="C:\Code\PythonTest\SourceFile\Chuthya.txt"
desti="C:\Code\PythonTest\DestinationFile"
destiF="C:\Code\PythonTest\DestinationFile\Chuthya.txt"

"""
if os.path.exists(source):
    if os.path.exists(destiF):
        print("File already exists")
    else: 
        shutil.move(source,desti)
    print("File has been moved")
else: 
    print("File was not moved")
print("All done")
input('')
"""


items=os.listdir(sourceF)
print(items)
# shutil.move(sourceF, desti)
source1=" "

for i in items:
    source1=sourceF+"\\"+i
    print(source1)
    shutil.move(source1,desti)
    print("File has been moved")
    
print("All done")
input('')

