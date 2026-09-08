# Exact duplicate-block packing and two disjoint static owner banks

**Date:** 2026-08-05  
**Method:** cyclic interval packing, normalized matching, and a uniform
queue-state circulation; no computation or search  
**Status:** unconditional reductions.  For a fixed lower trace, the maximum
number of canonical-lock-free depth-sized blocks has an exact transversal-gap
formula.  Independently, whenever the middle/lower layer ratio is at least
two, every lower vertex has two owner-disjoint containing extensions.  Thus
singleton fibres are not a static obstruction to the noncanonical
duplicate-block programme.  What remains is an integral chronological
rounding: one FIFO-compatible queue cycle, bijective on owners, whose
duplicate flags occur in the required blocks.

## 1. Set-up

Put

\[
 t=r-d,\qquad
 M={k\choose t},\qquad
 W={k\choose r},\qquad
 U=W-M.                                                        \tag{1.1}
\]

Let

\[
                         S=(S_i)_{i\in\mathbb Z_W}              \tag{1.2}
\]

be any cyclic word on the rank-`t` layer.  No Johnson or queue hypothesis is
needed in Sections 2--4.  For a lower vertex `X`, write

\[
 O_X=\{i:S_i=X\},\qquad \mu_X=|O_X|.                            \tag{1.3}
\]

Assume every `O_X` is nonempty.  A canonical lock transversal is a set

\[
 L=\{p(X):p(X)\in O_X\},                                       \tag{1.4}
\]

one position from every value fibre.

A depth-sized block bank is a union `R` of cyclic intervals of length `d`,
with at least one position outside `R` between successive blocks.  The
separation is the useful normal form for the short-gap antecedent theorem;
it is not needed for the elementary fibre criterion below.

## 2. Exact fixed-bank and one-block criteria

For \(R\subseteq\mathbb Z_W\), put

\[
                         \mu_X(R)=|O_X\cap R|.                   \tag{2.1}
\]

### Theorem 2.1 (exact multiplicity-capacity criterion)

There is a canonical lock transversal disjoint from `R` if and only if

\[
 \boxed{
                         \mu_X(R)\le \mu_X-1
                         \quad\hbox{for every }X.}
                                                                    \tag{2.2}
\]

#### Proof

Condition (2.2) is exactly \(O_X\setminus R\ne\varnothing\) for every fibre.
Choose one point from every such difference.  Fibres of different values
are disjoint, so the choices are automatically distinct.  The converse is
immediate.  \(\square\)

Thus for disjoint blocks `B_1,...,B_q`, the condition is the capacitated
interval-packing system

\[
 \boxed{
   \sum_{j=1}^q |O_X\cap B_j|\le \mu_X-1
   \quad\hbox{for every }X.}                                    \tag{2.3}
\]

In particular, a singleton fibre has capacity zero: its unique position may
not belong to any free block.

For a single cyclic block

\[
                         B_a=[a,a+d-1],                           \tag{2.4}
\]

define the forbidden-start set of a fibre by

\[
 J_X=\{a:O_X\subseteq B_a\}
    =\bigcap_{p\in O_X}[p-d+1,p].                                \tag{2.5}
\]

Here the intervals on the right are intervals in the cyclic start
coordinate.  The second equality simply says that a block starting at `a`
contains \(p\) precisely when \(a\in[p-d+1,p]\).

### Corollary 2.2 (one-block test)

A depth-`d` block with start `a` can be left completely unlocked if and only
if

\[
                         a\notin\bigcup_X J_X.                    \tag{2.6}
\]

When `2d<W` and a nonsingleton fibre fits in a depth-`d` block, let
`span(X)` be the length, in positions, of its unique shortest containing
cyclic arc.  Then

\[
                         |J_X|=d-\operatorname{span}(X)+1.       \tag{2.7}
\]

For a singleton fibre the same formula holds with `span(X)=1`, giving
\(|J_X|=d\).  A fibre which fits in no depth-`d` block has
\(J_X=\varnothing\).

This is the exact sense in which multiplicity alone is insufficient: the
sets `J_X` depend on the cyclic diameter of the occurrences, not only on
their number.

## 3. Exact packing after choosing the representatives

Fix a lock transversal `L`.  List the lengths of the maximal cyclic gaps of
\(\mathbb Z_W\setminus L\) as

\[
                         g_1,\ldots,g_M,                           \tag{3.1}
\]

