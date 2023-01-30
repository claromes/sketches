import py5
import py5_tools

pos = 0

def setup():
    py5.size(1000, 1000)
    py5.background(0)
    py5.no_stroke()

def draw():
    global pos, img

    pos += 10

    py5.fill(255, py5.random(0, 255))
    py5.rect(pos, py5.random(1, 1000), py5.random(5, 300), py5.random(1, 15))

    img = py5.load_image("frame3.png")
    mask = py5.load_image("mask.png")
    img.mask(mask)
    py5.image(img, 0, 0)

    if py5.frame_count == 150:
        py5.no_loop()

frames = py5_tools.save_frames('/frames', limit=150, start=0)

py5.run_sketch()