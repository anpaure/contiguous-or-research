# Independent audit of the fixed-factor cap-two LP, energy, and C6 applicability

**Date:** 2026-08-03  
**Method:** line-by-line symbolic and combinatorial audit; no finite search or
solver computation.  
**Verdict:** GO after one substantive scope repair and two clarifications.
The canonical LP, rainbow decomposition, general quadratic switch identity,
overlap-aware Boolean-hexagon formula, and occupied-phase upper bound are
correct.  The zero-occupied example proves only local pointer consistency,
not existence of a globally extendable Boolean factor pair.  The theorem
has been patched accordingly.

## 0. Audited files

The principal theorem after repair is

```text
1e60800bc78ab2c4a6f6d0fb884d42e0dcb725b2248b9c24e304ae1353cbf5f9
  MATH_THEOREM_FIXED_FACTOR_CAPTWO_LP_ENERGY_AND_C6_APPLICABILITY_20260803.md
```

Its fixed-factor input theorem is

```text
66d14b117304187df2cb1f16072a6e8cf7525f55d93a157be091e53436d379ce
  MATH_THEOREM_FIXED_FACTOR_FUNCTIONAL_DIGRAPH_STEINER_PARITY_AND_C6_20260803.md
```

Throughout, `m>=3`,

\[
 \mathcal M={ [2m-1]\choose m},\qquad
 \mathcal U={ [2m-1]\choose m+1},
\]

and `H=G-F_0` is `(m-1)`-regular on both middle-set shores.  Every upper
colour class has exactly `m+1` arcs and exactly one outgoing arc from each
of its `m+1` facet tails.

## 1. Canonical LP

At every tail and head, the constant vector

\[
                              x_e={1\over m-1}
\]

has total load one.  An upper colour has load

\[
                     {m+1\over m-1}=1+{2\over m-1},
\]

which belongs to `[1,2]` for every `m>=3`.  Therefore the canonical point
is feasible for the displayed tail/head/colour-box relaxation.

The count identity is also exact:

\[
 { |\mathcal M|\over |\mathcal U|}={m+1\over m-1},
 \qquad
 |\mathcal M|-|\mathcal U|
 ={2\over m-1}|\mathcal U|=\operatorname{Cat}_m.       \tag{1.1}
\]

An integral nonnegative solution to the unit tail rows selects one arc per
tail, and the unit head rows make those arcs a perfect matching.  The colour
box then says exactly that every colour occurs once or twice.  Hence the
integral points have the claimed interpretation.

The principal theorem originally said broadly that the selector has “no
fractional separator.”  What is proved is that the rows in its displayed LP
have a feasible fractional point.  Stronger valid inequalities are not
excluded.  The wording has been narrowed to that exact statement.

## 2. Rainbow base plus residual completion

Suppose a cap-two perfect matching `F` is given.  Choose one selected arc
of every upper colour and call the resulting set `Q`.  Since `Q subseteq F`,
it is a matching.  The remainder `P=F-Q` is vertex-disjoint from `Q`, and no
colour can occur twice in `P`, because it occurred at most twice in `F` and
one occurrence was removed.  Therefore `P` is rainbow.

The cardinalities are forced:

\[
 |Q|=|\mathcal U|,
 \qquad
 |P|=|\mathcal M|-|\mathcal U|=\operatorname{Cat}_m.   \tag{2.1}
\]

Conversely, if `Q` uses every colour once, `P` is rainbow, and their
vertex-disjoint union is perfect, then every colour occurs once from `Q`
and at most once more from `P`.  The cap-two condition follows.  This proves
the exact equivalence without prescribing the duplicate-colour set.

## 3. Quadratic switch identity, including repeated colours

For

\[
 f(z)={(z-1)(z-2)\over2},
 \qquad \Delta(F)=\sum_R f(\mu_R),
\]

direct expansion gives, for an arbitrary integer signed change `delta`,

\[
 f(\mu+\delta)-f(\mu)
 =\mu\delta+{\delta^2-3\delta\over2}.                  \tag{3.1}
\]

An alternating cycle removes and inserts the same number of edges, so its
consolidated colour changes satisfy

\[
                              \sum_R\delta_R=0.
\]

Summing (3.1) therefore proves

\[
 \boxed{
 \Delta(F\mathbin\triangle Z)-\Delta(F)
 =\sum_R\mu_R\delta_R+{1\over2}\sum_R\delta_R^2.}      \tag{3.2}
\]

No simplicity assumption is used: a colour may appear repeatedly among
the removed edges, the inserted edges, or both.  All its contributions
must first be combined into its one net integer `delta_R`.  If the removed
and inserted colour sets are disjoint, simple, and of equal size `ell`,
there are `ell` entries `-1` and `ell` entries `+1`, yielding the displayed
specialization in the theorem.

## 4. Boolean C6 colours and every possible overlap

Fix a full supported triple `{a,b,c}` over a core `C`, and write
`x_a=f_C(a)`, etc.  Full support plus fixed-point-freeness implies

\[
                         x_a,x_b,x_c\notin\{a,b,c\}.    \tag{4.1}
\]

The old and new colour triples are

\[
\begin{aligned}
\mathcal O&=\{C+ab+x_a,\ C+bc+x_b,\ C+ac+x_c\},\\
\mathcal N&=\{C+ac+x_a,\ C+ab+x_b,\ C+bc+x_c\}.
\end{aligned}                                          \tag{4.2}
\]

