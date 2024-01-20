from math import cos, sin, pi as PI



def setup():
    global n_sides, r
    background(0, 0, 0)
    stroke(255, 255, 255)
    size(600, 600)
    n_sides = 3
    r = 100
    
    
def draw():
    global n_sides, r
    
    
    x, y = 300, 300
    
    
    points = [(x+r, y)]
    
    for i in range(2, n_sides * 2, 2):
        px = x + r * cos(i*PI/n_sides)
        py = y + r * sin(i*PI/n_sides)
        points.append((px, py))

    for i in range(len(points)):
        
        x1, y1 = points[i]
        x2, y2 = points[(i+1)%len(points)]
        line(x1, y1, x2, y2)
        
    n_sides += 1
    if n_sides == 360:
        n_sides = 0
        r *= 1.5
        


    
    
