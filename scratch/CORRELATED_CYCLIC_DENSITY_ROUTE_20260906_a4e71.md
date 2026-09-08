# Correlated Width-Period Words: Full-Rank Search and Annular Tests

Date: 2026-09-06. Unique scratch work, suffix `a4e71`.

## Status

**This is an explicitly tested correlated construction route, not a proof of
coefficient one or an improvement of the universal asymptotic constant.**

The positive output consists of actual width-period cyclic set-words, an
exact simultaneous-rank objective including every seam, independently checked
finite inventories through dimension 23, and exact off-middle covers in two
smaller dimensions. There is no asserted growing-rank matching theorem.

In particular, the new large finite words have:

| Dimension | Actual Cyclic Period | Actual Nonempty Holes | Hole Density | Holes / Width |
|---:|---:|---:|---:|---:|
| 19 | 92,378 | 45,277 | 0.0863591 | 0.490128 |
| 21 | 352,716 | 213,860 | 0.101977 | 0.606324 |
| 23 | 1,352,078 | 1,097,123 | 0.130788 | 0.811435 |

Every period in the table is exactly `W(k)`. The increasing finite hole
densities do **not** establish a vanishing-density trend. Nor does observing
`h<W(k)` in these three cases establish an asymptotic `O(W(k))` bound.

The direction was chosen after checking `MASTER_HANDOFF.md`, I.3A and I.7,
the cylinder-completion theorem, the seam-inclusive independent-relabeling
barrier, the Gaussian packet-energy and paired-row-rounding notes, and the
existing GK/MTF and growing-rank matching obstructions. The construction below
does not assume that independently sampled blocks cover almost everything,
that central exactness supplies deeper ranks, or that a chain matching is
automatically a literal word.

## 1. One Coupled Word

Let `k=2m+1>=3`, and let `rho` cyclically permute the `k` ground coordinates.
Choose an ordered seed of nonempty masks

\[
 S=(S_0,\ldots,S_{L-1}),\qquad
 L=\operatorname{Cat}_m=\frac1k\binom{k}{m}.
\]

Its literal cyclic development is

\[
 A(S)=S,\rho S,\ldots,\rho^{k-1}S.                 \tag{1}
\]

The specified cyclic period has exactly `kL=W(k)` letters. A smaller
fundamental period is harmless. Since the seed is nonempty, the union of
the developed word is the whole ground set. No derivative compiler,
unpaid collar, designated-start restriction, or fragment serialization is
used. All intervals of lengths one through `kL` are allowed.

Changing one seed entry changes all its rotated copies together. These
blocks are not independently relabelled. Their common seed is optimized
using the inventory of the complete word, including intervals crossing one
or several presentation seams. Thus the independent-block obstruction is
not applicable to this coupling.

The already proved cyclic normalization gives a linear word of length at
most `W(k)+k-2` preserving all these targets. Computational warm-up passes
used below are not physical letters of the output.

This includes the handoff's `k=7` seed and its 12-hole `k=9` seed, but does
not claim an inductive composition of either fixed seed. The larger searches
start from fresh singleton seeds and then allow general nonempty masks.

## 2. Exact Simultaneous Inventory

For a right endpoint `j`, let `P_j` be the strictly increasing chain of
distinct nonempty unions of cyclic intervals ending at `j`. Its update is

\[
 F_X(P)=\{X\}\cup\{Y\cup X:Y\in P\},              \tag{2}
\]

with duplicate sets removed. The output remains an inclusion chain, so it
has at most `k` members. This is the literal suffix-union recurrence, not
a permutation update which improperly separates simultaneous occurrences.

### Finite Forgetting

After reading any full developed period, (2) is independent of every
earlier suffix profile. Indeed, a suffix reaching farther back contains the
whole period and hence has union `[k]`; that target is already supplied by
the period itself. All shorter suffixes depend only on the period.

Consequently the cyclic profile system is unique. It can be computed by
warming up for one period and reading another, without imposing a witness
length cutoff. Equivariance gives

\[
 P_{j+L}=\rho P_j.                                    \tag{3}
\]

The search stores only the `L` profiles in the seed frame. On crossing the
end of that frame, it applies `rho^{-1}` to the carried profile before
processing the next unrotated seed letter.

Let `c(T)` be the least integer mask in the coordinate-rotation orbit of
`T`, let `R` be the set of its nonempty orbit representatives, and let
`o(T)` be the size of that orbit. Define