Intersecting any member with `{a,b,c}` recovers exactly the displayed
two-element pair.  Hence the three colours within each phase are distinct,
and an old colour can equal a new colour only when their displayed
two-element pairs agree.  The three possible equalities are exactly

\[
 x_a=x_b,
 \qquad x_b=x_c,
 \qquad x_c=x_a.                                       \tag{4.3}
\]

Let `kappa=|O intersection N|`.  Cancelling those common colours leaves
`3-kappa` removed and `3-kappa` inserted colours, all simple and mutually
disjoint.  Formula (3.2) becomes

\[
 \Delta(F')-\Delta(F)
 =\sum_{R\in\mathcal N\setminus\mathcal O}\mu_R
  -\sum_{R\in\mathcal O\setminus\mathcal N}\mu_R
  +(3-\kappa).                                         \tag{4.4}
\]

Because the quantities are integral, strict negativity is equivalent to

\[
 \sum_{R\in\mathcal O\setminus\mathcal N}\mu_R
 -\sum_{R\in\mathcal N\setminus\mathcal O}\mu_R
 \ge4-\kappa.                                          \tag{4.5}
\]

If all inserted colours are holes and all removed colours have multiplicity
at least two, (4.4) is at most `-(3-kappa)` whenever the switch changes the
colour vector.  Thus the overlap cases are fully and correctly priced.

## 5. Which potential C6s are occupied

For the incumbent second matching, define

\[
                       F(C+a)=C+a+g_C(a).
\]

The first alternating phase of the hexagon is contained in `F` exactly
when

\[
                  g_C(a)=b,\qquad g_C(b)=c,
                  \qquad g_C(c)=a,                     \tag{5.1}
\]

and the other phase is contained exactly when the arrows are reversed.
Full support is what guarantees that the complementary three edges survive
the deletion of `F_0`.  Thus an occupied full hexagon is exactly a directed
3-cycle of `g_C` whose support is full for `f_C`.

Directed cycles of a function are vertex-disjoint.  Since
`|[2m-1]-C|=m+1`, at most

\[
                         \left\lfloor{m+1\over3}\right\rfloor
                                                                    \tag{5.2}
\]

occupied full supports can occur at one core.  This part applies to every
actual incumbent second matching.

There is one additional local matching constraint worth recording.  Neither
`f_C` nor `g_C` can contain a directed 2-cycle: `a->b` and `b->a` would send
the two distinct lower vertices `C+a,C+b` to the same head `C+ab`.

For `m>=7`, the local maps on `Z/(m+1)Z`

\[
                         g_C(a)=a+1,\qquad f_C(a)=a+2   \tag{5.3}
\]

are fixed-point-free, have no directed 2-cycles, have distinct pointers at
every lower vertex, and therefore define two disjoint matchings on this
one core-star.  The first is one long cycle and has no directed 3-cycle,
while the general union-bound theorem gives cubic full-support supply for
the second pointer map.

This proves that the local pointer axioms—including local head injectivity—
do not force an occupied C6.  It does **not** prove that these two partial
matchings extend simultaneously to global perfect matchings of the Boolean
incidence graph.  The earlier wording “the incumbent may occupy none” was
therefore stronger than its proof.  The theorem has been patched to state
only the local-consistency obstruction.  The universal upper bound (5.2)
is unaffected.

## 6. Functional C8 counterexample: exact scope

The eight edges

\[
 e_i=L_iM_i,\qquad h_i=L_iM_{i+1}\quad(i\bmod4)
\]

form one bipartite 8-cycle, whose only perfect matchings are

\[
 E=\{e_0,e_1,e_2,e_3\},\qquad
 J=\{h_0,h_1,h_2,h_3\}.                                \tag{6.1}
\]

Colour `e_0,e_1,e_2,h_3` red and
`e_3,h_0,h_1,h_2` blue.  Each tail has one red and one blue outgoing edge,
so each colour is a four-edge functional class.  Every vertex has total
degree two.  The half-edge vector has unit tail and head loads and exact
colour load two.

The colour-tail and colour-head projections both have SDRs: for example,
red and blue may use distinct tails `L_0,L_3` and distinct heads `M_0,M_3`.
But the two integral cycle covers have colour vectors

\[
                              (3,1)\quad\hbox{and}\quad(1,3),
\]

so neither is cap-two.

This is a valid integrality obstruction for the listed row system.  It is
not a Boolean counterexample.  At `m=3` the true Boolean host has ten
middle vertices and five upper colours, and its colour classes are tied by
one root map across overlapping facet systems.  The 4-by-4, two-colour C8
does not encode those layer cardinalities, colour-facet incidences, or
cross-colour root consistency.  It proves only that regularity,
one-outgoing-per-tail functionality, the canonical fractional point, and
the two marginal SDRs do not imply integral cap-two selection without
additional Boolean structure.

## 7. Final proof-safe frontier

The audited chain is

\[
\boxed{
\begin{array}{c}
\text{canonical cap-two LP is feasible}\\
\Downarrow\\
\text{integral rainbow base plus rainbow residual completion is open}\\
\Downarrow\\
\text{one-component topology is deferred}.
\end{array}}
\]

The exact switch gradient (3.2) and occupied-C6 characterization (5.1) are
available.  Cubic potential support cannot alone imply applicability:
actual occupied supports are at most linear per core, and local matching
constraints permit zero.  A positive theorem must force a useful occupied
cycle, route defects through longer alternating cycles, or prove the
rainbow residual completion directly.  No Boolean cap-two second factor is
claimed here.
