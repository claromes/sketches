add_library('VideoExport')

def setup():
    global video_export
    size(600, 600)
    background(0)
    frameRate(50)
    rectMode(CENTER)

    stroke(56, 246, 175)
    video_export = VideoExport(this, "animacao.mp4")
    video_export.startMovie()

def draw():
    filter(BLUR, 1)
    size = 60
    line_mo = 0

    for j in range(10):
        y = j * size  + size / 2

        for i in range(10):
            x = i * size  + size / 2

            fill_var = fill(1)
            size_var = random(10, 20)
            line_mo = line_mo * 1000
            rotate(radians(random(PI*10)))

            if j <= i or i >= j:
              size_var += 20

            line(x, line_mo, x, line_mo)
            fill(56, 246, 175)
            ellipse(x, y, 2, 2)


    if frameCount < 500:
        video_export.saveFrame()
    else:
        video_export.endMovie()
        exit()