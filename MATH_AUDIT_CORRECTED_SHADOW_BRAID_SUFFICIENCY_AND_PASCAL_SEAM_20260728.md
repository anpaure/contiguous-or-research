# Audit of corrected Shadow--Braid sufficiency and the Pascal seam gate

Date: 2026-07-28

Status: the corrected fixed-braid theorem is proved and survives audit.  A
support/count-based Pascal seam implication is false, with sharp local
counterexamples at deadlines one and two.  An exact coordinate-position
witness interface is proved.  No unconditional all-`k` Pascal recursion and
no counterexample to the contiguous-OR conjecture is claimed.

## 0. Verdict

There are three logically different assertions.

1. **Fixed final chronology.**  If one is given an exact middle ordering,
   all lower pins in their final physical cells, all upper consecutive-union
   witnesses, and one common coordinatewise allowed-position system, then
   the maximal allowed word is a literal nonzero contiguous-OR word of the
   sharp length.  This assertion is valid.
2. **Fixed decorated braid.**  The cut-aware budgets are exact if, and only
   if, the old-occurrence ledger, disruption supports, and new final windows
   are exhaustive and incidence-aware.  With this convention, `SB0--SB4`
   are an exact fixed-braid certificate.  This assertion is valid.
3. **Pascal recursion.**  Parent occurrence survival, Johnson seams,
   nonempty erosion, and separately feasible sector compilers do not imply
   a common child compiler.  This proposed implication is false.  Its exact
   replacement must transport coordinate-position witnesses for every
   positive pin obligation and a nonempty-coordinate witness at every
   physical position.

The smallest central-collar failure occurs at the actual `k=4` deadline
`d=1`.  The first resident, pointwise-nonempty failure of sectorwise
compiler composition occurs at the actual `k=6` deadline `d=1`.  A stronger
deadline-two example additionally keeps a cut-aware natural lower seam pin
on a distinct physical cell, but fails the common-`Q` positive hit for that
pin; it first fits the actual middle-layer parameters at `k=7`.

Thus the corrected sufficient theorem is not circular, but its Pascal seam
existence hypothesis is still the entire open construction.  The results
below refute only weakened local or native-base seam rules.

## 1. Sharp-length notation

For a fixed dimension `k`, put

\[
 r=\left\lceil\frac{k}{2}\right\rceil,
 \qquad W=\binom{k}{r},
 \qquad \Lambda=\sum_{s=1}^{r-1}\binom{k}{s}.
\tag{1.1}
\]

Let `d=d(k)` be the least nonnegative integer such that

\[
 \Lambda\le dW+\binom{d+1}{2},
 \qquad B(k)=W+d.
\tag{1.2}
\]

For a set word `A=(A_0,...,A_{L-1})`, write

\[
 (D^tA)_i=\bigcup_{p=i}^{i+t}A_p.
\tag{1.3}
\]

Let

\[
 T=(T_0,\ldots,T_{W-1})
\tag{1.4}
\]

be a proposed ordering of the rank-`r` layer.  At physical length
`L=W+d`, define its maximal central erosion

\[
 E_p(T)=
 \bigcap_{\substack{0\le i<W\\i\le p\le i+d}}T_i,
 \qquad 0\le p<W+d.
\tag{1.5}
\]

The lower physical cells have the form

\[
 c=(t,i),\qquad 0\le t<d,\qquad 0\le i<W+d-t,
\tag{1.6}
\]

with interval `I_c=[i,i+t]`.  Their total number is exactly

\[
 \sum_{t=0}^{d-1}(W+d-t)
 =dW+\binom{d+1}{2}.
\tag{1.7}
\]

This is the monotone-deadline capacity appearing in (1.2).

## 2. Audited flat-middle theorem

Let `Pi` consist of the central pins

\[
 [i,i+d]\longmapsto T_i\qquad(0\le i<W)
\tag{2.1}
\]

together with selected lower, seam, endpoint, or boundary pins

\[
 I_c\longmapsto S_c.
\tag{2.2}
\]

No physical cell may carry two different labels.  For every coordinate
`x`, define

