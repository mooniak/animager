Animager
=======

##A tool to easily animate your graphic design or illustration project.

Save and git commit step by step, your graphic design process and use Animager to build a video to show the progress.
Animager users Git - a version control system to record and grab all the stages of your design project. Use [Sparkleshare](http://sparkleshare.org/) to easily commit file. What Animager does is rolling the git commits and capture the image for each commit as a temporary image, collect all temporary images and build a video.


###Supported image formats and OS's

Animager uses imagemagick to convert the images. Supported image format list is [here.](http://www.imagemagick.org/script/formats.php) 

Tested on Linux only.

###Dependencies
  - ffmpeg
  - imagemagick
  - python3
  - C++ compiler - g++


###Install Animager

- Download the `zip` file. 
- Open Terminal and do:
```
cd src
```

```
sh install.sh
```

Now Animager is installed.

###Setup with Git and/or Sparkleshare

We suggest you use Sparklshare to make the git commits to get a really nice staep by step video. Using Sparkleshare will allow Animager to get all the saved stages of your file into video. Otherwise you can do `git commit` once a while to get the needed stages.

- Install [Sparkleshare](http://sparkleshare.org/)
- Set Up a Git repo in a remote service. If it is a public project you can use GitHub. BitBucket let youhave free private repos.
- Set up the repo in Sparkleshare
- Save your file in any of the supported formats and start working. Save once in a while as you would normally do. 



###How to use animager

Once you are done and want to generate a video..

```
animager -p profileName -i [path-to-your-image] -o [path-to-your-output-folder]
```

Example: `animager -p hd-720p -i /home/lahiru/sparkleshare/test/drawing.svg -o /home/lahiru/desktop`

If you don't mention `-o [path-to-your-output-folder]`, video will be saved as `~/animager/out.mp4`

Included profiles : `hd-720p` `hd-1080p` `sd-360` `sd-480`


###Other options

- Get a list of profiles
`animager -plist all`

- Create a new profile
`animager -pnew profileName -h height -w weight -f frameRate`

Example: `animager -pnew test -h 240 -w 320 -f 30`


###ToDo
- See [Issues](https://github.com/mooniak/animager/issues) for future development plans. 


###Credits
- Lahiru Pathirage (lpsandaruwan)
- Pathum Egodawatta (pathumego)

###License

Animager is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License version 2 of the License, or (at your option) any later version.  You are welcome to change and redistribute it under certain conditions. For more information see the license file.
