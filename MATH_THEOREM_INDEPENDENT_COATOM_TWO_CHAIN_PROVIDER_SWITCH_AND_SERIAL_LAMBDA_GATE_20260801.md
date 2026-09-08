# Coatom safe moves are exact two-chain provider switches; terminal `lambda` changes only through augmenting linkage

Date: 2026-08-01  
Status: exact local support/address theorem and exact one-step matching-rank
criterion.  This identifies the missing serial-routing theorem; it does not
prove bounded terminal compiler defect or an all-`k` upper bound.

## 0. Outcome

The canonical `0110` mixed-coatom move has a considerably sharper lower-side
description than “it exchanges `2(d-1)` supports.”  At every depth
`q=2,...,d`, it swaps two active labels between a filler-prefix flag and a
filler-suffix flag.  In the complete flat compiler, those four labels occupy
the same two physical cells in the two phases:

* all prefix cells have one common left endpoint;
* all suffix cells have one common right endpoint; and
* each exchanged target has exactly one provider inside the local compiler
  bank.

Thus one move is literally a simultaneous relabelling of two nested physical
cell chains.

This does **not** make the terminal deletion number monotone.  The rectangle
exchange preserves every rankwise one-coordinate degree, and the same local
switch can improve, preserve, or worsen maximum matching rank depending on
the unchanged exterior incidence edges.  The exact one-step criterion is an
augmenting-linkage count after the old matching edges lost by the move have
been removed.

Inside the unplanted common-order subcatalogue there is also a genuine
coupled-depth restriction: the pair-degree change at depth `q` equals that
at reflected depth `d+2-q`.  This is **not** an invariant of the enlarged
endpoint-planted safe catalogue.  The adjacent-order packets in
`MATH_THEOREM_COATOM_ADJACENT_ORDER_REFLECTION_BREAKERS_20260801.md` supply
all missing reflection-odd quadratic directions while retaining U1--U4.

Consequently the serial route has been reduced further, but not closed:

> prove that a reachable sequence of safe moves creates more vertex-disjoint
> compiler augmenting paths than the number of old matched edges it destroys,
> until only `O(1)` holes remain.

The nested chains are a routing interface.  They are not, by themselves, an
annihilator.

## 1. Exact two-chain support formula

Use the canonical `0110` screen pattern and write

\[
                   F=\{f_0,f_1,\ldots,f_{d+1}\}.
\]

For `2<=q<=d`, put

\[
 P_q=\{f_1,\ldots,f_{d+1-q}\},\qquad
 S_q=\{f_q,\ldots,f_d\}.                                    \tag{1.1}
\]

The three positive contracted connector rows use the following pairs of
active bases:

\[
\begin{array}{c|c|c}
\text{row}&A&B\\ \hline
0&I_{bc}&I_{ca}\\
1&I_{ab}&I_{bc}\\
2&I_{ca}&I_{ab}.
\end{array}                                                   \tag{1.2}
\]

Any suppressed fixed core is understood to be adjoined to every displayed
set.

### Theorem 1.1 (coupled flag rectangles)

At depth `q`, the exact old-only and new-only lower supports are

\[
\begin{aligned}
 \mathcal L_q^-&=\{A\cup P_q,\ B\cup S_q\},\\
 \mathcal L_q^+&=\{B\cup P_q,\ A\cup S_q\}.                  \tag{1.3}
\end{aligned}
\]

There are no other support differences at that depth.  Hence the signed
change is the rectangle circuit

\[
 \Delta_q=e_{B\cup P_q}+e_{A\cup S_q}
          -e_{A\cup P_q}-e_{B\cup S_q}.                       \tag{1.4}
\]

#### Proof

A window of `q+1<=d+1` tensor owners crosses at most one screen.  Windows
inside coatom blocks agree in the two phases.  A lower-screen window depends
only on a common active intersection.  At an upper screen, every two-sided
window again has the common active intersection, leaving only the one-sided
endpoint windows.  Their filler intersections are exactly `P_q` and `S_q`.
Reading the two active endpoint labels in the three connector rows gives
(1.2)--(1.3).  The two flags are distinct for `q>=2`; the literal audit finds
no further difference. \(\square\)

