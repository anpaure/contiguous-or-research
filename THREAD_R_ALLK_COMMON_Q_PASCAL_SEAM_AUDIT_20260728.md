# Thread R: common-\(Q\) audit of the Pascal Shadow--Braid seam

Date: 2026-07-28

Status: exact fixed-seam literalization theorem; exact coordinate-protected
recursive interface; a minimal local depth-two counterexample to every seam
claim based only on target support/count, nonempty erosion, and separately
feasible sector compilers.  No unconditional Pascal recursion or all-\(k\)
upper bound is claimed.

## 0. Verdict

The corrected fixed-braid Shadow--Braid theorem in
`THREAD_D_EXACT_SHADOW_BRAID_INDUCTION_AND_CUT_AWARE_OBSTRUCTION_20260728.md`
is logically valid, provided its hypotheses are read literally:

* `SB2` is an upper-occurrence condition;
* `SB3` says that a protected lower occurrence supplies an **actual final
  physical pin**, not merely a target label or an intersection in the maximal
  erosion; and
* `SB4` rechecks every positive coordinate of every pin in one common
  allowed-position system.

In particular, `SB3` does not imply `SB4`.  That separation is essential.
The Pascal-recursive seam step is still unproved: parent support ledgers,
even with exact cut-aware occurrence counts and nonempty maximal erosion,
do not imply the child common-\(Q\) condition.

There are two boundary corrections that must remain explicit.

1. The equality

   \[
   T_i=\bigcup_{p=i}^{i+d}E_p(T)
   \tag{0.1}
   \]

   is coordinatewise residence allowing empty physical letters.  It is not
   by itself residence by a nonzero set word.  Nonemptiness of every final
   allowed letter is an additional condition.
2. A lower intersection window surviving inside an oriented middle piece
   transports its **label**, but not automatically its physical compiler
   interval.  After a cut, reversal, or reindexing, the final interval must
   be recomputed.  Every interval crossing an old or new cut is a new child
   pin obligation unless its whole physical support is explicitly
   transported.

The exact seam invariant is coordinate-protected, not target-counted: one
must retain one allowed physical position for every positive coordinate of
every central or lower pin, and one allowed coordinate at every physical
position.

## 1. Exact notation

Fix a proposed child middle chronology

\[
T=(T_0,\ldots,T_{W-1})
\]

and a deadline `d`.  Its physical positions are

\[
\Omega=\{0,1,\ldots,W+d-1\}.
\]

For `p in Omega`, define the maximal central erosion

\[
E_p=
\bigcap_{\substack{0\le i<W\\i\le p\le i+d}}T_i.
\tag{1.1}
\]

Let `Pi` be the family of all **noncentral** selected pins.  A pin
`c in Pi` consists of a physical interval `I_c` and a nonempty label
`S_c`.  The family includes every protected natural lower pin that is to be
used in the final word, every spill pin, and every seam, endpoint, or
boundary pin.

Put

\[
C_p=E_p\cap\bigcap_{\substack{c\in\Pi\\p\in I_c}}S_c.
\tag{1.2}
\]

The empty intersection over pins is the whole ground set, so with no active
extra pin one has `C_p=E_p`.  Equivalently, for each coordinate `x`,

\[
Q_x=\{p\in\Omega:x\in C_p\}
=\{p:x\in E_p\text{ and every pin covering }p\text{ contains }x\}.
\tag{1.3}
\]

Thus `C_p={x:p in Q_x}` is the maximal letter surviving all central and
noncentral negative requirements.

## 2. Exact local literal-seam theorem

### Theorem 2.1 (common-\(Q\) seam criterion)

There exists a word of nonempty sets

\[
A=(A_0,\ldots,A_{W+d-1})
\]

such that

\[
\bigcup_{p=i}^{i+d}A_p=T_i
\qquad(0\le i<W)
\tag{2.1}
\]

and

\[
\bigcup_{p\in I_c}A_p=S_c
\qquad(c\in\Pi)
\tag{2.2}
\]

if and only if all three conditions below hold.

**CQ0 (post-pin nonempty erosion).**

\[
C_p\ne\varnothing\qquad(p\in\Omega).
\tag{2.3}
\]

**CQ1 (central positive hits).**  For every `i` and every `x in T_i`,

\[
Q_x\cap[i,i+d]\ne\varnothing.
\tag{2.4}
\]

**CQ2 (extra-pin positive hits).**  For every `c in Pi` and every
`x in S_c`,

\[
Q_x\cap I_c\ne\varnothing.
\tag{2.5}
\]

