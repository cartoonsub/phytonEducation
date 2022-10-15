from cgi import print_directory
import re
import os
import shutil
from time import sleep

class FileManager():
    def __init__(self, folder, dest):
         self.folder = folder
         self.dest = dest
         self.walkFiles(folder)
    
    def walkFiles(self, folder):
        os.chdir(folder)
        curentDir = os.getcwd()
        for root, dirs, files in os.walk(curentDir):
            if not files:
                continue
            counter = 0
            for file in files:
                currentFile = os.path.join(root, file)
                # self.Rename(currentFile, root)
                print(currentFile)
                if (counter % 2) != 0:
                    # match = re.search(r'S01E(\d+)DUBx1080x(\w+)\.mp4', currentFile)
                    # match = re.sub(r'E[^0]', )
                    # newName = 'S01E' + str(int(match[1]) + 1) + 'DUBx1080x' + match[2] + '.mp4'
                    # newFile = os.path.join(root, newName)
                    print(currentFile)
                    # shutil.move(file, newFile)
                counter += 1

                

    def Rename(self, file, root):
        matches = re.search(r'x(\d{1,2})-(\d{1,2}).+?\[(\w+)].+?(\.\w+)$', file, re.IGNORECASE)
        newName = 'S01E' + matches[1] + 'DUBx1080x' + matches[3] + matches[4]
        newFile = os.path.join(root, newName)
        if os.path.isfile(newFile):
            newName = 'S01E' + matches[2] + 'DUBx1080x' + matches[3] + matches[4]
            newFile = os.path.join(root, newName)


        shutil.move(file, newFile)
            

    def moveFile(self, file, dest):
        shutil.move(file, dest)
        print('Moved:', file)

FileManager('G:\\cartoon\\gumball\\1season\\sound\\output', 'G:\cartoon\gumball\1season\sound\output')




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