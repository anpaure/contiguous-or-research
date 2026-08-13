# Period-`2q+1` distributed cores: exact two-schedule programmability and the fractional portal gate

**Date:** 2026-08-13  
**Method:** explicit three-hit cyclic schedules, orbit counting, and exact
incidence averaging.  Numerical evaluations were run only on `h100`.  
**Status:** unconditional local programmability theorem and exact
fractional/ILP reduction.  It does **not** assert that one schedule choice
per rail realizes all lower targets simultaneously.

## 1. The period and minimum schedules

Fix

\[
                         N=2q+1,qquad q\ge2,                        \tag{1.1}
\]

and work in `Z_N`.  Let `H_(N,q)` be the hitting sets which meet every
cyclic interval of `q` consecutive positions.  Every such set has size at
least

\[
                         \left\lceil{N\over q}\right\rceil=3.       \tag{1.2}
\]

A three-set belongs to `H_(N,q)` if and only if its three positive cyclic
gaps are each at most `q`.  Hence the minimum schedules are parametrized by

\[
                         g_1+g_2+g_3=2q+1,qquad1\le g_j\le q.       \tag{1.3}
\]

Equivalently, writing `g_j=q-u_j`,

\[
                         u_1+u_2+u_3=q-1,qquad u_j\ge0.             \tag{1.4}
\]

Their number as unpointed subsets of `Z_N` is

\[
 |\mathcal M_q|
 ={N\over3}{q+1\choose2}.                                          \tag{1.5}
\]

Indeed, there are `binom(q+1,2)` ordered triples `(u_1,u_2,u_3)` and `N`
choices of a pointed first hit; every unpointed three-set has three
pointings.

## 2. Two schedules which program one interval

For every `a in Z_N`, define

\[
                         E_a=\{a-1,a,a+q\}.                          \tag{2.1}
\]

Its cyclic gaps in the displayed order are

\[
                         1,q,q,                                    \tag{2.2}
\]

so `E_a in M_q`.

Let

\[
                         J= [i,i+\ell-1]\subset\mathbb Z_N,
                         \qquad1\le\ell<q,                          \tag{2.3}
\]

be a nonwrapping notation for a cyclic interval after rotating the origin.
Put

\[
                         E^+(J)=E_i,qquad E^-(J)=E_{i-1}.           \tag{2.4}
\]

### Theorem 2.1 (exact single-cell programmability)

Let `(F,sigma)` be a pure owner rail of period `N=2q+1`, with distinct
toggle order `sigma=(x_t)` and core `F`.  Fix `J=[i,i+ell-1]` as in (2.3)
and an arbitrary subset `H subseteq F`.  Assign the emission schedule

\[
 E_f=
 \begin{cases}
  E^+(J),&f\in H,\\
  E^-(J),&f\in F\setminus H.
 \end{cases}                                                        \tag{2.5}
\]

Then every `E_f` is a minimum legal hitting schedule, every length-`q`
owner and every longer proper row is unchanged, and the marked strict-
lower interval has value exactly

\[
                         A[i,\ell]=H\cup I_i^\ell(\sigma).           \tag{2.6}
\]

In particular, for this fixed interval, every subset of the core is
independently programmable.

#### Proof

After rotating so `i=0`,

\[
 E^+(J)=\{-1,0,q\},qquad
 E^-(J)=\{-2,-1,q-1\}.                                              \tag{2.7}
\]

Because `1<=ell<q`, the first set meets `J=[0,ell-1]` exactly at `0`,
while the second is disjoint from `J`.  Thus the union of emitted core
coordinates across `J` is precisely `H`.  The toggle contribution is
`I_i^ell(sigma)`, proving (2.6).  Equation (2.2) shows every chosen
schedule is legal and minimum.  The distributed-core formula then
preserves every row of width at least `q`.  \(\square\)

### Corollary 2.2 (local rank span)

If `|F|=c=R-q`, then, at every fixed strict width `ell`, (2.6) realizes
every rank

\[
                         \ell,\ell+1,\ldots,\ell+c.                  \tag{2.8}
\]

As `ell` runs from `1` to `q-1`, these ranges cover every rank from `1`
through `R-1` when `c>=1`.

