### main python script

import getpass
from genImages import gitGenTempImages
from genVideo import genVideo
from profiles import readProfile
from profiles import writeProfile


def main():

    userName = getpass.getuser()
    
    gitGenTempImages( '/home/' + userName + '/animager/' )
    genVideo( '/home/' + userName + '/animager/',
              '/home/' + userName + '/animager/' )


if __name__ == "__main__":
    main()
