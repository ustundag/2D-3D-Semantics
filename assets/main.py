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
using utils.py to get the correct index from the color coding.
"""

import os
from utils import *

#PATH_Base = os.path.dirname(os.path.dirname((os.path.realpath(__file__)))) # for just atom.io
PATH_Base = os.path.dirname(os.getcwd()) # for pycharm general
PATH_RGB_Images = os.path.join(PATH_Base, "area_3", "data", "rgb")
PATH_Semantic_Images = os.path.join(PATH_Base, "area_3", "data", "semantic")
PATH_Semantic_Labels_Json = os.path.join(PATH_Base, "assets", "semantic_labels.json")

def main():
    labels = load_labels(PATH_Semantic_Labels_Json)
    LIST_Semantic_Images = os.listdir(PATH_Semantic_Images)
    # LIST_Semantic_Images[0] -> .gitkeep is the first element
    #PATH_im = os.path.join(PATH_Semantic_Images, LIST_Semantic_Images[10])
    PATH_im = os.path.join(PATH_Semantic_Images, "camera_bbda26272dd346e595ed8e87a2d91020_office_3_frame_18_domain_semantic.png")

    image = cv2.imread(PATH_im)
    x_coor = 900
    y_coor = 100
    # OpenCV returns pixels in order of BGR. So, Flip it to be RGB.
    pix = np.flip(image[x_coor, y_coor])
    i = get_index(pix)
    instance_label = labels[i]
    instance_label_as_dict = parse_label(instance_label)
    print(instance_label_as_dict)

    height, width, depth = image.shape
    image_scaled = cv2.resize(image, (int(height/2), int(width/2)))

    font      = cv2.FONT_HERSHEY_SIMPLEX
    position  = (int(y_coor/2)+10, int(x_coor/2)-10)
    fontScale = 1
    fontColor = (255,255,255)
    lineType  = 2
    text      = instance_label_as_dict["instance_class"]
    cv2.putText(image_scaled, text,
        position,
        font,
        fontScale,
        fontColor,
        lineType)
    cv2.imshow('image', cv2.circle(image_scaled, (int(y_coor/2), int(x_coor/2)), 10, (255, 255, 255), -1))
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