This is a one-cell statement.  The same core coordinate has only one
global schedule on the rail, so arbitrary choices for two different
intervals may conflict.

## 3. Exact minimum-schedule orbit marginal

Let a minimum schedule `E` be uniform on `M_q`, and fix an `ell`-interval
`J`, `1<=ell<q`.  Put

\[
                         p_{q,\ell}=\Pr(E\cap J\ne\varnothing).       \tag{3.1}
\]

### Lemma 3.1 (closed hitting probability)

With `t=q-ell`,

\[
 |\{E\in\mathcal M_q:E\cap J=\varnothing\}|
 =\ell{t(t+1)\over2}+{t(t+1)(2t+1)\over6},                         \tag{3.2}
\]

and hence

\[
 \boxed{
 p_{q,\ell}=1-
 {\ell t(t+1)/2+t(t+1)(2t+1)/6
  \over (2q+1)\binom{q+1}{2}/3}.}                                  \tag{3.3}
\]

#### Proof

If `E` avoids `J`, all three points lie in the complementary path of
length

\[
                         L=N-\ell.                                  \tag{3.4}
\]

Write them as `0<=a<b<c<L` in path coordinates.  The two internal cyclic
gaps and the exterior gap must be at most `q`, so

\[
 b-a\le q,qquad c-b\le q,qquad N-c+a\le q.                        \tag{3.5}
\]

Put `x=b-a`, `y=c-b`, and `z=a+L-1-c`, the unused path positions before
and after the selected triple.  The last inequality is
`z<=q-ell-1=t-1`,
while `x,y<=q`, `x,y>=1`, and

\[
                         x+y+z=L-1=2q-\ell.                          \tag{3.6}
\]

For fixed `z`, the allowed `x` range has size `ell+z+1`; there are `z+1`
choices for `a` and the final unused suffix with total `z`.  Summing
`(z+1)(ell+z+1)` for `z=0,...,t-1` gives (3.2).  Divide by (1.5).
\(\square\)

For `ell=1`, formula (3.3) simplifies to

\[
                         p_{q,1}={3\over2q+1},                       \tag{3.7}
\]

as required by incidence double counting.

## 4. Exact portal count in a fixed rail

Fix a pure rail `(F,sigma)` with `|F|=c`, and fix a target `S` of rank
`s<R`.  A portal is a triple

\[
                         p=(i,\ell,(E_f)_{f\in F})                   \tag{4.1}
\]

with `1<=ell<q`, every `E_f in M_q`, and

\[
 (\bigcup_{t=0}^{\ell-1}G_{i+t})
       \cup I_i^\ell(\sigma)=S.                                    \tag{4.2}
\]

### Lemma 4.1 (fixed-rail portal formula)

The portal set is empty unless, for some `(i,ell)`,

\[
 I_i^\ell(\sigma)\subseteq S\subseteq
                         F\cup I_i^\ell(\sigma).                    \tag{4.3}
\]

For such an occurrence put

\[
 H=S\setminus I_i^\ell(\sigma),qquad h=|H|=s-\ell.                \tag{4.4}
\]

Then the number of minimum-schedule decorations realizing `S` on that
occurrence is exactly

\[
 D_{q,\ell}(h)
 =M_{q,\ell}^{h}
   (|\mathcal M_q|-M_{q,\ell})^{c-h},                               \tag{4.5}
\]

where

\[
 M_{q,\ell}=p_{q,\ell}|\mathcal M_q|.                              \tag{4.6}
\]

#### Proof

Condition (4.3) is forced because toggle letters occur only on the fixed
toggle interval and the remaining value must lie in the core.  Given it,
each core coordinate in `H` must choose one of the `M_(q,ell)` schedules
meeting `J`, while every coordinate in `F\H` must choose a schedule
avoiding `J`.  Coordinate schedules are independent in the antecedent
state space, giving (4.5).  \(\square\)

Theorem 2.1 is the nonvanishing certificate for every formula (4.5): both
factors are positive for `ell<q`.

## 5. Symmetric decorated-rail fractional coverage

Let `mathcal R` be any owner factor by period-`N` pure rails, and let
`G=S_k` act by coordinate conjugation.  Independently decorate every core
coordinate of every rail by a uniform member of `M_q`.  Average this
random decorated factor over `G`.

