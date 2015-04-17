### generate temporary images using GIT commits

import os

def generateTemporaryImage( inputName, inputExtension, options,
                  outputName, outputExtension, ouputDirectory ):
    os.system( 'convert ' + inputName + inputExtension + ' ' + options
               + ' ' + outputDirectory + outputName + outputExtension )

def generateGitCommitArray():
    os.system( 'git log --pretty=%h > log' )
    commits = open('log').read().splitlines()
    return commits

def gitCheckoutOld( commitHash ):
    os.system( 'git checkout ' + commitHash )

def gitGenerateTemporaryImages():
    os.system( 'mkdir temp' )
    commits = generateGitCommitArray()
    commits.reverse()

    count = 1
    for commitHash in commits:
        gitCheckoutOld( commitHash )
        generateTemporaryImage( 'test', '.svg', '', 'temp/', str(count),
                                '.png'  )
        count += 1
