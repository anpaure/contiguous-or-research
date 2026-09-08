# Distributed-core antecedents of pure rails: exact lower and upper ledgers

**Date:** 2026-08-13  
**Method:** cyclic core-emission schedules and literal interval unions  
**Status:** unconditional local theorem.  It shows that the repeated-core
source presentation of a pure owner rail is far from maximal: the fixed
owner core may be distributed across the `q` source phases while preserving
the entire owner and upper deck.  This repairs the private-letter defect of
common-core source words and exposes an explicit lower-deck design problem.
It does not assert that the resulting lower deck is globally complete.

## 1. Set-up

Let `q>=2` and let

\[
                         \sigma=(x_i)_{i\in\mathbb Z_N}           \tag{1.1}
\]

be a cyclic order of `N>=2q` distinct toggle coordinates.  Let `F` be a
disjoint fixed core.  For every `f in F`, choose a set of emission positions

\[
                         E_f\subseteq\mathbb Z_N                       \tag{1.2}
\]

which meets every cyclic interval of `q` consecutive positions.  Put

\[
                         G_i=\{f\in F:i\in E_f\}                       \tag{1.3}
\]

and define the source cycle

\[
                         A_i=G_i\cup\{x_i\}
                         \qquad(i\in\mathbb Z_N).                      \tag{1.4}
\]

For a cyclic interval of source positions write

\[
                         A[i,\ell]=\bigcup_{t=0}^{\ell-1}A_{i+t}.
                                                                         \tag{1.5}
\]

The emission condition is exactly a cyclic hitting condition.  Since one
position belongs to `q` cyclic `q`-intervals, double counting gives

\[
                         |E_f|\geq\left\lceil{N\over q}\right\rceil.
                                                                         \tag{1.6}
\]

When `q` divides `N`, equality is attained by one residue class modulo
`q`.  This is the phase-partition specialization used below.  In fact a
minimum hitting set has size `ceil(N/q)`: if

\[
                         N=aq+b,\qquad0\leq b<q,             \tag{1.7}
\]

then the gaps between successive points of a hitting set are at most `q`,
and conversely any cyclic gap composition of `N` into `a+1` positive parts
at most `q` supplies a hitting set when `b>0` (use `a` parts when `b=0`).
Thus economical schedules exist at every legal period; only the especially
transparent disjoint phase partition needs `q|N`.

## 2. Exact interval ledger

### Theorem 2.1 (distributed-core formula)

For every `i` and every `1<=ell<=N`,

\[
 \boxed{
 A[i,\ell]
 =\left(\bigcup_{t=0}^{\ell-1}G_{i+t}\right)
   \cup\{x_i,x_{i+1},\ldots,x_{i+\ell-1}\}.}                    \tag{2.1}
\]

Consequently:

1. for `1<=ell<q`,
   \[
    A[i,\ell]
    =(G_i\cup\cdots\cup G_{i+\ell-1})
      \cup I_i^\ell(\sigma);                                    \tag{2.2}
   \]
2. for `q<=ell<N`,
   \[
    A[i,\ell]=F\cup I_i^\ell(\sigma);                           \tag{2.3}
   \]
3. in particular the length-`q` row is the usual pure-rail owner row
   \[
    T_i=A[i,q]=F\cup I_i^q(\sigma),                              \tag{2.4}
   \]
   and every longer proper row agrees literally with the repeated-core
   presentation;
4. if `|F|=R-q`, every owner in (2.4) has rank `R`, and the strict-lower
   rank at width `ell<q` is
   \[
    |A[i,\ell]|=\ell+
    \left|\bigcup_{t=0}^{\ell-1}G_{i+t}\right|.                  \tag{2.5}
   \]

#### Proof

Taking the union of (1.4) over the displayed interval gives (2.1).  If
`ell>=q`, the source interval contains a cyclic `q`-interval.  Every `E_f`
meets that subinterval, so its `G`-union is all of `F`, proving (2.3).
Equations (2.2), (2.4), and (2.5) follow. \(\square\)

### Corollary 2.2 (owner and upper transport)

Replacing the repeated-core source letters `F∪{x_i}` by (1.4) leaves every
interval-union row of width at least `q` unchanged.  Hence it preserves:

* the full rank-`R` owner multiset;
* every designated upper target carried by a consecutive owner interval;
* every all-width equality between pure rails whose rows are compared only
  at widths at least `q`; and
* the positive and zero run geometry of the owner trace.

This is literal equality, not just equality of ranks or incidence currents.

## 3. Private letters and minimality

