# One-sided compiler near-cover: exact union gate and the limit of antipodal/enumerator data

Date: 2026-07-26

Method: pure mathematics only. No computation, search, solver, or web input is used.

## 0. Verdict

For one sign and depth, floor-balanced CPCR is stronger than necessary.
If the selected compiler images have loads

\[
                         L(T)=\#\{P:T\in I_{P,g_P,q}^{\epsilon}\},
\]

then the missing-target count satisfies the exact identity

\[
 \boxed{
 M_q^\epsilon
 =N_q-\left|\bigcup_PI_{P,g_P,q}^{\epsilon}\right|
 =\sum_T(L(T)-1)_+-(G-N_q).}
\]

Thus the one-sided target is precisely to make cross-packet repeat mass
equal its unavoidable value \(G-N_q\), up to \(o(W)\).  Loads larger
than the two floor values are harmless if they do not create additional
uncovered targets elsewhere.

The recursive column enumerator does not prove this near-cover.  After
antipodal fusion the local affine catalogue still has maximum codegree on
the full degree scale:

\[
                         \Delta_2\ge(1/4-o(1))D.
\]

The dispersed selector dilutes this particular type to
\(\Theta((R/m)^2)D\) in its packet-relative average, but:

1. antipodal fusion is packet-dependent and is not a quotient of the
   global target layer;
2. the enumerator computes within-option affine type multiplicities,
   whereas a near-cover is controlled by intersections of options from
   different parents;
3. the selector supplies annealed type/profile censuses, not the
   arbitrary-weight configuration Hall inequality; and
4. one affine label must serve all protected depths and both signs.

A full-image rainbow matching would be a sufficient one-sided theorem,
but the presently proved data do not satisfy the proposed
growing-uniformity codegree criterion and do not imply such a matching.
No \(\Omega(W)\) one-sided coverage deficit is proved either.  The exact
remaining statement is the integral multiple-choice union problem in
Section 4, or equivalently its repeat-excess form above.

## 1. Exact missing/repeat ledger

Fix \((q,\epsilon)\), suppress these indices, and choose one legal
compiler label \(g_P\) in every packet.  Packet trace injectivity gives

\[
                         |I_{P,g_P}|=K=2^R,
 \qquad
                         \sum_TL(T)=G.
\]

Since

\[
 L=\mathbf1_{\{L>0\}}+(L-1)_+,
\]

summing over targets gives

\[
 G=|\{T:L(T)>0\}|+\sum_T(L(T)-1)_+.
\]

Subtracting the first term from \(N_q\) proves

\[
 M_q^\epsilon
 =N_q-G+\sum_T(L(T)-1)_+.
\]

Because \(G\ge N_q\) in the protected central band, the pigeonhole
minimum of the repeat mass is \(G-N_q\).  Hence

\[
 \boxed{
 M_q^\epsilon
 =\mathcal R_q^\epsilon-(G-N_q),
 \qquad
 \mathcal R_q^\epsilon:=\sum_T(L(T)-1)_+.}
\]

The aggregate coefficient-one target is therefore

\[
 \sum_{q\le H}\sum_{\epsilon\in\{-,+\}}
 \left[\mathcal R_q^\epsilon-(G-N_q)\right]=o(W).
\]

This is strictly weaker than CPCR.  CPCR controls a quadratic penalty for
every departure from the two floor loads; the one-sided objective sees
only the size of the union.

## 2. A sufficient rainbow near-cover

For fixed \((q,\epsilon)\), form the colored hypergraph

\[
 \mathcal H_{q,\epsilon}:
 \quad V(\mathcal H)=\mathcal T_q^\epsilon,
 \quad E_{P,g}=I_{P,g,q}^\epsilon,
\]

where the edge color is the packet \(P\).  Every edge has size \(K\).

### Lemma 2.1 (full-image rainbow matching is sufficient)

If \(\mathcal H_{q,\epsilon}\) has a matching of differently colored
edges of size

\[
                         {N_q-o(W)\over K},
\]

then legal labels can be chosen in all packets so that

\[
                         M_q^\epsilon=o(W).
\]

#### Proof

Use the matching option in every represented color and arbitrary legal
options in the remaining colors.  The matched images are disjoint and
cover \(N_q-o(W)\) targets.  Adding the remaining packet images cannot
decrease the union.  \(\square\)

Since \(K=2^{o(m)}=o(W)\), even the integer remainder on dividing
\(N_q\) by \(K\) is negligible.

