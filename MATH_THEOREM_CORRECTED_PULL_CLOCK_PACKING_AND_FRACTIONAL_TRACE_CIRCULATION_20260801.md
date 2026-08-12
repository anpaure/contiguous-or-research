# Corrected pull-clock packing and the fractional trace-circulation gate

**Date:** 2026-08-01  
**Status:** unconditional fractional theorem.  The two ratio comparisons in
the first draft had their directions reversed.  This note gives the corrected
proof and an independent finite audit.  It proves the stationary marked-trace
membership required by the optimal triangular fractional factor.  It does
**not** round that circulation to one copy of every named owner, connect it
into one Euler chronology, or prove an upper bound for `nu(k)`.

## 0. Result

Put

\[
 r=\lceil k/2\rceil,\qquad W=\binom kr,
 \qquad \Lambda=\sum_{s=1}^{r-1}\binom ks,
\]

and

\[
 d=\min\left\{t:tW+\binom{t+1}{2}\ge\Lambda\right\}.
\]

Choose the triangular boundary multiplicities

\[
 b_1\ge b_2\ge\cdots\ge b_d\ge0,
 \qquad \sum_s b_s=(\Lambda-dW)_+,
\]

by filling the Ferrers columns of heights `d,d-1,...,1` from left to
right, and put `b_s=0` for `s>d`.  Define

\[
 q_s={\binom ks-b_s\over W},\qquad 1\le s<r.       \tag{0.1}
\]

Because the binomial coefficients increase up to rank `r` while the
chosen `b_s` are nonincreasing, `0<=q_1<=...<=q_(r-1)<=1`.

### Theorem 0.1 (stationary pull clock)

There is a rational stationary circulation on literal depth-`d` traces
whose length-`(d+1)` union is a rank-`r` owner, and whose marked proper
suffixes have rank marginal exactly `(q_1,...,q_{r-1})`.  Averaging over
owners and their stabilizers gives every named rank-`s` target load

\[
 1-{b_s\over\binom ks}.                                  \tag{0.2}
\]

The literal Ferrers boundary contributes the complementary load.  Hence
the optimal triangular fractional chain factor satisfies the stationary
literal trace constraint.

The theorem is fractional.  Its integral one-copy/Euler rounding remains
open.

## 1. Pull blocks

Set

\[
 c=r-d-1.
\]

When `c<=0`, the all-high clock already dominates the residual profile, so
assume `c>0`.  Split a fixed owner as

\[
 T=C\mathbin{\dot\cup}F,\qquad |C|=c,\quad |F|=d+1.
\]

At a high position put all of `C` together with the current private clock
letter.  A pull block of type `(delta,j)` consists of `j` consecutive
positions omitting a fixed `delta`-subset of `C`, followed by a high
separator, where

\[
 1\le\delta\le c,\qquad 1\le j\le d.
\]

Relative to the all-high clock, one such block has low-rank row marginal

\[
 L_{\delta,j}(t)=
 \begin{cases}
 j-\delta+t,&1\le t\le\delta,\ j-\delta+t\ge1,\\
 0,&\text{otherwise},
 \end{cases}                                                \tag{1.1}
\]

where row `t` means rank `c-t+1`.  Its net deficit at high rank `c+q` is

\[
 R_{\delta,j}(q)=\min\{\delta,j-q+1\}_+.                    \tag{1.2}
\]

Both are the row and column sums of the staircase

\[
 S_{\delta,j}=\{(t,q):1\le t\le\delta,
                         1\le q\le j-\delta+t\}.             \tag{1.3}
\]

The `min(delta,...)` in (1.2) is important: a long low window shifted down
by `delta` may land at another high-band rank, so (1.2) is a *net* deficit.

## 2. Product demand and staircase coefficients

Reverse the low demands and record the high capacities:

\[
 A_t=q_{c-t+1}\quad(1\le t\le c),\qquad
 P=\sum_{t=1}^c A_t,                                        \tag{2.1}
\]

\[
 G_j=1-q_{c+j}\quad(1\le j\le d),\qquad
 H=\sum_{j=1}^dG_j.                                         \tag{2.2}
\]

Since `sum_s q_s<=d`,

\[
 H-P=d-\sum_{s<r}q_s\ge0.                                  \tag{2.3}
\]

If `H=0`, then `P=0` and there is nothing to pull.  Otherwise put

\[
 w_j={G_j\over H},\quad w_{d+1}=w_{d+2}=0,
 \qquad \Delta_j=w_j-w_{j+1}.                              \tag{2.4}
\]

The matrix

\[
 M_{tq}=A_tw_q                                             \tag{2.5}
\]

has row sums `A_t` and column sums `Pw_q<=G_q`.  Define

\[
 x_{\delta,j}=A_\delta\Delta_j-A_{\delta+1}\Delta_{j+1},
 \qquad A_{c+1}=0.                                         \tag{2.6}
\]

