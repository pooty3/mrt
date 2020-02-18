from vertexclass import vertex
from edgeclass import edge

def validstation(String):
    stations=[]
    for i in range(1,30):
        stations=stations+['EW'+str(i)]
    for i in range (1,29):
        stations=stations+['NS'+str(i)]
    for i in range(1,30):
        stations=stations+['CC'+str(i)]
    for i in range(1,18):
        stations=stations+['NE'+str(i)]
    for i in range(1,20):
        stations=stations+['DT'+str(i)]
    for i in range (1,7):
        stations=stations+['BP'+str(i)]
    stations=stations+['CG1','CG2','CE1','CE2']
    yes=False
    for name in stations:
        if name==String:
            yes=True
    return yes
def isintersection(String):
    number=0
    yes=False
    if String=='EW29':
        yes=True
        number=1
    elif String == 'EW24'or String=='NS1':
        yes = True
        number = 2
    elif String == 'BP1'or String=='NS4':
        yes = True
        number = 3
    elif String == 'BP6'or String=='DT1':
        yes = True
        number = 4
    elif String == 'NS17' or String=='CC15':
        yes = True
        number = 5
    elif String == 'CC13'or String=='NE12':
        yes = True
        number = 6
    elif String == 'NE17':
        yes = True
        number = 7
    elif String == 'CC19'or String=='DT9':
        yes = True
        number = 8
    elif String == 'NS21' or String=='DT11':
        yes = True
        number = 9
    elif String == 'NE7' or String == 'DT12':
        yes = True
        number = 10
    elif String == 'EW12' or String == 'DT14':
        yes = True
        number = 11
    elif String == 'CC4' or String == 'DT15':
        yes = True
        number = 12
    elif String == 'CC9' or String == 'EW8':
        yes = True
        number = 13
    elif String == 'EW4':
        yes = True
        number = 14
    elif String == 'EW1':
        yes = True
        number = 15
    elif String == 'CG2':
        yes = True
        number = 16
    elif String == 'EW13' or String == 'NS25':
        yes = True
        number = 17
    elif String == 'NS26' or String == 'EW14':
        yes = True
        number = 18
    elif String == 'NS28':
        yes = True
        number = 19
    elif String == 'NS27' or String == 'CE2':
        yes = True
        number = 20
    elif String == 'DT16' or String == 'CE1':
        yes = True
        number = 21
    elif String == 'NE4' or String == 'DT19':
        yes = True
        number = 22
    elif String == 'EW16' or String == 'NE3':
        yes = True
        number = 23
    elif String == 'NE1' or String == 'CC29':
        yes = True
        number = 24
    elif String == 'CC22' or String == 'EW24':
        yes = True
        number = 25
    elif String == 'NS24' or String == 'CC1' or String=='NE6':
        yes = True
        number = 26
    else:
        yes=False
        number=0
    return [yes,number]

def checkdegree1s(list):
    default='False'
    for vertex1 in list:
        if vertex1.degree<2 and vertex1.code!='START' and vertex1.code!='END':
             default='True'
    return default
def pointexist(String,list):
    default='False'
    for vertex1 in list:
        if String==vertex1.code:
            default='True'
    return default


def retrievetime(String1,String2,edgelist):
    for edge1 in edgelist:
        if ((edge1.end==String1) and (edge1.start==String2)) or ((edge1.end==String2) and (edge1.start==String1)):
            return edge1.time
    print('Error')
    return -1

def retrievevertexbycode(String1,vertexlist):
    for vertex1 in vertexlist:
        if vertex1.code==String1:
            return vertex1
    return -1
def vertexinpath(String1,path1):
    default='False'
    for vertex in path1.sequence:
        if vertex.code==String1:
            default="True"
    return default
def getpath(path1):
    String=''
    for vertex1 in path1.sequence:
        String += ' '
        String+=vertex1.code
    return String






