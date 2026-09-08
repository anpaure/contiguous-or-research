# Integral normal form for the tight Type A/Type B mixture

Date: 2026-09-07.  This note gives necessary conditions for rounding the
two-orbit fractional optimum in
`EXACT_SATURATED_PAIR_FRACTIONAL_OPTIMUM_20260907.md`.  It does not construct
an integral cube cover and does not prove a lower bound for unrestricted OR
words.

Put

\[
 X=[2b],\qquad W={2b\choose b},\qquad M={2b\choose b-1}
       ={b\over b+1}W.
\]

For a cyclic coordinate order

\[
 \pi=(z_0,z_1,\ldots,z_{2b-1})
\]

(indices are modulo `2b`), define

\[
 T_i=\{z_i,z_{i+1},\ldots,z_{i+b-1}\},\qquad
 L_i=T_i\cap T_{i+1}
     =\{z_{i+1},\ldots,z_{i+b-1}\}.                 \tag{1}
\]

The `T_i` are the all-start half-window deck and the `L_i` are its lower
edge colours.  Both displayed families are simple.

## 1. Every dual-tight column is one deck with zero, one, or two cuts

**Lemma 1 (cyclic normal form).**  Every column on which the three-rank dual
is tight has, after a coordinate relabelling, the following middle and lower
rank target families.

\[
\begin{array}{c|c|c}
 \text{type}&\text{rank }b&\text{rank }b-1\\ \hline
 A:(b,b)&\{T_i:i\in\mathbb Z_{2b}\}
       &\{L_i:i\ne r,r+b\}\\
 B:(b+1,b)&\{T_i:i\in\mathbb Z_{2b}\}
       &\{L_i:i\ne r\}\\
 C:(b+1,b+1)&\{T_i:i\in\mathbb Z_{2b}\}
       &\{L_i:i\in\mathbb Z_{2b}\}.
\end{array}                                                   \tag{2}
\]

The rank-`b+1` family is the family of complements of the displayed
rank-`b-1` family.  Conversely, every row of (2) is realized by the
corresponding saturated complementary-chain rectangle.

Proof.  For a Type A column, the two length-`b` chains have `2b-2`
increments in total.  Rank center `b` forces the union of their fixed
bottom sets to be a singleton and the union of their permanently omitted
top coordinates to be a singleton.  This argument is independent of how
the shore sizes and the two cap coordinates are distributed.  Hence the
column is a side-`b` centered square with a middle geodesic of `b` vertices
and its complementary geodesic.  If the first geodesic is

\[
 T_0,T_1,\ldots,T_{b-1},
\]

then its successive deleted coordinates, common singleton cap, successive
inserted coordinates, and omitted singleton cap form the cyclic order

\[
 z_0,z_1,\ldots,z_{2b-1}.
\]

Its trace is therefore all `2b` sets `T_i`.  Its internal Johnson edges are
all cyclic edges except the opposite pair at the two path joins.  Their
lower colours are exactly all `L_i` except `L_r,L_(r+b)`.  This proves the
Type A row.

For Type B, the chain lengths are `b+1,b` and the rank center is
`b+1/2` or `b-1/2`.  If their bottom ranks have total `rho` and their
permanently omitted top-coordinate counts have total `sigma`, then

\[
             \rho+\sigma=1.
\]

Thus exactly one shore end contributes a single cap coordinate and all
other shore coordinates are chain increments.  This includes both possible
support patterns: balanced supports `b,b`, with one maximal chain and one
one-end-truncated chain, and supports `b+1,b-1`, with the length-`b` chain
maximal on the smaller shore and the length-`b+1` chain one-end-truncated
on the larger shore (plus exchanged shores).  Reading the two increment
lists in the directions of the middle diagonals and inserting the unique cap
gives a cyclic order of all `2b` coordinates.  The two middle diagonals are
its `2b` half-windows.  The lower diagonals traverse every consecutive
middle edge except the unique edge across the truncated end, so their lower
colours are all `L_i` except one.  Rotation makes that exception an arbitrary
`L_r`.

For Type C use full maximal chains on both `b`-supports.  The two middle
diagonals are the two complementary halves of the same deck (with their two
endpoints identified), and the two lower diagonals give every `L_i`.
Complementation gives the upper row in every case.  These constructions can
be reversed, proving the converse. `square`

Thus the Type A/Type B mixture is not two different middle designs.  It is
one special cyclic-deck design with two allowed deletion patterns in its
first shadow.

The same normal form is valid at every depth.  Write

\[
 I_j^s=\{z_j,z_{j+1},\ldots,z_{j+s-1}\}.
\]

After choosing the cut used in the proof and, for Type B, reversing the
cyclic order when necessary so that the unique cap is on the normalized
side of the cut, for `1<=d<b` the rank-`b-d` families are exactly

\[
\begin{aligned}
 A_d&=\{I_j^{b-d}:j\in[d,b-1]\mathbin\cup[b+d,2b-1]\},\\
 B_d&=\{I_j^{b-d}:j\in[d,b]\mathbin\cup[b+d,2b-1]\}.
                                                               \tag{2a}
\end{aligned}
\]

