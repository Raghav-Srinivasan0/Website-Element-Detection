import numpy as np
import cv2
from mss import mss
from PIL import Image
import torch

# Screen capture
sct = mss()

# Model
model = torch.hub.load('ultralytics/yolov5', 'custom', path=r'C:\Users\woprg\Desktop\CCIR\LearningML\TrainingYOLOv7_3\yolov5\runs\train\yolo_website6\weights\best.pt')  # local custom model

while 1:
    #set the capture size
    w, h = 800, 640
    #set the capture position
    monitor = {'top': 0, 'left': 0, 'width': w, 'height': h}
    img = Image.frombytes('RGB', (w,h), sct.grab(monitor).rgb)
    screen = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)
    #set the model use the screen 
    result = model(screen)
    result.display(render=True) 
    
    #show the result
    cv2.imshow('Screen', result.ims[0])
    #print(result.xyxy[0])

    if cv2.waitKey(25) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break