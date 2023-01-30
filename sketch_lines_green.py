add_library('VideoExport')

def setup():
    global video_export
    size(1080, 1080)
    background(0)
    frameRate(12)
    #rectMode(CENTER)

    stroke(56, 246, 175)
    video_export = VideoExport(this, "sketch_210919b.mp4")
    video_export.startMovie()

def draw():
    filter(BLUR, 1)
    size = 108
    line_mo = 0

    for j in range(10):
        y = j * size  + size
        #translate(random(600), random(10))
        for i in range(10):
            x = i * size  + size

            fill_var = fill(1)
            size_var = random(10, 20)
            line_mo = line_mo * 1000
            rotate(radians(random(PI*10)))

            if j <= i or i >= j:
              size_var += 20


            #rect(x, y, size_var, size_var)
            line(x, x, line_mo, line_mo)
            fill(56, 246, 175)
            ellipse(x, y, 2, 2)
            #translate(width, random(10))

    if frameCount < 99:
        video_export.saveFrame()
    else:
        video_export.endMovie()
        exit()