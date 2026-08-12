# Common-root Macaulay runs: exact fibres, shielding, and protected current

**Date:** 2026-08-04  
**Status:** unconditional pure-mathematical theorem.  It proves that every
constant-aperture run in a canonical Macaulay expansion is a common-root
union of principal stars.  Such a run is exactly one principal star with a
two-sided Boolean interval removed.  Its owner fibres, scalar Ore slack,
and protected loss collapse to one root current plus one unique-coordinate
boundary current.  This gives a width-linear, rather than exponential,
protected bound for the run.  It does not yet prove that every broad run is
safe.

No computation, search, or solver result is used.

## 0. Macaulay notation

Retain the canonical expansion and notation of
`MATH_THEOREM_MACAULAY_INTERVAL_DNF_EROSION_AND_TRIANGULAR_CROSSING_20260804.md`:

\[
 c_m>c_{m-1}>\cdots>c_s,
 \qquad
 \rho_j=c_j-j+1,
 \qquad
 p_j=c_j+1,
\]

and

\[
 C_j=[n]\setminus(Q_j\cup[c_j]),
 \qquad Q_j=\{p_{j+1},\ldots,p_m\}.
\]

The lower colex complement is the principal-star DNF

\[
 A=\bigcup_j\mathcal A_{C_j}.
\]

## 1. Saturated runs are common-root star unions

Except for the trivial full-shore endpoint discussed below, fix consecutive indices

\[
 a\le j\le b
\]

on which

\[
 \rho_j=\rho
\tag{1.1}
\]

is constant.  Then

\[
 c_j=j+\rho-1,
 \qquad p_j=j+\rho.
\tag{1.2}
\]

Put

\[
 R=[n]\setminus(Q_b\cup[\rho+b]),
 \qquad
 X=\{p_a,p_{a+1},\ldots,p_b\},
 \qquad h=|X|=b-a+1.
\tag{1.3}
\]

Here and below the nontrivial run hypothesis is

\[
 c_b<n,
 \qquad\text{equivalently}\qquad
 p_b=\rho+b\in[n].
\tag{1.3a}
\]

The only canonical term excluded by this hypothesis is the isolated top
term `b=a=m`, `c_m=n`, whose colex segment is the complete `m`-shore and
whose complement is the complete lower shore.  That endpoint is already
safe with zero Ore slack and zero protected loss.  Its formal pivot
`p_m=n+1` is not a ground-set coordinate, so it must not be included in
the common-root representation below.

### Theorem 1.1 (common-root run identity)

For every `a<=j<=b`,

\[
 \boxed{C_j=R\cup\{p_j\}.}
\tag{1.4}
\]

Consequently the DNF carried by the run is

\[
 \boxed{
 \mathcal D(R,X)
 :=\bigcup_{j=a}^b\mathcal A_{C_j}
 =\{L\in\mathcal L:R\subseteq L,\ L\cap X\ne\varnothing\}.}
\tag{1.5}
\]

It also has the exact shielding representation

\[
 \boxed{
 \mathcal D(R,X)
 =\mathcal A_R\setminus
   \mathcal A(R,[n]\setminus X),}
\tag{1.6}
\]

where

\[
 \mathcal A_R=\{L:R\subseteq L\},
 \qquad
 \mathcal A(R,[n]\setminus X)
 =\{L:R\subseteq L\subseteq[n]\setminus X\}.
\]

#### Proof

On the run, the pivots are the consecutive coordinates
`rho+a,...,rho+b`.  Hence

\[
 Q_j=Q_b\cup\{\rho+j+1,\ldots,\rho+b\}.
\]

The set excluded in the definition of `C_j` is therefore

\[
 Q_b\cup[\rho+j-1]\cup
 \{\rho+j+1,\ldots,\rho+b\}.
\]

Inside `[rho+b]` its unique missing point is `rho+j=p_j`; outside that
interval its complement is the fixed set `R`.  This proves (1.4).
Taking the union of the corresponding clauses gives (1.5).  Finally,
among the lower sets containing `R`, the only ones omitted by (1.5) are
those lying in `[n]\setminus X`, which proves (1.6). \(\square\)

Thus strict increases of `rho_j` are the only places where the common root
can change.  A long saturated broad run is not an arbitrary large DNF: it
is one common-root hit condition.

