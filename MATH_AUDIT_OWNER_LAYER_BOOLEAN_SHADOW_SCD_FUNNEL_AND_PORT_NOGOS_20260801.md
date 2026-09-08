# Independent audit of the Boolean owner-layer shadow and SCD funnel theorem

Date: 2026-08-01  
Audited theorem SHA-256:
`5beb6f7ef9ad2bb5a05b85cbe93cdcd100fcebbf654070aa86c95d62f4e0039c`

Verdict: **PASS** for the restricted-shadow cut, Catalan-scale
Kruskal--Katona surplus, four-row SCD perfect matching, sharp
`Cat_(m-1)` funnel capacity, total-order/reset obstructions, explicit
Greene--Kleitman head fibre, ballot-bank Hall cut, and both literal `m=3`
forests.  No finite search is used.

The result is a partial construction plus sharp no-go theorem.  It does not
construct the correlated multi-funnel upper-exact support or place the
tight-pivot predecessor/successor phases in that support.

## 1. Endpoint and Hall rows

For a component with initial root `s_K`, terminal root `o_K`, and incoming
middle label `J_K=M_0(s_K)`, a legal external connector is exactly

\[
                         K\to K'\iff K\ne K'
                         \text{ and }o_K\subset J_{K'}.
\]

The restricted-shadow intersection counts every prospective incoming port.
The correction `e_X` removes exactly those counted only through their own
component's terminal.  Hall deficiency is therefore precisely

\[
 \max_X\bigl(|X|-|\mathcal J\cap\partial^+\mathcal T_X|+e_X\bigr).
\]

The principal-filter inequalities follow immediately.  The coordinate
separation example is correctly scoped to abstract endpoint banks for
`m>=4`; no claim that those banks arise from `Q_0` is made.

## 2. Kruskal--Katona and the owner shell

For `m>=4`, `Cat_m<C(2m-2,m)` forces the leading KK parameter
`s<=2m-3`.  The colex remainder is a family of rank-`(m-1)` sets on at most
`s` points.  Normalized matching downward gives remainder shadow at least
its order, while

\[
 D(s)=\binom{s}{m-1}-\binom{s}{m}
\]

is nondecreasing through `s<=2m-3` and starts at `D(m)=m-1`.  The `m=3`
KK values `3,5,6,6,8` give the same result.  Deleting `m-1` owner labels
therefore leaves Hall for every Catalan-size terminal bank.  Deleting all
`m` supersets of one terminal proves sharpness.

This assigns owner labels only.  It does not make them the free incoming
bank of an upper-exact forest.

## 3. The born-linear SCD funnel

On `G dotunion {a,z}`, the central SCD chains are either
`R<S<L<U` or `S<L`.  The four matching rows exhaust the lower types

\[
                         azR,\ zS,\ aS,\ L
\]

and map bijectively onto the upper types

\[
                         azS,\ zL,\ aL,\ U.
\]

For every short chain, `M_0(zS)=azS` and `M_0(aS)=aL`, so `aS->zS` is a
legal socket with physical endpoints `aL,azS` and upper colour `azL`.
Distinct short chains give disjoint tail, head, physical-owner and upper
banks.  The support is therefore a literal matching and hence born-linear.

There are `D-E=Cat_(m-1)` sockets.  Every lower set `azR` can use only the
`D` middle sets `azS`, consuming `E` of them under any perfect matching.
Thus the same funnel can never exceed `D-E`; the construction is sharp.

## 4. Canonical and serialization obstructions

A forward reservoir on a fixed total order has a size-`C-1` matching only
when every consecutive arc is present.  The height argument then gives the
reset floor `ceil(W/H)-1`.

For standard GK, the displayed `m-1` words have distinct upper colours but
one common off-chain middle endpoint and hence one common contracted head.
The coordinate-sum argument is only a monotone calibration; the separate
positive-density GK pruning theorem is stronger and is not transferred to
arbitrary non-GK funnels.

If both port banks are the canonical ballot family, every connector lowers
coordinate sum.  Since `Cat_m` exceeds the number of sum layers, a level of
multiplicity at least two gives a literal Hall cut of deficiency two.

Finally, both `m=3` examples replay from the frozen arc table.  The first
has two terminal components with no free incoming neighbour.  The second
has matching deficiency exactly one, but every size-four matching contains
the displayed directed two-cycle, so no acyclic Hall subreservoir exists.
At `m=2` the directed three-cycle gives an acyclic completion after choosing
the one upper representative, proving dimension minimality.

## 5. Protected-root scope

The tight-pivot version must jointly choose the predecessor-compatible
`M_0`, a born-linear upper-surjective support containing the successor
path, and a distinguished component `K_*`.  Its first protected root must
remain the free incoming port of `K_*`; then the incoming copy of `K_*` is
deleted and rooted Hall, not unrooted one-defect Hall, is required.

The single SCD funnel and the protected marginal-flow theorems prove
separate rows of this target.  They do not prove their intersection.

