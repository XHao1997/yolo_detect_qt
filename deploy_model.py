from roboflow import Roboflow


rf = Roboflow(api_key="tZOwB39itZ7xS7VZVoPv")
project = rf.workspace("yolodetect-pa1yv").project("yolo_detect-kkaki-evsav")
version = project.version(1)
                
version.deploy("yolov11", ".", "best_v11s2.pt")