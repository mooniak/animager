### generate a video file using generated temporary image files
### dependencies : ffmpeg, imagemagick

import os
import glob

'''
def morphImages( inDir, outDir, value, inputExt, outputExt ):

    print('\nmorphing images...\n')
    os.system( 'mkdir -p ' + outDir +'morph-cache' )
    os.system( 'convert ' + inDir +
               + '\%05d' + inputExt
               + ' -delay ' + value
               + ' -morph 20 '
               + outDir + 'morph-cache/'
               + '%05d' + outputExt )  '''


def genVideo( inputDir, outputDir ):

    ###morphImages( inputDir, outputDir, '10', '.png', '.jpg' )


    ##os.system('ls morph-cache/')
    os.system( 'ffmpeg '
               +'-framerate 1/5 '
               + '-i ' + inputDir + 'morph-cache\/\%05d.jpg '
               + '-c:v h264 '
               + '-r 30 '
               + '-pix_fmt yuv420p '
               + outputDir +' out.mp4' )
