from mimetypes import init
import time

class Loggable:
    def log(self, msg):
        print(str(time.ctime()) + ": " + str(msg))

class LoggableList(Loggable, list):
    def append(self, elem):
        list.append(self, elem)
        self.log(elem)
        


a = LoggableList()
a.append('msg 1')
a.append('msg 2')
print(a)