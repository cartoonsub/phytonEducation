
import sys
sys.stdin = open("phytonEducation/firstStep\static/test.txt", "r")
class ancestor:
    classes = {}
    answers = []
    def __init__(self):
        self.classes = {}
        self.answers = []
    
    def getInput(self, count):
        if not count.isdigit():
            return ''
        if not self.classes:
            for i in range(int(count)):
                self.addClasses(input())
        else:
            for i in range(int(count)):
                self.checkClass(input())
            return 'stop'
        return ''

    def addClasses(self, data):
        classes = data.split(':')
        if not classes:
            return

        ancestor = classes[0].strip()
        del classes[0]
        
        if not classes:
            return
        
        for mainClass in classes[0].strip().split(' '):
            if not mainClass in self.classes:
                self.classes[mainClass] = []
                self.classes[mainClass].append(ancestor)
                continue
            self.classes[mainClass].append(ancestor)

    def checkClass(self, classNames):
        classNames = classNames.split(' ')
        if classNames[0] == classNames[1]:
            self.answers.append('Yes')
            print('Yes')
            return
        if classNames[0] in self.classes:
            if self.findAncestor(classNames[0], classNames[1]):
                print('Yes')
                self.answers.append('Yes')
            else:
                print('No')
                self.answers.append('No')
        else:
            print('No')
            self.answers.append('No')

    def findAncestor(self, parent, child):
        if child in self.classes[parent]:
            return True
        return self.arrayProcessing(parent, child)

    def arrayProcessing(self, mainClass, needClass):
        if mainClass == needClass:
            return True
        if mainClass not in self.classes:
            return False
        
        if needClass in self.classes[mainClass]:
            return True

        for className in self.classes[mainClass]:
            if self.arrayProcessing(className, needClass):
                return True
        return False


ancestor = ancestor()
while True:
    answer = ancestor.getInput(input())
    if answer == 'stop':
        break