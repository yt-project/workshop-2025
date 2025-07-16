# ----------------------- I
tall = ds.region(center, [center[0]-Rvir/10, center[1]-Rvir/10, center[2]-Rvir], [center[0]+Rvir/10, center[1]+Rvir/10, center[2]+Rvir])

p = yt.ProjectionPlot(
    ds,
    "x",
    ("gas", "density"),
    data_source=tall,
    center=sp.center,
    width=4 * Rvir,
    weight_field="density",
)
p.annotate_sphere(center, Rvir)
p

# ----------------------- Plus
tall = ds.region(center, [center[0]-Rvir/10, center[1]-Rvir/10, center[2]-Rvir], [center[0]+Rvir/10, center[1]+Rvir/10, center[2]+Rvir])
wide = ds.region(center, [center[0]-Rvir/10, center[1]-Rvir, center[2]-Rvir/10], [center[0]+Rvir/10, center[1]+Rvir, center[2]+Rvir/10])

plus = tall + wide

p = yt.ProjectionPlot(
    ds,
    "x",
    ("gas", "density"),
    data_source=plus,
    center=sp.center,
    width=4 * Rvir,
    weight_field="density",
)
p.annotate_sphere(center, Rvir)
p



#----------------------- Smiley
wedge = sp_halo.cut_region(["obj['spherical_theta'] > 2*np.pi/3", "obj['spherical_theta'] < 5*np.pi/3"], locals={"np": np})
shell = ds.sphere(center, Rvir) - ds.sphere(center, Rvir * 0.9)

smile = wedge & shell

left_eye  = ds.region(center, center+[-Rvir/10, -Rvir/10*5, 0*Rvir], center+[Rvir/10, -Rvir/10*3, Rvir])
right_eye = ds.region(center, center+[-Rvir/10, +Rvir/10*3, 0*Rvir], center+[Rvir/10, +Rvir/10*5, Rvir])

eyes = left_eye + right_eye

smiley = smile | eyes

dope = sp_halo - smiley

p = yt.SlicePlot(
    ds,
    "x",
    ("gas", "density"),
    data_source=dope,
    center=sp.center,
    width=4 * Rvir,
)
p