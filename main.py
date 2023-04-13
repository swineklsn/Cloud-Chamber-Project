from filter_frames import *
from video_tools import *

frames = read_frames_from_video('data/video.mp4')
filtered_frames = filter_frames(frames)
save_as_video(filtered_frames, 'data/filtered_video.mp4')
show_as_video(filtered_frames)
