import glfw
from openal import *
import math
from helpers import load_wav_file, get_format
import numpy as np


def init_sound():
	global device, context, buffer, source
	device = alcOpenDevice(None)
	context = alcCreateContext(device, None)
	alcMakeContextCurrent(context)
	buffer = ALuint()
	alGenBuffers(1, buffer)
	f = 261.6
	A = 32767
	fp = 44100
	op = 1 / fp
	lp = 10 * fp
	data = np.asarray([ signal(op*x, f, A) for x in range(lp) ], dtype=np.int16) # import numpy as np
	alBufferData(1, AL_FORMAT_MONO16, data.tobytes(), len(data.tobytes()), fp)
	source = ALuint()
	alGenSources(1, source)
	alSourcei(source, AL_BUFFER, 1)
	alSourcePlay(source)

def free_sound():
	global device, context, buffer, source
	

def sound_events():
	global device, context, buffer, source

def signal( t,  f,  A):
	return float(A * math.sin(2.0 * math.pi * f * t))

def key_callback(window, key, scancode, action, mods):
	state = ALint()
	global speed_y, speed_x, observer_eye, observer_front, observer_up, current_animation_speed
	if action == glfw.PRESS:
		if key == glfw.KEY_1:
			alGetSourcei(source, AL_SOURCE_STATE, state)
			if state.value == AL_PLAYING:
				print("ODTWARZANIE")
			if state.value == AL_PAUSED:
				print("ZAPAUZOWANE")
			if state.value == AL_STOPPED:
				print("ZATRZYMANE")
		

	

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
