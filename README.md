[![Build Status](https://travis-ci.com/PythonSerious/speakerapi.svg?branch=main)](https://travis-ci.com/PythonSerious/speakerapi)


# speakerapi
manage your speakers from your PC with your RPI


##
Requirements:
- PC: Python added to path, FFMPEG added to path, flask installed (pip install flask) < if not installed


- RPI: python installed, ffmpeg installed, flask installed.

### Local PC instructions
first of all this isnt really meant for PC, its meant for RPI.
go into app.py and replace IPHERE with 127.0.0.1 (ctrl + f for IPHERE) in app.py 
(port 5000)

### RPI instructions
go into app.py and replace IPHERE (ctrl + f for IPHERE) with your RPI's locak network address.
(port 2000)

#### Notes:
The tempstorage folder is where the audio files are temp stored. add that to the directory where your app.py file will run.
