def setup():
    size(600, 600)
    background(0, 14, 251)

def draw():
    filter(BLUR, 1)
    stroke(179, 216, 236)

    line(601, -1, -1, random(-1, 300))
    line(-1, 601, 601, random(300, 600))