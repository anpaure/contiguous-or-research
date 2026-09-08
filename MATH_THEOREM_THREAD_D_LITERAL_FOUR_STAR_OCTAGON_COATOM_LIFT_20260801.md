# The literal four-star octagon lift closes the local deck but not residence

Date: 2026-08-01  
Lane: Thread D, smallest literal source-star algebra after the two-star no-go  
Status: exact separated-arm source, owner, interval-OR and common-cap theorem.
Its minimal no-buffer concatenation is not resident.  Cross-arm exterior
intervals and a global host are not claimed.

## 0. Outcome

The quaternary octagon admits a literal four-source-star lift at every depth
`d>=2`.  Each of the four octagon atoms is replaced by one asymmetric
**coatom** arm of source width `2d-1`.  Only the source immediately next to
each star changes phase.  The resulting four-arm direct sum has:

* exact support `4(2d-1)=8d-4`;
* exactly four phase-changing source positions;
* `4(d-1)` distinct, equicardinal owner coatoms forming four Johnson paths;
* exactly permuted crossing and owner banks;
* exactly permuted complete arm-internal interval-OR **multisets**; and
* one literal common cap family, nontrivial at only the four changing
  positions.

This is the smallest literal star algebra currently available.  It is not
resident as a standalone macro.  In the minimal concatenation of its four
owner blocks, each varying filler is omitted once per block.  Consecutive
zeros are `d-1` positions apart, so each of the three strict intervening
positive runs has length exactly `d-2<d+1`.  At least three filler-present
buffer owners are needed at every internal block join to repair this
particular concatenation.

The resident `8d+23` octagon tensor is therefore a genuinely different
object: it expands all eight tail/head ports.  Its two maximal inverse words
differ at `4d+16` positions, although exact thinning reduces the minimum to
eight phase-changing source addresses for `d>=2` (twelve for `d=1`).  It is
not merely this four-star lift with a different notation.

## 1. The four source arms

Let `S` be a fixed nonempty core and choose distinct active labels

\[
                         z,a_0,a_1,a_2,a_3                 \tag{1.1}
\]

outside `S`.  Indices are modulo four.  Put

\[
\begin{aligned}
 L_i&=S\cup\{a_i\},& A_i&=S\cup\{z,a_i\},\\
 B_i&=S\cup\{a_i,a_{i+1}\},&
 U_i&=S\cup\{z,a_i,a_{i+1}\}.                           \tag{1.2}
\end{aligned}
\]

Let `F={f_1,...,f_d}` be disjoint from these labels.  In phase
`epsilon in {0,1}`, define

\[
 H_i^0=B_i,\qquad H_i^1=B_{i-1},\qquad
 V_i^0=U_i,\qquad V_i^1=U_{i-1}.                         \tag{1.3}
\]

The source arm `X_i^epsilon` occupies relative positions
`-(d-1),...,d-1` and is

\[
\begin{aligned}
 X_{i,0}^\epsilon&=A_i,\\
 X_{i,-t}^\epsilon&=L_i\cup\{f_t\},
                         &&1\le t<d,\\
 X_{i,1}^\epsilon&=H_i^\epsilon,\\
 X_{i,t}^\epsilon&=L_i\cup\{f_{d-t+2}\},
                         &&2\le t<d.                     \tag{1.4}
\end{aligned}
\]

Thus the left filler order, read toward the star, is
`f_(d-1),...,f_1`, and the reflected right order after the head source is
`f_d,...,f_3`.

### Theorem 1.1 (crossing coatoms and equicardinal owners)

For `1<=j<d`, delete the star and take the length-`d` crossing using `j`
left sources and `d-j` right sources.  Its value is

\[
 C_{i,j}^\epsilon
   =H_i^\epsilon\cup\bigl(F-\{f_{j+1}\}\bigr).          \tag{1.5}
\]

The corresponding length-`d+1` owner containing the star is

\[
 T_{i,j}^\epsilon
   =V_i^\epsilon\cup\bigl(F-\{f_{j+1}\}\bigr).          \tag{1.6}
\]

Consequently all owners have rank `|S|+d+2`, consecutive owners in one
arm are Johnson-adjacent, and

\[
 C_{i,j}^1=C_{i-1,j}^0,\qquad
 T_{i,j}^1=T_{i-1,j}^0.                                  \tag{1.7}
\]

In particular the complete crossing and owner multisets return exactly.

#### Proof

The crossing contains `H_i^epsilon`, the left fillers
`f_1,...,f_j`, and the right fillers `f_(j+2),...,f_d`.
This proves (1.5), and adjoining the star `A_i` gives (1.6).  Increasing
`j` exchanges the omitted filler `f_(j+1)` for `f_(j+2)`, so the owner row
is a simple Johnson path.  Finally

\[
 H_i^1=B_{i-1}=H_{i-1}^0,\qquad
 V_i^1=U_{i-1}=V_{i-1}^0,
\]

which proves (1.7).  \(\square\)

This is precisely the nonflat correction missing from the asymmetric
two-star construction: the crossing cells are incomparable coatoms rather
than a strictly increasing prefix chain, so adjoining the star no longer
changes rank.

## 2. Complete local interval deck and common cap

For a finite source word `X`, let `M_vee(X)` be the multiset of unions of
all its nonempty contiguous intervals.

### Theorem 2.1 (full arm-internal deck permutation)

The complete four-arm direct sums satisfy

