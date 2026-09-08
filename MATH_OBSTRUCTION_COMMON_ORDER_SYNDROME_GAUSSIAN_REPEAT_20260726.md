# Common-order syndrome factors have a Gaussian-window repeat obstruction

Date: 2026-07-26

Method: pure mathematics only.

## 0. Verdict

The exact repeat formula for the global \(Q_D\) syndrome packing cannot
be made \(o(W)\) at a fixed Gaussian depth by choosing the syndrome map,
the antipodal coset vector, affine conjugates, or rank-twisted packet
labels.

The obstruction is simpler and stronger than a bad covariance estimate.
In one \(Q_D\) packet whose cycles are all translates of one
doubled-permutation word, a depth-\(q\) window uses one of only \(D\)
cyclic interval supports.  For a fixed support, at most \(2^{D-q}\)
literal lower targets are possible.  Hence one complete packet exposes at
most

\[
                         D\,2^{D-q}                 \tag{0.1}
\]

distinct rank-\((m-q)\) targets, independently of every syndrome choice.

If such packets cover \(G=W-o(W/H)\) owners, their total distinct target
coverage at depth \(q\) is at most

\[
                         {D\over2^q}G.              \tag{0.2}
\]

For

\[
                         q=A\sqrt m+O(1),\qquad A>0, \tag{0.3}
\]

we have

\[
 {D\over2^q}=o(1),\qquad
 {2m\choose m-q}=(e^{-A^2}+o(1))W.                 \tag{0.4}
\]

Therefore the number of missing lower targets is at least

\[
                         (e^{-A^2}-o(1))W.          \tag{0.5}
\]

Equivalently, the repeat excess above the forced layer-size overload is
at least the same quantity.  This already refutes the requested
\(o(W)\) conclusion for one fixed Gaussian window; no diagonalization in
\(q\) is possible.

Random linear codes and character sums cannot help after conditioning on
exact owner factorhood, because (0.1) holds pointwise for every code and
every physical conjugate.  An escape must abandon the one-common-order
translation factor.  At Gaussian depth, a successful \(Q_D\) factor must
display \(\Omega(2^q)\) distinct physical \(q\)-window supports per
packet on average.  The syndrome factor displays only \(D\).

## 1. Setup and path-hitting normal form

Let \(P\) be one physical \(Q_D\) packet inside a rank-twisted status
cell.  Its \(D\) active axes are disjoint physical pairs.  All other
coordinates, pair statuses, selector labels, and exterior tags are frozen
on \(P\).

Let

\[
                         \Pi=(\pi_1,\ldots,\pi_D)    \tag{1.1}
\]

be a permutation of the active axes.  Assume the packet is factored into
kernel translates of the isometric cycle with word \(\Pi\Pi\).  The
syndrome construction gives \(2^D/(2D)\) cycles and partitions all
\(2^D\) owners exactly.

Use the literal path-hitting formulation.  A lower rank-\((m-q)\) target
\(T\) is produced by a start owner \(X\) precisely when the next
\(q\) Johnson moves stay in the up-set of \(T\); then \(T\) is the
intersection of the \(q+1\) consecutive middle owners.  Because the
window is a geodesic, its \(q\) directions are distinct.

For a window with direction support \(J\subseteq[D]\):

1. the intersection contains neither endpoint of every active physical
   pair in \(J\);
2. it contains the selected endpoint of every active pair outside \(J\);
3. all frozen exterior coordinates are fixed by the packet.

Thus the literal target records \(J\) as its exact set of empty active
pairs, and is otherwise determined by the \(D-q\) outside orientations.
Consequently:

### Lemma 1.1 (one-support capacity)

For one physical \(Q_D\) packet and one fixed \(q\)-set \(J\) of active
axes, there are at most

\[
                              2^{D-q}                \tag{1.2}
\]

distinct lower targets whose deleted direction support is \(J\).

The analogous upper statement holds with the pairs in \(J\) full rather
than empty.

