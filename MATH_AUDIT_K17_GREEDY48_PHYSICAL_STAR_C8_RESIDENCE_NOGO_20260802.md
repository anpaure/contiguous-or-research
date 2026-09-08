# `k=17` greedy48: complete physical star-`C8` residence census

Date: 2026-08-02  
Status: exact finite no-go for one protected-disjoint physical **star** `C8`
on the frozen `greedy48` factor.  This note does not cover octahedral
rank-six-core `C8`s, compound circuits, or more than one toggle.

## 1. Frozen face

The source factor is

```text
scratch/k17_c68b_double_fusion_residence_greedy_20260802/
  c68b.greedy48.factor.tsv
```

It is one physical cycle on all `24,310` rank-nine owners, uses every
rank-eight facet once, covers all `19,448` rank-ten caps, and fixes `3,944`
protected facets.  Its positive coordinate-run census is

```text
length 1:    0
length 2: 2312
length 3: 1887
```

Thus its number of positive runs shorter than four is `4199`, with residence
deficit

```text
3*0 + 2*2312 + 1887 = 6511.
```

Its cyclic accumulated-owner deck has respectively

```text
rank 11 holes: 2006
rank 12 holes:  391
rank 13 holes:   34.
```

## 2. Complete star-`C8` parameterization

A directed physical star octagon has a rank-seven core `S` and four distinct
petals `a0,a1,a2,a3` outside `S`.  Put, with indices modulo four,

```text
C_i = S + a_i,
T_i = S + a_i + a_(i+1).
```

The old phase consists of the four selected incidences `(C_i,T_i)`.  The
toggle removes those incidences and adds `(C_i,T_(i-1))`.  Quotienting only
by cyclic choice of root leaves exactly

```text
binom(17,7) * (10*9*8*7)/4 = 24,504,480
```

geometric directed rotation classes.  Reverse direction is not identified:
it is the other directed phase and is tested separately when active.

The primary enumerator follows the two selected owner transitions at every
facet.  An independent verifier instead scans all `24,504,480` geometric
classes directly.  They agree on every count and replay every retained row.

## 3. Exact filter ledger

The direct census is:

| gate | surviving/count at gate |
|---|---:|
| active directed star-`C8` rotation classes | 74,851 |
| blocked by at least one protected facet | 37,995 |
| blocked because a new incidence is already selected | 10,404 |
| preserve every rank-ten cap | 238 |
| also leave one physical component | 102 |

For every one of the final `102`, the code mutates the four literal
incidences, independently reconstructs the full `24,310`-owner cycle, and
replays owner degree, cap multiplicity, coordinate runs, and cyclic upper
interval unions.  Exact rank-eight facet use and rank-nine degree two are
preserved by the incidence circuit and are also checked during traversal.

## 4. Residence result

No retained star octagon improves either the number of positive short runs
or their residence deficit.  In fact every retained octagon strictly
worsens them.  The complete `(delta length-2, delta length-3)` histogram is

| `delta length-2` | `delta length-3` | count |
|---:|---:|---:|
| 0 | +1 | 17 |
| 0 | +3 | 17 |
| +1 | 0 | 34 |
| +2 | 0 | 17 |
| +3 | 0 | 17 |

Every candidate has `delta length-1 = 0`.  Therefore, on this frozen factor,

> no individual protected-disjoint physical rank-seven-core star-`C8`
> preserving every rank-ten cap and one physical component can improve
> positive depth-three residence.

This is a finite face theorem, not a global residence obstruction.

## 5. Deeper-upper trade-off

Thirty-four retained octagons reduce the number of rank-eleven holes, while
none reduces rank-twelve or rank-thirteen holes.  The best upper move is

```text
core = 319
petals = (6,10,15,13)
```

and changes the hole vector

```text
(2006,391,34) -> (2003,391,34).
```

It simultaneously changes the positive short-run vector

```text
(0,2312,1887) -> (0,2314,1887),
```

so it is an upper/residence trade rather than a joint improvement.  Its
literal factor and patch are frozen for any later compound search.

## 6. Scope exclusions

The no-go covers exactly one active directed **star** `C8`, with rank-seven
core and four distinct petals, applied to the frozen `greedy48` factor while
requiring:

* no protected facet is changed;
* exact rank-eight facet use;
* rank-nine owner degree two;
* every rank-ten cap remains covered;
* the physical factor remains one cycle.

It does **not** cover:

* octahedral `C8`s with a rank-six core;
* compound or sequential `C8` moves;
* a move that temporarily sacrifices a rank-ten cap or connectivity;
* another carrier or another protected bank;
* source-letter binding, lower compilation, or a universal OR word.

## 7. Frozen artifacts

```text
d3f305bd85517a5ac03eb7af9abc2a640fe823e4b30f2b0954eeb02e28446e6a  scratch/enumerate_k17_greedy48_physical_star_c8_20260802.cpp
14ecc80b3876fd2dfff0cb06929c514677ffe1c82dbf8eddf1f66057198da6ab  scratch/verify_k17_greedy48_physical_star_c8_20260802.cpp
b1343737cb0e3d99dec503e526e566521504478af1c5792c9a7949b6a5796616  scratch/k17_c68b_double_fusion_residence_greedy_20260802/c68b.greedy48.factor.tsv
a2674abc956e6e227c5255b82841cf474bb945aac49c1eda01b09b7b10869812  scratch/k17_greedy48_physical_star_c8_20260802/pc8_greedy48_star.audit.json
7a81037620c9ea1acecd6eee66f77f4665072fb7838e9397fc4974c13d7a9cf4  scratch/k17_greedy48_physical_star_c8_20260802/pc8_greedy48_star.independent.audit.json
2c00a7cd83087db4de5356a2228449d2f1aacd485a7e07719eafc7ef37af1987  scratch/k17_greedy48_physical_star_c8_20260802/pc8_greedy48_star.valid.tsv
6c1ded8f0a0169358cfe1ae4a93a9638a350dec5f2102c18080261a11a475839  scratch/k17_greedy48_physical_star_c8_20260802/pc8_greedy48_star.delta23.tsv
f03867aa94c4114e912794017af3cbf65603809725c173899d064e71ed4c7c5b  scratch/k17_greedy48_physical_star_c8_20260802/pc8_greedy48_star.best_upper.patch.tsv
3b26ec59e13bba403ce288a25ace0e681cd05e5198bff2726177c76f9c4bff07  scratch/k17_greedy48_physical_star_c8_20260802/pc8_greedy48_star.best_upper.factor.tsv
```

Remote O3 runs were CPU-only and isolated under

```text
/home/amodo/or15/work/pc8_greedy48_star_20260802
/home/amodo/or15/work/pc8_greedy48_star_verify_20260802
```

