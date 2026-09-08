# Certified finite gaps and the next construction priorities outside `k=11`

## 1. Conventions and authoritative evidence

`nu(k)` is the zero-free optimum: entries and required targets are nonzero.
For the original problem, which also requires zero,

\[
N(k)=\nu(k)+1.
\]

The lower bounds below are the record rank-count bounds recomputed by
`scratch/check_iterated_boundary_core_rigidity.py`.  A fresh run on
2026-07-24 ended in `PASS`.  The upper bounds are the lengths emitted by
`construct_or_array.cpp`; `construct_best_suffix_verification.log` records
independent full coverage for every `0 <= k < 20`.

| `k` | certified `nu(k)` | gap | status/source of upper bound |
|---:|---:|---:|---|
| 0 | 0 | 0 | exact convention |
| 1 | 1 | 0 | exact |
| 2 | 2 | 0 | exact |
| 3 | 4 | 0 | exact |
| 4 | 7 | 0 | exact |
| 5 | 12 | 0 | exact |
| 6 | 21 | 0 | exact |
| 7 | 37 | 0 | exact |
| 8 | 72 | 0 | exact certificate |
| 9 | 128 | 0 | exact certificate |
| 10 | 254 | 0 | exact certificate |
| 11 | `465..477` | 12 | live exact/construction lane |
| 12 | 926 | 0 | exact certificate |
| 13 | `1719..1852` | 133 | trimmed lift of the `k=12` optimum |
| 14 | `3434..3676` | 242 | explicit `k14_completed_3676.txt` |
| 15 | `6438..7352` | 914 | trimmed lift from `k=14` |
| 16 | `12873..14704` | 1831 | trimmed lift from `k=14` |
| 17 | `24313..29408` | 5095 | trimmed lift from `k=14` |
| 18 | `48623..58816` | 10193 | trimmed lift from `k=14` |
| 19 | `92381..117632` | 25251 | trimmed lift from `k=14` |

Relevant current hashes are:

```text
9a019a65028f9e9d5d69340c67af3bd298f530ea6e9b590a86d37b1768e8ec6e  FINITE_K_STATUS_20260724.md
1814bc48a4d10fc6b5fd7867e0188860a3d2e37cf25c8d33f54b222b3ce1fb64  ITERATED_BOUNDARY_CORE_RIGIDITY.md
47369819af5d4aa82fe2398150abad1d0891802b3f038a307c63e80f628eb6b1  scratch/check_iterated_boundary_core_rigidity.py
2ed012350cce77e09df791224cd02af03c629b9e02518d502c17c6c135bb0e87  construct_or_array.cpp
190273949c7a08de811d6da8c874e9a132d7a3440580b07361f17186bb9e8daa  construct_best_suffix_verification.log
```

## 2. Audited `k=13` one-interface screen

For the 926-entry exact `k=12` word `A`, and two deleted indices `a<b`, put

\[
P_{a,b}=(0,A_0,\ldots,\widehat{A_a},\ldots,
                 \widehat{A_b},\ldots,A_{925}).
\]

The intended 13-bit word is

\[
A\ \Vert\ (4096\mathbin{\mathrm{OR}}P_{a,b}),
\]

of length `926+925=1851`.  The leading zero in `P` becomes the nonzero
literal `4096`.

The evaluator in `k13_one_interface_trim.cpp` is exact for this family:

* intervals wholly inside the transformed suffix project to interval ORs of
  `P`;
* intervals crossing the interface project to a suffix OR of `A` joined with
  a prefix OR of `P`;
* the original half `A` already covers every target not containing bit 12.

The old `FOUND` writer emitted an additional standalone `4096` before also
emitting `4096|P[0]=4096`.  It therefore wrote 1852 entries while claiming
1851.  The writer has been corrected by removing that extra output entry;
the corrected source hash is

```text
78a9eb8d62791a5d3aaad5b0cf7c9436b461f85f5caf0d4a79e252909ab25e81
```

Both orientations were then screened on RunPod.  Each run exhausts all
`C(926,2)=428275` deletion pairs.  Results:

```text
forward:  found=0 best=4094/4096
reverse:  found=0 best=4094/4096
```

In both orientations a best deletion is the two endpoints, `(0,925)`.
Independent construction of those two 1851-entry words gives the exact
remaining targets

```text
forward:  5712 5972   (high-bit projections 1616 1876)
reverse:  4897 4977   (high-bit projections  801  881)
```

Thus the corrected screen yields no new bound, but it rigorously closes this
entire two-deletion one-interface neighborhood.  Any improvement in this
architecture needs value changes, reordering, more than one interface, or a
shorter non-high prefix.

## 3. Highest downstream-leverage finite construction attempt

The best next construction target is the exact 241-entry suffix problem for
the certified 3434-entry `k=14` prefix.  A SAT model would give

\[
\nu(14)\le3675.
\]

Because the stored construction for every `k>=15` is a trimmed lift from
`k=14`, one saved `k=14` entry propagates as reductions

```text
k=14: 1,  k=15: 2,  k=16: 4,  k=17: 8,  k=18: 16,  k=19: 32.
```

No one-entry `k=13` improvement propagates: its lift has length 3702, still
above the current 3676-entry `k=14` word.  `k=13` would have to reach at most
1837 before its lift superseded the present `k=14` base.

The `k=14` attempt is already exact and independently audited:

* prefix: `k14_pinnable_factor_missing260.txt` (3434 entries);
* phase seed: `k14_append_242.txt`;
* exact generator: `scratch/k14_append241_exact.cpp`;
* branch manifest: `k14_append241_branch_manifest.txt` (52 branches);
* recommended first branches: branch 5 (`x=1,p=5,f=2`) and branch 36
  (`x=2,p=23,f=2`), both carrying the successful seam target `13423`;
* candidate verification: first require exactly 3675 entries after prefix
  concatenation, then run both `verify_or_array 14` and
  `verify_or_suffix 14`;
* UNSAT may be promoted only after a proof trace passes an independent DRAT
  checker; a timeout or solver exit alone has no mathematical force.

The exact source and manifest hashes are

```text
b4b7b586766906bf0727adeb587cccb98cb57b9783e9e3059498bce292fab964  scratch/k14_append241_exact.cpp
5f5881811446be60dd83e51da8adfe7577e6331b7277219161800eb95280602e  k14_append241_branch_manifest.txt
```

This should be scheduled only after a current high-memory `k=11` exact lane
releases a CPU and memory headroom.  The present RunPod was near its memory
ceiling and every allowed CPU was occupied during this audit, so no competing
`k=14` solver was launched.
