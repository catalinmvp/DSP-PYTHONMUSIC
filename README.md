# DSP-PYTHONMUSIC
For this project I m combining the principels of speech recognition ploting in order to search on youtube for a song , download it, transform it into a wav file and plot 
its waveform.
In order to do that, i ve used multiple libraries such as:webbrowser , pafy , wave, moviepy.audio.

Projoect execution step by step:

1. The computer will listen and recognize what i have saind in the microphone. With what i ve said he will take youtube link(can be google too), combine them and search for that url (line 26)
2. Once opened , in the terminal you will be asked to copy the link of a video from the new page opened and paste it in the terminal.
3. Once he get the link he will download in a given folder the video in a WEBM file(this file will have to be converted to mp4 manually).
4. With the new wav file, he will extract the frames from the wav file and plot it.

Conclusion: Basically i ve tried to make an assistant who can download a song from youtube and plot its waveform. I will leave a video to demonstrate its usage to avoid a lot of pip installations.
