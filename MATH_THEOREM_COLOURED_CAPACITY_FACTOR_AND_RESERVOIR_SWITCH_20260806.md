# Coloured capacity factor and reservoir switches for fresh Johnson paths

**Date:** 2026-08-06  
**Method:** orbit double counting, LP duality, and the coloured spectral
escape theorem; no computation or search  
**Status:** unconditional fractional macro selector and unconditional
hotspot transport.  The true `2/3` macro orbits have one exact joint
fractional factor respecting every lower vertex, every owner, and the sharp
per-coordinate `b_2` capacity; its level-two marked-owner marginal is
exactly `1/[r(d+1)]`.  An `O(M/d)` live leave permits literal one-for-one
switches which erase any prescribed `O(k/d)` mark bank and gives a global
integral cap `O(M/k)`.  What remains is a growing-rank integral rounding
theorem improving that cap by the final factor `d` while retaining the
owner/kernel cylinder.

## 1. Setup

Put

\[
 \mathcal L={ [k]\choose t},\qquad M=|\mathcal L|,
 \qquad {k\over3}\le t\le {k\over2},\qquad d\ge3,
 \qquad d^2\le k.
\tag{1.1}
\]

Let `\widetilde H` be the labelled orbit of all oriented fresh `d`-paths

\[
 P=(S_0,S_1,\ldots,S_{d-1}),
 \qquad S_j=S_{j-1}-a_j+b_j,                              \tag{1.2}
\]

whose `2(d-1)` event labels are distinct.  Its colour is

\[
                         c(P)=b_2\in[k].                    \tag{1.3}
\]

Write

\[
 D=d(t)_{d-1}(k-t)_{d-1}                                 \tag{1.4}
\]

for the labelled fresh-path degree of a lower vertex.  The complete orbit
has

\[
 |\widetilde H|={MD\over d},\qquad
 |\{P:c(P)=s\}|={MD\over dk}\quad(s\in[k]).              \tag{1.5}
\]

The first identity is incidence counting.  The second follows from
coordinate transitivity, since every path has one colour.

The sharp average (equivalently, fractional) colour load is

\[
                         L_*={M\over kd}.                   \tag{1.6}
\]

This is forced by averaging: a path factor has `M/d` paths and `k`
colours.  The corresponding integral cap is `L=ceil L_*` below.

## 2. The capacity-slot hypergraph

Put

\[
                         L=\lceil L_*\rceil                 \tag{2.1}
\]

and create `L` private slots `(s,1),...,(s,L)` for every colour `s`.  Define
a `(d+1)`-uniform multihypergraph `\mathcal A` on

\[
 \mathcal L\ \dot\cup\ ([k]\times[L])                    \tag{2.2}
\]

by putting in the edge

\[
                         V(P)\cup\{(c(P),j)\}              \tag{2.3}
\]

for every labelled fresh path `P` and every `j\in[L]`.

### Theorem 2.1 (exact sharp-cap fractional factor)

The assignment

\[
                         x_e={1\over LD}                   \tag{2.4}
\]

to every edge of `\mathcal A` is a fractional matching which saturates
every lower vertex.  Every colour slot has load exactly `L_*/L\le1`, and

\[
                         \sum_e x_e={M\over d}.             \tag{2.5}
\]

If `kd` divides `M`, every vertex of `\mathcal A` has degree `LD` and
`x` is a fractional perfect matching.

#### Proof

A lower vertex lies in `D` labelled fresh paths, and each has `L` slot
copies.  Its degree in `\mathcal A` is therefore `LD`, so its `x`-load is
one.

A fixed slot `(s,j)` lies in every path of colour `s`.  By (1.5), its
degree and load are

\[
 {MD\over dk}=L_*D,
 \qquad {L_*D\over LD}={L_*\over L}\le1.                 \tag{2.6}
\]

Finally, summing the lower loads counts every augmented edge `d` times,
so `d\sum_e x_e=M`.  If `L=L_*`, (2.6) is also one. \(\square\)

### Corollary 2.2 (dual form)

Let `y_S\ge0` and `z_{s,j}\ge0` satisfy

