import pymunk as pm

space = pm.Space()
shapes = []

x1 = 0
x2 = 100
y1 = 100
y2 = 100

coll = 0

def settings():
    size(650, 650)

def setup():
    global x1, x2, y1, y2, coll
    space.gravity = (0, 600)
    
    for _ in range(4):
        x1 += 100
        x2 += 100
        
        y1 += 100
        y2 += 100
        
        coll += 1
        
        seg = pm.Segment(space.static_body, (x1, y1), (x2, y2), 4)
        
        #seg.elasticity = 0.2
        seg.friction = 0.05
        seg.collision_type = coll
        
        shapes.append(seg)
        space.add(seg)
        
def draw_square():
    mass = 100 * 0.02
    moi = pm.moment_for_box(mass, (10, 10))
    
    body = pm.Body(mass, moi)
    body.position = (width / 4 + random(0, 10), height / 50 + random(-10, 0))
    
    shp = pm.Poly.create_box(body, (10, 10))
    
    shp.density = 0.02
    shp.friction = 1
    #shp.elasticity = 0.5
    shp.collision_type = 5
    
    shapes.append(shp)
    shp.color = "#323232"
    space.add(body, shp)
    
    handler_1 = space.add_collision_handler(1, 5)
    handler_2 = space.add_collision_handler(2, 5)
    handler_3 = space.add_collision_handler(3, 5)
    handler_4 = space.add_collision_handler(4, 5)
    
    handler_1.pre_solve = collide_1
    handler_2.pre_solve = collide_2
    handler_3.pre_solve = collide_3
    handler_4.pre_solve = collide_4
        
def collide_1(arbiter, space, data):
    for shp in arbiter.shapes:
        shp.color = "#00ffcc"
    return True
    
def collide_2(arbiter, space, data):
    for shp in arbiter.shapes:
        shp.color = "#ff0033"
    return True
    
def collide_3(arbiter, space, data):
    for shp in arbiter.shapes:
        shp.color = "#ffcc00"
    return True

def collide_4(arbiter, space, data):
    for shp in arbiter.shapes:
        shp.color = "#ff007f"
    return True 

def draw():
    background(000)
    stroke_weight(2)
    
    for shp in shapes:
        if isinstance(shp, pm.Segment):
            stroke("#00ffcc")
            line(102, 202, 202, 202)
            stroke("#ff0033")
            line(202, 302, 302, 302)
            stroke("#ffcc00")
            line(302, 402, 402, 402)
            stroke("#ff007f")
            line(402, 502, 502, 502)
        if isinstance(shp, pm.Poly):
            x, y = shp.body.position
            no_stroke()
            fill(shp.color)
            square(x, y, 10)
            
    space.step(0.02)
    
def key_pressed():
    draw_square()