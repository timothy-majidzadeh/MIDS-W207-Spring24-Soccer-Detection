# MIDS-W207-Spring24-Soccer-Detection
T. Majidzadeh and E. Ndedi's work on the MIDS w207 Project

# Follow the below steps to run!

1. Clone this repository inside of a folder <YOUR-PATH-HERE> on your machine. By default, we use the directory "D:\\MIDS-W207" or "c:/Desktop/MIDS-W207".

2. Within <YOUR-PATH-HERE>, or equivalent, clone the following repositories:
    a. yolov3 https://github.com/ultralytics/yolov3
    b. yolov5 https://github.com/ultralytics/yolov5
    c. yolov7 https://github.com/WongKinYiu/yolov7
    Other YOLO versions are implemented by importing the Ultralytics package into Python.

3. Copy the *contents* of the config folder in our repository (not the config folder itself) inside <YOUR-PATH-HERE>. These config files tell YOLO packages where to find our data and set values for certain image augmentations and hyperparameters. If you are prompted to replace existing files, accept.

4. Copy the datasets folder in this repository (*including* the datsets folder itself) inside <YOUR-PATH-HERE>.
    
5. The video and image data was too large for us to host on GitHub - you will need to download it. Go to the data source: https://www.kaggle.com/datasets/atomscott/soccertrack. Download the videos in top_view/videos and place them in <YOUR-PATH-HERE>/datasets/soccertrack/untouched/top_view. Download the videos in wide_view/videos and place them in <YOUR-PATH-HERE>/datasets/soccertrack/untouched/wide_view. We have already included the untouched labels data in the datasets folder which you copied in Step 4, but you can also find them at the data source.
    
6. Replace the paths in programs with your paths. Usually, this means replacing "D:\\MIDS-W207" or "c:/Desktop/MIDS-W207" with <YOUR-PATH-HERE>.
    
7. Run the programs in the order indicated by the numbers. Programs with the same number can run in any order. Programs that rely on Tensorflow and Keras function best with Python 3.10, Tensorflow 2.15.0. Expect the process of extracting and saving images from videos, and cropping images to random squares, to take about 4-6 days of time and up to 700 GB of storage space.