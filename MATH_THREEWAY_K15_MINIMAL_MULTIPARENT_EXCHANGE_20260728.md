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

## 7. Exact four-chord reduction

The support-eight `2+2+2+2` case has a stronger normal form. Number the
four transposition chords and let `a_ij` be one when chords `i,j` interlace
in the base cyclic order.

### Theorem 7.1 (odd crossing-split theorem)

The four-transposition transfer is Hamilton if and only if

\[
 a_{12}a_{34}+a_{13}a_{24}+a_{14}a_{23}=1\pmod2.
\tag{7.1}
\]

Consequently an odd number of the three splits of the four chords into two
pairs have both pairs crossing. In particular every Hamilton four-chord
deck has a decomposition into two support-four Hamilton kernels.

#### Proof

For a product of transpositions, the exact circuit formula is

\[
 c(f_0p)=1+\operatorname{nullity}_{\mathbf F_2} A,
\]

where `A=(a_ij)` is the symmetric zero-diagonal chord-intersection matrix.
Thus Hamiltonity is equivalent to nonsingularity. In characteristic two,
the determinant of a `4x4` alternating matrix is the square of its
Pfaffian, and squaring is the identity. Its Pfaffian is exactly the left
side of (7.1). Each product in (7.1) records one split into two crossing
pairs. \(\square\)

There are `105` perfect matchings on eight cyclic positions. Exact abstract
enumeration gives the component-count histogram

\[
 \{1:21,\ 3:70,\ 5:14\}.
\tag{7.2}
\]

Thus only 21 ordered chord diagrams need be physically embedded.

### Theorem 7.2 (mutual residence-rescue criterion)

Let `A` be one crossing-pair kernel. Evaluate its partial transfer and, for
each resulting forbidden residence word, let `R` be the set of tails in
that word which are outside `supp(A)` and occur in at least one available
transposition. Delete supersets and call the remaining family
`cal R(A)`.

If a disjoint crossing-pair kernel `B` completes `A` to a residence-safe
four-chord deck, then

\[
 \operatorname{supp}(B)\cap R\ne\varnothing
 \qquad(R\in\mathcal R(A)),
\tag{7.3}
\]

and symmetrically with `A,B` reversed. An empty `R` proves that `A` has no
completion. Conversely, after (7.3), literal evaluation of the combined
eight-tail transfer is necessary and sufficient.

#### Proof

If no outgoing arc at a tail of a bad partial word is changed by `B`, every
arc of that word survives in the combined transfer, so the residence defect
survives. This proves necessity and the empty-clause obstruction. Once the
supports are fixed, direct evaluation is the definition of residence and is
therefore sufficient. \(\square\)

For each of the 21 abstract diagrams, the four positions of `B` lie in four
literal open intervals cut out by the four sorted positions of `A`. Hence
the complete enumeration is a four-dimensional orthogonal range join of
crossing-pair kernels, restricted by the two hitting systems (7.3). This is
an exact indexed join, not a sample from the `18,518,759,260` raw
four-transposition subsets.

The frozen run gives:

```text
crossing-pair kernels            118600
impossible partial kernels       114918
indexed kernels                    3682
pattern-box joins                 45614
mutual-rescue joins                1638
intrinsic candidates               1523
parent-pure candidates              115
intrinsic all-upper/resident         483
parent-pure all-upper/resident        103
```

All 1,523 intrinsic candidates are componentwise parent-pure but globally
incompatible: each transposition has a donor, yet no one donor supplies all
four. This is exactly the case that an “at least one rainbow component”
filter would incorrectly delete.

## 8. The all-shore Hall-delta identity

Let `G_0` be the compiler graph of `P0`, with deficiency `delta_0=29`, and
let `G_Q` be the graph after any transfer. For a target shore `A` put

\[
 g_0(A)=|A|-|N_0(A)|,\qquad
 s_0(A)=29-g_0(A)\ge0,
\]

and

\[
 \Delta_Q(A)=|N_Q(A)|-|N_0(A)|.
\]

### Theorem 8.1 (exact moving-shore gain)

\[
 \boxed{\mu(G_Q)-\mu(G_0)
   =\min_{A\subseteq\mathcal T}\bigl(s_0(A)+\Delta_Q(A)\bigr).}
\tag{8.1}
\]

Therefore `Q` improves Hall 29 if and only if

\[
 s_0(A)+\Delta_Q(A)\ge1
 \qquad\text{for every target shore }A.
\tag{8.2}
\]

#### Proof

Hall's deficiency formula gives

\[
 \delta(Q)=\max_A\{g_0(A)-\Delta_Q(A)\}.
\]

Since matching size is `|T|-delta`, subtract from `delta_0=29` and move the
maximum through the minus sign. \(\square\)

This identity says exactly why passing the five displayed private shores is
only a filter. A transfer can move the minimizing shore. An exact positive
certificate is either the universal inequality (8.2), or, finitely, a
matching of size at least 16,355 together with the usual maximum-matching
audit. For a fixed old maximum matching `M_0`, if `r` of its edges are
destroyed and `alpha` is the maximum number of augmenting paths from the
retained matching in `G_Q`, then the same gain is

\[
 \mu(G_Q)-\mu(G_0)=\alpha-r.
\tag{8.3}
\]

Thus a four-chord candidate must provide at least `r+1` compatible
augmentations; raw new-cell count is not enough.

## 9. Exact support-eight outcome

All four parity-legal support-eight types have now been exhausted, including
parent-pure candidates:

| type | locally legal | best exact Hall deficiency |
|---|---:|---:|
| `6+2` | 0 | -- |
| `5+3` | 0 | -- |
| `4+4` | 3 | 34 |
| intrinsic `2+2+2+2` | 483 | 39 |
| parent-pure `2+2+2+2` | 103 | 40 |

The full four-chord deficiency histograms are

```text
intrinsic:   39:5,40:33,41:87,42:124,43:115,44:77,45:29,46:12,47:1
parent-pure: 40:6,41:21,42:32,43:24,44:14,45:4,46:2
```

Hence no Hamilton, residence-safe, all-upper intrinsic transfer of support
at most eight in the canonical five-parent atlas lowers Hall below 29. Once
the separate parent-pure support-seven audit is included, the same statement
holds for every transfer through support eight. Without that last audit, the
logically unconditional statement is: intrinsic transfers are closed
through eight and all transfers are closed through six.

The support-eight enumerator and compact audit are

```text
scratch/enumerate_k15_intrinsic_multiparent_support3_8.cpp
SHA-256 722731a8fdc51b4c3924be165e9a83d59f6e07da8dd3191bab75e460aa2d2d94

scratch/k15_support8_all_types_compact_audit.json
SHA-256 b81846ac94d7ef910a73dd75464678cd5c2e3f4486b964c5e8d8e5c16d65c88d
```
