# The joint level-two/bottom 4-graph: exact degrees, critical nibble scale, and the mark-depth barrier

**Date:** 2026-08-05  
**Method:** exact backward FIFO algebra and random role-bank counting; no
computation or search  
**Status:** unconditional reduction and quantitative barrier.  Joining
level two to the bottom pair produces a fixed 4-partite 4-graph of task
degree `Theta(d^3)` and intrinsic task--level-two codegree `Theta(d^2)`.
Under full degree/codegree regularity, its natural nibble leave is `H/d`,
exactly the separator scale.  Uniform role banks alone do not provide that
regularity: an explicit legal one-mark-skeleton cluster has right pair
codegree `Theta(d^3)`, the same order as a task degree.  Thus the joint
band removes the two-mark bottom *option* cylinder only if a one-mark
skeleton-spread theorem is carried into the joint selection; it is not an
unconditional fixed-uniformity shortcut.

## 1. Reserving three role banks

Use the separator sacrifice

\[
 s=\left\lceil{cH_0\over d}\right\rceil,
 \qquad H=H_0-s,
 \qquad W\ge(d+1)H_0.                                    \tag{1.1}
\]

Before installing levels `j>=3`, reserve disjoint uniform banks

\[
                         |B_j|=\beta_jH
                    \qquad(j=0,1,2),                      \tag{1.2}
\]

up to harmless rounding, and put `beta=beta_0+beta_1+beta_2`.

Exactly as in the two-bank calculation, immediately before level `j>=3`
the remaining right shore has ratio

\[
                         j+1+c-\beta+O_c(d^{-1})           \tag{1.3}
\]

to the task shore.  Hence

\[
                         3+c-\beta>0                       \tag{1.4}
\]

leaves every still-sequential upper level with strict scalar slack.  The
separator therefore permits all three final role banks to be selected
before the upper SDRs.

## 2. Exact joint-band hypergraph

After levels `3,...,d` have been fixed for task `i`, put

\[
                         K_i=T_3^i-\{b_3^i,b_2^i,b_1^i\}. \tag{2.1}
\]

Let `Y_i` be its fresh reservoir, of size

\[
                         y=q-d+2=\Theta(d^2).              \tag{2.2}
\]

For an ordered triple of distinct fresh labels `(x_3,x_2,x_1)`, backward
FIFO gives

\[
 \begin{aligned}
 T_2&=K_i\cup\{b_1^i,b_2^i,x_3\},\\
 T_1&=K_i\cup\{b_1^i,x_3,x_2\},\\
 T_0&=K_i\cup\{x_3,x_2,x_1\}.                            \tag{2.3}
 \end{aligned}
\]

Make the 4-partite 4-uniform hypergraph `H_4` with shores

\[
                         I,\quad B_2,\quad B_1,\quad B_0, \tag{2.4}
\]

and edge `{i,T_2,T_1,T_0}` whenever (2.3) holds in the three indicated
banks.  The maps in (2.3) recover `x_3`, then `x_2`, then `x_1`, so the
edge is simple once the task is named.

### Theorem 2.1 (joint-band equivalence)

The already installed upper owner paths extend through levels `2,1,0`
with all owners globally distinct if and only if `H_4` has a matching
saturating `I`.

#### Proof

A FIFO extension gives one edge through each task by (2.3), and owner
distinctness makes the edges disjoint.  Conversely a matching edge uniquely
recovers the three fresh labels from successive owner differences; the
three disjoint banks separate the owner roles, and the matching separates
tasks within each role.  \(\square\)

## 3. Exact one-task scales under uniform banks

Put

\[
                         p_j={|B_j|\over W}
                            ={\beta_j+o(1)\over d+1+c}.    \tag{3.1}
\]

For a fixed task, finite-population sampling differs from independent
multinomial colours by `exp(-Theta(d^2))`, because only `O(d^6)` owner
resources occur in its atlas while `W=exp(Theta(d^2))`.

