from mpi4py import MPI

my_size = MPI.COMM_WORLD.size
my_rank = MPI.COMM_WORLD.rank

print (f"Hello, I am process {my_rank} of {my_size}.")
