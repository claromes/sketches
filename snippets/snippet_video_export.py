#source: https://abav.lugaralgum.com/material-aulas/Processing-Python/exportar_animacoes.html

import __main__
add_library('VideoExport')

file_name = __main__.__file__.split(".", 1)

def setup():
    global video_export

    video_export = VideoExport(this, file_name[0] + ".mp4")
    video_export.startMovie()

def draw():
    if frameCount < 600:
        video_export.saveFrame()
    else:
        video_export.endMovie()
        exit()
