# Long-run move-to-front atoms: a global reduction

## 1. Outcome

There is an exact local-to-global mechanism which removes the dynamic
move-to-front obstruction from the symmetric-chain programme.

Take a Johnson path

\[
 S_{t+1}=S_t-\{p_t\}+\{q_t\},\qquad |S_t|=m,
\]

and suppose every coordinate remains inside for more than \(d\) transitions
and outside for at least \(d\) transitions.  The next \(d\) departure coordinates and the preceding
\(d\) departure coordinates determine a radius-\(d\) symmetric chain
through \(S_t\).  These chains are exposed by an explicit sequence of
move-to-front states; the update at step \(t\) is simply the minimum of the
next chain.

When the Johnson path is obtained from a binary Gray cycle in an orientation
cube, a long run of distinct transition directions gives more.  Any block
of \(H\) starts with

\[
 H+d\le \rho
\]

produces \(H\) pairwise disjoint radius-\(d\) symmetric chains, where
\(\rho\) is the Gray code's run length.  Goddyn and Gvozdjak proved that an
\(s\)-cube has a Hamilton cycle with

\[
 \rho\ge s-3\log_2s.
\]

Thus, for every

\[
 h=O(\sqrt{m\log m})=o(m),
\]

there are move-to-front-realizable atoms containing \(H=\Theta(m)\)
disjoint symmetric chains of every radius \(0\le d\le h\).

Taking all coordinate permutations of one atom of each radius gives an
exact fractional perfect matching of the entire central band.  Therefore
there is no fractional or state-dynamic obstruction to an asymptotically
optimal construction.  The remaining all-dimensional theorem is a sharply
defined **integral atom-packing theorem**: round this symmetric fractional
matching while leaving only \(o(W)\) Boolean sets uncovered.

This reduction is independent of the failed fixed-transposition Haar lift
and of every finite \(k\) certificate.

## 2. Two-sided separated Johnson paths

Let \(k=2m\), and let

\[
 S_0,S_1,\ldots,S_L\in\binom{[2m]}m
\]

be a Johnson path.  Write its transitions uniquely as

\[
 S_{t+1}=S_t-\{p_t\}+\{q_t\},
 \qquad p_t\in S_t,\quad q_t\notin S_t.             \tag{2.1}
\]

Fix \(0\le d<m\).  Call an index \(t\) **two-sided \(d\)-buffered** if

\[
\begin{aligned}
 F_t&=\{p_t,p_{t+1},\ldots,p_{t+d-1}\}
       \subseteq S_t,\qquad |F_t|=d,\\
 &p_t,p_{t+1},\ldots,p_{t+d}
       \text{ are distinct members of }S_t,\\
 P_t&=\{p_{t-d},p_{t-d+1},\ldots,p_{t-1}\}
       \subseteq [2m]\setminus S_t,\qquad |P_t|=d.
\end{aligned}                                       \tag{2.2}
\]

Indices can be cyclic, or one may use only the interior of a linear path.
Condition (2.2) says exactly that the coordinates scheduled to leave during
the next \(d+1\) transitions are already present and distinct, while the
coordinates that left during the preceding \(d\) transitions are still
absent and distinct.

Put

\[
 L_t=S_t\setminus F_t.                              \tag{2.3}
\]

The associated chain is

\[
\begin{aligned}
\mathcal C_t^{(d)}:\quad
L_t
&\subset L_t+p_{t+d-1}
 \subset\cdots\subset L_t+F_t=S_t\\
&\subset S_t+p_{t-1}
 \subset\cdots\subset S_t+P_t.                    \tag{2.4}
\end{aligned}
\]

It is a saturated symmetric chain from rank \(m-d\) to rank \(m+d\).

## 3. Exact lookahead factorization

### Theorem 3.1 (canonical MTF realization)

Suppose every index in a path interval is two-sided \(d\)-buffered.  There
are ordered-partition states \(\Pi_t\) which expose
\(\mathcal C_t^{(d)}\) and satisfy

\[
 \Pi_{t+1}=M_{L_{t+1}}(\Pi_t).                      \tag{3.1}
\]

More precisely, the beginning of \(\Pi_t\) is

