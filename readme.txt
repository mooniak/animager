### how to install

cd into src and,
sh install.sh

### create a video
animager -p [profile name] -i [filepath/name] -o [output folder]
{ ex :  animager -p hd-720p -i /home/lahiru/sparkleshare/test/drawing.svg -o /home/lahiru/desktop }
if you didnt mention -o (output folder) here, video will be saved as ~/animager/out.mp4

### to get a available profile list
animager -plist all

### to create a profile
animager -pnew [pname] -h [height] -w [width] -f [frame rate]
{ ex : animager -pnew test -h 240 -w 320 -f 30 }