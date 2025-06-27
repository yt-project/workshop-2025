A smaller code snippet for Tiled Arbitrary Grids, won't run but a bit 
easier to show quickly: 

```python

# create a tiled arbitrary grid (does not sample yet)
tag = YTTiledArbitraryGrid(
    ds.domain_left_edge, 
    ds.domain_right_edge, 
    (400, 400, 400),  # desired size across all grids
    100, # chunksize 
    ds=ds  # the dataset to sample: actually required until tied into full yt
)

print(tag)
# YTTiledArbitraryGrid with total shape of 
# (np.int64(400), np.int64(400), np.int64(400)) 
# divided into 64 grids: (np.int64(4), np.int64(4), np.int64(4)) grids 
# in each dimension.


# pre-allocate an array to store the output in. 
# agnostic to array type: e.g., numpy array for in-memory, zarr file for
# on-disk

my_pre_allocated_array = ... 


# sample desnity on all the tiled grids, storing in the pre-allocated
# array. Also take the log10 of the field (by chunk). 
_ = tag.to_array(
    ("gas", "density"),
    output_array=my_pre_allocated_array,
    ops=[
        np.log10,
    ],
)
```    