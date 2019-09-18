from node import Node
from random import randint

points = 20
radius = 20
nodes = []
visited = []
found = False

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
        dijkstras()
        p = None
        for n in visited:
            ellipse(n.x, n.y, radius, radius)
            if p:
                line(n.x, n.y, p.x, p.y)
            p = n
                                   
        
def mouseClicked():
    nodes.append(Node(mouseX, mouseY))
    

def dijkstras():
    found = True
    unvisited = nodes[:]
    global visited
    visited = [unvisited.pop()]
    
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
        
        
