# Near-minimal prime-cycle packets and their complement kernels

Date: 2026-07-26

Method: pure mathematics only.

## 1. Setup

Let `p` be an odd prime.  Consider one connected transversal component of
the row--necklace incidence graph.  Suppose it has `j=p+s` row vertices
and `j` necklace vertices, where `1<=s<p`.  Its biadjacency matrix `B` is
a `0`--`1` square matrix with every row and column sum equal to `p`.
Consequently

\[
                             B=J-Q,                            \tag{1.1}
\]

where `Q` is the biadjacency matrix of an `s`-regular bipartite graph on
the same two vertex classes.

The matrix `Q`, rather than the large matrix `B`, contains all
near-minimal freedom.

## 2. Count vectors

### Theorem 2.1 (real count kernel equals the complement kernel)

If `v in R^j` satisfies `Bv=0`, then

\[
                    \mathbf1^Tv=0,\qquad Qv=0.               \tag{2.1}
\]

Conversely every sum-zero vector in `ker Q` lies in `ker B`.  Hence

\[
                 \boxed{\ker_R B=\ker_R Q\cap\mathbf1^\perp.} \tag{2.2}
\]

In particular, an exact partial-orbit count vector `r` on this component,
which obeys `Br=p1`, can differ from `1` only along this complement
kernel.

#### Proof

From `(J-Q)v=0` we have `Qv=(1^Tv)1`.  Sum all coordinates.  The left
side has sum `s1^Tv`, whereas the right side has sum `(p+s)1^Tv`.
Their difference is `p1^Tv`, so over the reals `1^Tv=0`, and then
`Qv=0`.  The converse is immediate. \(\square\)

## 3. First-moment phase directions

Let `a` be a vector of row shifts modulo `p`.  At every necklace column,
the original phase labels and the shifted phase labels must both be the
complete residue system.  Comparing their first power sums gives

\[
                              B^Ta=0\pmod p.                  \tag{3.1}
\]

### Theorem 3.1 (near-minimal phase kernel)

Put `A=1^Ta in F_p` and `c=A/s` (which is defined because `1<=s<p`).
Then

\[
 b:=a-c1\quad\hbox{satisfies}\quad
 1^Tb=0,\qquad Q^Tb=0.                                      \tag{3.2}
\]

Conversely every such `b`, plus an arbitrary component-global constant,
satisfies the first-moment equations.  Thus

\[
 \boxed{
 \ker_{F_p}B^T=\langle1\rangle
       \oplus\bigl(\ker_{F_p}Q^T\cap1^\perp\bigr).}          \tag{3.3}
\]

This is only the first-moment gate; higher power sums (equivalently the
complete-residue equations) remain necessary for an actual legal lift.

#### Proof

Equation (3.1) and `B=J-Q` give `Q^Ta=A1`.  Since `Q^T1=s1`, subtracting
`c1` kills the right side.  Also
`1^Tb=A-(p+s)c=A-sc=0` in `F_p`.  The converse follows by reversing the
calculation. \(\square\)

## 4. The first two excess sizes

### Corollary 4.1 (size `p+1` is first-moment rigid)

For `s=1`, `Q` is a permutation matrix.  Therefore `B` is nonsingular
over the reals, every partial-orbit count vector is `r=1`, and every legal
phase lift has all row shifts equal.  After relabelling columns,

\[
                         B=J-I,qquad
                         \det B=p(-1)^p\ne0.                 \tag{4.1}
\]

The remaining `p` component-global shifts need not be inert: unlike a
minimal size-`p` orbit packet, a size-`p+1` row family need not be fixed
by translation.  They are nevertheless the only possible phase knobs.

### Corollary 4.2 (size `p+2`: even complement cycles are exact linear gates)

For `s=2`, the bipartite complement is a disjoint union of even graph
cycles.  Choosing one of its two perfect matchings as the identity gives

\[
                              Q=I+P                           \tag{4.2}
\]

for a permutation matrix `P`.  On a permutation cycle of length `ell`,
the equation `Qx=0` is `Px=-x`, and has a one-dimensional alternating
solution exactly when `ell` is even.  Therefore

