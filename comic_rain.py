import py5

# s = 0
# a = 255
# x = py5.random(392, 500)
# y = py5.random(0, 500)

def settings():
    py5.size(500, 500)

def draw():
    py5.frame_rate(12)
    py5.background(0)
    py5.no_stroke()

    #frame_1
    background(0, 0, 350, 350)
    sky()
    skyline(10, 60)
    skyline(40, 10)
    skyline()
    windows()

    #frame_2
    background(0, 350, 350, 150)
    windows_close()
    rain_skyline()

    #frame_3
    #background(358, 0, 150, 500)
    cables()
    bird()

    layout()

def rain_skyline():
    #tiny drops
    py5.fill("#f9f4a0")
    for i in range(350):
        py5.rect(i, py5.random(350, 500), 0.5, py5.random(0.5, 1.5))

    #standard drops
    py5.fill(255)
    for i in range(350):
        py5.rect(i, py5.random(350, 500), py5.random(1, 2), py5.random(5, 20))

def skyline(offset_x = 0, offset_y = 0):
    py5.fill(0)
    py5.rect(0 - offset_x, 100 - offset_y, 50, 250)
    py5.rect(50 - offset_x, 250 - offset_y, 30, 100)
    py5.rect(80 - offset_x, 50 - offset_y, 90, 300)
    py5.rect(170 - offset_x, 200 - offset_y, 35, 150)
    py5.rect(205 - offset_x, 150 - offset_y, 50, 200)
    py5.rect(255 - offset_x, 300 - offset_y, 65, 50)
    py5.rect(320 - offset_x, 180 - offset_y, 90, 170)

def sky():
    py5.fill(255)
    if (py5.frame_count == 15
        or py5.frame_count == 18
        or py5.frame_count == 20
        or py5.frame_count % 40 == 0
        or py5.frame_count % 42 == 0
        or py5.frame_count % 44 == 0
        or py5.frame_count % 46 == 0
        or py5.frame_count % 60 == 0
        or py5.frame_count % 62 == 0
        or py5.frame_count % 63 == 0):
        py5.rect(0, 0, 350, 350)

def windows():
    py5.fill("#f9f4a0")
    py5.rect(25, 80, 15, 25)
    py5.rect(45, 80, 15, 25)
    py5.rect(25, 250, 15, 25)
    py5.rect(200, 100, 15, 25)
    py5.rect(180, 200, 15, 25)
    py5.rect(295, 215, 15, 25)
    py5.rect(280, 300, 15, 25)

def windows_close():
    py5.fill("#f9f4a0")
    py5.rect(20, 375, 60, 100)
    py5.rect(90, 375, 60, 100)

def cables():
    if (py5.frame_count == 15
        or py5.frame_count == 18
        or py5.frame_count == 20
        or py5.frame_count % 40 == 0
        or py5.frame_count % 42 == 0
        or py5.frame_count % 44 == 0
        or py5.frame_count % 46 == 0
        or py5.frame_count % 60 == 0
        or py5.frame_count % 62 == 0
        or py5.frame_count % 63 == 0):
        py5.fill(255)
        py5.rect(358, 0, 150, 500)

    py5.no_fill()
    py5.stroke(0)
    py5.stroke_weight(2)
    py5.arc(500, 100, 298, 50, py5.HALF_PI, py5.PI)
    py5.arc(500, 100, 298, 40, py5.HALF_PI, py5.PI)

    py5.arc(550, 10, 200, 600, py5.HALF_PI, py5.HALF_PI*2)

    py5.arc(500, 250, 298, 50, py5.HALF_PI, py5.HALF_PI*2)
    py5.arc(500, 270, 298, 35, py5.HALF_PI, py5.HALF_PI*2)

    py5.arc(500, 450, 298, 40, py5.HALF_PI, py5.HALF_PI*2)
    py5.no_stroke()

def bird():
    py5.fill(0)

    py5.ellipse(400, 265, 10, 22)
    py5.ellipse(400, 258, 6, 8)
    py5.triangle(405, 270, 400, 280, 395, 270)
    py5.triangle(400, 255, 400, 260, 392, 256)

    py5.no_fill()

# def drop_floor():
#     global s, a, x, y
#     py5.no_fill()
#     py5.stroke(255)
#     py5.stroke_weight(2)

#     while s < 80 and a > 0:
#         s += 1
#         a -= 10
#         py5.stroke(255, a)
#         py5.ellipse(x, y, s, s)
#         break

def layout():
    #grid
    py5.fill(255)
    py5.rect(0, 350, 350, 12)
    py5.rect(350, 0, 12, 500)

    #frame
    py5.rect(0, 0, 500, 12)
    py5.rect(0, 0, 12, 500)
    py5.rect(488, 0, 12, 500)
    py5.rect(0, 488, 500, 12)

def background(x, y, w, h,):
    py5.fill(0)
    py5.rect(x, y, w, h)

py5.run_sketch()