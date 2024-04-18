# MIDS-W207-Spring24-Soccer-Detection
T. Majidzadeh and E. Ndedi's work on the MIDS w207 Project

# Follow the below steps to run!

1. Clone this repository inside of a folder YOUR-PATH-HERE on your machine. By default, we use the directory "D:\\MIDS-W207" or "c:/Desktop/MIDS-W207".

2. Within YOUR-PATH-HERE, or equivalent, clone the following repositories:
    a. yolov3 https://github.com/ultralytics/yolov3
    b. yolov5 https://github.com/ultralytics/yolov5
    c. yolov7 https://github.com/WongKinYiu/yolov7
    Other YOLO versions are implemented by importing the Ultralytics package into Python.

3. Copy the *contents* of the config folder in our repository (not the config folder itself) inside YOUR-PATH-HERE. These config files tell YOLO packages where to find our data and set values for certain image augmentations and hyperparameters. If you are prompted to replace existing files, accept.

4. Copy the datasets folder in this repository (*including* the datsets folder itself) inside YOUR-PATH-HERE.
    
5. The video and image data was too large for us to host on GitHub - you will need to download it. Go to the data source: https://www.kaggle.com/datasets/atomscott/soccertrack. Download the videos in top_view/videos and place them in YOUR-PATH-HERE/datasets/soccertrack/untouched/top_view. Download the videos in wide_view/videos and place them in YOUR-PATH-HERE/datasets/soccertrack/untouched/wide_view. Download the labels and place them in YOUR-PATH-HERE/datasets/soccertrack/untouched/top_view_labels and YOUR-PATH-HERE/datasets/soccertrack/untouched/wide_view_labels respectively. We provide one example of each image, video and label for reference. See our Works Cited.
    
6. Replace the paths in programs with your paths. Usually, this means replacing "D:\\MIDS-W207" or "c:/Desktop/MIDS-W207" with YOUR-PATH-HERE.

7. Download the necessary .pt files for YOLO: yolov3-tiny.pt, yolov5n.pt, yolov6n.pt, yolov7-tiny.pt, and yolov8n.pt.
    
7. Run the programs in the order indicated by the numbers. Programs with the same number can run in any order. Programs that rely on Tensorflow and Keras function best with Python 3.10, Tensorflow 2.15.0. Expect the process of extracting and saving images from videos, and cropping images to random squares, to take about 4-6 days of time and up to 700 GB of storage space.

# Works Cited
Uchida, I., et al. (2022) “SoccerTrack: A Dataset and Tracking Algorithm for Soccer with Fish-eye and Drone Videos,” (“SoccerTrack”), kaggle.com, available at https://www.kaggle.com/datasets/atomscott/soccertrack/data.

Redmon, J., et al. (2016). “You Only Look Once: Unified, Real-Time Object Detection,” (“YOLO Object Detection”), Proceedings of the IEEE conference on computer vision and pattern recognition.

Redmon, J., and Farhadi, A., (2018). “YOLOv3: An incremental improvement,” arXiv 1804.02767.

Jocher, G. (2020). YOLOv5 by Ultralytics (Version 7.0). https://doi.org/10.5281/zenodo.3908559.

Li, C., et al. (2023). YOLOv6 by Meituan Vision AI Department (Version 3.0), https://doi.org/10.48550/arXiv.2301.05586.

Wang, C., et al. (2022). “YOLOv7: Trainable bag-of-freebies sets new state-of-the-art for real-time object detectors.” arXiv 2207.02696.

Jocher, G., Chaurasia, A., & Qiu, J. (2023). Ultralytics YOLO (Version 8.0.0). https://github.com/ultralytics/ultralytics.

T. Majidzadeh and E. Ndedi, Project Proposal, “Detection of Ball and Player Location from Frame-by-Frame Soccer Match Videos,” MIDS W207 Spring 2024.

Homework Submissions of Etienne Ndedi, MIDS W207 Spring 2024.

Homework Submissions of Timothy Majidzadeh, MIDS W207 Spring 2024.

“How to Detect Small Objects: A Guide,” Jacob Solawetz, robloflow blog, available at https://blog.roboflow.com/detect-small-objects/.

“Imbalanced Data,” Machine Learning Foundational Courses, Google for Developers, available at developers.google.com/machine-learning/data-prep/construct/sampling-splitting/imbalanced-data.

“Model Training with Ultralytics YOLO,” Ultralytics, available at https://docs.ultralytics.com/modes/train/#augmentation-settings-and-hyperparameters.

“Tips for Best Training Results,” Glenn Jocher, docs.ultralytics.com, available at https://docs.ultralytics.com/yolov5/tutorials/tips_for_best_training_results/#training-settings.
