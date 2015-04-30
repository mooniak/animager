# Animating steps of a graphic design process using Git commits


Make videos of proccess in designing graphics in vector or raster editors ( Inkscape, GIMP ) easily.


Save and commit step by step, your graphic designing process and use Animager to build a video to see the progress.
What Animager does is rolling the git commits and capture the image for each commit as a temporary image, collect all temporary images and build the video.

###Supported image formats
Animager uses imagemagick to convert the images. Supported image format list is here, http://www.imagemagick.org/script/formats.php


###Dependencies
  - ffmpeg
  - imagemagick
  - python3
  - C++ compiler - g++


###Install

```
sh install.sh
```

###How to use animager
  - Get a list of profiles
`animager -plist all`
  - Create a new profile
`animager -pnew profileName -h height -w weight -f frameRate`
  - Animager your image
`animager -p profileName -i inputImage -o videoOutputLocation`


Once you are done and ready to generate a video..

```
animager -p hd-720p -i [path-to-your-image] -o [path-to-your-output-folder]
```


###ToDo


###Credits


###License
