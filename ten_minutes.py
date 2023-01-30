import py5
#import py5_tools

v = 0

def setup():
    py5.size(1000, 1000)
    py5.background(0)

def draw():
    global v

    v += 0.02

    x = py5.sin(v) * 500
    y = py5.cos(v) * 500

    x2 = py5.cos(v) * 500
    y2 = py5.sin(v) * 500

    py5.rect(500, 500, x, y)
    py5.rect(500, 500, x2, y2)

    if py5.frame_count % 10 == 0:
        py5.fill(py5.random(155, 255))
        py5.stroke_weight(py5.random(1, 10))

#frames = py5_tools.save_frames('/frames', limit=1000, start=0)

py5.run_sketch()