This count uses literal physical targets.  No abstract compiler,
syndrome, phase, or tag multiplicity increases it.

## 2. Only \(D\) supports occur in a common-order factor

For \(0\le j<D\), put

\[
 J_j=\{\pi_{j+1},\ldots,\pi_{j+q}\},                \tag{2.1}
\]

with indices modulo \(D\).  The support of a \(q\)-window starting at
phase \(j\) is \(J_j\), and the antipodal phase \(j+D\) has the same
support.  Since \(q<D\), the \(D\) cyclic sets \(J_j\) are distinct.
Every translated cycle has the same phase direction word, so no other
support occurs anywhere in the packet factor.

Lemma 1.1 immediately gives:

### Lemma 2.1 (common-order packet capacity)

Let \({\cal C}_{P,q}^-\) be the set of distinct lower depth-\(q\)
targets produced by the complete common-order syndrome factor of \(P\).
Then

\[
                         |{\cal C}_{P,q}^-|
 \le D\,2^{D-q}.                                    \tag{2.2}
\]

The same bound holds for upper targets.

The statement remains true after:

1. replacing the syndrome map by any other map for which the translates
   factor \(Q_D\);
2. changing the antipodal syndrome or coset representative;
3. applying an arbitrary affine physical conjugate to the whole packet;
4. changing the rank-twisted matching and frozen status label of the
   packet; or
5. choosing a different common direction order in every packet.

Each operation changes target names but leaves the count of window
supports at \(D\).

## 3. Recovery from the exact syndrome repeat formula

The same obstruction is visible term by term in the exact formula from
the global packing theorem.  Write \(D=2^s\), let
\(\phi:\mathbb F_2^D\to\Sigma\) be the syndrome map, let \(v\) be the
antipodal coset vector, and put

\[
 V_j=\phi(\mathbb F_2^{J_j}),\qquad h_j=\dim V_j,
 \qquad
 c_j=
 \begin{cases}
 1,&v\in V_j,\\
 2,&v\notin V_j.
 \end{cases}                                        \tag{3.1}
\]

The exact number of distinct targets in the packet is

\[
 |{\cal C}_{P,q}^-|
 =\sum_{j=0}^{D-1}
 c_j\,2^{D-(s+1)-q+h_j}.                            \tag{3.2}
\]

If \(c_j=1\), then \(h_j\le s+1\).  If \(c_j=2\), then
\(v\notin V_j\), so \(V_j\ne\Sigma\) and \(h_j\le s\).  In either case,

\[
 c_j\,2^{D-(s+1)-q+h_j}\le2^{D-q}.                 \tag{3.3}
\]

Summing (3.3) gives (2.2).  The exact within-packet repeat count therefore
satisfies

\[
 \begin{aligned}
 {\cal R}_{P,q}^-
 &=2^D-|{\cal C}_{P,q}^-|\\
 &\ge2^D\left(1-{D\over2^q}\right).                 \tag{3.4}
 \end{aligned}
\]

This lower bound includes all inherited-payload and cross-translate
repeats in the packet.  Optimizing the ranks \(h_j\), the coset cases
\(c_j\), or their character sums can at best attain the right side of
(2.2); it cannot change the factor \(D/2^q\).

## 4. Summing over the exact rank-twisted owner packing

Let \({\cal P}\) be the owner-disjoint family of \(Q_D\) packets.  Put

\[
                         G=|{\cal P}|\,2^D
                          =W-o(W/H).                 \tag{4.1}
\]

The target sets belonging to different packets may overlap.  Such
overlap only decreases their union.  By Lemma 2.1,

\[
 \begin{aligned}
 \left|\bigcup_{P\in{\cal P}}{\cal C}_{P,q}^-\right|
 &\le\sum_{P\in{\cal P}}|{\cal C}_{P,q}^-|\\
 &\le |{\cal P}|D2^{D-q}\\
 &={D\over2^q}G.                                    \tag{4.2}
 \end{aligned}
\]

