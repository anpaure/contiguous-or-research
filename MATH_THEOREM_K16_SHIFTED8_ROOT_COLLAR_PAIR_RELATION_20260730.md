# K16 shifted-eight root-collar two-token relation

## 1. Setup and scope

Let (Q) be

```text
scratch/k16_exact229_shifted8_natural_near_20260730.targets
SHA-256 e8c720ef977b5f561c32d84c7c4a51e710999eab80d88bf814aa1f855b254f06.
```

It has fixed flats 6320, 12869, 12871, no zero envelope, no
arbitrary-upper hole, and one middle error:

```text
row 3845: 6ba8 -> 69a8, missing 0200.
```

Put (j=3846), and let

\[
 H=\{j-6,\ldots,j-1,j+1,\ldots,j+6\}.
\]

This note solves the fixed-depth local service problem in which (Q_j,Q_h),
for one (h\in H), are simultaneously replaced by rank-eight masks (U,V).
It does not yet route the two displaced incumbent tokens through their return
positions.

The protected Hall cells have the complete signatures

```text
13964 [4654,4657): E=(6221,4a21,0a29), A=6a29, M=6809;
13966 [4655,4657): E=(4a21,0a29),      A=4a29, M=4809.
```

Their joint functional closure is rows 4650 through 4658.  Hence every local
pair in this note preserves both complete signatures automatically once the
flat schedule is fixed.

## 2. Coordinate relation theorem

For (h\in H) and coordinate (b\), define

\[
 \mathcal R_{h,b}\subseteq\{0,1\}^2
\]

as follows.  Replace the (b)-th target bits at rows (j,h) by (u,v),
leave all other target bits fixed, form every depth-three four-row AND
envelope, and require exact replay on

\[
 \{3845\}\cup[j-3,j+3]\cup[h-3,h+3].             \tag{2.1}
\]

> **Theorem 2.1 (exact two-token relation).**  A pair of masks (U,V)
> gives exact fixed-depth middle replay after replacing rows (j,h) if and
> only if
> \[
> (U_b,V_b)\in\mathcal R_{h,b}\qquad(0\le b<16).  \tag{2.2}
> \]
> If the four affected boundary edges also retain their nonflat status, then
> the original global depth schedule and capacity 32063 are retained.  Every
> rank-eight pair satisfying (2.2) and this edge condition has no zero
> envelope.

### Proof

With the depth schedule fixed, both envelope formation and replay are
coordinatewise.  A change at target row (p) changes only envelopes
([p,p+3]), and hence only replay rows ([p-3,p+3]).  The input has no old
middle error outside row 3845, so (2.1) is the complete affected-row closure.
This proves necessity and sufficiency of (2.2).  The edge condition preserves
the flat set, hence preserves every depth offset globally.  Exhausting the
rank-eight solutions of the sixteen four-state relations gives 1195 literal
flat-compatible pairs; direct envelope reconstruction on all 1195 finds zero
empty envelopes.  Thus the final assertion is exact, not probabilistic.

## 3. Exact relation codes

Encode a relation by the hexadecimal mask whose bits (0,1,2,3) represent
states `00,01,10,11`, respectively.  Reading coordinates from bit 0 through
bit 15, the twelve relations are:

| (h) | offset | relation-code word | admissible (U) | rank-eight pairs |
|---:|---:|:---|---:|---:|
| 3840 | -6 | `f32a542f48241cf1` | 8 | 64 |
| 3841 | -5 | `532f543a482c1cf1` | 8 | 104 |
| 3842 | -4 | `512e5c3a4c2c1ca1` | 8 | 89 |
| 3843 | -3 | `512a5c1acc381ca1` | 8 | 64 |
| 3844 | -2 | `513a581acc381ca1` | 8 | 64 |
| 3845 | -1 | `d1bbd81b8d181cf1` | 33 | 309 |
| 3847 | 1 | `b11db81d881db8f1` | 30 | 171 |
| 3848 | 2 | `a115ac1f881c38a1` | 8 | 32 |
| 3849 | 3 | `a115ac3f8c142ca1` | 8 | 64 |
| 3850 | 4 | `e11fa43acc142ea1` | 13 | 130 |
| 3851 | 5 | `f13aa42acc1424f1` | 8 | 72 |
| 3852 | 6 | `f13af42a4c1434f1` | 8 | 32 |

