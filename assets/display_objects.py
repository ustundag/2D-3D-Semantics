from utils import *

scale_size = 1
labels = load_labels('C:/Users/ustundag/GitHub/2D-3D-Semantics/assets/semantic_labels.json')

def mouse_clicked(event, x, y, flags, images):
    if event == cv2.EVENT_LBUTTONDBLCLK:
        object = get_object_name(images[0], x*scale_size, y*scale_size)
        print(object)

def get_object_name(image, x, y):
    # OpenCV returns pixels in order of BGR. So, Flip it to be RGB.
    pix = np.flip(image[y, x])
    print('pixels: ' + str(pix))
    i = get_index(pix)
    if i < len(labels):
        instance_label = labels[i]
        instance_label_as_dict = parse_label(instance_label)
        return instance_label_as_dict["instance_class"]
    return '<MISSING>'

image = cv2.imread('camera_81a9927c6b224f4bb5e6b9fbdcfae9c0_office_3_frame_25_domain_semantic_scaled.png')
#image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
height, width, depth = image.shape
image_scaled = cv2.resize(image, (int(height/scale_size), int(width/scale_size)))

def main():
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