### Corollary 1.2 (all additive rankwise valuations are blind)

For every coordinate `x`,

\[
 \sum_{R\in\mathcal L_q^-}\mathbf 1_{x\in R}
 =\sum_{R\in\mathcal L_q^+}\mathbf 1_{x\in R}.               \tag{1.5}
\]

The two phases also have the same support cardinality.  Thus every potential
of the form

\[
            c_q\,|\mathcal L_q|+
            \sum_x w_{q,x}\sum_{R\in\mathcal L_q}\mathbf1_{x\in R}
                                                                    \tag{1.6}
\]

is invariant under the move at every depth separately.

This includes all scalar and one-coordinate incidence ledgers.  Any strict
serial potential must see at least pair correlations, physical addresses, or
matching alternating structure.

### Corollary 1.3 (depth choices are coupled)

One phase choice applies the same active transposition simultaneously to
all `d-1` flag rectangles.  It does not offer `d-1` independent switches.
Formally, if the three rows are placed over one fixed core and filler flag,
their active transpositions generate `S_3`, but that group permutes the
whole depth-flag vectors.  It cannot independently route individual depths.

This is a local fixed-atlas statement, not a claim that arbitrary packets at
different anchors lie in one global `S_3` orbit.

### Theorem 1.4 (common-order quadratic reflection invariant)

Let `mu_q(T)` count occurrences, with multiplicity, of intersections of
`q+1` consecutive owners, and define

\[
 D_q(x,y;T)=\sum_{R\supseteq\{x,y\}}\mu_q(T;R).              \tag{1.7}
\]

For every coordinate pair `{x,y}` and every `2<=q<=d`,

\[
 \boxed{
 D_q(x,y;T)-D_{d+2-q}(x,y;T)
 }
                                                                  \tag{1.8}
\]

is invariant under an unplanted common-order canonical coatom move, and
hence under compositions restricted to that subcatalogue.

#### Proof

Write `t=d+1-q`.  In (1.4), every pair has zero signed change except pairs
of an active label with a filler `f_i`.  For `{A,f_i}` the signed change is

\[
 \epsilon_t(i)=\mathbf1_{i\le t}-\mathbf1_{i>d-t},            \tag{1.9}
\]

and for `{B,f_i}` it is `-epsilon_t(i)`.  Reflected depth
`q'=d+2-q` has prefix length `d-t`, and

\[
 \epsilon_{d-t}(i)
 =\mathbf1_{i\le d-t}-\mathbf1_{i>t}
 =\epsilon_t(i).                                               \tag{1.10}
\]

Thus the two pair-degree changes agree.  The reverse move changes both
signs, and stepwise invariance telescopes along any serial walk. \(\square\)

When all involved target ranks lie between `2` and `k-2`, these yield, modulo
the point degrees, at least

\[
 \left\lfloor\frac{d-1}{2}\right\rfloor
       \left(\binom{k}{2}-k\right)                             \tag{1.11}
\]

independent rational invariants.  This count and the complete depth-two
Pluecker-span theorem are proved independently in
`MATH_THEOREM_COATOM_NESTED_FLAG_PLUCKER_AND_REFLECTION_INVARIANT_20260801.md`.
In particular, the canonical common-order nested chains alone are not a
depth-by-depth Markov basis.  This is a subcatalogue statement, not a safe
component obstruction.

## 2. Exact physical provider chains

Let `E_p` be the maximal depth-`d` erosion envelopes of the padded local
carrier.  A width-`h` compiler cell `[s,s+h)` can carry a target `R` exactly
when

1. `R` is contained in the union of its envelopes;
2. `R` contains every owner-coordinate whose complete envelope carrier lies
   in the cell; and
3. `R` meets every envelope not already hit by a mandatory coordinate.

This is the exact incidence predicate from the complete-flat-compiler
theorem, not merely equality with the maximal cell value.

Put

\[
                s_0=6d+17,\qquad h_q=d+1-q.                   \tag{2.1}
\]

Define

