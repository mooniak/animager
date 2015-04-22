### main python script

import sys, getpass
from genImages import gitGenTempImages
from genVideo import genVideo
from profiles import readProfile
from profiles import writeProfile
from profiles import getProfList


def main( argv ):

    userName = getpass.getuser()
    gitDir = ''
    frameRate = '25'
    height = ''
    width = ''

    if '-p' in argv:
        pName = argv[ argv.index( '-p' ) + 1 ]
        options = readProfile( pName )

        print(options)
        
        if '-f' in options:
            i = options.index( '-f' ) + 1
            frameRate = str( options[ i ] )

        if '-h' in options:
            i = options.index( '-h' ) + 1
            height = options[ i ]

        if '-w' in options:
            i = options.index( '-w' ) + 1
            width = options[ i ]

    elif '-pnew' in argv:
        writeProfile( argv )
        sys.exit( 0 )

    elif '-plist' in argv:
        getProfList( userName )
        sys.exit( 0 )
    print(height)
    print(width)
    gitGenTempImages( '/home/' + userName + '/animager/' )
    
    genVideo( '/home/' + userName + '/animager/',
              frameRate, height, width,
              '/home/' + userName + '/animager/' )


if __name__ == "__main__":
    
    main( sys.argv )
