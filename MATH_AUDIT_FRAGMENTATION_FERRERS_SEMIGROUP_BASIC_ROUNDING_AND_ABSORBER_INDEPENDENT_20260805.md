# Independent audit: Ferrers fragmentation, basic rounding, and the finite absorber

**Date:** 2026-08-05  
**Audited theorem:**
`MATH_THEOREM_FRAGMENTATION_FERRERS_SEMIGROUP_BASIC_ROUNDING_AND_ABSORBER_20260805.md`  
**Audited self-audit:**
`MATH_AUDIT_FRAGMENTATION_FERRERS_SEMIGROUP_BASIC_ROUNDING_AND_ABSORBER_20260805.md`  
**Method:** independent pure-mathematical reconstruction; no computation,
search, or solver  
**Verdict:** **INDEPENDENT GO** at the theorem's stated conditional scope.
One wording clarification was inserted in the absorber proof so that the
divisible case visibly produces a positive last piece.  No mathematical
claim or bound changed.

## 1. Exact Ferrers correspondence

For a piece multiset with all lengths in `[D]`, its conjugate tail

\[
                         z_q=\#\{\ell:\ell\ge q\}
\]

is a nonincreasing nonnegative integer vector and double counting cells in
the Ferrers diagram gives

\[
                         \sum_{q=1}^D z_q=\sum_\ell\ell.
\]

Conversely, putting `z_(D+1)=0` and

\[
                         w_q=z_q-z_{q+1}
\]

recovers exactly `w_q` pieces of length `q`, with

\[
 \sum_{q=1}^D q w_q
 =\sum_{q=1}^D q(z_q-z_{q+1})
 =\sum_{q=1}^D z_q.
\]

For the aggregate piece multiset, let the piece lengths and socket
capacities be sorted decreasingly.  An injection exists exactly when the
`i`th piece is no longer than the `i`th socket.  This is equivalent to the
tail inequalities

\[
 \#\{\text{pieces of length at least }q\}
 \le \#\{\text{sockets of capacity at least }q\}=K_q
 \qquad(1\le q\le D).
\]

The aggregate left side is `sum_a z^a_q`.  This proves both directions of
Theorem 1.1, including distinct physical use of sockets.  The warning about
the naive real slice is also exact: for `L=1,D=2`, the segment has the
fractional endpoint `(1/2,1/2)`, so the correct job polytope is the convex
hull of integer Ferrers configurations, not that real slice.

## 2. Extreme-point support and the `D`-job bound

Each configuration set `P_a` is finite.  The feasible region of (2.1) is a
closed subset of a product of simplices and hence has an extreme point.
Fix such an extreme point `x`, let `S` be its positive support, let
`s=|S|`, and let `b` be the number of active socket inequalities.

On `S`, the active constraint matrix has the `N` job rows and `b<=D`
socket rows, so its rank is at most `N+b`.  If `s>N+b`, a nonzero vector
supported on `S` annihilates every active row.  Both signs of a sufficiently
small perturbation remain nonnegative.  Every inactive socket row has
strict positive slack, and there are finitely many such rows, so the same
small perturbation preserves them too.  This contradicts extremality.
Therefore

\[
                         s\le N+b\le N+D.
\]

If `f_a` is the number of positive configurations of job `a`, every job
has `f_a>=1`, and hence

\[
 \#\{a:f_a\ge2\}
 \le \sum_a(f_a-1)=s-N\le D.
\]

When `f_a=1`, the job equation forces its unique coefficient to be one.
Keeping all such configurations gives an aggregate tail vector no larger
than the full fractional use, so Theorem 1.1 packs them into the original
sockets.  Degeneracy or dependence among active rows can only strengthen
the support bound.  Thus Theorem 2.1 is exact.

## 3. Absorber count, positivity, trimming, and sharpness

For a residual job of length `L`, put `m=ceil(L/D)`.  Then

\[
                         R=L-(m-1)D
\]

satisfies `1<=R<=D`.  The pieces

\[
                         D,\ldots,D,R
\]

therefore are all positive, total `L`, and occupy exactly `m` maximal
sockets.  If `D` divides `L`, then `R=D`; otherwise only the last socket is
trimmed.  This verifies the corrected wording in Lemma 3.1 without adding
any assumption.

Each of at most `h` jobs uses at most `ceil(L_max/D)` sockets, so

\[
                         h\left\lceil{L_{\max}\over D}\right\rceil
\]

capacity-`D` sockets suffice.  This count is also sharp among universal
banks consisting only of capacity-`D` sockets: a family of `h` jobs all of
length `L_max` forces at least `ceil(L_max/D)` distinct sockets per job.

Taking `h=D`, the absorber has exactly

\[
 D\left\lceil{L_{\max}\over D}\right\rceil
\]

sockets and total capacity

\[
 D^2\left\lceil{L_{\max}\over D}\right\rceil.
\]

The absorber is disjoint from the original socket bank.  Hence the
fractional configurations of the discarded jobs need not be retained or
made compatible with the integral packing of the other jobs.  Theorem 2.1
packs the latter into the original bank and Lemma 3.1 packs at most `D`
residual jobs into the auxiliary bank, proving Theorem 3.2.

## 4. Boolean scaling

In the canonical Boolean residual system,

\[
 r=\left\lceil{k\over2}\right\rceil,
 \qquad D=d(k),
 \qquad t_0=r-D.
\]

A job beginning at rank `b>=1` has length `t_0-b`; therefore, whenever the
residual system is nonempty,

\[
                         L_{\max}\le t_0-1=r-D-1<k.
\]

Equality holds for the complete residual histogram; boundary deletion can
only shorten the longest surviving job.

The established coefficient-one asymptotic is

\[
                         D=\Theta(\sqrt{k}).
\]

Consequently

\[
 D\left\lceil{L_{\max}\over D}\right\rceil
 \le L_{\max}+D=O(k)
\]

and

\[
 D^2\left\lceil{L_{\max}\over D}\right\rceil
 \le DL_{\max}+D^2=O(k^{3/2}).
\]

Since the central width `W` is exponential in `k` up to a polynomial
factor, both quantities are `o(W)`.  These are only size comparisons: they
do not turn those maximal sockets into free, occurrence-disjoint physical
cells.

## 5. Boundary and scope

The endpoint triangle has one socket of each exact capacity `1,...,D`, so
it has only one maximal socket.  It therefore cannot dominate the absorber
bank, which may require

\[
                         D\left\lceil{L_{\max}\over D}\right\rceil
\]

maximal sockets.  Core sockets already charged to the fractional workload
cannot be reserved again.  Likewise, scalar short-window capacity created
by an additional word position does not identify the typed,
occurrence-disjoint bank required by Theorem 3.2.

The audited result proves none of the following:

1. feasibility of the fractional configuration LP for the Boolean
   binomial job/socket profile;
2. integral packing into the unaugmented socket multiset;
3. physical exposure of the auxiliary maximal sockets;
4. named containment, chronological serialization, upper coverage,
   residence, or topology;
5. a `B(k)+O(1)` word-length bound.

It proves exactly the anonymous conditional statement: fractional
whole-job feasibility leaves at most `D` unresolved jobs, and a genuinely
adjoined maximum-socket bank of the displayed size absorbs them.  This
matches the self-audit and the source's stated frontier.  **INDEPENDENT
GO.**
