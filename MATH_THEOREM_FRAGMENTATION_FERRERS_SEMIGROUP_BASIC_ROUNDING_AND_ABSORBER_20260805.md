# Fragmentation as a Ferrers semigroup: basic rounding and a universal finite absorber

**Date:** 2026-08-05  
**Method:** pure mathematics; no computation, search, or solver  
**Status:** unconditional exact finite reformulation and conditional integer
rounding theorem.  A feasible fractional whole-job configuration packs all
but at most `D` jobs integrally.  Adding the explicit absorber below makes
the packing completely integral.  The theorem does **not** prove the
fractional Rayleigh/binomial configuration inequalities, and the absorber is
not presently supplied by the coefficient-one triangular boundary bank.

## 0. Setup

Let the jobs have positive integer lengths

\[
                         L_1,\ldots,L_N,
\tag{0.1}
\]

and let the available sockets have capacities in `[D]`.  Write `M_u` for
the number of sockets of exact capacity `u`, and

\[
                         K_q=\sum_{u=q}^D M_u
\tag{0.2}
\]

for the capacity-tail vector.  A job may be cut into positive integer
pieces, each piece being injected into one socket of at least its length.
Sockets may be left unused and the last piece placed in a socket may be
shorter than its capacity.

The coefficient-one Boolean application has `D=d(k)` and canonical suffix
jobs as in
`MATH_THEOREM_MONOTONE_INTERVAL_CANONICAL_FRAGMENTATION_EQUIVALENCE_20260804.md`.
Nothing in Sections 1--3 below is asymptotic or Boolean-specific.

## 1. Exact Ferrers-semigroup formulation

For a fragmentation of job `a`, define its conjugate tail vector

\[
 z^a_q=\#\{\hbox{pieces of job }a\hbox{ having length at least }q\},
 \qquad 1\le q\le D.
\tag{1.1}
\]

### Theorem 1.1 (whole-job fragmentation is Ferrers packing)

The jobs can be fragmented and injected into the sockets if and only if
there are integer vectors `z^a` satisfying

\[
 z^a_1\ge z^a_2\ge\cdots\ge z^a_D\ge0,
 \qquad
 \sum_{q=1}^D z^a_q=L_a
 \quad(1\le a\le N),
\tag{1.2}
\]

and

\[
                         \sum_{a=1}^N z^a_q\le K_q
                         \qquad(1\le q\le D).
\tag{1.3}
\]

Thus the exact anonymous integer gate is a semigroup packing of Ferrers
columns.  It is not merely ordinary scalar Hall or a transportation table.

#### Proof

Given piece lengths, (1.1) is nonincreasing and

\[
 \sum_{q=1}^D z^a_q
 =\sum_{\ell\text{ a piece of }a}\sum_{q=1}^D
      {\bf1}_{\{q\le\ell\}}
 =\sum_{\ell\text{ a piece of }a}\ell=L_a.
\]

Conversely, put `z^a_(D+1)=0`.  The differences

\[
                         w^a_q=z^a_q-z^a_{q+1}
\tag{1.4}
\]

are nonnegative integers.  Taking `w^a_q` pieces of length `q` gives total
length

\[
 \sum_{q=1}^D q w^a_q=\sum_{q=1}^D z^a_q=L_a.
\]

For an aggregate piece multiset, injection into the capacities is
equivalent to all sorted-tail inequalities: the number of pieces of length
at least `q` must not exceed the number `K_q` of sockets of capacity at
least `q`.  Necessity is immediate; sufficiency follows by sorting pieces
and capacities decreasingly and matching equal indices.  The aggregate
piece tail is exactly `sum_a z^a_q`, proving (1.3) and the theorem.
`square`

### Warning 1.2 (the naive linear relaxation is not the job polytope)

The real slice

\[
 z_1\ge\cdots\ge z_D\ge0,
 \qquad \sum_qz_q=L
\tag{1.5}
\]

need not be integral.  For `L=1,D=2`, the point `(1/2,1/2)` is a vertex
of (1.5), while the only integer partition is `(1,0)`.  Fractional
whole-job feasibility therefore means a convex combination of the
**integer** vectors in (1.2), not arbitrary use of (1.5).

## 2. At most `D` jobs carry every fractional obstruction

For a job `a`, let `P_a` be its finite set of integer Ferrers vectors from
(1.2).  The exact fractional configuration LP is

\[
 \sum_{p\in P_a}x_{a,p}=1\quad(a\in[N]),
 \qquad
 \sum_{a,p}p_qx_{a,p}\le K_q\quad(q\in[D]),
 \qquad x\ge0.
\tag{2.1}
\]

This is the conjugate-tail version of the covering-price LP in the existing
configuration notes.

### Theorem 2.1 (basic rounding leaves at most `D` whole jobs)

If (2.1) is feasible, then there is a set `F` of at most `D` jobs such that
every job outside `F` has an integral fragmentation and all those
fragmentations together fit into the original socket multiset.

More precisely, one may choose a feasible extreme point of (2.1); the jobs
having more than one positive configuration at that point form such a set
`F`.

#### Proof