For a fixed target rank `s`, every named `s`-set has the same fractional
load.  If `P_s` is the total number of strict-lower portal occurrences of
rank `s` in one decorated factor, then that common load is exactly

\[
                         \mu_s={\mathbb E P_s\over\binom{k}{s}}.     \tag{5.1}
\]

If `|mathcal R|_own` denotes the number of owner positions covered by the
factor, then every rail has `N` owner positions and, for a uniform
minimum-schedule decoration, the core contribution at width `ell` is

\[
                         H_\ell\sim\operatorname {Bin}
                                  (c,p_{q,\ell}).                    \tag{5.2}
\]

Therefore

\[
 \boxed{
 \mu_s={|\mathcal R|_{own}\over\binom{k}{s}}
        \sum_{\ell=1}^{q-1}
        \Pr\{H_\ell=s-\ell\}.}                                    \tag{5.3}
\]

This is an exact symmetric fractional lower-coverage theorem, not an
integral selection.  It gives positive load at every rank `1<=s<R` for
which the binomial event is legal.  At the central first-hit near-factor,
`|mathcal R|_own=W-|mathcal L|`, with the exact leave from the first-hit
theorem.

The accompanying `h100` evaluation found the following minimum raw loads
over the PBBS deep band `d+1<=s<=R-d-1`, using all minimum three-hit
schedules uniformly:

| `k` | `q=d+1` | hit owners / `W` | minimum deep `mu_s` |
|---:|---:|---:|---:|
| 101 | 8  | 0.6715772 | 0.3941517 |
| 201 | 10 | 0.8255050 | 0.3092790 |
| 301 | 12 | 0.8783994 | 0.2573076 |
| 401 | 14 | 0.8780125 | 0.2337123 |
| 641 | 17 | 0.9272951 | 0.2144728 |
| 1001| 21 | 0.9499617 | 0.2216892 |

Thus the symmetric measure has uniformly positive finite-instance deep
marginals in the tested range.  No asymptotic lower bound is claimed here,
and positive marginals alone do not round to one antecedent per rail.

## 6. The exact simultaneous selection system

Let `mathcal D_r` be the finite set of legal schedule decorations
`theta=(E_f)_(f in F_r) in M_q^(F_r)` of rail `r`.  Let `P(r,theta,S)` be
the number of marked strict-lower intervals of the decorated rail whose
value is `S`.

Choosing exactly one antecedent for every already selected owner rail and
covering every desired lower target is the 0--1 system

\[
 \sum_{\theta\in\mathcal D_r}z_{r,\theta}=1
 \qquad(r\in\mathcal R),                                            \tag{6.1}
\]

\[
 \sum_{r\in\mathcal R}
 \sum_{\theta\in\mathcal D_r}
 P(r,\theta,S)z_{r,\theta}\ge1
 \qquad(S\in\mathcal L_{\rm required}),                            \tag{6.2}
\]

\[
                         z_{r,\theta}\in\{0,1\}.                    \tag{6.3}
\]

For occurrence-labelled or exact-once tickets, replace (6.2) by the
corresponding labelled equality rows.  Protected history, socket, or cap
tickets are additional rows on the same columns.

Equivalently, make one part for every rail, one vertex for every required
target, and one hyperedge for every decorated rail column; seek a
transversal selecting one column from each rail part whose union covers
the target shore.  Formula (4.5) gives the exact target degrees before
cross-target correlations are imposed.

Theorem 2.1 proves every **individual** target compatible with a fixed
toggle interval has a column.  It does not prove that the columns selected
for different targets agree coordinatewise on one global decoration.
That correlation is precisely the remaining integral gate in (6.1)--(6.3).

## 7. Verification artifacts

* `verify_period_2q_plus_1_minimum_core_schedules.py` enumerates every
  minimum schedule for `q=2,...,12`, checks the exact count (1.5), the
  avoid-count formula (3.2), and both schedules in Theorem 2.1.  The remote
  output was `PASS` in every case.
* `analyze_distributed_core_symmetric_fractional_coverage.py` evaluates
  (5.3) and the exact first-hit owner count with integer coefficient
  arithmetic on `h100`.
