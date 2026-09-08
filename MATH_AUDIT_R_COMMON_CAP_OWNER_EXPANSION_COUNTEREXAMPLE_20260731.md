# Common-cap expansion audit: permanent owners do not lift marginal Hall

Date: 2026-07-31  
Lane: R  
Status: unconditional abstract theorems and counterexamples; no finite search

## 1. Scope and verdict

The following data do **not** imply a simultaneous common-cap compiler:

1. lower cells of length at most \(d\);
2. middle rows of length at most \(d+1\);
3. a permanent immune (owner) coordinate at every physical position;
4. individual soundness of every target--cell incidence; and
5. ordinary marginal Hall, even with maximally uniform candidate
   neighbourhoods.

The obstruction can already be a lost middle-row bit, with no empty physical
letter and no failed individual incidence.  The smallest example has one
two-position row and two singleton cells.

The exact corrected statement is guard-sensitive.  For a fixed complete
guarded bank \(H\) inside the marginal graph \(G\), marginal Hall lifts if and
only if, on every target cut, the cells lost by guard pruning do not exceed
the original Hall surplus.  Existentially over the bank and its guards, this
condition is equivalent to common-cap existence.

## 2. Smallest owner-preserving counterexample

Let \(d=1\).  There are two physical positions \(p_0,p_1\), one middle row

\[
 I=\{p_0,p_1\},\qquad T=E_{p_0}=E_{p_1}=\{o,a,x\},
\]

two lower targets

\[
 S_0=\{o\},\qquad S_1=\{o,x\},
\]

and the two singleton cells \(C_0=\{p_0\}\),
\(C_1=\{p_1\}\).  Put every possible incidence into \(G\), so
\(G=K_{2,2}\).

### Proposition 2.1

Every incidence of \(G\) is individually sound, \(o\) is a permanent owner
at both positions, and \(G\) has a perfect matching.  Nevertheless no perfect
matching has a common cap.

#### Proof

Capping one singleton by either \(S_i\) realizes \(S_i\) on that singleton.
The other position remains \(T\), so the middle row remains exactly \(T\).
All resulting letters contain \(o\).

Every perfect matching uses both singleton cells.  Its two letters are
\(S_0\) and \(S_1\), whose union is \(\{o,x\}\), omitting the required row
bit \(a\).  Thus the simultaneous maximal cap fails the middle row. \(\square\)

At least two targets and two cells are needed for a nontrivial matching
conflict.  With a common owner in both distinct targets, a third coordinate
is needed to make the targets distinct while both omit a protected bit.
Thus this example is minimal in positions, targets, cells, and coordinates
within this failure mode.

## 3. Sharp all-\(d\) complete-neighbourhood obstruction

Fix integers \(d,r\ge1\).  Split the physical positions into \(r\) disjoint
middle rows \(I_1,\ldots,I_r\), each having exactly \(d+1\) positions.  Put

\[
 \Omega=\{o,a,x_1,\ldots,x_{dr}\},\qquad
 T_j=E_p=\Omega\quad(p\in I_j).
\]

Take \(dr+1\) lower targets

\[
 S_0=\{o\},\qquad S_i=\{o,x_i\}\quad(1\le i\le dr),
\]

and take every physical singleton as a lower cell.  Join every target to
every cell.  Hence

\[
 G=K_{dr+1,(d+1)r}.                                    \tag{3.1}
\]

### Theorem 3.1

The system above has all of the following properties.

1. Every candidate incidence is individually sound.
2. Coordinate \(o\) is immune at every physical position.
3. For every nonempty target set \(X\),
   \[
   N_G(X)={\cal C},\qquad |N_G(X)|=(d+1)r.              \tag{3.2}
   \]
4. The marginal graph has a target-saturating matching.
5. No target-saturating matching has a common cap.

#### Proof

An individual incidence caps one position in one row to \(S_i\).  Its cell
therefore has OR \(S_i\), while one of the other \(d\) positions of the row
still carries \(\Omega\).  Thus that middle row and every other row remain
exact.  Every letter contains \(o\).  This proves items 1--3.  Since
\(dr+1\le(d+1)r\), the complete bipartite graph has a target-saturating
matching.

