from math import cos, sin, pi as PI



def setup():
    global n_sides, r, x, y
    x = 0
    y = 300
    background(0, 0, 0)
    stroke(255, 255, 255)
    size(600, 600)
    n_sides = 3
    r = 10
        
def get_polygon_points(x, y, radius, n_sides):
    
    points = [(x+r, y)]
    
    for i in range(2, n_sides * 2, 2):
        px = x + radius * cos(i*PI/n_sides)
        py = y + radius * sin(i*PI/n_sides)
        points.append((px, py))
    return points

    
def draw():
    global n_sides, r, x, y
    
    
    points = get_polygon_points(x, y, r, n_sides)

    for i in range(n_sides):
        
        x1, y1 = points[i]
        x2, y2 = points[(i+1)%len(points)]
        line(x1, y1, x2, y2)
        
    n_sides += 1
    if n_sides == 40:
        n_sides = 0
        r *= 1.5
        x += 50
        


    
    
