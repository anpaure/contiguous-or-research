# Clustered dominance seams do not escape critical PBBS residence saturation

Date: 2026-07-26

Method: pure mathematics only.

## 0. Verdict

Write

\[
 N=2m+1,\qquad B_m=\operatorname {Cat}_m,\qquad W=NB_m,
\]

and, for fixed \(A>0\), put \(H=\lceil A\sqrt m\rceil\).  The
multi-cut dominance theorem is an exact sufficient replacement for the
separate-cut ledger: a quotient cut cluster of span \(S\), with

\[
 3H+S\le m+1,
\]

has charged auxiliary length

\[
 q_H(S)=7H+3S-3.                                  \tag{0.1}
\]

If the optimized total quotient charge is \(o_A(B_m)\), then its \(N\)
spatial lifts cost \(o_A(W)\), and the usual Gaussian diagonalization
proves coefficient one.

There is, however, an exact obstruction at the critical residence scale.
For every projected-edge-disjoint packing \(\mathcal P\) of PBBS return
traces of residence at most \(H\), every cut transversal and every
admissible clustering obey

\[
 \boxed{
   \sum_J q_H(S_J)\ \ge\
   \sum_{I\in\mathcal P}|E(I)|.}                  \tag{0.2}
\]

Thus the clustered charge dominates the maximum **packed trace mass**,
not merely the number of packed returns.

The critical-saturation theorem in
`MATH_AUDIT_CMS_AND_CRITICAL_RESIDENCE_SATURATION_20260726.md` says that
failure of \((\mathrm{ST}_A)\) supplies a simple fixed-core packing whose
traces cover \(\Omega_A(B_m)\) quotient edges.  Applying (0.2) gives

\[
 \boxed{
   \overline\nu_H\not=o_A(B_m/\sqrt m)
   \quad\Longrightarrow\quad
   \inf\sum_J q_H(S_J)=\Omega_A(B_m).}            \tag{0.3}
\]

Consequently the additive clustered-seam route does not bypass a genuine
critical failure of \((\mathrm{ST}_A)\).  It converts the old independent
\(HJ\) toll into a thickened active-span toll, but a critical double-deck
packing forces that toll to have positive density.

The weakest scalar statistic for the established clustered compiler is

\[
 \boxed{
 \Theta_{m,H}:=\inf_{Q,\Pi}
       \left(H|\Pi|+\sum_{J\in\Pi}S_J\right),}    \tag{0.4}
\]

where \(Q\) ranges over short-residence cut transversals and \(\Pi\) over
their admissible clusterings.  Its vanishing is equivalent, up to absolute
constants, to the formerly stated clustered gate \((\mathrm{CS}_A)\).
At critical saturation (0.3) forces \(\Theta_{m,H}=\Omega_A(B_m)\).
Hence the weakest remaining escape in that branch is no longer a cut
statistic: it is an \(\Omega(B_m)\) in-place baseline-replacement credit,
or an equally large saving from PBBS-specific coincidence of witnesses.

## 1. The optimized clustered functional

Let \(\mathscr C_m\) be the disjoint union of the cyclic quotient edge
sets of the step-two PBBS permutation.  Its total number of edges is
\(B_m\).  Let \(\mathcal R_H\) be the family of all nonwrapping quotient
residence intervals of residence at most \(H\).  A set of quotient edges
\(Q\) is a **short-residence transversal** when

\[
 Q\cap E(I)\ne\varnothing
 \qquad(I\in\mathcal R_H).                        \tag{1.1}
\]

Partition the cuts on each quotient cycle into clusters.  A cluster is
admissible if it is contained in a proper cyclic arc whose leftmost and
rightmost cuts have span \(S\) satisfying

\[
 0\le S\le m+1-3H.                               \tag{1.2}
\]

For a transversal \(Q\) and an admissible partition \(\Pi\), define

\[
 \Phi_H(Q,\Pi)
   :=\sum_{J\in\Pi}(7H+3S_J-3),                  \tag{1.3}
\]

