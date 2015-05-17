### make folders

mkdir -p /home/$USER/animager
###mkdir -p /home/$USER/animager/morph-cache
mkdir -p /home/$USER/animager/profiles

### install profiles
cp -fRr profiles/*.prof /home/$USER/animager/profiles

### install python scripts

sudo mkdir -p /opt/animager
sudo cp -fRr *.py /opt/animager

### build command line tool and install

g++ cmd.cpp -o animager
sudo cp -fR animager /usr/bin/