\[
 \sum_{S\in V(P)}y_S+z_{c(P),j}\ge1                    \tag{2.7}
\]

for every `P,j`.  Then

\[
 \boxed{
 \sum_{S\in\mathcal L}y_S+
 {L_*\over L}\sum_{s,j}z_{s,j}\ge {M\over d}.}           \tag{2.8}
\]

In particular the same inequality holds with coefficient one on the slot
sum.  No divisibility assumption is needed.

#### Proof

Multiply (2.7) by `1/(LD)` and sum over all augmented edges.  The
coefficient of every `y_S` is one and that of every `z_{s,j}` is
`L_*/L`.  This is exactly weak LP duality against Theorem 2.1. \(\square\)

Thus there is no scalar or ordinary fractional Hall obstruction to the
sharp colour cap.  The path choice and colour balance have already been
correlated; no post-hoc orientation is being used.

## 3. The full codegree sequence survives the augmentation

Let `\Delta_q` be the maximum labelled codegree of `q` distinct lower
vertices in `\widetilde H`.  The fresh-path orbit theorem gives, for an
absolute `C`,

\[
 {\Delta_q\over D}\le
 \left({Cd\over k^2}\right)^{q-1}
 \qquad(2\le q\le d).                                    \tag{3.1}
\]

Put

\[
                         \zeta={Cd\over k^2}.              \tag{3.2}
\]

### Theorem 3.1 (augmented codegrees)

The maximum degree of `\mathcal A` is `LD`.  Its codegrees obey:

1. for `2\le q\le d` lower vertices,
   \[
   \operatorname{codeg}_{\mathcal A}(S_1,\ldots,S_q)
       \le LD\,\zeta^{q-1};                               \tag{3.3}
   \]
2. for one colour slot and `1\le q\le d` lower vertices,
   \[
   \operatorname{codeg}_{\mathcal A}((s,j),S_1,\ldots,S_q)
       \le D\,\zeta^{q-1};                               \tag{3.4}
   \]
3. two distinct colour slots have codegree zero.

#### Proof

For all sufficiently large `k` in the range (1.1), every original path has
`L` augmented copies, so (3.3) is `L` times (3.1).  Once a slot is
prescribed its colour and slot index are fixed;
there is at most one augmented copy of each original path, and forgetting
the colour restriction bounds its codegree by `\Delta_q`.  This gives
(3.4), with `\Delta_1=D`.  No augmented edge contains two slots. \(\square\)

In the central regime `k=Theta(d^2)`,

\[
                         \zeta=O(d^{-3}).                  \tag{3.5}
\]

The capacity augmentation therefore loses none of the power-decaying
codegree structure.  It also exposes the exact growing-rank rounding gate:

> **Uniform coloured fresh-path rounding.**  Prove that the particular
> `(d+1)`-graph `\mathcal A`, with (3.3)--(3.5), has a matching leaving
> `O(M/d)` lower vertices uncovered.

Any such matching projects to pairwise vertex-disjoint oriented fresh
paths with

\[
\#\{P:c(P)=s\}\le L
       ={M\over kd}+O(1)\qquad(s\in[k]).                  \tag{3.6}
\]

There is an especially clean edge-colouring sufficient condition.

### Corollary 3.2 (quantitative edge-colouring reduction)

If, for an absolute `C_0`,

\[
 \chi'(\mathcal A)\le
       \left(1+{C_0\over d}\right)LD,                    \tag{3.7}
\]

then `\mathcal A` has a matching which leaves at most

\[
                         (C_0+o(1)){M\over d}              \tag{3.8}
\]

lower vertices uncovered and whose projected colour loads satisfy (3.6).

#### Proof

The number of augmented edges is

\[
 |E(\mathcal A)|=L|\widetilde H|={MDL\over d}.            \tag{3.9}
\]

One colour class in an edge-colouring as in (3.7) therefore has at least

\[
 {MDL/d\over(1+C_0/d)LD}
       ={M\over d(1+C_0/d)}                               \tag{3.10}
\]

edges.  It is a matching.  Every edge covers `d` lower vertices, so its
lower leave is at most

