# PBBS quotient residence: a mountain-tower lower bound at Catalan exponential rate

Date: 2026-07-25

Method: pure mathematics only.  No computation, finite search, or web search
is used.

## 0. Verdict

Put

\[
 N=2m+1,
 \qquad B=\operatorname{Cat}_m,
\]

and use the notation of Theorem 17.1 in
`PBBS_RESIDENCE_PACKING_REDUCTION_20260725.md`.

The desired quotient estimate

\[
 \overline\nu_H=O(B/N)                                      \tag{0.1}
\]

is neither proved nor disproved here.  The following exact lower-bound
family is proved.

Let

\[
 1\le L\le d,
 \qquad d+L\le \min\{H-1,m-1\},
 \qquad M=m-d-L,
 \qquad \theta_L={\pi\over L+2}.
\]

Then there are at least

\[
 a_{m;d,L}:=[z^M]C_L(z)                              \tag{0.2}
\]

Dyck quotient roots whose next consecutive omitted-label return has the
exact odd gap

\[
 \boxed{g=2(d+L)+1.}                                  \tag{0.3}
\]

Here (C_L) is the height-(L) Catalan generating function

\[
 C_{-1}=0,qquad C_0=1,qquad
 C_L={1\over1-zC_{L-1}}.
\]

Every root in the family has height exactly (d+L).  Thus (0.3) is
equality in the pointwise height--gap theorem:

\[
 g=2\operatorname{ht}(D)+1.                           \tag{0.4}
\]

The coefficient in (0.2) has the explicit spectral lower bound

\[
 \boxed{
 a_{m;d,L}
 \ge {4\over L+2}\sin^2\theta_L
       \bigl(2\cos\theta_L\bigr)^{2M}.}               \tag{0.5}
\]

After deleting the quotient roots on the short cycles of Theorem 17.1,
the equal-length interval greedy algorithm gives

\[
 \boxed{
 \overline\nu_H
 \ge {\bigl(a_{m;d,L}-Z_H\bigr)_+
        \over 2d+2L+3}.}                              \tag{0.6}
\]

In particular, suppose (H\gg m^{1/3}) and (H\log N=o(m)).  Taking

\[
 d=L=\left\lfloor
       \left({\pi^2\over\log4}\right)^{1/3}m^{1/3}
      \right\rfloor                                  \tag{0.7}
\]

gives

\[
 \boxed{
 \overline\nu_H
 \ge B\exp\left[-\left(
 3(\pi\log4)^{2/3}+o(1)\right)m^{1/3}\right].}        \tag{0.8}
\]

This applies throughout the intended slow window

\[
 H=\sqrt m\,\omega(m),
 \qquad \omega\to\infty,
 \qquad \omega\log m=o(\sqrt m).
\]

The lower bound (0.8) is still (o(B/N)), so it is not a numerical
counterexample to (0.1).  Its consequence is methodological but exact:
short-return roots already have the full Catalan exponential rate.  A proof
which loses merely (exp(-o(m))), or which only separates exponential
growth constants, cannot establish the required (1/N) quotient scale.
The missing estimate is genuinely polynomial-scale.

There is also a general deterministic necessary condition.  If
(R_H^{\rm long}) is the number of quotient roots on long quotient cycles
which start a residence-(H) interval, then

\[
 \boxed{
 \overline\nu_H\ge {R_H^{\rm long}\over2H+1}.}        \tag{0.9}
\]

Consequently (0.1) forces

\[
 R_H^{\rm long}=O\left({HB\over N}\right).           \tag{0.10}
\]

For (H=\sqrt m\,\omega), the exact quotient theorem must therefore show
that only an (O(\omega/\sqrt m)) fraction of all Dyck roots on long cycles
start a short return, or prove an equally strong clustering statement.

## 1. The mountain core

Let

\[
 E_d=1^d0^d.                                         \tag{1.1}
\]

This is the contour word of the rooted plane path with (d) edges.  Its
first maximum-reaching step is its (d)-th step.  Formula (8.1) of the
residence reduction therefore gives

\[
 \phi(E_d)=E_d,
 \qquad \delta(E_d)=d.                               \tag{1.2}
\]

