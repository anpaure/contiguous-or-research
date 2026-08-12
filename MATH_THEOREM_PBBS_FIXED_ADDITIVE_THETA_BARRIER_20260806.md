# Fixed additive slack does not remove the PBBS theta reset barrier

**Date:** 2026-08-06  
**Method:** exact merged-PBBS chain census and uniform local central-limit
asymptotics  
**Status:** unconditional obstruction to the naive `B+C` escape.  Raising
the endpoint-chain depth by any fixed additive constant leaves the limiting
full-piece reset deficit unchanged.  Thus the extra scalar short-window row
at length `B+1` cannot by itself replace shared literal serialization.

## 1. Fixed-charge parameters

Use the odd merged-PBBS parameters

\[
 n=2m+1,\qquad W={n\choose m}.
\]

Let `d=d(n)` be the coefficient-one deadline, so

\[
                         {d^2\over n}\longrightarrow{\pi\over8}.
\tag{1.1}
\]

Fix an integer `C>=0`, independently of `n`, and put

\[
 h=d+C,\qquad t_C=m-h,\qquad M_C={n\choose t_C},
 \qquad U_C=W-M_C.
\tag{1.2}
\]

The direct fixed-charge analogue of the merged free bank has

\[
 b_C=\left\lfloor{U_C\over h+1}\right\rfloor,
 \qquad g_C=b_Ch
\tag{1.3}

endpoint chains.  Split an arbitrary symmetric-chain decomposition into
top-aligned slabs of height `h`, clipped below rank `h+1`.  The exact number
of resulting nonempty pieces is

\[
 P_{n,h}=\sum_{\substack{q\ge0\\qh<t_C-h-1}}
                 {n\choose t_C-qh-1},
\tag{1.4}
\]

and the exact number containing every rank of an unclipped slab is

\[
 F_{n,h}=\sum_{\substack{q\ge0\\t_C-(q+1)h\ge h+1}}
                 {n\choose t_C-(q+1)h}.
\tag{1.5}

The proofs are the same SCD-start telescoping arguments as at charge zero:
a slab piece exists exactly when its chain reaches the slab top, and it is
full exactly when the chain reaches the slab bottom.

Put

\[
                         S_{n,h}:=g_C-P_{n,h}.
\tag{1.6}

This is the number of endpoint chains left after assigning one endpoint to
every SCD piece.

## 2. Fixed shifts disappear in the local limit

Define

\[
 \sigma:=\sum_{a=1}^{\infty}e^{-\pi a^2/4},
 \qquad
 \tau:=\sum_{a=2}^{\infty}e^{-\pi a^2/4}
       =\sigma-e^{-\pi/4}.
\tag{2.1}
\]

### Theorem 2.1 (fixed-charge census limits)

For every fixed `C`,

\[
 \boxed{
 {M_C\over W}\longrightarrow e^{-\pi/4},\qquad
 {g_C\over W}\longrightarrow1-e^{-\pi/4},}
\tag{2.2}
\]

and

\[
 \boxed{
 {P_{n,h}\over W}\longrightarrow\sigma,\qquad
 {F_{n,h}\over W}\longrightarrow\tau.}
\tag{2.3}
\]

#### Proof

Since `h=d+C`, equation (1.1) gives

\[
                         {h^2\over n}\longrightarrow{\pi\over8}.
\tag{2.4}
\]

The fixed displacement `C` and the `O(1)` endpoint offsets are invisible
under the central `sqrt(n)` scaling.  Hence the uniform local
central-binomial estimate gives, for every fixed integer `a>=1`,

\[
 { {n\choose m-ah+O(1)}\over W}
       \longrightarrow e^{-\pi a^2/4}.
\tag{2.5}
\]

Taking `a=1` proves the first limit in (2.2), and (1.3), together with
`h/(h+1)->1`, proves the second.

The `q`-th term of (1.4) has rank

\[
 t_C-qh-1=m-(q+1)h-1,
\]

so (2.5) gives the `(q+1)`-st summand of `sigma`.  The `q`-th term of
(1.5) has rank

\[
 t_C-(q+1)h=m-(q+2)h,
\]

so it gives the `(q+2)`-nd summand and hence `tau`.  A standard Gaussian
upper bound on off-central binomial coefficients dominates both tails by
a summable multiple of `exp(-c(q+1)^2)`, uniformly in `n`.  Dominated
convergence proves (2.3).  \(\square\)

## 3. The theta deficit is charge-invariant

### Theorem 3.1 (fixed-additive theta barrier)

For every fixed `C`,

\[
 \boxed{
 {F_{n,h}-S_{n,h}\over W}
 \longrightarrow
 2\sigma-1
 =4\sum_{j=1}^{\infty}e^{-4\pi j^2}>0.}
\tag{3.1}
\]

Consequently `F_(n,h)>S_(n,h)` for every sufficiently large `n`.

#### Proof

Equations (1.6) and (2.2)--(2.3) give

\[
 {F_{n,h}-S_{n,h}\over W}
 \longrightarrow
 \tau-\bigl(1-e^{-\pi/4}-\sigma\bigr)
 =2\sigma-1.
\]

Poisson summation for the Jacobi theta function gives

\[
 \sigma={1\over2}+2\sum_{j=1}^{\infty}e^{-4\pi j^2},
\]

which proves (3.1) and strict positivity.  \(\square\)

### Corollary 3.2

For no fixed `C` can the direct depth-`d+C` merged implementation satisfy
both of the following rules in all sufficiently large dimensions:

1. every SCD piece consumes one endpoint chain; and
2. every full SCD piece consumes a further private endpoint chain used by
   no other piece.

Indeed, those rules require `P_(n,h)+F_(n,h)` endpoints, whereas only
`g_C=P_(n,h)+S_(n,h)` exist.

## 4. Interpretation for `B+O(1)`

At length `B(k)+C`, the scalar short-interval vacancy gains

\[
                         CW+O_C(k)
\]

cells.  Theorem 3.1 shows that this gain does **not** automatically become
private physical resets in the two-SCD/merged-PBBS geometry.  After the
depth and slab boundary are shifted by any fixed `C`, the same positive
theta fraction of full pieces still requires shared serialization.

Thus one of the following genuinely structural inputs remains necessary
even for an additive-constant theorem:

* a target-disjoint shared packet such as the cyclic star construction;
* a different chain fragmentation whose joins are correlated with the
  owner chronology; or
* a non-PBBS architecture exposing the scalar `CW` vacancy as literal
  compatible cells.

The theorem does not obstruct `nu(k)<=B(k)+O(1)`.  It only rules out the
claim that fixed scalar slack, without a new serialization mechanism,
removes the theta gate.

