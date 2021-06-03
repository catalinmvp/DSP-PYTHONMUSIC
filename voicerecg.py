import webbrowser
from moviepy.audio.io.AudioFileClip import AudioFileClip
import speech_recognition as sp 
import pafy 
import wave
import numpy as np
import matplotlib.pyplot as plt
#pip install youtube_dl
#pip install pafy
#pip install moviepy
#pip install SpeechRecognition


def main():
    input = sp.Recognizer()

    with sp.Microphone() as source:
        input.adjust_for_ambient_noise(source)
        print("Say something")

        ad = input.listen(source)

        try:
            print("We will search on google or youtube " + input.recognize_google(ad))
            command = input.recognize_google(ad)
            webbrowser.open('https://www.youtube.com/results?search_query=' + command)
            

            
        except Exception as e:
            print(str(e))    


if __name__ == "__main__":
    main()
    print("Copy the link of one of the videos and paste it: ")
    #downloading stage
    folder = 'D:/all/sem 2/dsp proj'
    url = str(input())
    video = pafy.new(url)

    audio = video.audiostreams

    for i in audio:
        print('bitrate: %s, ext: %s, size: %0.2fMb' % (i.bitrate, i.extension,i.get_filesize()/1024/1024))

    #conversion from mp4 to wav
    audio[1].download(filepath = folder)
    video = AudioFileClip('Pitbull - Timber ft. Ke$ha.mp4')
    video.write_audiofile('song.wav')
    name = 'song.wav'
    video.close()

    #plot of wav file

    wav = wave.open("song.wav","r") #reand only mode

    raw = wav.readframes(-1)  #extract audio from wav file returning the frames
    raw = np.frombuffer(raw, "Int16") #converting to an array 16bits per sample
    sampleRate = wav.getframerate()

    time  = np.linspace(0,len(raw)/sampleRate,num = len(raw))

    plt.title('Waveform of song')
    plt.plot(time,raw,color = "blue")
    plt.ylabel("Amplitude")
    plt.xlabel("Time in seconds")
    plt.show()

