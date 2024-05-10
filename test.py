import glfw
from openal import *
from helpers import load_wav_file, get_format

def init_sound():
    global device, context, buffer, source

    device = alcOpenDevice(None)
    context = alcCreateContext(device, None)
    alcMakeContextCurrent(context)

    buffer = ALuint()
    alGenBuffers(1, buffer)

    channels, bits, frequency, data = load_wav_file("test.wav")
    alBufferData(1, get_format(channels, bits), data.tobytes(), len(data.tobytes()), frequency)
    
    source = ALuint()
    alGenSources(1, source)

    alSourcei(source, AL_BUFFER, 1)
    alSourcePlay(source)

def free_sound():
    global device, context, buffer, source
    alSourceStop(source)
    alDeleteSources(1, source)
    alDeleteBuffers(1, buffer)

    alcMakeContextCurrent(None)
    alcDestroyContext(context)
    alcCloseDevice(device)

def sound_events():
    global device, context, buffer, source
    pass

def main():
    glfw.init()
    window = glfw.create_window(500, 500, "Programowanie multimedialne", None, None)
    glfw.make_context_current(window)
    
    init_sound()

    while not glfw.window_should_close(window):
        sound_events()
        glfw.poll_events()
    
    
    free_sound()
    glfw.destroy_window(window)
    glfw.terminate()

if __name__ == "__main__":
    main()
