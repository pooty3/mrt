from edgeclass import edge


class vertex:
    code = '0'
    degree=0
    neighbour=[]

    def initalise(self, code):
        self.code = code
    def getneighbours(self,edgelist):
        self.neighbour=[]
        length=len(edgelist)

        for i in range(0,length):
            if (edgelist[i].end!=edgelist[i].start):
                if (edgelist[i].start==self.code):
                    self.neighbour=self.neighbour+[edgelist[i].end]
                if (edgelist[i].end==self.code):
                    self.neighbour = self.neighbour + [edgelist[i].start]
    def getdegree(self):
        self.degree=len(self.neighbour)





