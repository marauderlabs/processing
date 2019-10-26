from node import Node
from random import randint

points = 20 # no. of vertices to start with
radius = 20 # of each vertex
nodes = []
visited = []
found = False # found the MST?

def setup():
    size(500, 500)
    for i in range(points):
        nodes.append(Node(randint(radius, width-1-radius), randint(radius, height-1-radius)))

def draw():
    
    background(200)
    
    ellipseMode(CENTER)
    fill(255)
    stroke(255)
    
    if not found:
        prims() #find it and draw
        prev = None
        for n in visited:
            ellipse(n.x, n.y, radius, radius)
            if prev:
                line(n.x, n.y, p.x, p.y)
            prev = n
                                   
        
def mouseClicked():
    nodes.append(Node(mouseX, mouseY))
    

def prims():
    global found
    global visited

    unvisited = nodes[:]
    visited = [unvisited.pop()]
    
    # v is visited. vi is visited index.
    # u is unvisited. ui is unvisited index.
    # between every visited and unvisited, find the minimum.

    while unvisited:
        shortest = float('inf')
        for vi, v in enumerate(visited):
            for ui, u in enumerate(unvisited):
                d = dist(v.x, v.y, u.x, u.y)
                if  d < shortest:
                    shortest = d
                    nextvi = vi
                    nextui = ui
        visited.append(unvisited.pop(nextui))
        
        
    found = True
    return