\[
 M-{M\over1+C_0/d}=(C_0+o(1)){M\over d}.                 \tag{3.11}
\]

The slot vertices enforce (3.6). \(\square\)

Thus one exact form of the missing theorem is the uniform estimate
`chi'(A)=Delta(A)(1+O(1/d))`.  This is stronger than the single-matching
statement but has the advantage that all required parameters are visible
in (3.3)--(3.5).

The existing fixed-uniformity nibble statements do not prove this as
stated: both the uniformity and the demanded reciprocal error are `Theta(d)`.
Equations (3.3)--(3.5) are the precise quantitative data a valid uniform
rounding theorem may use.

## 4. The true `2/3` macro factor also admits the sharp colour cap

Now restrict to the central FIFO parameters

\[
 r=t+d=\lceil k/2\rceil,\qquad
 W={k\choose r},\qquad \rho={W\over M},                   \tag{4.1}
\]

and assume the spare-coordinate inequalities of the punctured duplicate
lift.  Let `\mathcal P_h`, `h\in\{2,3\}`, be the complete labelled orbit of
literal `h`-fold macros.  One macro contains:

* its `d` common lower vertices;
* its `h(d+1)` pairwise distinct rank-`r` owners; and
* one common second insertion mark `b_2`.

Put

\[
 w_h={M\over d|\mathcal P_h|},\qquad
 \lambda_3={\rho d\over d+1}-2,\qquad
 \lambda_2=3-{\rho d\over d+1}.                           \tag{4.2}
\]

In the central asymptotic regime these are nonnegative and sum to one.  The
existing exact macro-factor theorem gives lower load one and owner load one
to the vector which assigns weight `\lambda_h w_h` to every macro in
`\mathcal P_h`.

Augment every macro `A\in\mathcal P_h` by one of the `L` slots of its common
colour `b_2(A)`, and assign the augmented edge `(A,j)` weight

\[
                         x_{A,j}={\lambda_h w_h\over L}.    \tag{4.3}
\]

### Theorem 4.1 (joint lower/all-owner/sharp-colour macro factor)

The vector in (4.3) is a fractional matching with all of the following
properties simultaneously.

1. Every rank-`t` lower vertex has load exactly one.
2. Every rank-`r` owner has load exactly one.
3. Every colour slot has load exactly `L_*/L\le1`.
4. Every marked level-two owner occurrence
   \[
   (T,s)\in\Omega:=\{(T,s):T\in{[k]\choose r},\ s\in T\}
   \tag{4.4}
   \]
   has marginal exactly
   \[
                         {1\over r(d+1)}.                  \tag{4.5}
   \]
5. Every owner has total level-two load exactly `1/(d+1)`.

#### Proof

Splitting the old weight `\lambda_h w_h` equally among its `L` slot copies
does not change lower or owner loads, proving 1 and 2.

Coordinate transitivity gives

\[
 |\{A\in\mathcal P_h:b_2(A)=s\}|={|\mathcal P_h|\over k}.
\tag{4.6}
\]

Hence a fixed slot `(s,j)` has load

\[
 \sum_{h=2}^3 {|\mathcal P_h|\over k}
       {\lambda_hM\over d|\mathcal P_h|L}
 ={M\over kdL}={L_*\over L},                              \tag{4.7}
\]

which proves 3.

The weighted mean multiplicity is

\[
 \bar h=2\lambda_2+3\lambda_3={\rho d\over d+1}.          \tag{4.8}
\]

Every macro has `h` level-two owners carrying its common mark.  The total
weighted marked level-two mass is therefore `\bar h M/d`.  The action of
the coordinate symmetric group is transitive on the `Wr` marked owner
occurrences, so their common marginal is

\[
 {\bar h M/d\over Wr}
 ={(W/M)d\over d+1}{M\over dWr}
 ={1\over r(d+1)},                                        \tag{4.9}
\]

proving 4.  Summing (4.5) over the `r` possible marks in a fixed owner
proves 5. \(\square\)

### 4.2 Literal companion-tail spread inside the fractional orbit

For clarity, the local tail orbit can be made explicit.  For an oriented
fresh lower path `P`, put

