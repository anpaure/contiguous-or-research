# Full SCD pieces almost fit one reset each, but a theta-function excess forces shared serialization

**Date:** 2026-08-06  
**Method:** exact symmetric-chain counting and local central-limit asymptotics  
**Status:** unconditional counting theorem and sharp obstruction to one
natural completion of the merged PBBS architecture.  The unused endpoint
chains are enough for almost every full SCD piece, but not for all of them:
the deficit has positive limiting density

\[
             4\sum_{j\ge1}e^{-4\pi j^2}=0.0000139\ldots
\]

relative to the central layer.  Hence a construction which spends one
otherwise unused endpoint after every full piece is asymptotically
impossible.  Only a very small positive fraction of the full pieces must
share joins, so this does not refute the merged architecture.

## 1. Parameters

Use the odd merged-PBBS parameters

\[
 n=2m+1,\qquad r=m,\qquad t=m-d,\qquad
 W={n\choose m},\qquad M={n\choose t},\qquad U=W-M.
\tag{1.1}
\]

The merged free region has

\[
 b=\left\lfloor {U\over d+1}\right\rfloor,
 \qquad g=bd
\tag{1.2}
\]

endpoint chains.  The exact number of SCD pieces needed for the deep band
is

\[
 P_{n,d}=\sum_{\substack{q\ge0\\qd<t-d-1}}
                 {n\choose t-qd-1}.
\tag{1.3}
\]

Thus

\[
                         S_{n,d}:=g-P_{n,d}
\tag{1.4}
\]

is the number of endpoint chains left after assigning one endpoint to
every SCD piece.

Split the deep band into the top-aligned slabs

\[
 [t-(q+1)d,\,t-qd-1],\qquad q=0,1,\ldots,
\tag{1.5}
\]

clipped at rank \(d+1\).  Call a piece **full** if it contains all \(d\)
ranks of its slab.

## 2. Exact full-piece census

### Theorem 2.1

The number of full pieces is exactly

\[
 \boxed{
 F_{n,d}=\sum_{\substack{q\ge0\\t-(q+1)d\ge d+1}}
                 {n\choose t-(q+1)d}.}
\tag{2.1}
\]

#### Proof

Fix a nonclipped slab and put

\[
                         L_q=t-(q+1)d.
\]

A symmetric chain contributes a full piece to this slab exactly when it
passes through rank \(L_q\).  Every rank-\(L_q\) set belongs to one SCD
chain.  Conversely, because \(L_q<t\le m\), the symmetric mate of that
set lies above the upper end \(t-qd-1\), so its chain crosses the entire
slab.  Hence the full pieces in slab \(q\) are in bijection with the
rank-\(L_q\) sets and number \({n\choose L_q}\).  Summing over precisely
the nonclipped slabs gives (2.1). \(\square\)

This count is independent of which symmetric-chain decomposition is used.
Changing the SCD cannot remove the reset demand measured here.

## 3. The limiting theta constants

At the optimal deadline,

\[
                         {d^2\over n}\longrightarrow {\pi\over8}.
\tag{3.1}
\]

For every fixed integer \(a\ge1\), the uniform central-binomial estimate
therefore gives

\[
 { {n\choose m-ad+O(1)}\over W}
       \longrightarrow e^{-\pi a^2/4}.
\tag{3.2}
\]

The standard Gaussian upper bound dominates the tails uniformly, so
dominated convergence may be used in all sums below.  Put

\[
 \sigma:=\sum_{a=1}^{\infty}e^{-\pi a^2/4}.
\tag{3.3}
\]

The merged-piece census already gives

\[
                         {P_{n,d}\over W}\longrightarrow\sigma,
\tag{3.4}
\]

and (1.2) gives

\[
                         {g\over W}\longrightarrow1-e^{-\pi/4}.
\tag{3.5}
\]

Equation (2.1) begins at displacement \(2d\), so it gives the new limit

\[
 \boxed{
 {F_{n,d}\over W}\longrightarrow
       \tau:=\sum_{a=2}^{\infty}e^{-\pi a^2/4}
             =\sigma-e^{-\pi/4}.}
\tag{3.6}
\]

Consequently

\[
 {S_{n,d}\over W}\longrightarrow
             1-e^{-\pi/4}-\sigma.
\tag{3.7}
\]

## 4. The reset deficit is strictly positive

### Theorem 4.1 (theta reset barrier)

For all sufficiently large parameters,

\[
                         \boxed{F_{n,d}>S_{n,d}.}
\tag{4.1}
\]

More exactly,

\[
 \boxed{
 {F_{n,d}-S_{n,d}\over W}\longrightarrow
       2\sigma-1
       =4\sum_{j=1}^{\infty}e^{-4\pi j^2}>0.}
\tag{4.2}
\]

#### Proof

Subtract (3.7) from (3.6):

\[
 \tau-(1-e^{-\pi/4}-\sigma)
 =\sigma-e^{-\pi/4}-1+e^{-\pi/4}+\sigma
 =2\sigma-1.
\tag{4.3}
\]

Poisson summation for the Jacobi theta function gives

\[
 \sigma={1\over2}+2\sum_{j=1}^{\infty}e^{-4\pi j^2}.
\tag{4.4}
\]

Substitution proves (4.2), and every term in the final series is positive.
The strict limiting inequality implies (4.1). \(\square\)

Numerically,

\[
 \begin{aligned}
 F_{n,d}/W&\longrightarrow0.044068\ldots,\\
 S_{n,d}/W&\longrightarrow0.044054\ldots,
 \end{aligned}
\tag{4.5}
\]

so the failure is very small but macroscopic: it is still a positive
constant times \(W\), not a boundary term.

### Corollary 4.2

Any merged-PBBS implementation satisfying both of the following rules is
impossible for all sufficiently large parameters:

1. every SCD piece consumes one endpoint chain; and
2. every full SCD piece additionally consumes a distinct endpoint chain
   which carries no other piece.

#### Proof

The two rules require at least \(P_{n,d}+F_{n,d}\) endpoint chains.  The
available number is \(g=P_{n,d}+S_{n,d}\), while Theorem 4.1 says
\(F_{n,d}>S_{n,d}\). \(\square\)

## 5. What the tiny excess means

The barrier is much weaker than a no-go for merging.  The fraction of full
pieces which cannot receive a private extra endpoint tends to

\[
 {2\sigma-1\over\sigma-e^{-\pi/4}},
\tag{5.1}
\]

which is about three parts in ten thousand.  Thus any of the following
would evade Corollary 4.2:

* a positive-density family of directly compatible consecutive full
  pieces;
* one reset endpoint shared by two or more full pieces;
* a bounded-width Euler splice which joins several full-piece traces at
  once; or
* a support-first chart in which full SCD pieces are replaced by a
  different, jointly serializable chainization.

The exact next target is therefore not private reset supply.  It is the
much narrower statement that at least

\[
                         (2\sigma-1+o(1))W
\tag{5.2}
\]

full pieces can be paired or grouped into shared literal joins while
preserving their target labels and owner envelopes.  This is only a tiny
fraction of the full-piece bank, but it is an integral, occurrence-level
condition and does not follow from endpoint counts.

## 6. Scope

This theorem proves an exact SCD-independent full-piece census and a sharp
asymptotic obstruction to one private-reset architecture.  It does not
prove that a single endpoint really suffices to reset an otherwise isolated
full piece; that is an additional literal hypothesis in Corollary 4.2.  It
also does not construct the shared joins required by (5.2), satisfy the
PBBS cover inequalities, or prove \(\nu(k)\le B(k)+O(1)\).