\[
 Q_x(\Pi)={0,\ldots,W+d-1\}\setminus
 \bigcup_{c:\,x\notin S_c}I_c,
\tag{2.3}
\]

where (2.3) includes the central pins (2.1).

### Theorem 2.1 (exact flat-middle certificate)

Assume all of the following.

1. `T` is a bijection onto `binom([k],r)`.
2. Every target of rank below `r` is assigned injectively to a valid cell
   (1.6), jointly with every mandatory lower seam, endpoint, and boundary
   pin.
3. For every pin `I_c -> S_c` and every `x in S_c`,

   \[
   Q_x(\Pi)\cap I_c\ne\varnothing.
   \tag{2.4}
   \]

4. Every physical position has a common allowed coordinate:

   \[
   \bigcup_xQ_x(\Pi)=\{0,\ldots,W+d-1\}.
   \tag{2.5}
   \]

5. Every target above rank `r` is a union of a consecutive block of `T`.

Then

\[
 A_p=\{x:p\in Q_x(\Pi)\}
\tag{2.6}
\]

is a nonzero set word of length `B(k)`, realizes every pin exactly, covers
every nonempty subset of `[k]`, and therefore

\[
 \boxed{\nu(k)=B(k).}
\tag{2.7}
\]

Conversely, every length-`B(k)` word whose depth-`d` row is a permutation
of the middle layer yields data satisfying conditions 1--5.

#### Proof

If `x notin S_c`, the definition of `Q_x` excludes `x` throughout `I_c`.
If `x in S_c`, (2.4) places `x` somewhere in `I_c`.  Hence the union of
(2.6) on `I_c` is exactly `S_c`.  Condition (2.5) makes every letter
nonempty.  In particular the central pins give

\[
 D^dA=T.
\tag{2.8}
\]

The selected lower pins cover the lower ideal and `T` covers the middle
layer.  For every valid `i,q>=0`,

\[
 \bigcup_{p=i}^{i+d+q}A_p
 =\bigcup_{j=0}^{q}T_{i+j}.
\tag{2.9}
\]

Thus condition 5 covers the upper ideal.  The word has length `W+d`; the
monotone-deadline lower bound gives (2.7).

For the converse, take an actual witness cell for each lower target.  Such
a witness must have depth `<d`: any interval of length at least `d+1`
contains a depth-`d` central window and hence has union of rank at least
`r`.  Distinct labels cannot use the same physical cell, so these choices
are jointly injective.  An upper-rank witness must have length greater than
`d+1`; its union equals the union of the consecutive central windows it
contains, giving condition 5.  The original word proves (2.4)--(2.5).
\(\square\)

The converse is only inside the flat-middle normal form.  Arithmetic slack
does not imply that every optimum exposes such a middle row.

### Corollary 2.2 (central pins, residence, and nonempty erosion)

With no noncentral pins, a literal nonzero word satisfying `D^dA=T` exists
if and only if

\[
 T_i=\bigcup_{p=i}^{i+d}E_p(T)
 \qquad(0\le i<W)
\tag{2.10}
\]

and

\[
 E_p(T)\ne\varnothing
 \qquad(0\le p<W+d).
\tag{2.11}
\]

In that event `A_p=E_p(T)` is the maximal central word.

#### Proof

For the central pins alone, (2.3) gives

\[
 Q_x=\{p:x\in E_p(T)\}.
\]

Condition (2.4) is exactly (2.10), coordinate by coordinate, while (2.5)
is exactly (2.11).  Apply Theorem 2.1.  \(\square\)

Thus the residence equation allowing empty set letters is not enough;
nonempty erosion is a separate literal-word condition.  After extra pins
are added, even (2.10)--(2.11) are not enough, because their negative
requirements can erase positive witnesses.

## 3. Exact cut-aware occurrence audit

Consider source middle chronologies cut into oriented pieces and rejoined
into a final chronology.  For a target `S`, let `O^+(S)` be the declared
old upper occurrences and `O^-(S)` the declared old natural lower
occurrences.  A lower occurrence of `q+1` middle vertices is eligible only
for

\[
 1\le q\le d;
\tag{3.1}
\]

