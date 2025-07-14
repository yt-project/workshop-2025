import yt
import numpy as np
import sys

MANUAL = len(sys.argv) == 2 and (sys.argv[1].strip() == "manual")

yt.enable_parallelism()
yt.mylog.setLevel(40)
ds = yt.load("output_00239")

# Load in a sphere
# *center, Rvir = np.loadtxt("halo_qties.txt", delimiter=",")
# sp = ds.sphere(center, Rvir * 4)``

# Load in everything
sp = ds.all_data()

if MANUAL:
    T = sp["gas", "temperature"]
    n = sp["gas", "number_density"]
    dx = sp["index", "dx"]
    V = sp["gas", "cell_volume"]

    T_mean, n_mean, dx_mean = (np.average(_, weights=V) for _ in (T, n, dx))
    T_std, n_std, dx_std = (
        np.sqrt(np.average((x - m) ** 2, weights=V))
        for x, m in zip((T, n, dx), (T_mean, n_mean, dx_mean))
    )
else:
    (T_std, T_mean), (n_std, n_mean), (dx_std, dx_mean) = (
        sp.quantities.weighted_standard_deviation(
            [("gas", "temperature"), ("gas", "number_density"), ("index", "dx")],
            weight=("gas", "cell_volume"),
        )
    )

if yt.is_root():
    import resource

    print(
        f"Temperature:    {T_mean:.2f} ± {T_std:.2f}\n"
        f"Number density: {n_mean.to('1/cm**3'):.2e} ± {n_std.to('1/cm**3'):.2e}\n"
        f"Cell size:      {dx_mean.to('kpc'):.2e} ± {dx_std.to('kpc'):.2e}\n"
        f"Memory usage:   {resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1024:.1f} MiB",
    )

# MANUAL:                             2m 3s    22 970 Mib
# yt's derived quantities,  1 core:   1m32s     2 327 Mib
# yt's derived quantities,  2 cores:    48s     1 375 MiB
# yt's derived quantities,  4 cores:    26s       908 Mib
# yt's derived quantities,  8 cores:    16s       663 Mib
# yt's derived quantities, 16 cores:    10s       563 Mib