\[
 R(P)=S_0\cup\{b_1,\ldots,b_{d-1}\},\qquad
 K_2(P)=S_0\cup\{b_1,b_2\}.                               \tag{4.10}
\]

Then `|R(P)|=r-1` and `|K_2(P)|=t+2`.  A level-two queue tail is an
**unordered** set

\[
 Y\in{[k]\setminus R(P)\choose d-2},\qquad
 T=K_2(P)\cup Y,                                          \tag{4.11}
\]

and `Y\mapsto T` is injective.  Its orbit size is

\[
 N_{\rm tail}={k-r+1\choose d-2},\qquad
 \log N_{\rm tail}=\Theta(d\log d).                       \tag{4.12}
\]

For an `h`-fold macro, choose `h` pairwise disjoint such tails and the
remaining private FIFO completion labels.  The complete macro orbit is
uniform on these literal choices.  Thus (4.12) is a genuine
superpolynomial local companion supply inside the fractional factor.
Indeed the spare-coordinate inequality is exactly

\[
 k-r+1\ge h(d+1):                                         \tag{4.13}
\]

the `h` tails use `h(d-2)` labels and leave the required `3h` labels for
the two earlier private queue positions and the terminal insertion of each
copy.

Theorem 4.1 is stronger than a separately chosen path factor followed by
owner decoration: it correlates the lower blocks, **all** owner resources,
the exact `2/3` multiplicities, and the sharp `b_2` capacity in one vector.
It is nevertheless fractional.  It does not prove an integral
owner-disjoint macro selector, a marked cylinder, or hereditary
regeneration.

## 5. A literal one-for-one reservoir switch

The coloured spectral escape theorem gives a useful integral operation
which is stronger than post-hoc orientation.

### Theorem 5.1 (fresh reservoir switch)

Let `\mathcal P` be any matching of oriented fresh `d`-paths and let

\[
 U=\mathcal L\setminus\bigcup_{P\in\mathcal P}V(P)        \tag{5.1}
\]

be its lower leave.  Fix `H\subseteq[k]`.  If, for some selected path
`P\in\mathcal P`,

\[
 {|U|+d\over M}>
 {4|H|\over k}+{12d+2\over k},                            \tag{5.2}
\]

then there is an oriented fresh path `Q\subseteq U\cup V(P)` with

\[
                         c(Q)\notin H.                     \tag{5.3}
\]

Replacing `P` by `Q` preserves the number of paths and the size of the
leave, and does not meet any other selected path.

#### Proof

Apply the failure bound (3.2) of the coloured spectral escape theorem to
the lower family `X=U\cup V(P)`.  Inequality (5.2) says that `X` cannot be
a counterexample, so it contains `Q` satisfying (5.3).  The set `X` is
disjoint from every selected path other than `P`.  Both `P` and `Q` have
`d` lower vertices, hence the replacement preserves the matching size and
leave size. \(\square\)

### Corollary 5.2 (erase every fixed separator-scale hotspot)

Fix `A\ge0`.  If

\[
 |H|\le {Ak\over d},\qquad
 |U|\ge {(4A+14)M\over d},                                \tag{5.4}
\]

then a finite sequence of one-for-one reservoir switches transforms
`\mathcal P` into a matching of the same size with no selected path coloured
in `H`.

#### Proof

As long as an `H`-coloured path remains, apply Theorem 5.1 to it.  The
leave size remains fixed, and no replacement has colour in `H`, so the
number of `H`-coloured paths decreases by one. \(\square\)

This directly defeats the codimension-eight fixed-mark trap once a
constant-factor `O(M/d)` separator is retained.  That trap is therefore not
an invariant of the fresh-path exchange component.  Corollary 5.2 does
**not** balance all coordinates at once: a set of coordinates above a
constant-factor average cap can have size `Theta(k)`, while (5.4) only
permits `O(k/d)` protected colours.  This is the exact gap between local
escape and global coloured matching.

The switches in this section act only on the undecorated lower-path
matching.  They do not preserve a previously assigned colour-slot index,
owner tails, the `h=2,3` macro grouping, owner disjointness, or chronology.
Those resources must be regenerated after the lower switch, or included in
a stronger compound switch theorem.

