# Bottom two-level matching: empty rectangles suffice, cylinder spread does not

**Date:** 2026-08-05  
**Method:** exact two-level FIFO algebra, Hall deficiency, and a direct
empty-rectangle union bound; no computation or search  
**Status:** rigorous sufficient probabilistic theorem and sharp logical
obstruction.  The bottom `s=2` problem is a rainbow matching of the graphs
of a complete-graph incidence atlas.  A uniform empty-rectangle estimate
gives the required `O(H/d^2)` discarded tasks.  The previously isolated
one-point cylinder/factorial-moment invariant does not imply that estimate:
it permits a two-component Hall imbalance with completely benign local
degrees.  A cut-spread or coordinate-balance invariant is genuinely new
information required at the bottom band.

## 1. Exact colour graph of one task

Fix a task `i` after owner levels `2,...,d` have been installed.  Put

\[
                         L_i=T_2^i-\{b_2^i,b_1^i\}.          \tag{1.1}
\]

Its fresh reservoir `Y_i` has size

\[
                         y=q-d+1=\Theta(d^2).                \tag{1.2}
\]

For distinct `x_2,x_1 in Y_i`, the two bottom owners are

\[
 \begin{aligned}
 T_1(i;x_2)&=L_i\cup\{b_1^i,x_2\},\\
 T_0(i;x_2,x_1)&=L_i\cup\{x_2,x_1\}.                       \tag{1.3}
 \end{aligned}
\]

Thus the colour graph of task `i` is the incidence graph

\[
                         x_2\longleftrightarrow\{x_2,x_1\}  \tag{1.4}
\]

of the complete graph on `Y_i`, after applying the two owner maps in (1.3).
It has `y(y-1)` labelled oriented edges.  A bottom completion is a rainbow
matching which chooses one colour edge per task.

## 2. Splitting the two owner roles

Let `I` be the task set, `|I|=n`.  From the bottom owner reservoir choose two
disjoint role banks `A_1,A_0`, each of size `n`; retain every excess owner in
the separator bank.

First form the bipartite graph

\[
 G_1:\quad i\sim T_1(i;x_2)\in A_1.                         \tag{2.1}
\]

A matching in `G_1` fixes one `x_2` for every matched task.  Conditional on
those choices, form

\[
 G_0:\quad i\sim T_0(i;x_2,x_1)\in A_0,\qquad x_1\ne x_2. \tag{2.2}
\]

Matchings in `G_1` and then `G_0` produce pairwise distinct bottom owners,
because the role banks are disjoint.  Conversely every completion respecting
the role split has this form.

The role split is only a sufficient subface of the full 3-uniform problem,
but it exposes the exact probabilistic requirement as an ordinary
bipartite matching statement.

## 3. A quantitative empty-rectangle theorem

Let `G` be a random bipartite graph with shores `L,R`, both of size `n`.
Fix \(d\to\infty\) and put

\[
                         s=\left\lceil {n\over d^2}\right\rceil.  \tag{3.1}
\]

Assume that for some absolute `c>0`, every fixed \(X\subseteq L\) and
\(Y\subseteq R\) satisfy

\[
 \boxed{
 \Pr(E_G(X,Y)=\varnothing)
      \le\exp\!\left(-{c d\over n}|X||Y|\right).}           \tag{3.2}
\]

### Theorem 3.1 (cut spread gives `n/d^2` deficiency)

With probability at least

