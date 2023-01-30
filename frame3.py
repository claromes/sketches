import py5
import py5_tools

v = 0
i = 0

def setup():
    py5.size(1000, 1000)
    py5.background(0)

def draw():
    global v, i

    v += 0.05
    i += 1

    x = py5.sin(v) * 250
    y = py5.cos(v) * 250

    x2 = py5.cos(v) * 250
    y2 = py5.sin(v) * 250

    py5.rect(0, i, x, y)
    py5.rect(250, i, x2, y2)
    py5.rect(500, i, x, y)
    py5.rect(750, i, x2, y2)
    py5.rect(1000, i, x, y)

    if py5.frame_count % 2 == 0:
        py5.fill(255, py5.random(0, 100))
        py5.stroke_weight(py5.random(2, 10))

#frames = py5_tools.save_frames('/frame3', limit=2000, start=0)

py5.run_sketch()