allowing zero gaps between adjacent locks.  Put

\[
 f_d(g)=\left\lfloor{g+1\over d+1}\right\rfloor.                \tag{3.2}
\]

### Theorem 3.1 (exact transversal-gap packing formula)

The maximum number of pairwise separated depth-`d` blocks disjoint from
this fixed `L` is

\[
 \boxed{
                         \kappa_d(L)=\sum_{j=1}^M f_d(g_j).}      \tag{3.3}
\]

Consequently a depth-sized free bank of `q` blocks exists for the word `S`
if and only if

\[
 \boxed{
   \max_{p(X)\in O_X}
      \sum_{g\in\operatorname{Gap}(\{p(X)\})}
          \left\lfloor{g+1\over d+1}\right\rfloor
      \ge q.}                                                   \tag{3.4}
\]

#### Proof

Inside an unlocked gap of length `g`, `h` blocks use `hd` positions and the
`h-1` internal separators use another `h-1`.  Hence they fit exactly when

\[
                         h(d+1)-1\le g,
\]

or `h<=f_d(g)`.  Packing from one endpoint attains this bound.  Locked
endpoints already separate blocks lying in different gaps, so the gap
optima add, proving (3.3).  Maximizing over the independent representative
choices gives (3.4).  \(\square\)

For the scalar template in the short-gap theorem, the target value is

\[
                         q=\left\lfloor{U\over d+1}\right\rfloor.\tag{3.5}
\]

Equation (3.4), rather than an aggregate multiplicity estimate, is the exact
canonical-face target.

There is nevertheless an automatic size-only refinement which separates
fibre hitting from interval capacity.  Starting from any transversal `L`,
write

\[
 g_j=q_j(d+1)+r_j,\qquad 0\le r_j\le d.                       \tag{3.6}
\]

In the `j`-th gap, declare positions `d+1,2(d+1),...,q_j(d+1)` to be
additional separators.  The positions left free form `q_j` blocks of
length `d` and one terminal block of length `r_j`.

### Corollary 3.2 (automatic short-gap refinement)

Every surjective cyclic lower word has a set `R` such that:

1. no value fibre is contained in `R`;
2. every component of `R` has length at most `d`; and
3.
   \[
   |R|\ge U-{U\over d+1}.                                    \tag{3.7}
   \]

For the fixed transversal, the minimum number of extra separators needed to
make every complementary gap have length at most `d` is exactly

\[
 s(L)=\sum_j\left\lfloor{g_j\over d+1}\right\rfloor.       \tag{3.8}
\]

The exact short-interval capacity of the displayed refinement is

\[
 C_d(L)=\sum_j\left[
      q_j{d(d+1)\over2}+{r_j(r_j+1)\over2}\right].           \tag{3.9}
\]

#### Proof

The original lock in each gap boundary keeps one point of every fibre
outside `R`, proving item 1.  The construction gives item 2.  It uses
`s(L)` added separators, and `s(L)<=U/(d+1)`, proving (3.7).

If `h` separators split a gap of length `g` into pieces of length at most
`d`, then `g-h<=d(h+1)`, or

\[
 h\ge\left\lceil{g-d\over d+1}\right\rceil
   =\left\lfloor{g\over d+1}\right\rfloor.
\]

The displayed construction attains equality.  Its component lengths give
(3.9) by the triangular interval count.  \(\square\)

Corollary 3.2 closes the **bare** positional fibre-hit and short-gap rows.
It does not close the deep scalar row.  If the selected representatives are
evenly dispersed so that every `g_j<=d`, then `s(L)=0` and (3.9) can be only
`O(W)`, whereas the deep demand is `Theta(dW)`.  The load-bearing quantity
is therefore still (3.3), or equivalently the exact capacity (3.9), not the
large cardinality of `R` alone.

## 4. What component rotations can and cannot do

The packing functional is almost additive.  For all nonnegative integers
`x,y`,

\[
 \left|f_d(x+y)-f_d(x)-f_d(y)\right|\le1.                       \tag{4.1}
\]

Indeed, put `D=d+1`, write `x+1=uD+r` and `y+1=vD+s`, and compare
`floor((r+s-1)/D)` with zero.

Suppose a word is initially a disjoint union of `c` cyclic components, each
of which contains at least one selected lock.  Cut every component once,
rotate and order the resulting linear words arbitrarily, and join them into
one cycle without changing their internal orders.  Only the gap containing
each cut is split, and only the resulting boundary pieces are rejoined.
Applying (4.1) to the `c` splits and the `c` joins gives

