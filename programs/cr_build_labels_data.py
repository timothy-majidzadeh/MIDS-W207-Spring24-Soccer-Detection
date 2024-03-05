from pathlib import Path
import os
import numpy as np
import pandas as pd
import random 

mids_dir = Path("D:\\MIDS-W207")
data = mids_dir/"MIDS-W207-Spring24-Soccer-Detection-Data"
project = mids_dir/"MIDS-W207-Spring24-Soccer-Detection"
analysis = project/"analysis"

# Author: Timothy Majidzadeh
# Date Created: March 4, 2024
# Date Updated: March 4, 2024
# Description: Develop the label import script.
# Notes: [v1] Created program.
# Inputs: Data label CSV files.
# Outputs: Stacked & reshaped CSV file.

def load_and_label(dir, filename):
	"""
	Loads the CSV file at path, returning it as a dataframe with the sourcefile as a column.
	Inputs:
		A path to a CSV with the bounding boxes for images.
	Outputs:
		A Pandas DataFrame with the loaded & cleaned CSV.
	"""
	raw = pd.read_csv(dir/filename, header=[0, 1, 2])[1:].reset_index()
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
	raw['filename'] = filename.replace(".csv", "")
	raw.set_index(["filename", "frame"], inplace=True)
	return raw

top_view_input = data/"untouched/top_view_labels"
top_view_output = data/"base/top_view_labels"
wide_view_input = data/"untouched/wide_view_labels"
wide_view_output = data/"base/wide_view_labels"

stacked_data = pd.concat([load_and_label(top_view_input, filename) for filename in os.listdir(top_view_input)])
stacked_data.to_csv(top_view_output/"top_view_labels.csv")
stacked_data.to_pickle(top_view_output/"top_view_labels.pkl")

stacked_data = pd.concat([load_and_label(wide_view_input, filename) for filename in os.listdir(wide_view_input)])
stacked_data.to_csv(wide_view_output/"wide_view_labels.csv")
stacked_data.to_pickle(wide_view_output/"wide_view_labels.pkl")