Thus Type A deletes two opposite runs of `d` cyclic starts, while Type B
restores one boundary start and deletes runs of lengths `d` and `d-1`.
Their sizes are `2(b-d)` and `2(b-d)+1`, respectively.  The corresponding
rank-`b+d` targets are their complements.  Formula (2a) follows by reading
the two product diagonals outward from the normalized cap: the two allowed
start intervals have lengths `b-d,b-d` for Type A and `b-d+1,b-d` for
Type B.  Reversing the cyclic order exchanges the two Type B intervals, so
the same displayed convention covers balanced and unbalanced shore splits
and either choice of truncated end.  For Type A the same formula also
follows by writing a target as the intersection of two trace vertices at
Johnson distance `d`; the allowable vertex indices lie in one of the two
uncut geodesics.

Consequently any integral rounding must solve a single correlated
all-depth cyclic-window problem.  The choices of missing starts at different
ranks cannot be made independently.

## 2. Exact equality forces a decorated tight-cycle decomposition

**Theorem 2 (necessary integral normal form).**  Suppose an integral cover
by saturated complementary rectangles has cost equal to

\[
 \left(1+{1\over b(b+1)}\right)W.                    \tag{3}
\]

Then every selected column is dual-tight, and every target at ranks
`b-1,b,b+1` is covered exactly once.  Consequently its middle decks form a
decomposition of `binom(X,b)` into all-start half-window decks.

If only Types A and B are selected, and their numbers are `A` and `B`, then

\[
 \boxed{
 A={W\,(b-1)\over2b(b+1)},\qquad
 B={W\over b(b+1)},\qquad
 A+B={W\over2b}.}                                    \tag{4}
\]

Moreover, after replacing each column by the cyclic normal form (2), the
undeleted `L_i` partition `binom(X,b-1)`.  Equivalently, if

\[
 \mu(S)=\#\{\text{selected middle decks whose full lower deck contains }S\},
\]

then `mu(S)>=1` for every lower target, and precisely `mu(S)-1` occurrences
of `S` are deleted.  Type A deletions must be opposite pairs
`L_r,L_(r+b)`; Type B deletions are single windows.

Proof.  Write the primal cost minus the value of the feasible dual as the
sum of (i) the nonnegative dual slack of every chosen column and (ii), for
each positive-dual target, its positive dual weight times its coverage
excess over one.  Equality in (3) makes every summand zero.  The equality
classification in the fractional-optimum theorem and Lemma 1 now give the
deck decomposition and exact lower partition.

There are `2b` middle targets per column, so

\[
 A+B={W\over2b}.                                     \tag{5}
\]

Before deletion the lower decks have `W` slots, whereas only `M` lower
targets are required.  Type A deletes two slots and Type B one, hence

\[
 2A+B=W-M={W\over b+1}.                              \tag{6}
\]

Solving (5)--(6) proves (4).  Exact lower coverage gives the assertion about
`mu`. `square`

In particular, every selected middle deck must contain a globally repeated
lower window, and a proportion

\[
 {A\over A+B}={b-1\over b+1}                         \tag{6a}
\]

of the decks must contain an **opposite pair** of globally repeated lower
windows.  Only the remaining proportion `2/(b+1)` may use a single repeated
window.  This is an exact coverage obstruction: a middle-deck factor with a
row having no repeated lower window, or with too few rows containing an
opposite repeated pair, cannot support the Type A/Type B optimum, even if
its aggregate first-shadow counts are perfect.

The middle decomposition in this theorem is a decomposition of the complete
`b`-uniform hypergraph on `2b` points into tight Hamilton cycles.  It is not
a Baranyai--Katona wreath decomposition under the standard non-coprime
definition: a `(2b,b)` Baranyai--Katona wreath has only two sets.  The
folded-codegree calculation for this deck hypergraph was already proved in
`MIDDLE_BLOCK_FACTOR.md`; the new content here is the forced A/B deletion
decoration.

The theorem is only necessary for a full cube cover.  A decorated
decomposition satisfying the three central ranks need not cover the farther
ranks.

## 3. Arithmetic obstruction

The number of columns in (5) is integral if and only if

\[
 \boxed{b\mid \operatorname{Cat}_{b-1}.}             \tag{7}
\]

Indeed,

\[
 {W\over2b}={1\over b}{2b-1\choose b-1}
 ={2b-1\over b}\operatorname{Cat}_{b-1},
\]

and `gcd(b,2b-1)=1`.  Once (7) holds, both values in (4) are automatically
integers, since `W/(b+1)=Cat_b` and

\[
 A={W\over b+1}-{W\over2b},\qquad
 B=2{W\over2b}-{W\over b+1}.
\]

In particular, exact equality is impossible whenever `b` is prime.  For a
prime `p`, the product formula gives

\[
 \operatorname{Cat}_{p-1}
 =\prod_{j=2}^{p-1}{p-1+j\over j}
 \equiv\prod_{j=2}^{p-1}{j-1\over j}
 ={1\over p-1}\equiv-1\pmod p.                      \tag{8}
\]