For the common all-depth problem one may use a different subfamily of
packet colors at each \((q,\epsilon)\), but the option \(g_P\) attached to
a packet must be the same in every subfamily.  Thus separate rainbow
matchings at separate depths are not composable after the fact.

The lemma is sufficient, not necessary.  A near-cover may use heavily
overlapping full images and assign different nonoverlapping home subsets
inside them.

## 3. Why antipodal fusion is not a global quotient

Inside a fixed abstract packet, every compiler image is closed under

\[
                         (J,\eta)\longmapsto
                         (J,\eta+\mathbf1_{J^c}).
\]

Contracting this pair turns a local option edge of size \(K\) into one of
size \(K/2\).  This is legitimate for the affine catalogue of one fixed
packet.

For a physical target \(T\), however, its mate uses all unvaried active
axes of the packet.  If \(P\) and \(P'\) have different active supports,
then in general

\[
                         \bar T^{P}\ne\bar T^{P'}.
\]

Thus there is no equivalence relation on the global target layer whose
classes are the antipodal pairs for every color.  Contracting the
incidences separately gives packet-face clones
\((P,[f]_P)\), not global target supervertices.  A matching of those
clones can use the same physical target in different colors and therefore
does not imply a target matching or target cover.

This is an exact obstruction to the proposed inference

\[
 \text{local antipodal quotient matching}
 \Longrightarrow
 \text{global rainbow near-cover}.
\]

## 4. Exact one-sided configuration problem

Introduce binary option variables

\[
 x_{P,g}\in\{0,1\},
 \qquad
                         \sum_gx_{P,g}=1,
\]

and target-reserve variables \(z_T\in\{0,1\}\).  The one-sided
near-cover problem with reserve \(E\) is exactly

\[
\begin{aligned}
 \sum_{P,g}a_{P,g,T}x_{P,g}+z_T&\ge1&& (T\in\mathcal T_q^\epsilon),\\
 \sum_Tz_T&\le E,\\
 a_{P,g,T}&=\mathbf1_{\{T\in I_{P,g,q}^\epsilon\}}.
\end{aligned}
\]

Equivalently, after the labels are chosen, assign every covered target to
one incident selected option as its home.  No additional packet capacity
constraint is needed: an option contains only \(K\) targets, so it cannot
receive more than \(K\) distinct homes.

The exact fractional dual is the configuration Hall inequality

\[
 \boxed{
 \sum_P\max_g\sum_Ty_Ta_{P,g,T}+\rho_E(y)
 \ge\sum_Ty_T
 \qquad(y\ge0),}
\]

where \(\rho_E(y)\) is the sum of the \(E\) largest target weights.  This
is necessary and sufficient for the fractional relaxation.  Integral
near-cover requires rounding the product of packet simplices without
losing more than \(o(W)\) targets.

There is a sharp finite integrality warning.  Let the packet colors be
\([b]\), with two options \(0,1\) in every color.  For each unordered
pair \(\{i,j\}\) and each \((s,t)\in\{0,1\}^2\), make one target

\[
                         T_{ij}^{s,t}.
\]

Join this target to option \((i,1-s)\) and option \((j,1-t)\), and to no
others.  Every option contains exactly \(2(b-1)\) targets, while

\[
                         N=4\binom b2=2b(b-1)=G.
\]

The fractional choice \(x_{i,0}=x_{i,1}=1/2\) covers every target with
load exactly one.  But an integral choice is a bit vector
\(g\in\{0,1\}^b\).  For every pair \(\{i,j\}\), precisely the target

\[
                         T_{ij}^{g_i,g_j}
\]

is uncovered.  Hence every integral choice misses

\[
                         \binom b2=N/4
\]

targets.  Options of the same color are disjoint, and two options of
different colors intersect in exactly one target.  Thus regular option
sizes, exact fractional coverage, and tiny pairwise option intersections
still do not round the grouped union problem.

To add the same forced local feature as the compiler, replace every target
by two antipodal copies and put both copies in every incident option.
The missing fraction remains \(1/4\).  Contracting the antipodal copies
returns the original obstruction.  Therefore antipodal fusion cannot, by
itself, repair the multiple-choice integrality gap.

For all depths and signs, insert every token \((q,\epsilon,T)\) in the
same system and retain the same variables \(x_{P,g}\).  This is the exact
common-label one-sided gate.  It is weaker than the floor-quota dual but
still tests arbitrary literal weights, not merely safe profile weights.

## 5. What the recursive enumerator contributes

The exact recursion in

`MATH_AUDIT_RECURSIVE_COMPILER_COLUMN_ENUMERATOR_AND_CPCR_CODEGREE_20260726.md`

computes

\[
 A_q(a,\delta)
 =\#\{(f,f')\text{ in one base image}:
                    \omega(f,f')=(a,\delta)\}.
\]

For the full affine catalogue of one packet it gives the exact
conditional pair incidence

\[
                         p_q(a,\delta)
 ={A_q(a,\delta)\over K M_{R,q}(a,\delta)}.
\]

In particular, unvisited recursive context leaves give

\[
                         p_q(q,2)\ge1/4-o(1),
\]

uniformly for \(q\le A\sqrt m\).  Hence even after local antipodal
contraction,

\[
                         \Delta_2=\Theta(D)
\]

in the affine option catalogue.

For one dimension-\(S\) product cell, the dispersed selector changes the
packet-relative mean to

\[
 \eta_q(a,\delta;S)
 =(1+o(1)){(R-q)_{q-a+\delta}\over(S-q)_{q-a+\delta}}
 p_q(a,\delta),
\]

away from group collisions.  Thus the surviving type \((q,2)\) has

\[
                         \eta_q(q,2;S)
 \ge(1/4-o(1))(R/S)^2.
\]

This is useful pair information, but it does not imply the arbitrary
weight inequality of Section 4.  A pair enumerator is a second-moment
object.  The maximum-union problem depends on all higher intersections
of the packet-option sets and on how those intersections align across
different parent cells.  The multivariate stacked recursion computes the
local higher column types when a relative embedding is specified; the
present selector theorem does not supply their quenched cross-parent
census.

## 6. Audit of the rainbow criterion

The previously proposed growing-uniformity hypothesis after antipodal
fusion was

\[
                         \Delta_2=o(D/K).
\]

It fails locally because \(\Delta_2\ge(1/4-o(1))D\).  Even after the
packet-relative selector dilution, the type-\((q,2)\) ratio is

\[
                         \Theta((R/S)^2),
\]

whereas \(1/K=2^{-R}\).  Therefore the deficit in this criterion is at
least

\[
                         K(R/S)^2\longrightarrow\infty.
\]

An ordinary bounded-uniformity nibble asks only for
\(\Delta_2=o(D)\), and the selector average is compatible with that
weaker scale.  Here the edge size is \(K=2^R\to\infty\), the colors impose
one option per packet, and the available estimate is annealed rather than
a maximum.  No bounded-uniformity theorem can therefore be invoked
uniformly in the present parameters.

The recursive enumerator hence gives a negative answer to the specific
question whether *antipodal fusion plus the current pair census* already
yields a rainbow near-cover.  It does not show that a near-cover is
false.  A proof may still use structured block recoloring, cross-parent
slab transport, or a direct integral configuration-Hall argument rather
than a generic low-codegree nibble.

## 7. Exact remaining one-sided discrepancy

Define

\[
\begin{aligned}
 \mathfrak M_m:=
 \min_{\substack{
  \text{legal frames, dispersed selectors, slab trades}\\
  g_P\in\Gamma_R\ \text{one common label per packet}}}
 \sum_{q\le H}\sum_{\epsilon\in\{-,+\}}
 \left[
  N_q-left|\bigcup_PI_{P,g_P,q}^\epsilon\right|
 \right].
\end{aligned}
\]

Equivalently,

\[
\boxed{
 \mathfrak M_m=
 \min_{\mathrm{legal}}
 \sum_{q\le H,\epsilon}
 \left[
  \sum_T(L_q^\epsilon(T)-1)_+-(G-N_q)
 \right].}
\]

The desired one-sided theorem is exactly

\[
                         \mathfrak M_m=o(W).
\]

This is the sharp weaker replacement for CPCR.  The recursive enumerator
and selector census identify entries and annealed moments of its
cross-parent incidence system, but do not presently bound this minimum.

## 8. Certified boundary

Proved:

1. missing targets equal repeat excess above \(G-N_q\);
2. a near-spanning full-image rainbow matching is sufficient;
3. packetwise antipodal contraction is not a global target quotient;
4. the exact integral and fractional one-sided configuration gates;
5. failure of the proposed post-fusion growing-uniformity codegree
   criterion; and
6. the exact all-depth common-label one-sided discrepancy
   \(\mathfrak M_m\).

Not proved:

1. a rainbow near-cover;
2. integral rounding of the one-sided configuration Hall system;
3. an \(\Omega(W)\) global missing-target obstruction; or
4. coefficient one.

The one-sided reformulation removes unnecessary floor balancing, but it
does not remove the cross-parent compiler-realizability gate.