\[
 a(T)=\sum_{0\le j<L}
       \mathbf 1\{\text{some }Y\in P_j\text{ has }c(Y)=T\}.
                                                               \tag{4}
\]

Two distinct members of one profile have different cardinalities. They
cannot belong to the same coordinate orbit, so the implementation may
equivalently count profile members in (4).

### Exact Hole Formula

\[
 \boxed{h(A(S))=\sum_{T\in R}o(T)\mathbf 1_{\{a(T)=0\}}.}          \tag{5}
\]

**Proof.** By (3), the inventories in the remaining seed blocks are exactly
the rotations of the stored profiles. An orbit is therefore present in the
whole word if and only if it meets a stored profile. In that case its entire
orbit is present. Summing the absent orbit sizes proves (5).

In particular, at composite dimensions such as 21, a short orbit is not
mistakenly counted as 21 targets. Formula (5) uses one actual word and all
ranks at once. It does not combine separate rankwise optimizers.

## 3. Joint Literal Repairs

The search includes ordinary bit edits and exchanges, but also the following
joint interval operation. It is useful because a coordinate may need to be
removed from several letters of the same old witness simultaneously.

Let an old interval contain letters `A_1,...,A_d`, with union `U`, and let
`T` be any nonempty desired target. Choose one owner position `q`. First put

\[
 B_j=A_j\cap T\quad(j\ne q),\qquad
 B_q=(A_q\cap T)\cup(T\setminus U).                    \tag{6}
\]

Replace every empty `B_j` by any fixed singleton contained in `T`. Then

\[
                   \bigcup_{j=1}^d B_j=T.              \tag{7}
\]

**Proof.** Before replacing empties, the union in (6) is
`(U intersect T) union (T minus U)=T`. Replacing empty letters by subsets
of `T` neither removes a positive coordinate nor introduces a negative one.
Every resulting letter is nonempty, proving (7).

For (1), use an interval of length at most `L`, so its positions have
distinct seed indices. Translate each edited letter back to the seed frame,
then develop all the edits together. The chosen interval realizes `T`, and
its translated intervals realize every member of its rotation orbit.
The code further limits the chosen interval to length at most `k` for search
cost, not for coverage verification.

This is not a no-loss lemma. Other targets can disappear; their loss is
computed exactly by (5). The elementary operation closes its literal
coinstantiation question, not its global augmentation question.

### Exact Incremental Evaluation

After changing seed letters, propagate (2) from the first changed seed
index. Continue past the last directly changed index. Stop when the next
profile equals its stored value. At that point the remaining recurrence is
unchanged, so every stored profile is consistent with the new word.

This stopping rule remains valid across the twisted seed seam. Initially
only directly changed letters break their recurrence equations. Updating a
profile can break only the next equation. Once all directly changed indices
have been processed, equality at the advancing boundary eliminates the last
possible break. Finite forgetting shows that after one developed period
and one extra seed sweep all profiles are the actual new cyclic profiles;
the code's `(k+2)L` update limit is therefore safe.

Old/new representative counts are subtracted and added exactly. If an
index is visited more than once, its intermediate differences telescope.
Rejecting a trial restores its original letters and profiles. No cached
short-window inventory is substituted for the full cyclic inventory.

## 4. What the Search Optimizes

The primary output criterion is the exact count (5). A secondary search
potential uses

\[
 \phi(0)=1,\qquad \phi(a)=0.06/a\ (a>0),\qquad
 E=\sum_{T\in R}\frac{o(T)}k\phi(a(T)).                \tag{8}
\]

The constant in (8) is a heuristic tie-breaking choice, not a theorem
constant. Simulated annealing accepts some increases of (8); the program
retains the best actual hole count encountered, with (8) breaking ties.
Every retained candidate is integral and has unchanged physical period.

The optional annular mode ignores specified middle ranks in (8) and first
minimizes their complement's actual hole count. It still computes and
reports the actual holes in **every** rank. Ignoring ranks in the objective
does not mean they have been covered or repaired.

No local-minimum theorem, approximation ratio, or monotone-augmentation
claim is made for this search. In particular, even the joint updates did
not improve the original `k=9` total of 12 holes in the tested runs.

## 5. Independently Checked Finite Words

The dependency-free checker contains the complete small seeds. Its full
word, last-occurrence audit gives:

