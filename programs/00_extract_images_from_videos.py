from moviepy.editor import VideoFileClip
from pathlib import Path
from PIL import Image
import os

mids_dir = Path("D:\\MIDS-W207")
data = mids_dir/"datasets/soccertrack"
project = mids_dir/"MIDS-W207-Spring24-Soccer-Detection-Data"
analysis = mids_dir/"analysis"

# Author: Timothy Majidzadeh
# Date Created: March 2, 2024
# Date Updated: April 6, 2024
# Description: Extract frame-by-frame image data from input videos.
# Notes: [v1] Created program.
#		 [v2, v3] Fixed errors. Used ChatGPT to optimize and reduce runtime
# from approximately 17 days to 2.5 days.
# Inputs: Untouched video data.
# Outputs: Frame-by-frame image data.

def extract_frames(mp4_path, filename, output_folder):
    '''
    Save every frame of an mp4 file as an image.
    Inputs:
        mp4_path: The path to a .mp4 video file.
        filename: The name of the .mp4 file (without the extension)
            as a string.
        output_folder: The path of the desired output folder.
    Outputs:
        Each frame of the mp4 input saved as a .png file.
    '''
    output_folder = Path(output_folder)
    output_folder.mkdir(parents=True, exist_ok=True)

    print(f"Loading video {mp4_path}...")
    clip = VideoFileClip(str(mp4_path), audio=False)
    print("Loaded!")

    frame_rate = clip.fps
    total_frames = int(clip.duration * frame_rate)

    for i, frame in enumerate(clip.iter_frames()):
        if i % 30 == 0:
            print(f"Frame {i + 1}...")
        
        # Convert numpy array to PIL Image
        pil_frame = Image.fromarray(frame)

        output_filepath = output_folder / f"{filename}_{i + 1}.png"
        pil_frame.save(output_filepath)

    print(f"All frames saved for video {mp4_path.with_suffix('')}!")

# Iterate over every video type from our source data.
for type in ["top_view", "wide_view"]:
	input_folder = data/"untouched/{}".format(type)
	for mp4 in os.listdir(input_folder):
		
		filename = mp4.replace(".mp4", "")
		output_folder = data/"images/{}/{}".format(type, filename)
		extract_frames(input_folder/mp4, filename, output_folder)