For a cell `(t,q)`, summing all staircases containing it gives

\[
 \begin{aligned}
 \sum_{\delta=t}^c\sum_{j=q+\delta-t}^d x_{\delta,j}
 &=\sum_{\delta=t}^c
   \left(A_\delta w_{q+\delta-t}
         -A_{\delta+1}w_{q+\delta-t+1}\right)\\
 &=A_tw_q.
 \end{aligned}                                             \tag{2.7}
\]

Thus nonnegativity of the `x` gives an exact staircase decomposition of
the product coupling.

## 3. Corrected nonnegativity proof

Assume first `c>d`; then the Ferrers correction lies wholly below the high
band.  Put

\[
 p_s={\binom ks\over W},\qquad
 \rho={k-c+1\over c}>1.                                    \tag{3.1}
\]

The original draft wrote the next two inequalities in the opposite
directions.  The correct comparisons are

\[
 {A_\delta\over A_{\delta+1}}\ge\rho                 \tag{3.2}
\]

when `A_{delta+1}>0`, and

\[
 {\Delta_{j+1}\over\Delta_j}\le\rho                 \tag{3.3}
\]

when `Delta_j>0`.

For (3.2), the uncorrected adjacent ratio

\[
 {p_s\over p_{s-1}}={k-s+1\over s}
\]

is decreasing in `s`, so it is at least `rho` for `s<=c`.  Moreover the
left-filled Ferrers multiplicities satisfy `b_s<=b_{s-1}`.  Since the
uncorrected ratio is greater than one, subtracting `b_s` from the numerator
and the at-least-as-large `b_{s-1}` from the denominator can only increase
the ratio.  This proves (3.2).

For (3.3), write

\[
 D_s=p_{s+1}-p_s
     =p_s{k-2s-1\over s+1}.                                \tag{3.4}
\]

In the uncorrected high band `Delta_j=D_{c+j}/H`.  Whenever the numerator
is positive,

\[
 {D_{s+1}\over D_s}
 ={(k-s)(k-2s-3)\over(s+2)(k-2s-1)}
 <{k-s\over s+1}.                                           \tag{3.5}
\]

The last ratio decreases with `s`; for `s>=c+1` it is strictly below
`rho`.  A zero numerator is automatic.  Hence (3.3).

Equations (3.2)--(3.3) give

\[
 A_\delta\Delta_j\ge A_{\delta+1}\Delta_{j+1},
\]

so every coefficient (2.6) is nonnegative.

## 4. Corrected packing-cost proof

The normalized number of physical clock positions consumed by the pull
blocks and their separators is

\[
 \mathcal C=\sum_{\delta=1}^c\sum_{j=1}^d(j+1)x_{\delta,j}.  \tag{4.1}
\]

Two summations by parts give

\[
 \mathcal C=A_1+Pw_1+(P-A_1)(w_1-w_2).                      \tag{4.2}
\]

Here `A_1=p_c`; write

\[
 \alpha=p_c,\qquad\beta=p_{c+1},\qquad\gamma=p_{c+2},
 \qquad \theta={c\over k-c+1}={1\over\rho}.                \tag{4.3}
\]

Again, the first draft interchanged `rho` and `theta`.  From (3.2),

\[
 A_{t+1}\le\theta A_t.
\]

Therefore

\[
 {P-\alpha\over H}\le {P-\alpha\over P}\le\theta.       \tag{4.4}
\]

Equation (3.5), now at `s=c`, gives

\[
 {\gamma-\beta\over\beta-\alpha}\le\rho={1\over\theta},  \tag{4.5}
\]

and hence

\[
 {P-\alpha\over H}(\gamma-\beta)\le\beta-\alpha.          \tag{4.6}
\]

Since `Pw_1<=G_1=1-beta` and
`w_1-w_2=(gamma-beta)/H`, substituting (4.6) into (4.2) yields

\[
 \mathcal C
 \le\alpha+(1-\beta)+(\beta-\alpha)=1.                   \tag{4.7}
\]

Thus all pull blocks fit on one stationary timeline.

## 5. Literal realization

Clear denominators with an integer `N` divisible by `d+1`.  Place
`Nx_{delta,j}` blocks of type `(delta,j)` on a cyclic timeline of length
`N`, each followed by its high separator; fill unused positions with high
positions.  At time `t`, use private letter `f_(t mod d+1)`.

Every low run has length at most `d`, so every `d+1` consecutive positions
contain a high position.  They also contain all `d+1` private letters.
Therefore every length-`(d+1)` union is exactly `T=C union F`.

A proper window wholly contained in a type-`(delta,j)` block has rank
`c-delta+q`; every other proper `q`-window contains a high position and
has rank `c+q`.  Sections 1--4 therefore give a literal stationary rank
profile `v` satisfying

\[
 v_s=q_s\quad(s\le c),\qquad v_s\ge q_s\quad(c<s<r).         \tag{5.1}
\]

