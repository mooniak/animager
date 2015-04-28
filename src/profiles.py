### animate svg profile options - media presets
### preset folder default location set to ~/animage/profiles

import os
import sys
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
    i = 2

    home = '/home/' + getpass.getuser() + '/animager/profiles/'

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
    os.system( 'ls /home/' + userName + '/animager/profiles/*.prof'
               + ' | xargs -n 1 basename' )
    print()