\[
 \boxed{
   |\kappa_d^{\rm joined}-\sum_{j=1}^c\kappa_d^{(j)}|\le2c.}    \tag{4.2}
\]

Thus component rotation and ordering can change the depth-block count by
only `O(c)`, unless whole components are left lock-free.  A lock-free
component is not a rotation effect: it already says that every one of its
value fibres has an occurrence elsewhere.

For the centered PBBS factor one has `c<=W/k`.  Since

\[
                         {W/k\over W/d}={d\over k}=o(1),         \tag{4.3}
\]

component rotations cannot repair a positive-proportion deficit in the
required \(\Theta(W/d)\) block count.  They can only provide a lower-order
boundary correction.  Therefore a positive proof must produce either the
block gaps inside the components or a positive mass of genuinely
duplicate-only components.

The hypothesis that each component contains a selected lock is essential
in (4.2).  Components without locks are precisely the favourable exceptional
case and must be counted by their full lengths.

## 5. Two disjoint static owner extensions always exist

The preceding obstruction is specific to a fixed chronology.  It is not a
static incidence obstruction.

Let `B_(t,r)` be the bipartite containment graph between

\[
                         \mathcal L={ [k]\choose t}
 \quad\hbox{and}\quad
                         \mathcal O={ [k]\choose r}.             \tag{5.1}
\]

Every lower vertex has degree

\[
                         A={k-t\choose d},                        \tag{5.2}
\]

and every owner has degree

\[
                         B={r\choose d}.                          \tag{5.3}
\]

Double counting gives

\[
                         {A\over B}={W\over M}.                   \tag{5.4}
\]

### Theorem 5.1 (two-bank containment factor)

If

\[
                         W\ge2M,                                  \tag{5.5}
\]

then there are two injections

\[
 \phi_0,\phi_1:\mathcal L\longrightarrow\mathcal O             \tag{5.6}
\]

such that

\[
 X\subseteq\phi_j(X)\quad(j=0,1),
 \qquad
 \operatorname{im}\phi_0\cap\operatorname{im}\phi_1=\varnothing. \tag{5.7}
\]

Consequently the owner set admits a partition

\[
                         \mathcal O=\mathcal A\dot\cup\mathcal D,
 \qquad |\mathcal A|=M,\quad |\mathcal D|=U,                    \tag{5.8}
\]

and a lower label \(\ell(T)\subseteq T\) of rank \(t\) on every owner such
that:

1. every lower vertex labels exactly one owner in \(\mathcal A\); and
2. every owner in \(\mathcal D\) has a label which already labels an owner
   in \(\mathcal A\).

Thus \(\mathcal A\) is a complete anchor bank and every owner of
\(\mathcal D\)
is statically duplicate-labelled.

#### Proof

Replace every lower vertex by two labelled copies.  For a set `Y` of
underlying lower vertices, edge counting in the biregular containment graph
gives

\[
                         A|Y|\le B|N(Y)|,
\]

and therefore, by (5.4)--(5.5),

\[
                         |N(Y)|\ge2|Y|.                           \tag{5.9}
\]

Any set of labelled copies has size at most `2|Y|`, so (5.9) is Hall's
condition for the doubled left shore.  A matching saturating both copies
gives `phi_0,phi_1` with disjoint owner images.

Put \(\mathcal A=\operatorname{im}\phi_0\) and
\(\mathcal D=\mathcal O\setminus\mathcal A\).  Label \(\phi_0(X)\) and
\(\phi_1(X)\) by \(X\).  Every remaining owner in \(\mathcal D\) contains
at least one rank-\(t\) subset; label it by any such subset.  Its chosen
lower label already has its \(\phi_0\) occurrence in \(\mathcal A\).  This
proves both assertions.  \(\square\)

At the optimal deadline,

\[
                         {W\over M}\longrightarrow e^{\pi/4}>2,\tag{5.10}
\]

so Theorem 5.1 applies in every sufficiently large dimension.  It proves
that singleton fibres and dispersed mandatory points are artefacts of a
fixed chosen chronology, not an unavoidable owner/lower incidence law.

If an owner ordering placed the members of \(\mathcal D\) in the duplicate
blocks and realized the displayed labels as its delayed lower trace, the
canonical fibre gate would close automatically.