### Theorem 3.1 (private toggle emission)

For every `i`, the toggle coordinate `x_i` occurs in the source cycle only
at address `i`.  Thus

\[
 x_i\in A_i\setminus\bigcup_{j\ne i}A_j.                         \tag{3.1}
\]

In particular no two adjacent source letters are comparable, and each
transition of the length-`q` owner row has the required outgoing and
incoming private coordinates `x_i` and `x_(i+q)` (subscripts modulo `N`).

Moreover, if all `G_j` are nonempty, every source letter remains nonempty
after deleting its toggle, so singleton toggle pins may be varied without
destroying source nonemptiness.

#### Proof

The toggle labels in (1.1) are distinct and disjoint from `F`; (3.1) follows
from (1.4).  For adjacent letters, `x_i` belongs only to the first and
`x_(i+1)` only to the second, so neither contains the other.  The last
claim follows from `G_i!=emptyset`. \(\square\)

Thus distributed cores exactly satisfy the private-letter necessity for a
flat middle row, unlike a literal nested diagonal fan.

## 4. Phase partitions and balanced lower ranks

Assume now that `q` divides `N`, and choose an ordered partition

\[
                         F=F_0\mathbin{\dot\cup}\cdots
                              \mathbin{\dot\cup}F_{q-1}.            \tag{4.1}
\]

For `f in F_s`, take

\[
                         E_f=\{i:i\equiv s\pmod q\}.                \tag{4.2}
\]

Then `G_i=F_(i mod q)`.  Every strict-lower interval meets distinct phase
blocks, and (2.5) specializes to

\[
                         |A[i,\ell]|=\ell+
                         \sum_{t=0}^{\ell-1}|F_{i+t}|.              \tag{4.3}
\]

Write

\[
                         |F|=aq+b,
                         \qquad0\leq b<q.                          \tag{4.4}
\]

Choose `b` phase blocks of size `a+1` and the other `q-b` blocks of size
`a`.  Then for every `ell<q`, the core contribution in (2.5) lies between

\[
                         a\ell
 \quad\hbox{and}\quad   a\ell+\min\{b,\ell\}.                    \tag{4.5}
\]

If the large blocks are distributed as evenly as possible around the
phase circle, the number in any `ell` consecutive phases is either
`floor(b ell/q)` or `ceil(b ell/q)`.  Hence the width-`ell` rank is one of

\[
 \ell+a\ell+\left\lfloor{b\ell\over q}\right\rfloor,
 \qquad
 \ell+a\ell+\left\lceil{b\ell\over q}\right\rceil.               \tag{4.6}
\]

At the central parameters `|F|=R-q`, the typical rank is therefore

\[
                         {R\over q}\ell+O(1).                       \tag{4.7}
\]

For `q=Theta(sqrt R)`, the `q-1` strict-lower widths traverse the whole
rank scale from `Theta(sqrt R)` up to `R-Theta(sqrt R)`, rather than being
stuck near rank `R`.

### Corollary 4.1 (exact remaining lower compiler)

Fix any factor of the rank-`R` owner layer into legal pure rails.  On every
rail choose a core-emission schedule satisfying (1.2), independently of
the other rails.  Then all owner and upper requirements of that factor
remain unchanged, and the complete strict-lower deck is the explicit family

\[
 \boxed{
 \left\{
 (G_i\cup\cdots\cup G_{i+\ell-1})\cup I_i^\ell(\sigma):
 \text{rail},\ i\in\mathbb Z_N, 1\leq\ell<q
 \right\}.}                                                       \tag{4.8}
\]

Thus the lower problem reduces to selecting the core-emission schedules
(and, when available, the rail factor) so that (4.8) covers every target
below rank `R`.  This is a concrete cyclic hitting/covering problem.  On
rails whose periods are divisible by `q`, the phase-partition construction
(4.1)--(4.7) gives its most economical form.  No further source-cap or
residence condition is hidden in the local closed-rail statement.

### Corollary 4.2 (state-space factorization of the schedule choice)

For a fixed pure owner rail `(F,sigma)`, the admissible source antecedents
of the form (1.4) are parametrized independently coordinate by coordinate:

\[
                         (E_f)_{f\in F}\in
                         \mathcal H_{N,q}^{F},                     \tag{4.9}
\]

where `H_(N,q)` is the family of hitting sets of cyclic `q`-intervals in
`Z_N`.  In particular the schedule bank has cardinality

\[
                         |\mathcal H_{N,q}|^{|F|}.                  \tag{4.10}
\]

