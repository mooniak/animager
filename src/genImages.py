### generate temporary images using GIT commits
### dependencies : imagemagick


import os


def genTempImage( inputName, inputExt, options,
                  outputName, outputExt, outputDir ):
    
    os.system( 'convert ' + inputName
               + inputExt + ' '
               + options
               + ' ' + outputDir
               + outputName
               + outputExt )


def gitCommitArray():
    
    os.system( 'git log --pretty=%h > log' )
    commits = open('log').read().splitlines()
    return commits


def gitCheckoutOld( commitHash ):
    
    os.system( 'git checkout ' + commitHash )


def gitGenTempImages( outputDir ):
    
    os.system( 'mkdir' + outputDir )
    commits = gitCommitArray()
    commits.reverse()

    count = 1
    for commitHash in commits:
        gitCheckoutOld( commitHash )
        
        genTempImage( inputName = 'drawing',
                                inputExt = '.svg',
                                options = '',
                                outputDir = outputDir,
                                outputName = str(count),
                                outputExt = '.png'  )
        count += 1

    print ("\nRolling changes back to master branch...\n")
    os.system( 'git checkout master' )