otherwise it has no lower physical cell.  Let `C_Gamma` be the typed
disruption set and `N_Gamma^\pm(S)` the final seam-crossing windows.

### Theorem 3.1 (conditions for the cut-aware identity)

The identity

\[
 \beta_\Gamma^\pm(S)=
 \#\{P\in\mathcal O^\pm(S):
          \operatorname{supp}(P)\cap C_\Gamma=\varnothing\}
 +\#\mathcal N_\Gamma^\pm(S)-1
\tag{3.2}
\]

equals the number of final occurrences of `S` minus one if the ledger has
all four properties below.

1. The oriented pieces are position-disjoint, partition the selected
   source material, and are each used exactly once.
2. Every `O^\pm(S)` is exhaustive in the class called old, and every listed
   member is an actual source interval.
3. `supp(P)` includes every cut transition, selector-deleted vertex or
   index, and every other typed incidence whose disruption destroys `P`;
   `C_Gamma` is exact for those incidences.
4. `N_Gamma^\pm(S)` lists every distinct final interval crossing at least
   one new seam exactly once, at its actual label and depth.  A multi-seam
   interval is one interval, not several credits.

Reversal does not change an internal interval's union or intersection.
However, if a reversed lower middle occurrence becomes the final window
`[i,i+q]`, its physical pin is

\[
 [i+q,i+d],
\tag{3.3}
\]

not a formal reversal of its old physical interval.

#### Proof

Every final window is uniquely either wholly internal to one oriented old
piece or crosses at least one new seam.  In the first case exact support
disjointness is equivalent to survival; in the second case the window is
listed once in `N_Gamma`.  These two classes are disjoint and exhaustive,
which proves (3.2).  Formula (3.3) is the derivative-row dictionary for the
intersection of `q+1` final middle entries.  \(\square\)

If `C_Gamma` over-approximates disruption, (3.2) gives only a sufficient
lower bound.  If it under-approximates disruption, even sufficiency can
fail.  Merely recording cut endpoints is not an exact ledger.

### Lemma 3.2 (natural lower pins are negative-inert but not positive-safe)

Assume (2.10).  For a natural lower occurrence

\[
 S=\bigcap_{h=0}^{q}T_{i+h},\qquad1\le q\le d,
\tag{3.4}
\]

its correct physical interval satisfies

\[
 S=\bigcup_{p=i+q}^{i+d}E_p(T).
\tag{3.5}
\]

Consequently, adding the pin `[i+q,i+d] -> S` to the central system deletes
no element of any `E_p`: if `x notin S`, it was already absent from every
`E_p` in that interval.  Nevertheless, other exceptional pins may delete
all allowed positions of some `x in S`, so the natural pin must still pass
the final common-`Q` positive-hit test.

#### Proof

Equation (3.5) follows coordinatewise from (2.10), or equivalently from the
run description: a coordinate lies in every `T_i,...,T_(i+q)` precisely
when its eroded run meets `[i+q,i+d]`.  The negative-inert statement is
immediate from (3.5).  Positive safety is not monotone under the addition of
other negative interval constraints; Theorem 5.3 below gives an explicit
failure.  \(\square\)

Therefore (3.2) is exact for `SB2` and for the set-theoretic part of `SB3`.
It does not imply the literal compiler condition `SB4`.

## 4. Audited fixed-braid theorem

### Theorem 4.1 (fixed decorated Shadow--Braid equivalence)

Under the exact-ledger conventions of Theorem 3.1, a fixed decorated braid
produces a sharp-length flat-middle word if and only if all of the following
hold.

* `SB0`: its final middle chronology is the exact middle deck;
* `SB1`: the final chronology satisfies the exact residence equation
  (2.10);
* `SB2`: every upper target has `beta_Gamma^+(S)>=0`;
* `SB3`: every protected lower target has a selected surviving or new final
  occurrence at a valid depth `q<=d`, every residual lower target is
  assigned to an actual cell of depth `<d`, and all protected, residual,
  seam, endpoint, and boundary assignments are jointly cell-injective; and
* `SB4`: all these pins and the central pins satisfy the one common system
  (2.4)--(2.5).