\[
 \Theta_H(Q,\Pi)
   :=H|\Pi|+\sum_{J\in\Pi}S_J.                  \tag{1.4}
\]

Let \(\Phi_{m,H}\) and \(\Theta_{m,H}\) be the respective infima over
all such \((Q,\Pi)\).  Empty inactive cycles contribute zero.

### Lemma 1.1 (exact equivalence of the two cluster statistics)

For every \(H\ge1\),

\[
 \boxed{
  3\Theta_{m,H}\le\Phi_{m,H}\le7\Theta_{m,H}.}  \tag{1.5}
\]

In particular,

\[
 \Phi_{m,H}=o(B_m)\quad\Longleftrightarrow\quad
 \Theta_{m,H}=o(B_m).                            \tag{1.6}
\]

#### Proof

For every fixed pair \((Q,\Pi)\),

\[
 \Phi_H(Q,\Pi)
  =(7H-3)|\Pi|+3\sum_J S_J.
\]

Since \(3H\le7H-3\le7H\) for \(H\ge1\),

\[
 3\left(H|\Pi|+\sum_J S_J\right)
 \le\Phi_H(Q,\Pi)
 \le7\left(H|\Pi|+\sum_J S_J\right).
\]

Taking infima proves (1.5), and (1.6) follows. \(\square\)

Thus the exact content of \((\mathrm{CS}_A)\) is the simultaneous
existence of transversals and clusterings with

\[
 |\Pi|=o_A(B_m/H),\qquad \sum_{J\in\Pi}S_J=o_A(B_m).          \tag{1.7}
\]

The first term is a component count; the second is active span.  Calling
only the second one the obstruction can hide the case of many singleton
clusters, so (0.4) is the invariant scalar formulation.

## 2. Coefficient one from vanishing thick active span

### Theorem 2.1 (clustered-seam sufficient theorem)

Suppose that for every fixed \(A>0\), with
\(H=\lceil A\sqrt m\rceil\), one can choose a deck-invariant quotient
transversal and admissible clustering such that

\[
 \Theta_{m,H}=o_A(B_m).                           \tag{2.1}
\]

Then

\[
 \nu(k)\le(1+o(1))
       \binom{k}{\lfloor k/2\rfloor}.             \tag{2.2}
\]

#### Proof

Keep only the nonnegative endpoint-capped erosion letters on active
physical paths.  Their total length is the original physical owner mass
\(W\).  For each quotient cluster use the virtual-cut lower dominance
staircase and the chronological upper halo from the clustered endpoint
and seam theorem.  Its \(N\) spatial lifts have total length
\(Nq_H(S)\).  Inactive projected cycles use cyclic erosion; the standard
cycle ledger adds at most \(2HB_m\) physical letters.  Hence

\[
 L_H\le W+2HB_m+N\Phi_{m,H}.                      \tag{2.3}
\]

Lemma 1.1 and (2.1) give \(N\Phi_{m,H}=o_A(NB_m)=o_A(W)\), while

\[
 \frac{2HB_m}{W}=\frac{2H}{2m+1}=O_A(m^{-1/2}).  \tag{2.4}
\]

Thus every fixed Gaussian central band has a literal word of length
\(W+o_A(W)\).  Diagonalize through integer \(A\to\infty\) slowly, append
the audited product-SCD outer tail, and apply the trimmed one-coordinate
lift in even dimension.  These are exactly the final steps in the
dominance-seam reduction, and prove (2.2). \(\square\)

No packing estimate was used in this theorem.  It records the strongest
conclusion available from the multi-cut chart itself.

## 3. A packed-trace lower certificate for every clustering

For a return interval \(I\), let \(E(I)\) be its quotient transition-edge
support.  Residence at most \(H\) gives

\[
 |E(I)|\le H+1,                                  \tag{3.1}
\]

with the harmless \(+1\) allowing either convention for the two endpoint
edges.  Define the maximum packed trace mass

\[
 \Lambda_{m,H}:=\max_{\mathcal P}
     \sum_{I\in\mathcal P}|E(I)|,                \tag{3.2}
\]

