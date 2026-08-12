# From the exact words to one mathematical target

Date: 2026-07-28

Status: theorem-level synthesis.  No `k=15` solution is claimed.

## 0. Main conclusion

The exact words through `k=14` and the Hall-29 carrier at `k=15` are best
viewed through one object, not through separate residence, shadow, Hall, and
compiler searches.

Let

\[
  A=(A_0,\ldots,A_{W+d-1}),\qquad T=D^dA,
\]

where `T` is the middle chronology.  Its maximal erosion is

\[
  P_p=\bigcap_{\max(0,p-d)\le i\le\min(W-1,p)}T_i.
\]

For a resident Johnson chronology, the short cells of `P` are exactly the
consecutive-intersection tableau of `T`.  The lower compiler then only
chooses nested local cuts of that tableau.  This gives the following single
sufficient target for the conjectured equality `nu(k)=B(k)`:

> Construct an upper-complete, depth-`d` resident ordering of the middle
> layer whose consecutive-intersection tableau admits an injective lower
> target assignment with pointwise owner meet dimension at most two.

All parts of that sentence except existence are exact theorems below.  The
bound two is empirical: it is one through `k=13` and two at exactly five
positions for `k=14`.

## 1. The erosion/intersection identity

Assume that every internal run of every coordinate in `T` has length at
least `d+1`.  This is exactly the condition that `D^dP=T`.

### Theorem 1.1 (intersection tableau)

For `1<=q<=d`, away from the two boundary ramps,

\[
  \boxed{
  (D^{d-q}P)_{i+q}=\bigcap_{h=0}^{q}T_{i+h}.}
  \tag{1.1}
\]

At a boundary the same formula holds after clipping the displayed middle
index interval to `[0,W-1]`.

#### Proof

It is enough to work coordinatewise.  On one run `[a,b]` of a coordinate in
`T`, the coordinate occurs in `P_p` precisely for

\[
                  a+d\le p\le b.
\]

The source interval on the left of (1.1) meets `[a+d,b]` precisely when the
run contains all middle indices `i,...,i+q`.  The only possible failure of
this equivalence would be a run shorter than `d+1`, which is excluded by
residence.  Taking the union over coordinate runs proves (1.1).  Clipping
the erosion windows gives the boundary statement.  \(\square\)

This identity is the exact explanation for the OR--Pascal rank grading seen
in every stable optimum.  It is not an extra empirical pattern.

### Theorem 1.2 (rank grading)

Suppose additionally that consecutive `T_i` are Johnson adjacent and every
newly inserted coordinate survives the next `d` transitions.  Then

\[
 \left|\bigcap_{h=0}^{q}T_{i+h}\right|=r-q
 \qquad(0\le q\le d).
 \tag{1.2}
\]

#### Proof

Across the `q` transitions, an element inserted inside the block cannot be
deleted again, by residence.  Hence all `q` deletions remove distinct
elements already present in `T_i`.  The intersection is `T_i` with exactly
those `q` elements removed.  \(\square\)

Put `s=r-d`.  A short cell of depth `h` (length `h+1`) therefore has maximal
rank `s+h` in the interior.  Consequently an interior target of rank `t`
cannot be assigned above row

\[
                         h=\max(0,t-s).
 \tag{1.3}
\]

It may be assigned to that nominal row or to a deeper row after compiler
cuts.  This proves the forced half of the observed `nominal or one row
deeper` rule and explains why degree-one peeling at `k=15` proceeds in the
order

\[
  (\text{rank }7,\text{depth }2),\quad
  (\text{rank }6,\text{depth }1),\quad
  (\text{rank }5,\text{depth }0).
\]

## 2. Deleted-symbol chains and cross-depth correlation

Write the Johnson transition `T_i -> T_{i+1}` as deleting `a_i` and
inserting `b_i`.  Theorem 1.2 gives, simultaneously for every `q<=d`,

\[
  \boxed{
  \bigcap_{h=0}^{q}T_{i+h}
   =T_i\setminus\{a_i,a_{i+1},\ldots,a_{i+q-1}\}.}
 \tag{2.1}
\]

Thus one starting position supplies the whole nested flag

\[
 T_i-a_i\supset
 T_i-\{a_i,a_{i+1}\}\supset\cdots\supset
 T_i-\{a_i,\ldots,a_{i+d-1}\}.
 \tag{2.2}
\]

The lower depths are therefore not separate covering problems.  They are
the levels of one deletion-chain system.  This is the deterministic
correlation that the earlier independent-depth entropy ledger omitted.

The upper tableau has the dual form

\[
  \bigcup_{h=0}^{q}T_{i+h}
   =T_i\cup\{b_i,b_{i+1},\ldots,b_{i+q-1}\}
 \tag{2.3}
\]

under the corresponding no-early-reuse condition.  Hence the carrier
problem is a two-sided flag-ordering problem on one transition word.

