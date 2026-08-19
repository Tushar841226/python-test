import os
#specified the directory
directory_path='/'
#list of direcory 
contents=os.listdir(directory_path)
#print the directory items
for item in contents:
    print(item)