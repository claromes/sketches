import py5
import py5_tools

v = 0
p = 0

def setup():
    py5.size(1000, 1000)
    py5.background(0)

def draw():
    global v, p

    v += 0.05
    p += 1

    x = py5.sin(v) * 100
    y = py5.cos(v) * 100

    x2 = py5.sin(v) * 100
    y2 = py5.cos(v) * 100

    py5.rect(0 + p, 0 + p, x, y)
    py5.rect(0 + p, 0 + p, x2, y2)

    py5.rect(250 + p, 0 + p, x, y)
    py5.rect(0 + p, 250 + p, x2, y2)

    py5.rect(500 + p, 0 + p, x, y)
    py5.rect(0 + p, 500 + p, x2, y2)

    py5.rect(750 + p, 0 + p, x, y)
    py5.rect(0 + p, 750 + p, x2, y2)

    if py5.frame_count % 10 == 0:
        py5.fill(py5.random(200, 255), py5.random(0, 255))
        py5.stroke_weight(py5.random(1, 2))

#frames = py5_tools.save_frames('/frame1', limit=2500, start=0)

py5.run_sketch()