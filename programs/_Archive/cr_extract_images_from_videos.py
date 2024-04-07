from moviepy.editor import VideoFileClip
from pathlib import Path
import os

mids_dir = Path("D:\\MIDS-W207")
data = mids_dir/"MIDS-W207-Spring24-Soccer-Detection-Data"
project = mids_dir/"MIDS-W207-Spring24-Soccer-Detection-Data"
analysis = mids_dir/"analysis"

# Author: Timothy Majidzadeh
# Date Created: March 2, 2024
# Date Updated: March 2, 2024
# Description: Extract frame-by-frame image data from input videos.
# Notes: [v1] Created program.
# Inputs: Untouched video data.
# Outputs: Frame-by-frame image data.

def extract_frames(mp4, filename, output_folder):
	'''
	Save every frame of an mp4 file as an image.
	Inputs:
		mp4: The path to a .mp4 video file.
		filename: The name of the .mp4 file (without the extension)
			as a string.
		output_folder: The path of the desired output folder.
	Outputs:
		Each frame of the mp4 input saved as a .png file.
	'''
	if not os.path.exists(output_folder):
		print("Creating output folder {}...".format(output_folder))
		os.makedirs(output_folder)

	print("Loading video {}...".format(mp4.__str__()))
	clip = VideoFileClip(mp4.__str__(), audio = False)
	print("Loaded!")
	times = [i/clip.fps for i in range(int(clip.fps * clip.duration))]
	for t in times:
		frame_num = int(t * clip.fps) + 1 # 0-index is traditional, but the labels are 1-indexed.
		if frame_num % 30 == 0:
			print("Frame {}...".format(str(frame_num)))
		output_filepath = output_folder/'{}_{}.png'.format(filename, str(frame_num))
		clip.save_frame(output_filepath)
	print("All frames saved for video {}!".format(mp4.with_suffix("").__str__()))

# Iterate over every video type from our source data.
for type in ["top_view", "wide_view", "top_view_visualized", "wide_view_visualized"]:
	input_folder = data/"untouched/{}".format(type)
	for mp4 in os.listdir(input_folder):
		filename = mp4.replace(".mp4", "")
		output_folder = data/"base/{}/{}".format(type, filename)
		extract_frames(input_folder/mp4, filename, output_folder)