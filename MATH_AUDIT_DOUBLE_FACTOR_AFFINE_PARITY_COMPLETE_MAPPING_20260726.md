# Audit of the double-factor affine parity complete mapping

Date: 2026-07-26

Method: exact algebra and hand verification of the displayed `Q_4` tables.

## 0. Verdict

The affine complete-mapping lemma in
`MATH_THEOREM_DOUBLE_FACTOR_AFFINE_PARITY_COMPLETE_MAPPING_20260726.md`
is correct.  Its application to the two common-phase `Q_4` factors is
also an exact owner factorization: the resulting family gives one
pair-clustered factor of `Q_8` into sixteen isometric `C_16` cycles.

There is, however, one substantive correction to the claimed amount of
context dependence.  The eight even contexts do **not** give eight
distinct coarse factors.  They give exactly two distinct coarse factors,
each repeated on four contexts.  Equivalently, the construction reads
only the single quotient bit

\[
                 \eta(p)=p_1\mathbin\oplus p_3
                         =p_2\mathbin\oplus p_4
                 \qquad (p\in Q_4^{\rm even}).       \tag{0.1}
\]

Thus the corollary is genuinely nonconstant, but its phase-shift
dependence is already exponentially degenerate under a naive tensor or
recursion: one seed consumes only one of the three independent even
parity bits.

All code-fibre counts below refer to the augmented code carrying `J`.
A literal lower or upper target may forget `J`, so its fibres can only be
larger.  Explicit cross-tag collisions already occur at depth one; see
`MATH_AUDIT_REPAIRED_CROSSED_WITNESS_TAGGED_HALFSTEP_RAW_COLLISION_20260726.md`.

## 1. The affine lemma, with the shore bookkeeping explicit

Extend the coordinate permutation `S` linearly to `Q_r`, and define

\[
 A_p(x)=Sp\oplus x,\qquad B_x(p)=Sp\oplus x.          \tag{1.1}
\]

For fixed even `p`, the asserted definition gives

\[
\begin{aligned}
 A_pF_p(x)
 &=Sp\oplus x\oplus e_{\delta _0(Sp\oplus x)}\\
 &=G_0(A_p x).
\end{aligned}                                        \tag{1.2}
\]

Hence

\[
                         F_p=A_p^{-1}G_0A_p.          \tag{1.3}
\]

This proves both permutation and neighbour properties.  It also proves
the cycle assertion without any additional compatibility assumption:
translation is a cube automorphism, so it preserves cycle lengths,
directions, vertex disjointness, and isometry.

For fixed `x`, put `T_x(p)=p\oplus e_{d_p(x)}`.  Then

\[
\begin{aligned}
 B_xT_x(p)
 &=Sp\oplus x\oplus e_{S\delta _0(Sp\oplus x)}\\
 &=G_1(B_xp).                                        \tag{1.4}
\end{aligned}
\]

The map `B_x` sends the even shore to the shore of parity `|x| mod 2`
and the odd shore to the opposite shore.  A neighbour permutation of a
cube swaps the two parity shores; because it is a permutation, its
restriction between them is a bijection.  Equation (1.4) therefore gives

\[
 T_x=B_x^{-1}G_1B_x:
 Q_r^{\rm even}\longrightarrow Q_r^{\rm odd}         \tag{1.5}
\]

bijectively.  This verifies the parity claim, including the parity shift
caused by an odd `x`; that shift was implicit in the original proof and
causes no problem.

No conjugacy between `G_0` and `G_1` is used.  The same-vertex direction
identity is exactly what is required in (1.4).

## 2. Exact physical factorhood of the lift

Use physical bits

\[
                         x_i=a_i,\qquad p_i=a_i\oplus b_i.   \tag{2.1}
\]

At an even state `(p,x)`, the first lifted move is

\[
 (p,x)\longmapsto(p\oplus e_i,x),\qquad i=d_p(x),    \tag{2.2}
\]

which toggles only `b_i`.  Bijection (1.5) makes these first moves a
perfect matching from all even-context owners to all odd-context owners,
separately for each `x`.  From the odd endpoint, the second move is

\[
 (p\oplus e_i,x)\longmapsto(p,F_p(x)),               \tag{2.3}
\]

which toggles only `a_i`.  Since each `F_p` is a permutation, these
second moves also have unique targets.  Consequently the lifted successor
is a permutation of all `2^{2r}` owners, and

\[
                         \widetilde F^{2}(p,x)=(p,F_p(x)). \tag{2.4}
\]

