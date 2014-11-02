# Dark Theme For FontForge

A dark theme for [FontForge](http://fontforge.org)


### Animating a SVG in a Git Repository



Here's how we made the animation, in case you'd like to play alongat home:


       Install
          <a href="http://inkscape.org/">Inkscape</a>,
          <a href="http://www.imagemagick.org/script/index.php">ImageMagick</a>,
          <a href="http://git-scm.com/">Git</a>,
          <a href="http://www.python.org/">Python</a>,
          <a href="http://ffmpeg.org/">Ffmpeg</a>, and
          <a href="http://v2v.cc/~j/ffmpeg2theora/">Ffmpeg2theora</a>.
          On <a href="http://www.ubuntu.com/">Ubuntu</a> <a href="http://www.kernel.org/">Linux</a>, you can do this via:

apt-get install inkscape imagemagick git-core python ffmpeg ffmpeg2theora

          If you want to include a soundtrack,you'll also want
          <a href="http://www.xiph.org/oggz/">oggz</a> and
          <a href="http://www.xiph.org/downloads/">vorbis-tools</a>:


```
 apt-get install oggz-tools vorbis-tools
```


Make a new directory for your comic and initialize a git repository

`mkdir ~/ElectricPuppetTheatre`

` cd ~/ElectricPuppetTheatre`
`git init`
         (All of the remaining commands will be run from this directory)
  Use Inkscape to generate a template for your comic pages, or
        <a href="http://eptcomic.com/images/Template.svg">download ours</a>.  Save it as
         ~/ElectricPuppetTheatre/Template.svg .  If you create your
        own template, make the width:height ratio 2:3 ( e.g.  1200:1800).
        Add the template to your git repository:
         git add Template.svg
git commit Template.svg -m "Template for new pages"
        Make a subdirectory for the first issue and initialize the
        pages from the template:
         mkdir 001
for i in {01..24}; do
  cp Template.svg 001/"Page-${i}.svg";
done

        Draw each page in Inkscape.  Pause periodically to commit your
        work to the git repository.  The first time you commit a page,
        you will need to add it to the repository:
         git add 001/Page-01.svg
git commit 001/Page-01.svg -m "Started page 1 of issue 1"
        For subsequent commits, you can skip the add step:
         git commit 001/Page-01.svg -m "Inked first panel"
        Now we're ready to animate the repository!  First, make
        a working directory for the rendered images:
         mkdir IssueMovie
        Use our <a href="http://eptcomic.com/code/issuemovie.py">issuemovie.py</a>
        script to render a montage of the pages for each commit in
        the archive:
         chmod "a+x" issuemovie.py
./issuemovie.py
        Here's what the script is doing behind the scenes:

           Find all of the commits that touch this issue with
             git log .
            Find the pages touched by a particular commit with
             git show .
            Extract each page version from the repository with
             git cat-file blob .
            Render each page to a 160x240 pixel PNG with inkscape.
            Render each set of pages as an 8x3 grid with the
             montage  tool from ImageMagick.

         (This step took about 40 minutes to render 656 commits
          on 32-bit Ubuntu 10.04 on a 2GHz T7300).
        Move to the working directory for the final rendering steps:
         cd IssueMovie
        Use ImageMagick to convert the PNG (lossless) frames to
        JPEGs, setting quality to 100% to avoid lossy compression:
         for i in frame*.png ; do
  convert -quality 100 $i `basename $i png`jpg;
done
         Use ffmpeg2theora to combine the frames into an ogg video:
          ffmpeg2theora -F 6 -v 10 -i frame%04d.jpg -o MOS.ogv
         -v 10  gives the highest image quality, which is necessary
        to keep the pencils from blurring and to avoid artifacts on flat
        images, and  -F  sets the frame rate.  

        For  Round Midnight , we had 656 frames, for a length of
        1 minute 49 seconds at 6 frames per second.  Combining this
        with a slightly longer audio track gives the nice effect of
        holding for a few seconds on the final image; we used a 2 minute
        14 second mix of Sara and Louis jamming on the Electric Puppet
        Waltz, converting it to ogg audio with vorbis-tools:
          oggenc -n MOI.oga GuitarWaltz.wav
        and then combining (muxing) the audio and video streams with
        oggz-tools:
         oggz merge -o ept1.ogv MOS.ogv MOI.oga


     Bonus: Animating for YouTube
     The instructions above work for making an animation in the open,
      patent-safe OGG format.  Unfortunately, there are many places that
      OGG won't play.  Mark Pilgrim's Dive Into HTML5 <a title="410" href="http://eptcomic.com/images/410.png">had</a> an excellent
      discussion of <a title="cached copy from the internet archive" href="http://web.archive.org/web/20110726002026/http://diveintohtml5.org/video.html">the hairy details of distributing video on the web</a>, the short version of which is:
        There is no single combination of containers and codecs that works in all HTML5 browsers.</blockquote>
      More importantly, it is impossible to support all platforms without
      using patent-encumbered formats.  Rather than deal with this directly,
      we will punt the problem to Google by uploading our video to YouTube
      which supports uploads in the patent-safe WebM format.


      Here are the things we need to know about YouTube:


       YouTube supports OGG audio (vorbis) but not OGG video
        (theora).  It will let you upload an OGG audio+video file,
        but the result will be an audio stream on top of a green screen
        (so don't do this).
        The audio and video tracks need to be the same length.  If they
        aren't, YouTube will truncate the video to the shortest track.


      Got that?  Okay, here we go:


       Prepare your frames by following steps 1-10 of the OGG instructions
        above.
        Pad out the video portion to match the audio portion using
        additional "frames" symlinked to the last real frame.  Our last
        frame was frame0656.jpg.  We added a "closing credit" to this
        in inkscape, giving frame0657, then added 142 symlinked copies
        (23 seconds at 6 fps):
         for i in {658..800}; do ln --symbolic frame0657.jpg "frame0${i}.jpg"; done
        Use Ffmpeg to generate a WebM video, using our previous OGG audio
        track:
         ffmpeg -qscale 1 -r 6 -b 9600 -i frame%04d.jpg -vcodec libvpx -i MOI.oga ept1.webm

     Ffmpeg has WebM support starting with version 0.6.  If your system
      copy is older than this (as was the case for us on Ubuntu 10.04)
      you can compile a single-user bleeding-edge copy without overwriting
      the system copy.  Here's how:


       Make sure you have the GNU toolchain:
         sudo apt-get install build-essential
        Make a build directory:
         mkdir ffmpegwebm
cd ffmpegwebm
mkdir local
        Download and compile the latest V8 code, targeting our build
        directory:
         git clone http://git.chromium.org/webm/libvpx.git
cd libvpx
./configure --prefix=../local/
make &amp;&amp; make install
cd ..
        Download and compile the latest Ffmpeg code, enabling the WebM
        codecs:
         git clone git://git.videolan.org/ffmpeg
cd ffmpeg
./configure --prefix=../local/ --enable-libvorbis --enable-libvpx --enable-gpl \
--extra-cflags=-I../local/include/ --extra-libs=-L../local/lib/
make &amp;&amp; make install
cd ../..
         (The  --extra
          config flags tell autotools to look for the V8 headers and libraries
          in our local build directory)
        To reference the local build, step 3 above is now:
         ffmpegwebm/local/bin/ffmpeg -qscale 1 -r 6 -b 9600 \
-i frame%04d.jpg -vcodec libvpx -i MOI.oga ept1.webm



      Questions, comments, corrections?  Please send any and all feedback
      to markv [at] eptcomic.com.



## Credits
    <a href="http://eptcomic.com/videos/ept1.ogv" title="Click for ogg video">
    <img src="./Animating a Git Repository_files/ept1.png" alt="Montage of Hensen ex Machina, issue 1">
    </a>

      To celebrate EPT's first issue,
      <a href="http://eptcomic.com/cgi-bin/comic.cgi?volume=1">Round Midnight</a>,
      we made a two minute animation of all 24 pages being drawn:


       <a href="http://eptcomic.com/videos/ept1.ogv">ept1.ogv</a> (7.5 MB ogg video)
        <a href="http://eptcomic.com/videos/ept1.webm">ept1.webm</a> (11 MB webm video)


      If the ogg video doesn't play in your browser, you can
      <a href="http://www.youtube.com/watch?v=WY9A2mug4dw">watch it on YouTube</a>
      or install an ogg-compatible video player like
      <a href="http://www.videolan.org/vlc/">VLC</a>.
