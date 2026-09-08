# PBBS peak deletion as an exact capacitated quotient projection

Date: 2026-07-25

No computation or web search is used in this note.

## 0. Verdict

Let \(N=2r+1\), \(B_r=\operatorname{Cat}_r\), and let
\(\partial:\mathcal D_r\to\bigcup_{d<r}\mathcal D_d\) be simultaneous
peak deletion.  For an arbitrary pairwise quotient-edge-disjoint family
of rank-\(r\) short-return intervals, peak deletion gives an exact
capacitated interval system over the reduced PBBS:

* a reduced root \(E\in\mathcal D_d\), with
  \(k=\operatorname{pk}(E)\), has fibre capacity
  \[
    P_r(E)=\binom{r+d-k}{2d};
  \]
* a gap-\(g\) return over \(E\) may start only in the Pascal hyperplane
  \(n_0=z_E(g)\), of exact size
  \[
    K_r(E,z_E(g))
    =\binom{r+d-k-z_E(g)-1}{2d-1};
  \]
* at every reduced transition edge, the projected occurrence load is at
  most \(P_r(E)\); and
* the sum of all reduced capacities is exactly \(B_r\).

These statements give the mass identity

\[
 \sum_{I\in\mathcal P}|I|
 =\sum_e L_e(\mathcal P)
 \le\sum_eP_r(e)
 =B_r.
\tag{0.1}
\]

There is no local \(o(1)\) contraction after normalizing by fibre capacity.
For the central gap-seven fibre, an edge-disjoint family over one reduced
passage has normalized start mass

\[
 \frac{|\mathcal P|}{P_r(E_d)}
 \ge \frac1{18}-o(1).
\tag{0.2}
\]

Thus the first false weighted inequality is any assertion that a fixed
reduced passage receives \(o(P_r(E))\) edge-disjoint parent lifts.  Even
remembering both nested child returns does not repair it.

A positive reduction does survive.  Up to \(o(B_r/N)\) start roots, every
possible short return has

\[
 d\ge \frac r4,
 \qquad
 z_*(D)\le\lceil3\log r\rceil.
\tag{0.3}
\]

Equivalently, in the reduced passage the predecessor particle has been
selected at most \(6\log r+O(1)\) times before its final entry.  Hence the
remaining theorem is a high-defect, low-predecessor-multiplicity,
Pascal-weighted passage packing estimate.  Capacity mass transport alone
does not prove it.

## 1. The fibre and its skew permutation

Fix a nonempty reduced core

\[
 E\in\mathcal D_d,
 \qquad
 k=\operatorname{pk}(E),
 \qquad
 p=2d+1,
 \qquad
 y=r-d-k.
\tag{1.1}
\]

The inverse leaf-pruning fibre is canonically the weak-composition simplex

\[
 \Omega_r(E)
 =
 \left\{
   \mathbf n=(n_0,\ldots,n_{p-1})\in\mathbb Z_{\ge0}^{p}:
   \sum_jn_j=y
 \right\}.
\tag{1.2}
\]

The coordinates are the free ordered child-slot occupancies after one
mandatory new leaf has been removed at each of the \(k\) core leaves.  Thus

\[
 \boxed{
 P_r(E):=|\Omega_r(E)|
 =\binom{y+2d}{2d}
 =\binom{r+d-k}{2d}.}
\tag{1.3}
\]

Let \(\tau=\phi^2\) be the step-two Dyck quotient map.  Peak deletion is a
semiconjugacy:

\[
 \partial(\tau D)=\tau(\partial D).
\tag{1.4}
\]

The statistic \(k\) is invariant on the reduced PBBS orbit, because peak
defect is PBBS-invariant.  Hence adjacent reduced fibres have equal size.
Since \(\tau\) is a permutation on the parent roots, its restriction gives
a bijection

\[
 \boxed{
 \Sigma_E:\Omega_r(E)\longrightarrow\Omega_r(\tau E).}
\tag{1.5}
\]

Write \(\Sigma_E^{(t)}\) for the corresponding bijection along \(t\)
reduced transition edges.

For a reduced predecessor-passage time \(g<N\), the exact one-level
classification fixes the final-root slot:

\[
 n_0=z_E(g)
 =\frac{n_{-1}(g)-1}{2}.
\tag{1.6}
\]

