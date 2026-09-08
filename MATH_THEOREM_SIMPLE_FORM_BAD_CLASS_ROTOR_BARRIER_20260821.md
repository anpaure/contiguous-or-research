# Simple-form bad classes have no internal colour-simple circulation

**Date:** 2026-08-21  
**Status:** unconditional theorem; no computation is used in the proof.

This note isolates an exact obstruction to the most direct
Curtis--Hines--Hurlbert--Moyer/difference-form attempt at a central
near-Ucycle.  A gap-multiset class whose every value has multiplicity at
least two cannot be closed internally, even if the omitted occurrence is
chosen separately for every cyclic form.  Consequently the positive-density
central family of non-good classes cannot be repaired class by class.  Any
simple-form construction retaining those forms must mix different gap
multisets at a linear number of quotient transitions (up to a factor
`m`), or use crossing forms.

This is a route-specific obstruction.  It neither disproves a central
near-Ucycle nor applies to the full tail-MTF palette.

## 1. Simple-form overlap graph

Fix integers `m>=2` and `n`.  A **simple oriented form** is a tuple

\[
 e=(a_1,\ldots,a_{m-1}),\qquad a_i\in\mathbb Z_{>0},
 \qquad r(e):=n-\sum_{i=1}^{m-1}a_i>0.                 \tag{1.1}
\]

Its colour is the cyclic class

\[
 \chi(e)=[a_1,\ldots,a_{m-1},r(e)]_{\rm cyc},          \tag{1.2}
\]

and its unordered gap class is the multiset

\[
 C(e)=\{a_1,\ldots,a_{m-1},r(e)\}_{\rm multi}.         \tag{1.3}
\]

Regard `e` as the directed overlap edge

\[
 (a_1,\ldots,a_{m-2})
 \longrightarrow
 (a_2,\ldots,a_{m-1}).                                \tag{1.4}
\]

A set of such edges is **colour-simple** if no two have the same colour
(1.2).  A circulation is a set of edges having equal indegree and outdegree
at every overlap vertex.  Hence every nonempty circulation decomposes into
directed cycles.

For one fixed multiset `C` of `m` positive integers summing to `n`, let
`D(C)` be the restriction of (1.4) to the edges with `C(e)=C`.  Call `C`
**good** if some value occurs exactly once, and **bad** otherwise.

## 2. Exact two-rotor transition law inside one class

Take two consecutive edges of a walk in `D(C)`, written

\[
 e_t=(a_t,a_{t+1},\ldots,a_{t+m-2}),\qquad
 e_{t+1}=(a_{t+1},\ldots,a_{t+m-1}),                  \tag{2.1}
\]

and put

\[
 r_t=n-\sum_{j=0}^{m-2}a_{t+j}.
\]

Equality of their full gap multisets gives

\[
 C-\{r_t\}-\{a_t\}+\{a_{t+m-1}\}=C-\{r_{t+1}\}.
\]

Cancellation in the free commutative monoid of multisets yields exactly
the following two possibilities:

\[
\begin{array}{c|cc}
 &a_{t+m-1}&r_{t+1}\\ \hline
 A&a_t&r_t\\
 B&r_t&a_t.
\end{array}                                             \tag{2.2}
\]

Equivalently, for the ordered state

\[
 s_t=(a_t,\ldots,a_{t+m-2},r_t),                       \tag{2.3}
\]

the two transitions are

\[
 A(x_1,\ldots,x_m)=(x_2,\ldots,x_{m-1},x_1,x_m),
\]

\[
 B(x_1,\ldots,x_m)=(x_2,\ldots,x_m,x_1).              \tag{2.4}
\]

Thus the difference-form overlap graph has the same two-rotor normal form
as the injective `(n-1)`-word graph, now acting on a multiset.  The `B`
move is a full cyclic rotation, so

\[
 \chi(Bs)=\chi(s).                                    \tag{2.5}
\]

## 3. Bad-class circulation theorem

### Theorem 3.1

If `C` is bad and nonconstant, `D(C)` contains no nonempty colour-simple
circulation.  The excluded constant multiset has one loop; it cannot occur
when `gcd(n,m)=1`, in particular when `n=2m+1`.

#### Proof