\[
 c_q^L=[s_0,s_0+h_q),\qquad
 c_q^R=[s_0+q,s_0+q+h_q).                                    \tag{2.2}
\]

All left cells have start `s_0`, and all right cells have endpoint
`s_0+d+1`.

### Theorem 2.1 (unique local providers)

Inside the complete padded local compiler bank, the old phase has exactly

\[
 A\cup P_q\longleftrightarrow c_q^L,\qquad
 B\cup S_q\longleftrightarrow c_q^R,                          \tag{2.3}
\]

and the new phase has exactly

\[
 B\cup P_q\longleftrightarrow c_q^L,\qquad
 A\cup S_q\longleftrightarrow c_q^R.                          \tag{2.4}
\]

Each displayed cell is the target's unique local provider.  Each crossed
target in (2.4) has no local provider in the old phase, and conversely for
(2.3).

#### Proof

Substitute the coatom envelope schedule into the three exact incidence
conditions.  On the prefix side, the only cell satisfying the allowed,
mandatory, and hit constraints begins at the upper screen and has width
`d+1-q`.  On the suffix side, the unique cell begins `q` positions later and
has the same width.  The active label at those two cells is exchanged by the
connector phase while the filler flag and address remain fixed.  Exhausting
all physical starts verifies uniqueness and the absence of a crossed
provider.  The calculation is uniform in the active row. \(\square\)

The theorem explains the word “router” literally: the move keeps both
physical chains and swaps their target labels.

## 3. The primary chains are not the complete incidence disturbance

The two chains describe the exact **support** difference.  A compiler edge
can change even when its target remains available elsewhere, because its
allowed, mandatory, or hit predicate changes.

For the first positive row, the complete padded local incidence graphs have
the following audited ranks:

\[
\begin{array}{c|r|r|r|r}
d&|\mathcal R^-\cup\mathcal R^+|&|\mathcal C|&
 \nu(H^-)=\nu(H^+)&\nu(H^-\cap H^+)\\ \hline
2&297&190&190&157\\
3&547&345&345&277\\
4&943&540&540&427\\
5&1597&775&775&607\\
6&2733&1050&1050&817.
\end{array}                                                    \tag{3.1}
\]

Here `H^- cap H^+` means edgewise intersection on the same physical cells.
Both phases saturate every local cell, but the common edge bank need not.
Therefore an exact terminal analysis must use the full compiler incidence
graph.  Counting only the `2(d-1)` support tokens can miss a quadratic
reassignment burden.

## 4. Exact one-move matching formula

Fix one boundary state `rho` and let

