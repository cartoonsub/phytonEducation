
from operator import ne
from re import M
import sys
sys.stdin = open("phytonEducation/firstStep/static/testAncestorsException.txt", "r")


class ancestorExceptions():
    def __init__(self):
        self.classes = {} #список классов
        self.hierarchy = {} #список ответов
        self.answers = [] #список ответов
    
    def getInput(self, count):
        if not count.isdigit():
            return ''
        if not self.classes:
            for i in range(int(count)):
                self.addClasses(input())
        else:
            for i in range(int(count)):
                pass
                self.checkClass(input(), i)
            return 'stop'
        return ''

    def addClasses(self, data):
        classes = data.split(':')
        if not classes:
            return
        ancestor = classes[0].strip()
        del classes[0]
        if not ancestor in self.classes:
            self.classes[ancestor] = []

        if not classes:
            return
        
        for mainClass in classes[0].strip().split(' '):
            self.classes[ancestor].append(mainClass)
            if mainClass in self.classes:
                self.classes[ancestor].extend(self.classes[mainClass])
            for key, value in self.classes.items():
                if ancestor in value:
                    if mainClass in self.classes[key]:
                        continue
                    self.classes[key].append(mainClass)
                    # extend


    def checkClass(self, className, i):
        self.hierarchy[className] = i
        if className not in self.classes:
            return
        
        self.findAncestor(className)


    def findAncestor(self, needClass):
        if not self.classes[needClass]:
            return
        
        currentNum = self.hierarchy[needClass]
        for exceptName in self.classes[needClass]:
            if exceptName in self.hierarchy:
                if currentNum > self.hierarchy[exceptName]:
                    if needClass in self.answers:
                        continue
                    self.answers.append(needClass)


ancestor = ancestorExceptions()
while True:
    answer = ancestor.getInput(input())
    if answer == 'stop':
        break

for i in ancestor.answers:
    print(i)

print()
print(ancestor.classes)
print(ancestor.hierarchy)
print()