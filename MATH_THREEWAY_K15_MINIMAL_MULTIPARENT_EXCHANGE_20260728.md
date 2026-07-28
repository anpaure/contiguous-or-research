# The minimal genuine multiparent exchange at `k=15`

Date: 2026-07-28

This note is relative to the five frozen canonical parents `P0,...,P4` in
`MATHEMATICAL_HANDOFF.md`, Section 335.  It proves a small-support normal
form, gives an exact finite certificate criterion, and records an exhaustive
census.  It does **not** quantify over carriers outside this five-parent
directed atlas.

## 1. Relative transfer graph and the correct notion of multiparent

Close every parent path through the common dummy vertex.  Let `f_0` be the
successor cycle of `P0`, and put

\[
 \rho_a=f_0^{-1}f_a\qquad(1\le a\le4).
\]

For a possible transferred head define the exact source-label set

\[
 L(x,y)=\{a\in\{1,2,3,4\}:\rho_a(x)=y\}.
\tag{1.1}
\]

Every exact successor factor is uniquely `f_0 p`, where `p` is a
permutation and `p(x)` belongs to the transfer choices at `x`.  For a
nontrivial transfer with support `S`, define

\[
 I(p)=\bigcap_{x\in S}L(x,p(x)).
\tag{1.2}
\]

Then

\[
 I(p)\ne\varnothing
 \iff f_0p\text{ is contained in }P0\cup Pa
      \text{ for some one donor }a.
\tag{1.3}
\]

Thus the exact intrinsic multiparent condition is `I(p)=empty`.  It is
strictly weaker than requiring an individually rainbow cycle of `p`.
Several cycles can each be parent-pure but pure in incompatible parents;
their product is intrinsically multiparent.  The exhaustive code uses the
bitwise AND of **all changed-edge source masks**, so it includes this case.

## 2. Complete small-support classification

Let `S=supp(p)`, `s=|S|`, and let `alpha` be the cyclic order induced on
`S` by the base cycle `f_0`.

### Theorem 2.1 (monodromy and parity)

The child `f_0p` is Hamilton if and only if `p alpha` is one cycle on `S`.
In particular `p` is even.  For `3<=s<=8`, the only possible derangement
cycle types are

\[
\begin{array}{c|c}
s&\text{even transfer types}\\ \hline
3&3\\
4&2+2\\
5&5\\
6&3+3,\ 4+2\\
7&7,\ 3+2+2\\
8&6+2,\ 5+3,\ 4+4,\ 2+2+2+2.
\end{array}
\tag{2.1}
\]

For `s=3`, exactly the forward 3-cycle in the physical cut order is
Hamilton.  For `s=4`, exactly the crossing pair of transpositions is
Hamilton.

#### Proof

Cut the base arcs at `S`.  The unchanged segments are indexed by `S`, their
base transition is `alpha`, and the new transition is `p alpha`.  This proves
the first assertion.  Since `f_0` and `f_0p` are cycles of the same length,
they have the same sign, so `p` is even.  A derangement with cycle lengths
`lambda_1,...,lambda_c` has sign `(-1)^(s-c)`.  Listing the partitions of
`s<=8` with all parts at least two and `s-c` even gives (2.1).

For three cut points, the forward cycle gives `alpha^2`, while the reverse
cycle gives the identity.  For four cut points the only even derangements
are double transpositions; the cut-segment test, equivalently the nonsingular
two-chord intersection matrix, retains only the crossing pairing.  \(\square\)

This theorem proves completeness of the finite type list.  A search over
only forward `C6` atoms is not complete at support six: reverse or
parent-pure 3-cycles can become Hamilton when correlated with another
3-cycle.

## 3. Exact local legality and Hall certificate

Suppose `p` changes the successor arcs at `S`.

1. The new path is obtained by traversing `f_0p` from the dummy.  The
   monodromy theorem and this literal traversal are checked independently.
2. Since the base is residence-safe, any new forbidden residence word of
   two through four arcs contains a changed arc.  It is therefore enough,
   and necessary, to inspect the starts lying at most three new-predecessor
   steps before each member of `S`.  A full-path scan is performed on every
   survivor as an independent check.
3. A changed upper `q`-window contains a changed arc.  The signed old/new
   window ledger therefore consists exactly of the starts lying at most
   `q-1` predecessor steps before `S`, for `1<=q<=7`.  The implementation
   also reconstructs the full path and checks every upper target directly.
4. For every local survivor, the exact depth-three compiler graph is passed
   to `fast_k15_hall_dm`.  A claimed deficiency `delta` has both sides:
   a matching of size `16383-delta`, and the canonical alternating DM shore
   with `|A|-|N(A)|=delta`.  Thus the score is exact, not a frozen-shore
   projection.

This is also a finite positive certificate criterion: a record consisting of
the transfer cycles, a one-cycle trace, zero residence witnesses, one literal
upper witness per target, a compiler matching, and an equal-size vertex
cover proves every required condition without trusting the search.

## 4. Exhaustive five-parent census

