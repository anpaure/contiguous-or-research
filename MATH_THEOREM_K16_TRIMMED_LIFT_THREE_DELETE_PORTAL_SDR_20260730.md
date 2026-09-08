# Exact portal criterion for three-entry compression of the `k=16` trimmed lift

Date: 2026-07-30

Status: exact localization and finite feasibility theorem; exact baseline and
single-deletion audit.  No feasible deletion triple and no global
`nu(16)=12873` construction is claimed here.

## 1. Frozen lift

Let

```text
A = answers/k15.word,
n = 6438,
z = 32768,
B = A[0:n-1].
```

The standard trimmed lift is

\[
 Q=A\ \Vert\ [z]\ \Vert\ [z\vee B_0,\ldots,z\vee B_{n-2}],       \tag{1.1}
\]

of length `12876`.  The frozen hashes are

```text
f35da2f0c98ec07de3e5318554157af490558e881be5c8bbcb5e3d1c8c08b14b
    answers/k15.word

9d0214f6c7cea45a1f26d031687ecada9ac34500e925dcfc127bdf1514b624c8
    canonical whitespace-plus-newline serialization of Q.
```

All indices below are zero based.  Thus `A` occupies `Q[0:6438]`, the
literal singleton `z` is `Q[6438]`, and the transformed `B` shore occupies
`Q[6439:12876]`.

## 2. Exact localization of a direct deletion triple

### Lemma 2.1 (the first shore and `z` are undeletable)

If deleting three literal entries of `Q` leaves a universal word, all three
deleted entries lie in the transformed `B` shore.

#### Proof

Every entry outside the first `A` block contains `z`.  Hence every target
avoiding `z` must be witnessed wholly inside the retained part of `A`.  If
one entry of `A` were deleted, that retained block would be a universal word
on 15 points of length at most `6437`, contradicting the proved equality

\[
                             \nu(15)=6438.                       \tag{2.1}
\]

The entry `z` is also undeletable.  Every other entry of `Q` has nonempty
old projection, so no interval avoiding that literal cell has union exactly
`{z}`.  QED.

This is a theorem about literal deletion from the frozen lift.  A recompilation
which changes cell contents is a different search space.

## 3. Exact projected portal formula

For a word `W`, write

\[
 \operatorname{IntOR}(W)
 =\left\{\bigvee_{t=i}^{j}W_t:0\le i\le j<|W|\right\}.            \tag{3.1}
\]

Let `Pref(W)` and `Suff(W)` be its prefix-OR and suffix-OR state sets,
including the empty state zero.  For set families `X,Y`, put

\[
                         X\vee Y=\{x\vee y:x\in X,y\in Y\}.       \tag{3.2}
\]

For a three-set `D` of positions in `B`, let `B_D` be the word obtained by
deleting those positions and closing the gaps.

### Theorem 3.1 (direct three-deletion iff criterion)

The compressed lift

\[
                 Q_D=A\ \Vert\ [z]\ \Vert\ (z\vee B_D)          \tag{3.3}
\]

is universal on 16 points if and only if

\[
 \boxed{
  2^{[15]}\setminus\{\varnothing\}
  \subseteq
  \operatorname{IntOR}(B_D)
  \ \cup\ 
  \bigl(\operatorname{Suff}(A)\vee\operatorname{Pref}(B_D)\bigr).
 }                                                               \tag{3.4}
\]

#### Proof

The intact first block `A` covers every nonempty target avoiding `z`, and
the intact singleton covers `{z}`.

Project a witness for `z union S` onto the old 15 coordinates.  If the
witness lies wholly in the transformed shore, its projection is an internal
interval OR of `B_D`.  Otherwise it crosses the unique central seam and is
exactly a suffix of `A`, followed by `z`, followed by a prefix of `B_D`.
Allowing an empty suffix or prefix includes witnesses starting or ending at
`z`.  These cases are exhaustive and give the right side of (3.4).
Conversely, each displayed projected interval lifts literally to a witness
for `z union S`.  QED.

Equation (3.4) is the smallest exact fixed-word test: it uses neither a
flat-middle normal form nor a compiler conjecture.

## 4. Why ordinary interval Hall collapses

Split `B` at the deleted positions.  Call an interval **native** if it lies
inside one retained original run.  Let `L_D` be the projected masks with no
native witness.  Let `P_D` be the physical intervals of `Q_D` which use a
new deletion adjacency or the central seam.  Form the bipartite graph

\[
 S\sim I\quad\Longleftrightarrow\quad
 S\in L_D,\ I\in P_D,\ \operatorname{OR}(I)=z\vee S.              \tag{4.1}
\]

### Lemma 4.1 (exact Hall reduction)

The Hall inequalities for (4.1) hold if and only if every `S in L_D` has at
least one portal witness.

#### Proof

One physical interval has one exact OR label.  Therefore neighborhoods of
two distinct masks are disjoint.  For every `X subseteq L_D`,

\[
 \left|\bigcup_{S\in X}N(S)\right|
 =\sum_{S\in X}|N(S)|.                                           \tag{4.2}
\]

