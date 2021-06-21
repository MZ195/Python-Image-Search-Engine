# import the necessary packages
from Multiprocessing.mapReduce import MapReduce
from Multiprocessing.multiprocessHelper import feature_extraction

import argparse
import glob

if __name__ == '__main__':
    # construct the argument parser and parse the arguments
    ap = argparse.ArgumentParser()
    ap.add_argument("-d", "--dataset", required=True,
                    help="Path to the directory that contains the images to be indexed")
    ap.add_argument("-i", "--index", required=True,
                    help="Path to where the computed index will be stored")
    args = vars(ap.parse_args())

    # use glob to grab the image paths and loop over them
    inputs = glob.glob(args["dataset"] + "/*.jpg")
    mapper = MapReduce(feature_extraction)

    mapper_result = mapper(inputs)

    output = open(args["index"], "w")
    for i in range(len(mapper_result)):
        output.write(mapper_result[i])
