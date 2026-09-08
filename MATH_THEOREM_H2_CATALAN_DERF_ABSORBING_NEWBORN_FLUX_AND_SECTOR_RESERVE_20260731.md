# Absorbing newborn terminals: signed flux, complement expansion, and four-sector reserve

Date: 2026-07-31  
Status: exact all-parameter identities and all-parameter sufficient reserve
theorems; exact finite regeneration at `n=4 -> 5`; solver-free sector audits
through output parameter seven.  No all-parameter construction of an
absorbing newborn bank is claimed.

## 0. Result

Fix one strict DERF output at parameter `n`.  Its paths split canonically
into the inherited face `I=c+F_(n-1)` and the newborn complement `B`.  Fix
the orientation only of `B`, and allow every inherited path to be oriented
adversarially.

The complement form below agrees with
`MATH_THEOREM_THREAD_D_CATALAN_NEWBORN_RESERVE_ISOPERIMETRY_20260731.md`.
The new content here is the signed-flux decomposition, the exact
three-overlap identity, and the cumulative sector/deletion reserve state.

There are three equivalent and useful forms of the resulting robust SBE
condition.

1.  In the original Hall coordinate, for every outer family `U`, with
    `W=N(U)`, one needs

    \[
      N|U|\le R|W|+C\bigl(p_I(W)+t_B(W;y)\bigr).       \tag{0.1}
    \]

2.  In the complement coordinate `H=X\setminus W`, the same condition is

    \[
      R|H|+C\bigl(q_I(H)+t_B(H;y)\bigr)
      \le N|\partial H|.                              \tag{0.2}
    \]

    Here `q_I(H)` counts inherited endpoint pairs touched by `H`, and
    `partial H` is the set of outer rows having a neighbour in `H`.

3.  In the occurrence-slack coordinate, the exact worst-inherited numerator
    is

    \[
      h(W)+(2n+1)\bigl(\phi_B(W;y)-\chi_I(W)\bigr),   \tag{0.3}
    \]

    where `h` is the orientation-independent half-endpoint slack,
    `chi_I` counts inherited paths split by `W`, and `phi_B` is the signed
    newborn terminal flux across `W`.

Thus a dimension-uniform positive sufficient condition is

\[
 h(W)\ge (2n+1)\bigl(\chi_I(W)-\phi_B(W;y)\bigr)      \tag{0.4}
\]

on both shores and every occurrence neighbourhood.  In particular,
half-SBE together with `phi_B>=chi_I` is sufficient.  This is a structural
slack/flux theorem, not an orientation-integrality statement.

The strict four-sector lift gives a second exact reduction.  On each shore
the three source-overlap links form a path.  The robust slack of a union of
all four source sectors equals the sum of four sector slacks, minus the
three overlap charges, plus one exact credit for inherited endpoint pairs
split across the two feeders of the copied sector.  Cumulative nonnegative
reserve along this path is therefore an all-parameter sufficient
certificate.  Separate edge-by-edge payment is too strong and is refuted
on every authenticated output `n=5,6,7`.

## 1. Parameters and terminal statistics

At output parameter `n`, put

\[
 M={2n\choose n},\qquad N={2n\choose n-1},\qquad
 P={2n\choose n-2},\qquad K=M-N,\qquad
 C=M-P,\qquad R=N-C.                                  \tag{1.1}
\]

The middle ground is `X`, of order `M`, and the outer ground has order
`P`.  The complete output forest has exactly `K=Cat_n` components.  Write its
inherited and newborn path banks as `I` and `B`; hence

\[
                         |I|+|B|=K.                   \tag{1.2}
\]

For `W subseteq X`, define

\[
 p_I(W)=\#\{i\in I:\text{ both endpoints of }i\text{ lie in }W\}, \tag{1.3}
\]

\[
 \chi_I(W)=\#\{i\in I:\text{ exactly one endpoint of }i\text{ lies in }W\}, \tag{1.4}
\]

and let `t_B(W;y)` count the selected newborn terminals lying in `W`.
Let `delta_B(W)` count newborn endpoint incidences in `W`, with an isolated
path contributing two incidences at its repeated endpoint.  The signed
newborn flux is

\[
 \phi_B(W;y)=2t_B(W;y)-\delta_B(W).                   \tag{1.5}
\]

Equivalently, a nontrivial newborn path contributes `+1` when its selected
terminal is in `W` and its other endpoint is outside, `-1` in the opposite
case, and zero otherwise.  Isolated newborn paths contribute zero.