Hall is consequently equivalent to `|N(S)|>=1` for each singleton family.
QED.

This matters conceptually.  Ordinary OR witnesses may overlap in positions;
positions are not consumed when an interval witnesses a mask.  Thus a
cell-capacity-one SDR imposed directly on fixed intervals would be an
unsound strengthening.  In the literal deletion problem, (3.4), or an
equivalent full replay, is the exact simultaneous test.

### Lemma 4.2 (target-subset run localization)

Fix a projected target `S`.  Call position `p` of `B` **good** for `S` when
`B_p subseteq S`, and **bad** otherwise.  Suppose deleting a good position
`d` loses `S`.  Deleting any further set consisting only of good positions
cannot recreate `S`.

Indeed, if an interval of the further-compressed word had union `S`, insert
back every additionally deleted good entry lying between its endpoints.
Every inserted entry is a subset of `S`, so the interval remains labelled
`S`; it would already be a witness after deleting only `d`, a contradiction.

Consequently, with at most two further deletions, every minimal **internal**
repair atom for `S` is one of:

1. one bad position, joining a suffix and prefix of its two adjacent good
   runs; or
2. two consecutive positions in the ordered list of bad positions, joining
   the intervening three good runs.

If two deleted bad positions were not consecutive in that list, an undeleted
bad entry would contaminate every interval spanning both; any witness using
only one makes the other deletion nonminimal.

There is a parallel central-seam rule.  Fix a suffix state `R in Suff(A)`
with `R subseteq S`.  A prefix of `B_D` satisfying `R union prefix = S` may
pass only bad positions which were deleted.  Thus, under a two-additional-
deletion budget, the only new central atoms are deletion of the first bad
prefix position or of the first two bad prefix positions, followed by a
literal OR check.  These target-specific singleton/pair atoms give an exact
finite candidate generator; sufficiency still requires (3.4), because a
deleted good cell may remove a required coordinate from the proposed
witness.

## 5. Where a genuine Hall/SDR condition enters

Hall becomes nontrivial only when source cells are variable compiler
resources rather than fixed letters.  The following criterion includes
literal occurrence capacities, overlapping interval conflicts, and boundary
legality.

Let `J` be a finite line of source positions.  Give position `p` a nonempty
upper envelope `E_p`.  Let `W_0` be a family of protected exact windows
`(I,R)`, where `I` is an interval and the required OR is `R`.  It may include

* every middle/compiler window;
* the one-core adjacency windows
  `R=P_p union P_(p+1)` when `DA=DP` is required;
* fixed native witnesses which touch a variable boundary halo; and
* prescribed boundary pins.

For each residual target `S`, let `C(S)` be its finite set of admissible
literal or cross-seam intervals.  An assignment chooses one
`phi(S) in C(S)`.  Repeated use of one singleton position or of one physical
interval by distinct labels is forbidden.

For a choice `phi`, put

\[
 \mathcal W(\phi)=\mathcal W_0\cup
                  \{(\phi(S),S):S\text{ residual}\},             \tag{5.1}
\]

and define its joint maximal envelope

\[
 J_p(\phi)=E_p\cap
     \bigcap_{(I,R)\in\mathcal W(\phi):\ p\in I}R.                \tag{5.2}
\]

### Theorem 5.1 (conflict-aware finite SDR criterion)

The choice `phi` lifts to a nonzero literal word `C=(C_p)` satisfying every
protected compiler window and every assigned target window if and only if

\[
 J_p(\phi)\ne\varnothing\quad(p\in J),                            \tag{5.3}
\]

and

\[
 \bigcup_{p\in I}J_p(\phi)=R
 \quad\text{for every }(I,R)\in\mathcal W(\phi).                 \tag{5.4}
\]

#### Proof

Every realizing word is entrywise contained in (5.2), since an entry in a
window labelled `R` cannot contain a coordinate outside `R`.  Hence
nonemptiness and every inclusion in (5.4) are necessary.  Conversely, take
`C_p=J_p(phi)`.  Equation (5.2) excludes every coordinate outside each
window label, and (5.4) supplies every coordinate inside it.  Thus all
window ORs are exact.  QED.

This is precisely the simultaneous-interval conflict test.  If two selected
windows overlap incompatibly, their intersections in (5.2) empty a source
cell or destroy a required carrier coordinate in (5.4).

Equivalently, introduce binary selection variables `y_(S,I)` and literal
bits `a_(p,x)`.  The finite exact system is

\[
 \sum_{I\in\mathcal C(S)}y_{S,I}=1,\qquad
 \sum_S y_{S,I}\le1,                                            \tag{5.5}
\]

\[
 a_{p,x}=0\ (x\notin E_p),\qquad \sum_xa_{p,x}\ge1,              \tag{5.6}
\]

and, for every selected `(S,I)`,

\[
 a_{p,x}\le1-y_{S,I}\quad(p\in I,x\notin S),                    \tag{5.7}
\]

\[
 \sum_{p\in I}a_{p,x}\ge y_{S,I}\quad(x\in S),                 \tag{5.8}
\]

