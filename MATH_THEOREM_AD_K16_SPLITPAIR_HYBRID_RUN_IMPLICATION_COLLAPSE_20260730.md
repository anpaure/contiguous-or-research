# AD theorem: the five large split-pair hybrid lattices collapse to their endpoints

Date: 2026-07-30  
Status: **proved, solver-free, exact for the ordered-occurrence hybrid model**

## 1. Result

Let `A` and `B` be two of the eight authenticated split-pair chronologies,
and pair equal-mask occurrences in increasing occurrence order, exactly as in

```text
scratch/search_k16_splitpair_hybrid_lattice_20260730.cpp
```

The resulting assignment permutation on the 12,873 physical positions has
cycles `C_0,...,C_(c-1)`.  For `z in {0,1}^c`, form the hybrid `H(z)` by
taking the `B` assignment at every position of `C_j` when `z_j=1`, and the
`A` assignment there when `z_j=0`.

### Theorem 1.1 (large-lattice collapse)

For each of the five pairs

```text
(151,282), (155,282), (178,282), (231,282), (233,282),
```

and every `z` other than the all-zero and all-one vectors, `H(z)` is not an
exact generalized `COMP3` middle chronology.  More precisely, the affine
coordinate traces of `H(z)` contain an interior positive run of length one,
two, or three in the honest depth-three prefix.  If a hybrid creates an
additional adjacent equality first, it is already structurally invalid.

Consequently the complete `2^c` hybrid lattices for the five pairs contain no
new middle-exact word.  Upper coverage and Hall need not be evaluated.

For these eight authenticated endpoints this also closes every **unlabelled
pointwise `A/B` hybrid which preserves the row multiset**.  All masks are
unique except the three doubled masks `4e71,cc63,ce61`, and both copies of
each doubled mask occupy the same fixed positions in every endpoint.  The
unique-mask balance equations force a pointwise switch to be constant on
each canonical occurrence cycle; the six repeated positions are value-inert.

This closes exactly the five pairs whose cycle count exceeds 20.  Together
with the authenticated exhaustive endpoint-only result for the other 23
pairs, every unordered pair of the eight endpoints is now rigid in this
pointwise, multiset-preserving `A/B` class.  It does not close an operation
which uses a third parent, changes mask values, or is not pointwise `A/B`.

## 2. Authenticated inputs

The eight source words and SHA-256 hashes are

| ID | SHA-256 |
|---:|---|
| 151 | `a509899b9e331b4c0743b2a814707ea2d899586b35b9aba38605d31ea718b6a3` |
| 155 | `059600a7098beb9c01df1fa36ea973a7d1111591d71ae5e609a2aac6a2d07b4f` |
| 162 | `ad58f4f4f0039e44d811842dfaa65399f81a56f763fa0e4853102331fe80dac4` |
| 178 | `e0b2d3f0d5b68dfb699a36cc771d7412c6ddae2a9a4e57de02fd96276349e9e6` |
| 229 | `cae23cfcedbc9d193ebd9191045edd0e5c14f56af5fc96a802b8cefa7cd7e974` |
| 231 | `6dc7a62f632814e09a74b265d2b33737d5a3923cdf4ee71a796b4e149200c78d` |
| 233 | `ab6e72cf98a32efe9b66567ff1908239d291f1488d7d1e21c8d630566c66ef7d` |
| 282 | `e9dfecd67bf34bbc93ae54179d43e942f802e2ea28198d0024dd8c76da07e0f3` |

Every word has exact middle replay, zero maximal envelopes, and the same
three fixed flat pairs:

```text
positions 6320,6321     value 4e71
positions 12869,12870   value cc63
positions 12871,12872   value ce61.
```

The values, not merely the positions, agree in all eight words.  Hence every
hybrid retains these three flats.  The forced depth begins at three and is
decremented at every adjacent equality.  Any additional flat therefore gives
a fourth decrement and a negative depth, so such a hybrid is structurally
invalid.  In the absence of an additional flat, every row through position
6320 has depth three.

The exact all-28-pair cycle census verifies that the five pairs in Theorem
1.1 are precisely those with `c>20`.

## 3. Assignment cycles and affine coordinate traces

For each mask value `v`, list its positions in `A` and `B` in increasing
order and pair the `j`-th occurrence in `A` with the `j`-th occurrence in
`B`.  If `p` is a position in `B`, let `pi(p)` be its paired position in
`A`.  Then

\[
 B_p=A_{\pi(p)}.
\]

Thus `pi` is a permutation.  On a cycle `C` of `pi`, replacing all `A_p` by
all `B_p` merely permutes the masks occupying `C`.  Selecting any collection
of cycles therefore preserves the full row multiset exactly.

Fix a coordinate `b` and a position `p`.  Write `h_(p,b)(z)` for the `b`-bit
of `H(z)_p`.  If `p` belongs to cycle `C`, then