The even context is therefore fixed on the even-time subsequence.  A
coarse `C_{2r}` becomes one physical `C_{4r}`, rather than joining another
coarse cycle.  If the coarse cycle is isometric, its circular direction
word is `pi pi`: in an isometric `C_{2r}`, the two occurrences of every
direction must be separated by exactly `r` steps.  Replacing every `i`
by the adjacent pair `b_i,a_i` gives an isometric `C_{4r}`.

This also settles edge disjointness.  Distinct lifted cycles are
owner-disjoint; two cube edges with the same endpoints cannot then lie in
different cycles.  The two certificate factors `G_0,G_1` need not be
edge-disjoint from one another, and in the displayed `Q_4` example they
are not.  Cross-factor edge disjointness is neither assumed nor used.

## 3. Hand audit of the `Q_4` certificate

Let

\[
                         v=0101.
\]

The first displayed row `a_0,...,a_7` is the prefix walk with direction
word

\[
                         1234\,1234,                 \tag{3.1}
\]

and `b_j=a_j\oplus v`.  The two rows are disjoint and contain sixteen
vertices, so they partition `Q_4`.  Their cyclic seams also have the
claimed directions.  This verifies `G_0`.

In the crossed factor, each row still contains one member of each column
`{a_j,b_j}`.  Hence the two crossed rows again partition all owners.  The
first crossed row has successive differences

\[
 1,4,3,2,1,4,3,2,                                  \tag{3.2}
\]

including its cyclic seam; the second has the same list.  Thus `G_1` is
an exact factor into two isometric `C_8` cycles.  Giving both vertices in
column `j` colour `j mod 8` orients all four cycles consistently.
Consequently, owner by owner,

\[
\begin{array}{c|cccccccc}
j&0&1&2&3&4&5&6&7\\ \hline
\delta _0&1&2&3&4&1&2&3&4\\
\delta _1&1&4&3&2&1&4&3&2,
\end{array}                                         \tag{3.3}
\]

and `delta_1=S delta_0` for `S=(2 4)`.

The factors share eight of their sixteen undirected edges: the two edges
at each of the phase transitions `0->1`, `2->3`, `4->5`, and `6->7`.
The other eight edges differ.  Again, this overlap is harmless because
`G_1` certifies the column matching and is not superposed with `G_0` in
the lifted physical factor.

There are eight even contexts and sixteen phases.  The lift therefore
has `8*2=16` physical cycles, each of length sixteen, accounting exactly
for all `256` owners of `Q_8`.

## 4. Exact context stabilizer and the correction

The four direction fibres of `delta_0` are the cosets

\[
\begin{array}{c|c}
\text{direction}&\text{vertices}\\ \hline
1&L\\
2&1000+L\\
3&1100+L\\
4&1110+L,
\end{array}                                         \tag{4.1}
\]

where

\[
 L=\langle0101,1010\rangle
  =\{0000,0101,1010,1111\}.                         \tag{4.2}
\]

It follows that every translation in `L` fixes `delta_0`.  Conversely,
if translation by `u` fixes `delta_0`, it must carry the direction-one
fibre `L` to itself, whence `u in L`.  Thus

\[
 \operatorname {Stab}_{\rm tr}(\delta _0)=L.         \tag{4.3}
\]

The transposition `S=(2 4)` preserves `L`.  Therefore, for even contexts
`p,p'`,

