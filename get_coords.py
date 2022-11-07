import numpy as np
import cv2
import torch
from os import listdir
from os.path import isfile, join

class Data:
    def __init__(self, directory="small_test/", pt=r'C:\Users\woprg\Desktop\CCIR\LearningML\TrainingYOLOv7_3\yolov5\runs\train\yolo_website6\weights\best.pt', show_img=False, shuffle=False):
        onlyfiles = [f for f in listdir(directory) if isfile(join(directory, f))]

        self.directory2 = directory

        for i in range(len(onlyfiles)):
            onlyfiles[i] = self.directory2 + onlyfiles[i]

        self.file_paths = onlyfiles

        #print(onlyfiles)

        # Model
        model = torch.hub.load('ultralytics/yolov5', 'custom', path=pt,force_reload=True)  # local custom model

        self.data = {}

        for file in onlyfiles:
            img = cv2.imread(file)
            screen = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)
            #set the model use the screen 
            result = model(screen)
            #result.display(render=True) 

            #show the result
            if show_img:
                cv2.imshow('Screen', result.ims[0])

            temp = result.xyxy[0]

            self.data[file.replace(str(directory),str(""))[:file.replace(str(directory),str("")).index(".")]] = temp

            if show_img:
                while True:
                    if cv2.waitKey(25) & 0xFF == ord('q'):
                        cv2.destroyAllWindows()
                        break
        if shuffle:
            import random
            keys = list(self.data.keys())
            random.shuffle(keys)

            shuffled_temp = dict()
            for key in keys:
                shuffled_temp.update({key: self.data[key]})

            self.data = shuffled_temp
    def raw_data(self):
        return self.data

    def images(self):
        return self.file_paths

    def data_from_img(self, img):
        return self.data[img]

    def raw_data_list(self):
        return list(self.data.values())
    
    def filter_confidence(self, minimum=0.5, maximum=1, img=None):
        temp = {}
        if img == None:
            for key, value in self.data.items():
                new_value = []
                for item in list(value):
                    if item[4] >= minimum and item[4] <= maximum:
                        new_value.append(item)
                temp[key] = new_value
        else:
            for key, value in self.data_from_img(img):
                new_value = []
                for item in list(value):
                    if item[4] >= minimum and item[4] <= maximum:
                        new_value.append(item)
                temp[key] = new_value
        return temp

if __name__ == "__main__":
    d = Data(show_img=True)
    print(d.images())