There is, however, an unconditional global coarse balance consequence.

### Theorem 5.3 (top-`h` quadratic descent)

Let `N=|\mathcal P|`, and fix `1\le h<k` such that

\[
 {|U|+d\over M}>{4h\over k}+{12d+2\over k}.              \tag{5.5}
\]

There is a sequence of one-for-one reservoir switches leading to a matching
of the same size and leave size whose colour loads `n_s` satisfy

\[
 \boxed{
 \max_s n_s\le \left\lfloor {N\over h+1}\right\rfloor+1.}
\tag{5.6}
\]

#### Proof

At any state, order the loads as

\[
                         n_1\ge n_2\ge\cdots\ge n_k.       \tag{5.7}
\]

If `n_1\ge n_{h+1}+2`, let `H` be the current top `h` colours and remove a
path of a maximum-load colour.  Theorem 5.1 supplies a replacement whose
colour lies outside `H`, and hence has current load at most `n_{h+1}`.

For the integral potential

\[
                         \Phi=\sum_{s=1}^k n_s^2,          \tag{5.8}
\]

this switch changes the two affected terms by

\[
 (n_1-1)^2+(n_s+1)^2-n_1^2-n_s^2
       =2(n_s-n_1+1)\le-2.                                \tag{5.9}
\]

Thus the process terminates, and at termination
`n_1\le n_{h+1}+1`.  Since `(h+1)n_{h+1}\le N`, (5.6) follows. \(\square\)

If `|U|=C M/d` with a sufficiently large fixed `C`, condition (5.5) permits

\[
                         h=\Theta(k/d).                    \tag{5.10}
\]

Since `N=Theta(M/d)`, Theorem 5.3 gives

\[
                         \max_s n_s=O(M/k).                \tag{5.11}
\]

This is a genuine global integral improvement over an arbitrary hotspot,
but it is still a factor `d` above the sharp cap `M/(kd)`.  Replacing
`O(M/k)` by `O(M/(kd))` is exactly the all-colour rounding row; it cannot be
claimed from the present escape inequality.

### Proposition 5.4 (the existential escape oracle has a sharp factor-`d` ceiling)

The conclusion of Theorem 5.3 is best possible if one uses only the
following information about a replacement: for every forbidden `h`-set of
colours, at least one permitted replacement colour lies outside it.

#### Proof

Fix a colour bank `B\subseteq[k]` of size `h+1`, and consider an abstract
replacement system in which the available colours at every state are
exactly `B`.  For every `H\subseteq[k]` with `|H|=h`, at least one member of
`B` lies outside `H`, so the stated existential escape property holds.

Nevertheless every `N`-path state supported by this system has

\[
                         \max_s n_s\ge {N\over h+1}.        \tag{5.12}
\]

Thus no argument which sees only the yes/no escape oracle can improve
(5.6).  At separator scale `h=Theta(k/d)`, the sharp colour cap requires
an additional factor `d`; obtaining it needs quantitative path counts,
alternating exchanges with prescribed endpoints, or a true coloured
matching theorem. \(\square\)

## 6. Sharp remaining theorem

The bottom marked selector is now separated into two statements.

1. **Solved, exactly:** the sharp-cap fractional lower-path factor,
   Theorem 2.1, and the stronger joint fractional
   lower/all-owner/`2/3`-macro factor, Theorem 4.1.
2. **Solved integrally at coarse scale:** fixed `O(k/d)` hotspots may be
   erased, and all colours may simultaneously be reduced to `O(M/k)`, by
   Theorems 5.1--5.3.
3. **Open:** improve the integral cap by the remaining factor `d`, while
   rounding the all-owner macro resources and retaining a fixed-factor
   marked cylinder through order `O(d)`.

A sufficient quantitative theorem is:

> **Pseudorandom macro-capacity rounding.**  For the slot-augmented `2/3`
> macro orbits of Section 4, there is a distribution on integral
> owner-disjoint macro matchings whose lower leave is `O(M/d)`, whose
> projection obeys (3.6), and whose prescribed marked-owner clusters obey
> the fixed-factor cylinder uniformly through order `O(d)`.

