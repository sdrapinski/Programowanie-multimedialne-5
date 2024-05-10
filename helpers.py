from openal import *
import numpy as np
import wave

def load_wav_file(filename):
    with wave.open(filename, 'rb') as wav:
        channels = wav.getnchannels()
        bitrate = wav.getsampwidth() * 8
        frequency = wav.getframerate()
        frames = wav.readframes(wav.getnframes())
        data = np.frombuffer(frames, dtype=np.int16 if bitrate == 16 else np.int8)
    return channels, bitrate, frequency, data

def get_format(channels, bits):
    if channels == 1:
        return AL_FORMAT_MONO16 if bits == 16 else AL_FORMAT_MONO8
    elif channels == 2:
        return AL_FORMAT_STEREO16 if bits == 16 else AL_FORMAT_STEREO8
    else:
        raise ValueError("Unsupported audio format")