Put (p=2d+1).  Normalize its first omitted particle label to zero.  The
omitted-particle word in the rank-(d) PBBS is then

\[
 \kappa_t=td\pmod p.                                 \tag{1.3}
\]

Since

\[
 -2d\equiv1\pmod p,
\]

the inverse of (d) modulo (p) is (-2).  For (1\le j\le d), the
first two selections of particle (-j) consequently occur at

\[
 \boxed{t=2j\quad\hbox{and}\quad t=p+2j.}             \tag{1.4}
\]

The inequality (2j<p) is exactly where (j\le d) is used.

## 2. The terminal peak-pruning tower

We use the plane-tree contour bijection.  Simultaneous deletion of every
Dyck peak is simultaneous pruning of every tree leaf, as in Theorem 14.1.

Start with the core path (P_d).  At the root, immediately before its core
child, insert an arbitrary ordered forest all of whose branches have height
at most (L), with total (M) edges.  At the terminal vertex of (P_d),
attach one forced path of (L) new edges.  Make no other attachments.  Call
the resulting tree (T), and let (D(T)) be its Dyck contour.

An ordered forest of branches of height at most (L), placed in one child
slot, is counted by (C_L(z)): a branch contributes
(zC_{L-1}(z)), and an ordered sequence contributes

\[
 {1\over1-zC_{L-1}(z)}=C_L(z).                       \tag{2.1}
\]

Thus the number of choices with total size

\[
 |E(T)|=d+L+M=m
\]

is exactly ([z^M]C_L(z)), proving the count (0.2).

Every inserted forest branch disappears after at most (L) simultaneous
leaf-pruning rounds.  The forced terminal path disappears one edge per
round, and protects the terminal core vertex through the (L)-th round.
Consequently

\[
 \boxed{\partial^L D(T)=E_d.}                        \tag{2.2}
\]

The core path is the last root branch and its forced extension has no side
branches.  Hence the contour ends with exactly the descent along that path,
of length (d+L).  In particular all the terminal equality particles
needed in the (L) successive renormalizations are adjacent.  Also

\[
 \operatorname{ht}(D(T))=d+L,                       \tag{2.3}
\]

because every other inserted branch has height at most (L<d+L).

## 3. The ordered-particle flux lemma

The exact equality-particle skew system from (14.4) is

\[
 x_{\kappa_t}(t+1)=x_{\kappa_t}(t)+1,
 \qquad
 \lambda_t=x_{\kappa_t}(t)+1,                       \tag{3.1}
\]

with every other particle fixed.  Particle order is preserved.

We need the following iterated form of the adjacent-particle passage
principle.

### Lemma 3.1 (terminal tower flux)

Suppose a Dyck root (D) has (L) successive peak-pruning
renormalizations ending at (E), and its terminal descent supplies the
corresponding (L+1) adjacent particles.  Before any particle can travel
once around the outer coordinate circle, the first re-entry into the initial
omitted physical coordinate occurs exactly when particle (-L) of the
rank-(E) PBBS is selected for the second time.

#### Proof

At the outermost level, the distinguished particle moves into the returned
edge at time zero.  The only particle which can next enter that edge is its
immediate predecessor.  Because the two particles initially occupy adjacent
equality edges, the predecessor enters the returned edge on its second move:
its first move occupies the edge just vacated at time zero.  Particle order
prevents every other particle from bypassing it.

Apply the same statement inside the renormalized PBBS.  The second move of
that predecessor is driven by the second entry into the preceding physical
edge, which in turn is made by the next predecessor.  The terminal descent
makes each successive predecessor pair adjacent.  Iterating through (L)
renormalizations identifies the outer re-entry time with the second
selection of particle (-L) in the final compressed PBBS.

At every stage, the predecessor one level earlier makes its second move
strictly before the next predecessor, so the required edge has been vacated.
No other entry is possible by the no-overtaking property.  The only
alternative is for one particle to travel around the full outer coordinate
circle; this is excluded by the stated time range.  This proves the lemma.
\(\square\)