| Dimension | Period | Holes | Nonzero Rank Deficits |
|---:|---:|---:|---|
| 7 | 35 | 0 | none; existing handoff seed |
| 9 | 126 | 12 | rank 5: 9; rank 6: 3; existing handoff seed |
| 11 | 462 | 77 | rank 4: 11; rank 5: 22; rank 6: 33; rank 7: 11 |
| 13 | 1,716 | 546 | rank 5: 39; rank 6: 182; rank 7: 247; rank 8: 78 |
| 19 | 92,378 | 45,277 | ranks 7--13: `171,4047,14136,16169,8721,1938,95` |
| 21 | 352,716 | 213,860 | ranks 7--15: `3,2037,26887,64806,68691,39151,10920,1302,63` |
| 23 | 1,352,078 | 1,097,123 | ranks 8--16: `1817,35719,164335,302795,314042,197202,68632,11983,598` |

All unlisted ranks have zero deficit. No claim of minimum possible hole
count is made. In particular, these are not improvements of the known
finite values of `nu(k)`.

The initial and final **actual** hole counts in the three large runs were:

| Dimension | Initial Holes | Final Holes | Attempted Proposal Slots |
|---:|---:|---:|---:|
| 19 | 139,251 | 45,277 | 36,000,000 |
| 21 | 555,470 | 213,860 | 60,000,000 |
| 23 | 2,206,666 | 1,097,123 | 64,000,000 |

Some proposal slots are skipped before evaluation. These counts are not
numbers of accepted edits or runtime-normalized comparisons.

### Annular Tests

At period `W(9)=126`, the seed

```
44 134 6 68 28 16 36 360 168 137 76 145 146 10
```

has exactly 135 holes, all in the two middle ranks: 72 four-sets and 63
five-sets. Every other nonempty target is realized.

A 132-letter seed in the checker gives the same exact off-middle property
at `k=13`, period 1,716. Its only holes are 1,027 six-sets and 923
seven-sets, totaling 1,950. This is a worse total-hole count than the
all-rank seed, but a successful finite test of allowing the middle ranks
to absorb the entire deficiency.

The corresponding `k=19` test did **not** close: after 30,000,000 proposal
slots it had 7,847 off-middle holes, plus 37,031 rank-nine and 36,613
rank-ten holes. Its total 81,491 is also worse than the all-rank run.
Thus removing the middle objective alone is not an established scalable
solution.

## 6. Exact-Width Nine: Do Not Impose Short Witnesses Silently

The separate Z3 experiment tests an exact universal 14-letter seed at
`k=9`. It must distinguish a genuinely complete model from a convenient
short-window restriction.

Here are two exact facts used to make that distinction.

### Adjacent Width Ranks Have Consecutive Witness Lengths

Suppose a width-period cycle covers every target in two adjacent ranks
`r,r+1`, both of size equal to its period. By the fixed-length rigidity
proved in the handoff, their windows enumerate those ranks at lengths `p`
and `q`, respectively. Then

\[
                              q=p+1.                  \tag{9}
\]

**Proof.** Necessarily `q>p`: every interval of length at most `p` lies in a
rank-`r` window. Every `(p+1)`-window contains two distinct consecutive
rank-`r` windows, so has union size at least `r+1`. If `q>=p+2`, a
`(p+1)`-window fits in two consecutive `q`-windows. Its union must equal
both of their rank-`r+1` unions. This contradicts their distinctness.

For nine coordinates, the lower-rank count below rank four is
`9+36+84=129>126`. The handoff's cyclic-width bounds therefore force
`p in {3,4}`. By (9), the only pairs are `(3,4)` and `(4,5)`.

### A Safe Upper Witness Bound

If length-`q` windows enumerate rank `r` once, an interval of union rank
`s>=r` and length `d>=q` contains `d-q+1` distinct `r`-sets. Hence

\[
                       d\le q+\binom{s}{r}-1.          \tag{10}
\]

This justifies the solver's upper-rank witness bounds without asserting that
all targets have witnesses of length at most nine. Fixing the first seed
letter to `{0}` loses no universal developed seed: a universal word has a
singleton letter, and time rotation followed by a coordinate rotation puts
it there while preserving `A_{j+14}=rho(A_j)`.

The model with cap 126 therefore considers all literal witness lengths for
the coordinate-developed architecture and the specified pair in (9).
Observed solver results were:

| Middle Lengths | Additional Window Restriction | Solver Result |
|---|---|---|
| `(3,4)` | every 9-window is full | UNSAT |
| `(4,5)` | every 9-window is full | UNSAT |
| `(3,4)` | none beyond one full period | UNKNOWN, 240-second timeout |
| `(4,5)` | none beyond one full period | UNKNOWN, 240-second timeout |

