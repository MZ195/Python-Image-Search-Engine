# import the necessary packages
from color_descriptor import ColorDescriptor
from Multiprocessing.MapReduce import MapReduce
from Multiprocessing.MultiprocessHelper import feature_extraction

import argparse
import glob
import cv2
import csv

if __name__ == '__main__':
    # construct the argument parser and parse the arguments
    ap = argparse.ArgumentParser()
    ap.add_argument("-d", "--dataset", required=True,
                    help="Path to the directory that contains the images to be indexed")
    ap.add_argument("-i", "--index", required=True,
                    help="Path to where the computed index will be stored")
    args = vars(ap.parse_args())
    # initialize the color descriptor
    cd = ColorDescriptor((8, 12, 3))

    # use glob to grab the image paths and loop over them
    inputs = glob.glob(args["dataset"] + "/*.jpg")
    mapper = MapReduce(feature_extraction)

    mapper_result = mapper(inputs)
    
    exit(0)

    # open the output index file for writing
    output = open(args["index"], "w")
    write = csv.writer(output)
    write.writerows(mapper_result)
    output.close()

    # for imagePath in glob.glob(args["dataset"] + "/*.jpg"):
    #     # extract the image ID (i.e. the unique filename) from the image
    #     # path and load the image itself
    #     imageID = imagePath[imagePath.rfind("/") + 1:]
    #     image = cv2.imread(imagePath)
    #     # describe the image
    #     features = cd.describe(image)
    #     # write the features to file
    #     features = [str(f) for f in features]
    #     output.write("%s,%s\n" % (imageID, ",".join(features)))
    # # close the index file
    # output.close()
