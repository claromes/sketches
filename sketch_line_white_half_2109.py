def setup():
    size(600, 600)
    background(0)

def draw():
    filter(BLUR, 1)
    stroke(255)
    fill(255)

    x = 0
    y = 0

    for j in range(10):
        x = j + x
        y = j + y

        line(601, 601, -1, 0)

        for i in range(15):
            x = i + x
            y = i + y

            line(x, y, x, random(y))
            stroke(random(255))
            fill(random(255))
            for i in range(5):
                ellipse(x,  random(y), 2, 2)
                stroke(255)
                fill(255)