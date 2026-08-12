# Exact block replacement around the transformed K16 ripple seed

Date: 2026-07-30

Status: exact finite search model and solver-free width-one obstruction.  No
length-12,873 word is claimed here.  An `UNKNOWN` solver result has no negative
meaning.

## 1. Authenticated effective source

The retained byte file

```text
scratch/k16_ripple_insert12874_onehole.word
SHA-256 5ac147eca512b7e398c7217f1796836f454a304274c6e54fda7050fc9b4f66db
```

still has value `0xa069` at zero-based position `6440` and has the one hole
`0x287d`.  The newer source named in the construction discussion is the
following explicit transform of that retained file:

```text
position 6440: 0xa069 -> 0x2069.
```

Under canonical decimal, single-space, trailing-newline serialization, the
effective word has SHA-256

```text
a62cb41fc97127edbac362afa0447cf6a45d795f327ec7f2a3652f7c12873181.
```

Two independent ending/start replays give length `12874` and exact hole set

```text
0xa879 = 43129,
0xa87d = 43133.
```

Every model below pins both source hashes and performs this one transform in
memory.  It does not silently overwrite the older retained artifact.

## 2. Direct deletion is impossible

Let `W` be the effective word.  For a position `p`, let `E_{p-1}` be the
multiset of suffix OR states ending at `p-1`, and let `S_{p+1}` be the multiset
of prefix OR states beginning at `p+1`.  The intervals removed by deleting
`W_p` have labels

\[
                    e\vee W_p\vee s,
\qquad e\in E_{p-1}\cup\{0\},\quad
       s\in S_{p+1}\cup\{0\}.                    \tag{2.1}
\]

The only new intervals are the gap-crossing intervals labelled

\[
                         e\vee s,
\qquad e\in E_{p-1},\quad s\in S_{p+1}.           \tag{2.2}
\]

Subtracting the exact multiplicities in (2.1) and adding those in (2.2) is
therefore an iff test for every direct deletion.

The complete `12,874`-position census has minimum four holes.  Equality occurs
at exactly seven positions:

| deleted position | exact holes afterward |
|---:|:---|
| `0` | `0xa86d,0xa879,0xa87d,0xac6d` |
| `1` | `0x286d,0x2c6d,0xa879,0xa87d` |
| `6435` | `0x4e61,0x4e63,0xa879,0xa87d` |
| `6438` | `0x4879,0x6879,0xc879,0xe879` |
| `6439` | `0x2879,0x287d,0xa879,0xa87d` |
| `12870` | `0x8ce6,0x9ce6,0xa879,0xa87d` |
| `12873` | `0xa879,0xa87d,0xce61,0xce63` |

The full hole-count histogram is

```text
4:7  5:5  6:181  7:930  8:1636  9:1895  10:1990  11:1656
12:1132  13:773  14:636  15:741  16:499  17:366  18:190
19:176  20:3  21:58.
```

Thus width-one shrinkage is rigorously excluded, and widths at least two are
the first nontrivial contiguous replacement class.

The solver-free checker is

```text
scratch/audit_r_k16_ripple_a62cb_direct_deletion_20260730.py
SHA-256 2a58c31a210b89d3fcb4378f36a0e2f5df75faf99b706f73bdaddef4bf400fd7
```

It checks the multiplicity formula and then independently replays the seven
equality words literally.

## 3. Exact block theorem

Fix an original interval `[lo,hi)` of width `b`.  Let `L=W[:lo]` and
`R=W[hi:]`.  Replace the original block by an arbitrary nonzero word `Y` of
length

\[
                         |Y|=b-\delta,
\qquad \delta\in\{0,1\}.                         \tag{3.1}
\]

Here `delta=0` seeks a universal word of length `12874`; `delta=1` seeks the
optimal length `12873`.

### Theorem 3.1 (exact suffix/subinterval/prefix reduction)

The candidate `L|Y|R` is universal if and only if every target not already
covered wholly inside `L` or wholly inside `R` has a representation

\[
 t=\ell\vee\left(\bigvee_{i=a}^{c}Y_i\right)\vee r,            \tag{3.2}
\]

