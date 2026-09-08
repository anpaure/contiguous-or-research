# Point-margin-compatible balanced capacities

Date: 2026-07-24

## Status

The capacity-respecting wreath reduction requires floor/ceiling capacities at
every controlled rank.  Their total sum is not the only linear constraint:
every cyclic order has an exact coordinate-incidence margin.  This note proves
that balanced capacities can always be chosen to satisfy those margins
exactly.  Thus there is no hidden one-coordinate divisibility obstruction to
the CRP gate.

Throughout,

\[
n=2m+1,\qquad W=\binom nm,\qquad B=W/n,
\]

and fix a lower rank `r=m-q`, with `1<=r<n` and

\[
N=\binom nr,\qquad
c=\left\lfloor\frac WN\right\rfloor,
\qquad
a=W-cN,\quad 0\le a<N.
\tag{1}
\]

## Theorem 1 (regular high-capacity family)

There is a family

\[
\mathcal R\subseteq\binom{[n]}r
\]

of exactly `a` targets such that every coordinate belongs to exactly

\[
\boxed{d=\frac{ra}{n}}
\tag{2}

members of `R`.  In particular, `d` is an integer.

Consequently the capacities

\[
b(S)=c+\mathbf 1_{\{S\in\mathcal R\}}
\tag{3}
\]

satisfy

\[
\boxed{
b(S)\in\{\lfloor W/N\rfloor,\lceil W/N\rceil\},
\qquad \sum_Sb(S)=W,
}
\tag{4}
\]

and the exact point margins

\[
\boxed{
\sum_{S\ni x}b(S)=rB
\qquad(x\in[n]).
}
\tag{5}

### Proof

First,

\[
\frac{ra}{n}
=\frac{rW}{n}-c\frac{rN}{n}
=rB-c\binom{n-1}{r-1}
\tag{6}
\]

is an integer.  Moreover `0<=d<binom(n-1,r-1)` because `0<=a<N`.

For completeness, use the almost-regular partition form of Baranyai's
theorem: if prescribed part sizes sum to the number of edges of a complete
uniform hypergraph, its edges can be partitioned into parts which are almost
regular.  Apply it with part sizes `a` and `N-a` (with the case `a=0`
handled by taking the empty family).  The first part has average vertex
degree

\[
\frac{ra}{n}=d.
\tag{7}
\]

Since this average is an integer, an almost-regular first part is actually
`d`-regular.  Choose it as `R`.  Equivalently, this is the
`(d,binom(n-1,r-1)-d)` instance of the arbitrary-degree factorization form
of Baranyai's theorem.  Double-counting incidences gives

\[
|\mathcal R|=\frac{nd}{r}=a.
\]

Equations (3)--(4) follow.  Finally,

\[
\sum_{S\ni x}b(S)
=c\binom{n-1}{r-1}+d
=\frac{r(cN+a)}n
=\frac{rW}{n}=rB,
\]

which proves (5).  QED

The precise almost-regular statement is Baranyai's theorem as restated in
Theorem 1.1 of A. Bahmanian,
[*Connected Baranyai's Theorem*](https://arxiv.org/abs/1909.09643).
Bahmanian's Theorem 1.2 also gives the arbitrary-degree factorization form
used in the equivalent description above (and additionally supplies
connectivity when the factor degree is at least two).

## Corollary 2 (exact local deficit margins)

Let `P` consist of `s` cyclic orders and put

\[
L=W-ns.
\]

For the capacities in Theorem 1, suppose every depth-`q` load obeys
`mu_q(S)<=b(S)`.  Then for every coordinate `x`,

\[
\boxed{
\sum_{S\ni x}\bigl(b(S)-\mu_q(S)\bigr)=\frac{rL}{n}.
}
\tag{8}

### Proof

Every cyclic order has exactly `r` cyclic intervals of length `r` containing
`x`.  Therefore

\[
\sum_{S\ni x}\mu_q(S)=rs.
\]

Subtract this from (5) and use `B-s=L/n`.  QED

In particular, `L` is automatically divisible by `n`, and the global deficit
identity `sum_S(b-mu)=L` refines to uniform coordinate margins.  The
floor/ceiling capacity fibre is therefore compatible with every unavoidable
zero- and first-moment invariant of a wreath packing.

## What remains

The theorem only constructs the capacity vectors, not the wreath packing that
respects them.  Higher-order correlations between coordinates and the common
ownership of all depths remain the integral obstruction.  Its value is that a
future switching or absorption proof may fix the high-capacity families in
advance without fighting a latent point-degree mismatch.
