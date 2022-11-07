to run yolo on new images:

cd C:\Users\woprg\Desktop\CCIR\LearningML\TrainingYOLOv7_3\yolov5

python detect.py --source <path_to_folder_containing_images> --weights C:\Users\woprg\Desktop\CCIR\LearningML\TrainingYOLOv7_3\yolov5\runs\train\yolo_website6\weights\best.pt --conf 0.25 --name run_on_original_dataset_resized