Here “supports the decorated braid” means that every declared mandatory
decoration is realized as its actual final pin.  Under these hypotheses,
`nu(k)=B(k)`.

#### Proof

`SB4` and Theorem 2.1 give one literal word realizing the central and lower
pins.  `SB0` supplies the middle layer.  Theorem 3.1 and `SB2` supply an
actual final consecutive-middle-window witness for every upper target;
(2.9) lifts it to the same physical word.  The lower bound proves equality.

Conversely, choose actual witnesses from a flat-middle word.  The argument
in the converse of Theorem 2.1 gives valid lower depths and global cell
injectivity.  Partition every upper witness by Theorem 3.1 into its old
internal or new seam-crossing class.  The original word proves `SB4`.
\(\square\)

The residence line is logically implied by successful central pins in
`SB4`; it is retained as a fail-fast structural test.  For `d=0`, the
controller/run reformulation is unavailable and Theorem 2.1 must be used
directly.  Statements excluding a coordinate spanning the complete middle
deck assume `0<r<k`; `k=1` is the trivial exception.

The formal “Shadow--Braid induction theorem” obtained by assuming a child
braid satisfying `SB0--SB4` at every Pascal step is valid but conditional.
Its hypothesis already contains the missing recursive construction.

## 5. Exact common-`Q` seam criterion

It is useful to factor the central negative constraints out of (2.3).  Let
`Pi_0` be all noncentral pins and put

\[
 C_p=E_p(T)\cap
 \bigcap_{\substack{c\in\Pi_0\\p\in I_c}}S_c,
 \qquad
 Q_x=\{p:x\in C_p\}.
\tag{5.1}
\]

### Theorem 5.1 (literal seam criterion)

There is a nonzero word realizing every central and noncentral pin if and
only if

\[
 \begin{aligned}
 &C_p\ne\varnothing
     &&\text{for every physical position }p,\tag{CQ0}\\
 &Q_x\cap[i,i+d]\ne\varnothing
     &&\text{for every }i\text{ and }x\in T_i,\tag{CQ1}\\
 &Q_x\cap I_c\ne\varnothing
     &&\text{for every }c\in\Pi_0\text{ and }x\in S_c.\tag{CQ2}
 \end{aligned}
\tag{5.2}
\]

When they hold, `A_p=C_p` is the unique coordinatewise maximal feasible
word.

#### Proof

Every feasible word has `A_p \subseteq E_p` by the central negative
constraints and `A_p \subseteq S_c` for every pin covering `p`.  Thus
`A_p \subseteq C_p`.  Nonzeroness and all positive pin requirements imply
`CQ0--CQ2`.  Conversely, `A_p=C_p` is contained in every required label;
`CQ1--CQ2` give every positive coordinate a hit, and `CQ0` makes every
letter nonempty.  \(\square\)

This separates three gates that must not be conflated:

* the raw residence equation and raw erosion;
* post-pin physical nonemptiness `CQ0`; and
* central and extra-pin private hits `CQ1--CQ2`.

### Theorem 5.2 (first resident sectorwise common-`Q` obstruction)

At the actual `k=6` parameters,

\[
 r=3,\qquad W=20,\qquad \Lambda=6+15=21,
 \qquad d(6)=1,
\tag{5.3a}
\]

consider the rank-three Johnson path segment

\[
 T_{-1}=136,\qquad T_0=123,\qquad
 T_1=124,\qquad T_2=145.
\tag{5.3b}
\]

Its five local erosion letters are

\[
 136,\quad13,\quad12,\quad14,\quad145.
\tag{5.3c}
\]

They are all nonempty, and the segment is depth-one resident: coordinates
`3,2,4` have the two-middle-vertex runs
`T_{-1}T_0,T_0T_1,T_1T_2`; coordinate `1` spans the segment; and the
singleton runs of `6,5` meet its two linear endpoints.

Add the two distinct lower singleton pins

\[
 [1]\longmapsto\{3\},
 \qquad [2]\longmapsto\{2\}.
\tag{5.3d}
\]

Each one-pin system is feasible.  Their maximal local words are respectively