Its mean degree is

\[
 \boxed{
                         D=(y)_3p_2p_1p_0=\Theta(d^3).}    \tag{3.2}
\]

The conditional mean codegrees with one fixed role owner are

\[
 \begin{array}{c|c}
 \text{fixed vertices}&\text{mean codegree}\\ \hline
 (i,T_2)&(y-1)(y-2)p_1p_0=\Theta(d^2),\\
 (i,T_1)&2(y-2)p_2p_0=\Theta(1),\\
 (i,T_0)&6p_2p_1=\Theta(d^{-2}).
 \end{array}                                               \tag{3.3}
\]

The factors `2` and `6` are the possible orders of the unordered two- and
three-element fresh sets recovered from `T_1` and `T_0`.

In particular, even in the ideal product model,

\[
                         {\Delta_2\over D}=\Theta(1/d)     \tag{3.4}
\]

is the best possible pair-codegree scale because of `(i,T_2)`.

If task degrees are all `(1+o(1))D`, then incidence double counting gives
the average right degrees

\[
                         \bar R_j=(1+o(1)){D\over\beta_j}
                         \qquad(j=0,1,2).                  \tag{3.5}
\]

Nested hypergeometric Chernoff bounds give `exp(-Omega(d))` lower tails for
one fixed task degree.  They do not control right degrees, which also
depend on the multiplicity pattern of the already selected upper traces.

## 4. Uniform banks alone do not bound right codegrees

The following legal family is the exact obstruction.

Fix a rank-`r-3` core `K`, a mark `b_1`, and two fresh labels `a,b`.  Take
two disjoint sets `P,Q` of `Theta(q)` further labels.  For every

\[
                         (b_2,b_3)\in P\times Q            \tag{4.1}
\]

make one task whose already selected level-three owner is

\[
                         T_3=K\cup\{b_1,b_2,b_3\}.         \tag{4.2}
\]

These owners are pairwise distinct.  All tasks have the common prospective
level-one owner

\[
                         U_1=K\cup\{b_1,a,b\}              \tag{4.3}
\]

by taking `(x_3,x_2)=(a,b)` (or the reverse order).

Condition on `U_1 in B_1`.  For a fixed `b_2`, the corresponding level-two
owner is `K+b_1+b_2+a`; among the `Theta(q)` choices of `b_2`,
`Theta(qp_2)=Theta(d)` lie in `B_2` with exponentially high probability.
For each such `b_2` there are `Theta(q)=Theta(d^2)` choices of `b_3`, and
there are `Theta(yp_0)=Theta(d)` choices of `x_1` whose level-zero owner
lies in `B_0`.  Therefore

\[
                         d_{H_4}(U_1)=\Theta(d^4),         \tag{4.4}
\]

a factor `Theta(d)` above the nominal right degree in (3.5).  More sharply,
for every retained level-two owner belonging to one fixed `b_2`,

\[
                         d_{H_4}(U_1,T_2)=\Theta(d^3)
                                      =\Theta(D).          \tag{4.5}
\]

Thus the maximum right pair-codegree need not be `o(D)`.

The obstruction is exactly a one-mark skeleton cluster.  For fixed `b_2`,
all `Theta(q)` tasks obtained by varying `b_3` have the same rank-`r-1`
skeleton

\[
                         T_3-\{b_3\}=K\cup\{b_1,b_2\}.    \tag{4.6}
\]

It is detected by the size-biased one-mark tail in the slack-level
cylinder programme, but it is not altered by independently colouring the
three bottom role banks.

Consequently:

\[
 \boxed{
 \text{random role banks do not imply the degree/codegree hypotheses of a
 fixed-uniformity nibble.}}                               \tag{4.7}
\]

At least the one-mark trace-spread invariant, or an equivalent deterministic
cluster cleanup, must survive through level three.

## 5. What a classical nibble would and would not give

Assume hypothetically that a strengthened trace theorem supplies