Already the lower-path projection has checked quantifiers: its rank is
`d+1`, its target error is `1/d`, and its normalized codegrees are exactly
(3.3)--(3.5).  The true macro edges have rank `Theta(d)` and the existing
macro theorem supplies vanishing pair codegrees, but not yet the complete
higher-codegree and hereditary marked-test ledger required by a uniform
nibble.  A uniform full-codegree theorem for those edges, or a compound
alternating-switch proof extending Section 5 to slots and owners, would
close the selector.  Theorem 4.1 by itself is a fractional factor, not a
cylinder theorem.

### 6.1 Why the available edge-colouring black boxes do not yet close it

It is worth recording the numerical audit, because the capacity slots make
the augmented degree much larger than the original path degree.  In the
central regime,

\[
 \log D=\Theta(d\log d),\qquad
 \log L=\Theta(k)=\Theta(d^2),\qquad
 \log(LD)=\Theta(d^2).                                    \tag{6.1}
\]

Thus lack of absolute degree is not the issue.  The first normalized
codegree is

\[
 {\Delta_2(\mathcal A)\over\Delta(\mathcal A)}
       =O(d^{-3}),                                         \tag{6.2}
\]

and the higher ones decay by another `O(d^-3)` per prescribed lower
vertex.

The classical Pippenger--Spencer theorem assumes fixed uniformity before
taking the degree to infinity and gives no threshold uniform in the rank.
It therefore cannot be diagonalized at rank `d+1` and requested error
`1/d`.

The 2025 full-codegree nibble theorem of Gould--Kelly is quantitatively
closer, but its published main statement also has the hierarchy

\[
 {1\over\Delta}\ll {1\over A}\ll\gamma\ll {1\over d}.
\tag{6.3}
\]

Even if one formally inserts (3.3), its bottleneck parameter is at most on
the scale

\[
 B\asymp
 \sqrt{\Delta/\Delta_2}=\Theta(d^{3/2}),                  \tag{6.4}
\]

while the stated leftover contains the factor
`B^{-1+gamma} log^A Delta`.  Since `log Delta=Theta(d^2)` and the hierarchy
requires `A` to be large rather than uniformly below `3/4`, the displayed
bound does not imply a `1/d` leave.  More fundamentally, its hidden degree
threshold is not uniform under `d\to\infty`.

The same quantifier issue applies to the fixed-rank pseudorandom matching
and conflict-free matching theorems.  Their conclusions are consistent
with the desired result, but none of their stated hypotheses and error
terms prove it for this diagonal parameter sequence.  A valid citation
would need an explicit theorem of the following form:

\[
 \begin{gathered}
 q=d+1,\quad
 \Delta_j\le\Delta\zeta^{j-1},\quad
 \zeta\le c d^{-3}
 \\
 \Longrightarrow\quad
 \text{lower leave at most }C|V_{\rm low}|/d,
 \end{gathered}                                            \tag{6.5}
\]

with constants independent of `d`, together with the marked test-function
version.  Equation (6.5), not a fixed-rank asymptotic theorem, is the exact
black-box target.

## 7. Dependencies and scope

The path degree and all-order codegrees are in
`MATH_THEOREM_FRESH_JOHNSON_PATH_PACKING_AND_ALL_ORDER_RESIDUAL_20260805.md`.
The marked escape inequality is in
`MATH_THEOREM_COLOURED_SPECTRAL_FRESH_PATH_ESCAPE_20260806.md`.
The legal owner tails and companion orbit are in
`MATH_THEOREM_FRESH_FIFO_BLOCK_CHAIN_KERNEL_AND_PAYLOAD_ATLAS_GATE_20260805.md`
and `MATH_THEOREM_SHARED_MARK_MACRO_COMPANION_SPREAD_CYLINDER_20260805.md`.

No claim is made here about owner-disjoint integral macro packing,
chronological joining, or hereditary regeneration after arbitrary accepted
macros.  Those are precisely the remaining integral rows.