\[
 \bigl(
 L_t,
 \{p_{t+d-1}\},\ldots,\{p_t\},
 \{p_{t-1}\},\ldots,\{p_{t-d}\},
 \mathcal R_t
 \bigr),                                           \tag{3.2}
\]

where \(\mathcal R_t\) is some ordered partition of the remaining
coordinates.  The first state can be initialized with \(\mathcal R_t\) as
one block, so it has at most \(2d+2\) blocks.

#### Proof

The sets displayed before \(\mathcal R_t\) are disjoint by (2.2).  Their
prefix unions are exactly (2.4), so (3.2) exposes the desired chain.

We verify the transition.  Since \(p_{t+d}\) is present at time \(t\), while
the new arrival \(q_t\) cannot be scheduled to depart among the next \(d\)
steps, equations (2.1)--(2.3) give

\[
 L_{t+1}=(L_t-\{p_{t+d}\})\cup\{q_t\}.             \tag{3.3}
\]

Apply the update \(X=L_{t+1}\).  It becomes the new first block.  The
residue of the old first block is the singleton \(\{p_{t+d}\}\).  The
surviving future-departure blocks follow it in the old order, giving

\[
 \{p_{t+d}\},\{p_{t+d-1}\},\ldots,\{p_{t+1}\}.
\]

The just-departed singleton \(\{p_t\}\) is now the first upper block,
followed by

\[
 \{p_{t-1}\},\ldots,\{p_{t-d+1}\}.
\]

Any coordinate re-entering through \(L_{t+1}\) is simply deleted from its
old tail block.  The old block \(\{p_{t-d}\}\), which has just fallen out of
the displayed window, joins the unrestricted tail.  Thus the new state has
exactly the form (3.2) with \(t\) replaced by \(t+1\), proving (3.1) by
induction. \(\square\)

This theorem gives the missing converse to the residence-time obstruction:
long two-sided residence is not merely necessary for a deep MTF flag; it
has an explicit canonical factorization.

## 4. Orientation cubes and long-run Gray codes

Partition the coordinates into pairs

\[
 \{a_1,b_1\},\ldots,\{a_m,b_m\}.
\]

Fix a pair-type stratum of the middle layer: some pairs are full, the same
number are empty, and a set \(R\) of \(s\) pairs is split.  Its middle sets
are the vertices of the orientation cube \(Q_s\).  A flip in direction
\(i\in R\) replaces the currently present member of pair \(i\) by its
partner and is therefore a Johnson edge.

Let

\[
 v_0,v_1,\ldots,v_{2^s-1}
\]

be a cyclic Gray code of \(Q_s\), and let \(c_t\) be its transition
direction.  Its run length \(\rho\) means that every \(\rho\) consecutive
transition directions are distinct.

### Lemma 4.1 (run length implies buffering)

For every \(d<\rho\), the induced Johnson cycle is two-sided
\(d\)-buffered.

#### Proof

During any \(d+1\) consecutive transitions, no pair direction repeats.
Consequently the current member of each pair scheduled to flip in the next
\(d\) steps is already present, remains present until its unique flip, and
the corresponding departure coordinates are distinct.  Dually, a member
which departed during the preceding \(d\) transitions has not yet had its
pair flipped again, so it remains absent.  This is exactly (2.2). \(\square\)

Theorem 3.1 therefore turns every sufficiently short arc of a long-run Gray
cycle into an MTF state path.  The chains inside such an arc are also
automatically disjoint.

### Theorem 4.2 (long-run atom lemma)

Let \(I\) be \(H\) consecutive starts in the induced Johnson cycle.  If

\[
 H+d\le\rho,                                        \tag{4.1}
\]

then the \(H\) chains

\[
 \{\mathcal C_t^{(d)}:t\in I\}                     \tag{4.2}
\]

are pairwise vertex-disjoint.  Together they form one genuine MTF state
path, initialized in at most \(2d+2\) entries and continued with one entry
per additional chain.

#### Proof

The MTF statement is Theorem 3.1.  It remains to prove disjointness.

At lower depth \(1\le q\le d\), the member of \(\mathcal C_t^{(d)}\) of rank
\(m-q\) is

