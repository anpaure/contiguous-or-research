# R2 audit: compact-v3 + rank11 + C18 union694 capped solver pair

Date: 2026-08-02  
Finite root: `/home/amodo/or15/work/r2_k17_v3_rank11_c18_union694_child_20260802`

The independently replayed child is

```text
p cnf 366131 2037544
SHA256 7d7ed776c2141f492187cebfff01653a430af5ca574afa84cdaa9994f4b418dd
```

Exactly two solver processes were launched on this child. Kissat 4.0.4 was
pinned to CPU 20 and CaDiCaL 3.0.1 to CPU 22. Each wrapper authenticated the
child hash, imposed an 8-GiB address-space limit, used nice level 15, and
applied `timeout --signal=TERM --kill-after=30s 1800s`. The wrapper hashes are
`b4a6cc6c173230da398a057993b6eed3849f553e27d334d767435c0c5e29837c`
and `6fb31b9c2a12d34cffe75734d4886c204eaf2646ce0c68c2fefb76469dc711a0`.
The solver-binary hashes are
`3ee4239c0bef4d237ab72827613426855b17c636d3b5843158fe5e549b175b0d`
and `49c86c5f8447d768906dcd12d62fb4752e80a48a0d52bbc633929f32eec00b3d`.

Both wrappers exited 124 at their caps. Neither output contains a terminal
`s SATISFIABLE` or `s UNSATISFIABLE` line, neither contains a model `v` line,
and no model artifact exists. The exact result of each run, and hence of this
two-solver portfolio, is **UNKNOWN**.

| solver | wall seconds | maximum RSS KiB | output SHA256 | retained trace bytes | retained trace SHA256 |
|---|---:|---:|---|---:|---|
| Kissat | 1800.03 | 426588 | `0e43e7f6e7d56bd7664fdf993fdda93ab9da4ee2af52627f75a45446c5b31ba` | 4793951471 | `3ac04b81bda1029123a64105d36c60a99074741d318e092fd4149833fdcdec67` |
| CaDiCaL | 1800.05 | 723124 | `7d0bb52f0948961da42a4f5d4a723859a01ff5808146473ce84380504d7436f7` | 4712214528 | `141828f39c09a087b79f4549ad94f45649acb917444da7b71f7407ef97823458` |

The retained files are interrupted binary-DRAT traces. They are not complete
UNSAT certificates, `proof_complete=false`, and `proof_verified=false`. No
proof checker was launched. The large traces remain only at the finite root;
the small fail-closed inventory and solver outputs are mirrored under
`scratch/r2_k17_v3_rank11_c18_union694_timeout_20260802`.

The remote timeout manifest has SHA-256
`2bf2f76f62442ac5a94a6fa3f2bcbc4b884d25a2a0284e73efd943c2f5236a14`.
The fail-closed inventory has SHA-256
`aef977c3ade943a54cf075481704ee0b7cbf826d0be4f6338e81b48304b9fd37`.
The local small-artifact manifest has SHA-256
`6906916044cf54078115a19a658445eee59912108383ff7dbed316940ec33b0c`;
its complete replay passes.

This is a solver-status audit only. It proves neither SAT nor UNSAT and makes
no source, compiler, opening, exterior-window, regeneration, or word claim.