This is valid for arbitrary, dependently chosen syndrome maps, coset
vectors, direction orders, affine conjugates, and rank-twisted cell
labels in the different packets.

The global repeat count is

\[
 {\cal R}_q^-
 =G-\left|\bigcup_{P\in{\cal P}}{\cal C}_{P,q}^-\right|,
                                                               \tag{4.3}
\]

so (4.2) also gives

\[
                         {\cal R}_q^-
 \ge G\left(1-{D\over2^q}\right).                  \tag{4.4}
\]

Owner leave cannot repair this bound.  Even if every one of the
\(o(W/H)\) omitted owners were appended as a separate useful occurrence
at this depth, it could add only \(o(W/H)\) distinct targets.

## 5. The fixed Gaussian window

Let

\[
                         q=A\sqrt m+O(1)             \tag{5.1}
\]

for a fixed \(A>0\).  Since \(D=\Theta(m)\),

\[
                         {D\over2^q}
 \le\exp(O(\log m)-A(\log2)\sqrt m)=o(1).            \tag{5.2}
\]

The lower target layer has size

\[
                         N_q={2m\choose m-q}.        \tag{5.3}
\]

Relative to \(W={2m\choose m}\),

\[
 {N_q\over W}
 =\prod_{i=0}^{q-1}{m-i\over m+i+1}.                \tag{5.4}
\]

Taking logarithms and using \(q=O(\sqrt m)\),

\[
 \begin{aligned}
 \log{N_q\over W}
 &=-{1\over m}\sum_{i=0}^{q-1}(2i+1)
   +O\!\left({q\over m}+{q^3\over m^2}\right)\\
 &=-{q^2\over m}+o(1)
 =-A^2+o(1).                                        \tag{5.5}
 \end{aligned}
\]

Hence

\[
                         N_q=(e^{-A^2}+o(1))W.       \tag{5.6}
\]

Combining (4.2), (5.2), and (5.6), the number \(M_q^-\) of missing lower
targets satisfies

\[
 \boxed{
 M_q^-
 \ge N_q-{D\over2^q}G-o(W/H)
 =(e^{-A^2}-o(1))W.}                                \tag{5.7}
\]

This proves the one-window obstruction.

## 6. Exact repeat excess

The total occurrence count is \(G\), while the target layer has only
\(N_q\) vertices.  Thus \(G-N_q\) repeats are forced even under perfect
coverage.  The meaningful discrepancy is the repeat excess

\[
                         {\cal E}_q^-
 ={\cal R}_q^--(G-N_q).                              \tag{6.1}
\]

Using (4.3),

\[
 {\cal E}_q^-
 =N_q-\left|\bigcup_{P\in{\cal P}}{\cal C}_{P,q}^-\right|
 =M_q^-                                             \tag{6.2}
\]

up to the explicitly appended owner-leave reserve.  Therefore (5.7)
gives

\[
                         {\cal E}_q^-
 \ge(e^{-A^2}-o(1))W.                               \tag{6.3}
\]

So both interpretations of the requested estimate fail:

1. the raw inherited-payload plus cross-translate repeat count is
   \((1-o(1))W\) by (4.4); and
2. after subtracting the unavoidable layer-size overload, the excess is
   still \((e^{-A^2}-o(1))W\).

The obstruction is not one of the \(O(H/D)\) controlled seams.

## 7. Why conditioning and random codes cannot help

Suppose that, before choosing each packet factor, one samples:

1. a random linear syndrome map;
2. a random antipodal vector or quotient identification;
3. a random physical coordinate permutation and translation;
4. a random rank-twisted cell label; and
5. arbitrary dependencies between different packets.

Condition on the event that every sampled object gives an exact
owner-factor of its \(Q_D\).  Lemma 2.1 holds for every point of this
conditioned sample space.  Therefore

\[
 \Pr\!\left(
 |{\cal C}_{P,q}^-|\le D2^{D-q}
 \ \text{for every }P
 \,\middle|\,
 \text{exact factorhood}\right)=1.                  \tag{7.1}
\]

