from copy import *
class edge:
    start=''
    end=''
    time=-1
    def init(self,start,end,time):
        self.start=start
        self.end=end
        self.time=time
    def getstring(self):
        return "Take "+self.line+" line from "+str(self.start)+"to "+str(self.end)+". Time taken: "+str(self.time)+"mins."




