# Rank-separated named targets and equitable owner loads round exactly

**Date:** 2026-08-03  
**Status:** unconditional integral theorem.  No computation is used.  The
theorem deliberately does not assert that the targets assigned to one owner
form a flag, or that its selected ranks obey the nonadjacent-rank law.

## 0. Outcome

Let the ground set have size `k`, fix an owner rank `r`, and put

\[
                    \mathcal O={ [k]\choose r},
                    \qquad W=|\mathcal O|.
\]

For every `s<r`, prescribe an integer

\[
                    0\le n_s\le \min\left\{W,{k\choose s}\right\},
\]

and put `N=sum_s n_s`.  Then there are owner sets

\[
                    O_s\subseteq\mathcal O,
                    \qquad |O_s|=n_s,
\]

and injections

\[
 \phi_s:O_s\longrightarrow {[k]\choose s},
 \qquad \phi_s(T)\subseteq T,                              \tag{0.1}
\]

such that the owner loads

\[
                    \ell(T)=|\{s:T\in O_s\}|
\]

differ by at most one.  More precisely, if

\[
                    q=\left\lfloor {N\over W}\right\rfloor,
                    \qquad h=N-qW,
\]

then exactly `h` owners have load `q+1` and the other `W-h` owners have
load `q`.

Consequently, for the optimal triangular inventory

\[
                    n_s={k\choose s}-b_s,
\]

all nonboundary named lower targets can be assigned integrally to distinct
containing owner/rank ports, with the exact rank multiplicities and the
equitable load histogram required by the scalar lower bound.  The omitted
targets are simply the complements of the images in (0.1), so the boundary
families need not be fixed in advance.

This closes rank-separated containment and load balancing.  It does not
close the actual OR compiler: for one owner `T`, the sets
`phi_s(T)` selected at its different ranks need not be mutually nested.

## 1. The containment transversal matroids

For each `s<r`, let `M_s` be the transversal matroid on the owner set
`mathcal O` induced by the bipartite containment graph

\[
             T\sim S \quad\Longleftrightarrow\quad S\subseteq T,
             \qquad
             T\in\mathcal O,
             \quad S\in{[k]\choose s}.                    \tag{1.1}
\]

Thus a family `A subseteq mathcal O` is independent in `M_s` precisely
when its owners can be injected into distinct rank-`s` subsets that they
contain.

### Lemma 1.1 (uniform fractional owner vector)

For every `A subseteq mathcal O`, writing
`p_s=binom(k,s)/W`,

\[
             r_{M_s}(A)\ge \min\{1,p_s\}|A|.               \tag{1.2}
\]

Hence, for every `n_s<=min(W,binom(k,s))`, the constant vector

\[
             x^s_T={n_s\over W}\qquad(T\in\mathcal O)      \tag{1.3}
\]

belongs to the independence polytope of the rank-`n_s` truncation of
`M_s`.

### Proof

For `X subseteq mathcal O`, double-count containment edges from `X` to its
rank-`s` lower shadow `partial_s X`.  Every owner has degree `binom(r,s)`,
while a rank-`s` target belongs to at most `binom(k-s,r-s)` owners.  Thus

\[
 {r\choose s}|X|
 \le {k-s\choose r-s}|\partial_sX|.
\]

The identity

\[
 {r\choose s}W={k\choose s}{k-s\choose r-s}
\]

gives

\[
                 |\partial_sX|
                 \ge { {k\choose s}\over W}|X|.           \tag{1.4}
\]

The transversal-matroid rank formula is

\[
 r_{M_s}(A)
 =\min_{X\subseteq A}\bigl(|A\setminus X|+|\partial_sX|\bigr).
\]

If `p_s<=1`, (1.4) gives

\[
 |A\setminus X|+|\partial_sX|
 \ge |A|-(1-p_s)|X|
 \ge p_s|A|,
\]

which proves (1.2) in this case.

If `p_s>1`, then (1.4) implies `|partial_sX|>=|X|`.  Every term in the
transversal-rank formula is therefore at least `|A|`, so
`r_(M_s)(A)=|A|`.  This proves (1.2) in the remaining case.

Now let `M_s'` be the rank-`n_s` truncation.  For every `A`,

\[
 x^s(A)={n_s\over W}|A|
 \le r_{M_s}(A),
\qquad
 x^s(A)\le n_s.
\]

Indeed, the first inequality uses

\[
 {n_s\over W}\le\min\{1,p_s\},
\]

and the second uses `|A|<=W`.  Hence