Therefore the allowed start set is

\[
 A_r(E,g)
 =
 \{\mathbf n\in\Omega_r(E):n_0=z_E(g)\},
\tag{1.7}
\]

with exact cardinality

\[
 \boxed{
 |A_r(E,g)|
 =K_r(E,z_E(g))
 =\binom{r+d-k-z_E(g)-1}{2d-1}.}
\tag{1.8}
\]

Different consecutive-return times over the same \(E\) prescribe different
values of \(z_E(g)\): otherwise the same parent root would have two distinct
next-return times.  Thus their allowed start hyperplanes are disjoint.

## 2. Exact multiplicities for an arbitrary outer packing

Let \(\mathcal P\) be any pairwise quotient-edge-disjoint family of
nonwrapping rank-\(r\) short-return intervals.  Partition its members by
their reduced start \(E\) and gap \(g\).  Their selected slot vectors form
sets

\[
 S_{E,g}\subseteq A_r(E,g),
 \qquad
 m_{E,g}=|S_{E,g}|.
\tag{2.1}
\]

If the parent interval has \(L_g=(g+3)/2\) transition edges, let

\[
 Q(E,g)=(e_0(E,g),e_1(E,g),\ldots,e_{L_g-1}(E,g))
\tag{2.2}
\]

be its ordered reduced transition-edge trace, with repetitions retained
when the reduced cycle is short.  The first edge includes the fixed
insertion-edge shift relative to the time-zero omitted-label state; after
that shift these are consecutive edges of the reduced \(\tau\)-cycle.

PBBS evolution from the time-zero inverse fibre to the \(t\)-th trace edge
induces a bijection

\[
 \Theta_{E,g}^{(t)}:
 \Omega_r(E)\longrightarrow\Omega_r(e_t(E,g)).
\tag{2.3}
\]

Thus the parent transition edges above \(e_t(E,g)\) are indexed by
\(\Theta_{E,g}^{(t)}S_{E,g}\).

### Theorem 2.1 (exact capacitated projection)

Two selected parent intervals are quotient-edge-disjoint if and only if
all lifted trace points

\[
 \bigl(e_t(E,g),\Theta_{E,g}^{(t)}\mathbf n\bigr),
 \qquad
 \mathbf n\in S_{E,g},
 \quad 0\le t<L_g,
\tag{2.4}
\]

are distinct.

Consequently, for every reduced transition edge \(e\), the exact projected
load

\[
 L_e(\mathcal P)
 =
 \sum_{E,g}
 \sum_{\substack{0\le t<L_g\\e_t(E,g)=e}}
 \left|\Theta_{E,g}^{(t)}S_{E,g}\right|
\tag{2.5}
\]

satisfies

\[
 \boxed{L_e(\mathcal P)\le P_r(e).}
\tag{2.6}
\]

Moreover,

\[
 \boxed{
 \sum_eL_e(\mathcal P)=\sum_{I\in\mathcal P}|I|.}
\tag{2.7}
\]

#### Proof

A rank-\(r\) quotient transition edge is determined uniquely by its
reduced edge and its inverse-tree slot vector.  The semiconjugacy and
PBBS invertibility transport that vector bijectively along the projected
trace, giving the maps (2.3).  Thus equality of two
pairs in (2.4) is exactly equality of the corresponding parent transition
edges.  This proves the first assertion.

For fixed \(e\), edge-disjointness says that the sets in (2.5), including
sets coming from different offsets of a repeated reduced trace, are
pairwise disjoint subsets of \(\Omega_r(e)\).  Their total size is at most
\(|\Omega_r(e)|=P_r(e)\), proving (2.6).  Counting every lifted trace point
first by its parent interval and then by its reduced edge gives (2.7).
\(\square\)

The reduced fibres partition all parent Dyck roots, so

\[
 \boxed{
 \sum_{\substack{d<r\\E\in\mathcal D_d}}P_r(E)
 =B_r.}
\tag{2.8}
\]

Equations (2.6)--(2.8) give (0.1).  This is the complete universal
mass-transport consequence of peak deletion without further information
about which reduced cores satisfy the predecessor-passage condition.

