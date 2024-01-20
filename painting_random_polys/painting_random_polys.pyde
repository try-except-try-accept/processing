from math import cos, sin, pi as PI



def setup():
    global n_sides, r, x, y, frame, side_change, mul
    frameRate(10)
    x = 300
    y = 300
    background(0, 0, 0)
    stroke(255, 255, 255)
    size(600, 600)
    n_sides = 12
    r = 10
    side_change = -1
    mul = 5
        
def get_polygon_points(x, y, radius, n_sides):
    
    points = [(x+r, y)]
    
    for i in range(2, n_sides * 2, 2):
        px = x + radius * cos(i*PI/n_sides)
        py = y + radius * sin(i*PI/n_sides)
        points.append((px, py))
    return points

def draw_poly(points):
    fill(random(255), random(255), random(255))
    beginShape()
    for i in range(n_sides):        
        x1, y1 = points[i]
        
        vertex(x1, y1)
    endShape()
    
    
def draw():
    global n_sides, r, x, y, frame, side_change, mul
    
    
    points = get_polygon_points(x, y, r, n_sides)
    
    
    
    #background(0, 0, 0)
    draw_poly(points)
        
    n_sides += side_change
    r += (side_change * mul)
    
    if n_sides == 3:
        side_change = 1
        mul /= 2
        
    elif n_sides == 12:
        side_change = -1
        mul /= 2

def mouseMoved():
    global x, y
    x = mouseX
    y = mouseY

    
    
