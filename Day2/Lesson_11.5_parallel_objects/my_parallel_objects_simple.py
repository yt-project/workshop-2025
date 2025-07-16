import numpy as np
import time
import yt
yt.enable_parallelism()

def do_some_work(some_work):
    return np.random.random() * some_work

if __name__ == "__main__":
    all_work = np.arange(10)
    for my_work in yt.parallel_objects(all_work):
        yt.mylog.info(f"Working on {my_work}.")
        do_some_work(my_work)
