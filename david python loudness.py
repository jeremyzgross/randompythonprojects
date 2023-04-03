
#import library soundfile as a variable
import soundfile as sf
#importing library as a variable
import pyloudnorm as pyln
import os, shutil
#setting a field that points to ffmpeg (a library)
os.environ["IMAGEIO_FFMPEG_EXE"] = "/opt/homebrew/bin/ffmpeg"
#importing library as variable
import moviepy.editor as mp

BASE_PATH = '/Users/jeremyzgross/Downloads/BLACKSPOT QC/'

#converts video files to sound only files (mp3s)
def measure_loudness():

#for loop that loops through a directory in your OS. Replace the directory in the () to where your video files are located.
    for filename in os.listdir(BASE_PATH+'TEST VIDEOS'):
        if not filename.endswith(".mp4") and not filename.endswith(".mov"):
            continue

        print(filename) #prints which file is being processed

        #uses moviepy to load video file into 'clip' varaible. Replace the directory in the () to where your video files are locate bewtween f and {filename}. Make sure there is a / at the end of your directory
        clip = mp.VideoFileClip(f'/Users/jeremyzgross/Downloads/BLACKSPOT QC/TEST VIDEOS/{filename}')
        #removes extension from file name before converting
        noext = os.path.splitext(filename)[0]
        print(f'noext {noext}')
        print(f'writing file')
        #creates mp3 file. Replace the directory with where the converted video to audio file will be placed bewtween F and {noext}
        clip.audio.write_audiofile(f'/Users/jeremyzgross/Downloads/BLACKSPOT QC/EXPORTED MP3s/{noext}.mp3')

#for loop that measures loudness.  Replace the directory with where the converted video to audio file are placed
    badCounter = 0
    for filename in os.listdir(BASE_PATH+'/EXPORTED MP3s'):
        if not filename.endswith(".mp3"): #specifies that it is looking for mp3 files
            continue
        data, rate = sf.read(f'/Users/jeremyzgross/Downloads/BLACKSPOT QC/EXPORTED MP3s/{filename}')  # load audio (with shape (samples, channels)). Replace the directory in the () to where your audio files are located bewtween f and {filename}. Make sure there is a / at the end of your directory
        meter = pyln.Meter(rate)  # create BS.1770 meter
        loudness = meter.integrated_loudness(data)  # measure loudness
        sourceMp4Path = '/Users/jeremyzgross/Downloads/BLACKSPOT QC/TEST VIDEOS/'+filename+'.mp4'
        if loudness <= -22 and loudness >= -26:
            # move mp4 to a folder GOOD
            shutil.move(sourceMp4Path, BASE_PATH+'/GOOD VIDEOS')
        else:
            badCounter += 1
            # move mp4 to a folder BAD
            shutil.move(sourceMp4Path, BASE_PATH+'/BAD VIDEOS')
        # print(filename)
        # print('loudness')
        # print(loudness)
    print(badCounter+" BAD FILES")

# clears files in MP3 folder
    mp3Folder = BASE_PATH+'/EXPORTED MP3s'
    for filename in os.listdir(mp3Folder):
        file_path = os.path.join(mp3Folder, filename)
        try:
            # if the filename is a file, delete it
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            # # if the filename is a dir, delete the dir
            # elif os.path.isdir(file_path):
            #     shutil.rmtree(file_path)
        except Exception as e:
            print('Failed to delete %s. Reason: %s' % (file_path, e))


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    measure_loudness()




# loop through files
# if outside of thresh, move mp4 to a folder TOO_LOUD, else move to GOOD_VOLUME
# print out number of files that are too loud
# either way, delete mp3s