When these conditions hold, the coordinatewise maximal literal word

\[
A_p=C_p
\tag{2.6}
\]

realizes every central and noncentral pin simultaneously.

#### Proof

Any word satisfying (2.1) is pointwise contained in `E_p`: a coordinate
placed at `p` belongs to every central target whose window contains `p`.
Similarly, (2.2) forces \(A_p\subseteq S_c\) whenever `p in I_c`.  Hence
every feasible word satisfies

\[
A_p\subseteq C_p.
\tag{2.7}
\]

Nonzeroness gives CQ0.  Every positive coordinate in a central or extra pin
must occur at an allowed position of its interval, giving CQ1--CQ2.

Conversely take (2.6).  By construction, its union on a central interval is
contained in `T_i`, and its union on `I_c` is contained in `S_c`.  CQ1 and
CQ2 give the reverse inclusions coordinate by coordinate.  CQ0 makes every
letter nonempty.  This proves (2.1)--(2.2).  \(\square\)

This is Proposition 1.1 of the corrected Shadow--Braid note with the central
negative constraints factored into `E`.  The factorization exposes the
three distinct gates:

* raw residence/nonempty `E`;
* survival after all negative pin intersections, CQ0; and
* positive recovery, CQ1--CQ2.

Neither of the first two implies the third.

### Corollary 2.2 (natural lower seam pins)

Suppose `T` is depth-`d` resident.  A natural lower occurrence

\[
S=\bigcap_{h=0}^{q}T_{i+h},\qquad1\le q\le d,
\tag{2.8}
\]

has final physical cell

\[
I(i,q)=[i+q,i+d].
\tag{2.9}
\]

Within a pin system that passes CQ0--CQ1 and CQ2 for its other pins, the
set-theoretic occurrence (2.8) may be credited as a literal lower witness if
and only if it is included as the pin `(I(i,q),S)` and, after **all** other
pins are imposed,

\[
Q_x\cap[i+q,i+d]\ne\varnothing
\qquad(x\in S).
\tag{2.10}
\]

In particular, the equality

\[
\bigcup_{p=i+q}^{i+d}E_p=S
\tag{2.11}
\]

does not suffice.  Other pins can delete all occurrences of one coordinate
of `S` from this cell while leaving every `C_p` nonempty.

#### Proof

Equation (2.9) is the derivative-row dictionary: the cell has depth `d-q`
and starts at `i+q`.  Under residence, (2.11) follows coordinatewise from
the run criterion.  Applying CQ2 to this actual cell gives (2.10), which is
necessary and sufficient.  \(\square\)

## 3. Coordinate-protected recursive seam interface

Theorem 2.1 has an exact witness form suited to cuts and reversals.  Define
the positive obligations

\[
\begin{aligned}
\mathcal B_{\rm cen}&=\{(i,x):x\in T_i\},
 &J(i,x)&=[i,i+d],\\
\mathcal B_{\rm pin}&=\{(c,x):c\in\Pi,\ x\in S_c\},
 &J(c,x)&=I_c.
\end{aligned}
\tag{3.1}
\]

An admissible witness for an obligation `(b,x)` is a position

\[
p\in J(b,x)\cap Q_x.
\tag{3.2}
\]

In addition, every physical position `p` has the nonempty-letter obligation
to select some `x in C_p`.

### Theorem 3.1 (coordinate-protected seam transport)

A decorated child seam has a common literal compiler if and only if one can
choose:

1. one admissible witness (3.2) for every central and noncentral positive
   obligation; and
2. one coordinate `x_p in C_p` for every physical position `p`.

Consequently, let a cut/reversal/reconnection transport a previously
certified collection of pieces.  A sufficient and necessary recursive
interface is the following.

* Each transported obligation carries a named coordinate-position witness.
* A witness is retained only if its final position is still in the actual
  final pin interval, the coordinate is still in the final erosion there,
  and no final pin covering that position omits the coordinate.
* Every obligation whose witness is destroyed, and every genuinely new seam
  obligation, receives a new admissible witness.
* Every final physical position retains or receives a nonempty-letter
  witness.

#### Proof

The two witness conditions are exactly CQ0--CQ2 with one element chosen
from each nonempty eligible set.  Theorem 2.1 proves both directions.
\(\square\)

This formulation is not a matching problem: witnesses for different
positive obligations may coincide.  The obstruction is instead the union
of **negative** interval constraints covering every eligible position of a
particular coordinate.

For a fixed braid, define the physical disruption region `Z` to contain:

* every position whose central erosion differs from the transported parent
  erosion;
* every position in an added, deleted, moved, or relabelled pin interval;
  and
* every physical interval crossing an old or new cut.

Away from `Z`, the old covering-pin pattern and the erosion transport
verbatim.  Hence an old obligation with a named witness outside `Z` remains
satisfied.  It is enough to recheck obligations without such a witness,
central windows meeting `Z`, all changed/crossing pins, and nonemptiness on
`Z`.  This is an exact localization; it does not replace the checks inside
`Z` by a scalar seam budget.

Reversal deserves emphasis.  If the middle occurrence
`[u,u+q]` is reversed into the final interval `[i,i+q]`, its intersection
label is unchanged, but its child physical pin is (2.9), namely
`[i+q,i+d]`.  It is not licensed by merely reversing an old physical
interval.  A multi-seam interval is likewise evaluated once as its actual
final interval; the presence of several seams gives no duplicate positive
credit.

Thus the protected object required for Pascal recursion is not just a
target occurrence.  It is the coordinate-labelled witness triple

\[
(\hbox{pin or central obligation},\ x,\ p).
\tag{3.3}
\]

Target-level cut-aware budgets remain exact for `SB2` and for the
set-theoretic part of `SB3`, but they cannot establish `SB4` without these
witnesses.

## 4. The two smallest interface obstructions

### 4.1 Residence does not imply a nonzero erosion

At `d=1`, take

\[
T_0=\{1\},\qquad T_1=\{2\}.
\tag{4.1}
\]

Then

\[
E_0=\{1\},\qquad E_1=\varnothing,\qquad E_2=\{2\},
\tag{4.2}
\]

and nevertheless

\[
T_0=E_0\cup E_1,qquad T_1=E_1\cup E_2.
\]

Thus (0.1), or equivalently coordinatewise binary residence allowing empty
letters, passes.  No nonzero physical word can realize these two central
pins because its middle letter is forced empty.  This is the smallest
nonempty-erosion obstruction.

### 4.2 Minimal depth-two common-\(Q\) obstruction

Let the deadline be `d=2`.  On five named coordinates
`x,y,z,a,b` (and, if one wants the actual `k=7,r=4,d(7)=2` parameter,
adjoin two unused coordinates), take the Johnson seam