The raw exact answers give a particularly clean calibration.  Counting only
the internal consecutive intersections (before using either boundary ramp),
their lower hole vectors are:

\[
\begin{array}{c|c|c}
k&d&(h_1,\ldots,h_d)\\ \hline
9&2&(1,1)\\
10&2&(0,0)\\
11&3&(1,1,0)\\
12&2&(0,0)\\
13&3&(1,0,0)\\
14&2&(0,0).
\end{array}
\tag{2.4}
\]

Every internal coordinate run in these six chronologies has the exact
theoretical minimum `d+1` or more.  Thus the solved instances do not cover
the depths independently: one resident deletion word is simultaneously
perfect, or within one boundary flag of perfect, at every relevant depth.
For comparison the current `k=15` carrier has `(4,21,4)`.

## 3. The exact odd-dimensional immediate-shadow tax

Let `k=2r-1`, so

\[
  W=\binom{k}{r}=\binom{k}{r-1}.
\]

A spanning cover by `p` middle paths has `W-p` internal adjacent
intersections of rank `r-1`.  Let `h_1` be the number of missing
`(r-1)`-sets and let `c_1` be the total repeat excess among those colours.

### Lemma 3.1

\[
                         \boxed{h_1=c_1+p.}
 \tag{3.1}
\]

#### Proof

The number of distinct colours is both `W-h_1` and `(W-p)-c_1`.
\(\square\)

This is the exact palette algebra behind the successful seam construction:
a join using a missing colour decreases `p` and `h_1` together, while a join
using an already present colour decreases `p` but increases `c_1`.

At optimal length the nominal first-shadow row has `W+1` cells: the
`W-1` internal intersections and its two boundary-ramp cells.  Shallower
rows can also have rank-`r-1` envelopes at the ramps, so the simpler
rank-only argument is false there.  The exact boundary-wing classification
repairs it: every such eligible cell lies on one of the same two nested
endpoint chains, and a nested chain contains at most one distinct set of a
fixed rank.  Therefore every optimal resident flat construction must satisfy

 \[
                         \boxed{h_1\le2,qquad c_1\le1.}
 \tag{3.2}
 \]

For one final path, (3.1) reads `h_1=c_1+1`.  The current Hall-29 carrier has
`h_1=4,c_1=3`.  It is therefore exactly two
immediate-shadow units beyond what the two boundary flags can absorb.  This
is a theorem-level explanation of why it is close but not compilable.

## 4. Pointwise owner meets

Fix an injective assignment `phi` of lower targets `X` to short physical
intervals `I_X`.  At source position `p`, put

