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
    p += 2

    x = py5.sin(v) * 500
    y = py5.cos(v) * 500

    x2 = py5.sin(v) * 500
    y2 = py5.cos(v) * 500

    py5.rect(500, p, x, y)
    py5.rect(500, p, x2, y2)

    if py5.frame_count % 10 == 0:
        py5.fill(py5.random(155, 255))
        py5.stroke_weight(py5.random(1, 10))

#frames = py5_tools.save_frames('/frame4', limit=1500, start=0)

py5.run_sketch()