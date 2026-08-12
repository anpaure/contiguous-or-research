# Mixed coatom screens give an all-depth resident, upper-transparent simple ECO path

Date: 2026-08-01  
Status: exact local construction for every residence depth.  It closes the
owner, immediate-palette, upper-deck, residence and simple-Johnson-path rows
of one buffered ECO actuator.  Its embedding as a prescribed Pascal repair,
quadratic fixed-anchor menu, and unused compiler-basis label remain open.
Consequently this note does **not** by itself prove
`nu(k) <= B(k)+O(1)`.

## 0. Outcome

For every `d >= 1` and `r >= d+4`, one fixed twelve-owner active ECO switch
has two expansions `X_d,Y_d` of length

\[
                              12d+35                              \tag{0.1}
\]

into rank-`r` **simple Johnson paths** such that:

1. their endpoints and complete owner multisets agree;
2. all owners in each path are distinct;
3. their adjacent-intersection and adjacent-union multisets agree exactly;
4. their ordered prefix-OR and suffix-OR signatures agree pointwise;
5. their complete internal interval-OR support decks are equal; and
6. their clipped residence boundary states agree and every internal positive
   coordinate run has length at least `d+1`.

Thus `X_d <-> Y_d` is a reversible, owner-exact, immediate-palette-exact,
upper-transparent, resident path replacement.  The construction first used
full-filler lower screens at all eleven seams, which left four repeated
owners.  The decisive repair is to use the *other* Johnson common neighbour
at four alternating seams.  This mixed screen schedule removes all four
collisions without sacrificing any upper or residence invariant.

This is the first local packet in the repository to close rows U1--U4 at the
true growing depth:

```text
U1 crossing upper witnesses       exact,
U2 internal upper witnesses       exact as support,
U3 residence + boundary state     exact,
U4 simple physical topology       exact,
U5 fixed compiler-unused label    open.
```

Interval-OR **multiplicities** need not agree, and full deeper intersection
decks need not agree.  Coverage uses support; the lower compiler remains a
separate gate.

## 1. The active switch

Use six active coordinates `(e,a,b,c,d,infinity)` and the twelve triples

```text
Ad=e a d,  Bd=e b d,  Cd=e c d,
ab=e a b,  bc=e b c,  ca=e c a,
Iab=infinity a b, Ibc=infinity b c, Ica=infinity c a,
Ia=infinity e a, Ib=infinity e b, Ic=infinity e c.
```

Take

```text
P = Iab Ib bc Cd Ic Ibc Ica Ia ca Ad Bd ab,
Q = Iab Ia ca Cd Ic Ica Ibc Ib bc Bd Ad ab.
```

These are rank-three simple Johnson paths with common endpoints and the same
twelve vertices.  Direct calculation gives

\[
 \operatorname{Pre}_\vee(P)=\operatorname{Pre}_\vee(Q),\qquad
 \operatorname{Suf}_\vee(P)=\operatorname{Suf}_\vee(Q),\qquad
 \mathcal I_\vee(P)=\mathcal I_\vee(Q),                         \tag{1.1}
\]

where `mathcal I_vee` is the support of all nonempty interval unions.  This
is row 1 of the authenticated six-seam connector catalogue.  Rows 3 and 5
give two further copies of the theorem.

Index the eleven active transitions by `j=0,...,10` and put

\[
                             E=\{1,3,5,7\}.                      \tag{1.2}
\]

At the seven transitions outside `E`, the selected adjacent intersections
in either phase form the same seven-element set.  At the four transitions
inside `E`, the selected adjacent unions in either phase form the same
four-element set.  For `P` these masks are

\[
\begin{aligned}
 j\notin E:&\quad b\infty,ec,c\infty,a\infty,ea,ed,eb,\\
 j\in E:&\quad ebc\infty,ecd\infty,abc\infty,eac\infty.
\end{aligned}                                                    \tag{1.3}
\]

For `Q` they occur in another order.  In particular, all eleven selected
screen colours are distinct and their selected-colour multisets agree.

## 2. Tensor and mixed screens

Put `n=d+2`.  Take a fresh filler set

\[
 F=\{f_0,\ldots,f_{n-1}\},\qquad C_i=F-\{f_i\},\qquad
 F^\circ=F-\{f_0,f_{n-1}\},                                    \tag{2.1}
\]

disjoint from the active coordinates.  Take a further disjoint fixed core
`K` of size

\[
                              |K|=r-d-4.                         \tag{2.2}
\]

For an active triple `V`, define its coatom block

\[
 B(V)=\bigl(K\cup V\cup C_0,\ldots,K\cup V\cup C_{n-1}\bigr).  \tag{2.3}
\]