\[
 \mathcal O_p=\{X:p\in I_X\},\qquad
 A_p=P_p\cap\bigcap_{X\in\mathcal O_p}X.
 \tag{4.1}

The owner meet dimension is

\[
 \kappa_p=\min\left\{|S|:S\subseteq\mathcal O_p,
 P_p\cap\bigcap_{X\in S}X=A_p\right\}.
 \tag{4.2}

When `kappa_p<=1`, choose an active owner `O_p` with

\[
                         A_p=P_p\cap O_p,
 \tag{4.3}

or use the empty owner when `A_p=P_p`.  Equivalently, the traces
`{P_p cap X:X in O_p}` have a least member.  The full global negative-window
system then becomes the following local dominance system.

### Theorem 4.1 (nested-owner realization)

An injective interval assignment with `kappa_p<=1` is realizable if and only
if one can select active owners `O_p` so that

\[
 P_p\cap O_p\subseteq X
 \quad(p\in I_X),                                      \tag{4.4}
\]

\[
 X\subseteq\bigcup_{p\in I_X}(P_p\cap O_p),           \tag{4.5}
\]

\[
 T_i\subseteq\bigcup_{p=i}^{i+d}(P_p\cap O_p),        \tag{4.6}
\]

and every `P_p cap O_p` is nonempty.

#### Proof

Equation (4.4) is the negative part of every pin.  Equation (4.5) is its
positive part.  Equation (4.6) is exactly `D^dA=T`, since every entry is
already contained in all middle windows defining `P_p`.  Nonemptiness is
the nonzero-word condition.  These are precisely the fixed-middle full-
witness equations after substituting (4.3).  \(\square\)

This theorem explains both sides of the raw census:

* the assignment is globally nonlocal because a target may own a far-away
  interval;
* its final coordinate dependence is locally tiny because one active owner
  usually dominates every other owner trace at a position.

The exact data are

\[
 \max_p\kappa_p\le1\quad(6\le k\le13),
 \qquad
 \#\{p:\kappa_p=2\}=5\quad(k=14).
 \tag{4.7}

Thus ordinary Hall is too weak, but the missing information is a bounded
local meet condition rather than a second global matching problem.

The `k=14` six-piece odd-to-even braid fits this split exactly.  The six
pieces are a global operation needed to create the required short run of the
new coordinate while restoring two lost upper colours.  After that global
chronology is fixed, the compiler's only departure from one-owner form is
the five local binary meets in (4.7).  The construction is globally braided
but locally width two.

## 5. What Hall 29 actually is

On the best `k=15` carrier the three raw lower-shadow hole counts are

\[
                         4,quad21,quad4,
 \tag{5.1}

and their sum is the exact compiler deficiency `29`.  This equality is not
universal over all saved carriers, so it is a diagnostic, not an identity.
It nevertheless agrees with the exact degree-one peeling:

* 1,013 forced rank-7/depth-2 owners;
* 395 forced rank-6/depth-1 owners;
* 81 forced rank-5/depth-0 owners;
* a residual `35 targets / 6 cells` kernel.

The residual consists of 23 isolated targets and six `two targets -> one
cell` collisions.  Hence its deficiency is literally

\[
                         23+6=29.                       \tag{5.2}
\]

There is a sharper conservation picture.  Compare the raw shadow holes with
the peeled residual:

\[
\begin{array}{c|c|c}
\text{rank}&\text{raw intersection holes}&
 \text{targets surviving in the peeled kernel}\\ \hline
7&4&8\ (=2\text{ holes}+6\text{ collision partners})\\
6&21&17\ (=17\text{ holes})\\
5&4&1\ (=1\text{ hole})\\
4&-&9\ (=9\text{ isolated spill targets}).
\end{array}
\tag{5.3}
\]

Thus 20 of the 29 raw holes survive at their own ranks.  The other nine are
absorbed by boundary/deeper-row capacity, but that use of capacity displaces
exactly nine rank-four targets.  The six shared residual cells pair six of
the rank-six holes with six otherwise available rank-seven targets.  Counting
defect tokens after this transport gives

\[
  (2+11+1+9)\text{ isolated}
  +6\text{ collisions}=29.                             \tag{5.4}
\]

So, on this carrier, degree-one peeling does not destroy the shadow deficit;
it transports nine units down the graded tableau and converts six units into
collisions.  This is the concrete finite model for a possible general
"defect-flow" theorem.

If the 1,489 peeled owners are preserved, any successful repair must match
at least 29 residual targets to distinct cells outside the old six-cell
kernel.  This is the exact fresh-cell theorem.  It explains why increasing
one old DM-neighbourhood count can merely transport the obstruction.

An independent channel audit found and quarantined an allocation-order bug in
the first native test of one precise transport convention.  The corrected
two-pass channel was then checked on all 32,178 mask rows and 19,305 boundary
bits with zero errors.  On that corrected channel, the unrestricted
five-parent H29-anchor-transported owner architecture is again UNSAT: the
correct formula has 842,541 variables and 4,942,711 clauses, and its new DRAT
proof was independently verified by `drat-trim`.  Consequently, inside that
precise architecture, a solution must change a transported frozen owner, use
an option beyond the retained defect-at-most-one atlas, or leave the
five-parent arc union.  This does **not** close ordinal-position ownership,
other owner transports, defect-two options, or a larger arc catalogue.  The
corrected model, semantic audit, proof hashes, and invalid-artifact quarantine
are recorded in `K15_NATIVE_CHRONOLOGY_OWNER_FORMULATION_20260728.md`.

The finite local-transfer census adds a scoped fact: no globally intrinsic
single transfer of support at most nine, and no parent-pure transfer of
support at most seven, improves 29.  A larger fixed-endpoint path-closure
census is **not** a global support lower bound, because disjoint alternating
cycles may be added; that scope correction is essential.

## 6. The resulting construction problem

The exact formula would follow from a uniform construction of the following
object.  The unrestricted five-parent no-go above is why the target is stated
globally rather than as a repair of the H29 owner skeleton.

### Nested-owner flag chronology

For `r=ceil(k/2)` and `d=d(k)`, find an ordering `T` of all rank-`r` sets
such that:

1. consecutive sets are Johnson adjacent;
2. every coordinate run has length at least `d+1`;
3. all upper consecutive unions occur;
4. its deletion-chain tableau (2.2), with the boundary ramp, admits an
   injective owner assignment for all lower targets; and
5. that assignment satisfies Theorem 4.1, or its `kappa<=2` analogue.

Given such data, set

\[
 A_p=P_p\cap O_p
\]

(or intersect the two active owners at the exceptional positions).  The
upper identity `D^{d+q}A=D^qT`, the intersection-tableau theorem, and the
owner realization theorem then give a universal word of length `W+d=B(k)`.
The monotone-deadline lower bound gives equality.

This formulation reconciles all current observations:

* PBBS-like carriers pay for many depths with one deletion-chain choice;
* residence forces the observed rank grading;
* exact solutions are globally rearranged but locally one/two-owner;
* the Hall-29 obstruction is a 29-cell transversal shortage in the same
  tableau; and
* isolated local switches fail because they change only bounded collars of
  the deletion-chain system.

The remaining theorem is therefore not “Hall zero” by itself and not
“Hamiltonicity” by itself.  It is existence of one nested-owner flag
chronology.