\[
 S_t\setminus\{p_t,p_{t+1},\ldots,p_{t+q-1}\}.     \tag{4.3}
\]

Take \(t<u\) in \(I\).  Pair direction \(c_t\) is empty in (4.3).  It was
flipped at transition \(t\), and it cannot occur again before transition
\(u+q\), because the interval from \(t\) through \(u+q-1\) has fewer than
\(H+d\le\rho\) terms.  Therefore the rank-\((m-q)\) member belonging to
start \(u\) contains one member of pair \(c_t\), and the two targets differ.

At upper depth \(1\le q\le d\), the target is

\[
 S_t\cup\{p_{t-1},p_{t-2},\ldots,p_{t-q}\}.        \tag{4.4}
\]

Now use direction \(c_{u-1}\).  It is full in the target (4.4) belonging to
\(u\).  It cannot occur in the preceding \(q\)-window belonging to \(t\),
again by (4.1), so the target belonging to \(t\) contains only one member of
that pair.  Hence the upper targets differ as well.  Middle targets are the
distinct vertices \(S_t\), and targets at different ranks cannot coincide.
This proves pairwise disjointness. \(\square\)

Goddyn and Gvozdjak's long-run theorem supplies

\[
 \rho(s)\ge s-3\log_2s.                             \tag{4.5}
\]

See L. Goddyn and P. Gvozdjak, *Binary Gray Codes with Long Bit Runs*,
Electronic Journal of Combinatorics 10 (2003), R27,
<https://doi.org/10.37236/1720>.

Thus, in an all-split stratum \(Q_m\), for every
\(h=o(m)\) one may choose a common

\[
 H=m-3\log_2m-h=\Theta(m)                           \tag{4.6}
\]

and obtain an atom of \(H\) disjoint chains for every radius
\(0\le d\le h\).

## 5. Exact OR-array accounting

Call any family (4.2), together with its MTF path, a radius-\(d\)
**long-run atom**.

### Theorem 5.1 (atom-packing reduction)

Suppose a collection of \(p\) long-run atoms contains \(N\) pairwise
disjoint symmetric chains, and their union misses \(q\) nonempty Boolean
sets.  If atom \(j\) has radius \(d_j\), then

\[
 \nu(2m)\le
 N+\sum_{j=1}^{p}(2d_j+1)+q.                        \tag{5.1}
\]

In particular, if

\[
 N=W-o(W),\qquad q=o(W),\qquad
 \sum_jd_j=o(W),                                    \tag{5.2}
\]

then

\[
 \nu(2m)=(1+o(1))W.                                 \tag{5.3}
\]

#### Proof

For each atom, initialize its first state by updating its at most
\(2d_j+2\) blocks in reverse order.  If it contains \(H_j\) chains, its
remaining \(H_j-1\) states cost one update each by Theorem 3.1.  Thus its
total cost is at most

\[
 H_j+2d_j+1.
\]

Sum over the atoms and append each of the \(q\) missed nonempty sets
literally.  Previously obtained interval witnesses remain valid.  This
proves (5.1), and (5.2) gives (5.3). \(\square\)

For atoms of common length \(H=\Theta(m)\) and radii at most
\(h=O(\sqrt{m\log m})\), the reset excess per chain is

\[
 O(h/H)=o(1).                                       \tag{5.4}
\]

The dynamic cost of joining the atoms is therefore negligible.

## 6. An exact fractional tiling

Let

\[
 N_q=\binom{2m}{m-q},\qquad 0\le q\le h.           \tag{6.1}
\]

Define truncated symmetric-chain radius counts by

\[
 c_d=N_d-N_{d+1}\quad(0\le d<h),qquad c_h=N_h.    \tag{6.2}
\]

They telescope:

\[
 \sum_{d=q}^{h}c_d=N_q.                             \tag{6.3}
\]

Fix one length-\(H\) long-run atom \(\mathcal A_d\) of every radius
\(d\le h\), with \(H+h\le m-3\log_2m\).  Let
\(\mathcal O_d\) be its orbit under all coordinate permutations of
\([2m]\).

### Theorem 6.1 (symmetric fractional perfect matching)

The hypergraph on the central band