Choose an extreme point `x`.  Let `s` be the number of its positive
configuration variables.  Restricted to this support, the coefficient
matrix has `N` job-equality rows and at most `D` active socket rows, hence
rank at most `N+D`.  If `s>N+D`, there is a nonzero direction supported on
the positive variables which preserves every job equality and every active
socket equality.  A sufficiently small perturbation in either sign remains
nonnegative and preserves every inactive socket inequality, contradicting
extremality.  Therefore

\[
                              s\le N+D.
\tag{2.2}
\]

Every job has at least one positive variable.  If `F` is the family having
at least two, then

\[
                    |F|\le s-N\le D.
\tag{2.3}
\]

For `a` outside `F`, its unique positive variable equals one by the job
equation.  Retain that integer configuration.  Their aggregate tail use is
at most the total use of `x`, and hence at most `K`; Theorem 1.1 injects
their pieces into the original sockets.  Discarding the jobs in `F` proves
the claim. `square`

### Scope

The theorem is independent of the number and lengths of the jobs.  In the
Boolean application it turns an exponentially large potential integrality
gap into at most `d(k)=Theta(sqrt(k))` unresolved whole chains.  It does not
make that number constant.

## 3. An explicit universal absorber for the residual jobs

Let

\[
                         L_{\max}=\max_aL_a.
\tag{3.1}
\]

For an integer `h>=0`, define an auxiliary socket multiset `A(h)` consisting
only of

\[
             A_D(h)=h\left\lceil{L_{\max}\over D}\right\rceil
\tag{3.2}
\]

sockets of maximum capacity `D`.

When `D=0` there are no positive jobs in the intended application and the
statement is vacuous; assume `D>=1` below.

### Lemma 3.1 (universal residual absorber)

Every family of at most `h` jobs, each of length at most `L_max`, can be
fragmented into the sockets `A(h)`.

#### Proof

Give a residual job of length `L_a` exactly `ceil(L_a/D)` of the auxiliary
sockets.  If `m=ceil(L_a/D)`, fill the first `m-1` sockets to capacity `D`
and put

\[
                         R=L_a-(m-1)D
\]

in the last socket.  The ceiling definition gives `1<=R<=D`, including
`R=D` when `D` divides `L_a`; hence no zero piece is introduced.  Trimming
that last socket when `R<D` is allowed by the physical model.  Each job
uses at most `ceil(L_max/D)` sockets, so (3.2) is sufficient for all `h`
jobs. `square`

### Theorem 3.2 (fractional feasibility plus a finite absorber is integral)

If the fractional configuration LP (2.1) is feasible, then after adjoining
the auxiliary sockets `A(D)` all jobs admit an integral fragmentation.

#### Proof

Apply Theorem 2.1.  Pack every job outside `F` into the original sockets;
these jobs use no auxiliary socket.  Since `|F|<=D`, apply Lemma 3.1 with
`h=D` to the remaining jobs using only the disjoint auxiliary multiset.
The union of the two packings is integral and covers every job. `square`

The absorber contains exactly

\[
 D\left\lceil{L_{\max}\over D}\right\rceil
\tag{3.4}
\]

sockets and has total capacity at most

\[
 D^2\left\lceil{L_{\max}\over D}\right\rceil.
\tag{3.5}
\]

For the even Boolean residual system, `D=Theta(sqrt(k))` and
`L_max=O(k)`.  Hence (3.4) is `O(k)` and (3.5) is `O(k^(3/2))`, both
`o(W)` by an exponential margin.

## 4. Exact boundary of the result

The coefficient-one endpoint triangle supplies only one socket of each
capacity `1,...,D`.  In particular it supplies only one maximum socket,
whereas (3.2) may require

\[
                         D\left\lceil{L_{\max}\over D}\right\rceil
\tag{4.1}
\]

maximum sockets.  Thus the triangle does not dominate the absorber.  Raw
abundance of maximum sockets inside the core does not make them auxiliary;
the fractional scalar ledger can be tight, and reserving core sockets
without simultaneously removing the workload they carried is invalid.

Likewise, the fact that one extra word position creates `W`-scale scalar
short-window capacity does not by itself produce occurrence-disjoint
sockets with exact-type vector (3.2).  The existing generic
configuration counterexamples already show that scalar augmentation alone
does not imply whole-job packing.

Thus Theorem 3.2 identifies a precise next bridge:

> **Capacity-faithful absorber exposure.**  Produce, in one extra-position
> or regenerative carrier face, an occurrence-disjoint socket bank
> dominating (3.2), while the remaining factor still realizes a feasible
> fractional configuration for the nonabsorbed jobs.

If that bridge and the all-price fractional binomial inequality are proved,
the anonymous integer fragmentation gate closes.  Neither premise is
proved here.

## 5. Dependencies

1. `MATH_THEOREM_MONOTONE_INTERVAL_CANONICAL_FRAGMENTATION_EQUIVALENCE_20260804.md`;
2. `MATH_THEOREM_RAYLEIGH_JOB_SOCKET_COAGULATION_EXACT_REDUCTION_20260804.md`;
3. `MATH_THEOREM_RAYLEIGH_INTERVAL_FLOW_DUAL_CLOSEDNESS_AND_RENEWAL_OBSTRUCTION_20260804.md`.