\[
 (136,3,12,14,145)
 \quad\text{and}\quad
 (136,13,2,14,145),
\tag{5.3e}
\]

and both retain every displayed central union.  With both pins, the maximal
word is

\[
 (136,3,2,14,145).
\tag{5.3f}
\]

Every physical letter remains nonempty and both extra pins are exact, but

\[
 Q_1\cap[1,2]=\varnothing,
 \qquad A_1\cup A_2=23\ne123=T_0.
\tag{5.3g}
\]

The intended seam `123|124` is Johnson and has the correct set-theoretic
windows

\[
 123\cap124=12,
 \qquad123\cup124=1234.
\tag{5.3h}
\]

Thus a cut-aware ledger can correctly retain those target occurrences while
the literal central compiler still fails.  If the natural lower value `12`
is selected at its depth-zero seam cell `[2]`, it also conflicts with the
already selected label `{2}` on that cell; this is why global cell
injectivity and common-`Q` installation are separate from occurrence
survival.

This is minimal among local obstructions satisfying: the actual deadline is
one; there is a Johnson seam; two distinct nonempty singleton lower targets
occupy the two physical positions of one central window; each one-pin
system is feasible; and the combined maximal word stays pointwise nonempty
but loses a central positive coordinate.  Rank two cannot work, because
after omitting the lost coordinate both nonempty singleton labels would be
the same remaining coordinate.  Hence `r>=3`.  The only smaller actual
dimension with `r>=3` is `k=5`, but `d(5)=2`; (5.3a)--(5.3g) attain the
first possible case `k=6`.

This is a scoped minimum for sectorwise compiler composition, not a full
Pascal child counterexample.

### Theorem 5.3 (minimal natural-seam common-`Q` obstruction)

Let `d=2`.  On coordinates `x,y,z,a,b`, take the Johnson seam

\[
 T_0=\{x,y,z,a\},\qquad T_1=\{x,y,z,b\}.
\tag{5.3}
\]

Its erosion on positions `0,1,2,3` is

\[
 (E_0,E_1,E_2,E_3)
 =(xyza,xyz,xyz,xyzb).
\tag{5.4}
\]

Both central rows are exact and every erosion letter is nonempty.  The
natural lower seam occurrence is

\[
 S=T_0\cap T_1=xyz
\tag{5.5}
\]

at its correct physical cell `[1,2]`.  Add the two distinct lower pins

\[
 [1]\longmapsto\{y\},
 \qquad [2]\longmapsto\{z\}.
\tag{5.6}
\]

Then:

1. all three lower targets and cells are distinct;
2. the protected seam occurrence exists and may have exact new-occurrence
   budget `beta_Gamma^-(S)=0+1-1=0`;
3. each one-blocker subsystem has a common literal word realizing `S`;
4. after both blockers, every `C_p` is nonempty and both central rows remain
   exact; but
5. the combined system has no literal realization of the natural seam pin.

Indeed,

\[
 (C_0,C_1,C_2,C_3)=(xyza,y,z,xyzb),
\tag{5.7}
\]

so

\[
 C_0\cup C_1\cup C_2=T_0,
 \qquad C_1\cup C_2\cup C_3=T_1,
\tag{5.8}
\]

but

\[
 Q_x\cap[1,2]=\{0,3\}\cap[1,2]=\varnothing,
 \qquad C_1\cup C_2=yz\ne xyz.
\tag{5.9}
\]

With only the first blocker, `(xyza,y,xyz,xyzb)` is feasible; with only the
second, `(xyza,xyz,z,xyzb)` is feasible.  Thus residence, raw and post-pin
nonempty erosion, Johnson adjacency, target support, cut-aware budget, cell
injectivity, and separate compilers do not imply the common child compiler.

