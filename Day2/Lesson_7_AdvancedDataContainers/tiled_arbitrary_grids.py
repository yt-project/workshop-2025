# requires yt_experiments and zarr

import yt 
import numpy as np 

try: 
    import zarr 
except ImportError:
    raise ImportError("you need zarr! pip install zarr")

try: 
    from yt_experiments.tiled_grid import YTTiledArbitraryGrid
except ImportError:
    raise ImportError("you need yt_experiments! pip install yt_experiments")


if __name__ == "__main__":
    import os
    ds = yt.load_sample("DeeplyNestedZoom")

    # create a tiled arbitrary grid (does not sample yet)
    tag = YTTiledArbitraryGrid(
        ds.domain_left_edge, 
        ds.domain_right_edge, 
        (400, 400, 400),  # desired size across all grids
        100, # chunksize 
        ds=ds  # required for now
    )

    print(tag)
    # YTTiledArbitraryGrid with total shape of 
    # (np.int64(400), np.int64(400), np.int64(400)) 
    # divided into 64 grids: (np.int64(4), np.int64(4), np.int64(4)) grids 
    # in each dimension.

    # initialize a zarr store
    zarr_store = zarr.group("./tiled_grid_full.zarr")
    if "gas_density" in zarr_store:
        # remove it so we can re-run the script without error
        del zarr_store["gas_density"]
    zarr_field = zarr_store.empty("gas_density", 
                                shape=tag.dims, 
                                chunks=tag.chunks, 
                                )

    # store the log10(density) in the zarr array
    _ = tag.to_array(
        ("gas", "density"),
        output_array=zarr_field,
        ops=[
            np.log10,
        ],
    )

    print("resulting zarr directory structure:")
    print(os.listdir(os.path.join(zarr_store.store.path, "gas_density"))[:10])

    # resulting zarr directory structure:
    # ['0.0.0', '2.3.0', '1.3.2', '1.3.3', '3.1.1', '3.2.0', '3.2.2', '2.2.0', '0.3.1', '.zarray']
