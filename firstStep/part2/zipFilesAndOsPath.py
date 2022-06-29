from this import s
from time import sleep
import zipfile, os

curentDir = os.getcwd()

if not(os.path.exists(curentDir + '\\phytonEducation\\firstStep\\part2\\static\\unziped')):
    print('unziping')
    os.chdir('phytonEducation/firstStep/part2/static')
    folder = (os.path.dirname(os.path.realpath(__file__)))

    filePath = (os.path.abspath('main.zip'))

    zipFile = zipfile.ZipFile(filePath)
    zipFile.extractall(folder + '\\static\\unziped')
    zipFile.close()

if not(os.path.exists(curentDir + '\\phytonEducation\\firstStep\\part2\\static\\unziped')):
    print('don\'t unzip')
    exit()

# folders = set()
folders = list()
for root, dirs, files in os.walk(curentDir + '\\phytonEducation\\firstStep\\part2\\static\\unziped'):
    if not files:
        continue
    
    for file in files:
        if file.endswith('.py'):
            needPath = root.replace('C:\\phytonProjects\\phytonEducation\\firstStep\\part2\\static\\unziped\\', '') 
            # folders.add(needPath)
            folders.append(needPath)
            break
    

for path in folders:
    # print(path)
    pass
# main
# main/afkgv
# main/frtrl
# main/hgyoc
# main/hgyoc/kwawh
# main/hgyoc/kwawh/hapry
# main/hgyoc/kwawh/rzgzv
# main/hgyoc/ycbxr/ivjta
# main/ksuvk/xjrqt
# phytonEducation/firstStep/part2/static/main.zip
# print(os.getcwd())
# print(os.listdir())
# os.chdir('phytonEducation/firstStep/part2/static')
# print(os.listdir())
# os.chdir('/')
# print(os.listdir())


array = [i for i in range(10)]
print(array[::-1])
print(array)