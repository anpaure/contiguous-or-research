# Provenance and certificate formats

Date: 2026-09-09. One source-reviewed build and one fixed mathematical run.
Root authorized execution after its own and both peer agents' full reads.
No alternate graph, cut, seed, word modification, or retry occurred.

`exact_commands.txt` retains the full executed commands, including the build
resource guard and remote source-hash assertion. The C++17 optimized build
exited 0 under CPU60/wall90/2GiB. The compiler's one indentation warning
concerns the correctly external offset update after a collar-check loop;
no source change or rebuild followed it. The build log is retained.

The mathematical run used CPU120 total (driver5 + child115), wall150,
2GiB address space, and512MiB per individual file. It exited0 and completed
both its primal-flow and dual-Hall replay. Actual aggregate CPU was
2.877601905 seconds and wall was2.879199883900583 seconds. The final flow
695397 and deficiency462 were observed and proved, not assumed.

The entire original output directory was copied from
`h100:/home/amodo/exact-b-k21-fixed-candidate-hall-20260909/`. Every entry
in the runner-generated `SHA256SUMS` passed local hash verification after
copying. Added build/wrapper logs and this provenance are included in the
supplementary complete manifest, while the original manifest is preserved.

Important hashes:

* Input: `0b166713d18f9ba4d064b07575c17068008954ac808313359c5fd0bf5dfe24d7`.
* C++: `26fb17223bcd5ef0d79ac27a90b37d2c7b52b1c7cf706622f7c22f624fdee120`.
* Runner: `e615be577c4e43427fc022b7e88eb0616299d460f70e226b8886bb58d1651d33`.
* Binary: `f6595344c18876165034bec17e0d8c9a629736a151b98a283ba63cfea0d9f591`.
* Complete report: `88590f8fa501a342fbbf6f9b244144296f067d8ac47c391a034a98135103c916`.
* Candidate report: `149c4e9a88ab9f88e66cac1fe8ebed0cc0f79078a3dcbea3d8e37d00d69132a9`.

All identifiers and cyclic positions below are zero-based.

* `target_orbits.tsv`: target ID, canonical mask, actual orbit size, rank.
* `cell_orbits.tsv`: cell ID, length1/2, cycle ID, start position, canonical
  R mask, forced K, available V, first E, second E or0, neighbor count.
* `graph_rows.bin`: eight-byte magic `H21ROW01`; little-endian uint32
  target count, uint32 cell count, uint64 edge count; then for every cell
  a uint32 degree followed by that many sorted uint32 target IDs.
* `positive_flow.tsv`: target ID, cell ID, positive integral amount.
  Zero-flow edges are implicit. The graph contains every eligible edge.
* `cut_target_orbits.txt`, `cut_cell_orbits.txt`: complete dual cut sets.
* `hall_physical_target_masks.txt`: all31,185 actual target masks.
* `hall_physical_neighbor_cells.tsv`: cycle ID, start, length, cell-orbit
  ID for all30,723 candidate cells in the COMPLETE physical neighborhood.

The latter family has462 fewer cells than targets. This is a fixed cyclic
candidate-graph obstruction. Simultaneous cap compatibility, seam/tail
repairs, other carriers, and unrestricted optimum claims are not certified.