## 2. Exact owner fibres and scalar slack

Assume

\[
 |R|=m-\rho-1,
\tag{2.1}
\]

as follows from (1.3), and put

\[
 N=|[n]\setminus R|=m+\rho.
\]

For an owner `U`, write

\[
 q_U=|U\cap X|.
\]

### Theorem 2.1 (two-level owner fibres)

An owner meets `D(R,X)` exactly when `R subset U` and `q_U>=1`.  Its
selected-facet multiplicity is

\[
 \boxed{
 a_U=
 \begin{cases}
  \rho,&q_U=1,\\
  \rho+1,&q_U\ge2.
 \end{cases}}
\tag{2.2}
\]

When `rho>=2`, every nonzero fibre is therefore two-covered, and

\[
 \boxed{
 |\mathcal D(R,X)|
 =\binom N\rho-\binom{N-h}\rho,}
\tag{2.3}
\]

\[
 \boxed{
 |N(\mathcal D(R,X))|
 =\binom N{\rho+1}-\binom{N-h}{\rho+1},}
\tag{2.4}
\]

and

\[
 \boxed{
 {\sigma(\mathcal D(R,X))\over2}
 =\binom N{\rho+1}-\binom{N-h}{\rho+1}
  -\binom N\rho+\binom{N-h}\rho.}
\tag{2.5}
\]

Equivalently,

\[
 \boxed{
 {\sigma(\mathcal D(R,X))\over2}
 =\sum_{t=0}^{h-1}
 {m-\rho-t\over\rho}
 \binom{m+\rho-t-1}{\rho-1}.}
\tag{2.6}
\]

The summands in (2.6) need not all be positive; (2.5) is the primary
nonnegative form.

#### Proof

At an owner containing `R`, every active clause has the form `R+x` with
`x in U cap X`.  If there is one such coordinate, the intersection of the
active cores is `R+x`, and the fibre size is

\[
 m-|R+x|=\rho.
\]

If there are at least two, the active-core intersection is `R`, and the
fibre size is `m-|R|=rho+1`.  This proves (2.2).

A lower set containing `R` chooses `rho` coordinates from the `N` outside
coordinates; it belongs to the DNF exactly when at least one choice lies
in `X`.  This gives (2.3).  Owners choose `rho+1` outside coordinates,
giving (2.4).  When `rho>=2`, all active fibres contribute two to the
truncated shadow, so (2.5) follows.

Apply Pascal telescoping separately to the two binomial differences in
(2.5).  At step `t` the difference is

\[
 \binom{m+\rho-t-1}{\rho}
 -\binom{m+\rho-t-1}{\rho-1}
 ={m-\rho-t\over\rho}
  \binom{m+\rho-t-1}{\rho-1},
\]

which proves (2.6). \(\square\)

## 3. Exact protected-current collapse

Assume `rho>=2`.  For a protected incidence `UL`, write
`del(U,L)` for the unique coordinate in `U-L`.  Define

\[
 \xi_P(R,X)
 =|\{UL\in E(P):R\subseteq U,\ U\cap X\ne\varnothing,
                   \operatorname{del}(U,L)\in R\}|,
\tag{3.1}
\]

and

\[
 \eta_P(R,X)
 =|\{UL\in E(P):R\subseteq U,\ U\cap X=\{x\},
                   \operatorname{del}(U,L)=x\}|.
\tag{3.2}
\]

### Theorem 3.1 (root current plus unique-hit current)

For every protected bank of maximum degree at most two,

\[
 \boxed{
 \lambda_P(\mathcal D(R,X))
 =\xi_P(R,X)+\eta_P(R,X).}
\tag{3.3}
\]

#### Proof

All active fibres have size at least two, so local protected loss is the
number of protected incidences to unselected facets.  At an owner with
`U cap X={x}`, the selected deletions are `U-(R+x)`; the unselected
deletions are exactly `R+x`.  At an owner containing at least two points
of `X`, the active-core intersection is `R`, so the unselected deletions
are exactly `R`.  These are precisely the two disjoint currents in
(3.1)--(3.2). \(\square\)

Now suppose `P` is a union of simple owner paths on which every coordinate
has one interval of owner occurrences.  Let `mathscr P(R)` be the protected
paths containing an owner above `R`.

### Corollary 3.2 (width-linear path bound)

One has