For the family of Section 2, the final compressed root is (E_d).  By
(1.4), particle (-L) is selected first at (2L) and for the second time
at

\[
 p+2L=2d+1+2L=2(d+L)+1.                              \tag{3.2}
\]

The outer circumference is (2m+1), and (d+L\le m-1), so (3.2) is
strictly below it.  Lemma 3.1 applies and proves both the exact consecutive
return statement (0.3) and, with (2.3), equality (0.4).

By the residence dictionary, this gap has projected residence

\[
 {g+1\over2}=d+L+1                                  \tag{3.3}
\]

and its quotient interval contains

\[
 k={g+3\over2}=d+L+2                                \tag{3.4}
\]

transition edges.

## 4. Spectral lower bound

The coefficient ([z^M]C_L(z)) is the number of length-(2M) walks from
zero to zero in the path graph on

\[
 \{0,1,\ldots,L\}.
\]

The adjacency eigenvalues and the squared first-coordinate weights are

\[
 2\cos {j\pi\over L+2},
 \qquad
 {2\over L+2}\sin^2 {j\pi\over L+2}
 \qquad(1\le j\le L+1).                             \tag{4.1}
\]

All terms are nonnegative after taking the even power (2M).  Keeping the
two terms (j=1,L+1), which have opposite eigenvalues of equal magnitude,
gives exactly (0.5).

## 5. Quotient interval packing

Discard the constructed starting roots which lie on quotient cycles of
length at most (H+1).  There are at most (Z_H) of them, because quotient
directed edges are indexed by Dyck roots.

Every remaining interval is nonwrapping and has the same (k) from (3.4).
On one directed quotient cycle, an interval beginning at edge (e) meets
only intervals whose starting edges are among the (k-1) preceding edges,
(e) itself, and the (k-1) following edges.  Its closed conflict
neighborhood therefore has size at most

\[
 2k-1=2d+2L+3.                                      \tag{5.1}
\]

Greedy selection on every quotient cycle produces at least the number of
remaining starts divided by (5.1).  This proves (0.6).

The same proof with variable interval lengths at most (H+1) shows that an
interval can conflict with starts in at most (2H+1) positions.  Summing
over cycles proves (0.9), and (0.10) follows immediately from (0.1).

## 6. Optimization

Take (d=L), so (M=m-2L).  From (0.5), the standard Catalan asymptotic,
and

\[
 \log\cos x=-{x^2\over2}+O(x^4),
\]

we obtain, uniformly for (L\asymp m^{1/3}),

\[
 \log{a_{m;L,L}\over B}
 \ge
 -2L\log4- {\pi^2m\over L^2}+O(\log m).             \tag{6.1}
\]

The right side is optimized at

\[
 L=\left({\pi^2m\over\log4}\right)^{1/3}+O(1),      \tag{6.2}
\]

where its main loss is

\[
 3(\pi\log4)^{2/3}m^{1/3}.                          \tag{6.3}
\]

If (H\gg m^{1/3}), the residence condition (2L\le H-1) holds.  If also
(H\log N=o(m)), Theorem 17.1 gives

\[
 Z_H\le(2H+2)N^{2H+2}=\exp(o(m)),                   \tag{6.4}
\]

whereas (0.5) is

\[
 \exp(m\log4-O(m^{1/3})).
\]

Thus subtracting (Z_H) and dividing by (4L+3) changes only the
(o(m^{1/3})) term.  Equations (6.1)--(6.4) prove (0.8).

## 7. Exact scope of the obstruction

The mountain tower proves three things and no more.

1. The height--gap inequality is sharp on an exponentially large symbolic
   family at every chosen tower height.
2. Short-return quotient packing has Catalan exponential growth; an
   exponential-rate large-deviation bound cannot reach Theorem 17.1's gate.
3. The numerical lower bound remains smaller than (B/N) by the factor

   \[
   N\exp(-\Theta(m^{1/3}))=o(1).
   \]

Accordingly this is an obstruction to entropy-only and pointwise-height
proofs, not a counterexample to the exact quotient residence conjecture.
The unresolved issue remains a (1/N)-scale correlation or clustering
theorem for the full recursive Dyck cocycle.
