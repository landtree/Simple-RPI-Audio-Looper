Installation

Replace the videos with your needed files. Make sure to follow the naming scheme, what ever video you want to play on a loop name it 'splash.mpv'

Copy the 'code' folder to /home/pi/ directory.

After the folder has been copied we must set it to auto start when the Pi boots.

sudo nano /etc/rc.local

and then replace the IP dummy script with

sudo python /home/pi/code/audio.py