\[
 \boxed{
 \xi_P(R,X)\le2|\mathscr P(R)|,
 \qquad
 \eta_P(R,X)\le2h|\mathscr P(R)|.}
\tag{3.4}
\]

Hence

\[
 \boxed{
 \lambda_P(\mathcal D(R,X))
 \le2(h+1)|\mathscr P(R)|.}
\tag{3.5}
\]

There is also the clause-wise principal-current bound

\[
 \boxed{
 \lambda_P(\mathcal D(R,X))
 \le\sum_{x\in X}\lambda_P(\mathcal A_{R\cup\{x\}}).}
\tag{3.6}
\]

For the common-core constant-spread reservoir, the frozen trace counts give

\[
 |\mathscr P(R)|\le
 N_{\rho+1}:=H_{\rho+1}(m)+m+H_d,
\tag{3.7}
\]

and

\[
 \lambda_P(\mathcal A_{R\cup\{x\}})\le
 2N_\rho,
 \qquad N_\rho:=H_\rho(m)+m+H_d.
\tag{3.8}
\]

Therefore

\[
 \boxed{
 \lambda_P(\mathcal D(R,X))
 \le2\min\{hN_\rho,(h+1)N_{\rho+1}\}.}
\tag{3.9}
\]

#### Proof

On one protected path, the owners containing all of `R` form an interval.
A protected incidence deleting a root coordinate can occur only at one of
its two boundary edges, proving the first inequality.

For a fixed `x in X`, its owner occurrences on the path form an interval.
An incidence counted by `eta` and deleting `x` can occur only at one of the
two boundary incidences of that coordinate interval.  Summing over the `h`
coordinates proves the second inequality.  For (3.6), every union-loss
incidence deletes either the common root or, at a unique-hit owner, the one
active coordinate.  It is therefore counted by the loss of at least one
active clause.  Sum the frozen principal-current bounds to obtain
(3.8)--(3.9). \(\square\)

The bound is deliberately occurrence-level.  It does not sum the currents
of all `h` clauses independently at every owner; root exits are paid once,
and only the unique-hit coordinate boundary remains width-dependent.

### Corollary 3.3 (direct safe-run criterion)

For the constant-spread reservoir, a saturated run with `rho>=2` is safe
whenever

\[
 \boxed{
 \binom N{\rho+1}-\binom{N-h}{\rho+1}
 -\binom N\rho+\binom{N-h}\rho
 \ge\min\{hN_\rho,(h+1)N_{\rho+1}\}.}
\tag{3.10}
\]

This is a single explicit binomial inequality, with no inclusion--exclusion
over the `h` clauses.

## 4. Uniform closure of the localized broad runs

### Theorem 4.1 (uniform common-root broad-run closure)

For the constant-spread reservoir and all sufficiently large `m`, every
common-root run satisfying

\[
 \boxed{2\le\rho\le {m\over2},
        \qquad h\le\rho}
\tag{4.1}
\]

passes protected Ore.

#### Proof

Every active owner fibre has size at most `rho+1`.  Regularity therefore
gives

\[
 m|\mathcal D(R,X)|
 \le(\rho+1)|N(\mathcal D(R,X))|,
\]

and hence

\[
 \sigma(\mathcal D(R,X))
 \ge {2(m-\rho-1)\over\rho+1}|\mathcal D(R,X)|.
\tag{4.2}
\]

First suppose `rho<=m/10`.  For all sufficiently large `m`, the coefficient
in (4.2) is at least sixteen.  If `h=1`, the family is one principal star
and is already safe.  If `h>=2`, then its size exceeds `2m`: at `rho=2`,
two distinct clauses have union size `2(m+1)-1=2m+1`; at `rho>=3`, one
clause already has size

\[
 \binom{m+\rho-1}{\rho-1}\ge\binom{m+2}2>2m.
\]

The frozen all-cut estimate now gives

\[
 \lambda_P(\mathcal D(R,X))
 \le15|\mathcal D(R,X)|+2m
 \le16|\mathcal D(R,X)|
 \le\sigma(\mathcal D(R,X)).
\]

Now assume `m/10<=rho<=m/2`.  Since `h<=rho`, every summand in (2.6) is
nonnegative.  Keeping only the first gives

