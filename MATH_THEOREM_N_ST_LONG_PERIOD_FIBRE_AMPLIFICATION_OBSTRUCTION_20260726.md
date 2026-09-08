# Long-period PBBS passages amplify entire Pascal hyperplanes

Date: 2026-07-26

Method: pure mathematics only. No computation, finite search, solver, or
external input is used.

## 0. Outcome

Put

\[
 N=2r+1,\qquad B_r=\operatorname {Cat}_r,
 \qquad H=\lceil A\sqrt r\rceil,
\]

where \(A>0\) is fixed.  For a nonempty first-pruned PBBS core
\(E\in\mathcal D_d\), put

\[
 k=\operatorname {pk}(E),\qquad
 P_r(E)=\binom{r+d-k}{2d}.
\]

If \((E,g)\) is a genuine reduced predecessor passage and

\[
 z=z_E(g)=\frac{n_{-1}(g)-1}{2},
\]

then the exact permitted parent hyperplane has size

\[
 K_r(E,g)=\binom{r+d-k-z-1}{2d-1}.                 \tag{0.1}
\]

Here and below this binomial is declared zero unless
\(0\le z\le r-d-k\).

This note proves the following exact lower, rather than upper, capacity
statement.

> **Fibre-amplification theorem.**  Let \(\mathcal Q\) be any collection
> of reduced predecessor passages whose projected quotient trace supports
> are simple and pairwise edge-disjoint.  Then all permitted parent lifts
> of all passages in \(\mathcal Q\) form a pairwise quotient-edge-disjoint
> family.  Consequently
> \[
>  \boxed{
>  \overline\nu_H(r)\ge
>  \sum_{(E,g)\in\mathcal Q}K_r(E,g),}             \tag{0.2}
> \]
> whenever the associated outer residences are at most \(H\).

In particular, at the Pascal saddle

\[
 \frac dr\longrightarrow\frac12,qquad
 \frac kr\longrightarrow\frac16,qquad z=0,
\]

one passage packet has the exact utilization

\[
 \boxed{
 \frac{K_r(E,0)}{P_r(E)}\longrightarrow\frac34.}  \tag{0.3}
\]

Thus a long first-pruned period supplies no local contraction.  Its useful
effect is the opposite: it makes the reduced trace simple, so the whole
slot hyperplane amplifies without a collision.

This is an actual PBBS obstruction, not only an abstract capacity model.
Fix \(0<\alpha<A\), \(\eta>0\), and put

\[
 s=\lfloor\alpha\sqrt r\rfloor.
\]

For all sufficiently large \(r\), there are genuine first zero-winding
PBBS returns of gap \(2s+1\) whose first-pruned cores satisfy simultaneously

\[
 \boxed{
 \begin{gathered}
  d/r\to1/2,\qquad k/r\to1/6,\qquad z=0,\\
  \kappa_{2s+1}=-1,\qquad h_E=2s-1<2s+1,
  \qquad n_{-1}(2s+1)=1,\\
  \operatorname {per}_\tau(E)
  \ge(\gamma_P-o(1))\frac r{\log r},
 \end{gathered}}                                  \tag{0.4}
\]

where

\[
 \boxed{
 \gamma_P=\frac12\log\frac3{4^{1/3}}.}           \tag{0.5}
\]

The top roots may additionally be required to have linearly many canonical
frame changes and no stable frame block longer than
\((1/2+\varepsilon)\log_2r+1\).  Their total exact start mass is at least

\[
 \boxed{
 B_r\exp\!\left(-\bigl(\log(3+\eta)+o(1)\bigr)s\right).}       \tag{0.6}
\]

After reduced-arc selection and exact fibre amplification, this gives an
actual long-period saddle packing of size at least

\[
 \boxed{
 \frac{B_r}{2s+3}
 \exp\!\left(-\bigl(\log(3+\eta)+o(1)\bigr)s\right).}          \tag{0.7}
\]

The bound (0.7) is stretched-exponentially below the critical scale
\(B_r/s\), so it neither proves nor disproves \((ST_A)\).  It rigorously
rules out every proposed proof in which long core period, the exact
bounded-slot passage equations, or a per-core Hall inequality is supposed
to give the missing \(o(1)\).  The remaining possible gain is an aggregate
phase/orbit incidence theorem: the Pascal-weighted passage arcs must
cluster on their long reduced cycles.

