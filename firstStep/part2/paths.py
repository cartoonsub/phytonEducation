import os
import shutil

print(os.listdir())
print(os.path.exists('fuck'))

print(os.path.isfile('textFile.txt'))
print(os.path.isdir('.idea'))

print(os.walk(""))

# for root, dirs, files in os.walk("phytonEducation"):
#     print(root, dirs, files)
#     print('\n')

# shutil.copytree("phytonEducation/checkio", "phytonEducation_copy")