together with the identical exact-window clauses for `W_0`.  This is a
finite SAT/MILP iff criterion, not an LP relaxation.

### Corollary 5.2 (conditioned literal Hall theorem)

Suppose a portal packet has already produced bounds `C_p subseteq E'_p`
such that every protected or selected portal window `(I,R)` is immune:

\[
 \bigcup_{p\in I}C_p=R,
 \qquad E'_p\subseteq R\quad(p\in I).                            \tag{5.9}
\]

For the remaining targets, which must be literal, put

\[
 N_{C,E'}(S)=\{p:C_p\subseteq S\subseteq E'_p\}.                 \tag{5.10}
\]

There is a capacity-one literal assignment preserving the packet if and
only if

\[
 \boxed{
 \left|\bigcup_{S\in X}N_{C,E'}(S)\right|\ge|X|
 \quad\text{for every residual family }X.
 }                                                               \tag{5.11}
\]

Pinned positions are contracted exactly as usual: validate the pin, delete
its position from every other neighborhood, remove the supplied target, and
apply (5.11).  This is the genuine boundary/compiler Hall test.  Condition
(5.9) is what makes Hall sufficient; without it, Theorem 5.1's joint carrier
clauses are indispensable.

## 6. Frozen audit on the trimmed lift

The solver-free audit

```text
scratch/audit_k16_trimmed_lift_three_delete_portal_sdr_20260730.py
```

and its machine-readable all-position ledger are

```text
c368c0c2174b68f9ff5dc2cb181b29c99a00a2bd1d519537258f88bac4546282
    scratch/audit_k16_trimmed_lift_three_delete_portal_sdr_20260730.py

703d588045b91168479ecedde58aabd2028c21e3870294103cd065b5b7b7297b
    scratch/k16_trimmed_lift_three_delete_portal_sdr_full_20260730.audit.json
```

The JSON contains the exact residual set for each of all `6437` possible
single deletions, not only aggregate counts.

A separately written auditor produced

```text
aef2ee487f44fcb44a7005b9b4d0b55edbc6744b94e7ecf1ff2e3fe704d83bca
    scratch/audit_k16_trimmed_lift_single_delete_loss_atlas_20260730.py

97f64fe015d82a21cebe91af20ee3dc3b1aace22b2b3938f11a4f0409d43655d
    scratch/k16_trimmed_lift_single_delete_loss_atlas_20260730.audit.json
```

Direct row-by-row comparison gives zero mismatches in position, deleted
projection, deficit, and exact missing-projection set for all `6437` rows.
Across the atlas, `25593` distinct projections are vulnerable to at least
one single deletion; their numbers of vulnerable positions have histogram

```text
1^4085  2^12502  3^7387  4^1544  5^75.
```

reconstructs the lift, checks both hashes, and computes:

```text
IntOR(B) nonempty masks                    32764 / 32767
baseline internal holes              18033, 20081, 20215
rank histogram of holes                     7:1, 8:1, 11:1
suffix states of A, including zero                        10
prefix states of B, including zero                        10
central labels, including projection zero                 28
nonzero central labels                                     27
```

All three baseline holes are covered at the central seam.  In particular,
they have suffix-only witnesses, so deleting in `B` cannot destroy those
witnesses.

The exact all-position single-deletion census gives

```text
viable single deletions                                      0
minimum projected deficit                                    2
```

and the only minimum rows are

| `B` index | `Q` index | deleted projection | unrecovered projections |
|---:|---:|---:|:---|
| 0 | 6439 | 18553 | 18553, 26745 |
| 1 | 6440 | 8249 | 10361, 10365 |
| 6436 | 12875 | 2657 | 20065, 20067 |

This is not a monotone pruning rule: deleting further cells can create a
larger seam whose OR omits additional coordinates.  A feasible triple need
not pass through a feasible single deletion.

Conversely, the union of the three single-deletion loss sets is not the full
triple loss family.  A target can have several native witnesses which are
jointly hit by three cells even though no one cell hits all of them.  The
single-deletion atlas is therefore a necessary-separator input, not a
replacement for the exact triple replay (3.4).

As a regression, deleting the three individually best positions
`D={0,1,6436}` leaves exactly the six projected masks displayed in the
table, hence six missing `k=16` targets.

For any proposed triple, run

```sh
python3 scratch/audit_k16_trimmed_lift_three_delete_portal_sdr_20260730.py \
  --delete i,j,k --skip-single-census
```

The script independently compares (3.4) with a full literal replay of all
contiguous ORs in the `12873`-entry compressed word.  A positive result must
have `status=PASS_UNIVERSAL_12873` and an empty `full_missing` list.

## 7. Scope warning about the third derivative

The frozen lift has third-window rank histogram

```text
rank 8: 6435, rank 9: 6436, rank 10: 1, rank 11: 1.
```

This excludes pure deletion as a route to the **flat-middle `COMP_3` normal
form**.  It is not a no-go for direct universality at length `12873`:
the monotone-deadline slack at `k=16` is `12284`, and positive slack does not
force an optimal word to have a flat third derivative.  Only (3.4) or full
literal replay decides the direct-deletion question.
