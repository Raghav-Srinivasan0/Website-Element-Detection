# Website Element Detection
 A fitted YOLO v5 model for the detection of website elements within images of webpages.

# To run YOLO on new images:
 cd Website-Element-Detection\yolov5

 python detect.py --source (path_to_folder_containing_images) --weights Website-Element-Detection\yolov5\runs\train\compiled_weights\weights\best.pt --conf 0.25 --name (the name given to the run)