\[
 \begin{aligned}
 d(i)&=(1+o(1))D,\\
 d(U)&=O(D)\quad(U\in B_0\cup B_1\cup B_2),\\
 d(U,V)&=O(d^2)=O(D/d)\quad(U\ne V).                      \tag{5.1}
 \end{aligned}
\]

Then the ordinary fixed-uniformity nibble applies and gives a matching
covering `1-o(1)` of the tasks.  This qualitative conclusion is not enough
for the OR-word ledger, which permits only `O(H/d)` discarded copies.

The scale `H/d` is intrinsic here.  If a proportion `x` remains in a
4-uniform pseudorandom instance, its residual degree is of order

\[
                         Dx^3.                             \tag{5.2}
\]

At

\[
                         x=D^{-1/3}=\Theta(1/d),           \tag{5.3}
\]

this degree becomes constant.  Thus `H/d` is the natural terminal or
jamming scale of the nibble, not a loose target.  A qualitative
Pippenger--Spencer theorem gives only `o(H)` and cannot be cited for the
sharp (5.3).  A quantitative nibble with a logarithmic loss would likewise
exceed the separator allowance.  One needs either

* a sharp `O(H/d)` terminal estimate; or
* a prebuilt local absorber of that capacity.

If the sharp estimate is available, no absorber is required for the
current additive programme: the separator ledger may simply discard those
`O(H/d)` copies.  Neither estimate is presently proved for the physical
joint-band law.

## 6. A stronger exact route once scalar right tails are known

There is no need to stop at a nibble if the role-bank amplification gives
uniform right-load bounds.  Make the option conflict graph whose classes
are the task edge sets of `H_4`, joining options from different classes
when they share one of their three owner resources.

### Theorem 6.1 (joint-band Haxell criterion)

If

\[
 \min_i d(i)\ge D_-,
 \qquad
 \max_{U\in B_j}d(U)\le R_j,                              \tag{6.1}
\]

and

\[
                         D_-\ge2(R_0+R_1+R_2),             \tag{6.2}
\]

then `H_4` has a matching saturating every task.

#### Proof

An option conflicts with at most `R_0+R_1+R_2-3` options in other task
classes.  Haxell's independent-transversal theorem applies because every
class has size at least twice this maximum degree.  The independent
transversal is exactly a task-saturating matching of `H_4`.  \(\square\)

At the natural scales (3.2) and (3.5), (6.2) has the asymptotic constant
condition

\[
                         2\left({1\over\beta_0}
                              +{1\over\beta_1}
                              +{1\over\beta_2}\right)<1.  \tag{6.3}
\]

It is compatible with fixed large role-bank constants and then a still
larger fixed separator constant `c` in (1.4).  Thus an exponential
low-task/high-resource scalar-tail theorem would solve the joint band
*exactly*, stronger than a nibble plus absorber.

The missing assertion is again trace spread.  The random banks give the
one-task lower tail, but (4.4)--(4.6) show that they do not give the three
right-load tails.  The existing one-mark cylinder is the first relevant
input and plausibly controls the displayed worst cluster; a theorem deriving
all three right-load factorial moments from it has not yet been proved.

## 7. Verdict

The joint level-two/bottom route is useful but does not presently bypass
the marked-cylinder gate:

\[
 \boxed{
 \begin{array}{c}
 D=\Theta(d^3),\quad\Delta_2^{\rm intrinsic}=\Theta(d^2),\\
 \text{ideal nibble leave scale}=H/d,\\
 \text{random banks alone allow }\Delta_2=\Theta(D).
 \end{array}}                                             \tag{7.1}
\]

Its best possible payoff is substantial: if the one-mark trace law can be
shown to imply the three scalar right-load tails, Theorem 6.1 gives an exact
joint completion and avoids the stronger two-mark bottom theorem.  Until
that implication is established, the pre-reserved two-mark theorem remains
the proof-safe exact route.