## 2. Exact complement-boundary form

For `H subseteq X`, let

\[
 \partial_sH=\{o\in O_s:N_{G_s}(o)\cap H\ne\varnothing\},       \tag{2.1}
\]

and let `q_I(H)` count inherited endpoint pairs with at least one endpoint
in `H`.  The fixed newborn orientation supplies `t_B(H;y)` selected
terminals in `H`.

### Theorem 2.1 (complement expansion equivalence)

The newborn orientation `y` absorbs every inherited orientation on shore
`s` if and only if, for every `H subseteq X`,

\[
 \boxed{R|H|+C\bigl(q_I(H)+t_B(H;y)\bigr)
             \le N|\partial_sH|.}                    \tag{2.2}
\]

#### Proof

For `S subseteq X`, put

\[
 O_s(S)=\{o:N_{G_s}(o)\subseteq S\}.
\]

Let

\[
 f(S)=R|S|+C\bigl(p_I(S)+t_B(S;y)\bigr).
\]

The function `f` is monotone.  Absorption applied to the maximal family
`O_s(S)` gives

\[
 N|O_s(S)|\le f(N(O_s(S)))\le f(S).                 \tag{2.3}
\]

Conversely, if this last inequality holds for every `S`, then for an
arbitrary outer family `U`, with `S=N(U)`, one has
`U subseteq O_s(S)` and hence `N|U|<=f(S)`.  Thus absorption is equivalent
to these maximal-closure rows.  Set `H=X\setminus S`.  Then

\[
 O_s(S)=O_s\setminus\partial_sH.                     \tag{2.4}
\]

Moreover

\[
 p_I(S)=|I|-q_I(H),\qquad
 t_B(S;y)=|B|-t_B(H;y).                              \tag{2.5}
\]

The total capacity identity is

\[
 NP=RM+C(|I|+|B|)=RM+CK.                             \tag{2.6}
\]

Subtracting the maximal-closure row from (2.6), using (2.4)--(2.5), gives
exactly (2.2), and the same algebra in reverse completes the equivalence.
\(\square\)

This form contains no orientation variables.  It is a weighted expansion
condition for a fixed terminal bank: a middle vertex costs `R`, a touched
inherited endpoint pair costs `C` once, and a selected newborn terminal
costs `C`.

## 3. Exact half-slack plus signed-flux identity

For an outer family `U`, put `W=N(U)`.  Retain occurrence multiplicity and
write

\[
 \kappa(W)=\sum_{v\in W}(d_G(v)-a_v),\qquad
 \delta(W)=\sum_{v\in W}(2-d_F(v)),                  \tag{3.1}
\]

where `a_v` is the number of occurrences from `U` to `v`.  Define the
twice-half-endpoint numerator

\[
 h(W)=n\kappa(W)+(n+1)\delta(W)-2|W|.                \tag{3.2}
\]

The standard occurrence-degree identity shows that `h(W)>=0` for every
row exactly when the half-endpoint point is SBE.

### Theorem 3.1 (signed-flux absorption identity)

For the worst inherited orientation and fixed newborn orientation `y`, the
exact scaled SBE numerator is

\[
 \boxed{h(W)+(2n+1)\bigl(\phi_B(W;y)-\chi_I(W)\bigr).} \tag{3.3}
\]

Consequently (0.4), on both shores and all rows, is necessary and
sufficient for `y` to be absorbing.

#### Proof

Split `delta=delta_I+delta_B`.  Worst inherited orientation gives

\[
 2p_I(W)=\delta_I(W)-\chi_I(W).                       \tag{3.4}
\]

The exact integral numerator with terminal count `p_I+t_B` is

\[
 n\kappa+(4n+2)(p_I+t_B)-n\delta-2|W|.               \tag{3.5}
\]

Substitute (3.4), use `phi_B=2t_B-delta_B`, and collect terms.  The result
is (3.3).  \(\square\)

### Corollary 3.2 (cut-column absorber packets)

Suppose the newborn paths can be partitioned into packets whose signed
endpoint-incidence columns satisfy, on every occurrence neighbourhood,

\[
 \sum_{b\in B_i}\phi_b(W)\ge\chi_i(W)                \tag{3.6}
\]

for the inherited path `i` assigned to the packet, where `chi_i(W)` is the
indicator that `W` splits the two endpoints of `i`, while every unused
packet has nonnegative total flux.  Require these packet inequalities
separately on both occurrence shores.  If the output half point is SBE on
both shores, then the newborn bank is absorbing.

