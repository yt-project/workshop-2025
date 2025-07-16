import numpy as np
import time
import yt
yt.enable_parallelism()

def do_some_work(some_work):
    return np.random.random() * some_work

if __name__ == "__main__":
    all_work = np.arange(10)

    # this will store all the results on the root process
    all_storage = {}
    
    for my_storage, my_work in yt.parallel_objects(all_work, storage=all_storage):
        yt.mylog.info(f"Working on {my_work}.")
        my_result = do_some_work(my_work)

        my_storage.result = my_result

        # change the key for the result
        # my_storage.result_id = SOME KEY

    if yt.is_root():
        for key, val in sorted(all_storage.items()):
            yt.mylog.info(f"{key=}: result={val}")
