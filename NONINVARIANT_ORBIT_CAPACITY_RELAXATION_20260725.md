# Non-invariant orbit capacity: the exact relaxed gate after seed invariance

Date: 2026-07-25

Method: pure combinatorics only.

## 0. Outcome

Invariant targets are only the one-point orbits of the coordinate group.
This note identifies the next obstruction for non-invariant suspended-seed
targets and proves that it too disappears on a logarithmic connected
support if row lineages are allowed to choose their group elements
independently.

The independence is a relaxation of legal exact-factor switching.  Thus
the result is not an FSP construction.  Its purpose is to isolate the
remaining mathematics: **correlation between row lineages inside legal
interaction components**.

Let (mathscr M) be any row-disjoint matching of three-owner depth-one
packets in the canonical MSW factor, with distinct common targets, all
containing the distinguished coordinate (infty).  Every suspended copy
of the audited (A/B/DD) seed has this property.

Choose a connected coordinate support (B) of size (b) containing
(infty), and put (G=operatorname{Sym}(B)).  Partition the source
targets of (mathscr M) into their (G)-orbits.  For an orbit
(mathcal O), write

\[
 d_{\mathcal O}=|\mathcal O|,
 \qquad
 R_{\mathcal O}
 =\#\{P\in\mathscr M:\operatorname{target}(P)\in\mathcal O\}.
\]

If

\[
 \boxed{3R_{\mathcal O}\le2d_{\mathcal O}}                    \tag{0.1}
\]

for every orbit, then independent rowwise (G)-actions can distribute all
three owners of every packet so that no target receives more than two of
the designated owners.  Since the number of available depth-one quota-two
resources exceeds the total number of matching rows, a balanced quota can
then assign quota two wherever needed.  The entire designated seed
certificate disappears in this rowwise relaxation.

Moreover, for a random (B=\{\infty\}\cup R), with (R) a uniform
((b-1))-subset of the finite coordinates, all orbits whose source targets
meet (B) in at most (2b/3) automatically satisfy (0.1).  The expected
number of remaining high-intersection source packets is at most

\[
 \boxed{
 |\mathscr M|\exp(-c b)
 }                                                               \tag{0.2}
\]

for an absolute constant (c>0) (one may take any fixed
(c<1/18) for all sufficiently large (b,m) with (b=o(m))).

Consequently a support of size (C\log m) makes the relaxed residual
(o(\operatorname{Cat}_m/\sqrt m)).  What remains unproved is whether
legal component switches can approximate these independent rowwise orbit
assignments.

## 1. Orbit capacity

Fix one (G)-orbit (mathcal O) of rank-((m-1)) targets.  Suppose it
contains (R=R_{\mathcal O}) source triples.  There are (3R) distinct
designated owner rows, because (mathscr M) is row-disjoint.

In the rowwise relaxation, a row owning (S\in\mathcal O) may be acted on
by an arbitrary element of (G).  Since (G) is transitive on
(mathcal O), that row may be sent to an owner of any prescribed target
in (mathcal O).  The choices for different rows are independent.

Thus the (3R) owners can be placed with load at most two on the (d)
resources exactly when

\[
 3R\le2d.
\]

Necessity is total capacity.  Sufficiency follows by filling the (d)
boxes successively, at most two units per box.

The number of boxes which need quota two is at most (3R).  Summed over
all orbits this is at most

\[
 3|\mathscr M|\le t,
 \qquad t=\operatorname{Cat}_m,
\]

because the matching uses three distinct rows per triple.  At depth one
the number of quota-two resources is

\[
 \delta_1=W-N_1
 =\frac{2W}{m+2}
 =\frac{2(2m+1)}{m+2}t
 >t.
\]

Hence a balanced quota can put value two on every designated load-two
resource and place its remaining bonuses arbitrarily.  No designated
owner set then contains a packet.

This proves (0.1).

## 2. Targets containing the distinguished coordinate occupy only one slice

Let a target (S) satisfy

\[
 a=|S\cap B|.
\]

Its (G)-orbit consists of all targets with the same outside part
(S\setminus B) and any (a)-subset of (B).  Therefore

\[
 d_{\mathcal O}=\binom ba.                                     \tag{2.1}
\]

Every source target in (mathscr M) contains (infty).  Among all
members of (mathcal O), exactly

\[
 \binom{b-1}{a-1}
 =\frac ab\binom ba                                             \tag{2.2}
\]

contain (infty).  The source targets are distinct, so

\[
 \boxed{
 R_{\mathcal O}
 \le\frac ab,d_{\mathcal O}.
 }                                                               \tag{2.3}
\]

If (a\le2b/3), equation (2.3) gives

\[
 3R_{\mathcal O}\le2d_{\mathcal O},
\]

which is precisely (0.1).  Thus only source targets containing more than
two thirds of the support can create a capacity obstruction in the
rowwise relaxation.

## 3. A random support eliminates high-intersection targets

Fix one source target (S), of rank (m-1), containing (infty).
Choose

\[
 B=\{\infty\}\cup R,
\]

where (R) is a uniform ((b-1))-subset of the (2m) finite
coordinates.  Then

\[
 |S\cap B|
 =1+X,
\]

where (X) is hypergeometric with population (2m), success count
(m-2), and sample size (b-1).  Its mean is less than

\[
 \frac{b-1}{2}.
\]

Hoeffding's inequality for sampling without replacement gives, for all
sufficiently large (b) and (b=o(m)),

\[
 \Pr\left(1+X>\frac{2b}{3}\right)
 \le \exp(-c b)                                                 \tag{3.1}
\]

with any fixed (c<1/18).  (The threshold lies (b/6+O(1)) above the
mean, and the usual bound is
(\exp(-2(b/6+O(1))^2/(b-1))\).)

By linearity of expectation, the expected number of source packets with
high-intersection target is at most the right side of (0.2).  Some fixed
support (B) attains that bound.

For that support, every remaining orbit satisfies (0.1) and can be erased
in the independent-row relaxation.  Since

\[
 |\mathscr M|\le t/3,
\]

taking (b=C\log m) with (cC>1/2) makes the exceptional packet count

\[
 o(t/\sqrt m).
\]

## 4. Exact status

Proved:

1. orbit capacity (0.1) is necessary and sufficient in the independent
   rowwise (G)-action relaxation;
2. because every suspended-seed target contains (infty), every orbit
   below the two-thirds slice automatically has enough capacity;
3. a logarithmic connected support leaves only
   (o(t/\sqrt m)) high-slice source triples.

Not proved:

1. independent rowwise choices (g_E\in G) need not be realizable by
   legal exact-factor component switches;
2. rows outside the designated seed matching may create other packets;
3. the theorem therefore does not produce an FSP exact factor.

The remaining gate has now become precise: prove a legal-switch
approximation/suspension theorem for the rowwise orbit allocation, or prove
that interaction-component correlations force positive packet mass even
when every target orbit has ample capacity.