\[
h_{p,b}(z)\in\{0,1,z_C,1-z_C\}.
\]

Indeed it is constant when the two endpoint bits agree, equals `z_C` for
endpoint bits `(0,1)`, and equals `1-z_C` for endpoint bits `(1,0)`.  Fixed
points necessarily have `A_p=B_p`.

This is the exact per-cycle boundary ledger: every possible new coordinate
boundary is an affine literal in the one cycle bit owning that position.

### Lemma 3.1 (catalogue-specific unlabelled completeness)

For any two of the eight authenticated endpoints, let `Q_p` be chosen from
`{A_p,B_p}` at every position and suppose the multiset of rows of `Q` equals
the common endpoint multiset.  Then, up to choices at positions where
`A_p=B_p`, the set of positions using `B` is a union of the canonical cycles
of `pi`.

#### Proof

First suppose the mask `A_r` is unique.  It occurs in `Q` once.  It is kept
at position `r` exactly when `r` is not switched, and it is imported at the
unique position `p=pi^{-1}(r)` exactly when `p` is switched.  Therefore

\[
 (1-z_r)+z_{\pi^{-1}(r)}=1,
\]

so `z_r=z_(pi^{-1}(r))`.  Iterating makes `z` constant on every nontrivial
cycle containing unique masks.

The only repeated masks are `4e71,cc63,ce61`.  Their two occurrences occupy
the same six physical positions in every endpoint, so those positions are
fixed points and `A_p=B_p`; their switch labels do not change `Q`.  Hence no
repeated-mask balance equation can couple or split a nontrivial cycle.  This
proves the claim.  ∎

Thus a different labelling of the fixed duplicate occurrences adds no new
literal word in this catalogue.  This conclusion would be false for generic
equal-multiset words whose repeated occurrences move; Section 7 gives an
explicit counterexample.

## 4. The short-positive-run obstruction

Let `T_0,...,T_(N-1)` be a target chronology with depth `d_i=3` on the
relevant prefix.  Its maximal envelope at position `j` is

\[
 P_j=\bigcap_{i:\ i\le j\le i+d_i}T_i.
\]

In the interior depth-three prefix, for `3<=j<=6320`, this is simply

\[
 P_j=T_{j-3}\cap T_{j-2}\cap T_{j-1}\cap T_j.       \tag{4.1}
\]

### Lemma 4.1 (honest depth-three run obstruction)

Fix a coordinate `b`.  Suppose its target trace has

\[
0,\underbrace{1,\ldots,1}_{\ell},0                 \tag{4.2}
\]

on positions `s-1,...,s+ell`, where `1<=ell<=3`, `s>=3`, and

\[
s+\ell-1+3\le6320.                                  \tag{4.3}
\]

Then every positive row in this run fails maximal-envelope middle replay in
coordinate `b`.

#### Proof

Take a positive row `i` in the run and an envelope position
`j in [i,i+3]`.  The four consecutive target rows in (4.1) contain `i`.
They cannot lie wholly inside a positive run of at most three rows.  Since
the block is contiguous and contains `i`, leaving the run crosses one of its
two displayed zero boundary rows.  Hence `b` is absent from `P_j`.  This
holds for all four envelopes available to row `i`, so their union omits `b`
although `T_i` contains it.  ∎

The hypotheses about location are essential.  A positive run meeting the
left endpoint can use a truncated predecessor intersection; for example
`P_0=T_0`, so a leading singleton is not automatically bad.  After a depth
drop from three to `h`, the honest threshold is `h+1`, and a length-three run
can be legal when `h<=2`.  These are the endpoint/depth-drop exceptions.
Every certificate below lies strictly between positions 1986 and 5939, well
inside the common depth-three prefix, so none uses an exception.

## 5. Robust windows give implications

For a coordinate `b`, start `s`, and `1<=ell<=3`, define the boundary/run
indicator

\[
R_{b,s,\ell}(z)=
(1-h_{s-1,b})\left(\prod_{i=s}^{s+\ell-1}h_{i,b}\right)
(1-h_{s+\ell,b}).                                   \tag{5.1}
\]

Here juxtaposition denotes Boolean conjunction.  Thus `R=1` means precisely
the forbidden trace (4.2).

Suppose all nonconstant literals in this window belong to two cycles `C,D`.
If substituting `(z_C,z_D)=(1,0)` makes `R=1`, every exact hybrid must avoid
that assignment.  Equivalently,

\[
 z_C\le z_D.                                         \tag{5.2}
\]

Record a directed arc `C -> D`.  This implication is robust: no assignment
outside `C,D` occurs in its three-to-five-position window.

### Lemma 5.1 (strong implication criterion)

