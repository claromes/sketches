import time
x = 0

def setup():
    size(650, 650)
    background(000)
    time.sleep(4)
    
def draw():
    global x
    no_fill()
    
    x += cos(12) * 10

    for i in range(200):
        stroke(random(256), random(256), random(256))
        stroke_weight(1)

        point(PI * i * 2, x / PI * 2)

    for j in range(200):
        stroke(random(256), random(256), random(256))
        stroke_weight(random(1, 2))

        point(PI * j * 5, x * PI / PI * 0.5)

    frame_rate(24)
    
    if frame_count > 160:
        no_loop()