\[
 H^-=H_\rho(T),\qquad H^+=H_\rho(T')                         \tag{4.1}
\]

be the two compiler incidence graphs, with the same target shore
`mathcal R` and physical-cell shore `mathcal C`.  Put

\[
                 \delta_\rho(T)=|\mathcal R|-\nu(H_\rho(T)). \tag{4.2}
\]

Let `M` be any maximum matching of `H^-`.  Delete from `M` every edge which
is absent from `H^+`, obtaining `M_0`, and write

\[
                  \ell=|M|-|M_0|.                             \tag{4.3}
\]

Let `alpha(M_0,H^+)` be the maximum number of pairwise vertex-disjoint
`M_0`-augmenting paths in `H^+`.

### Theorem 4.1 (augmenting-linkage identity)

\[
 \boxed{
 \delta_\rho(T')-\delta_\rho(T)
       =\ell-\alpha(M_0,H^+).}                                \tag{4.4}
\]

In particular, this move strictly reduces the compiler deletion number in
the fixed state exactly when the new graph contains more disjoint augmenting
paths than the number of old matched edges destroyed.

#### Proof

`M_0` is a matching of `H^+` of size `\nu(H^-)-\ell`.  The symmetric
difference of `M_0` with a maximum matching of `H^+` decomposes into
alternating cycles, balanced paths, and pairwise vertex-disjoint augmenting
paths.  There can be no component with one more `M_0` edge than maximum-
matching edge, since exchanging on that component would enlarge the maximum
matching.  Hence

\[
             \nu(H^+)=|M_0|+\alpha(M_0,H^+).
\]

Substitution into (4.2) gives (4.4). \(\square\)

If the terminal compiler parameter optimizes over boundary states, then

\[
                  \lambda_d(T)=\min_\rho\delta_\rho(T),       \tag{4.5}
\]

and (4.4) applies state by state.  Changing the optimizing state can help,
but does not create monotonicity.

### Corollary 4.2 (the exact serial gate)

A sufficient serial certificate is one admissible compiler state carried
through the route, together with evolving matchings whose accumulated
augmenting-linkage surplus recovers all but `O(1)` unmatched targets.  More
generally, (4.4) is the exact transition law whenever the state is fixed
across that transition.  The new chain targets are possible starting
vertices for these paths; the displaced old targets must be rerouted through
common or exterior alternate providers.

Allowing the optimizing state in (4.5) to change between moves may help, but
then the one-step quantities do not automatically telescope.  A global
serial theorem must either carry one evolving state/matching or include an
explicit state-regeneration inequality.  This is the missing correlated
theorem in the serial route.

## 5. Non-monotonicity is genuine, not an artefact of the tensor

Retain just one prefix/suffix cell pair `L,R`.  In the old phase let

\[
       AP\!\sim L,\quad BS\!\sim R,
\]

and in the new phase let

\[
       BP\!\sim L,\quad AS\!\sim R.
\]

Add unchanged external cells in three ways.  Direct maximum-matching
calculation gives

\[
\begin{array}{c|c|c}
\text{host}&\nu(H^-)&\nu(H^+)\\ \hline
\text{external alternates only for old labels}&2&4\\
\text{external alternates for all four labels}&4&4\\
\text{external alternates only for new labels}&4&2.
\end{array}                                                    \tag{5.1}
\]

The labels “old” and “new” in the first column are relative to which labels
are locally present; reversing the move reverses the sign.  Thus the exact
same nested provider switch can improve, preserve, or worsen defect.  Any
proof based only on the local chain formula is impossible; the exterior
alternating graph is essential.

## 6. Consequence for the `B+O(1)` program

The serial-safe-move theorem remains a strict reduction: intermediate
compilers need not survive, and packet supports may overlap in time.  The
present result now separates what the local move supplies from what a global
proof must add.

### Supplied exactly

1. safe upper/residence motion in the carrier graph;
2. `d-1` synchronized rankwise rectangle circuits;
3. two nested physical provider chains with fixed opposite endpoints; and
4. three active transposition types.

### Still missing

1. enough planted moves in every relevant reachable carrier;
2. a theorem producing the required exterior/common alternate-provider
   paths;
3. vertex-disjointness of those augmenting paths across successive moves;
4. a bounded terminal repair bank; and
5. use of the adjacent-order breaker directions when a common-order route
   would otherwise be quadratically trapped; and
6. regeneration under the same-parity lift.

The sharp next target is therefore:

> **Serial augmenting-linkage theorem.**  In every relevant same-parity
> child, there is a safe coatom route and a sequence of compiler states for
> which the total augmenting-path surplus
> `sum(alpha_i-ell_i)` is at least the initial defect minus an absolute
> constant, using canonical and adjacent-order safe packets as needed.

One should not expect `sum(alpha_i-ell_i)` to telescope without additional
compatibility: maximum matchings and boundary states can change between
steps.  A usable theorem must either maintain one evolving matching or give
a regeneration rule that canonically reselects it.

## 7. Replay

The dependency-light replay reconstructs all three positive rows for every
`2<=d<=12`, verifies the exact support rectangles, unique physical provider
addresses, crossed-provider absence, coordinate-degree invariance, and
reflected pair-degree invariance.  It also computes (3.1) and the three tiny
host ranks (5.1):

```text
python3 scratch/audit_coatom_two_chain_provider_switch_20260801.py
```

Expected status:

```text
PASS_COATOM_TWO_CHAIN_PROVIDER_SWITCH_AND_SERIAL_LAMBDA_GATE
```

No global safe-move reachability, bounded terminal `lambda`, or all-`k`
construction is claimed.
