"""
Semantic images come in two variants, semantic and semantic_pretty.
They both include information from the point cloud annotations,
but only the semantic version should be used for learning.
The semantic images have RGB images which are direct 24-bit base-256 integers
which contain an index into /assets/semantic_labels.json.
Pixels where the data is missing are encoded with the color #0D0D0D
which is larger than the len( labels ).

You can use the data/rgb images as input for the network.
You can get the correct label by converting the corresponding image from data/semantic
susing utils.py to get the correct index from the color coding.
"""

import os
from utils import *
import random

PATH_Base = os.path.dirname(os.path.dirname((os.path.realpath(__file__)))) # for just atom.io
#PATH_Base = os.path.dirname(os.getcwd()) # for pycharm general
PATH_RGB_Images           = os.path.join(PATH_Base, "area_3", "data", "rgb")
PATH_Semantic_Images      = os.path.join(PATH_Base, "area_3", "data", "semantic")
PATH_Semantic_Labels_Json = os.path.join(PATH_Base, "assets", "semantic_labels.json")

labels = load_labels(PATH_Semantic_Labels_Json)
LIST_Semantic_Images = os.listdir(PATH_Semantic_Images)
# LIST_Semantic_Images[0] -> .gitkeep is the first element

def mouse_clicked(event, x, y, flags, images):
    if event == cv2.EVENT_LBUTTONDBLCLK:
        write_object_name(images, x, y)

def write_object_name(images, x, y):
    cv2.circle(images[1], (x, y), 3, (255, 255, 255), -1)
    font      = cv2.FONT_HERSHEY_SIMPLEX
    position  = (x-20, y+20)
    fontScale = 0.5
    fontColor = (255,255,255)
    lineType  = 1
    text      = get_object_name(images[0], x*2, y*2)
    cv2.putText(images[1], text, position, font, fontScale, fontColor, lineType)

def get_object_name(image, x, y):
    # OpenCV returns pixels in order of BGR. So, Flip it to be RGB.
    object = 'MISSING'
    pix = np.flip(image[y, x])
    i = get_index(pix)
    if i < len(labels):
        instance_label = labels[i]
        instance_label_as_dict = parse_label(instance_label)
        object = instance_label_as_dict["instance_class"]
    print('pixels: ' + str(pix) + ' = ' + object)
    return object

def main():
    random_i = random.randint(1, len(LIST_Semantic_Images)-1)
    PATH_im = os.path.join(PATH_Semantic_Images, LIST_Semantic_Images[random_i])
    #image = cv2.imread(PATH_im)
    image = cv2.imread('camera_0ccf3c78ef354902b516c62ef8fb7cf1_lounge_2_frame_13_domain_semantic.png')
    height, width, depth = image.shape
    image_scaled = cv2.resize(image, (int(height/2), int(width/2)))

    cv2.namedWindow('image')
    cv2.setMouseCallback('image', mouse_clicked, [image, image_scaled])

    while True:
        cv2.imshow('image', image_scaled)
        # Esc key to terminate
        if cv2.waitKey(20) == 27:
            break

    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