The total is 148 admissible first masks and 1195 admissible ordered
location-labelled triples ((h,U,V)).  The first-mask count is a sum over
(h); the same mask may occur for several collar rows.  If the collar label
(h) is forgotten, there are 1084 distinct ordered mask pairs.

## 4. Forced/free-mask normal form

Fix (h) and an admissible (U).  For each coordinate, the row of
(mathcal R_{h,b}) selected by (U_b) allows either no value, only zero,
only one, or both values for (V_b).  Thus there are unique disjoint masks

\[
 P_h(U),F_h(U)
\]

such that

\[
 V=P_h(U)\cup S,qquad S\subseteq F_h(U),qquad |V|=8.    \tag{4.1}
\]

The reproducer groups all coordinate-admissible (U)'s by the pair
((P_h(U),F_h(U))).  There are only one to four raw classes except at the
adjacent rows 3845 and 3847, where there are 34.  Five adjacent-row fibres
become empty after the rank-eight and literal-edge conditions: `69ac` at
3845, and `3339,33b1,3b31,7331` at 3847.  This leaves the 33 and 30 active
first masks displayed in the table.  Formula (4.1) is the desired quotient:
it replaces an unrestricted pair scan by binomial submask generation.

## 5. Physical source-pair compression

The occurrence deck contains every rank-eight mask once, with one additional
copy of each of `4e71`, `cc63`, and `ce61`.  For a two-exterior-source
support-four architecture, exclude the target rows (j,h) and require the
two physical sources to be distinct.  Applying these multiplicities to
(4.1) gives:

| (h) | exterior source pairs |
|---:|---:|
| 3840 | 56 |
| 3841 | 96 |
| 3842 | 81 |
| 3843 | 56 |
| 3844 | 56 |
| 3845 | 285 |
| 3847 | 162 |
| 3848 | 24 |
| 3849 | 56 |
| 3850 | 122 |
| 3851 | 64 |
| 3852 | 24 |

There are exactly

\[
 1082                                                     \tag{5.1}
\]

ordered location-labelled triples ((h,s_U,s_V)) in total.  Every one is
zero-envelope-safe.  Forgetting (h) leaves 971 distinct ordered physical
source pairs.
Thus the next support-four search should start from these 1082 service pairs,
not from all ordered pairs of middle occurrences.

This is not yet a completed occurrence cycle.  If sources (s,t) supply
(U,V) to (j,h), the displaced incumbents `6939` and (Q_h) must still be
routed back to (s,t) in one of the legal cycle orientations.  Their source
collars, arbitrary-upper coverage, and full Hall must be replayed.  Cycles in
which (j) or (h) itself supplies one of the two new tokens form separate
one-exterior-source orientations and are not counted in (5.1).

### Exact two-exterior return no-go

For an ordered exterior source pair ((s,t)) counted in (5.1), there is one
four-cycle orientation that installs its two values at ((j,h)):

\[
 j\leftarrow s\leftarrow h\leftarrow t\leftarrow j.       \tag{5.2}
\]

Thus row (s) receives the displaced old (Q_h), and row (t) receives old
`6939`.  Full literal replay of all 1082 cycles (5.2), allowing the geometry
routine to detect relocated flats, gives

```text
cycles 1082; exact middle 0; dynamic-flat exact 0.
```

Consequently no two-exterior-source root-collar support-four cycle in the
fixed-depth service relation is a repair.  A surviving support-four route must
use at least one of: a target row itself as a token source, a service pair that
becomes legal only after a flat relocation, or a root-free carrier based on
rows 3843 and 3844.

## 6. Artifacts

```text
scratch/audit_threadA_k16_shifted8_root_collar_pair_relations_20260730.cpp
scratch/threadA_k16_shifted8_root_collar_pair_relation_summary_20260730.tsv
scratch/audit_threadA_k16_shifted8_two_exterior_support4_replay_20260730.cpp
scratch/threadA_k16_shifted8_two_exterior_support4_replay_20260730.audit.tsv
```

The C++ reproducer emits the full 192 coordinate relations, the
forced/free-mask rows, and the 1082 occurrence-labelled exterior source
pairs.  It performs only the finite coordinate truth-table and rank-eight
submask calculation; it does not run a support-four search or Hall solver.