Taking expectations, second moments, Fourier transforms, or character
sums after this conditioning cannot improve (4.2).  Those methods can
redistribute the at most \(D2^{D-q}\) targets or reduce overlap between
different packets; they cannot create a missing window support.

## 8. Necessary order diversity for an escape

The counting argument extends beyond syndrome kernels.  In an arbitrary
cycle factor of a physical \(Q_D\) packet, let

\[
 {\cal J}_{P,q}
 =\{J\subseteq[D]:J\text{ occurs as the physical direction support
 of a consecutive }q\text{-window}\}.               \tag{8.1}
\]

Lemma 1.1 gives

\[
                         |{\cal C}_{P,q}^-|
 \le |{\cal J}_{P,q}|\,2^{D-q}.                     \tag{8.2}
\]

If a family of \(Q_D\) packets is to cover
\((1-o(1))N_q=(e^{-A^2}+o(1))W\) targets at the Gaussian depth, then
(8.2) and \(G=(1-o(1))W\) force

\[
 {1\over|{\cal P}|}\sum_{P\in{\cal P}}|{\cal J}_{P,q}|
 \ge(e^{-A^2}-o(1))\,2^q.                           \tag{8.3}
\]

This is the exact diversity threshold.  A common doubled-permutation
order has

\[
                         |{\cal J}_{P,q}|=D,         \tag{8.4}
\]

which is exponentially too small at \(q=A\sqrt m\).

More generally, if one packet factor is assembled from at most \(K\)
common-order resolution classes, then

\[
                         |{\cal J}_{P,q}|\le KD,     \tag{8.5}
\]

so a necessary condition is

\[
                         K\ge
 (e^{-A^2}-o(1)){2^q\over D}.                        \tag{8.6}
\]

Thus polynomially many affine conjugate orders per packet still fail.
The next viable owner theorem must incorporate exponentially many
direction orders **within the same exact owner factor**, through
owner-preserving trades or a genuinely nonparallel recursive resolution.
Changing only \(\phi\), \(v\), or packet labels cannot do this.

## 9. Final theorem

### Theorem 9.1 (Gaussian-window no-go for global common-order syndrome packing)

Let

\[
 \sqrt m\ll H=o(m),\qquad D=\Theta(m),
\]

and let \(q=A\sqrt m+O(1)\le H\) for fixed \(A>0\).  Partition
\(G=W-o(W/H)\) middle owners into physical \(Q_D\) packets.  In every
packet choose arbitrarily a syndrome map, antipodal coset vector,
rank-twisted frame, affine physical conjugate, and doubled-permutation
order, and factor that packet by translates of the chosen common-order
cycle.

Then the number of distinct lower depth-\(q\) targets covered by all
packets is \(o(W)\), and

\[
                         M_q^-\ge(e^{-A^2}-o(1))W.   \tag{9.1}
\]

The repeat excess has the same lower bound.  Hence the aggregate literal
target loss cannot be \(o(W)\), already for this one depth.

The obstruction is invariant under all choices named above and survives
arbitrary dependence and conditioning on exact owner factorhood.
\(\square\)

## 10. Scope update: the diverse-order compiler escapes this theorem

The subsequent theorem

\[
\texttt{MATH\_THEOREM\_DIVERSE\_ORDER\_COMPILER\_PACKET\_FACTOR\_20260726.md}
\]

uses the parity-complete recursive compiler rather than translates of one
common direction order.  Its trace map is injective on all \(2^R\)
packet owners through the protected range and consequently exposes at
least \(2^q\) physical \(q\)-window supports.  It therefore satisfies the
necessary diversity threshold (8.3) and is not covered by Theorem 9.1.

The remaining discrepancy for that construction is purely cross-packet.
It is audited in

\[
\texttt{MATH\_AUDIT\_DIVERSE\_ORDER\_COMPILER\_CROSS\_PACKET\_COVARIANCE\_20260726.md}.
\]