Between `B(V_j)` and `B(V_(j+1))`, use one of the two common neighbours

\[
\begin{aligned}
 L_j&=K\cup(V_j\cap V_{j+1})\cup F, &&j\notin E,\\
 U_j&=K\cup(V_j\cup V_{j+1})\cup F^\circ, &&j\in E.            \tag{2.4}
\end{aligned}
\]

Expand `P,Q` using the same positional schedule (1.2)--(2.4).  Call the
resulting words `X_d,Y_d`.  Every block, lower screen and upper screen has
rank `r`, and (0.1) follows from twelve length-`n` blocks and eleven screens.

## 3. Simple Johnson topology and exact owner current

### Theorem 3.1

`X_d,Y_d` are simple rank-`r` Johnson paths with common endpoints and the
same owner multiset.

#### Proof

Inside a block, consecutive coatoms exchange `f_i` and `f_(i+1)`.

At a lower screen, the last block owner changes to `L_j` by deleting the
departing active coordinate and inserting `f_(n-1)`; from `L_j` to the next
first block owner it deletes `f_0` and inserts the entering active coordinate.

At an upper screen, the last block owner changes to `U_j` by deleting `f_0`
and inserting the entering active coordinate; from `U_j` to the next first
block owner it deletes the departing active coordinate and inserts
`f_(n-1)`.  Thus every step is a Johnson step.  The active endpoints and the
coatom order are common.

Block equality determines both its active triple and missing filler, so all
`12n` block owners are distinct.  A block omits one filler, a lower screen
omits none, and an upper screen omits two, so the three types cannot collide.
Within each screen type, equality determines the selected colour in (1.3),
and all eleven selected colours are distinct.  Hence every expanded owner is
distinct.

Finally, `P,Q` use the same active triples, and (1.3) says that their selected
lower-intersection and upper-union screen multisets agree.  Their expanded
owner multisets therefore agree. \(\square\)

### Corollary 3.2 (immediate palettes)

The multisets

\[
 \{X_i\cap X_{i+1}\}_i,\quad \{X_i\cup X_{i+1}\}_i            \tag{3.1}
\]

agree respectively with the analogous multisets for `Y_d`.

#### Proof

Inside blocks the values depend only on the active vertex and coatom index.
At a lower or upper screen boundary they depend only on the oriented active
edge, the common screen type, and whether the boundary is left or right.
Substitution into the two explicit active words gives the same multisets;
equivalently, it is the finite identity (1.3) with its incident endpoint
triples retained. \(\square\)

The identity is also checked independently for all three connector rows.

## 4. Exact upper transparency

### Theorem 4.1 (external signatures)

The pointwise prefix-OR signatures of `X_d,Y_d` agree, and so do their
pointwise suffix-OR signatures.

#### Proof

The first active block is common.  The first screen, at `j=0`, is lower and
therefore fills all of `F`.  Thereafter the filler part of every prefix is
already `F`.  At a lower screen the active prefix is the contracted active
prefix through `V_j`; at an upper screen it is the contracted active prefix
through `V_(j+1)`.  Inside a block it is again a contracted active prefix.
All corresponding active prefix unions agree by (1.1).  Reverse the argument:
the last screen `j=10` is lower and fills `F`, so the suffix signatures agree
as well. \(\square\)

### Theorem 4.2 (complete internal OR support)

\[
                         \mathcal I_\vee(X_d)
                         =\mathcal I_\vee(Y_d).                  \tag{4.1}
\]

#### Proof

First separate the singleton lower screens.  Their seven values are

\[
              K\cup I\cup F,
\]

where `I` ranges over the common seven-element lower-colour set in (1.3), so
their support is identical in the two phases.  (The active part of such a
singleton is a rank-two intersection and need not itself be the union of an
active-vertex interval.)

Now consider an expanded interval containing a lower screen and at least one
block cell.  Its filler part is all of `F`.  Its active part is the union of a
contiguous active interval: an upper screen met at an endpoint may extend
that interval by one adjacent active triple, but does not make it
noncontiguous.  Hence every such value lies in the common family

\[
       \{K\cup F\cup A:A\in\mathcal I_\vee(P)\}
       =\{K\cup F\cup A:A\in\mathcal I_\vee(Q)\}.              \tag{4.2}
\]

Conversely every member of this family is realized in each phase, by taking
two cells of one block or the span of the corresponding blocks.  Thus all
full-filler interval values contribute exactly this common family.

Delete the seven lower screens.  Because the four upper indices in `E` are
isolated, every remaining component is either one block or

\[
                              B(V_j),U_j,B(V_{j+1})               \tag{4.3}
\]

for one `j in E`.  Intervals inside one block depend only on its active
triple: a singleton sees one coatom, while two or more cells fill `F`.