The intrinsic multiparent results are:

| type | intrinsic | Hamilton | residence-safe | all-upper | exact Hall deficiencies |
|---|---:|---:|---:|---:|---|
| `3` | 68 | 29 | 0 | 0 | -- |
| `2+2` | 231999 | 82742 | 51 | 24 | `34:2,35:9,36:6,37:5,38:1,39:1` |
| `5` | 186 | 58 | 0 | 0 | -- |
| `3+3` | 62658 | 18761 | 244 | 48 | `29:13,30:8,31:2,32:1,33:18,34:3,35:1,37:2` |
| `4+2` | 204235 | 54366 | 61 | 35 | `32:2,33:8,34:8,35:10,36:5,37:2` |
| `7` | 736 | 168 | 0 | 0 | -- |
| `3+2+2` | 123113563 | 30445049 | 2452 | 746 | `33:2,34:58,35:192,36:178,37:121,38:67,39:56,40:41,41:20,42:9,43:2` |

Consequently no intrinsic multiparent transfer of support at most seven
improves the Hall-29 carrier in the canonical five-parent atlas.

The broadened parent-pure audit through support six gives:

| type | all-upper resident | exact Hall deficiencies |
|---|---:|---|
| `3` | 13 | `29:8,30:2,33:3` |
| `2+2` | 26 | `34:4,35:11,36:5,37:5,38:1` |
| `5` | 0 | -- |
| `3+3` | 41 | `29:20,30:7,31:1,33:8,34:3,35:1,37:1` |
| `4+2` | 20 | `32:3,33:2,34:7,35:2,36:3,37:1,38:2` |

Thus **all** Hamilton/residence/all-upper transfers through support six,
whether intrinsic or parent-pure, fail to improve Hall 29.  Parent-pure
support seven is a separate finite audit and is not claimed by this table.

The support-three result is especially sharp: the atlas has 29 intrinsic
Hamilton rainbow `C6` atoms and all 29 violate residence.  Moreover each
has a private bad residence path untouched by every disjoint forward-rainbow
`C6` companion.  The complete `3+3` census above is stronger than that
restricted deck statement because it also includes reverse and parent-pure
3-cycles.

## 5. Reproduction and frozen evidence

Primary enumerator:

```text
scratch/enumerate_k15_intrinsic_multiparent_support3_7.cpp
SHA-256 317219cf064045ec47dbd75d964e85537a1fda7dc0ef2c824f19eb0267001f54
```

Exact compiler engine:

```text
scratch/fast_k15_hall_dm.cpp
SHA-256 366f289028738151f13e7d59196610c1cbad7f5bacc64c4c29d20a9346d7c979
```

Compact intrinsic audit (all 853 locally legal paths, their transfer parts,
path hashes, and exact Hall scores):

```text
scratch/k15_intrinsic_multiparent_support3_7_compact_audit.json
SHA-256 2854ff10ac29f08565d814ea2e35260840a36bee531c5e9dbe738600d52b1bc4
```

Parent-pure-through-six audit:

```text
scratch/k15_parent_pure_support_le6_compact_audit.json
SHA-256 b6f28030b09436bb073610c4554b7977e34e9e342c1ac2fb9648c200b5805838
```

Build and intrinsic run:

```text
c++ -O3 -march=native -DNDEBUG -std=c++20 \
  scratch/enumerate_k15_intrinsic_multiparent_support3_7.cpp \
  -o scratch/enumerate_k15_intrinsic_multiparent_support3_7

scratch/enumerate_k15_intrinsic_multiparent_support3_7 \
  scratch/k15_doubletrans_05_213_hall29.json \
  scratch/k15_outer2_p1_h30_bridge.json \
  scratch/k15_trans1113_balanced_hall31.json \
  scratch/k15_transposition_parent_winner.json \
  scratch/k15_accumulated_zero_parent_winner.json OUT

python3 scratch/fast_k15_hall_dm_cli.py OUT/candidate_*.json \
  --output OUT/hall.jsonl
```

For the broadened audit, append

```text
--max-support=6 --include-parent-pure
```

The compact audits also freeze the SHA-256 hashes of all five parent inputs.

## 6. Consequence and next exact size

The pair no-go theorems established that a terminal carrier cannot lie in
one canonical two-parent union.  The present census says more locally:
small multiparent surgery cannot even improve the exact Hall score.  The
first unresolved arbitrary-improvement size is support seven until its
parent-pure half is scored; after that, support eight has exactly the four
types

\[
 6+2,\qquad5+3,\qquad4+4,\qquad2+2+2+2.
\]

The last type should be enumerated through the exact mod-two chord criterion

\[
 a_{12}a_{34}+a_{13}a_{24}+a_{14}a_{23}=1,
\tag{6.1}
\]

where `a_ij` says that transposition chords `i,j` interlace in the base
order.  Equation (6.1) is the nonsingularity condition for the four-chord
intersection matrix and avoids treating all `binom(818,4)` quadruples as
Hamilton candidates.
