# Separator-funded slack closes the bottom cut problem conditionally on scalar tails

**Date:** 2026-08-05  
**Method:** exact owner accounting and the exceptional-core Hall lemma; no
computation or search  
**Status:** rigorous reduction and new budget trade.  The formerly targeted
`O(H/d^2)` bottom deficiency is stronger than the global construction needs.
Discarding `Theta(H/d)` copies *before* owner assignment frees `Theta(H)`
owner slots, because every copy consumes `d+1` owners.  The two bottom role
banks can then each be a fixed factor larger than the task shore.  Under the
same one-dimensional low-left/high-right tails already used at the slack
levels, both bottom matchings exist with only `o(H/d)` additional loss.  No
Boolean-star cut-spread or random-Sperner theorem is then required.

## 1. Exact slack amplification

Let `H_0` be the nominal number of punctured copies and let `W` be the
number of rank-`r` owners.  Assume the usual scalar inequality

\[
                         W\ge(d+1)H_0.                      \tag{1.1}
\]

Fix a constant `c>0`, put

\[
 s=\left\lceil{cH_0\over d}\right\rceil,
 \qquad
 H=H_0-s,                                                   \tag{1.2}
\]

and retain only `H` copies.  After owner levels `2,3,...,d` have been
installed, exactly `(d-1)H` owners are occupied.  Hence the bottom reservoir
`A_2` satisfies

\[
 \begin{aligned}
 |A_2|
 &=W-(d-1)H\\
 &\ge(d+1)H_0-(d-1)(H_0-s)\\
 &=2H+(d+1)s.                                               \tag{1.3}
 \end{aligned}
\]

Choose disjoint role banks `B_1,B_0 subseteq A_2` of equal size

\[
 M=H+\left\lfloor{(d+1)s\over2}\right\rfloor.              \tag{1.4}
\]

Then

\[
 {M\over H}
 =1+{c\over2}+O(1/d)+O(1/H).                               \tag{1.5}
\]

Thus an `O(H_0/d)` copy sacrifice creates a *constant-factor* right-side
slack in each bottom role graph.

For example, `c=2` gives

\[
                         M=(2-o(1))H.                       \tag{1.6}
\]

The identity (1.3) is the central point: copy loss and owner slack differ by
a factor `d`.

## 2. The two role graphs

After levels `2,...,d` are fixed, put

\[
                         L_i=T_2^i-\{b_2^i,b_1^i\}.         \tag{2.1}
\]

For a fresh `x_2`, set

\[
                         K_i=L_i\cup\{x_2\},
 \qquad
                         T_1=K_i\cup\{b_1^i\}.             \tag{2.2}
\]

The first role graph `G_1` joins task `i` to `T_1 in B_1` whenever (2.2)
holds with all freshness restrictions.

After a matching of `G_1` fixes `x_2^i` and `K_i`, the second role graph
`G_0` joins task `i` to

\[
                         T_0=K_i\cup\{x_1\}\in B_0          \tag{2.3}
\]

for a fresh `x_1`.  Matchings in `G_1` and `G_0` give globally distinct
bottom owners because the role banks are disjoint.

Write

\[
                         \beta={M\over H}>1.                \tag{2.4}
\]

In the product-residual model, a raw star of size `q-O(d)=Theta(d^2)` sees
the role-bank density

\[
                         {M\over W}={\beta+o(1)\over d+1}.  \tag{2.5}
\]

Its nominal left-degree scale is therefore

\[
                         a=\beta d+O(1).                    \tag{2.6}
\]

On the other hand, double counting all task--owner incidences shows that
the average right degree is

\[
                         {Ha\over M}=d+O(1),                \tag{2.7}
\]

a fixed factor below the left degree.

## 3. A deterministic two-tail theorem

Choose `eta>0` so small that

\[
                         (1-2\eta)\beta>1+2\eta.            \tag{3.1}
\]

For a role graph `G=(I,B;E)`, define

\[
 \begin{aligned}
 I_{\rm low}&=\{i:d_G(i)<(1-\eta)a\},\\
 B_{\rm high}&=\{T:d_G(T)>(1-2\eta)a\},\\
 \mathsf B(G)&=e_G(I,B_{\rm high}).                         \tag{3.2}
 \end{aligned}
\]

