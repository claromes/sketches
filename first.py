#Thonny IDE
#Imported mode for py5 on

import pymunk as pm

space = pm.Space()
shapes = []

def settings():
    size(800, 80)

def setup():
    space.gravity = (0, 600)
    
    shapes.extend((
        pm.Segment(space.static_body, (0, 0), (800, 0), 1),
        pm.Segment(space.static_body, (0, 0), (0, 80), 1),
        pm.Segment(space.static_body, (0, 80), (800, 80), 1),
        pm.Segment(space.static_body, (800, 0), (800, 800), 1)
        ))  
    
    for shp in shapes:
        shp.elasticity = 0.8
        space.add(shp)
    
def draw():
    background(000)
    
    mass = 10
    moi = pm.moment_for_circle(mass, 0, 5)
    
    body = pm.Body(mass, moi)
    body.position = (1, 1)
    
    shp = pm.Circle(body, 5, (0, 0)) 
    shp.friction = 0.5
    shp.elasticity = 1
    
    shapes.append(shp)
    space.add(body, shp)
    
    for shp in shapes:
        no_stroke()
        x, y = shp.body.position
        circle(x, y, 10)
        
    space.step(0.02)