Already the minimum schedules give the lower bound

\[
 |\mathcal H_{N,q}|
 \ge {N\over \lceil N/q\rceil},                                   \tag{4.11}
\]

by rotating one minimum hitting set and quotienting by its stabilizer.
Hence a rail with `|F|=Theta(R)` has exponentially many literal antecedent
choices even when its owner and upper rows are frozen.

#### Proof

The owner equation for a core coordinate `f` says exactly that every
length-`q` source interval contains an emission of `f`; this is the
definition of `E_f in H_(N,q)`.  No equation couples two different core
coordinates, so the choices form the Cartesian power (4.9).  Equations
(4.10)--(4.11) follow. \(\square\)

This exponential bank is not yet a lower-target covering theorem: one
target prescribes correlated membership choices for many core coordinates.
It does show that the antecedent is a large design variable, rather than a
fixed maximal erosion which must be accepted unchanged.

## 5. Exact single-cell programming at period `2q+1`

Take `N=2q+1`.  For every address `a in Z_N` put

\[
                         E_a=\{a-1,a,a+q\}.                        \tag{5.1}
\]

Its three cyclic gaps are `1,q,q`, so it meets every cyclic `q`-interval
and is a minimum emission schedule.

### Theorem 5.1 (arbitrary core mask at one strict-lower cell)

Fix a source interval

\[
                         J=[i,i+\ell-1],
                         \qquad1\leq\ell<q.                       \tag{5.2}
\]

Then

\[
                         E_{i-1}\cap J=\varnothing,
 \qquad                  E_i\cap J\ne\varnothing.                 \tag{5.3}
\]

Consequently, for every prescribed `H subseteq F`, choose

\[
                         E_f=
 \begin{cases}
 E_i,&f\in H,\\
 E_{i-1},&f\in F-H.
 \end{cases}                                                     \tag{5.4}
\]

The distributed-core source word then has the exact marked interval value

\[
                         A[i,\ell]=H\cup I_i^\ell(\sigma).         \tag{5.5}
\]

#### Proof

The positions of `E_(i-1)` are `i-2,i-1,i+q-1`.  The first two precede
`J`, while the last follows it because `ell<q`; hence it misses `J`.
The schedule `E_i` contains `i`, so it meets `J`.  Formula (5.4) makes
exactly the coordinates of `H` emit somewhere in `J`.  Apply (2.1).
\(\square\)

### Corollary 5.2 (local rank span)

For one period-`2q+1` pure rail with core size `|F|=R-q`, every set of the
form

\[
                         H\cup I_i^\ell(\sigma),
 \qquad H\subseteq F,quad1\leq\ell<q,                         \tag{5.6}
\]

is realizable at its indicated source interval by an admissible antecedent
of the *same* owner and upper rail.  Its rank is `|H|+ell`; these ranks span
`1,...,R-1`.

This is a one-cell programming theorem.  Different requested cells impose
simultaneous hit/avoid conditions on each `E_f`; arbitrary collections of
them need not be compatible.  The exact multi-cell gate is a product of
cyclic hitting-set constraint systems, one per core coordinate.

### Theorem 5.3 (immediate-lower-preserving programming)

Assume `q>=4` and, for every `a in Z_(2q+1)`, put

\[
                         S_a=\{a,a+q-1,a+2q-2\}.                   \tag{5.7}
\]

The cyclic gaps of `S_a` are `q-1,q-1,3`.  Hence `S_a` meets every
cyclic interval of `q-1` consecutive source positions.  In particular it
is an admissible owner schedule and it also preserves the fixed core in
every width-`q-1` source cell.

For any

\[
                         J=[i,i+\ell-1],
                         \qquad1\leq\ell\leq q-2,                 \tag{5.8}
\]

one has

\[
                         S_{i-1}\cap J=\varnothing,
 \qquad                  S_i\cap J\ne\varnothing.                 \tag{5.9}
\]

Therefore the coordinatewise choice

\[
                         E_f=
 \begin{cases}
 S_i,&f\in H,\\
 S_{i-1},&f\in F-H
 \end{cases}                                                     \tag{5.10}
\]

realizes

\[
                         A[i,\ell]=H\cup I_i^\ell(\sigma)         \tag{5.11}
\]

for any `H subseteq F`, while leaving every interval-union row of width
at least `q-1` unchanged from the repeated-core pure rail.

#### Proof

Between consecutive points of `S_a` there are at most `q-2` unselected
positions, so every `(q-1)`-interval meets it.  The gap from `i-1` to
`i+q-2` in `S_(i-1)` has precisely the unselected positions