where \(\mathcal P\subseteq\mathcal R_H\) ranges over families with
pairwise disjoint quotient edge supports.

### Lemma 3.1 (intervals assigned to one cut cluster)

Let \(\mathcal P\) be projected-edge-disjoint, let \(Q\) meet every
member of \(\mathcal P\), and assign to each \(I\in\mathcal P\) one edge

\[
 q(I)\in Q\cap E(I).                             \tag{3.3}
\]

If the assigned cuts belonging to one cluster \(J\) have span at most
\(S_J\), then

\[
 \boxed{
  \sum_{I:q(I)\in J}|E(I)|
    \le S_J+2(H+1).}                             \tag{3.4}
\]

#### Proof

Use a proper carrier arc for \(J\) and cut the cycle open outside that
arc.  Order the assigned cuts linearly.  Because the supports in
\(\mathcal P\) are disjoint cyclic intervals, their order is the order of
their assigned cuts.  Every support except possibly the supports
containing the first and last assigned cuts lies wholly between those two
cuts: otherwise it would cross one of the two extreme supports.  The
internal supports are disjoint and therefore have total length at most
the separation of the extreme cuts, which is at most \(S_J\).  Each of
the two extreme supports has length at most \(H+1\) by (3.1).  This proves
(3.4).  The cases of zero, one, or two assigned intervals are included
directly. \(\square\)

### Theorem 3.2 (packed trace mass obstructs clustered seams)

For every \(m\) and \(H\ge2\),

\[
 \boxed{
   \Phi_{m,H}\ge\Lambda_{m,H},\qquad
   \Theta_{m,H}\ge\frac17\Lambda_{m,H}.}        \tag{3.5}
\]

#### Proof

Fix a transversal \(Q\), an admissible clustering \(\Pi\), and a packing
\(\mathcal P\).  Make the assignment (3.3).  Edge-disjointness ensures
that no cut is assigned twice.  Lemma 3.1 and \(H\ge2\) give, cluster by
cluster,

\[
 \begin{aligned}
 \sum_{I:q(I)\in J}|E(I)|
 &\le S_J+2(H+1)\\
 &\le 7H+3S_J-3=q_H(S_J),
 \end{aligned}                                   \tag{3.6}
\]

because the difference in the second line is \(5H+2S_J-5\ge0\).
Summing over clusters proves

\[
 \Phi_H(Q,\Pi)\ge\sum_{I\in\mathcal P}|E(I)|.
\]

Take first the maximum over \(\mathcal P\), then the infimum over
\((Q,\Pi)\), to obtain the first assertion of (3.5).  The second follows
from the upper inequality \(\Phi_{m,H}\le7\Theta_{m,H}\) in Lemma 1.1.
\(\square\)

This lower certificate uses only interval chronology and edge
disjointness.  Freedom to choose the cut anywhere in a return, the
fixed-core open-wreath decoration, and alternative ambient completions do
not affect it.

## 4. Critical failure of \((\mathrm{ST}_A)\) forces positive cluster cost

The quotient form of the separate-cut condition is

\[
 \overline\nu_H=o_A(B_m/\sqrt m).                 \tag{ST_A}
\]

Suppose it fails for one fixed \(A\).  Along a subsequence there is
\(\varepsilon>0\) such that

\[
 \overline\nu_H\ge\varepsilon B_m/\sqrt m.       \tag{4.1}
\]

The critical double-deck saturation theorem applies to a maximizing
packing in (4.1).  After an absolute factor-two loss it supplies constants
\(a,c>0\) and a projected-edge-disjoint family \(\mathcal Q\) of simple
fixed-core sectors satisfying

\[
 |\mathcal Q|\ge cB_m/\sqrt m,                   \tag{4.2}
\]

\[
 a\sqrt m\le |E(I)|\le H+1
 \qquad(I\in\mathcal Q),                         \tag{4.3}
\]

and, most importantly,

