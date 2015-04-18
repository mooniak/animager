### generate a video file using generated temporary image files
### dependencies : ffmpeg, imagemagick

import os
import glob


def morphImages( value, inputExt, outputExt ):

    print('\nmorphing images...\n')
    os.system( 'mkdir -p temp\/morph-cache' )
    os.system( 'convert ' + 'temp\/*' + inputExt
               + ' -delay ' + value
               + ' -morph 20 '
               + 'temp\/morph-cache\/\%'
               + '05d'
               + outputExt )


def genVideo():

    morphImages( value = '10',
                 inputExt = '.png',
                 outputExt  = '.jpg' )


    ##os.system('ls morph-cache/')
    os.system( 'ffmpeg '
               +'-framerate 20 '
               + '-i temp\/morph-cache\/\%05d.jpg '
               + '-c:v h264 '
               + '-r 30 '
               + '-pix_fmt yuv420p '
               + 'out.mp4' )
