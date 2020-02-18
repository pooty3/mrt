from vertexclass import vertex
from edgeclass import edge
from copy import *
from pathclass import Path
import functions

def go(start,end):
    vertexlist=[]
    edgelist=[]
    for i in range (1,30):
        vertex1=vertex()
        vertex1.initalise('EW'+str(i))
        vertexlist=vertexlist+[vertex1]
    for i in range(1, 30):
        vertex1 = vertex()
        vertex1.initalise('CC' + str(i))
        vertexlist = vertexlist + [vertex1]
    for i in range(1, 18):
        vertex1 = vertex()
        vertex1.initalise('NE' + str(i))
        vertexlist = vertexlist + [vertex1]
    for i in range(1, 29):
        vertex1 = vertex()
        vertex1.initalise('NS' + str(i))
        vertexlist = vertexlist + [vertex1]
    for i in range(1, 7):
        vertex1 = vertex()
        vertex1.initalise('BP' + str(i))
        vertexlist = vertexlist + [vertex1]
    for i in range(1, 20):
        vertex1 = vertex()
        vertex1.initalise('DT' + str(i))
        vertexlist = vertexlist + [vertex1]
    for i in ['CG1', 'CG2', 'CE1', 'CE2']:
        vertex1=vertex()
        vertex1.initalise(i)
        vertexlist=vertexlist+[vertex1]


    for i in range (1,29):
        edge1=edge()
        edge1.init('EW'+str(i),'EW'+str(i+1),2)
        edgelist=edgelist+[edge1]
    edge1=edge()
    edge1.init('EW4','CG1',9)
    edgelist = edgelist + [edge1]
    edge1=edge()
    edge1.init('CG1', 'CG2', 5)
    edgelist = edgelist + [edge1]
    for i in range(1,28):
        edge1=edge()
        edge1.init('NS'+str(i),'NS'+str(i+1),2)
        edgelist=edgelist+[edge1]
    for i in range(1,17):
        edge1 = edge()
        edge1.init('NE' + str(i), 'NE' + str(i + 1), 2)
        edgelist = edgelist + [edge1]
    for i in range(1, 19):
        edge1 = edge()
        edge1.init('DT' + str(i), 'DT' + str(i + 1), 2)
        edgelist = edgelist + [edge1]
    for i in range(1, 29):
        edge1 = edge()
        edge1.init('CC' + str(i), 'CC' + str(i + 1), 2)
        edgelist = edgelist + [edge1]
    edge1 = edge()
    edge1.init('CC4', 'CE1', 6)
    edgelist = edgelist + [edge1]
    edge1 = edge()
    edge1.init('CE1', 'CE2', 2)
    edgelist = edgelist + [edge1]
    for i in range(1,6):
        edge1 = edge()
        edge1.init('BP' + str(i), 'BP' + str(i + 1), 2)
        edgelist = edgelist + [edge1]


    edgelist[0].time=3
    edgelist[2].time = 3
    edgelist[3].time = 3
    edgelist[4].time = 3
    edgelist[5].time = 1
    edgelist[21].time=3
    edgelist[22].time = 4
    edgelist[27].time = 4
    edgelist[30].time = 3
    edgelist[32].time = 4
    edgelist[34].time = 5
    edgelist[37].time=3
    edgelist[38].time = 3
    edgelist[39].time = 4
    edgelist[41].time = 5
    edgelist[42].time=3
    edgelist[43].time = 3
    edgelist[45].time = 1
    edgelist[54].time = 3
    edgelist[56].time = 1
    edgelist[58].time = 1
    edgelist[61].time = 3
    edgelist[62].time = 1
    edgelist[64].time = 3
    edgelist[68].time = 3
    edgelist[84].time = 1
    edgelist[79].time = 1
    edgelist[71].time = 3
    edgelist[96].time = 3
    edgelist[99].time = 3
    edgelist[101].time = 3
    edgelist[102].time = 5
    edgelist[110].time = 3
    edgelist[111].time = 1
    edgelist[112].time = 3
    edgelist[116].time = 1
    edgelist[118].time = 1
    edge1 = edge()
    edge1.init('EW24', 'NS1', 0)
    edgelist = edgelist + [edge1]
    edge1 = edge()
    edge1.init('BP1', 'NS4', 0)
    edgelist = edgelist + [edge1]
    edge1 = edge()
    edge1.init('BP6', 'DT1', 0)
    edgelist = edgelist + [edge1]
    edge1 = edge()
    edge1.init('NS17', 'CC15', 0)
    edgelist = edgelist + [edge1]
    edge1 = edge()
    edge1.init('CC13', 'NE12', 0)
    edgelist = edgelist + [edge1]
    edge1 = edge()
    edge1.init('CC19', 'DT9', 0)
    edgelist = edgelist + [edge1]
    edge1 = edge()
    edge1.init('NS21', 'DT11', 0)
    edgelist = edgelist + [edge1]
    edge1 = edge()
    edge1.init('NE7', 'DT12', 0)
    edgelist = edgelist + [edge1]
    edge1 = edge()
    edge1.init('EW12', 'DT14', 0)
    edgelist = edgelist + [edge1]
    edge1 = edge()
    edge1.init('CC4', 'DT15', 0)
    edgelist = edgelist + [edge1]
    edge1 = edge()
    edge1.init('CC9', 'EW8', 0)
    edgelist = edgelist + [edge1]
    edge1 = edge()
    edge1.init('NS25', 'EW13', 0)
    edgelist = edgelist + [edge1]
    edge1 = edge()
    edge1.init('EW14', 'NS26', 0)
    edgelist = edgelist + [edge1]
    edge1 = edge()
    edge1.init('CE2', 'NS27', 0)
    edgelist = edgelist + [edge1]
    edge1 = edge()
    edge1.init('CE1', 'DT16', 0)
    edgelist = edgelist + [edge1]
    edge1 = edge()
    edge1.init('DT19', 'NE4', 0)
    edgelist = edgelist + [edge1]
    edge1 = edge()
    edge1.init('EW16', 'NE3', 0)
    edgelist = edgelist + [edge1]
    edge1 = edge()
    edge1.init('NE1', 'CC29', 0)
    edgelist = edgelist + [edge1]
    edge1 = edge()
    edge1.init('EW21', 'CC22', 0)
    edgelist = edgelist + [edge1]
    edge1 = edge()
    edge1.init('NS24', 'CC1', 0)
    edgelist = edgelist + [edge1]
    edge1 = edge()
    edge1.init('NS24', 'NE6', 0)
    edgelist = edgelist + [edge1]


    startvertex=vertex()
    startvertex.initalise('START')
    vertexlist=vertexlist+[startvertex]
    edge1=edge()
    edge1.init('START',start,0)
    edgelist=edgelist+[edge1]

    endvertex = vertex()
    endvertex.initalise('END')
    vertexlist = vertexlist + [endvertex]
    edge1 = edge()
    edge1.init(end,'END', 0)
    edgelist = edgelist + [edge1]

    for vertex1 in vertexlist:
        vertex1.getneighbours(edgelist)
        vertex1.getdegree()

    while (functions.checkdegree1s(vertexlist)=='True'):


        length = len(vertexlist)
        newvertexlist = []
        for i in range(0,length):
            if vertexlist[i].degree>1 or vertexlist[i].code=='END' or vertexlist[i].code=='START':
                newvertexlist=newvertexlist+[deepcopy(vertexlist[i])]

        vertexlist=deepcopy(newvertexlist)

        length=len(edgelist)
        newedgelist=[]
        for i in range(0,length):
             if functions.pointexist(edgelist[i].start,vertexlist)=='True' and functions.pointexist(edgelist[i].end,vertexlist)=='True':
                newedgelist=newedgelist+[deepcopy(edgelist[i])]
        edgelist=newedgelist


        for vertex1 in vertexlist:
           vertex1.getneighbours(edgelist)
           vertex1.getdegree()

    pathlist=[]
    path1=Path()
    path1.time=0
    path1.sequence=[functions.retrievevertexbycode('START',vertexlist)]
    pathlist=[path1]
    bestpath=Path()
    bestpath.time=9999

    while (len(pathlist)!=0):
        newpathlist=[]
        for path1 in pathlist:
            endvertex=path1.sequence[len(path1.sequence)-1]
            neighbourlist=endvertex.neighbour
            for neighbour1 in neighbourlist:
                if functions.vertexinpath(neighbour1,path1)=='False':
                    path2=deepcopy(path1)
                    path2.addvertex(functions.retrievevertexbycode(neighbour1,vertexlist),edgelist)
                    if path2.time<bestpath.time:
                        if path2.sequence[len(path2.sequence)-1].code=='END':
                            bestpath=path2
                        else:
                            newpathlist=newpathlist+[path2]
        pathlist=newpathlist
    return bestpath

















