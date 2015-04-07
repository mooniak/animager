# Animating a SVG process using a Git commits

So the idea is to make videos of proccess in designing graphics in Inkscape easily using git commits. 
Im just a dumb designer and dont know how to do this. :)

Idea came from [here](https://www.youtube.com/watch?v=WY9A2mug4dw).

##Process

The proposed process goes like this.

- Setup [Sparklshare](http://sparkleshare.org/)
- Set Up a git repository insde Sparklshare
- Start a new design project on Inkscape and save it as svg in the repository.
- Keep working and save from time to time.
- Sparklshare is making a git commit each time you save a file with Inkscape as a SVG.
- So we have all these git commits with different stages of the design process.
- The a python script will do the following.
     - Find all of the commits that touch this file with git log .
     - Find the file touched by a particular commit with git show .
     - Extract each page version from the repository with git cat-file blob .
     - Render each page to a PNG with Inkscape. (Size should be user configurable based on the size of Inkscape canvas size)
     - Use ImageMagick to convert the PNG (lossless) frames to JPEGs.
     - Use ffmpeg2theora to combine the frames into an ogg video.
 - Use some other tool to convert video into any other format. 

##Deliverables

- A Python script
- Dependency installer script
- SVG Template file
- A GitHub repo with all these files

##Needed stuff / References

- [Inkscape](http://inkscape.org)
- [ImageMagick](http://www.imagemagick.org/script/index.ph)      
- [Git](http://git-scm.com/)
- [SparkleShare](http://sparkleshare.org/)
- [Python](http://www.python.org/)
- [Ffmpeg](http://ffmpeg.org/)
- [Ffmpeg2theora](http://v2v.cc/~j/ffmpeg2theora/)  
