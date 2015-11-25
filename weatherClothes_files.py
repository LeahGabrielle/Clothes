#All file functions

#open file
def openFile():
    fileName = input('Enter file name of all clothes\n')
    file = open(fileName,'r') 
    clothes = readFile(file)
    file.close
    return clothes

#creates a list of all clothes from file and sorts it into [ [tops] [bottoms] ]
def readFile(file):
    clothes = [ [], []]
    #tops = [ [top name, type, weather, location] ]
    for line in file:
        #section out files
        line.lower()
        cLine = line.split()
        #top or bottom?
        if cLine[1]=="top":
            clothes[0].append(cLine)
        else:
            clothes[1].append(cLine)
    print(clothes)
    return clothes