This example is minimal in the following natural two-window class: the
failed pin is the intersection of two distinct equal-rank central windows;
all labels are nonempty and distinct; blockers use distinct lower cells;
all post-pin letters are nonempty; and both central rows remain exact.
Necessarily `d>=2`.  At `d=2` the natural cell has two positions, so erasing
one coordinate with distinct nonempty blockers requires at least two other
coordinates in `S`; hence `|S|>=3`.  The two distinct equal-rank central
sets then have rank at least four and need two distinct outside coordinates,
so at least five ground coordinates are necessary.  Equations
(5.3)--(5.6) attain all these bounds.  For the actual parameters
`r=ceil(k/2),d=d(k)`, the first compatible dimension is `k=7`, where

\[
 r=4,\quad W=35,\quad
 \Lambda=63,\quad d(7)=2
\tag{5.10}
\]

because `W+1=36<63<=2W+3=73`.  This is local minimality; extension of the
collar to a full exact `k=7` braid is not asserted or needed to refute a
local seam implication.

### Proposition 5.4 (smallest nonempty-erosion central-collar failure)

At the actual `k=4` parameters `r=2,W=6,d=1`, take three consecutive middle
states

\[
 T_{a-1}=\{1,2\},\qquad
 T_a=\{2,3\},\qquad
 T_{a+1}=\{2,4\}.
\tag{5.11}
\]

Both transitions are Johnson, both adjacent intersections are the nonempty
set `{2}`, and both adjacent upper unions have the correct rank three.  All
four local erosion letters are nonempty.  Nevertheless coordinate `3` has
the final trace `0,1,0`, so (2.10) fails at `T_a`.  Equivalently, the two
erosion states incident with it both equal `{2}` and the controller repeats
rather than making a nontrivial step.  In common-`Q` form, the central pins
on `[a-1,a]` and `[a+1,a+2]` forbid coordinate `3` at both positions of the
middle central interval `[a,a+1]`, so `CQ1` fails.

This is minimal among deck-injective local collars with distinct middle states,
nonempty adjacent erosions, and `d>0`: `d=0` has no mixed erosion state;
three central vertices are needed to make a piece-end run internal; rank one
cannot have nonempty intersections between distinct vertices; and the three
rank-two sets on a three-coordinate ground set give each coordinate of the
middle set to at least one neighbor.  A fourth coordinate first permits
(5.11).

This obstruction refutes Johnson-seam plus nonempty-erosion rules before
the compiler is considered.  Theorem 5.3 is stronger in a different
direction: it passes central residence and fails only the simultaneous
lower-pin compiler.

### Proposition 5.5 (`CQ0` is independent)

On positions `0,1,2`, the two pins

\[
 [0,1]\longmapsto\{a\},\qquad
 [1,2]\longmapsto\{b\}
\tag{5.12}
\]

have `Q_a={0}` and `Q_b={2}`.  Every positive pin requirement passes and
the interval incidence matrix is consecutive-ones and totally unimodular,
but position `1` has no allowed coordinate.  Hence no nonzero word realizes
the pins.  Two pins and three positions are minimal among crossing-interval
examples.  Thus interval TU and positive hits do not imply literal
nonemptiness.

## 6. Exact recursive interface

For every central positive coordinate create an obligation

\[
 (i,x),\qquad x\in T_i,qquad J(i,x)=[i,i+d],
\tag{6.1}
\]

and for every noncentral pin create

\[
 (c,x),\qquad x\in S_c,qquad J(c,x)=I_c.
\tag{6.2}
\]

An admissible witness is a position

\[
 p\in J(b,x)\cap Q_x.
\tag{6.3}
\]

### Theorem 6.1 (coordinate-protected seam transport)

A fixed final decorated seam has a literal common compiler if and only if:

1. every obligation (6.1)--(6.2) has an admissible witness (6.3); and
2. every physical position `p` has a coordinate `x_p` with `p in Q_(x_p)`.

Consequently, a cut/reversal/reconnection is recursive exactly when every
transported obligation carries a named coordinate-position witness, every
witness remains in its actual final interval and final erosion and survives
all final negative pins, every destroyed or new obligation gets a new
witness, and every final physical position retains a nonempty-coordinate
witness.

#### Proof

The two assertions are precisely `CQ1--CQ2` and `CQ0`, with an element
chosen from each nonempty set.  Apply Theorem 5.1.  \(\square\)

