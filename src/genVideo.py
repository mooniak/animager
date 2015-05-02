### generate a video file using generated temporary image files
### dependencies : ffmpeg, imagemagick

import os, getpass

'''
def morphImages( inDir, outDir, value, inputExt ):

    print('\nmorphing images...\n')
    userName = getpass.getuser()
    os.system( 'mkdir -p ' + '/home/' + userName
               + '/animager/morph-cache' )
    os.system( 'convert ' + inDir
               + '*' + inputExt
               + ' -delay ' + value
               + ' -morph 5 '
               + '/home/' + userName + '/animager/morph-cache/'
               + '\%05d.jpg')
'''

def genVideo( inputDir, frameRate, height , width , outputDir ):

    ##morphImages( inputDir, outputDir, '10', '.png' )

    if height is '' and width is '':
        os.system( 'ffmpeg '
                   +'-framerate ' + frameRate
                   + ' -i ' + inputDir + '%05d.png '
                   + '-c:v h264 '
                   + '-r 30 '
                   + '-pix_fmt yuv420p '
                   + outputDir +'out.mp4' )

    elif height is '' and width is not '':
        os.system( 'ffmpeg '
                   +'-framerate ' + frameRate
                   + ' -i ' + inputDir + '%05d.png '
                   + '-c:v h264 '
                   + '-r 30 '
                   + '-pix_fmt yuv420p '
                   + ' -vf scale=' + width + ':-1'
                   + ' ' + outputDir +'out.mp4' )

    elif height is not '' and width is '':
        os.system( 'ffmpeg '
                   +'-framerate ' + frameRate
                   + ' -i ' + inputDir + '%05d.png '
                   + '-c:v h264 '
                   + '-r 30 '
                   + '-pix_fmt yuv420p '
                   + ' -vf scale=' + '-1:' + height
                   + ' ' + outputDir +'out.mp4' )

    else:
        os.system( 'ffmpeg '
                   +'-framerate ' + frameRate
                   + ' -i ' + inputDir + '%05d.png '
                   + '-c:v h264 '
                   + '-r 30 '
                   + '-pix_fmt yuv420p '
                   + ' -vf scale=' + width + ':' + height
                   + ' ' + outputDir +'out.mp4' )