\[
 \left|\bigcup_{I\in\mathcal Q}E(I)\right|
   =\sum_{I\in\mathcal Q}|E(I)|
   \ge cB_m.                                      \tag{4.4}
\]

The one-edge translates are also pairwise disjoint, although that extra
property is not needed below.

### Theorem 4.1 (critical clustered-seam obstruction)

Under (4.1), along the same subsequence,

\[
 \boxed{
  \Lambda_{m,H}\ge cB_m,\qquad
  \Phi_{m,H}\ge cB_m,\qquad
  \Theta_{m,H}\ge(c/7)B_m.}                     \tag{4.5}
\]

Consequently the quotient gate \((\mathrm{CS}_A)\) fails, and the
spatially lifted additive cluster charge is \(\Omega_A(W)\).

#### Proof

The family \(\mathcal Q\) is eligible in (3.2), so (4.4) gives
\(\Lambda_{m,H}\ge cB_m\).  The remaining inequalities are Theorem 3.2.
Multiplication by the deck size \(N\) changes \(cB_m\) into \(cW\).
\(\square\)

In particular,

\[
 \boxed{
   \neg(\mathrm{ST}_A)\ \Longrightarrow\
   \neg(\mathrm{CS}_A)}                           \tag{4.6}
\]

for the established deck-invariant, append-only cluster ledger.  The
implication is not a claim that coefficient one is false.  It says that
critical residence saturation and an \(o(W)\) sum of the charges (0.1)
cannot coexist.

The tiled length-\(H\) simple-sector model is the equality-scale example:
it has \(B_m/H\) edge-disjoint sectors, packed trace mass \(B_m\), and
every cluster charge is \(\Omega(B_m)\).  Thus Theorem 4.1 is not losing
an artificial power of \(H\).

## 5. The weakest remaining statistic and the only possible escape

For the literal compiler proved in
`PBBS_MULTI_CUT_DOMINANCE_CLUSTER_20260725.md`, the exact remaining
statistic is the thick active span \(\Theta_{m,H}\) in (0.4).  By Lemma
1.1 its vanishing is neither stronger nor weaker, up to fixed constants,
than vanishing of the advertised charge.  Theorem 3.2 gives its dual
lower certificate

\[
 \Theta_{m,H}\ge\Lambda_{m,H}/7.                 \tag{5.1}
\]

Thus a packing proof can establish impossibility of cheap clustering by
showing positive packed trace mass.  Critical saturation does exactly
that.

If one nevertheless works in the critical branch, an enhanced compiler
must cease to append the whole cluster charge to the principal word.  Let
\(R_H\) denote the number of quotient baseline letters which a proposed
cluster construction validly replaces, or, equivalently for the ledger,
the number of letters saved through proved PBBS-specific coincidence of
cluster witnesses with already charged letters.  Its net quotient excess
is

\[
 \Delta_{m,H}:=\Phi_H(Q,\Pi)-R_H.                 \tag{5.2}
\]

The weakest numerical completion condition in this branch is

\[
 \boxed{\Delta_{m,H}=o_A(B_m).}                  \tag{5.3}
\]

Theorem 4.1 makes the required scale of the new phenomenon explicit:

\[
 \boxed{R_H\ge\Lambda_{m,H}-o_A(B_m)=\Omega_A(B_m).}          \tag{5.4}
\]

Therefore no further regrouping of cuts, no choice of a different cutting
edge inside each simple sector, and no independent choice of ambient
completion can finish the critical case.  One must prove one of the
following genuinely new statements:

1. critical saturation is impossible for the canonical PBBS chronology,
   which restores \((\mathrm{ST}_A)\);
2. cluster charts replace a positive-density part of the principal
   erosion word while retaining all internal targets; or
3. PBBS-specific cross-cluster witness coincidences save
   \(\Omega_A(B_m)\) quotient letters.

The first is the strict residence theorem already isolated by the
double-deck saturation normal form.  The last two are baseline-reuse
theorems, not residence-clustering theorems.  This is the exact boundary
left after the \(7H+3S-3\) dominance staircase is fully exploited.
