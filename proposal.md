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


##Options 

- Video Name

- Service Presets
     By Service presets (This will cancel out video size and qulity )
     - Vimeo[spec](https://vimeo.com/help/compression)
               - Size
               - HD / SD
     - YouTube [spec](https://support.google.com/youtube/answer/1722171?hl=en)
               - Size
               - HD / SD
     - FaceBook [spec](https://www.facebook.com/help/124738474272230)
               - Size
               - HD / SD

- Custom Settings
     - Other FileFormat selections
          - All supported formats from ffmepg
     - Video Size / Qulity settings
          - 1080p
          - 720p
          - 360p
     - Save custom setting (optional)
     - Video Qulity (1-10 scale)

- Add a title slide
     - Add a 10 sec title slid at the begining of the video
     - Text Input

- Append Audio File to video (Not that important) -  
     - Colud be done using [Ffmpeg2theora](http://v2v.cc/~j/ffmpeg2theora/) 
     - 

##Deliverables

- Installer script (http://voidandany.free.fr/index.php/installer-de-facon-automatique-une-liste-de-package-et-les-depots-associes/ )
- Script
- Template files to start
- Documentation
- A GitHub repo with all these files

##Extras
- Support GIMP and Krita file formats. (.xfc / )
- Support on Windows
- Supprt on Mac
- GUI (Maybe Someday)

##Needed stuff / References

- [Inkscape](http://inkscape.org)
- [ImageMagick](http://www.imagemagick.org/script/index.ph)      
- [Git](http://git-scm.com/)
- [SparkleShare](http://sparkleshare.org/)
- [Python](http://www.python.org/)
- [Ffmpeg](http://ffmpeg.org/)
- [Ffmpeg2theora](http://v2v.cc/~j/ffmpeg2theora/)  
