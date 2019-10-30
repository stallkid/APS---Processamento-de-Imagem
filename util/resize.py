import cv2
import util.filter as fr

class Resize():

    def __init__(self, target_image, input_image, context):
        self.target_image = target_image
        self.input_image = input_image
        self.context = context

    def resize_image(self):
        resize_to = cv2.imread(self.input_image)
        target = cv2.imread(self.target_image)
        height, width, depth = resize_to.shape
        new_shape = cv2.resize(target,(int(width),int(height)))
        if self.context == "flora":
            cv2.imwrite("background/flora/resized_flora.jpg", new_shape)
        else:
            cv2.imwrite("background/fauna/resized_fauna.jpg", new_shape)

        if self.context == "flora":
            image_filter = fr.Filter("background/flora/resized_flora.jpg", self.context)
        else:
            image_filter = fr.Filter("background/fauna/resized_fauna.jpg", self.context)

        new_filtered_shape = image_filter.blur_image()
        new_filtered_shape = image_filter.edge_enhancement()

        if self.context == "flora":
            cv2_new_shape = cv2.imread("background/flora/filtered_flora.jpg")
        else:
            cv2_new_shape = cv2.imread("background/fauna/filtered_fauna.jpg")
        
        return cv2_new_shape