### Theorem 3.1 (slack bottom matching)

The graph `G` has a matching leaving unmatched at most

\[
 |I_{\rm low}|+{\mathsf B(G)\over\eta a}                   \tag{3.3}
\]

tasks.

#### Proof

This is the exceptional-core Hall lemma applied with nominal scale `a`.
Delete the low left vertices and the high right vertices.  Delete in
addition every remaining left vertex losing more than `eta a` incident
edges to the high-right set.  At most `mathsf B(G)/(eta a)` vertices are
lost in this second deletion.  The residual minimum left degree is at least
`(1-2eta)a`, while the maximum right degree is at most the same quantity.
Double counting proves Hall. \(\square\)

The role-bank size does not enter Hall directly; it creates the constant
gap between the natural left and right degree distributions which makes the
two exceptional tails small.

## 4. Probabilistic tail input

Suppose a role graph obeys

\[
 \begin{aligned}
 |I_{\rm low}|&\le H e^{-\gamma d},\\
 \mathsf B(G)&\le Ha e^{-\gamma d}                          \tag{4.1}
 \end{aligned}
\]

for an absolute `gamma>0`.  Then Theorem 3.1 loses only

\[
                         O(H e^{-\gamma d})=o(H/d)          \tag{4.2}
\]

tasks.

These are exactly scalar, one-dimensional tails.

* A fixed task list has hypergeometric mean `beta d+O(1)`; its lower tail
  below `(1-eta)a` is `e^{-Omega(d)}`.
* A fixed owner has mean right load `d+O(1)`.  By (3.1), the high threshold
  `(1-2eta)a` is a constant factor above that mean.  The occurrence-cylinder
  factorial-moment estimate therefore gives an `e^{-Omega(d)}` size-biased
  upper tail.

No union bound over Hall cuts is involved.  Exceptional tasks are discarded
rather than forbidden.

## 5. Sequential two-stage theorem

### Theorem 5.1 (separator-funded bottom completion)

Assume:

1. the upper owner levels `2,...,d` have been installed for the `H` retained
   copies;
2. `A_2` is partitioned into banks `B_1,B_0` as in (1.4);
3. `G_1` satisfies (4.1); and
4. there exists a matching of the exceptional-core remainder of `G_1` for
   which the resulting conditional graph `G_0` also satisfies (4.1).

Then complete FIFO owner paths exist after discarding a total of

\[
                         {cH_0\over d}+o(H_0/d)=O(H_0/d)    \tag{5.1}
\]

copies.

#### Proof

Discard the `s` copies in (1.2).  Apply Theorem 3.1 to `G_1`, discard its
exceptional-core loss, and fix the matching supplied in hypothesis 4.
Apply Theorem 3.1 to the resulting `G_0`.  The two role banks are disjoint,
so the two matchings use distinct owners.  Together with the already fixed
upper levels they form complete owner-disjoint FIFO paths.  Equations
(1.2) and (4.2) give (5.1). \(\square\)

The conditional quantifier in hypothesis 4 is genuine but much weaker than
the former cut-spread target.  It asks for one first matching preserving two
scalar tails, not for every first matching to preserve every Hall cut.

## 6. Comparison with the former target

Without the preliminary sacrifice, both role banks have asymptotic size
`H`, their left and right mean degrees are equal, and the exceptional-core
degree-ratio argument has no gap.  This led to the stronger target

\[
                         \operatorname{def}=O(H/d^2),       \tag{6.1}
\]

and to the independent random-Sperner/container problem.

But the global duplicate ledger already tolerates

\[
                         O(H/d)                             \tag{6.2}
\]

discarded copies: each discarded copy costs `d` lower positions, so (6.2)
costs only `O(H)=O(W/d)`, the separator scale.  Spending that allowance
before owner assignment creates the constant role-bank slack in (1.5).

Therefore (6.1) is unnecessary unless the same separator budget has already
been exhausted elsewhere.

