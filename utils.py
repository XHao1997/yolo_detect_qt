import numpy as np
import cv2
from ultralytics import YOLO
from collections import defaultdict

def store_track_info(track_ids, classes, track_history=defaultdict(lambda: [])):
    result = np.vstack((track_ids, classes))
    for track_id, cls in zip(track_ids,classes):
        track = track_history[track_id,int(cls)]
        track.append(track_id)
    return result, track_history
                    

def count_from_track_history(track_history, is_video=False):
    # Count occurrences for each class (using just the first element as the "class")
    class_counts = defaultdict(int)

    for key, values in track_history.items():
        # Get the class identifier
        class_id = key[1]
        # For video, check if there are at least 2 values before counting
        if is_video and len(values) < 2:
            continue
        else:
            # Add the count of values for this class
            class_counts[class_id] += 1
    return dict(class_counts)

def remap_dictionary(old_dict):
    # Define the mapping from numbers to words
    number_to_word = {0: 'fallen tree', 1: 'landslide', 2: 'road collapse', 3: 'stone'}
    # Initialize the remapped dictionary with all keys set to 0
    remapped_number_dict = {word: 0 for word in number_to_word.values()}

    # Update the dictionary with values from the old dictionary
    for key, value in old_dict.items():
        word = number_to_word.get(key, None)
        if word:  # Only update if the word exists in the mapping
            remapped_number_dict[word] = value

    print("Remapped dictionary:", remapped_number_dict)
    return remapped_number_dict

def count_yolo_pred(result):
    cls = result[0].boxes.cls
    cls_name = np.unique(cls)
    cls_num = np.unique(cls, return_counts=True)[1]
    count_result = {}
    for i,j in zip(cls_name,cls_num):
        count_result[i] = j
    return count_result



if __name__ == "__main__":
    # Example input dictionary
    remap_dictionary({1: 1, 3: 11})  # 11 won't be found in the mapping
