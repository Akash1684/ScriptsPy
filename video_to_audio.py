
import time
import os
import pipes

def video_to_audio(fileName):

	try:
		file,file_extension=os.path.splitext(fileName)
		file=pipes.quote(file)
		video_to_wav = 'ffmpeg -i '+file+file_extension+' '+file+'.wav'
		final_audio ='lame '+file+'.wav'+' '+file+'.mp3'
		os.system(video_to_wav)
		os.system(final_audio)
		print("sucessfully converted ",fileName, " into audio!")
	except OSError as err:
		print(err.reason)
		exit(1)



def main():

	   filePath="################################################"

	   # convert video to audio
	   video_to_audio(filePath)
	   time.sleep(1)

# install ffmpeg and/or lame if you get an error saying that the program is currently not installed

if __name__ == '__main__':
	main()
