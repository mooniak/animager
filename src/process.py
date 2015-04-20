### main python script

import getpass
from genImages import gitGenTempImages
from genVideo import genVideo
from profiles import readProfile
from profiles import writeProfile


def main():

    userName = getpass.getuser()
    
    gitGenTempImages( '/home/' + userName + '/animage/' )
    genVideo( '/home/' + userName + '/animage/',
              '/home/' + userName + '/animage/' )


if __name__ == "__main__":
    main()