This gives a proof-safe meaning to a paired absorber: it must dominate the
two possible directed cuts of an inherited endpoint pair simultaneously.
Merely assigning one local socket to each endpoint is insufficient.

## 4. Exact four-sector identity

Encode a collar sector by

\[
                        j=c+2z\in\{0,1,2,3\}.         \tag{4.1}
\]

Thus the isolated inherited face is middle sector `1`.  Split an outer
family as `U=U_0 dotcup U_1 dotcup U_2 dotcup U_3`, and put

\[
 W_{ij}=N(U_i)\cap X_j,\qquad W_i=\bigcup_jW_{ij}.    \tag{4.2}
\]

The source-overlap graphs are the paths

\[
 \text{upper: }0-2-3-1,
 \qquad
 \text{lower: }1-0-2-3.                              \tag{4.3}
\]

Their shared middle sectors are respectively `(0,2,1)` and `(1,2,3)`.
In particular the inherited link is `3-1` above and `1-0` below.

Define robust sector slack

\[
 \sigma_i=R|W_i|+C\bigl(p_I(W_i)+t_B(W_i;y)\bigr)-N|U_i|. \tag{4.4}
\]

For an overlap edge `e=ab`, let `O_e=W_a\cap W_b` and

\[
 \omega_e=R|O_e|+C\bigl(p_I(O_e)+t_B(O_e;y)\bigr).   \tag{4.5}
\]

Only the inherited link can have a nonzero `p_I` term.  Let `xi` count
inherited endpoint pairs with one endpoint in `W_a\setminus W_b` and the
other in `W_b\setminus W_a` on that link.

### Theorem 4.1 (three-overlap reserve identity)

The complete robust slack is exactly

\[
 \boxed{
 R|N(U)|+C\bigl(p_I(N(U))+t_B(N(U);y)\bigr)-N|U|
 =\sum_{i=0}^3\sigma_i-\sum_{e}\omega_e+C\xi.}       \tag{4.6}
\]

#### Proof

Every middle sector has at most two source sectors, so there are no triple
intersections and cardinality and newborn-terminal contributions obey
ordinary inclusion-exclusion over the three edges in (4.3).  Both endpoints
of every inherited path lie in middle sector `1`, which has exactly two
feeders.  For their two neighbourhoods `A,B`,

\[
 p_I(A\cup B)=p_I(A)+p_I(B)-p_I(A\cap B)+\xi.        \tag{4.7}
\]

Substitution into inclusion-exclusion proves (4.6).  \(\square\)

### Theorem 4.2 (exact cumulative sector-reserve criterion)

Choose either direction `v_0,v_1,v_2,v_3` along the appropriate path in
(4.3).  Let `e_k=v_(k-1)v_k` and put

\[
 \rho_0=\sigma_{v_0},\qquad
 \rho_k=\rho_{k-1}+\sigma_{v_k}-\omega_{e_k}
          +C\xi\,1[e_k\text{ is the inherited link}].        \tag{4.8}
\]

The fixed newborn bank absorbs every inherited orientation if and only if,
for every four-sector outer family on both shores,

\[
                         \rho_0,\rho_1,\rho_2,\rho_3\ge0,     \tag{4.9}
\]

for either fixed direction along each path in (4.3).

#### Proof

The recursion (4.8) is precisely inclusion-exclusion as connected source
sectors are adjoined along the overlap path.  Its final value `rho_3` is
the right side of (4.6), hence the complete robust slack.  Thus (4.9)
proves every robust Hall row.  Conversely, each proper prefix is itself a
valid outer family obtained by setting all later sector families to empty,
so absorption makes every `rho_k` nonnegative.  The proper-prefix values
are therefore an exact compositional state: they allow overlap debt to be
carried as reserve rather than requiring each sector to pay one edge in
isolation.  \(\square\)

This is an all-parameter sufficient theorem.  It is deliberately not the
false stronger rule `sigma_child>=omega_edge` at every rooted edge.

## 5. Equivalent deletion-reserve dynamics

For the complement deficit in (2.2), write

\[
 F(H)=R|H|+C(q_I(H)+t_B(H;y))-N|\partial H|,
 \qquad A(H)=-F(H).                                   \tag{5.1}
\]

Suppose `v in H`.  Let `a=1` when deleting `v` kills one `C`-resource:
`v` is a selected newborn terminal, or it is the last endpoint of an
inherited pair remaining in `H`.  Let

