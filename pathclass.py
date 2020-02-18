from vertexclass import *
import functions

class Path:
    time=9999
    sequence=[]
    def addvertex(self,vertex1,edgelist):
        endvertex=self.sequence[len(self.sequence)-1]
        time=functions.retrievetime(vertex1.code,endvertex.code,edgelist)
        self.time=self.time+time
        self.sequence=self.sequence+[vertex1]