Any such matching occupies \(dr+1\) distinct positions.  If it occupied at
most \(d\) positions of each middle row, it would occupy at most \(dr\)
positions.  Hence one row is fully occupied.  Every target label omits
\(a\), so every letter of that row omits \(a\); the row loses \(a\).
Therefore no matching has a common cap. \(\square\)

The minimum multiplicative marginal expansion is

\[
 \min_{\varnothing\ne X}\frac{|N_G(X)|}{|X|}
   =\frac{(d+1)r}{dr+1}\longrightarrow 1+\frac1d.      \tag{3.3}
\]

More importantly, the incidence distribution is already as uniform as it
can be: every target sees every singleton in every physical block, prefix,
or cut bucket.  Thus no label-blind refinement of marginal neighbourhood
counts detects the obstruction.  The missing datum is which selected labels
oppose which protected trace bits.

### Sharp surplus calculation

To protect bit \(a\) in each row by a static row guard, at least one cell of
each row must be unavailable to every candidate, because every candidate
label omits \(a\).  Any guarded bank therefore has, for the full target set,

\[
 |N_H({\cal L})|\le dr.
\]

The marginal surplus on the same cut is

\[
 \sigma_G({\cal L})=(d+1)r-(dr+1)=r-1,
\]

whereas guard pruning loses at least \(r\) cells.  The corrected cut
inequality fails by exactly one.  This proves sharpness of the loss-versus-
surplus boundary.

## 4. Robust assigned-cell obstruction with immune owners

There is also a \(5/2\)-expanding owner-preserving obstruction at the abstract
common-cap interface.  Use positions \(0,1,2,3,4\), envelopes

\[
 E_2=\{o,a,b\},\qquad E_p=\{o,x,y\}\quad(p\ne2),
\]

targets

\[
 A=\{o,a,x\},\qquad B=\{o,b,y\},
\]

and cells

\[
 [1,2],\ [2,3],\ [0,2],\ [1,3],\ [2,4].               \tag{4.1}
\]

Every cell individually realizes either target, so the marginal graph is
\(K_{2,5}\).  Coordinate \(o\) is immune everywhere.  In every injection,
the two chosen cells meet at position \(2\), where their common cap is only
\(\{o\}\).  No other position carries \(a\) or \(b\).  Thus the assigned
cell for \(A\) loses \(a\), and the assigned cell for \(B\) loses \(b\).
The interface has uniform \(5/2\)-fold Hall expansion but no common cap.
Disjoint, coordinate-disjoint copies give arbitrary size with the same
ratio.

This example is an envelope-interface obstruction; Theorem 3.1 is the
counterexample which additionally has the exact middle-span relation
\(D=d+1\).

## 5. Exact guard-profile cut factorization

Let \(G\) be any sound marginal target--cell graph.  A **complete guarded
bank** \(H\subseteq G\) consists of the position, middle-bit, and
assigned-lower-bit traces of the binary trace theorem, with every edge of
\(H\) preserving every trace it covers and every ordered co-selectable pair
passing the corresponding edge-trace test.

For \(X\subseteq{\cal L}\), define

\[
 \sigma_G(X)=|N_G(X)|-|X|,
 \qquad
 \lambda_H(X)=|N_G(X)\setminus N_H(X)|.                \tag{5.1}
\]

### Theorem 5.1 (exact guarded expansion factorization)

A common-cap compiler exists if and only if there are a complete guarded
bank \(H\subseteq G\) and guards for which

\[
 \lambda_H(X)\le\sigma_G(X)qquad(X\subseteq{\cal L}). \tag{5.2}
\]

For a fixed guarded bank, (5.2) is the weakest possible neighbourhood-count
condition: it is exactly Hall in \(H\).

#### Proof

Since \(H\subseteq G\),

\[
 |N_H(X)|=|N_G(X)|-\lambda_H(X).
\]

