import matplotlib.pyplot as plt
import numpy as np
import wave
import os
import math
import contextlib
from scipy.io import wavfile
import librosa
import librosa.display
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from pydub.silence import detect_nonsilent
from pydub import AudioSegment
from keras.models import load_model
from keras_preprocessing import image
from keras.applications.vgg16 import preprocess_input
import numpy as np


global model
model = load_model('covid.h5')

cutOffFrequency = 200.0

def WavToSpec(audiofile,output):
    print('Spectogram based on>>>>',audiofile)
    aud,Fs=librosa.load(audiofile)#,offset=0,duration=5.0)
    aud = np.array(aud)
    S = librosa.stft(aud)
    duration=librosa.get_duration(S=S, sr=Fs)
    first=aud
    first=np.array(first)
    first = first.astype('float64')
    window_size = 1024
    window = np.hanning(window_size)
    stft  = librosa.core.spectrum.stft(first, n_fft=window_size, hop_length=512, window=window)
    out = 2 * np.abs(stft) / np.sum(window)
    fig = plt.Figure()
    canvas = FigureCanvas(fig)
    ax = fig.add_subplot(111)
    p = librosa.display.specshow(librosa.amplitude_to_db(out, ref=np.max), ax=ax, y_axis='log', x_axis='time')
    ax.axis('off')
    fig.savefig(output,bbox_inches='tight', pad_inches=0)
    #fig.savefig(output)


def running_mean(x, windowSize):
  cumsum = np.cumsum(np.insert(x, 0, 0)) 
  return (cumsum[windowSize:] - cumsum[:-windowSize]) / windowSize

def interpret_wav(raw_bytes, n_frames, n_channels, sample_width, interleaved = True):

    if sample_width == 1:
        dtype = np.uint8 # unsigned char
    elif sample_width == 2:
        dtype = np.int16 # signed 2-byte short
    else:
        raise ValueError("Only supports 8 and 16 bit audio formats.")

    channels = np.fromstring(raw_bytes, dtype=dtype)

    if interleaved:
        # channels are interleaved, i.e. sample N of channel M follows sample N of channel M-1 in raw data
        channels.shape = (n_frames, n_channels)
        channels = channels.T
    else:
        # channels are not interleaved. All samples from channel M occur before all samples from channel M-1
        channels.shape = (n_channels, n_frames)

    return channels


def remove_sil(path_in, path_out, format="wav",sensitivity = 43):
    print('File without silence:>>>>',path_out)
    sound = AudioSegment.from_file(path_in, format=format)
    non_sil_times = detect_nonsilent(sound, min_silence_len=5, silence_thresh=sound.dBFS * 1.5)
    if len(non_sil_times) > 0:
        non_sil_times_concat = [non_sil_times[0]]
        if len(non_sil_times) > 1:
            for t in non_sil_times[1:]:
                if t[0] - non_sil_times_concat[-1][-1] < sensitivity :
                    non_sil_times_concat[-1][-1] = t[1]
                else:
                    non_sil_times_concat.append(t)
        non_sil_times = [t for t in non_sil_times_concat if t[1] - t[0] > 350]
        if  non_sil_times:
            First = sound[non_sil_times[0][0]: non_sil_times[-1][1]]
        else:
            First = sound
        sound = First.reverse()
        non_sil_times = detect_nonsilent(sound, min_silence_len=5, silence_thresh=sound.dBFS * 1.5)
        if len(non_sil_times) > 0:
            non_sil_times_concat = [non_sil_times[0]]
            if len(non_sil_times) > 1:
                for t in non_sil_times[1:]:
                    if t[0] - non_sil_times_concat[-1][-1] < sensitivity:
                        non_sil_times_concat[-1][-1] = t[1]
                    else:
                        non_sil_times_concat.append(t)
            non_sil_times = [t for t in non_sil_times_concat if t[1] - t[0] > 350]
            if  non_sil_times:
                First = sound[non_sil_times[0][0]: non_sil_times[-1][1]]
            else:
                First = sound
        

        #First-=6
        First.export(path_out, format='wav')

def Filter(fname,outname,finalname,output):
    with contextlib.closing(wave.open(fname,'rb')) as spf:
        sampleRate = spf.getframerate()
        ampWidth = spf.getsampwidth()
        nChannels = spf.getnchannels()
        nFrames = spf.getnframes()

        # Extract Raw Audio from multi-channel Wav File
        signal = spf.readframes(nFrames*nChannels)
        spf.close()
        channels = interpret_wav(signal, nFrames, nChannels, ampWidth, True)

        # get window size
        freqRatio = (cutOffFrequency/sampleRate)
        N = int(math.sqrt(0.196196 + freqRatio**2)/freqRatio)

        # Use moviung average (only on first channel)
        filtered = running_mean(channels[0], N).astype(channels.dtype)


    #finalname = outname
    print('File After Filter:>>>>',outname)

    wav_file = wave.open(outname, "w")
    wav_file.setparams((1, ampWidth, sampleRate, nFrames, spf.getcomptype(), spf.getcompname()))
    wav_file.writeframes(filtered.tobytes('C'))
    wav_file.close()

    remove_sil(fname,finalname,'wav')
    print('Filtering done')
    WavToSpec(finalname,output)

def Predict(path):
    img = image.load_img(path, target_size=(150, 150))
    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0)
    img_data = preprocess_input(x)
    classes = model.predict(img_data)
    return classes[0][0]


def main():
    #Voice('test.wav')
    Filter('test.wav','Filtered.wav','out.wav','out.png')
    from PIL import Image
    os.remove('test.wav')
    os.remove('Filtered.wav')
    os.remove('out.wav')
    with Image.open("out.png") as im:

        im_resized = im.resize((334,216))
    im_resized.save('out.png',"PNG")
    x = Predict('out.png')

    if x==0:
        return('negative')
    else:
        return('positive')
    