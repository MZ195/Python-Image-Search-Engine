from time import time
import multiprocessing


class MapReduce(object):

    def __init__(self, map_func, num_workers=None):
        """
        map_func
          Function that's gonna be run by each worker over the given data.

        num_workers
          The number of workers to create in the pool. 
          Defaults to the number of Cores available on the current machine.
        """
        self.map_func = map_func
        self.pool = multiprocessing.Pool(num_workers)

    def __call__(self, inputs, chunksize=6):
        """Process the inputs through the map and reduce functions given.

        inputs
          List of images to be proccessed.

        chunksize
          The portion of the input data to hand to each worker.
          You can fine tune the number to your specific machine.
        """

        print("Mapping...")
        start_timer = time()
        map_responses = self.pool.map(
            self.map_func, inputs, chunksize=chunksize)

        self.pool.close()
        self.pool.join()

        print("Done Processing in {}s".format(time() - start_timer))

        return map_responses