In (4.3), every interval meeting `U_j` has active part
`V_j union V_(j+1)`.  Its filler part is exactly one of

\[
 F^\circ,\qquad F-\{f_{n-1}\},\qquad F-\{f_0\},\qquad F,    \tag{4.4}
\]

according as it uses no adjacent block cell, only the last left cell, only
the first right cell, or any larger/bilateral piece.  Thus these values
depend only on the selected active union at `j`.  The four selected active
unions have the same multiset in `P,Q` by (1.3).  This exhausts all intervals
and proves (4.1). \(\square\)

The four filler/active-rank families in this proof are disjoint.  Since the
contracted active interval-OR deck has size `25`, the common expanded deck
has exact size

\[
                   12n+7+3\cdot4+25=12d+68.                    \tag{4.5}
\]

The equality is one of supports, not multiplicities.  By compressed-deck
replacement, either phase may replace the other inside any linear exterior
without losing a single old interval-union target.

## 5. Residence

### Theorem 5.1

Every positive coordinate run internal to either expanded fragment has
length at least

\[
                              n-1=d+1.                            \tag{5.1}
\]

The two phases have the same leading/trailing run state after clipping at
`d+1`.

#### Proof

Core coordinates are present everywhere.  Each active coordinate is constant
through every block in which it occurs, giving `n` consecutive positions.
A lower screen contains it only if both adjacent active triples do, while an
upper screen contains it if either does.  Screens can therefore extend or
join existing block runs but cannot create an isolated active run.  Every
internal active run has length at least `n`.

For `0<i<n-1`, filler coordinate `f_i` is absent once per block and present
at every screen, so consecutive absences are separated by `n` positive
positions.  Coordinates `f_0,f_(n-1)` are additionally absent at upper
screens.  Since upper screens are isolated, the shortest positive segment is
the `n-1` remaining cells of one adjacent block.  This proves (5.1).

At the fragment boundaries the first and last active triples are common.
Every active coordinate present there survives a whole block and saturates
the clipped state; absent ones have state zero.  The filler block order and
screen schedule are common, and core coordinates are saturated.  Hence the
clipped boundary states agree. \(\square\)

## 6. What this changes for the additive-constant program

Before this theorem, the positive compressed-deck ECO core failed scalable
residence, while resident thickening either repeated owners or lost the
internal deck.  The mixed coatom screen closes those rows simultaneously and
without an additive owner defect.  The local physical packet is no longer
the missing theorem.

Three global bridges remain.

1. **Task embedding / menu.**  A nonexceptional Pascal defect must expose a
   compatible active six-label ECO incidence and fixed core/filler placement.
   To use greedy/LLL selection, the admissible relabellings at a prescribed
   anchor must still form an `Omega(m^2)` menu after `O(md)` exclusions.
2. **Compiler U5.**  One phase choice must name a distinct deletion cell in
   the unused part of a fixed worst-frontier compiler matching, or the packet
   and all lower targets must be selected in one joint Hall matching.
3. **Regeneration.**  A same-parity Pascal lift must recreate the same packet
   interface and keep the number of carried tasks bounded.

The construction does not contradict the canonical independently sealed
`O(d)`-microcollar no-go.  It is a candidate-dependent ECO tensor proposed
for a bounded regenerative task set, not `Theta(W/d)` isolated standard
collars.

If the three bridges above are proved, the existing bounded-defect spine
immediately yields `nu(k) <= B(k)+C` for an absolute `C`.

## 7. Audit

Run

```bash
python3 scratch/audit_coatom_screen_tensor_resident_eco_packet_20260801.py
```

The self-contained audit checks all three authenticated active connector
rows for every `1 <= d <= 32`: ranks, literal Johnson adjacency, distinct
owners, owner multisets, endpoints, immediate intersection/union multisets,
pointwise prefix/suffix signatures, complete interval-OR support equality,
clipped boundary residence and every internal positive run.  It is a finite
replay supporting, not replacing, the all-`d` proofs above.

The independent minimal-splitter census
`scratch/audit_coatom_screen_crossed_orientation_splitter_20260801.py`
exhausts the `16*16` choices which cross exactly one occurrence of each
doubled lower-screen colour.  Exactly three paired choices work in every
authenticated row for owner current, signatures, internal OR support,
topology and residence, with transition sets `{1,3,5,7}`, `{2,5,8,10}`,
and `{3,4,7,10}`.  Only the first two also preserve both immediate palette
multisets; the third does not.  The separate complete `2^11` screen census
finds sixteen owner-simple transparent patterns, of which exactly ten
preserve both immediate palettes.  The displayed `E={1,3,5,7}` is the
canonical minimum-size fully palette-exact one.