## 6. The exact queue-state graph has a uniform fractional solution

We now include the chronological constraints.  A queue state is

\[
                         (S;q_1,\ldots,q_d),                     \tag{6.1}
\]

where `|S|=t` and the `q_j` are ordered, distinct and outside `S`.  Its owner
is

\[
                         \pi(S;q_1,\ldots,q_d)=S\cup\{q_1,\ldots,q_d\}.
                                                                    \tag{6.2}
\]

There is a directed transition

\[
 (S;q_1,\ldots,q_d)
 \longrightarrow
 (S-a+b;q_2,\ldots,q_d,a)                                     \tag{6.3}
\]

for every

\[
                         a\in S,
 \qquad b\notin S\cup\{q_1,\ldots,q_d\}.                       \tag{6.4}
\]

This is exactly the FIFO queue law of the delay-`d` lift.

### Proposition 6.1 (regularity and exact fractional marginals)

The queue-state digraph is in- and out-regular of degree

\[
                         t(k-r).                                  \tag{6.5}
\]

Every owner has exactly

\[
                         (r)_d                                    \tag{6.6}
\]

queue states above it, and every lower vertex has exactly

\[
                         (k-t)_d                                  \tag{6.7}
\]

queue states above it.  Giving every state weight `1/(r)_d` and splitting
that weight uniformly among its outgoing transitions is a balanced
circulation with owner marginal exactly one and lower marginal exactly

\[
                         {(k-t)_d\over(r)_d}={W\over M}.           \tag{6.8}
\]

#### Proof

In (6.3), there are `t` choices for `a` and `k-r` choices for `b`, proving
the outdegree.  For a prescribed terminal state, choose the formerly
inserted `b` in its lower set (`t` choices) and the dropped queue head
outside its owner (`k-r` choices); this reconstructs a unique predecessor,
proving the indegree.

Above an owner, choose and order the `d` queue elements inside it, giving
`(r)_d` states.  Above a lower vertex, choose and order `d` elements of its
complement, giving `(k-t)_d`.  Regularity makes the uniform edge weights a
circulation.  The first marginal follows from (6.6), and (6.8) follows from
the binomial identity

\[
                         M(k-t)_d=W(r)_d.                          \tag{6.9}
\]

\(\square\)

Thus the delayed chronology has no scalar or fractional owner/lower
separator.  The missing obstruction, if any, is integral and connected.

## 7. Exact remaining theorem

The owner/fibre part of the construction is now equivalent to the following
single statement.

> **Duplicate-block queue-cycle theorem.**  The queue-state digraph contains
> a directed cycle `Gamma` of length `W` such that:
>
> 1. \(\pi\) is bijective on the states of \(\Gamma\);
> 2. every rank-`t` lower vertex occurs on `Gamma`;
> 3. there are `q=floor(U/(d+1))` separated length-`d` intervals whose lower
>    values all have another occurrence outside their union.

Condition 1 is the owner Hamiltonicity cut.  Condition 3 is exactly (2.3),
not an additional matching problem.  The delay-`d` queue theorem converts
such a cycle into a resident owner Hamilton cycle whose maximal antecedent
has the required free blocks.

Theorem 5.1 and Proposition 6.1 prove, respectively, the exact static and
fractional projections of this statement.  Neither proves their common
integral chronological rounding.  Ordinary Johnson Hamiltonicity, random
choice of lock representatives, or rotation of pre-existing PBBS components
does not supply that rounding.

After this theorem, one still needs the coordinate-value chart inside the
blocks, arbitrary-width upper witnesses, and any typed common-cap/opening
interface required by the final architecture.

## 8. Dependency and audit scope

The FIFO equivalence used in Sections 6--7 is

`MATH_THEOREM_DELAY_D_JOHNSON_QUEUE_LIFT_AND_DUPLICATE_BLOCK_TARGET_20260805.md`.

Its equations have been independently checked as follows.  Under the queue
conditions, the update of `S` and the shift of the queue cancel the lower
deletion label and give the owner update `T_(i+1)=T_i-a_(i-d)+b_i`.  Every
old queue member is absent from one of `T_i,...,T_(i+d)`, every coordinate
outside `T_i` is absent from the first owner, and every member of `S_i`
survives through the window; hence their intersection is exactly `S_i`.
Conversely, the last `d` owner deletions are exactly the queue recovered
from a biresident owner trace.

This note proves no duplicate-block queue cycle and no universal OR word.
