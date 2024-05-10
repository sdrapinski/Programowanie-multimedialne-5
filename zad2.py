import glfw
from openal import *
from helpers import load_wav_file, get_format

def init_sound():
	global device, context, buffer, source

def free_sound():
	global device, context, buffer, source
	

def sound_events():
	global device, context, buffer, source
	

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
