### animate svg profile options - media presets

import os


def readProfile( pName ):

    file = open( pName + '.prof', 'r' )
    options = []
    
    for line in file:
        options.append( line.split() )

    return options


def writeProfile( arguments ):

    options = arguments.split()
    print(options)
    i = 1
    
    file = open( options[ i ] + '.prof', 'w+' )

    for option in options:
        
        if option.startswith( '-' ):
            file.write( option )
        else:
            file.write( ' ' + option + '\n' )
