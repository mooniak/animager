### generate a video file using generated temporary image files
### dependencies : ffmpeg, imagemagick

import os
import glob


def morphImages( value, inputExt, outputExt ):

    os.system( 'mkdir -p morph-cache' )
    os.system( 'convert ' + '*' + inputExt
               + ' -delay ' + value
               + ' -morph 10 '
               + 'morph-cache\/\%'
               + '05d'
               + outputExt )


def genVideo():

    morphImages( value = '1000',
                 inputExt = '.png',
                 outputExt  = '.jpg' )


    ##os.system('ls morph-cache/')
    os.system( 'ffmpeg '
               +'-framerate 1\/\5 '
               + '-i morph-cache\/\%05d.jpg '
               + '-c:v h264 '
               + '-r 30 '
               + '-pix_fmt yuv420p '
               + 'out.mp4' )