\[
 x^s(A)\le\min\{r_{M_s}(A),n_s\}=r_{M_s'}(A).
\]

Together with `x^s>=0`, these are exactly the matroid
independence-polytope inequalities.  `square`

For the Boolean middle rank used in the OR problem, `s<r=ceil(k/2)`, so
`binom(k,s)<=W` and the first case is the only one needed.

## 2. Two-matroid intersection

Take disjoint rank-labelled copies of the owner set,

\[
                   E=\{(T,s):T\in\mathcal O, s<r\}.
\]

On `E`, let

\[
                   M=\bigoplus_{s<r}M_s'                 \tag{2.1}
\]

be the direct sum of the truncated containment transversal matroids.

If `h=0`, let `c=q`.  If `h>0`, put `c=q+1` and introduce one extra dummy
rank `star` of demand

\[
                   D=cW-N=W-h.                            \tag{2.2}
\]

Its matroid is the uniform matroid `U_(D,W)` on the dummy owner tokens
`(T,star)`.  Add this component to (2.1).  In either case call the resulting
direct sum `widetilde M`; when `h=0` there is no dummy component and
`D=0`.

Let `P_c` be the partition matroid on the same ground set with one part for
each owner:

\[
       E_T=\{(T,s):s<r\}
       \quad\text{and, when }h>0,\quad
       E_T\leftarrow E_T\cup\{(T,\star)\},
       \qquad |I\cap E_T|\le c.                            \tag{2.3}
\]

Define the constant fractional vector

\[
 x_{T,s}={n_s\over W},
 \qquad
 x_{T,\star}={D\over W}.                                  \tag{2.4}
\]

Lemma 1.1, direct sums, and the elementary inequalities for a uniform
matroid show that `x` belongs to `P(widetilde M)`.  At every owner,

\[
 \sum_sx_{T,s}+x_{T,\star}
 ={N+D\over W}=c,                                         \tag{2.5}
\]

so `x` also belongs to `P(P_c)`.  Its total weight is `cW`.

For completeness, membership in the partition-matroid polytope follows
from (2.5) together with `0<=x_e<=1`: every subset of one owner part has
weight at most both its cardinality and `c`.  Also the number of available
tokens in every owner part is at least `c`, because
`c=ceil(N/W)` is at most the number of real rank components, with the dummy
token added only in the nonintegral-average case.  Thus `P_c` has total
rank exactly `cW`.

Edmonds' matroid-intersection polytope is integral.  Therefore

\[
                   P(\widetilde M)\cap P(P_c)
\]

contains an integral common independent set `I` of size at least `cW`.
The partition matroid has total rank `cW`, so equality holds.

Every owner part in (2.3) is consequently saturated.  The direct sum has
total rank

\[
                   \sum_s n_s+D=cW,
\]

so every real rank component has size exactly `n_s` and the dummy
component has size exactly `D`.

Delete the dummy tokens.  The `D=W-h` owners that carried one dummy token
have real load `q`; the remaining `h` owners have real load `q+1`.  For
each real rank `s`, independence in `M_s` supplies the injection (0.1).
This proves the theorem.

## 3. Exact relation to the noncontiguous rank law

The equitable rank-law theorem proves a different projection: it chooses
exactly `W` abstract rank patterns with the right multiplicities, maximum
load, and no adjacent residual ranks.  The present theorem chooses exact
named targets and containing owners with the same multiplicities and the
same equitable load histogram.  Neither theorem implies the other at the
labelled flag level.

Their missing intersection is now particularly explicit.  For every
owner `T`, one needs simultaneously

1. its selected ranks to be one allowed edge matching in the
   collar/residual rank graph; and
2. its assigned targets to be the corresponding prefixes of one ordering
   of `T`.

Condition 1 is an owner-local path-matching constraint.  Condition 2 is
owner-local flag compatibility.  Adding either to the two-matroid proof is
not another rank or containment inequality: it correlates different direct
summands `M_s` on the same owner.

In particular, arbitrary rank-by-rank matchings cannot be declared
chainized.  Already two assigned targets `S` and `U` at ranks `s<t` fail to
come from one owner ordering unless `S subset U`.  The theorem makes no
such assertion.

## 4. Proof-safe conclusion

For the lower compiler, the following rows are now separately integral:

* the exact noncontiguous rank inventory and equitable pattern sizes;
* every named rank target against Boolean containment; and
* the exact equitable owner-load histogram.

The remaining lower-side theorem is a **correlated flag intersection**:
choose the two integral objects so that the rank occurrences on each owner
are nonadjacent where required and their named targets form one inclusion
flag.  Any proof of `nu(k)=B(k)+O(1)` must still couple that flag object to
the upper chronology, common-cap state, and regeneration.  The present
theorem removes no such gate and makes no all-`k` upper-bound claim.
