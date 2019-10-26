from Cell import Cell
from heapq import heappop, heappush

cells = []
H = W = 10 # Height & width of cells
R = C = 0  # no of rows and cols
S = D = None #src and destination
cellsToExplore = []
done = False

def setup():
    global R
    global C
    global S
    global D
    
    size(400, 400)
    background(255)
    
    R = height/H
    C = width/W
    Cell.setSize(H, W)
    
    #create the cells
    for r in range(R):
        row = []
        for c in range(C):
            row.append(Cell(c, r))
        cells.append(row)
    
    S = cells[0][0]
    D = cells[R-1][C-1]
    S.setSource()
    D.setDestination()
    heappush(cellsToExplore, (S.d, S))

def draw():
    global done
    
    drawCells()
    if done:
        noLoop()
        return
    
    if not cellsToExplore:
        print("No Path!")        
        noLoop()
        return        
    
    done = dijkstra()
    
    
    
    
def dijkstra():
    
    _, cur = heappop(cellsToExplore) #ignore the dist. We have it in the obj
    
    if cur == D:
        drawPath(D)
        return True
    
    for n in getNeighbors(cur):
        n.visited = True
        d = cur.d + 1 #all neighbors are away by 1 step
        
        if d < n.d: # better new distance
            n.d = d
            n.parent = cur
            heappush(cellsToExplore, (n.d, n))
        

def drawPath(dst):
    steps = 0
    while dst:
        steps += 1
        dst.best = True
        dst = dst.parent
        
    print("Steps: ", steps)    

def drawCells():

    for r in range(R):
        for c in range(C):
            cells[r][c].show()

            
        
def getNeighbors(cell, diagonals=False): #need diagonal neighbors?
    if not diagonals:
        dirs = [        (0, -1),        #UP
                (-1, 0),        (1, 0), #L, R
                        (0, 1)          #DOWN
                ]
    else:
        dirs = [(-1, -1),  (0, -1), (1, -1),
                (-1,  0),           (1,  0),
                (-1,  1),  (0,  1), (1,  1)
            ]
    n = []
    #get neighbors in all directionss and see if they're on the map. return them
    for d in dirs: 
        x = cell.x + d[0]
        y = cell.y + d[1]
        if x < 0 or x >= C or y < 0 or y >= R:
            continue
        n.append(cells[y][x])
    
        
    return n

# A local implementation of heappop and heappush which does no heapify but linear search for smallest
# push just appends
# pop finds the first lowest item. 
# To test against actual heappush to see how the path turns out to be

# def heappush(arr, item):
#     arr.append(item)
    
# def heappop(arr):
#     lowest = arr[0][0]
#     lowesti = 0
#     for i in range(1, len(arr)):
#         if arr[i][0] < lowest:
#             lowest = arr[i][0]
#             lowesti = i
    
#     return arr.pop(lowesti)
