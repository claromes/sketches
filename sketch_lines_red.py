def setup():
    size(600, 600)
    background(0)
    stroke(240, 26, 17)

def draw():
    filter(BLUR, 3)
    size = 100
    line_mo = 0

    for j in range(10):
        y = j * size  + size

        for i in range(10):
            x = i * size  + size

            fill_var = fill(1)
            size_var = random(1, 50)
            line_mo = line_mo * 300
            rotate(radians(random(PI*10)))
            rect(x, line_mo, size_var, line_mo)