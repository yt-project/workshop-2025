# yt user/developer workshop 2025
The 2025 yt user/developer workshop was held July 15-18, 2025 at the Higgs Centre for Theoretical Physics at University of Edinburgh.
This repository contains Jupyter notebooks and links to videos for the tutorials and lightning talks from the workshop.

* webpage: https://indico.ph.ed.ac.uk/event/346/
* program: https://indico.ph.ed.ac.uk/event/346/timetable/
* youtube playlist: https://www.youtube.com/playlist?list=PL8tPWjc5gBfQLLvTK1G_48o_D6RgaLC48
* sample datasets: https://girder.hub.yt/#collection/68628933ed776d031cebf8ea

## Workshop Videos
The links below are to the individual presentation videos on youtube. See the [youtube playlist](https://www.youtube.com/playlist?list=PL8tPWjc5gBfQLLvTK1G_48o_D6RgaLC48) for a playlist of all presentations.

### Day 1

| Speaker | Title
| :-------| :----
| Britton Smith | [Welcome and Introduction](https://www.youtube.com/watch?v=J-D04EEHQsE)
| Matt Turk | [Introduction to yt’s core principles or The yt Way (Lessons 1 and 2: the dataset and the frontend)](https://www.youtube.com/watch?v=kB8a8UvhOlA)
| Britton Smith | [Lesson 3: on-disk fields and basic data containers](https://www.youtube.com/watch?v=oAlavG3BZUw)
| Corentin Cadiou | [Lesson 4: Derived Quantities](https://www.youtube.com/watch?v=AbR6KVILjQM)
| Matt Turk | [Lesson 5: Derived Fields](https://www.youtube.com/watch?v=b91ZNv2FKZM)
| Chris Havlin | [Lesson 6: Plots](https://www.youtube.com/watch?v=VOKiVmI_08s)
| Clément Robert | [Customising yt plots with user-defined annotations](https://www.youtube.com/watch?v=fTy3AlksPk4)
| Avery Meiksin | [Using yt in teaching](https://www.youtube.com/watch?v=YQ310-JLeq0)
| Adam Koval | [Analysing SPH simulations of fragmenting protoplanetary discs](https://www.youtube.com/watch?v=B7nVrFUs6H0)

### Day 2

| Speaker | Title
| :-------| :----
| Corentin Cadiou | [Lesson 7: Advanced Data Containers](https://www.youtube.com/watch?v=XdfPUDrfs_I)
| Britton Smith | [Lesson 8: Time-series](https://www.youtube.com/watch?v=YhJ_AsXLAu4)
| Chris Havlin | [Lesson 8.5: Generic Data Loaders](https://www.youtube.com/watch?v=Ry_tNcRXijE)
| Chris Havlin | [Lesson 9: Volume Rendering](https://www.youtube.com/watch?v=Ry_tNcRXijE&t=4s)
| Matt Turk | [Lesson 10: Widgyts](https://www.youtube.com/watch?v=juJzYyTuxfQ)
| Matt Turk | [Lesson 11: Parallelism and Performance](https://www.youtube.com/watch?v=XnZnDKmuAKU)
| Britton Smith | [Lesson 12: Saving reloadable data](https://www.youtube.com/watch?v=rmW8Wrq-9UQ)
| Evan Jones | [A New Axis to the Circumgalactic Medium](https://www.youtube.com/watch?v=cTjuIWR326o)
| Jordi De Jonghe | [MHD simulation of tearing thermal instability](https://www.youtube.com/watch?v=goo8Y1jqm0E)
| Corentin Cadiou | [A New Way to Add Fields](https://www.youtube.com/watch?v=kCutEjhimr8)

### Day 3

| Speaker | Title
| :-------| :----
| Dan Eastwood | [yt_georaster (satellite imagery)](https://www.youtube.com/watch?v=Hgx4td6YvDs)
| Chris Havlin | [yt_xarray (geophysics), yt_aspect (geophysics), yt-napari (biology)](https://www.youtube.com/watch?v=DKPcywy5JLU)
| Théo Gayoux | [Clustering dark energy with Nefertiti](https://www.youtube.com/watch?v=aGyAo7md2GM)
| Romeel Davé | [Caesar](https://www.youtube.com/watch?v=cqDDAy-Ccmo)
| Britton Smith | [ytree: yt for merger trees](https://www.youtube.com/watch?v=0uxVXGajP78)
| Britton Smith | [pygrackle: grackle with yt](https://www.youtube.com/watch?v=wB-1STFs54E)
| Romeel Dave | [Crackle](https://www.youtube.com/watch?v=VWKKDscubPI)
| Matt Turk | [Lesson 13: Development Environments](https://www.youtube.com/watch?v=5s0XtZu8ELU)
| Matt Turk | [Will yt Blend?](https://www.youtube.com/watch?v=wxf2UpZ0mao)
| Matt Turk | [Lesson 14: Implementing New Frontends](https://www.youtube.com/watch?v=HihJEIo3QjU)

## Installation

The `requirements.txt` in the root folder of this repository contains some general requirements used across sessions for a base `yt` installation with the requirements for using `yt.load_sample_data()`. Individual session folders may contain additional requirements to install. 

To install the base requirements with `pip`:

```shell
python -m pip install --upgrade pip 
python -m pip install -r requirements.txt
```
