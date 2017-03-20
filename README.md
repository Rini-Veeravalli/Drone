#Set-up Guide
Guide to setting up the Drone LiveStream
------

###Table of Contents

[Virtual Machine](#virtualmachine)	

[Using an Ubuntu VM](#usinganubuntuvm)	

[Motion Pre-requisites](#motionprerequisites)

[Package Installation](#packageinstallation)

[Motion Installation](#motioninstallation)

[Editing the Motion configuration file](#editingthemotionconfigurationfile)	

[Daemon](#daemon)  
[Basic Setup Mode](#basic)  
[Capture Device Options](#capture)  
[Motion Detection Settings](#motion)  
[Image File Output](#image)  
[FFMPEG related options](#ffmpeg)  
[Text Display](#text)  
[Target Directories and filenames For Images And Films](#target)  
[Live Stream Server](#live)    
[HTTP Based Control](#http)     
[Tracking(Pan/Tilt)](#tracking)  
[Thread config files](#thread)  

[Web Browser](#webbrowser)



----
<a name="virtualmachine"/>###Virtual Machine</a>


<a name="usinganubuntuvm"/>####Using an Ubuntu VM:</a> 

For testing on your own machine:  
Download VMware and Ubuntu ISO file/image (See Naim’s document for VMware installation).

Testing Purposes: Continue the rest of the set-up on the virtual machine.

Drone: The rest of the set-up should be run on the JETSON TK1.

----

<a name="motionprerequisites"/>###Motion Pre-requisites:</a> 

Needed are certain libraries from _glibc_, _libjpeg_, _zlib_, _ffmpeg_ and their development counterparts, GNU ‘make’ 3.79 or newer, GCC 4.7 or newer.  
_Perl5_ not needed, but can be used to test installation. 

| Libraries needed: |	Found in Debian Packages: |
| ------------------|--------------------------:|
| libm, libresolv, libdl, libpthread, libc, ld-linux, libcrypt, libnsl  |	libc6, libc6-dev, libglib1.2 |
| libjpeg	 | libjpeg62, libjpeg62-dev (optional libjpeg-mmx-dev) |
| libz |	zlib1g, zlib1g-dev |
| libavcodec, libavformat |	libavcodec-dev, libavcodec0d, libavformat-dev, libavformat0d, libav-tools |
											    	
<a name="packageinstallation"/>
####Package Installation:
</a> 

Can download these packages online, follow their installation guides, which usually require: `./configure; make; sudo make install`.

- For _lipjpeg_ – use `dos2unix` before configuring  
- For _glibc_ – needs binutils, texinfo, gawk, coreutils, make, sed, tar, gcc first. (May need to configure binutils with `CC=gcc ./configure`)

 

OR type in terminal (Recommended – faster and less fiddly):  
`sudo apt-get update`			get updates  
`apt-cache policy libc6`         	check what’s installed and what’s a candidate  
`sudo apt-get install libc6` 		install  
`apt-cache policy libc6` 		check again if it’s there
do for each package. 

One-line installation version:  
`sudo apt-get install libjpeg62 libjpeg62-dev libavformat libavcodec libav-tools libavutil-dev libc6 libc6-dev libglib1.2 zlib1g zlib1g-dev libmysqlclient-dev libpq-dev`


Useful commands:  
`apt list --installed` 			see list of all Deb packages you have  
`ldd --version`				see which version of GNU C library you have

----

<a name="motioninstallation"/>
###Motion Installation:
</a> 

Again, you can download source code, 

OR type in terminal (Recommended): `sudo apt-get install motion`  
This installs motion 3.2.12 as of Feb 2017.  
Run motion: `sudo motion`  
Test video stream on web browser, URL: `localhost:8081`  
Motion control panel, URL: `localhost:8080`  
Should display grey box with time/date and ‘UNABLE TO OPEN VIDEO DEVICE’  
Close motion in terminal: `CTRL+C`


In home directory, create .motion directory (hidden directory due to the ‘.’), copy motion’s default configuration file into it and change ownership to you.
```
~$ mkdir .motion
~$ sudo cp /etc/motion/motion.conf .motion/
~$ sudo chown root:root .motion/motion.conf
```


Make directory to store images from motion:
`~$ mkdir motion-images`

----

<a name="editingthemotionconfigurationfile"/>
###Editing the Motion configuration file:
</a>

Edit ~/.motion/motion.conf  (.conf file in the home directory):



<a name="daemon">
####Daemon
</a>

__`daemon on`__  daemon starts automatically



<a name="basic">
####Basic Setup Mode
</a>

`logfile /var/log/motion/motion.log` 	file to save log messages



<a name="capture">
####Capture device options
</a>

`videodevice /dev/video0`	videodevice to be used for capturing, /dev/video0 present when video camera is connected to the computer via USB.

`rotate 0`			if using a camera mount that rotates, rotate image this no. of degrees. Values: 0=no rotation, 90, 180, 270

__`width 752`__			defined by camera - image width (pixels)

__`height 480`__			“ 	“	“ 	- image height

`framerate 2` 	max. no. of frames captured per second, range: 2-100, depends on camera

`netcam_URL` *		URL if using a network camera

`netcam_userpass` * username and password for network camera, if required



<a name="motion">
####Motion Detection Settings
</a>

`threshold 1500`	no. of changed pixes in an image that triggers motion detection

`lightswitch 0`		ignore sudden massive light intensity changes given as a percentage of the picture area that changed intensity. Range: 0-100

`miniumum_motion_frames 1` the least no. of frames in a row that must contain motion before true motion is said to be detection Range:1-thousands

__`pre-capture 2`__		capture specific no. of frames before motion, that will output at motion detection. Don't use large values, else video frames will skip.  Range:0-5

__`post-capture 2`__		“	“	“     “   “ 	after motion. Use large values to smooth movies.



<a name="image">
####Image File Output
</a>

`output_pictures off` Output pictures when motion is detected. 'first'-first picture of event saved. 'best'-picture with most motion is saved. 'center'-picture with motion nearest centre is saved.

`quality 75` quality (in %) use by the jpeg compression

`picture_type jpeg` output images type. Values: jpeg, ppm



<a name="ffmpeg">
####FFMPEG related options
</a>

__`ffmpeg_output_movies on`__	ffmpeg encodes movies in realtime

__`ffmpeg_bps 500000`__ 		ffmpeg encoder's bitrate

__`ffmpeg_video_codec msmpeg4`__	ffmpeg's codec for video compression. msmpeg4 better than mpeg4 as it's compatible with Windows Media Player. Gives file with .avi extension



<a name="text">
####Text Display
</a>

__`text_right %d-%m-%Y\n%T-%q`__ 	swap day and year, to follow the UK format

`text_event` swap day and year again



<a name="target">
####Target Directories and filenames For Images And Films
</a>

__`target_dir /home/username/.motion/motion-images`__ *	current working directory - target directory for 
picture and movie files to be saved, better as an absolute path

__`snapshot_filename`__ file path for snapshots, swap day and year for UK format

__`picture_filename %v-%d%m%Y%H%M%S-%q`__ filepath for motion-triggered images, same change as above

__`movie_filename %v-%d%m%Y%H%M%S`__  change to UK format

__`timelapse_filename %d%m%Y-timelapse`__ 	change to UK format



<a name="live">
####Live Stream Server
</a>

`stream quality 50` 	quality (in %) of jpeg images produced

__`stream_localhost off`__  Restricts stream connections to localhost only when 'on'. We want to be able to view the stream from other clients.



<a name="http">
####HTTP Based Control
</a>

__webcontrol_localhost off__  Restricts control connects to local host only when 'on'



<a name="tracking">
####Tracking(Pan/Tilt)
</a>

See .config file for options

------

Do we want to log to the database when creating motion-triggered picture/snapshot image/motion-triggered movie/timelapse movie files?


------
<a name="thread">
####Thread config files
</a>

One for each camera, with configurations for each. With one camera, need only the .config file. With two cameras, need the .config file and a thread file for each camera.



___

Create directory to store PID file (motion.conf tells you to do this): 
`sudo mkdir /var/run/motion`

___

When this is all working, do:  
`sudo nano /etc/default/motion`  
and change: `start_motion_daemon = yes`


Run again: `sudo motion`  
Test on web browser, URL: `localhost:8081`  
Video stream should appear

----


<a name="webbrowser">
###Web Browser
</a>

How to access the video stream via a html file.  

Save the _index.html_ inside the _.motion_ directory.
Then, run `python -m SimpleHTTPServer` in the terminal.  

In your web browser (Firefox OR Chrome), type the URL: `drones_ip_address:8000` 
SimpleHTTPServer gives you the port `8000` - you can define this yourself with:  
`python -m SimpleHTTPServer xxxx` in terminal, e.g. xxxx = 9000  


The index.html file embeds `drones_ip_address:8081` - which is the drones video livestream, within the .html file. The .html file is then served via python's SimpleHTTPServer.  

`ifconfig` in terminal gives the ip address of your machine


Installing NGinx 
`sudo apt-get update`