\[
\begin{aligned}
 d_p=d_{p'}
 &\iff S(p\oplus p')\in L\\
 &\iff p\oplus p'\in L.                             \tag{4.4}
\end{aligned}

Now `L` is a two-dimensional subspace of the three-dimensional even
shore.  Hence there are exactly two distinct functions `d_p`, and hence
exactly two distinct permutations `F_p`, each occurring four times.
On the even shore, `L` is the kernel of the quotient bit (0.1).

The two functions really are distinct.  For example, with
`p=1100`, one has `Sp=1001`, and

\[
 d_0(0000)=\delta _0(0000)=1,
 \qquad
 d_{1100}(0000)=\delta _0(1001)=3.                  \tag{4.5}
\]

Accordingly, "eight context-dependent coarse factors" is correct only
if it means eight *indexed occurrences*.  If it means eight distinct
factors, it is false and should be replaced by:

> The eight even contexts use exactly two context-dependent coarse
> `C_8` factors, each on four contexts; the choice is the bit `eta(p)`.

Likewise, translation by `Sp` does not always change the visible phase:
translations in `L` leave the entire outgoing-direction function fixed.

## 5A. A general phase-shift gauge collision

The affine double-factor formula has an invariant which does not depend
on the special `Q_4` tables.  Let

\[
 d_p(x)=\delta_0(Sp+x),
\]

and let `J=J_{p,d}(x)` be the direction set of an aligned coarse window.
For any even vector `u` supported on

\[
                         I_J=J\cap S^{-1}J,          \tag{5A.1}
\]

put

\[
                         p'=p+u,\qquad x'=x+Su.      \tag{5A.2}
\]

Then

\[
                         Sp'+x'=Sp+x.                \tag{5A.3}
\]

Inductively, the two coarse trajectories use exactly the same directions
and their phase vectors differ by the fixed vector `Su` at every time.
Because `supp(u)` is contained in `J` and `supp(Su)` is contained in `J`,
they have the same outside restrictions of both `p` and `x`.  Hence they
have the same aligned tagged code.  Distinct `u` give distinct starts.
Therefore every nonempty lower or upper code fibre satisfies

\[
 \boxed{
 |\mathcal C_d^{-1}(c)|
 \ge 2^{\max\{0,\,|J\cap S^{-1}J|-1\}}.}           \tag{5A.4}
\]

Indeed, the even vectors supported on a nonempty `t`-set form a space of
dimension `t-1`.  This proves (5A.4) without using linearity, a common
phase colouring, or a translation stabilizer of `delta_0`.

Consequently any recursive double-factor construction which retains the
phase-shift-only form and seeks near-injectivity must enforce, outside an
`o(1)` fraction of starts,

\[
                         |J\cap S^{-1}J|\le1         \tag{5A.5}
\]

on every protected window.  Indeed, overlap at least two already doubles
the fibre, so such windows can comprise only `o(1)` of all starts.  A
window family on which the overlap tends to infinity has pointwise
exponential trace degeneracy.

For a blockwise tensor of the present `Q_4` seed, `S` fixes local
directions `1,3` and swaps `2,4`.  Every cyclic interval of at least two
and at most three directions in `1234` contains a fixed direction.  If a
tensor window contains such a local interval in `b` disjoint seed blocks,
then those `b` fixed directions all lie in `J cap S^{-1}J`, and (5A.4)
gives multiplicity at least

\[
                              2^{b-1}.               \tag{5A.6}
\]

Thus ordinary tensoring cannot turn the seed into a near-injective code
when the number of locally completed seed intervals diverges.  A viable
recursion would have to destroy the phase-shift gauge itself or arrange
the almost-disjointness (5A.5), not merely choose different phase shifts.

There is also an order-independent form of this tensor obstruction.  Let
`f=|Fix(S)|`, `rho=f/r`, and consider the `r` cyclic aligned windows of
coarse length `d` in one half of any isometric `C_{2r}`.  Every direction
occurs in exactly `d` of those windows, so

\[
 {1\over r}\sum_J |J\cap\operatorname {Fix}(S)|
 = {df\over r}=\rho d.                              \tag{5A.7}
\]

Since each summand is at most `d`, at least a fraction

\[
                         {\rho\over2-\rho}           \tag{5A.8}
\]

of the windows have at least `rho d/2` fixed directions.  Indeed, if
that fraction is `theta`, the mean is at most
`theta d+(1-theta)rho d/2`, and comparison with (5A.7) gives (5A.8).
Every fixed direction in `J` belongs to `J cap S^{-1}J`.  If `N` is the
number of even-time starts, (5A.4) and a fibre count therefore give

\[
 N-|\operatorname {im}\mathcal C_d|
 \ge {\rho\over2-\rho}N
 \left(1-2^{1-\lceil\rho d/2\rceil}\right),        \tag{5A.9}
\]

for `rho>0`.  To justify the last step, the high-overlap starts form a
union of whole code fibres because
`J` is itself part of the code; each such fibre has the size supplied by
(5A.4), while every remaining start contributes at most one new code
value.

For the block tensor of the `Q_4` seed, `rho=1/2` for every tensor power,
regardless of how its directions are ordered.  Thus

\[
 N-|\operatorname {im}\mathcal C_d|
 \ge {N\over3}
 \left(1-2^{1-\lceil d/4\rceil}\right).            \tag{5A.10}
\]

In particular the collision excess is at least `(1/3-o(1))N` as soon as
`d` tends to infinity.  This closes arbitrary orderings of the ordinary
tensor seed, not just a fixed common order.  Any recursive double-factor
relation that hopes to evade this cut must produce coordinate
permutations with `rho=o(1)` and must additionally control overlap from
their nonfixed cycles (or leave the phase-shift ansatz entirely).  Direct
sums and conjugates of `(2 4)` retain `rho=1/2` and cannot do so.

## 5. Exact aligned tagged-code fibres of the seed

The stabilizer calculation permits an exact, non-enumerative trace audit.
Label the four directions by the elements of

\[
 G=\mathbb F_2^2=\{0,\alpha,\alpha+\beta,\beta\}
\]

in the cyclic order

\[
 1\leftrightarrow0,\quad
 2\leftrightarrow\alpha,\quad
 3\leftrightarrow\alpha+\beta,\quad
 4\leftrightarrow\beta.                             \tag{5.1}
\]

Define the quotient map

\[
 Qz=(z_1\oplus z_3)\alpha+(z_2\oplus z_4)\beta.    \tag{5.2}
\]

The fibres in (4.1) say exactly that the label of `delta_0(z)` is `Qz`.
Moreover `QS=Q`, and hence the label of the affine seed direction is

\[
                         d_p(x)=Qx+Qp.               \tag{5.3}
\]

Toggling directions `1,2,3,4` adds respectively
`alpha,beta,alpha,beta` to (5.3).  Thus the direction-label recurrence is

\[
 0\longmapsto\alpha\longmapsto\alpha+\beta
  \longmapsto\beta\longmapsto0.                     \tag{5.4}
\]

Let `C_d` be the aligned code

\[
 \mathcal C_d(p,x)=
 \bigl(J_{p,d}(x),x|_{J^c},p|_{J^c}\bigr).          \tag{5.5}
\]

For `1<=d<4`, a length-`d` interval `J` in the oriented cycle (5.4)
determines its initial label `s`.  Once a code value is fixed, its unknown
inside bits satisfy

\[
 Q(x_J+p_J)=s+Q(x_{J^c}+p_{J^c}),\qquad
                         \sum_{i\in J}p_i=\text{fixed}.       \tag{5.6}
\]

For one direction, `Q|_J` has rank one.  For two adjacent directions it
has rank two, because every adjacent pair in (5.4) contains one column of
type `alpha` and one of type `beta`.  It continues to have rank two for
three directions.  The parity equation is independent of the `Q`
equations: every nonzero equation coming from `Q` has a nonzero
`x_J` coefficient, whereas parity has none.  Therefore every nonempty
fibre has exactly

\[
\begin{array}{c|cccc}
d&1&2&3&4\\ \hline
|\mathcal C_d^{-1}(c)|&1&2&8&128.
\end{array}                                         \tag{5.7}
\]

For `d=4`, all four directions occur and both outside restrictions are
empty, so all `|Q_4^{even} x Q_4|=128` even-time starts have the same
code.  Reversing (5.4) gives the identical count for the upper aligned
code.

These are also exactly the fibre sizes for the context-independent lift
using `G_0`: in that case the first equation in (5.6) is `Qx_J=fixed`,
of ranks `1,2,2`, while the erased `p_J` bits satisfy only their parity
equation.  The resulting dimensions are again `0,1,3`.  Thus the `r=4`
double-factor seed is nonconstant but produces **no reduction at all** in
the aligned tagged-code multiplicities at any depth.  Since forgetting
`J` only merges fibres, these are also rigorous collision lower bounds for
the literal target map.

## 6. Exact audited boundary

The ownership theorem and the `Q_8` factor remain valid without
qualification.  The seed also remains the first nonconstant example
within the cited construction: (4.5) proves nonconstancy.  What the seed
does **not** provide is high-rate context coding.  Four even contexts are
already indistinguishable at the level of the complete coarse successor
map, and (5.7) shows that mixing the one visible context bit with the two
phase-syndrome bits merely exchanges which variables collide; it does not
decrease a tagged-code fibre.  Any tensor or recursion which only takes products
and affine phase shifts of this seed inherits a large factor-type quotient
kernel.  That kernel is fatal for direct tensors and for the literal
affine-lift recursion, but it is not by itself a shallow-trace no-go.  The
cross-once-then-parallel parity-alternating recursion in
`MATH_THEOREM_CONTROLLED_CROSS_DOUBLE_FACTOR_AUGMENTED_CODE_20260726.md`
retains a half-dimensional stabilizer while making the aligned tagged code
exactly injective through depth `R/8`.  Thus factor-type degeneracy and
tagged-code degeneracy must be kept separate.  Literal lower/upper target
injectivity still requires recovery of the forgotten support `J`.