## 7. Exact remaining mathematical row

The bottom theorem is reduced to:

> **Conditional scalar-tail preservation.** Choose the partition
> `A_2=B_1 dotcup B_0 dotcup B_sep` and one exceptional-core matching in
> `G_1` so that both (4.1) rows hold for `G_1` and for the induced `G_0`.

The first-stage tails follow from the existing product-thinning and
occurrence-cylinder estimates.  The only new correlation is preservation of
the second-stage low-left and size-biased high-right tails by *one* first
matching.  This is a scalar matching-selection problem, not an exponential
Hall-cut problem.

If this row is proved, the bottom owner band costs `O(H/d)` copies and no
small-junta, Sapozhenko, or random-Sperner theorem is needed.

## 8. A two-choice/bicircular reformulation with strict density margin

There is a second way to spend the same amplified reservoir which exposes a
standard sparse-graph object.  Split

\[
                         A_2=B_0\dot\cup B_1\dot\cup B_{\rm sep}, \tag{8.1}
\]

with

\[
                         |B_0|=\beta_0H,\qquad
                         |B_1|=\beta_1H,\qquad
 \beta_0>1,\quad\beta_1>2,quad
 \beta_0+\beta_1<2+c.                                      \tag{8.2}
\]

For `c=2`, for example, one may take `beta_0=3/2` and `beta_1=5/2`, up to
rounding.

For task `i`, choose an unordered fresh pair `{a,b}` and require

\[
 \begin{aligned}
 T_0(i;a,b)&=L_i\cup\{a,b\}\in B_0,\\
 T_1^a(i;a,b)&=L_i\cup\{a,b_1^i\}\in B_1,\\
 T_1^b(i;a,b)&=L_i\cup\{b,b_1^i\}\in B_1.
 \end{aligned}                                             \tag{8.3}
\]

Once `T_0` is selected, the two orientations of `{a,b}` give exactly the
two candidate level-one owners `T_1^a,T_1^b`.

In the product-residual model there are `Theta(d^4)` raw unordered pairs,
and the three required bank hits have density `Theta(d^{-3})`.  Hence the
task--`B_0` graph in (8.3) has degree

\[
                         \Theta(\beta_0\beta_1^2d).         \tag{8.4}
\]

Its average right degree is smaller by the factor `beta_0`, so the
exceptional-core lemma again gives a task-saturating `T_0` matching under
the corresponding scalar tails.

The selected `T_0` matching exports a multigraph `Q` on vertex set `B_1`:
task `i` contributes the edge

\[
                         T_1^a(i)T_1^b(i).                  \tag{8.5}
\]

There are `H` edges and `beta_1H` vertices, so its mean degree is

\[
                         {2\over\beta_1}<1.                 \tag{8.6}
\]

### Lemma 8.1 (exact orientation criterion)

The selected tasks admit pairwise distinct level-one owners if and only if
the edge--vertex incidence graph of `Q` has a matching saturating all edges.
Equivalently, every connected component of `Q` is a pseudoforest.

More generally, the exact number of tasks which must be deleted is

\[
                         \sum_C (e(C)-v(C))_+,              \tag{8.7}
\]

where the sum is over connected components of `Q`.

#### Proof

Choosing a level-one owner is orienting every edge of `Q` toward a distinct
endpoint.  Hall's condition for the edge--vertex incidence graph says that
every edge set spans at least as many vertices as edges.  This holds exactly
when every component has at most one cycle.  In a component with `e>v`, one
must delete at least `e-v` edges, and deleting that many cycle edges leaves a
unicyclic component.  Summing over components proves (8.7). \(\square\)

Thus an alternative exact final row is:

> choose the slack `T_0` matching so that its exported graph has bicircular
> excess `O(H/d)`.

The strict inequality (8.6) is important.  In an independent subcritical
random multigraph the total bicycle excess is tight (indeed `O(1)` with high
probability), far below `H/d`.  The remaining issue is to obtain the same
subcritical spread from a matching in the structured option graph.  This is
the receiver-bicycle form of the scalar-tail preservation problem, now with
a genuine constant density margin supplied by the separator budget.
