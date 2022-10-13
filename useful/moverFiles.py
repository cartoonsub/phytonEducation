import re
import os
import shutil

from soupsieve import match

os.chdir('G:\\cartoonsub\\stevenuniverse\\S06_future_done\\orig')
curentDir = os.getcwd()

for root, dirs, files in os.walk(curentDir):
    if root.find('converted') > -1:
        pass
    
    if not files:
        continue
    for file in files:
        if file.lower().find('original') == -1:
            pass
        path = root + '\\' + file\
        
        file_oldname = os.path.join(root, file)

        # matches = re.search(r'e(\d+)\.(\w+)', file)
        matches = re.search(r'S(\d+)E(\d+)', file, re.IGNORECASE)
        file_newname_newfile = os.path.join(root, "S06" + "E" + matches[2] + "ORIGINAL" + ".mp4")

        # newFileName=shutil.move(file_oldname, file_newname_newfile)
        print(file_newname_newfile)
        # shutil.move(path, r'G:/cartoonsub/stevenuniverse/S06_future/converted/')
        # print('Moved:', path)

# source_folder = r"E:\pynative\reports\\"
# destination_folder = r"E:\pynative\account\\"

# for file_name in os.listdir(source_folder):
#     # construct full file path
#     source = source_folder + file_name
#     destination = destination_folder + file_name
#     # move only files
#     if os.path.isfile(source):
#         shutil.move(source, destination)
#         print('Moved:', file_name)