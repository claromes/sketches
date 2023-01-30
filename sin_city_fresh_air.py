import py5
import py5_tools

def settings():
    py5.size(500, 900)

def setup():
    anime = py5.create_font("animeace2_reg.otf", 8)

    py5.background(255)
    py5.text_font(anime)
    py5.ellipse_mode(py5.CORNER)
    py5.stroke_cap(py5.ROUND)

    py5.no_loop()

def draw():
    layout()

    light()
    gate()

    flakes(50, 550, 470, 50)
    flakes(590, 850, 470, 50)

    text_fresh()
    text_its_good()
    text_page()

def flakes(low, high, stop, start = 0):
    py5.fill(255)
    py5.no_stroke()

    for i in range(start, stop):
        py5.ellipse(i - 10, py5.random(low, high) - 20, py5.random(2, 8), py5.random(3, 8))

def gate():
    py5.stroke(0)

    x_space_left = 0
    x_space_right_top = 0
    x_space_right_bot = 0
    y_space = 0
    for _ in range(14):
        x_space_left += 3
        y_space -= 3
        #left
        py5.stroke_weight(2)
        py5.line(95 + x_space_left, 120 + y_space, 160 + x_space_left, 400 + y_space)

        #right
        x_space_right_top += 15
        x_space_right_bot += 5
        py5.stroke_weight(3)
        py5.line(250 + x_space_right_top, 100, 252 + x_space_right_bot, 400)
        py5.line(252 + x_space_right_bot, 400, 258 + x_space_right_top, 555)

    py5.no_stroke
    py5.fill(0)

    #left
    py5.quad(140, 310, 186, 280, 192, 310, 148, 342)
    py5.quad(156, 372, 198, 338, 198, 342, 157, 376)

    #right
    py5.quad(256, 317, 362, 319, 344, 360, 254, 357)
    py5.quad(362, 319, 443, 343, 404, 405, 344, 360)

    py5.quad(255, 386, 327, 390, 325, 394, 255, 391)
    py5.quad(327, 390, 377, 416, 374, 429, 325, 394)

def light():
    py5.fill(255)
    py5.no_stroke()

    py5.triangle(50, 555, 250, 300, 450, 555)
    py5.triangle(150, 470, 250, 220, 50, 200)
    py5.triangle(250, 220, 350, 470, 450, 200)
    py5.triangle(80, 250, 420, 250, 250, 555)
    py5.ellipse(70, 150, 360, 120)

def text_fresh():
    t = "FRESH AIR.\nBRACING\nCOLD."

    py5.fill(255)
    py5.stroke(0)
    py5.stroke_weight(3)
    py5.rect(300, 500, 150, 120)

    py5.fill(0)
    py5.text_size(12)
    py5.text(t, 310, 520)

def text_its_good():
    t = "IT'S GOOD\nTO BE OUT."

    py5.fill(255)
    py5.rect(350, 715, 75, 45)

    py5.fill(0)
    py5.text_size(9)
    py5.text(t, 358, 732)

def text_page():
    t = "18"

    py5.fill(0)
    py5.text_size(12)
    py5.text(t, py5.width/2, 860)

def layout():
    py5.fill(0)
    py5.rect(30, 60, 440, 500)
    py5.rect(30, 570, 440, 270)

    py5.fill(255)
    py5.stroke(255)

    py5.rect(py5.width/2, 845, 15, 20)

frame = py5_tools.save_frames('/sin_city_fresh_air', limit=1, start=0)

py5.run_sketch()