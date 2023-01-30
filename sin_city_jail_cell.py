import py5
import py5_tools

def settings():
    py5.size(1000, 850)

def draw():
    py5.background(0)
    grid_horizontal()

def grid_horizontal():
    py5.push_matrix()
    py5.rotate(0.3)

    grid_vertical()

    py5.fill(255)
    py5.rect(500, 150, 200, 200)

    py5.no_fill()
    py5.stroke(255)
    py5.stroke_weight(15)

    s = 60
    sp = 0
    for i in range(4):
        sp += 1
        s *= 0.5 + sp
        py5.rect(500 - s/2, 150 - s/2, 200 + s, 200 + s)

    strips()
    seat()
    toilet()

    py5.pop_matrix()

def grid_vertical():
    py5.stroke(255)
    py5.stroke_weight(13)

    a = 0

    for _ in range(30):
        a += 12
        py5.line(
            600,
            250,
            740 + py5.cos(py5.radians(a)) * ((min(py5.width, py5.height) / 2) * 1.8),
            200 + py5.sin(py5.radians(a)) * ((min(py5.width, py5.height) / 2) * 1.8)
        )

def strips():
    py5.stroke(0)
    py5.stroke_weight(1)

    sp_grid = 0
    for _ in range(19):
        sp_grid += 10
        py5.rect(500 + sp_grid, 160, 1, 180)

def seat():
    py5.fill(255)
    py5.no_stroke()

    py5.rect(480, 130, 240, 80)

def toilet():
    py5.fill(0)
    py5.rect(685, 302, 30, 76, 8)
    py5.rect(670, 315, 30, 35)

    py5.fill(255)
    py5.rect(653, 318, 30, 30, 4)
    py5.ellipse(660, 332, 45, 45)

    py5.fill(0)
    py5.ellipse(660, 332, 30, 30)

    py5.fill(255)
    py5.rect(695, 300, 30, 80, 8)

    py5.rect(690, 304, 2, 10, 4)

frame = py5_tools.save_frames('/sin_city_jail_cell', limit=1, start=0)

py5.run_sketch()