where `0<=a<=c<|Y|`, `ell=0` unless `a=0`, in which case `ell` may be any
suffix OR of `L`, and `r=0` unless `c=|Y|-1`, in which case `r` may be any
prefix OR of `R`.

#### Proof

An interval avoiding `Y` lies wholly in exactly one of the two fixed sides.
An interval meeting `Y` meets one nonempty consecutive subinterval
`Y[a:c+1]`.  It can extend into `L` precisely when `a=0`, and that extension
is a suffix; similarly it can extend into `R` precisely when `c=|Y|-1`, and
that extension is a prefix.  These cases are disjoint and exhaustive.
Conversely every form (3.2) is a literal interval of `L|Y|R`.  QED.

For a fixed form and target `t`, its Boolean encoding is exact: every variable
cell in the subinterval is forbidden from using a bit outside `t`, while each
bit of `t` absent from the fixed mask `ell|r` must occur in at least one of
those cells.  A disjunction over all forms implements (3.2).  Each variable
cell also has a nonzero clause.

The production implementation is

```text
scratch/search_r_k16_ripple_a62cb_shrink1_block_csp_20260730.py
SHA-256 3d2f23416afe45545f5fc7159775e6aded31cfeac3fb56866d0696f7a1b9cec2
```

Despite its historical filename, version 2 accepts both `--shrink-by 0` and
`--shrink-by 1`.  It is H100-only, forces one CP-SAT worker, enforces an
address-space cap no larger than `2048 MiB`, treats `UNKNOWN` separately from
`INFEASIBLE`, and writes a PASS only after two literal interval replays agree
on `65535/65535` coverage.  A PASS also requires a fresh `--output-word`.

An implementation-independent three-bit audit reconstructs (3.2) naively and
checks both shrink modes on `23,016` complete nonzero assignments and
`161,112` target instances:

```text
scratch/audit_r_k16_ripple_shrink1_block_encoding_logic_20260730.py
SHA-256 62c7f72d552c6b88371391d021579c6fefed56138b6c26932a74bbdac990f826
status PASS_EXACT_FORM_EQUIVALENCE.
```

## 4. H100 preflight sizes, centered at 6440

No solve was launched in this lane.  One-CPU, `2048 MiB`-capped preflights
successfully built every width `2,...,16` model.

For the optimal-length mode `delta=1`, the width-16 model has

```text
replacement cells       15
residual targets         54
variables              7215
constraints          375439
reified witnesses      6975.
```

For the immediate-upper-bound mode `delta=0`, the width-16 model has

```text
replacement cells       16
residual targets         54
variables              8128
constraints          445054
reified witnesses      7872.
```

All fifteen models in either mode built in under eleven wall seconds.  These
are proto sizes before solving, not performance promises.

The coordinated equal-length run command is

```bash
cd /dev/shm/r_k16_ripple_shrink1_20260730
env OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 \
    MKL_NUM_THREADS=1 NUMEXPR_NUM_THREADS=1 \
nice -n 15 taskset -c FREE_CPU timeout 600 \
python3 search_r_k16_ripple_a62cb_shrink1_block_csp_20260730.py \
  --word k16_ripple_insert12874_onehole.word \
  --center 6440 --min-width 2 --max-width 16 --width-step 1 \
  --shrink-by 0 --seconds-per-width 30 --address-space-mb 2048 \
  --output equal_w2_16_solve.json \
  --output-word equal_w2_16_candidate.word \
  > equal_w2_16_solve.log 2>&1
```

Change only `--shrink-by 0` to `1`, and use fresh output names, for the
optimal-length branch.  The outer timeout permits at most fifteen 30-second
width attempts plus model construction.

## 5. Exact scope

An `INFEASIBLE` width result excludes exactly one centered contiguous
replacement of that original width with the complement frozen.  It does not
exclude:

* a block with a different center;
* two separated blocks;
* a deletion plus a nonlocal replacement;
* a permutation/rethreading of a larger carrier; or
* an unrelated K16 word.

Conversely, a SAT assignment is already a literal word candidate and must be
promoted only after the fresh exported word passes the repository verifier.