There is one important scope caveat.  The packet calibration used below
has endpoint excess \(\Lambda=0\), a sector already removable by the
separate phase-fusion start count.  Hence (0.4)--(0.7) show that the
long-period Pascal hypotheses listed there are insufficient; they do not
by themselves obstruct a proof which uses the additional positive-boundary
condition \(\Lambda>0\).  Section 4.1 gives a second, positive-boundary
long-period saddle calibration with a unique admissible phase and already
edge-disjoint intervals.  It removes the corresponding pointwise escape,
but it does not amplify a whole positive-boundary hyperplane: positivity
is not asserted for the additional inverse lifts.

## 1. Exact passage fibres

Let \(E\in\mathcal D_d\) be nonempty.  Label its equality particles
cyclically so that the time-zero particle is \(0\) and its immediate
predecessor is \(-1\).  Write

\[
 \kappa_t(E)\in\mathbb Z_{2d+1},\qquad
 n_j(g)=\#\{0\le t<g:\kappa_t(E)=j\}.
\]

A reduced predecessor passage at time \(g<N\) obeys

\[
 \kappa_g(E)=-1,\qquad
 h_E:=\min\{t>0:\kappa_t(E)=0\}<g,
\]

\[
 n_{-1}(g)=2z+1.                                  \tag{1.1}
\]

The exact peak-deletion passage theorem says that an outer rank-\(r\)
lift \(D\) has its next time-zero physical label occurrence at time \(g\)
if and only if its final root-slot occupancy is this exact integer \(z\).
Stars and bars then gives (0.1).  The whole inverse fibre has size
\(P_r(E)\).

The step-two trace of the resulting outer residence projects, under
simultaneous peak deletion, onto one canonical consecutive directed trace
of the reduced quotient orbit.  Denote its directed-edge support by

\[
 \Gamma(E,g).
\]

For \(g=2s+1\), the outer positive residence has \(s+1\) states and its
inclusive quotient trace has \(s+2\) directed edges.  Thus

\[
 |\Gamma(E,2s+1)|\le s+2,                         \tag{1.2}
\]

with equality when the reduced trace is simple.

## 2. Fibre amplification

### Theorem 2.1 (integral fibre amplification)

Fix the outer rank \(r\).  Let \(\mathcal Q\) be a collection of genuine
reduced predecessor passages \((E,g)\), possibly at different reduced
ranks, such that:

1. every \(\Gamma(E,g)\) is simple;
2. these directed-edge supports are pairwise disjoint; and
3. every associated outer residence is at most \(H\).

For each \((E,g)\), take every rank-\(r\) inverse lift whose terminal slot
equals \(z_E(g)\).  The resulting outer residence intervals are pairwise
quotient-edge-disjoint.  Hence (0.2) holds.

#### Proof

Peak deletion semiconjugates the quotient permutation:

\[
 \partial\tau=\tau\partial.                       \tag{2.1}
\]

For every reduced orbit edge \(F\), the restriction of \(\tau\) is a
bijection from the inverse fibre above \(F\) to the inverse fibre above
\(\tau F\).  Therefore two distinct parent lifts of one starting core
remain distinct at every common time offset.

Suppose two selected outer intervals shared a directed parent edge.  Their
images under \(\partial\) would be a shared directed edge of their reduced
supports.  By hypothesis 2, the two passages must be the same member of
\(\mathcal Q\).  Simplicity of that support then forces the two occurrences
to have the same time offset.  The fibre bijection at that offset forces
the two initial lifts to coincide.  Thus distinct selected intervals do
not share an edge.

For one passage there are exactly \(K_r(E,g)\) permitted lifts by (0.1).
Summing their cardinalities proves (0.2).  All intervals are integral
literal intervals in the original exact PBBS factor. \(\square\)

### Corollary 2.2 (long period makes one passage packet simple)

If

\[
 \operatorname {per}_\tau(E)>s+2
\]

and \((E,2s+1)\) is a predecessor passage, then all
\(K_r(E,2s+1)\) permitted parent intervals are pairwise edge-disjoint.
Moreover every parent quotient cycle containing one of them has period at
least \(\operatorname {per}_\tau(E)\).

#### Proof