\[
 \boxed{
 \dim\bigl(\ker Q\cap1^\perp\bigr)
 =\#\{\hbox{even cycles of }P\}.}                            \tag{4.3}
\]

The alternating vectors already have coordinate sum zero.  Hence a
size-`p+2` component has a nonconstant count/first-moment phase direction
if and only if its complement permutation has an even cycle.

For counts this direction is genuinely bounded-integral: on one even
cycle, add `+1,-1,+1,-1,...` to the all-one count vector.  The resulting
entries are `2,0,2,0,...`, lie in `[0,p]`, and satisfy `Br=p1`.  This does
**not** yet choose the two phases of an overused row or prove the
complete-residue equations; it isolates exactly where that nonlinear
completion can first occur.

For an ordinary one-shift-per-row lift, the next power sum gives an exact
and rather restrictive test.  Let `C` be one even cycle of `P`, let
`epsilon_i in {+1,-1}` alternate on its row vertices and vanish off `C`,
and consider the first-moment direction `a_i=t epsilon_i` after removing
a global shift.  Write `phi_(i,O)` for the original phase in column `O`.
If `t ne0` gives a legal lift, comparison of the second power sums in
every column gives

\[
 2\sum_{i\in C\cap N_B(O)}\epsilon_i\phi_{i,O}
 +t\,|C\cap N_B(O)|=0\pmod p.                               \tag{4.4}
\]

For `O` on the corresponding complement cycle,
`|C cap N_B(O)|=|C|-2`; for every other column it is `|C|`.
Thus the alternating phase correlation in (4.4) must be constant on each
of these two column classes.  This is necessary, not sufficient, but it
shows explicitly where higher moments can kill the first possible
near-minimal direction.

Indeed, the old and shifted phase multisets are both `F_p`, so their sums
of squares agree.  Expanding
`sum_(i in N_B(O))(phi_(i,O)+t epsilon_i)^2` and cancelling the old sum,
then dividing by `t`, proves (4.4).

The column-Latin condition by itself does not exclude this direction.

### Proposition 4.3 (exact one-column displacement criterion)

Fix one column with neighbor set `I`, `|I|=p`, and prescribed row shifts
`(a_i:i in I)`.  There is a bijection of original phases
`phi:I->F_p` for which both `phi` and `i |-> phi(i)+a_i` are bijections
if and only if the multiset `(a_i:i in I)` is the displacement multiset

\[
                         \{\tau(x)-x:x\in\mathbb F_p\}       \tag{4.5}
\]

of a permutation `tau` of `F_p`.

#### Proof

Given `phi`, define `tau(phi(i))=phi(i)+a_i`.  The shifted phases are
complete exactly when `tau` is a permutation, and its displacement at
`phi(i)` is `a_i`.  Conversely, match the rows having each shift value to
the points having that displacement under `tau` and use that matching as
`phi`. \(\square\)

For one alternating cycle with amplitude `t ne0`, every column contains
the same number `r` of `+t` and `-t` shifts, and all remaining shifts are
zero (on a column of the complement cycle the two excluded signs reduce
`r` by one).  Whenever `r<=(p-1)/2`, take `r` vertex-disjoint edges
`{x,x+t}` in the `p`-cycle generated by translation by `t`, transpose the
two endpoints of each edge, and fix every other point.  The resulting
permutation has precisely the required displacement multiset.  Since a
simple `Q=I+P` has no fixed cycle of `P`, every even cycle supporting a
single alternating direction has length at most `p-1`, so this inequality
holds in every column.

Choosing these bijections independently in the columns produces a full
abstract column-Latin phase array with a nonconstant legal alternating
lift.  Thus incidence, first moments, higher column power sums, and even
the complete residue condition in every column permit the first
direction.  Any rigidity proof must use **cross-column** constraints on
the phase array--in the actual application, that each row's class-phase
pairs are the middle windows of one cyclic wreath.

Equivalently, in the voltage quotient of the odd graph, the `p` labelled
incidences in every row must lift to one length-`p` odd-graph cycle.  This
row-cycle condition is the first hypothesis not present in the abstract
counterexample above, and is therefore the exact next rigidity gate for
size `p+2` packets.

## 5. Correct component accounting

If the component sizes are `j_i>=p`, then

\[
                 \sum_i(j_i-p)=T'-kp.                        \tag{5.1}
\]

There is no divisibility forcing each positive summand to be `p`.
Consequently:

* excess `O(p)` permits `O(p)` nonminimal components, not merely `O(1)`;
* `Theta(T/p)` components of size `p+1` have total excess only
  `Theta(T/p)`, not `Theta(T)`;
* the first possible **internal** linear direction occurs at size `p+2`,
  not at size `2p`.

Thus minimal-packet rigidity does not squeeze the lift lane into packets
of size about `2p`.  The correct successor problem is the nonlinear
complete-residue lift on the `p+2` even-complement-cycle components, and
then the general complement-kernel problem for `p+s`.

Connectedness alone supplies none of this rigidity.  A connected
component may have extra modular or Fourier kernel directions; it implies
only that the forced component-constant kernel has dimension one.

## 6. Exact status

Proved here: the complement-kernel reduction, full rigidity at size
`p+1`, and the exact even-cycle classification at size `p+2`.

Unproved: whether an alternating `p+2` direction can be completed to the
all-different phase equations for the phase arrays arising from MSW, and
whether such components occur in bulk for a smoothing-good coordinate
cycle.
