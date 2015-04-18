### generate a video file using generated temporary image files

import os
import glob


def getImageList( imageExtension ):
    
    return glob.glob( '*' + imageExtension )