Thus (5.2) is equivalent to \(|N_H(X)|\ge|X|\) for every \(X\).  Hall gives
a target-saturating matching in \(H\).  Restricting the complete guard system
to that matching gives a compatible trace decoration, so the binary trace
theorem gives one literal maximal common cap.

Conversely, suppose a common-cap matching \(M\) exists.  Take \(H=M\).
Choose a surviving coordinate at every physical position and one surviving
provider for each required middle and assigned-lower bit.  These are a
complete guard system on \(H\).  The matching itself proves Hall in \(H\),
and hence (5.2). \(\square\)

If permanent position owners are supplied in advance, only the middle and
assigned-lower guard choices remain.  Ordinary expansion must still be
measured after those two guard families: permanent owners remove only the
empty-position conflicts.

## 6. Why matching-dependent interval guards have no automatic matroid rank

In the singleton-cell, one-protected-bit specialization, the exact corrected
invariant is a partition-matroid rank.  If the positions are partitioned
into rows \(B_j\), and row \(j\) may use at most \(c_j=|B_j|-1\) opposing
singletons, define

\[
 r_{\cal P}(Y)=\sum_j\min\{c_j,|Y\cap B_j|\}.           \tag{6.1}
\]

There is an injective assignment independent in these capacities if and
only if

\[
 r_{\cal P}(N_G(X))\ge|X|\qquad(X\subseteq{\cal L}).   \tag{6.2}
\]

For completeness, this follows from integral max flow in the network
source--target--cell--row--sink, with capacities \(1,\infty,1,c_j\).
For a fixed source-side target set \(X\), minimizing over cell and row sides
gives cut capacity

\[
 |{\cal L}|-|X|+r_{\cal P}(N_G(X));
\]

so every cut has capacity at least \(|{\cal L}|\) exactly under (6.2).

This matroid structure disappears for genuine interval cells.  On the
three-position carrier \(\{1,2,3\}\), let all candidate labels oppose one
bit and take intervals

\[
 A=[2,3],\qquad B=[1,1],\qquad C=[1,2].                 \tag{6.3}
\]

A selected interval family is safe for that bit when its union does not
cover all three carrier positions.  Both \(\{A\}\) and \(\{B,C\}\) are
safe, but neither \(\{A,B\}\) nor \(\{A,C\}\) is safe.  The exchange axiom
therefore fails.  This occurs already for lower length \(d=2\) and middle
span \(d+1=3\).

Consequently, interval length alone does not turn matching-dependent guard
choice into a matroid-Hall problem.  Fixing trace guards and applying
Theorem 5.1, or solving the exact bounded conflict clutter, is the valid
replacement.

## 7. Audit of the three-position examples

The two examples in
`MATH_THEOREM_R_COMMON_CAP_GUARD_PRUNING_ROBUST_HALL_LIFT_20260731.md`
were checked directly.

1. Its first example is valid: the two selected cells leave every position
   nonempty but jointly remove the named middle bit.  Proposition 2.1 above
   is a smaller version with two positions and three coordinates.
2. Its second example is valid: an untouched third position protects every
   middle bit, while the overlapping second cap removes a private bit from
   the assigned singleton.  It correctly proves that position and row guards
   do not subsume assigned-lower guards.

The examples therefore support the three-family guard decomposition.  They
do not support any implication from unguarded marginal expansion to
compatible Hall.

## 8. Exact boundary

Proved:

* the minimal owner-preserving counterexample;
* the all-\(d\), arbitrary-size complete-neighbourhood obstruction;
* the immune-owner \(5/2\)-expanding interface obstruction;
* the exact existential guard-profile/cut factorization;
* the singleton partition-capacity criterion; and
* failure of the corresponding matroid structure for interval cells.

Not proved, and not implied by interval geometry:

* a PBBS/Pascal complete guarded bank satisfying (5.2);
* a source-independent bound on guard-pruning loss; or
* automatic compatible Hall from marginal Hall, owner bits, or label-blind
  physical-cut expansion.
