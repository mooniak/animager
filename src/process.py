### main python script


from genImages import gitGenTempImages
from genVideo import genVideo
from profiles import readProfile
from profiles import writeProfile


def main():

    gitGenTempImages()
    genVideo()


if __name__ == "__main__":
    main()
