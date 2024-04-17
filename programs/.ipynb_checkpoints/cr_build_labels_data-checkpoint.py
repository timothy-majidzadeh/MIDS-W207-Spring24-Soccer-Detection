from pathlib import Path
import os
import numpy as np
import pandas as pd
import random 

mids_dir = Path("D:\\MIDS-W207")
data = mids_dir/"datasets/soccertrack"
project = mids_dir/"MIDS-W207-Spring24-Soccer-Detection"
analysis = project/"analysis"

# Author: Timothy Majidzadeh
# Date Created: March 4, 2024
# Date Updated: March 12, 2024
# Description: Develop the label import script.
# Notes: [v1] Created program.
# Inputs: Data label CSV files.
# Outputs: Stacked & reshaped CSV file.

all_saved_images = [f for root,dirs,files in os.walk(data/"images/top_view") for f in files] + [f for root,dirs,files in os.walk(data/"images/wide_view") for f in files]

def load_and_label(dir, vidname, view_type):
	"""
	Loads the CSV file at path, returning it as a dataframe with the sourcefile as a column.
	Inputs:
		A path to a CSV with the bounding boxes for images.
	Outputs:
		A Pandas DataFrame with the loaded & cleaned CSV.
	"""
	raw = pd.read_csv(dir/vidname, header=[0, 1, 2])[1:].reset_index()
	raw.rename(columns={"index": "frame", "0" : "team_0", "1" : "team_1", "BALL": "ball"}, level=0, inplace=True)
	raw.rename(columns={
		"0" : "player_00",
		"1" : "player_01",
		"2" : "player_02",
		"3" : "player_03",
		"4" : "player_04",
		"5" : "player_05",
		"6" : "player_06",
		"7" : "player_07",
		"8" : "player_08",
		"9" : "player_09",
		"10" : "player_10",
		"11" : "player_11",
		"BALL" : "ball"
	}, level=1, inplace=True)
	raw.drop(columns="TeamID", inplace=True, level=0)
	raw['vidname'] = vidname.replace(".csv", "")
	raw['frame_imgname'] = raw.vidname.str.cat("_"+raw['frame'].astype(str)+".png")
	raw['frame_imgpath'] = str(data)+"/images/{}/".format(view_type)+raw['vidname']+"/"+raw['frame_imgname']
	raw['frame_saved'] = [frame in all_saved_images for frame in raw['frame_imgname']]

	raw.set_index(["vidname", "frame", "frame_imgname", "frame_imgpath"], inplace=True)
	raw.reset_index(inplace=True)
	return raw

top_view_input = data/"untouched/top_view_labels"
top_view_output = data/"labels/top_view_labels_stacked"
wide_view_input = data/"untouched/wide_view_labels"
wide_view_output = data/"labels/wide_view_labels_stacked"

top_view_labels = pd.concat([load_and_label(top_view_input, vidname, 'top_view') for vidname in os.listdir(top_view_input)])
top_view_labels.to_csv(top_view_output/"top_view_labels.csv")
top_view_labels.to_pickle(top_view_output/"top_view_labels.pkl")

wide_view_labels = pd.concat([load_and_label(wide_view_input, vidname, 'wide_view') for vidname in os.listdir(wide_view_input)])
wide_view_labels.to_csv(wide_view_output/"wide_view_labels.csv")
wide_view_labels.to_pickle(wide_view_output/"wide_view_labels.pkl")

stacked_labels = pd.concat([top_view_labels, wide_view_labels])
stacked_labels.to_csv(data/"labels/stacked_labels.csv")
stacked_labels.to_pickle(data/"labels/stacked_labels.pkl")