There is also an exact start-fibre inequality.  Let
\(\mathcal R_{\le G}(d)\) be the reduced roots whose distinguished omitted
particle has a consecutive return of gap at most \(G\).  Passage times
\(g\le G\) over one fixed \(E\) prescribe distinct values \(z_E(g)\), so
their hyperplanes (1.7) are disjoint.  Moreover a passage at time \(g\)
requires the distinguished particle to have returned at an earlier time.
Therefore

\[
 \boxed{
 \sum_{\substack{g\le G\\g\ {\rm passage\ for}\ E}}
 K_r(E,z_E(g))
 \le
 P_r(E)\,
 \mathbf1_{\{E\in\mathcal R_{\le G}(d)\}}.}
\tag{2.9}
\]

Summing gives the one-step weighted return recursion

\[
 \boxed{
 R_{\le G}(r)
 \le
 \sum_{d=1}^{r-1}
 \sum_{E\in\mathcal R_{\le G}(d)}P_r(E).}
\tag{2.10}
\]

This bound has no artificial factor \(G\).  It is nevertheless
noncontractive: replacing the left side by the full fibre on the right and
iterating retains only the fact that every successive pruned core has
height at most \(G\).  In the above-Gaussian range, that is precisely the
already-insufficient height gate.

### Corollary 2.2 (the capacitated-passage LP)

For every allowed type \(a=(E,g)\), let

\[
 a_e=\#\{0\le t<L_g:e_t(E,g)=e\}
\tag{2.11}
\]

be the occurrence multiplicity of the reduced edge \(e\) in its ordered
trace, and write \(K_a=K_r(E,z_E(g))\).  Every outer packing gives a
feasible point of

\[
\begin{aligned}
 \text{maximize}\quad&
   \sum_a m_a,\\
 \text{subject to}\quad&
   \sum_a a_e m_a\le P_r(e)
       &&\text{for every reduced edge }e,\\
 &0\le m_a\le K_a
       &&\text{for every allowed passage type }a.
\end{aligned}
\tag{2.12}
\]

Consequently the optimum of (2.12) is an upper bound for
\(\overline\nu_H\).  Its fractional dual is

\[
\begin{aligned}
 \text{minimize}\quad&
   \sum_eP_r(e)w_e+\sum_aK_av_a,\\
 \text{subject to}\quad&
   \sum_ea_ew_e+v_a\ge1
       &&\text{for every }a,\\
 &w_e,v_a\ge0.
\end{aligned}
\tag{2.13}
\]

Thus an \(O(B_r/N)\) dual certificate would prove the desired quotient
bound.  The slot-vector collision conditions in Theorem 2.1 are stronger
than (2.12); hence failure to bound this relaxation would not disprove the
PBBS theorem, but success would be a valid weighted contraction proof.

## 3. Why inverse-fibre normalization does not contract

For the gap-seven core

\[
 E_d=(10)^{d-2}1100,
\tag{3.1}
\]

one has \(k=d-1\), \(z_{E_d}(7)=0\), and hence

\[
 P_r(E_d)=\binom{r+1}{2d},
 \qquad
 K_r(E_d,0)=\binom r{2d-1}.
\tag{3.2}
\]

Their exact ratio is

\[
 \boxed{
 \frac{K_r(E_d,0)}{P_r(E_d)}
 =\frac{2d}{r+1}.}
\tag{3.3}
\]

Choose \(d=d(r)\) so that \(2d-1=r/2+O(1)\).  Then

\[
 \frac{K_r(E_d,0)}{P_r(E_d)}
 =\frac12+o(1).
\tag{3.4}
\]

After discarding the \(\exp(o(r))\) starts on short parent quotient cycles,
the five-edge gap-seven intervals admit a greedy edge-disjoint subfamily
of size at least

\[
 \frac19\bigl(K_r(E_d,0)-\exp(o(r))\bigr).
\tag{3.5}
\]

Every selected interval has the same reduced ordered passage trace.
Therefore

\[
 \boxed{
 \frac{|\mathcal P|}{P_r(E_d)}
 \ge\frac1{18}-o(1).}
\tag{3.6}
\]

The reduced itinerary contains the same two nested gap-five returns for
every parent lift: the distinguished particle returns at time five, while
the predecessor occurs at times two and seven.  Thus charging to a bounded
menu containing both child returns still has the constant normalized load
(3.6).

This disproves every proposed local contraction of the form

