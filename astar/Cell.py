import sys.maxsize as INF

class Cell():
    # h = 0
    # w = 0
    
    @staticmethod
    def setSize(h, w, p):
        Cell.h = h
        Cell.w = w
        Cell.wall_percentage = p
    
    def __init__(self, r, c):
        self.x = r # row
        self.y = c # col
        self.h = 0 # heuristic - dist to target
        self.d = 0 # dist from - dist from source
        self.wall = False # Am I wall?
        self.visited = False
        self.src = False #TODO: Use an enum
        self.dst = False
        
        self.h = 0 # the heuristic to dst. For use in A*. Unused in Dijkstras
        self.d = INF # the dist from src
        self.parent = None
        self.best = False
        self.visited = False
        
        if random(1) < Cell.wall_percentage:
            self.wall = True
    
    def show(self, clr=None):

        if self.src:
            fill(255, 0, 0)
        elif self.dst:
            fill(0, 255, 0)
        elif self.wall:
            fill(0)
        elif self.best:
            fill(0, 255, 255) #cyan
        elif self.visited:
            fill(255,255,0) #yellow
        else:
            fill(255) #white
    
        stroke(0)
        rect(self.x * Cell.w, self.y * Cell.h, Cell.w-1, Cell.h-1)
        
        #some debug
        #textSize(32)
        #fill(0)
        #text("({},{})".format(self.x, self.y), self.x * Cell.w, self.y * Cell.h +32)
    
    def setSource(self):
        self.d = 0
        self.src = True
        
    def setDestination(self):
        self.d = INF
        self.dst = True
    
    def __str__(self):
        return "({},{})".format(self.x, self.y)
