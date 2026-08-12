# The sigma map determines the complete central shadow tower

Date: 2026-07-27

## 0. Scope

For (k=2r-1), the map

\[
\sigma:\binom{[k]}{r-1}\longrightarrow\binom{[k]}{r+1},
\qquad X\subset\sigma(X),
\]

is not merely a q1 colour label.  Once its selected middle-level graph is a
Hamilton cycle, it determines the entire central chronology and hence every
higher union and intersection shadow.

This gives a literal one-map normal form for the **central** part of the
optimal-word problem.  It does not make the conjecture automatic: residence,
all-depth coverage, the boundary flag, and the lower-mask pinning Hall problem
become additional predicates on the same map.

## 1. From sigma to the transition word

Write

\[
\sigma(X)\setminus X=\{a_X,b_X\}
\]

and join (X) in the middle-levels graph to (X+a_X) and (X+b_X).
Assume the resulting graph is one Hamilton cycle.  Up to rotation and
reversal it has a unique form

\[
Y_0,X_0,Y_1,X_1,\ldots,Y_{W-1},X_{W-1},Y_0,
\tag{1.1}
\]

where

\[
X_i=Y_i\cap Y_{i+1},
\qquad
\sigma(X_i)=Y_i\cup Y_{i+1}.
\tag{1.2}
\]

Put

\[
d_i=Y_i\setminus Y_{i+1},
\qquad
a_i=Y_{i+1}\setminus Y_i.
\tag{1.3}
\]

Thus (Y_{i+1}=Y_i-d_i+a_i).  The cyclic transition word
((d_i,a_i)) is determined by (sigma).

## 2. Every central shadow is sigma-determined

For (q\ge0), define

\[
L_i^{(q)}=\bigcap_{h=0}^{q}Y_{i+h},
\qquad
U_i^{(q)}=\bigcup_{h=0}^{q}Y_{i+h}.
\tag{2.1}
\]

Then (L^{(1)}_i=X_i) and (U^{(1)}_i=\sigma(X_i)).  More generally,

\[
U_i^{(q)}=\bigcup_{h=0}^{q-1}\sigma(X_{i+h}),
\tag{2.2}
\]

and the analogous intersections are obtained from the consecutive lower
vertices.  In particular, for (q=2),

\[
L_i^{(2)}=X_i\cap X_{i+1},
\qquad
U_i^{(2)}=\sigma(X_i)\cup\sigma(X_{i+1}).
\tag{2.3}
\]

Thus at (k=11), the rank-eight condition is exactly surjectivity of the
adjacent-(sigma)-union map in (2.3); it is not a new free variable.

## 3. Residence is a local predicate on sigma

Let (d=d(k)).  A cyclic coordinate run of the middle word (Y) begins
when that coordinate occurs as some (a_i) and ends at its next occurrence
as a deletion (d_j).  Therefore every cyclic 1-run has length at least
(d+1) if and only if

\[
a_i\notin\{d_{i+1},\ldots,d_{i+d}\}
\qquad\text{for every }i.
\tag{3.1}
\]

This is exactly the cyclic residence condition needed for (Y) to be a
(d)-fold OR derivative.  It is a finite-memory condition on the Hamilton
cycle selected by (sigma), not a later labelling choice.

For a path obtained by cutting the cycle, the same condition is required on
all internal runs.  The initial and terminal exceptions are governed by the
nested boundary-flag criterion of
`MATH_BOUNDARY_FLAG_FACTOR_THEOREM_20260727.md`.

## 4. The maximal factor and exact shadow identities

Assume (3.1).  Define the cyclic maximal factor by

\[
E_j=\bigcap_{h=0}^{d}Y_{j-h}.
\tag{4.1}
\]

Coordinatewise, a 1-run ([s,t]) of (Y) becomes the run
([s+d,t]) of (E).  Consequently

\[
D^dE=Y.
\tag{4.2}
\]

More precisely, for (0\le q\le d),

\[
\boxed{
(D^{d-q}E)_i
=\bigcap_{h=0}^{q}Y_{i-h}}
\tag{4.3}
\]

and for every (q\ge0),

\[
\boxed{
(D^{d+q}E)_i
=\bigcup_{h=0}^{q}Y_{i+h}.}
\tag{4.4}
\]

These are identities of sets, not estimates.  They show that the complete
upper derivative tower and the top (d) lower derivative rows are already
encoded by (sigma).

### Proof

It suffices to work in one coordinate.  If its cyclic run in (Y) is
([s,t]), of length at least (d+1), then (4.1) gives its run in (E) as
([s+d,t]).  OR-dilating this interval by (d-q) positions gives
([s+q,t]), which is exactly the set of indices (i) for which
(Y_{i-q},\ldots,Y_i) all contain the coordinate.  This proves (4.3), and
the case (q=0) gives (4.2).  Applying another (q) OR derivatives to
(Y) is exactly the consecutive union in (4.4).  \(\square\)

## 5. Exact corrected one-map target

For odd (k), a sufficient central theorem is now the construction of one
(sigma) satisfying all of the following.

1. **Degree two:** every middle set has degree two in (G_\sigma).
2. **Connectivity:** (G_\sigma) is one Hamilton cycle.
3. **Immediate upper coverage:** (sigma) is surjective.
4. **Residence:** (3.1) holds after a suitable safe cut, with the exact
   boundary flag at the two ends.
5. **All-depth upper coverage:** the sets in (4.4) cover every required upper
   mask.
6. **Lower pinning:** submasks can be installed inside the maximal envelopes
   (4.1) while retaining one witness for every required cell in (4.3).

Clause 6 is the interval-hitting plus Hall problem from the preservable-shrink
theorem.  It is not implied merely by the aggregate number of available
cells.  Hence the statement “the full conjecture is just surjectivity of
(sigma)” is false, while the stronger and useful statement is true:

\[
\boxed{
\text{one map }\sigma\text{ determines every central constraint;}
\text{ the conjecture asks for one }\sigma\text{ satisfying them jointly}.}
\]

At (k=11), q1 is already realized by an explicit connector and by the
relaxed equivariant PBBS factor.  The unresolved sigma predicates are the
safe connected realization, delay-three residence, and the adjacent-union
rank-eight condition; the final lower pinning problem remains the compiler
interface.

## 6. The exact equivariant (k=11) specialization

For a translation-equivariant quotient cycle of nonzero voltage, all of the
remaining central predicates admit finite quotient tests.  In an oriented
42-cycle, delay-three residence is exactly (42\cdot3=126) forbidden
insert/delete equalities.  Any violation has eleven translated copies
separated by 42 positions, so no single linear cut can hide it.  Thus the
equivariant model requires genuine cyclic residence.

The q2 colours are the 42 adjacent unions

\[
 B_j=\sigma(X_j)\cup\sigma(X_{j+1})
\]

with the appropriate quotient voltage alignment.  The rank-eight layer has
15 translation orbits, and coverage is exactly surjectivity of the
nondegenerate (B_j)'s onto those 15 colours.  Once cyclic residence holds,
every cut admits exactly nine nested (5\supset4\supset3) endpoint flags.
The cut must nevertheless remove a repeated q1 colour and two nonessential
q2 occurrences simultaneously; counting alone does not force such a common
cut.

The complete coordinate formulas and the exact cut predicate are in
`K11_EQUIVARIANT_SIGMA_RESIDENCE_Q2_QUOTIENT_20260727.md`.
