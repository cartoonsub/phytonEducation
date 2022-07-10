import os
import shutil

os.chdir('G:/cartoonsub/stevenuniverse/S06_future')
curentDir = os.getcwd()
print(curentDir)

for root, dirs, files in os.walk(curentDir):
    if not files:
        continue
    for file in files:
        path = root + '\\' + file
        shutil.move(path, r'G:/cartoonsub/stevenuniverse/S06_future/')
        print('Moved:', path)

source_folder = r"E:\pynative\reports\\"
destination_folder = r"E:\pynative\account\\"

# for file_name in os.listdir(source_folder):
#     # construct full file path
#     source = source_folder + file_name
#     destination = destination_folder + file_name
#     # move only files
#     if os.path.isfile(source):
#         shutil.move(source, destination)
#         print('Moved:', file_name)