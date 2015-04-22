### animate svg profile options - media presets
### preset folder default location set to ~/animage/profiles

import os
import sys
import glob
import getpass


def readProfile( pName ):

    home = '/home/' + getpass.getuser() + '/animager/profiles/'
    try:
        file = open( home + pName + '.prof', 'r' )
        
        options = []
    
        for line in file:
            options.append( line.split() )

        return options

    except:
        print( "No such profile." )
        sys.exit( 0 )


def writeProfile( arguments ):

    options = arguments
    print(options)
    i = 2

    home = '/home/' + getpass.getuser() + '/animager/profiles/'
    print(home)
    file = open( home + options[ i ] + '.prof', 'w+' )

    for option in options:

        if option is 'process.py':
            continue
            
        elif option.startswith( '-' ):
            file.write( option )

        else:
            file.write( ' ' + option + '\n' )


def getProfList( userName ):

    print( '\nAvailable profiles.\n' )
    print(glob.glob( "/home" + userName + "/animager/profiles/*.prof" ))
    for prof in glob.glob( "/home" + userName + "/animager/profiles/*.prof" ):
        print( '* ' + prof )

    print( '\n' )