Witnesses are not a matching: different obligations may share a position.
The obstruction is that negative interval constraints can cover all
eligible positions for one coordinate.  This is why target-level occurrence
counts cannot replace Theorem 6.1.

For localization, let `Z` contain every physical position whose erosion
changes, every added/deleted/moved/relabelled pin interval, and every final
physical interval crossing an old or new cut.  Outside `Z`, a named witness
transports verbatim.  It is necessary and sufficient to recheck obligations
with no surviving outside witness, all central windows meeting `Z`, every
changed or crossing pin, and nonemptiness on `Z`.  This is an exact local
audit, not a scalar seam allowance.

### Corollary 6.2 (sharp elementary collar counts)

Suppose `J` old transition slots are cut and the resulting pieces are joined
through `J` new seams.  Before overlaps and endpoint truncation, the union
of old and new erosion collars has at most

\[
 2dJ
\tag{6.4}
\]

physical positions.  At flag depth `q`, at most `qJ` old windows meet a
deleted transition and at most `qJ` final windows cross a new transition;
therefore the old/new depth-`q` window symmetric difference has size at
most

\[
 2qJ.
\tag{6.5}
\]

If `M` changed noncentral pins all have depth `<d`, their interval union adds
at most `dM` positions to the crude collar bound.

#### Proof

A transition between middle positions `a,a+1` lies in exactly the mixed
erosion positions `a+1,...,a+d`, except for endpoint truncation.  Count both
deleted and inserted transitions.  An edge belongs to at most `q` windows
of `q+1` consecutive middle vertices, proving (6.5).  A depth-`t<d` cell
has interval length `t+1<=d`.  \(\square\)

These are localization bounds only.  They do not imply any private hit,
target replacement, or common compiler.

## 7. A second obstruction: protected-occurrence links

The source-only safe-cut complex for a protected family `P` is

\[
 \mathcal K_{\mathcal P}
 =\{C:\text{every protected target has an old occurrence whose support
 avoids }C\}.
\tag{7.1}
\]

Residence hazards form a clutter that the cut set must hit.  These two
conditions have opposite monotonicity.

The smallest extension failure has ground cut edges `{e_1,e_2}`.  Give one
protected target two old occurrences, supported respectively on `e_1` and
`e_2`.  Then

\[
 \mathcal K=\{\varnothing,\{e_1\},\{e_2\}\}=U_{1,2}.
\tag{7.2}
\]

After choosing the safe first-generation cut `{e_1}`, the link is
`{emptyset}`.  If the next residence hazard forces the cut `e_2`, no safe
extension exists.  Thus “safe at one generation” does not imply
“extendible at the next generation.”

This abstract obstruction occurs exactly in the standard native
same-parity architecture.  Put

\[
 C_r=\frac1{r+1}\binom{2r}{r}.
\]

### Proposition 7.1 (native extreme-shore link zero)

If `E_S` is the first-shadow edge-colour class of `S`, then the safe
deletion complex is

\[
 \bigoplus_S U_{|E_S|-1,|E_S|}.
\tag{7.3}
\]

The Catalan deletion retains one representative of every colour, spends
all `C_r-1` available deletions, is a base of (7.3), and has zero deletion
link.  The corresponding one-representative `U` value-fibre selector is
also a partition-matroid base with zero deletion link.  Ordinary
cross-sector seams cannot replace the two extreme signatures: their lower
intersection tags never contain both new coordinates, and their upper union
tags are never empty.  Hence the standard “freeze both native bases and
then add a positive-rank internally protected seam atlas” step is
impossible.

#### Proof

A first-shadow colour survives internally exactly when not all edges in its
class `E_S` are deleted.  The colour classes partition the edge ground set,
so their independent capacity constraints give (7.3).  Its rank is the sum
of `|E_S|-1`.  The native completed first-shadow path has `W-1` edges and
`W-C_r` colours; hence this rank equals

\[
 (W-1)-(W-C_r)=C_r-1.
\]

The Catalan deletion has this size and retains one edge in every class, so
it is a base and its matroid link contains only the empty extension.  The
same argument in each `U` value fibre proves the selector assertion.

