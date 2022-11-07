# Website Element Detection
 A fitted YOLO v5 model for the detection of website elements within images of webpages.

# Setup
 Follow instructions for setting up YOLO v5 here: https://github.com/ultralytics/yolov5/
 Put the contents of the Stuff_to_put_in_yolov5_directory directory into the yolov5 directory

# To run YOLO on new images:
 cd Website-Element-Detection\yolov5

 python detect.py --source (path_to_folder_containing_images) --weights Website-Element-Detection\yolov5\runs\train\compiled_weights\weights\best.pt --conf 0.25 --name (the name given to the run)
 
# Tutorials Used
 https://blog.paperspace.com/train-yolov5-custom-data/
 https://towardsdatascience.com/yolo-v5-object-detection-tutorial-2e607b9013ef

# Dataset Used
 YOLOv5 Pytorch format
 https://public.roboflow.com/object-detection/website-screenshots/1