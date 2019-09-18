from random import randint

cols = 50

heights = []
w = 0
iter = 0
jter = 0

def setup():
    # size(400,200)
    fullScreen()
    background(255)
    stroke(0)
    strokeWeight(1)
    fill(100, 50, 255)
    
    for i in range(cols):
        heights.append(randint(0, height-1))
    global w 
    w = width/cols
    
    frameRate(10)
    
            
def draw():
    global iter
    global jter
    
    background(255)
    
    # done with everyone. Stop animation
    if iter == cols-1:
        fill(100, 50, 255)
        for i in range(cols):
            rect(i*w, height-heights[i], w-1, heights[i])
        noLoop()

    #1 pass of sort        
    swapped = False
    if heights[jter] > heights[jter+1]:
        swapped = True
        swap(heights, jter, jter+1)
                   
    # draw everyone
    for i in range(cols):
        if i == jter or i == jter+1:
            if swapped:
                fill(255, 0, 0)
            else:
                fill(0, 255, 0)
        else:
            fill(100, 50, 255)
        rect(i*w, height-heights[i], w-1, heights[i])

    jter += 1
    if jter >= cols-1-iter:
        jter = 0
        iter += 1

def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]

                