Average over cyclic shifts, owners, private sets, private orders, and
omitted core subsets.  The owner stabilizer is transitive on each rank, so
every rank-`s` subset of a fixed owner receives equal mass.  Thin marked
occurrences at rank `s` by the factor `q_s/v_s`.  Any subset of the proper
suffixes of one trace is still nested, so this thinning is a legitimate
convex combination of marked trace states.

A named rank-`s` target belongs to `binom(k-s,r-s)` owners.  Its resulting
load is

\[
 \binom{k-s}{r-s}{q_s\over\binom rs}
 ={Wq_s\over\binom ks}
 =1-{b_s\over\binom ks},                                    \tag{5.2}
\]

which proves Theorem 0.1 after adding the Ferrers boundary bank.

## 6. Range reduction and exact finite cases

The standard central-binomial/Wallis estimate gives

\[
 {\Lambda\over W}\le\sqrt r,
 \qquad d\le\lceil\sqrt r\rceil.                            \tag{6.1}
\]

For completeness: in even dimension use
`binom(2m,m)>=4^m/(2 sqrt(m))`; in odd dimension multiply that bound by
`(2m+1)/(m+1)`.  The displayed inequality follows directly in both
parities.

For `r>=8`, (6.1) implies `r>=2d+2`, hence `c=r-d-1>d`.  Thus Sections
3--5 cover every `k>=15`.  For `k<=5`, `c<=0`.  The remaining exact
arithmetic is:

| `k` | `r` | `d` | `c` | pull cost |
|---:|---:|---:|---:|---:|
| 6 | 3 | 1 | 1 | `1/2` |
| 7 | 4 | 2 | 1 | `2/5` |
| 8 | 4 | 2 | 1 | `1/5` |
| 9 | 5 | 2 | 2 | `2/3` |
| 10 | 5 | 2 | 2 | `2665/7308` |
| 11 | 6 | 3 | 2 | `62/273` |
| 12 | 6 | 2 | 3 | `9/17` |
| 13 | 7 | 3 | 3 | `41/120` |
| 14 | 7 | 2 | 4 | `2583/3718` |

All staircase coefficients are nonnegative in these cases.  The exact
small-case audit is

* source: `scratch/audit_pull_clock_small_exact_20260801.cpp`, SHA-256
  `0774cb81f001da86fe840564e7b440958e804311e8487d8a52c3ba20beeb225b`;
* output: `scratch/pull_clock_small_exact_20260801.log`, SHA-256
  `d84599698d77ccf00658141b2598089283d1671ed087ceaf4ee4ed9a06b734fe`.

An independent long-double stress audit checked every `2<=k<=2000`, the
staircase row identities, every high-capacity inequality, coefficient
nonnegativity, and pull cost at most one:

* source: `scratch/audit_pull_clock_packing_20260801.cpp`, SHA-256
  `3993c3c3e2168425a83bc43c587df02f3c895f6c178a45e2aa0121f4fea30f65`;
* output: `scratch/pull_clock_audit_k2000_20260801.log`, SHA-256
  `2bd7af62b50ae8e98cb222c0707b842eafe38a4c365ac05fe4298eb06782016d`.

The stress audit is corroboration, not a substitute for Sections 3--6.

An independent audit repaired the same ratio chains, supplied a standalone
exact-bigint verifier through `k=2000`, and checked the literal staircase
interpretation.  It also records the sharp scope boundary: the pull-block
polytope is not integral, and a fixed-owner block repeats that owner rather
than furnishing one one-copy atom.  See
`MATH_AUDIT_PULL_CLOCK_RATIO_REPAIR_AND_ONE_COPY_GATE_20260801.md`, SHA-256
`2e7e6e378fc9b636966485f0b2727547f6044061e42e736e7e371deb699194dc`,
and `scratch/audit_pull_clock_exact_cppint_20260801.cpp`, SHA-256
`1359a3a12edae4d8886b0abf2af2e205ed0432d8804071b3a86b446546f178dc`.

## 7. Exact remaining gate

The following rows are now distinct:

| row | status |
|---|---|
| optimal rank marginals | exact |
| stationary literal trace circulation | exact by Theorem 0.1 |
| unrestricted/protected high-target chain selector | exact by the SCD selector theorem |
| common integral choice satisfying both systems | open |
| statewise legal successor Hall | open |
| one-copy owner-rainbow Euler component | open |
| residence, complete upper deck, terminal compiler | open |

For a flag rail `z_1,...,z_(d-1)`, a legal successor must have rail
`z_2,...,z_(d-1),gamma`, with `gamma` in the old bottom set, while the
owner turns by `q=p-z_1+beta`.  Hence flags split into overlap states `w`;
the next exact theorem is a common integral rounding of the pull-clock and
protected SCD factor inside all statewise Hall equations, followed by one
owner-rainbow connected Euler choice.

The theorem proved here removes every *fractional* separator at this gate.
It does not remove that correlated integral obstruction.