The period inequality makes the consecutive reduced trace simple.  Apply
Theorem 2.1 to the singleton collection.  If a parent has period \(L'\),
then its image under \(\partial\) has period dividing \(L'\), proving the
last assertion. \(\square\)

### Corollary 2.3 (exact saddle utilization)

For the zero slot,

\[
 \frac{K_r(E,0)}{P_r(E)}
 =\frac{2d}{r+d-k}.                               \tag{2.2}
\]

More generally,

\[
 \boxed{
 \frac{K_r(E,z)}{P_r(E)}
 =
 \frac{2d}{r+d-k}
 \prod_{j=0}^{z-1}
 \frac{r-d-k-j}{r+d-k-1-j}.}                     \tag{2.3}
\]

Consequently (0.3) holds uniformly whenever
\(d/r\to1/2\) and \(k/r\to1/6\).  In the audited Gaussian saddle tube

\[
 d=\frac r2+O(\sqrt{r\log r}),\qquad
 k=\frac r6+O(\sqrt{r\log r}),
\]

uniformly for \(0\le z\le3\log r\),

\[
 \boxed{
 \frac{K_r(E,z)}{P_r(E)}
 =\left(\frac34+o(1)\right)4^{-z}.}               \tag{2.4}
\]

#### Proof

Divide

\[
 K_r(E,0)=\binom{r+d-k-1}{2d-1}
\]

by

\[
 P_r(E)=\binom{r+d-k}{2d}.
\]

This gives (2.2), whose saddle limit is

\[
 \frac{1}{1+1/2-1/6}=\frac34.
\]

For general \(z\), divide first by
\(\binom{r+d-k-1}{2d-1}\); the remaining ratio is

\[
 \prod_{j=0}^{z-1}
 \frac{r-d-k-j}{r+d-k-1-j},
\]

which proves (2.3).  In the displayed Gaussian tube every factor is
\(1/4+O(\sqrt{\log r/r}+z/r)\).  Since \(z=O(\log r)\), multiplication
gives (2.4). \(\square\)

Thus the packet uses a \((3/4+o(1))\)-fraction of the available parent
edges above every reduced edge in its trace.  This is the precise local
recourse obstruction.

## 3. The long-period threshold at the Pascal saddle

We record the short-period estimate needed for the actual calibration.
The number of rank-\(d\) Dyck roots on quotient cycles of period at most
\(L\) is at most

\[
 2L(2d+1)^{2L}.                                   \tag{3.1}
\]

This is the normalized voltage-itinerary bound.  For one such core with
peak count \(k\), its complete rank-\(r\) inverse capacity is

\[
 P_r(E)=\binom{r+d-k}{2d}.                        \tag{3.2}
\]

At

\[
 d/r\to1/2,qquad k/r\to1/6,
\]

uniform Stirling expansion gives

\[
 \frac1r\log P_r(E)
 \le p_0+o(1),qquad
 p_0=\frac43\log4-\log3.                         \tag{3.3}
\]

If

\[
 L\le(\gamma+o(1))\frac r{\log r},
\]

then (3.1) contributes at most \((2\gamma+o(1))r\) to the logarithm.
Since

\[
 \log4-p_0
 =\log\frac3{4^{1/3}}=2\gamma_P,                \tag{3.4}
\]

all saddle roots whose first-pruned core has period at most \(L\) have
total mass

\[
 e^{-c r}B_r                                      \tag{3.5}
\]

for some \(c>0\), provided \(\gamma<\gamma_P\).

For completeness, outside every fixed neighbourhood of the saddle, the
exact cell mass

\[
 \frac1d\binom dk\binom d{k-1}
 \binom{r+d-k}{2d}                                \tag{3.6}
\]

has an exponential Catalan deficit.  This follows from Stirling's formula:
its continuous entropy has the unique maximum
\((d/r,k/r)=(1/2,1/6)\).  Polynomially many cells do not affect the
exponential deficit.

A standard diagonalization now permits both the saddle neighbourhood to
shrink to zero and \(\gamma\) to increase to \(\gamma_P\).  Therefore,
from any family of size

\[
 B_r e^{-o(r)},                                   \tag{3.7}
\]

one may discard a relative \(o(1)\) and retain

\[
 d/r\to1/2,\qquad k/r\to1/6,qquad
 \operatorname {per}_\tau(E)
 \ge(\gamma_P-o(1))\frac r{\log r}.              \tag{3.8}
\]

The strict inequality below \(\gamma_P\) is essential at every finite
stage of the diagonal.

## 4. Actual long-period saddle calibration

We use the exact spectator-conveyor family.  Fix
\(0<\alpha<A\), put \(s=\lfloor\alpha\sqrt r\rfloor\), and choose

\[
 k_0=\lfloor s/2\rfloor.
\]

The construction has one last-child spine of height \(s\), star forests
\((10)^{L_i}\) in its pre-spine sectors, and one arbitrary Dyck spectator
\(Q\) in the post-spine sector \(B_{k_0}\), with

\[
 \operatorname {ht}(Q)\le\min(k_0,s-k_0).
\]

Its literal sector transport proves:

1. it starts a first zero-winding return of gap \(2s+1\);
2. its return has height \(s\) and residence \(s+1\le H\);
3. a transition reframes exactly when its corresponding \(L_i\) is
   positive;
4. the root post-spine forest \(B_0\) is empty at the starting phase; and
5. its endpoint excess is \(\Lambda=0\).

Item 4 says precisely that the final inverse-pruning root slot is empty:
the surviving spine child is the last root child and no new leaf child
lies after it.  Hence

\[
 z=0.                                             \tag{4.1}
\]

Applying the exact predecessor-passage theorem to the first-pruned core
\(E=\partial D\) gives

\[
 \kappa_{2s+1}(E)=-1,qquad
 h_E=2s-1<2s+1,qquad
 n_{-1}(2s+1)=1.                                  \tag{4.2}
\]

The leader-child part of the exact two-child passage theorem says that
\([0,h_E]\) is a genuine consecutive return in the first-pruned PBBS.
Because the parent return is tight, oddness gives \(h_E\le2s-1\); the
height-gap theorem at reduced height \(s-1\) gives \(h_E\ge2s-1\).
This proves the displayed equality.

The exact weighted conveyor enumeration proves that, for every fixed
\(\eta>0\), the number of distinct starting roots can be chosen at least

\[
 |\mathcal S_r|
 \ge B_r
 \exp\!\left(-\bigl(\log(3+\eta)+o(1)\bigr)s\right).          \tag{4.3}
\]

The same roots may be required to have at least \(s/10\) frame changes
and no stable block of length

\[
 \left\lceil(1/2+\varepsilon)\log_2r\right\rceil.             \tag{4.4}
\]

Since (4.3) is \(B_re^{-o(r)}\), the exponential deletions of Section 3
remove only a relative \(o(1)\).  Let \(\mathcal S_r'\) be the surviving
family, and let \(\mathscr E_r\) be its set of distinct first-pruned cores.
Then every member of \(\mathscr E_r\) satisfies (0.4), and

\[
 \sum_{E\in\mathscr E_r}K_r(E,0)
 \ge|\mathcal S_r'|
 \ge B_r
 \exp\!\left(-\bigl(\log(3+\eta)+o(1)\bigr)s\right).          \tag{4.5}
\]

The first inequality is literal: every constructed root over \(E\) lies
in its terminal-zero hyperplane, while the complete hyperplane may contain
additional roots.

On each reduced quotient cycle, all cores have the same \((d,k)\), so
the weight \(K_r(E,0)\) is constant.  Every trace has at most \(s+2\)
directed edges.  The standard circular greedy selection therefore keeps
reduced supports of total weight at least

\[
 \frac1{2s+3}
 \sum_{E\in\mathscr E_r}K_r(E,0).                 \tag{4.6}
\]

Indeed a length-\((s+2)\) interval can conflict only with starts in its
\(s+1\) preceding positions, its own position, and its \(s+1\) following
positions.  The period bound in (0.4) is much larger than \(s+2\), so no
selected reduced trace wraps.

Apply Theorem 2.1 to the selected reduced supports.  Equations
(4.5)--(4.6) give (0.7).

The dense-reframing and no-long-stable-block properties belong to the
constructed seed roots in \(\mathcal S_r'\).  They are not asserted for
every additional inverse lift in the amplified hyperplanes.

### 4.1 A positive-boundary singleton-phase calibration

The preceding packet calibration has \(\Lambda=0\).  A separate literal
family shows that positive endpoint boundary and phase isolation also give
no pointwise long-period gain.

Let \(p\ge3\), put

\[
 h=p-2,\qquad s=2p-1,
\]

and let \(F\) range over all semilength-\(M\) Dyck words of exact height
\(h\).  Define

\[
 D(F)=1^p0^p1^{2p-1}0^{p+1}F0^{p-2},
 \qquad r=M+3p-1.                                 \tag{4.7}
\]

The exact terminal-singleton calculation gives all of the following.

1. \(D(F)\) starts a first zero-winding return of duration \(s\), hence
   omitted-label gap \(2s+1\).
2. Its endpoint excess is exactly
   \[
   \Lambda=2p>0.                                  \tag{4.8}
   \]
3. Phase zero is the unique return-start phase in the whole terminal
   rotor of period \(s\).
4. If two constructed roots lie on one top quotient cycle, their phase
   separation is a multiple of \(s\).

Item 4 follows by applying \(\partial^{p-1}\): every constructed root
projects to the same terminal rotor state \(A_0\), whose exact period is
\(s\).  An actual duration-\(s\) residence support has \(s+2\) quotient
edges, including insertion and removal.  Hence two constructed supports
can conflict only when their starts are adjacent in the \(s\)-spaced
lattice on that cycle.  The resulting conflict graph has maximum degree
two, and therefore has an independent set containing at least one third
of its vertices.  After deleting the globally negligible short parent
cycles, at least one third of the constructed starts form a pairwise
quotient-edge-disjoint family.

The first deepest root child lies in the second primitive component in
(4.7), and that component is the last root child.  It survives the first
pruning round, with no new leaf child after it.  Therefore the first
inverse-pruning terminal slot is exactly

\[
 z=0.                                             \tag{4.9}
\]

The first-pruned core \(E=\partial D(F)\) consequently satisfies

\[
 \kappa_{2s+1}(E)=-1,\qquad
 h_E=2s-1,\qquad n_{-1}(2s+1)=1.                 \tag{4.10}
\]

Choose fixed \(0<\alpha<\beta<A/2\).  The exact-height shell theorem gives
infinitely many \(M\), and a corresponding

\[
 \alpha\sqrt M\le h\le\beta\sqrt M,
\]

for which

\[
 \#\{F:|F|=2M,\operatorname {ht}(F)=h\}
 \ge c_{\alpha,\beta}\frac{4^M}{M^2}.             \tag{4.11}
\]

Then \(s+1\le H=\lceil A\sqrt r\rceil\) for all sufficiently large
\(M\).  The preceding
degree-two selection gives an actual edge-disjoint PBBS packing of size at
least one third of (4.11).  In ambient Catalan units,

\[
 \frac{4^M}{M^2}
 =
 \frac{B_r}{\sqrt r}
 \exp[-(3\log4+o(1))p].                           \tag{4.12}
\]

This is \(B_re^{-o(r)}\).  Hence the same saddle and period deletions as
in Section 3 remove only a relative \(o(1)\).  A relative \(1-o(1)\)
subfamily of (4.11) satisfies

\[
 \frac dr\to\frac12,\qquad
 \frac kr\to\frac16,\qquad
 \operatorname {per}_\tau(E)
 \ge(\gamma_P-o(1))\frac r{\log r},               \tag{4.13}
\]

while retaining (4.8)--(4.10), unique phase, and a pairwise
edge-disjoint subfamily of at least one third of its remaining starts.

Thus even in the positive-boundary sector, long first-pruned period cannot
supply a pointwise contraction or a compulsory phase-multiplicity gain.
The family remains stretched-exponentially below the critical scale, so
its exact obstruction is global context rarity, not \((ST_A)\) itself.
The complete zero-slot hyperplane above each retained core is eligible by
Theorem 2.1, but the additional lifts are not asserted to retain
\(\Lambda>0\) or the singleton-phase property.

## 5. Exact implication boundary

The following are proved.

1. **Long-period fibre amplification:** equation (0.2) is an integral
   lower bound for literal PBBS intervals.
2. **Saddle packet utilization:** a zero-slot passage uses
   \((3/4+o(1))\) of every parent fibre along its trace.
3. **Joint realizability:** Gaussian height, the exact passage equations,
   \(z=0\), Pascal-saddle ranks, dense reframing, logarithmically short
   stable blocks, and first-pruned period
   \((\gamma_P-o(1))r/\log r\) occur simultaneously in actual PBBS seed
   roots.
4. **Quantitative calibration:** the resulting actual packing has the
   lower bound (0.7).
5. **Positive-boundary calibration:** positive endpoint excess, one
   admissible terminal phase, an integral edge-disjoint subfamily of
   density at least \(1/3\), \(z=0\), saddle ranks, and the same
   long-period bound occur simultaneously in the family (4.7).

The following are not proved.

1. \(\overline\nu_H=o_A(B_r/\sqrt r)\), \((ST_A)\), or constant one.
2. A critical packing \(\Omega_A(B_r/\sqrt r)\).
3. A critical-size positive-endpoint-excess calibration, or
   positive-boundary preservation for the whole amplified hyperplane.
4. A phase-incidence estimate on the long reduced cycles.

The exact missing assertion can now be stated without a local loophole.
For every long reduced orbit \(\mathcal O\), let \(\mathcal A(\mathcal O)\)
be its actual predecessor-passage arcs, weighted by the exact binomials
\(K_r(E,g)\).  One must prove that the maximum total weight of pairwise
edge-disjoint arcs, summed over the Pascal saddle orbits and restricted to
the genuinely unresolved boundary sectors, is

\[
 o_A(B_r/\sqrt r).                                \tag{5.1}
\]

Long period cannot prove (5.1): it is already the hypothesis which turns
each individual arc into a constant-utilization packet.  Any successful
proof must instead use a PBBS-specific cross-phase correlation forcing the
weighted passage phases to cluster, or use the additional endpoint/common-
carrier constraints absent from (0.4).