\[
 \#\{\text{edge-disjoint parent lifts of one reduced passage}\}
 \le\eta_rP_r(E),
 \qquad \eta_r\longrightarrow0.
\tag{3.7}
\]

It does not disprove the global target because the total gap-seven mass is
only \(2^{r-1}-r=o(B_r/N)\).

## 4. A rigorous high-defect/small-slot reduction

Although there is no local contraction, the Pascal kernel removes two
regions completely.

### Lemma 4.1 (low first-pruned rank is negligible)

The number of \(D\in\mathcal D_r\) for which

\[
 d=|\partial D|\le r/4
\tag{4.1}
\]

is \(\exp(-c r)B_r\) for some absolute \(c>0\).

#### Proof

The first-pruned rank \(d=r-\operatorname{pk}(D)\) has Narayana count

\[
 \frac1r\binom rd\binom r{d+1}.
\tag{4.2}
\]

For \(d\le r/4\), monotonicity and the entropy bound give

\[
 \sum_{d\le r/4}\frac1r\binom rd\binom r{d+1}
 \le
 \exp\!\left(2r\,h(1/4)+o(r)\right),
\tag{4.3}
\]

where

\[
 h(x)=-x\log x-(1-x)\log(1-x).
\]

Since \(h(1/4)<\log2\), while
\(B_r=\exp(r\log4-o(r))\), (4.3) is
\(\exp(-c r)B_r\).  \(\square\)

### Lemma 4.2 (a large terminal slot is negligible)

Condition on a core \(E\in\mathcal D_d\) with \(d\ge r/4\).  In the
uniform inverse fibre \(\Omega_r(E)\),

\[
 \boxed{
 \Pr(n_0\ge L)
 =
 \frac{\binom{y-L+2d}{2d}}{\binom{y+2d}{2d}}
 \le\left(\frac35\right)^L,}
\tag{4.4}
\]

with the numerator interpreted as zero if \(L>y\).

#### Proof

Removing \(L\) units from the distinguished slot is a bijection from
compositions with \(n_0\ge L\) to weak compositions of \(y-L\) into
\(2d+1\) parts.  Hence the equality in (4.4).  The ratio is

\[
 \prod_{i=0}^{L-1}\frac{y-i}{y+2d-i}
 \le\left(\frac{y}{y+2d}\right)^L.
\tag{4.5}
\]

Here \(y=r-d-k\le r-d\le3r/4\), while \(2d\ge r/2\), so

\[
 \frac{y}{y+2d}\le\frac{3/4}{3/4+1/2}=\frac35.
\]

This proves (4.4).  \(\square\)

Take

\[
 L_r=\lceil3\log r\rceil.
\tag{4.6}
\]

Summing (4.4) over all cores and using (2.8) gives

\[
 \#\{D:d\ge r/4,\ n_0\ge L_r\}
 \le
 \left(\frac35\right)^{L_r}B_r
 =O\!\left(r^{-3\log(5/3)}B_r\right)
 =o(B_r/N).
\tag{4.7}
\]

Together with Lemma 4.1, this proves (0.3).  For a return lift,

\[
 n_{-1}(g)=2n_0+1,
\tag{4.8}
\]

so the surviving predecessor multiplicity is at most
\(6\log r+O(1)\).

## 5. The exact remaining RP gate

For every outer packing \(\mathcal P\), discard the \(o(B_r/N)\) intervals
whose start roots lie in Lemma 4.1 or Lemma 4.2.  Every remaining member
has:

\[
 d\ge r/4,
 \qquad
 g\le2H-1=o(r),
 \qquad
 n_{-1}(g)\le6\log r+O(1).
\tag{5.1}
\]

Its reduced itinerary contains both:

1. a consecutive return of the distinguished particle before time \(g\);
2. a consecutive return of the predecessor particle ending at time \(g\).

The exact capacitated data are (1.7)--(1.8) and (2.5)--(2.6).  The
gap-seven family proves that neither the start-hyperplane ratio nor a
bounded menu of the two child returns gives an \(o(1)\) local contraction.

Thus the first unresolved estimate is a global assertion about the set of
high-rank reduced roots whose PBBS itinerary realizes an adjacent-particle
passage with only \(O(\log r)\) prior predecessor selections.  It must use
the distribution or cross-orbit overlap of those passage cores.  The
unweighted child packing number and the total fibre-capacity identity
(0.1) do not contain that information.
