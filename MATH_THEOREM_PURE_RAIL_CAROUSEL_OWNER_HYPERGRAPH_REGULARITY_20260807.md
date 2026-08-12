# Exact regularity and codegrees of the pure-rail carousel owner hypergraph

**Date:** 2026-08-07  
**Status:** unconditional counting theorem.  It concerns the owner row only;
lower decorations, component fusion, and the common compiler are not included.

## 1. The owner-component hypergraph

Fix integers (k,R,d), and put

\[
 q=d+1,\qquad c=R-q,\qquad M=k-c=k-R+q.
\tag{1.1}
\]

Assume (c\ge0) and (M>2q).  The vertex set is the middle layer

\[
 \mathcal O={ [k]\choose R}.
\]

A rooted oriented pure-rail carousel is a pair ((C,\sigma)), where

* (C\in{[k]\choose c});
* (sigma:\mathbb Z_M\to[k]\setminus C) is a bijection.

Its owner edge is

\[
 E(C,\sigma)=
 \left\{
 C\cup\{\sigma(i),\sigma(i+1),\ldots,\sigma(i+q-1)\}:
 i\in\mathbb Z_M
 \right\}.
\tag{1.2}
\]

Thus every edge has exactly (M) owners.  Rooting and orientation retain
parallel copies of the same unrooted owner edge.  This is convenient for exact
regularity and does not change the existence of a matching.

This is precisely the (a=d,p=1,h_0=1) owner row of the unified rail queue:
the permanent core has rank (R-d-1=c), and the owners are the core plus
(d+1=q) consecutive toggle labels.

## 2. Exact degree

### Theorem 2.1

The carousel hypergraph is (M)-uniform and regular.  The degree of every
owner is

\[
 \boxed{
 D={R\choose c},M,q!\,(M-q)! .}
\tag{2.1}
\]

#### Proof

Fix (T\in\mathcal O).  Its carousel core can be any
(C\in{T\choose c}).  For a fixed (C), put (Q=T\setminus C), so
(|Q|=q).  To make (Q) a cyclic interval in the rooted order (sigma),
choose its initial position in (M) ways, order (Q) in (q!) ways, and
order the remaining labels in ((M-q)!) ways.  Because (q<M/2), the initial
position is unique.  Multiplying by ({R\choose c}) gives (2.1).  \(□\)

As a check, double counting incidences gives

\[
 {k\choose c}M!\,M={k\choose R}D.
\tag{2.2}
\]

## 3. Exact pair-codegrees

Let (T,T'\in\mathcal O) be distinct and put

\[
 t=|T\cap T'|,\qquad s=t-c.
\tag{3.1}
\]

### Theorem 3.1

If (t<c), the codegree of (T,T') is zero.  If (0\le s\le q-1), it is

\[
 \lambda_s={c+s\choose c}F_s,
\tag{3.2}
\]

where

\[
 F_0=M(M-2q+1)(q!)^2(M-2q)!
\tag{3.3}
\]

and, for (1\le s\le q-1),

\[
 F_s=2M\,s!\,((q-s)!)^2\,(M-2q+s)!.
\tag{3.4}
\]

#### Proof

A common carousel must have a specified core
(C\in{T\cap T'\choose c}).  For fixed (C), the residues
(Q=T\setminus C) and (Q'=T'\setminus C) are (q)-sets in an (M)-set
with intersection (s).

Two cyclic intervals of length (q<M/2) with positive intersection (s<q)
have exactly two possible relative offsets.  Choosing the first initial
position, then bijecting the four labelled regions
(Q\cap Q'), (Q\setminus Q'), (Q'\setminus Q), and the exterior gives
(3.4).

For (s=0), after choosing the first interval there are (M-2q+1) disjoint
initial positions for the second.  Bijection of the two (q)-blocks and the
exterior gives (3.3).  Finally multiply by the number
({c+s\choose c}) of possible specified cores.  \(□\)

### Corollary 3.2 (sharp maximum codegree)

Suppose

\[
 2(c+1)\ge q^2
\tag{3.5}
\]

and

\[
 (c+s+1)(M-2q+s+1)\ge(q-s)^2
 \quad(1\le s\le q-2).
\tag{3.6}
\]

Then (lambda_s) is nondecreasing, so the largest pair-codegree occurs for
two adjacent owners, (s=q-1).  Its exact relative size is

\[
 \boxed{
 \frac{\Delta_2}{D}=\frac{2}{R(M-q)}
 =\frac{2}{R(k-R)}=\Theta(k^{-2}).}
\tag{3.7}
\]

For (R=\lceil k/2\rceil) and the optimal
(d=\sqrt{\pi k/8}+O(1)), conditions (3.5)--(3.6) hold for all sufficiently
large (k).

#### Proof

Directly from (3.3)--(3.4),

\[
 \frac{\lambda_1}{\lambda_0}=\frac{2(c+1)}{q^2},
\tag{3.8}
\]

and for (1\le s\le q-2),

\[
 \frac{\lambda_{s+1}}{\lambda_s}
 =\frac{(c+s+1)(M-2q+s+1)}{(q-s)^2}.
\tag{3.9}
\]

The hypotheses therefore give monotonicity.  At (s=q-1), divide (3.4)
by (2.1) and use

\[
 \frac{{R-1\choose c}}{{R\choose c}}=\frac qR,
 \qquad M-q=k-R,
\]

to obtain (3.7).  The final assertion follows from
(c,M=\Theta(k)) and (q^2=(\pi/8+o(1))k).  \(□\)

## 4. Fractional factor and the exact integral gate

Giving every rooted carousel weight (1/D) is a fractional perfect matching:
every named owner has load one.  Its total component mass is

\[
 \frac{{k\choose R}}M.
\tag{4.1}
\]

Thus the pure owner problem has unusually strong pseudorandom local data:

\[
 \boxed{
 \text{exact regularity and }\Delta_2/D=\Theta(k^{-2}).}
\tag{4.2}
\]

This is enough for the standard near-perfect-matching heuristic, but it is
not by itself an exact perfect-matching theorem.  A pure-rail perfect matching
also requires

\[
 M\mid {k\choose R}.
\tag{4.3}
\]

The unified rail family supplies additional closed-component sizes.  Writing
(p=d-a+1\in\{1,\ldots,d+1\}), every maximal component has

\[
 \boxed{
 N_p=p\left\lfloor\frac Mp\right\rfloor
 =M-(M\bmod p).}
\tag{4.4}
\]

Consequently any exact selection made only from closed unified components
must satisfy the root-lattice condition

\[
 \gcd\{N_p:1\le p\le d+1\}\mid {k\choose R}.
\tag{4.5}
\]

An open residual carousel or a bounded component-size absorber is therefore
not merely a topological convenience: it is the natural mechanism for
removing closed-component divisibility defects.

## 5. Proof-safe consequence

The owner-rounding target has now been reduced to an explicit design problem:

> Find a perfect or bounded-defect matching in the carousel hypergraph, using
> the variable sizes (N_p) as needed, together with a bounded absorber for
> the root lattice; then refine each chosen owner component by one compatible
> lower-profile decoration.

The exact codegree calculation rules out local concentration as an owner-only
obstruction.  It does **not** yet prove the required matching, the decorated
target-once factor, palette-preserving fusion, or a universal OR word.