The UNSAT rows are reported solver outcomes; no independent UNSAT proof
certificate is supplied. The singleton `(4,5)` cap-nine case is also
elementarily impossible: every nine singleton positions would be a
permutation, forcing period nine and repeated middle windows.
There is **no** claim that a universal width-period nine-coordinate word,
or even an unrestricted developed seed of that period, is impossible.

## 7. Verification and Replay

New scratch files only:

- `correlated_cyclic_density_20260906_a4e71.cpp`: integral search and exact profile updates.
- `correlated_cyclic_density_check_20260906_a4e71.py`: independent full-word audit and small certificates.
- `correlated_cyclic_exact9_20260906_a4e71.py`: explicitly scoped optional Z3 search.

Compile the C++ file with `clang++ -O3 -std=c++17 -Wall -Wextra -Wpedantic`.
The `--test` mode passed 3,535 small base cases and 28,280 trial mutations,
including whole-seed changes, cyclic seams, accept/reject restoration,
short coordinate orbits, and omitted middle ranks. It compares incremental
counts against fresh computations and exhaustive literal cyclic intervals.
The same suite also passed with AddressSanitizer and UndefinedBehaviorSanitizer.

Run the independent small certificates with:

```sh
python3 -B scratch/correlated_cyclic_density_check_20260906_a4e71.py
```

All six stored certificates passed both explicit last-occurrence grouping
and exhaustive enumeration of every cyclic interval. The large runs were
replayed with emitted seeds and audited independently, not merely checked
against a second copy of the incremental routine.

The large replay parameters are:

| Dimension | Steps Per Round | Rounds | RNG Seed |
|---:|---:|---:|---:|
| 19 | 3,000,000 | 12 | 9,064,474 |
| 21 | 5,000,000 | 12 | 9,064,475 |
| 23 | 8,000,000 | 8 | 9,064,476 |

Pass the compiled executable to the checker's `--binary` option, together
with `--k`, `--steps`, `--rounds`, and `--seed` from that table. The checker
captures the seed in memory, expands the actual whole word, and computes
its last-occurrence groups at every endpoint. It does not use coordinate
orbit compression, a witness-length cutoff, or the C++ profile cache.
No certificate-output files are created by either program.

SHA-256 of the developed words, encoded as unsigned 32-bit little-endian
masks with no header:

```
k19 9bc6fea45c8090f75caca1585bc847b9a4bd885c35143a2737400b09a4bc367e
k21 a4b1629547bc501c001722adecd84f5000fc076faf3f226520ce8d05c10c22e6
k23 2a25acfff11aeac6d2c6a29d27aec17f0f1775f00c5e523dab343ddaa207694c
```

The search uses floating-point annealing decisions. The independent integer
inventory, rather than the annealing trajectory, is the finite mathematical
certificate; another platform may produce a different trajectory. Complete
small seeds are embedded directly. The large words are retained here as
replay recipes plus hashes, not as an asserted platform-independent search
theorem.

For the optional exact-nine model, use Z3 and pass `--window-cap 9` for the
restricted version. The default cap is 126. The complete tested models use
`--timeout 240` and either default depths or
`--depth-four 4 --depth-five 5`. A timeout is not a nonexistence result.

## 8. The Unproved Step

The cylinder theorem says that a growing family of these words with
`h=O(W(k))` would suffice: after `Theta(k^(2/3))` new coordinates, the
relative error is `O(k^(-1/3))`. More generally, `h=o(2^k)` suffices.
That theorem is already proved in the cited handoff and is not new here.

What is missing is an unbounded-dimension control on this **integral**
search or another selection of its seeds. We have not proved that joint
interval edits continue to improve until `h=o(2^k)`, that all local optima
have that property, or that the best developed seed does. The finite table
does not fill this gap. The executable itself deliberately uses dense
32-bit-mask tables and is capped at dimension 24.

The useful change from independent packet sampling is concrete: there is
one mutable cyclic word, one exact all-rank objective, legal joint edits
which can force a chosen missing orbit, and tested width-period outputs
well beyond the supplied `k=7,k=9` examples. There is no remaining
literalization or seam-accounting assumption for those outputs.
The unresolved question is global improvement and its asymptotic rate.

No constant improvement for universal words, no coefficient-one theorem,
and no scalable finite-seed composition should be inferred from this note.