\[
 b=\#\{o:N(o)\cap H=\{v\}\}.                         \tag{5.2}
\]

Then exactly

\[
 A(H\setminus\{v\})=A(H)+R+Ca-Nb.                   \tag{5.3}
\]

Since `A(X)=0`, absorption is equivalently certified by a target-wise
deletion order from `X` to every `H` whose cumulative reserve never becomes
negative.  Indeed, the endpoint of every such order gives `A(H)>=0`;
conversely, under absorption every intermediate set has nonnegative reserve,
so any deletion order works.  The word **cumulative** is
load-bearing.  Requiring every single deletion to have nonnegative
increment is generally impossible: the base `R` reserve from earlier
deletions must sometimes pay a later last-neighbour loss.  Formula (5.3)
is the vertex-level analogue of (4.8).

## 6. Exact finite evidence and obstruction

The authenticated output at `n=5` is already proved absorbing.  Its 28
stored newborn orientations make both shores SBE for all `2^10=1024`
effective orientations of the 14 inherited paths (and hence all `2^14`
formal orientations after the four singleton bits are restored).  A
separate clean-room replay agrees.

The solver-free sector calculations below are frozen in

```text
scratch/audit_h2_catalan_derf_sector_payment_obstruction_20260731.py
scratch/h2_catalan_derf_sector_payment_obstruction_20260731.audit.json
```

For the authenticated outputs `n=5,6,7`, the deterministic sector audit
reconstructs the literal overlap paths and evaluates the full-sector
prefix reserves.  In the orders displayed below they are

\[
\begin{array}{c|c|r}
n&\text{shore}&(\rho_0,\rho_1,\rho_2,\rho_3)\\ \hline
5&\text{upper}&(1494,2844,1848,0)\\
5&\text{lower}&(1428,2850,1602,0)\\
6&\text{upper}&(34320,49995,33462,0)\\
6&\text{lower}&(14454,49137,32736,0)\\
7&\text{upper}&(568139,740597,519090,0)\\
7&\text{lower}&(155727,840697,626054,0).
\end{array}                                             \tag{6.1}
\]

The upper order is `0,2,3,1`; the lower order is `1,0,2,3`.  Thus full
sectors exhibit exactly the desired pooled-reserve shape.

However, every possible rooting of the stronger edge-local payment rule is
refuted already by the full-sector rows.  In particular, both directions
of the central noninherited overlap fail at every `n=5,6,7`; at `n=6` the
two deficits are `16533,17820` above and `16401,15972` below.  Exact
cross-pair credit is included and is zero on these witnesses.  Therefore
any proof must pool at least two adjacent sector reserves or work at the
vertex deletion-reserve level.

Each shore also has proper tight singleton-complement rows.  Their counts
at `n=6` are `8/1` (upper/lower), and at `n=7` are `9/2`.  Hence, if the
global absorbing inequality holds there, both its unrestricted and proper
maxima are exactly zero: there is no positive uniform margin to spend.

The exact global `n=5 -> 6` and `n=6 -> 7` absorbing-bank verdicts are not
claimed here.  Capped exact searches at `n=6` are retained as `UNKNOWN`;
they found no counterexample but did not prove its absence.  No `n=7`
heavy solve is inferred from the solver-free sector table.

The fail-closed finite provenance bundle is

```text
scratch/audit_h2_catalan_derf_newborn_replay_bundle_20260731.py
scratch/h2_catalan_derf_newborn_replay_bundle_20260731.audit.json
```

It binds the exact `n=5` primary and clean-room replays, both capped `n=6`
`UNKNOWN` runs and their executed sources, the tight-row catalogue, and the
sector-payment audit.  In particular, a reported solver bound of zero in
the `n=6` satisfaction runs has no proof content because those runs had no
objective.

## 7. Remaining theorem

Generic endpoint-orientation integrality is irrelevant here and already
false.  The precise positive all-parameter target is now one of the
following structural formulations.  Items 1, 3 and 4 are equivalent exact
criteria for a fixed bank; item 2 is a stronger constructive sufficient
condition:

1. prove the lift-specific margin (0.4);
2. construct cut-column newborn packets satisfying (3.6);
3. prove the cumulative four-sector reserve inequalities (4.9); or
4. give a target-wise nonnegative deletion-reserve shell using (5.3).

Any one of these supplies an absorbing newborn bank and removes all
ancestral orientation bits before the next common-`Q` choice.  None by
itself supplies the rooted physical sides, residence, deep shadows, or the
compiler.