\[
                         1-\exp(-c'n/d),                    \tag{3.3}
\]

the graph `G` has a matching leaving fewer than `s` vertices of each shore
unmatched, where `c'>0` is absolute.

#### Proof

For a bipartite graph with equal shores, the matching deficiency is

\[
                         \max_{X\subseteq L}(|X|-|N(X)|).    \tag{3.4}
\]

If it is at least `s`, there is a set `X` of size `x` such that, with

\[
                         Y=R-N(X),\qquad |Y|=y,              \tag{3.5}
\]

we have

\[
                         x+y\ge n+s                         \tag{3.6}
\]

and \(E(X,Y)=\varnothing\).  In particular `x,y>=s`.

Union bound over all fixed pairs `(X,Y)` satisfying (3.6).  Suppose first
that `a=min(x,y)<=n/2`.  The other size is at least `n+s-a>=n/2`.  Writing
the complement of the larger set, the number of choices is at most

\[
 \exp\!\left(3a\log{en\over a}\right).                     \tag{3.7}
\]

On the other hand `xy>=an/2`, so (3.2) is at most

\[
                         \exp(-cda/2).                       \tag{3.8}
\]

Because `a>=s>=n/d^2`,

\[
                         \log(en/a)\le\log(ed^2)=O(\log d), \tag{3.9}
\]

and `d>>log d`.  Summing (3.7)--(3.8) over all such `a` gives
\(\exp(-\Omega(ds))=\exp(-\Omega(n/d))\).

If both `x,y>n/2`, there are at most `4^n` pairs, while (3.2) is at most
`exp(-cdn/4)`.  This contribution is \(\exp(-\Omega(dn))\).  Combining the two
cases proves (3.3), and (3.4) gives the matching.  \(\square\)

### Corollary 3.2 (two-bank bottom completion)

Suppose `G_1` satisfies (3.2), and conditional on every first matching with
fewer than `s` discarded tasks the graph `G_0` also satisfies (3.2).  Then
there is a bottom completion after discarding fewer than

\[
                         2n/d^2                              \tag{3.10}
\]


tasks.

#### Proof

Apply Theorem 3.1 to `G_1` and discard its unmatched tasks.  Remove the same
number of arbitrary vertices from `A_0` to equalize the second pair of
shores; the hypothesis on the conditional `G_0` includes this equalized
bank.  Apply Theorem 3.1 again.  The two role banks make the resulting owner
pairs globally disjoint.  \(\square\)

This is stronger than the `O(n/d)` copy loss allowed by the scalar duplicate
ledger.

## 4. Why cylinder spread alone is insufficient

The cylinder invariant from the slack-level theorem controls factorial
moments of the number of occurrence-labelled skeletons through one owner.
It is a local degree statement.  It cannot rule out a balanced-looking
large cut.

### Proposition 4.1 (two-component obstruction)

For every \(d\to\infty\) and arbitrarily large `n`, there is an exchangeable
random law on bipartite graphs with shores of size `n` such that:

1. every realization has every degree `d(1+O(1/d))`;
2. for every fixed collection of vertex-disjoint occurrence incidences, the
   law's
   cylinder probability is `(1+o(1))` times that in a random degree-`d`
   graph; but
3. in every realization, every matching leaves \(\Omega(n/d)\) left vertices
   unmatched.

#### Proof

Put `epsilon=1/(10d)`.  Choose uniformly random labelled partitions of the
two shores with sizes

\[
 \begin{aligned}
 |L_1|&=(1/2+\varepsilon)n,& |L_2|&=(1/2-\varepsilon)n,\\
 |R_1|&=(1/2-\varepsilon)n,& |R_2|&=(1/2+\varepsilon)n.
                                                               \tag{4.1}
 \end{aligned}
\]

Place no edges between different indices.  Conditional on the partitions,
choose independent uniform simple biregular bipartite graphs inside
`L_i,R_i`.  In the first component take left degree
`d(1-2epsilon)+O(1)` and right degree `d(1+2epsilon)+O(1)`; reverse these
degrees in the second component.  Harmless divisibility rounding may be
absorbed into `o(n/d)` vertices.  The edge counts on the two shores agree.

All local degrees are `d(1+O(1/d))`.  Fix any bounded collection of `m`
vertex-disjoint requested incidences.  Averaging over the random labelled
partition contributes a factor `2^{-m+o(1)}` forcing each endpoint pair into
one common component, while the conditional component edge densities are
`(2+o(1))d/n`.  These factors cancel, giving cylinder probability
`(1+o(1))(d/n)^m`, just as in the unpartitioned random model.

Nevertheless, every realized graph has no cross-component edges.  Every
matching inside the first component leaves at least

\[
                         |L_1|-|R_1|=2\varepsilon n
                                      =\Omega(n/d)            \tag{4.2}
\]

left vertices unmatched.  \(\square\)

The same obstruction has a literal upper-star interpretation.  Fix one
coordinate `z`.  Skeletons containing `z` have upper stars entirely inside
the owner class containing `z`.  Skeletons not containing `z` can be kept
entirely outside that class by making `z` one of their forbidden future
coordinates.  A discrepancy of order `n/d` between the two task classes
and the two owner classes creates (4.2), while every individual star still
has the expected \(\Theta(d)\) list size.

Therefore the cylinder/factorial-moment invariant, by itself, cannot prove
the bottom matching theorem.  One must additionally control coordinate cuts
or, more generally, empty rectangles.

## 5. The exact new invariant

The proof-safe bottom target is now:

> **Bottom cut-spread lemma.**  Choose the upper-level owner matchings and
> the two role banks so that (3.2) holds for `G_1` and conditionally for
> `G_0`.

It is enough to establish (3.2) only for pairs with

\[
                         |X|+|Y|\ge n+n/d^2,                 \tag{5.1}
\]


because those are the only pairs arising from a Hall deficiency of the
forbidden size.

For the ideal independent model with edge density \(p=\Theta(d/n)\), (3.2) is
exact:

\[
                         (1-p)^{|X||Y|}
       \le\exp(-p|X||Y|).                                   \tag{5.2}
\]

Uniform (3.2) is stronger than one should expect from the literal Boolean
star model.  A coordinate gives a structured empty rectangle: skeletons
containing `z` have no neighbours among owners avoiding `z`.  In an ideal
coordinate-exchangeable sampling, for fixed label sets `X,Y` of size about
`n/2`, the event

\[
 \{hbox{all skeletons of }Xhbox{ contain }z\}
 \cap
 \{hbox{all owners of }Yhbox{ avoid }z\}                   \tag{5.3}
\]

already has probability \(\exp(-\Theta(n))\), whereas (3.2) asks for
\(\exp(-\Theta(dn))\).  Thus the independent-edge estimate is a clean
sufficient theorem, not yet a plausible literal invariant.

The physically credible replacement is a **container cut-spread theorem**:

1. every large empty rectangle not explained by a low-complexity coordinate
   container has the strong probability bound (3.2); and
2. every coordinate container has task-versus-owner discrepancy less than
   `n/d^2`.

There are only `k` one-coordinate containers, and more generally only
\(k^{O(d)}=\exp(O(d\log k))\) coordinate juntas of width `O(d)`.  Since
`n` is exponential in `k`, ordinary hypergeometric concentration controls
all such prescribed containers far below the `n/d^2` scale.  The missing
structural statement is that these low-complexity containers capture every
large Boolean-star Hall cut.

The physical theorem need not reproduce independent edges.  It needs only
either the upper bound (3.2), or the weaker container alternative above.
These may follow from negative dependence, a switching argument, and a
Boolean-shadow stability theorem.

Once this cut row is proved, Corollary 3.2 closes the fixed 3-uniform bottom
band with loss well below budget.  Without it, local cylinder spread is not
a sufficient invariant.

## 6. Dependencies

The fixed-rank bottom-band reduction is in

`MATH_THEOREM_BOTTOM_OWNER_BAND_FIXED_RANK_REDUCTION_20260805.md`.

The local cylinder invariant for slack levels is in

`MATH_THEOREM_EXCEPTIONAL_CORE_STAR_HALL_20260805.md`.
