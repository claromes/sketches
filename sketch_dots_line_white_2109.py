def setup():
    size(600, 600)
    background(0)

def draw():
    filter(BLUR, 1)
    stroke(255)

    size = 20

    for i in range(100):
        x = size + 40 / 2

        ellipse(x*i, random(x*i), 2, 2)
        ellipse(random(x*i), x*i, 2, 2)