\[
 {\sigma(\mathcal D(R,X))\over2}
 \ge D_0:={m-\rho\over\rho}
          \binom{m+\rho-1}{\rho-1}.
\tag{4.3}
\]

Write `alpha=rho/m`.  Uniformly for `alpha in [1/10,1/2]`, Stirling's
formula gives

\[
 \log_2D_0
 =m\bigl((1+\alpha)\log_2(1+\alpha)
          -\alpha\log_2\alpha\bigr)+O(\log m),
\]

whereas

\[
 \log_2N_\rho\le mH_2(\alpha)+o(m).
\]

The exponent difference is

\[
 (1+\alpha)\log_2(1+\alpha)
 +(1-\alpha)\log_2(1-\alpha),
\tag{4.4}
\]

which has a positive minimum on `[1/10,1/2]`.  Thus

\[
 D_0>mN_\rho\ge hN_\rho
\]

for all sufficiently large `m`.  Corollary 3.3 proves the result.
\(\square\)

### Corollary 4.2 (every localized intrinsic broad run passes)

Suppose the whole initial colex segment lies in the small-side localization

\[
 |F|=O(m^2 2^m).
\tag{4.5}
\]

Then, for all sufficiently large `m`, every constant-`rho` run whose
indices satisfy `j<=rho` is safe.

#### Proof

At the top Macaulay term,

\[
 c_m=m+\rho_m-1,
 \qquad
 |F|\ge\binom{m+\rho_m-1}m.
\]

If `rho_m>=m/2`, Stirling's formula gives exponential rate at least

\[
 {3\over2}H_2(1/3)>1,
\]

contradicting (4.5).  Hence `rho<=rho_m<m/2` on every run.  A run whose
indices obey `j<=rho` has width `h<=rho`.  Apply Theorem 4.1 when
`rho>=2`; at `rho=1`, the condition leaves only the rank-one terminal
singleton clause, which is safe by the frozen singleton margin.
\(\square\)

Thus the blocks with intrinsically nonpositive margin credit in the
Macaulay block reduction are no longer individually open: they close in
their maximal constant-aperture runs.  What remains is their interaction
across strict aperture jumps.

## 5. Exact frontier

The theorem gives the requested reformulation of the broad-term geometry:

* strict increases of `rho_j` change the common root;
* constant-`rho` runs are common-root star unions;
* each such run is a principal star shielded by one two-sided interval;
* its protected loss is one root current plus one unique-hit current; and
* the direct safety test is (3.10), linear in the run width; and
* every localized run in the intrinsic broad regime `j<=rho` satisfies
  that test by Theorem 4.1.

Outside the localized broad regime, the theorem does not show that (3.10)
holds uniformly for every admissible `rho,h`.  More importantly, it does
not control gluing between different constant-`rho` runs.  Strict aperture
jumps are now the exact residual part of the localized broad-Macaulay
problem.

The case `rho=1` is excluded from the two-covered current formula; there
the clauses are rank-`m-1` singleton stars and are governed by the frozen
singleton margin instead.

## 6. Dependencies

| role | file | SHA-256 |
|---|---|---|
| Macaulay interval/DNF decomposition and triangular current | `MATH_THEOREM_MACAULAY_INTERVAL_DNF_EROSION_AND_TRIANGULAR_CROSSING_20260804.md` | `77253694d02d6d11c41a21b9875af843ede525d1751bca7d2463ac014b174cec` |
| all two-sided shielding intervals pass | `MATH_THEOREM_CONSTANT_SPREAD_ALL_TWO_SIDED_SUBCUBES_ORE_COMPLETE_20260804.md` | `c1bcfa900291760974c167c2c02248c65291d28beaf3ef8e66c095a2301f4817` |
| common-root path count and constant-spread reservoir | `MATH_THEOREM_PROTECTED_ORE_TWO_SIDED_SUBCUBE_EXACT_REDUCTION_20260804.md` | `6499abf7abf9536bdfcf421206ad1e56d3b3f9d2ce05258b92cb8873ddb26dd7` |
| all-cut constant-spread estimate and localization | `MATH_THEOREM_COMMON_CORE_RANDOM_TRACE_SPREAD_AND_LOW_EXPANSION_ORE_LOCALIZATION_20260804.md` | `d6875ab5e876aa3f1805ec387065be2b2bd1e07b5e3b27dbc120dff3e027eb65` |
