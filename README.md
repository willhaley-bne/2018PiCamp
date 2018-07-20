# 2018 Pi Camp

These are some simple scripts that I wrote for a Raspberry Pi Summer Camp to be used with the [Google's AIY Google Voice Kit](https://aiyprojects.withgoogle.com/voice/).  

Inspired by [Simone Giertz](www.simonegiertz.com), I decided to make the scripts as dumb and useless as possible.  
It will sort of be the theme of the camp: lets see if we can figure out the dumbest things we can make the
device do.

### Pre-reqs:
Below are a list of packages you'll need to add to the pi ( via apt-get ) so everything will work.  I hope this is a 
complete list, but there maybe something I missed.
* mpg321 (to play the mp3's)
* python-alsaaudio (to let python monkey with the volume)


### Startup-x scripts:
I wanted to make sure that the students in the summer camps didn't have to have the AIY app to know what the IP 
address of the Pi after initial set up.   Therefore, I made a couple of startup scripts that either slacked 
or said the IP of the device at boot up. 

To get the script to always run after boot I added the following to the root crontab.

 ``` 
 @reboot python3 /home/pi/startup.py
 ```
 You will need to change the path of the script to match where you put your start up.  
 
 Below is the list of scripts and a brief description:
 * startup-slack.py - sends a slack message that includes the name of the device and the IP address
 * startup-voice.py - speaks the IP address 
 * one/muppets_are_still_cool.py - press button play one of 20 random muppet mp3's. 
 * one/press_button_challenge.py - taunts you to press the button until it gets tired of you pressing the
 button.
 * two/bleep.py - adds a bleep sound effect in a sentence you say to it
 * two/schm.py - you tell it a word and it repeats that word to you plus the word with "schm" added to the 
 front
 * two/translator.py - it doesn't actually do any translating, it just repeats what you just said slower
 and louder back to you.  
 
 I'm working to add more scripts and to document the code before the camp in July.