\[
 \bigcup_{q=-h}^{h}\binom{[2m]}{m+q}               \tag{6.4}

whose hyperedges are the atoms in the orbits \(\mathcal O_d\) has an exact
fractional perfect matching.  The total fractional mass assigned to orbit
\(\mathcal O_d\) is

\[
 c_d/H.                                             \tag{6.5}
\]

#### Proof

Distribute the mass (6.5) uniformly over the orbit.  Every radius-\(d\)
atom contains exactly \(H\) vertices in each rank \(m-q\) and \(m+q\) for
\(0\le q\le d\), and none at greater depth.  The symmetric group is
transitive on every Boolean rank.  Hence a fixed vertex at depth \(q\)
receives from orbit \(d\) the fractional weight

\[
 \frac{c_d}{H}\frac{H}{N_q}=rac{c_d}{N_q}.
\]

Summing over \(d\ge q\) and using (6.3) gives weight one. \(\square\)

This proves three useful facts simultaneously:

1. the forced SCD radius distribution is exactly compatible with long-run
   MTF atoms;
2. every central rank is balanced, not merely the middle layer; and
3. the only missing step is integral packing, not a counting or divisibility
   correction.

## 7. The precise all-dimensional theorem left

Choose, for example,

\[
 h=\left\lceil\sqrt{m\log m}\right\rceil,
 \qquad H=m-3\log_2m-h.                             \tag{7.1}
\]

The number of Boolean sets outside the band (6.4) is

\[
 2\sum_{r=0}^{m-h-1}\binom{2m}{r}-1=o(W),          \tag{7.2}
\]

by the standard binomial tail estimate.  Theorem 5.1 and Theorem 6.1 reduce
asymptotic optimality to one statement.

> **Long-run atom packing theorem.**  From the coordinate-permutation
> orbits \(\mathcal O_0,\ldots,\mathcal O_h\), choose pairwise disjoint
> atoms whose chains leave only \(o(W)\) vertices of the central band
> uncovered and whose number is \(O(W/H)\).

If this holds, the chosen atoms contain \(W-o(W)\) chains, their total reset
cost is

\[
 O\!\left(\frac{Wh}{H}\right)=o(W),                \tag{7.3}
\]

and (7.2) handles the literal tails.  Therefore

\[
 \nu(2m)=(1+o(1))W(2m).                             \tag{7.4}
\]

The ordinary one-bit lift then gives the same asymptotic result in odd
dimension, because

\[
 \frac{2W(2m)}{W(2m+1)}=1+O(1/m).                  \tag{7.5}
\]

The atom-packing theorem is stronger than an ordinary almost-perfect
matching statement: the uncovered count must be \(o(W)\), not merely an
\(o(1)\) fraction of the whole central band, whose size is
\(\Theta(\sqrt m\,W)\).

## 8. What has and has not been solved

The following points are now theorems:

* two-sided long residence has an explicit MTF factorization;
* a long-run cube block gives many disjoint symmetric chains;
* blocks of linear length exist in every dimension;
* their reset/interface cost is \(o(W)\); and
* their full permutation orbit has the exact fractional SCD ledger.

The unresolved point is the integral rounding of that fractional ledger.
Adjacent members of one symmetric chain create fractional codegrees of
order \(1/m\), while one atom has growing size
\(\Theta(Hh)\).  Consequently the desired rounding is not an immediate
fixed-uniformity Pippenger--Rödl application.  The internal chains must be
exposed in the rounding argument rather than treating an atom as an
unstructured hyperedge.

There is also a genuine architecture warning.  If one insists on using one
fixed coordinate pairing for the entire construction, the pair-type capacity
bound in `FIXED_PAIR_RESIDUAL_SCD.md` misses almost all targets at depths
\(q/\sqrt m\to\infty\).  Since (7.1) lies in that range, an integral proof
must use the full coordinate-permutation reservoir (or an equivalent family
of many pairings).  The symmetric orbit in Theorem 6.1 already incorporates
exactly that necessary globalization.

So the big-picture frontier is no longer “find a clever finite central
path.”  It is:

\[
 \boxed{
 \text{round a symmetric fractional SCD made of long-run MTF atoms}
 \text{ while preserving their internal path bundles}.}
\]