\[
T_0=\{x,y,z,a\},\qquad
T_1=\{x,y,z,b\}.
\tag{4.3}

There are four physical positions `0,1,2,3`, and

\[
\begin{array}{c|cccc}
p&0&1&2&3\\ \hline
E_p&xyza&xyz&xyz&xyzb.
\end{array}
\tag{4.4}

Every erosion set is nonempty and both central windows are recovered.
The seam has the natural lower target

\[
S=T_0\cap T_1=\{x,y,z\}
\tag{4.5}

at its correct depth-one physical cell

\[
I_S=[1,2].
\tag{4.6}

Add the two distinct singleton lower pins

\[
[1]\longmapsto\{y\},
\qquad
[2]\longmapsto\{z\}.
\tag{4.7}

All three lower labels are distinct and assigned to distinct cells.  The
middle seam (4.3) is Johnson, the natural lower occurrence (4.5) exists,
and its cut-aware occurrence budget is exactly

\[
\beta^-_\Gamma(S)=0+1-1=0:
\]

it is one actual new seam occurrence.  Yet after imposing (4.7), the
maximal common letters are

\[
\begin{array}{c|cccc}
p&0&1&2&3\\ \hline
C_p&xyza&y&z&xyzb.
\end{array}
\tag{4.8}

They are all nonempty, and they still recover both central pins:

\[
C_0\cup C_1\cup C_2=T_0,
\qquad
C_1\cup C_2\cup C_3=T_1.
\tag{4.9}

The singleton pins also pass.  But

\[
Q_x\cap I_S=\{0,3\}\cap\{1,2\}=\varnothing,
\tag{4.10}
\]

and

\[
C_1\cup C_2=\{y,z\}\ne S.
\tag{4.11}
\]

Therefore no common literal word realizes these pins.  Notice that each
pin subsystem is separately feasible.  With the central pins and only the
`y` singleton pin, take

\[
(xyza,y,xyz,xyzb),
\]

and with the central pins and only the `z` singleton pin, take

\[
(xyza,xyz,z,xyzb).
\]

Both words already realize the same set-theoretic seam target `S` on
`[1,2]` (so explicitly adding the negative-inert `S` pin changes neither
word); their superposition does not.  Thus all of the following are
insufficient:

* a Johnson seam;
* exact target support and nonnegative protected-occurrence budget;
* nonempty maximal erosion;
* nonempty post-pin erosion at every physical position;
* separate common compilers for the two pin subfamilies; and
* injective target-to-cell assignment.

Only the common positive-hit condition detects (4.10).

### Proposition 4.1 (minimality in the natural two-window class)

The example above is minimal among local counterexamples satisfying all of
the following: the failed pin is the natural intersection of two distinct
equal-rank central windows; every lower target label is nonempty and used
once; blockers use distinct lower cells; all post-pin physical letters are
nonempty; and the two central pins remain realizable.

More precisely, one must have `d>=2`.  At `d=2`, the failed natural cell
has two positions, its target has at least three coordinates, the central
rank is at least four, and at least five ground coordinates are needed.
Thus (4.3)--(4.7) attain all local minima.  In the actual middle-layer
parameterization `r=ceil(k/2)` with `d=d(k)`, the first compatible dimension
is `k=7`.

#### Proof

For `d=1`, the natural adjacent-intersection cell has depth zero and consists
of one physical position.  A distinct lower cell cannot both cover that
position and omit a positive coordinate without either being the same cell
or using a central cell whose label contains the coordinate.  Hence a
common-\(Q\) conflict of the stated form needs `d>=2`.

At `d=2`, the natural cell is `[1,2]`.  To erase `x` at both positions while
leaving the two central windows able to obtain `x`, the blockers must leave
the outer positions `0` and `3` available.  The only distinct lower cells
that do this are the singleton cells `[1]` and `[2]`.  Their nonempty labels
are distinct subsets of `S\setminus\{x\}`, so `|S\setminus\{x\}|>=2` and
`|S|>=3`.  Two distinct equal-rank central sets both containing `S` then
have rank at least four and require two different outside coordinates, so
the ground set has size at least five.  The displayed example attains every
bound.

For the actual parameters, `k<=6` has either middle rank at most three or
deadline at most one; `k=7` has `r=4` and `d(7)=2`.  \(\square\)

The proposition is a local minimality statement.  It does not assert the
existence of a full exact rank-four deck extending this collar, nor does it
claim minimality among arbitrary non-Johnson or duplicate-pin systems.

## 5. Consequence for the Pascal-recursive seam step

The corrected Shadow--Braid fixed-braid sufficiency theorem survives this
audit.  The proposed recursive inference

\[
\begin{array}{c}
\text{parent protected target occurrences survive}\cr
\text{and the child erosion is nonempty}\cr
\text{and every sector has a compiler}
\end{array}
\quad\Longrightarrow\quad
\text{one child compiler}
\tag{5.1}
\]

is false by Section 4.2.

An exact Pascal seam lemma must instead propagate the witness system of
Theorem 3.1.  Equivalently, after all sectors, cuts, reversals, completion
vertices, and seam pins have been superposed, it must prove

\[
\boxed{
\begin{aligned}
&C_p\ne\varnothing &&\text{for every physical position }p,\\
&Q_x\cap[i,i+d]\ne\varnothing
   &&\text{for every }x\in T_i,\\
&Q_x\cap I_c\ne\varnothing
   &&\text{for every selected pin }c\text{ and }x\in S_c.
\end{aligned}}
\tag{5.2}
\]

The parent can make (5.2) recursive by reserving coordinate-position
witnesses (3.3) and requiring every seam to replace exactly those witnesses
it destroys.  A scalar protected-occurrence budget remains useful for the
upper tower and for identifying candidate lower cells, but it is not the
literal compiler interface.

No theorem presently proves that the Pascal sectors admit such a globally
compatible witness transport in every dimension.  Conversely, the local
counterexample refutes only support/count-based seam steps; it is not a
counterexample to the contiguous-OR conjecture or to the full corrected
Shadow--Braid theorem.

## 6. Audit boundary

Proved here:

1. the exact local common-\(Q\) seam criterion, with nonempty physical
   letters and all central positive hits included;
2. the coordinate-protected witness interface under cuts and reversals;
3. the exact rule that a cut-crossing lower interval must be reclassified
   and checked at its final physical cell;
4. the depth-one nonempty-erosion obstruction; and
5. the minimal local depth-two counterexample (4.3)--(4.11).

Not proved here:

* existence of a Pascal-recursive witness transport in all dimensions;
* extension of the local collar (4.3) to a full exact middle deck;
* an obstruction to adaptive/off-spine braids that explicitly satisfy
  (5.2); or
* the conjectured upper bound `nu(k)<=B(k)`.