In the native `UYAX` signature table, every ordinary cross-sector lower
intersection omits at least one of the two new tags, while every ordinary
cross-sector upper union contains at least one new tag.  Such a seam can
therefore create neither a both-new lower occurrence nor an empty-signature
upper occurrence.  Thus it cannot replace an extreme occurrence destroyed
after the corresponding base is frozen.  \(\square\)

This does not rule out joint basis reselection, balanced same-signature
exchanges, off-spine rethreading, compatible endpoint/compiler repair, or a
fresh child construction.

### Proposition 7.2 (finite raw-buffer obstruction)

If the relative residence buffer at dimension `k_i=k_0+2i` is `beta_i`,
direct first-shadow transport gives

\[
 \beta_n\le\beta_0-n-(d(k_n)-d(k_0))\le\beta_0-n.
\tag{7.4}
\]

Thus no finite initial scalar buffer closes all odd dimensions by the raw
adjacent-row functor.  This is independent of the common-`Q` and
protected-link obstructions.

#### Proof

At one `k -> k+2` step the first-shadow row consumes one absolute residence
level.  If the deadline rises by
`epsilon_i=d(k_(i+1))-d(k_i) in {0,1}`, the relative buffer therefore obeys

\[
 \beta_{i+1}\le\beta_i-1-\epsilon_i.
\]

Summing over `i=0,...,n-1` telescopes the deadline increments and gives
(7.4).  The right-hand side is negative for `n>beta_0`, independently of
the additional deadline loss.  \(\square\)

## 8. Exact all-`k` boundary

The following statements are proved.

1. The corrected flat-middle sufficient theorem is exact, including all
   constants and the literal nonzero-word condition.
2. The fixed-braid `SB0--SB4` theorem is exact under the exhaustive,
   incidence-aware ledger hypotheses of Theorem 3.1.
3. A natural lower occurrence supplies only a candidate final physical pin;
   it must still pass the common positive-hit condition after all
   exceptional pins are imposed.
4. Theorems 5.2--5.3 refute any Pascal seam rule based only on Johnson adjacency,
   cut-aware target survival, nonempty erosion, cell injectivity, and
   separately feasible sector compilers.
5. Theorem 6.1 is the exact coordinate-level interface that repairs the
   false implication.
6. The native frozen-base Pascal extension has the independent link-zero
   obstruction of Section 7, and raw scalar buffers cannot iterate forever.

The following statements are not proved.

* There is no proof that every Pascal child admits the witness transport of
  Theorem 6.1.
* The local collar of Theorem 5.3 is not asserted to extend to a complete
  exact `k=7` child deck with all other `SB` data.
* No obstruction here applies to an adaptive braid that recomputes the full
  final occurrence ledger and explicitly satisfies `CQ0--CQ2`.
* No result here disproves `nu(k)=B(k)` or gives the missing all-`k` upper
  bound.

The sharp remaining Pascal theorem is therefore not a target-count or
rankwise Hall statement.  It must construct one child chronology and one
joint pin system for which cut-aware occurrence survival, residence,
`CQ0`, `CQ1`, and `CQ2` hold simultaneously, with every lower label assigned
to one actual final physical cell.

## 9. Independent decisive-step audit

The two decisive computations are coordinatewise and require no finite
search.

* In (5.11), coordinate `3` is forbidden at both positions of its required
  middle central interval, so central `CQ1` fails although every erosion
  set is nonempty.
* In (5.3a)--(5.3g), each singleton blocker leaves one of the two allowed
  positions for coordinate `1`, whereas their combination deletes both.
  The resulting word is still pointwise nonempty, so this is a pure central
  positive-hit failure after resident sectorwise composition.
* In (5.3)--(5.9), the two blockers delete `x` exactly at positions `1,2`
  and nowhere else.  Hence the central windows recover `x` at their outer
  positions, every physical letter remains nonempty, but the natural seam
  pin has no allowed `x` position.  Removing either blocker restores one
  allowed `x` position.  This verifies both failure and inclusion-minimality
  of the blocking pair.

These checks independently separate the three necessary seam conditions:
nonempty erosion, central residence, and simultaneous common-`Q` pin
recovery.