\[
              \biguplus_{i=0}^3 M_\vee(X_i^0)
              =
              \biguplus_{i=0}^3 M_\vee(X_i^1).           \tag{2.1}
\]

This is equality with occurrence multiplicity, not merely equality of
supports.  It includes every singleton, fan, crossing and owner interval
lying wholly inside one arm.

#### Proof

Fix a relative interval shape in (1.4).  If it omits relative position
`+1`, its union is phase independent.  Suppose it contains `+1`.  Every
other nonstar active contribution is contained in `L_i`, and
`L_i subset H_i^epsilon` in both phases.

If the interval omits the star, its active part is `H_i^epsilon`.  If it
contains the star, its active part is `A_i union H_i^epsilon=V_i^epsilon`.
Its filler contribution depends only on the relative endpoints, not on
`i` or `epsilon`.  The two identities in (1.7) therefore match every
phase-one interval of arm `i` with the same relative interval of phase-zero
arm `i-1`.  \(\square\)

The qualification “arm-internal” is load-bearing.  An interval crossing
the exterior gap between two separated arms also sees the frozen host, and
must be checked by the ordinary prefix/suffix boundary test.  Equation
(2.1) does not silently certify those global intervals.

### Corollary 2.2 (literal common caps)

At every source position except relative `+1`, use the displayed common
letter in (1.4) as its cap.  At the four changing positions use

\[
                         P_{i,1}=B_i\cup B_{i-1}.          \tag{2.2}
\]

Both phase words are nonempty and lie pointwise in this same cap family.
Exactly four source positions differ between phases.  Both phases have the
same source length, so the phase switch has zero length charge.

Relative to a word in which the four star positions are deleted, planting
the lift costs four source cells.  The complete separated support of the
four canonical arms is

\[
                         4(2d-1)=8d-4.                    \tag{2.3}
\]

No overlap improvement is asserted here: (2.3) is the exact support of the
source-private separated-arm normal form.

## 3. Exact residence failure

Order the four owner blocks by `i=0,1,2,3` and concatenate them without
additional buffer owners, using the displayed coatom order (1.6) in every
block.  Reversing all four blocks simultaneously gives the same argument.
For every `2<=t<=d`, coordinate
`f_t` is absent exactly once in every block and is present at every other
owner.

### Theorem 3.1 (minimal concatenation has floor `d-2`)

For every `d>=3`, this canonical linear four-block concatenation has, for each
`f_t` with `2<=t<=d`, exactly three strict internal positive runs of length

\[
                              d-2.                        \tag{3.1}
\]

It therefore fails depth-`d` residence.  If `b` filler-present owners are
inserted at one internal block join, the corresponding run has length
`d-2+b`; hence this concatenation needs at least three such buffer owners at
each internal join.

#### Proof

Each block has length `d-1`, and the unique zero of `f_t` occurs at the same
relative coatom address in every block.  Consecutive zeros are therefore
`d-1` owner positions apart.  The positive run strictly between them has
length `d-2`, proving (3.1).  Inserting `b` positive positions increases
that run to `d-2+b`, which reaches the required `d+1` exactly when
`b>=3`.  \(\square\)

At the source level the same failure is already visible as a warning:
`z`, the phase-selected neighbouring active label, and several fillers have
singleton occurrences in one arm.  Singleton source occurrences are not
themselves forbidden—a depth-`d` dilation may stretch them—but the owner
calculation above shows that the minimal direct concatenation does not
provide enough spacing between the repeated coatom omissions.

Independently reversing selected blocks changes the exact gap ledger and is
not covered by Theorem 3.1.  Exterior path fragments containing the fillers
could also repair these runs.
Accordingly Theorem 3.1 is an exact standalone/no-buffer obstruction, not
an architecture-free proof that every host embedding of the four arms
fails residence.

## 4. Relation to the resident tensor

The literal lift and the resident coatom tensor close different rows:

\[
\begin{array}{c|c|c}
 &\text{literal four-star lift}&\text{resident port tensor}\\ \hline
 \text{source support}&8d-4&9d+23\text{ maximal-inverse positions}\\
 \text{owner support}&4(d-1)&8d+23\\
 \text{phase-changing sources}&4&
      4d+16\text{ maximal; }8\text{ thinned }(d\ge2)\\
 \text{local internal OR deck}&\text{exact direct sum}&\text{exact path deck}\\
 \text{residence}&\text{fails without buffers}&\text{floor }d+1
\end{array}                                                \tag{4.1}
\]

The resident tensor uses all eight octagon ports and seven alternating
screens; its union screens force block size at least `d+2`, giving the
sharp fixed-template owner width `8d+23`.  Thus it is a positive `O(d)`
replacement, but not a compression of (1.4) to four literal changing
sources.

## 5. Independent replay

Run

```text
python3 scratch/audit_threadD_literal_four_star_octagon_coatom_lift_20260801.py
```

The dependency-free replay checks `2<=d<=16`, both phases, every source,
crossing and owner formula, owner ranks and Johnson adjacency, exact
crossing/owner permutations, the complete arm-internal interval-OR
multiset, common caps, all counts, and the strict `d-2` runs.  Its frozen
output is

```text
scratch/threadD_literal_four_star_octagon_coatom_lift_20260801.audit.json
```

and reports

```text
PASS_THREADD_LITERAL_FOUR_STAR_OCTAGON_COATOM_LIFT
payload_sha256=df5ed0c70a8d25d1435078193ea739d8b8a7eaaf2f8b906e449cf500fdac45e4
```
