import cv2
from color_descriptor import ColorDescriptor

cd = ColorDescriptor((8, 12, 3))


def feature_extraction(imagePath):
    """Read an image and return a list features.
    """
    imageID = imagePath[imagePath.rfind("/") + 1:]

    image = cv2.imread(imagePath)
    # describe the image
    features = cd.describe(image)
    # write the features to file
    features = [str(f) for f in features]
    result = ("%s,%s\n" % (imageID, ",".join(features)))
    return result
