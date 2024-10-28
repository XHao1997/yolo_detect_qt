from roboflow import Roboflow


rf = Roboflow(api_key="jFmXIKys0UqwXbTlPmgC")
project = rf.workspace("pig-kft3y").project("traffic-disaster5")
version = project.version(5)
# dataset = version.download("yolov11")
project.version(5).deploy(model_type='yolov11', model_path=f'runs/detect5/train/')