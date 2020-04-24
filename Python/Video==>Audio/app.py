import moviepy.editor

video=moviepy.editor.VideoFileClip('input.mp4')

audio=video.audio

audio.write_audiofile('output.mp3')