\[
                         i,i+1,\ldots,i+q-3,
\]

which contain `J`; thus the first relation in (5.9) holds.  The schedule
`S_i` contains `i`, proving the second.  Now (5.10)--(5.11) follow exactly
as in Theorem 5.1.  Since every selected schedule meets every
`(q-1)`-interval, each such interval emits every coordinate of `F`; longer
intervals do as well. \(\square\)

### Corollary 5.4 (three-shore invariance)

Suppose a period-`2q+1` pure rail is used inside an owner/immediate-lower/
upper construction.  Replacing its repeated-core antecedent by any schedule
built from the family `(S_a)` preserves literally:

* every rank-`R` owner at width `q`;
* every immediate-lower target at width `q-1`;
* every upper interval target at widths above `q`; and
* the complete owner residence trace.

At the same time any one cell of width at most `q-2` remains arbitrarily
programmable on the core by Theorem 5.3.  The simultaneous multi-cell
constraint is now a rotation-selection problem in the finite family
`{S_a:a in Z_(2q+1)}` for each core coordinate.

## 6. The sharper period-`q+2` two-hole ring

The shortest common-core ring with a simple immediate-upper row has period

\[
                         N=q+2.                                  \tag{6.1}
\]

For `q>=4`, define the two-emission schedules

\[
                         P_a=\{a,a+q-1\}
                         \subseteq\mathbb Z_{q+2}.                 \tag{6.2}
\]

Their cyclic gaps are `q-1` and `3`; hence they meet every cyclic
`(q-1)`-interval.

### Theorem 6.1 (two-hole three-shore programming)

Let a period-`q+2` pure rail have core `F`, toggle order `sigma`, and source
letters `(G_i∪{x_i})` obtained by assigning every `f in F` one schedule
`P_a`.  Then every source interval of width at least `q-1` has the same
union as in the repeated-core two-hole ring.

For every

\[
                         J=[i,i+\ell-1],
                         \qquad1\leq\ell\leq q-2,                 \tag{6.3}
\]

one has

\[
                         P_{i-1}\cap J=\varnothing,
 \qquad                  P_i\cap J\ne\varnothing.                 \tag{6.4}
\]

Thus, for arbitrary `H subseteq F`, choosing `P_i` on `H` and `P_(i-1)`
on `F-H` gives the exact short-cell value

\[
                         H\cup I_i^\ell(\sigma),                   \tag{6.5}
\]

while preserving literally the entire immediate-lower, owner, and upper
rows.

#### Proof

The gap bound proves the first statement.  The two positions of
`P_(i-1)` are `i-1` and `i+q-2`; the intervening unselected run is
`i,...,i+q-3`, which contains `J`.  The schedule `P_i` contains `i`.
Coordinatewise assignment and (2.1) give (6.5). \(\square\)

### Corollary 6.2 (link to the exact fractional packet factor)

The period-`q+2` rail is exactly the all-parity two-hole packet of
`MATH_THEOREM_ONE_STEP_TWO_HOLE_RING_ALL_PARITY_OWNER_LOWER_UPPER_FACTOR_20260806.md`.
That packet hypergraph has an exact symmetric fractional factor on the
owner and immediate-lower shores and, after the proved uniform marking, on
the immediate-upper shore.  Theorem 6.1 decorates every packet in this
fractional factor by an independent source-schedule bank without changing
any of those three resource incidences.

Consequently the remaining fractional lower problem is explicit: select,
for each core coordinate of each weighted packet, a rotation `P_a` so that
the marked strict-lower cells cover the required target measures.  The
integral problem additionally asks for a one-copy packet matching and one
simultaneous schedule choice.  Neither conclusion is claimed here.

The last sentence is local to closed rail components.  Opening and joining
components can create exterior intervals, so a final linear universal word
still needs a seam theorem or a bounded boundary charge.

## 7. Parameter boundary

A phase partition into `q` nonempty blocks requires

\[
                         |F|=R-q\geq q,                            \tag{5.1}
\]

or `R>=2q`.  This holds eventually in the target regime
`q=Theta(sqrt R)`.  It also requires a rail period divisible by `q`; period
`2q` is the canonical choice.  For other legal periods, including `2q+1`,
the general hitting schedules (1.2)--(1.6) remain available, at the cost of
repeating each core coordinate at least `ceil(N/q)` times.  If some phase
blocks are empty, all formulas remain correct and every toggle still makes
its source letter nonempty; only the final robustness sentence of Theorem
3.1 is lost.