If the directed graph of robust implication arcs on the assignment cycles
is strongly connected, the only middle-exact cycle assignments are all zero
and all one.

#### Proof

Every exact assignment satisfies (5.2) on every arc.  Directed paths give
the same inequality between their endpoints.  Strong connectivity gives
both `z_C<=z_D` and `z_D<=z_C` for every pair, hence all cycle bits are
equal.  Equivalently, any nonconstant Boolean assignment has a directed path
from a 1-cycle to a 0-cycle and therefore an arc on that path assigned
`1 -> 0`; its stored window is a short positive run.  ∎

This is a polynomial certificate.  Constructing all affine windows costs
`O(16*3*N)` per pair, followed by ordinary graph reachability.  It does not
inspect the `2^c` subsets.

## 6. Exact certificates for the five large pairs

| pair | cycles `c` | robust arcs | SCC sizes | selected windows | certificate span |
|---|---:|---:|---|---:|---|
| 151/282 | 26 | 153 | 26 | 50 | `[2184,4053)` |
| 155/282 | 23 | 133 | 23 | 44 | `[2185,4009)` |
| 178/282 | 24 | 143 | 24 | 46 | `[1986,5939)` |
| 231/282 | 26 | 157 | 19, 7 | 50 | `[2186,4053)` |
| 233/282 | 21 | 98 | 21 | 40 | `[2993,3861)` |

For each strongly connected row, the frozen certificate stores one outward
and one inward spanning arborescence.  Hence the selected windows alone,
without relying on unrecorded arcs, prove strong connectivity.

### The exceptional pair 231/282

The pairwise graph has exactly two strongly connected classes

\[
S_0=\{0,\ldots,18\},\qquad S_1=\{19,\ldots,25\}.     \tag{6.1}
\]

The selected arborescences force one common bit `X_0` on `S_0` and one
common bit `X_1` on `S_1`.

There is a robust forward arc `2 -> 19`.  Its coordinate is `0008`, its
window is `[3844,3847)`, and its affine trace is

```text
~x2, 1, x19.
```

At `(x2,x19)=(1,0)` this is `0,1,0`.  Hence `X_0<=X_1`.

The missing reverse quotient implication is supplied by one exact
three-cycle window.  Coordinate `0400` on `[3842,3847)` has affine trace

```text
x4, 1, 1, ~x1, ~x19.
```

The assignment `(x4,x1,x19)=(0,0,1)` gives

```text
0,1,1,1,0,
```

a forbidden length-three run.  Since `x1=x4=X_0` and `x19=X_1` by (6.1),
this excludes `(X_0,X_1)=(0,1)` and gives `X_1<=X_0`.  Thus `X_0=X_1`, so
the exceptional pair also has only the two endpoint assignments.

## 7. Why an unqualified generic theorem would be false

Same multiset and exact endpoint run lengths do not by themselves imply
hybrid collapse.  At the level of one coordinate, take

```text
A = 0000000011110000000011110000
B = 0000111100000000111100000000.
```

Ordered equal-symbol pairing gives eight nontrivial 2-cycles, four in each
of two balanced eight-position gadgets.  Selecting all four cycles of the
first gadget and none of the second is a nonempty proper subset and gives

```text
0000111100000000000011110000,
```

whose positive runs still both have length four.  Thus the correct reusable
hypothesis is the strong robust-implication criterion of Lemma 5.1, with the
explicit quotient-clause extension used for 231/282—not merely equal
multisets or exact endpoints.

## 8. Reproducibility and exact scope

The solver-free audit is

```text
scratch/audit_ad_k16_splitpair_hybrid_run_implications_20260730.py
SHA256 56ae3c146c41d43de65c0b65ddf8ae67ab99b3f7f7b28a787994e0445c6fdac1
```

and writes

```text
scratch/ad_k16_splitpair_hybrid_run_implications_20260730.audit.json
SHA256 111ae02e333d410a52b72ac0ce56a88c99fe4947bf79dbb091cdddbf8e8c747e
payload 8cd03159e511893e26468e09c4219b59ae7eb1f12db2f29a00ef4999f87b40d8
```

The audit authenticates all eight words, independently replays their exact
middle geometry, verifies the common flat values, recomputes all 28 cycle
counts, constructs the affine local windows, freezes spanning certificates,
and checks the exceptional quotient bridge.  It performs no SAT solve and no
subset enumeration.

The run-implication certificate is stated for the ordered-equal-occurrence
cycle-selection model implemented by the frozen C++ program.  Lemma 3.1
proves that this model is WLOG for literal pointwise `A/B` choices preserving
the row multiset on the eight authenticated endpoints; other duplicate
pairings are value-inert.  The theorem does not exclude a third-parent
hybrid, new row values, a non-pointwise braid, a non-multiset-preserving
construction, or another K16 equality architecture.