This is an obstruction to exact equality in the rectangle model, not to an
asymptotic `(1+o(1))W` construction.

Indeed the purely numerical A/B relaxation has essentially no asymptotic
rounding loss.  If `n=A+B`, middle and lower incidence require

\[
 2bn\ge W,\qquad (2b-2)n+B\ge M,                     \tag{8a}
\]

and the charge is `2bn+B`.  Hence its exact integer optimum is obtained at

\[
 n_0=\left\lceil{W\over2b}\right\rceil,\qquad
 B_0=\max\{0,M-(2b-2)n_0\},                          \tag{8b}
\]

with numerical value `2bn_0+B_0`.  For fixed `n`, increasing `B` only
increases charge, and increasing `n` while the second constraint is active
increases the optimized charge by two; after it becomes inactive the charge
increases by `2b`.  Also `B_0<=n_0`, since
`M<=(2b-1)W/(2b)<=(2b-1)n_0`, so the displayed counts are feasible in the
rank-count relaxation.  This proves (8b).  Thus the serious obstruction is the
simultaneous deck/deletion geometry, not scalar rounding.  When exact
equality is arithmetically possible, (8b) specializes to (4).

## 4. A pointwise port-balance law and a symmetry obstruction

In a Type A row the two deleted lower windows are disjoint and omit exactly
the antipodal coordinate pair `z_r,z_(r+b)`.  For `x in X`, let

\[
 o_x=\#\{\text{Type A rows whose omitted coordinate pair contains }x\},
\]

and let

\[
 m_x=\#\{\text{Type B deleted lower windows which contain }x\}.
\]

**Lemma 3 (exact port balance).**  Every exact Type A/Type B rounding in
Theorem 2 satisfies

\[
                         \boxed{o_x=m_x\quad(x\in X).}       \tag{9}
\]

Proof.  In every full lower deck a coordinate occurs in exactly `b-1`
windows.  Hence its load before deletion is `(b-1)(A+B)`.  Its load in the
complete lower layer is

\[
 {2b-1\choose b-2}.
\]

Using (4), their difference is exactly

\[
 (b-1){W\over2b}-{2b-1\choose b-2}
 ={W\,(b-1)\over2b(b+1)}=A.                          \tag{10}
\]

The Type A deletion pair contains `x` exactly once unless `x` is one of its
two omitted coordinates, and a Type B deletion contributes precisely when
its deleted window contains `x`.  Thus the deleted load at `x` is

\[
 A-o_x+m_x.
\]

Equating this with (10) proves (9). `square`

For completeness, if tight Type C columns are also allowed, with counts
`A,B,C`, then

\[
 A+B+C={W\over2b},\qquad 2A+B={W\over b+1},
\]

so, on putting `K=W\,(b-1)/(2b(b+1))`, one has `A-C=K`.  The identical
point-load calculation gives the generalized port law

\[
                         \boxed{o_x-m_x=C\quad(x\in X).}      \tag{10a}
\]

Thus Type C does not remove the port constraint; it prescribes a uniform
positive imbalance between its two sides.

This immediately obstructs the most symmetric development.

**Corollary 4 (transitive-development divisibility).**  If an exact
Type A/Type B rounding is invariant under a coordinate-transitive group
(in particular, if each type is a union of full orbits of such a group),
then

\[
 \boxed{b\mid A={W\,(b-1)\over2b(b+1)}.}             \tag{11}
\]

Proof.  The Type A omitted-pair incidence is then point-regular, so
`o_x=2A/(2b)=A/b` is an integer.  Lemma 3 gives the same regular load on the
Type B side. `square`

Condition (11) is strictly stronger than the column-count divisibility (7).
For example, the first arithmetically admissible values `b=6,15,28` have

\[
 A\equiv1\pmod6,\qquad A\equiv6\pmod {15},\qquad
 A\equiv11\pmod {28},
\]

respectively.  Hence none admits an exact coordinate-transitive A/B
development, even though the raw numbers of A and B columns are integral.

## 5. Exact remaining design gate

The two-orbit fractional optimum can therefore be rounded exactly only if
one constructs, simultaneously,

1. a tight-Hamilton-cycle decomposition of the middle layer;
2. full coverage of its lower cyclic-window deck;
3. a deletion of every lower excess occurrence, using an opposite pair in
   every Type A row and one window in every Type B row;
4. the pointwise balance (9), and all farther-rank coverage.

The folded middle-deck hypergraph has excellent local codegree, but that fact
alone was already known and does not enforce items 2--4.  Corollary 4 shows
that the obvious coordinate-transitive orbit rounding is unavailable for
many of the first dimensions in which even the middle decomposition passes
its divisibility test.  Any exact construction there must break that
symmetry or mix additional tight types.

The finite checker `scripts/check_tight_cyclic_normal_form_20260907.py`
enumerates every tight balanced and unbalanced support/rank-interval shape
for `b=2,3,4`. It verifies (2) for Types A--C and the all-depth formulas
(2a) for Types A and B, allowing rotation and reversal of the cyclic order.
The proofs above, not this check, establish the general statements.
