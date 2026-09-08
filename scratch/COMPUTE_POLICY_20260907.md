# Computation constraint

User instruction, received 2026-09-07:

> you can do any heavy computation you want, but only explicitly on ssh h100

All heavy enumeration, optimization/solver runs, simulation, and substantial
numerical workloads must therefore run through `ssh h100`, not locally.
Local proof development, file inspection/editing, and genuinely small
verification checks may continue. Do not treat availability of a local
solver environment as permission to use it for heavy work.

The connection was checked with `ssh -o BatchMode=yes -o ConnectTimeout=10
h100 hostname`; the remote host reported `arboghast`. The ten-axis catalogue
and 30-second local CP attempt had already finished before this constraint
arrived. No local heavy job was left running. Future heavy work must be
relocated, not restarted locally.

The dedicated remote directory for the next ten-axis template search is
`/home/amodo/or-research-20260907-QiqXT3`. The host reports 64 CPUs and has
Python 3.12.3 with OR-Tools, NumPy, and SciPy available. The three
`binary10_involution_*_20260907` source files were copied there with `scp`;
the C++ catalogue was compiled there through `ssh h100`. No heavy local
enumeration or solver run was used for this migration.
