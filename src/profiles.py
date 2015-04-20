### animate svg profile options - media presets
### preset folder default location set to ~/animage/profiles

import os
import getpass


def readProfile( pName ):

    home = '/home/' + getpass.getuser() + '/animage/profiles/'
    try:
        file = open( home + pName + '.prof', 'r' )
        
        options = []
    
        for line in file:
            options.append( line.split() )

        return options

    except:
        print( "No such profile." )


def writeProfile( arguments ):

    options = arguments.split()
    print(options)
    i = 1

    home = '/home/' + getpass.getuser() + '/animage/profiles/'
    print(home)
    file = open( home + options[ i ] + '.prof', 'w+' )

    for option in options:
        
        if option.startswith( '-' ):
            file.write( option )
        else:
            file.write( ' ' + option + '\n' )