Suppose a nonempty colour-simple circulation exists and take one directed
cycle in it.  By (2.5), a `B` transition would put the same cyclic-form
colour on two consecutive edges.  It is therefore forbidden.  A one-edge
self-loop has its first `m-1` entries equal.  If the remaining entry differs,
it is a singleton and `C` is good; if it agrees, `C` is constant.  Both cases
are excluded by the hypotheses.

Every transition on the cycle is consequently `A`.  In particular the last
entry `r` of (2.3) is constant, while the first `m-1` entries are cyclically
rotated.

Because `C` is bad, the value `r` occurs somewhere among those first
`m-1` entries.  After some number of `A` rotations it reaches the first
position.  At that state `x_1=x_m=r`, so the two successors in (2.4)
coincide:

\[
 A(x_1,\ldots,x_m)=B(x_1,\ldots,x_m).
\]

By (2.5), the next edge has the same cyclic-form colour as the current
edge, contradicting colour-simplicity.  Hence no such cycle, and therefore
no nonempty circulation, exists.  \(\square\)

### Theorem 3.2 (converse for good classes)

If a value `r` occurs exactly once in `C`, orient every cyclic form of class
`C` by omitting that unique `r`.  The resulting edges constitute a
colour-simple Eulerian subgraph of `D(C)` containing every cyclic form of
the class exactly once.

#### Proof

The unique `r` gives one and only one orientation of each cyclic form.  The
edge words are precisely the distinct linear permutations of the multiset
`C-\{r\}`.  For every overlap vertex, prepending a permissible remaining
value and appending the same value give inverse bijections between its
incoming and outgoing edges.  Thus indegree equals outdegree.  Distinct
cyclic forms give distinct colours by construction.  \(\square\)

Together with the trivial loop for the constant class, Theorems 3.1--3.2
characterize exactly which individual unordered simple-form classes admit a
colour-simple internal circulation.

## 4. Quantitative run boundary

Consider a colour-simple directed walk in the full simple-form overlap graph
and a maximal consecutive segment whose edges all have the same bad,
nonconstant multiset class `C`.  Throughout any such segment, (2.5) again
forbids `B`, so the
omitted value `r` is fixed and the other `m-1` entries rotate.  If `r` has
multiplicity `p_r>=2` in `C`, at least `p_r-1` of those positions contain
`r`.  Before the segment can take more than `m-p_r` transitions, one of them
must reach the first position and force a repeated colour.  Hence the segment
has at most

\[
 m-p_r+1\le m-1                                      \tag{4.1}
\]

edges.

Therefore, if a colour-simple simple-form circulation uses `N_bad` bad-form
edges, it has at least

\[
 \left\lceil {N_{\rm bad}\over m-1}\right\rceil       \tag{4.2}
\]

transitions at which the unordered gap class changes (counted cyclically,
apart from the vacuous `N_bad=0` case).

At the central parameters `n=2m+1`, a positive proportion of all cyclic
simple forms are bad by Theorem 3.1 of
`MATH_AUDIT_CHHM_ALL_FORM_VOLTAGE_EULER_COMPONENT_GATE_20260726.md`.
Consequently an all-simple-form central
near-Ucycle cannot be assembled from independently closed class gadgets or
from a bounded repair attached to every bad class.  It needs macroscopic
cross-class circulation: at least `Omega(Cat_m/m)` class changes in the
quotient if it retains a positive density of the bad forms.  This lower
bound is still `o(Cat_m)` and is not by itself an obstruction to a genuinely
global construction.

## 5. What survives

The theorem rules out precisely these proposed shortcuts:

1. choose an omitted occurrence independently in every bad class and close
   that class by itself;
2. decompose every bad class into colour-simple internal cycles; or
3. repair the published good-class Euler system by adding isolated
   bad-class cycle gadgets.

Three logically possible direct routes remain:

1. one global simple-form circulation with `Omega(Cat_m/m)` cross-class
   transitions and favourable voltage;
2. crossing forms, whose gap sum is a larger multiple of `n`; or
3. the full injective-word/tail-MTF rotor, which is not confined to numeric
   difference forms.

Even a central near-Ucycle from one of these routes would still need the
Gaussian band and recurrence-gap conditions required by the DCC reduction.
