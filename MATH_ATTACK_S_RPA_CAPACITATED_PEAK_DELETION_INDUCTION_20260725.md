# RP_A under peak deletion: exact capacitated induction and the harmonic-tower obstruction

Date: 2026-07-25

This note uses pure mathematics only.  There is no computation, finite
search, or web search.

## 0. Correct normalization and verdict

Put

\[
 N_r=2r+1,
 \qquad B_r=\operatorname{Cat}_r,
 \qquad H_A=\lceil A\sqrt r\rceil
\]

for fixed \(A>0\).  The residence statement needed in Section 22 of
`PBBS_RESIDENCE_PACKING_REDUCTION_20260725.md` is the **physical** estimate

\[
 \nu_{H_A}(P_r)=o_A(B_r).                         \tag{RP_A}
\]

After the negligible short-quotient-cycle term is removed, Theorem 17.1
makes this equivalent to

\[
 \boxed{
 \overline\nu_{H_A}
   =o_A\!\left(\frac{B_r}{N_r}\right).}           \tag{0.1}
\]

In particular, a proof of merely \(\overline\nu_H=o(B_r)\) is short by a
factor of order \(r\) and does not prove \((\mathrm{RP}_A)\).

This note builds the exact induction furnished by equality-particle peak
deletion.  It proves:

1. the full fibre-capacity and passage-hyperplane recursion for an arbitrary
   edge-disjoint outer family;
2. a reduction, with error \(o(B_r/N_r)\), to first-pruned rank at least
   \(r/4\) and terminal slot at most \(3\log r\);
3. the two-dimensional Pascal saddle
   \((d,k)=(r/2,r/6)\), including its exact Gaussian leading constant;
4. a new multilevel tower formula showing that even prescribing an empty
   terminal slot at every deletion level has no vanishing multiplicative
   cost at the harmonic saddle; and
5. an exact two-child return genealogy, including its second terminal-block
   Pascal equation, and the reason bounded block constraints still give no
   capacity contraction.

The result is a rigorous obstruction, not a proof or disproof of
\((\mathrm{RP}_A)\).  Rank-only, unweighted, pointwise-fibre, bounded-child,
and seam-slot-product inductions are all closed.  The first remaining
assertion is a peak-sensitive **dynamical** theorem: bounded-slot
adjacent-particle passages must have vanishing Pascal-weighted density, or
must cluster more strongly than the universal interval conflict bound, in
the Gaussian saddle tube.  No theorem presently cited in the handoff
implies that assertion.

## 1. One-level inverse fibres and exact passage data

Let \(D\in\mathcal D_r\), and write

\[
 E=\partial D\in\mathcal D_d,
 \qquad k=\operatorname{pk}(E),
 \qquad p=2d+1,
 \qquad y=r-d-k.                                   \tag{1.1}
\]

In the plane-tree model, the inverse of simultaneous leaf pruning is
specified by the free leaf occupancies of the \(p\) ordered child slots of
the core tree.  After the mandatory child at each of the \(k\) old leaves
is removed, these occupancies form a weak composition of \(y\) into \(p\)
parts.  Therefore

\[
 \boxed{
 F_r(E):=|\partial^{-1}(E)|
 =\binom{r+d-k}{2d}.}                              \tag{1.2}
\]

Let \(z_*(D)\) be the free occupancy in the final root slot.  In the
equality-particle picture it is the gap between the predecessor particle
\(-1\) and the distinguished particle \(0\):

\[
 x_0(0)-x_{-1}(0)=2z_*(D)+1.                      \tag{1.3}
\]

Run the reduced PBBS on \(0E\), and let \(\kappa_t(E)\in\mathbb Z_p\) be
its omitted particle label, with \(\kappa_0=0\).  Put

\[
 n_j(t)=|\{0\le s<t:\kappa_s(E)=j\}|.             \tag{1.4}
\]

Call \((E,g)\) a **reduced predecessor passage** when

\[
 \kappa_g(E)=-1,
 \qquad \kappa_h(E)=0\text{ for some }0<h<g,
 \qquad n_{-1}(g)\text{ is positive and odd}.     \tag{1.5}
\]

For such a passage define

\[
 z_E(g)=\frac{n_{-1}(g)-1}{2}.                    \tag{1.6}
\]

Then, for \(g<N_r\), the parent root \(D\) has its next omitted
physical-label occurrence exactly at time \(g\) if and only if \((E,g)\)
is a reduced predecessor passage and

\[
 z_*(D)=z_E(g).                                    \tag{1.6a}
\]

The proof is the no-overtaking law: the predecessor is the only particle
which can next enter the edge vacated by particle \(0\), while particle
\(0\) must first be reselected.  Since \(g<N_r\), a full physical wrap is
impossible.  Notice that \(n_{-1}(g)\) counts selections strictly before
the time-\(g\) update; this is the floor-correct indexing in (1.5).

Fixing the final slot to this value leaves the exact number

\[
 \boxed{
 K_r(E,g)
 =\binom{r+d-k-z_E(g)-1}{2d-1},}                  \tag{1.7}
\]

with the convention that an inadmissible binomial coefficient is zero.
Thus the exact number \(R_g(r)\) of quotient roots starting gap \(g\) is

\[
 \boxed{
 R_g(r)=
 \sum_{d=1}^{r-1}
 \sum_{\substack{E\in\mathcal D_d\\(E,g)\text{ is a reduced passage}}}
 \binom{r+d-\operatorname{pk}(E)-z_E(g)-1}{2d-1}.} \tag{1.8}
\]

Equation (1.8), rather than an unweighted count of reduced returns, is the
literal one-step induction kernel.

## 2. Exact capacities for an arbitrary edge-disjoint family

The quotient step-two map \(\tau=\phi^2\) commutes with pruning:

\[
 \partial\tau D=\tau\partial D.                  \tag{2.1}
\]

The peak count \(k\) is invariant on the reduced PBBS orbit.  Hence \(\tau\)
transports adjacent inverse fibres bijectively.  Let \(\mathcal P\) be any
pairwise quotient-edge-disjoint family of nonwrapping parent residence
intervals.  If \(e\) is a reduced quotient edge, count every occurrence of
\(e\) in every projected trace, retaining repetitions when a projected
trace wraps a smaller reduced cycle, and call the resulting load
\(L_e(\mathcal P)\).

For the fully pruned boundary put \(F_r(\varnothing)=1\); its unique inverse
is the height-one word \((10)^r\).  With this convention the fibre sum below
is literally exact, including \(d=0\).

### Theorem 2.1 (capacitated projection)

For every reduced edge \(e\),

\[
 \boxed{L_e(\mathcal P)\le F_r(e),}                \tag{2.2}
\]

and

\[
 \boxed{
 \sum_eL_e(\mathcal P)
 =\sum_{I\in\mathcal P}|I|
 \le\sum_eF_r(e)=B_r.}                            \tag{2.3}
\]

#### Proof

A parent quotient edge above \(e\) is uniquely the pair consisting of
\(e\) and its inverse-tree slot vector.  PBBS invertibility transports the
slot vector bijectively along the reduced trace.  If two projected
occurrences above \(e\) had the same transported vector, the corresponding
parent transition edges would coincide, contrary to edge-disjointness.
Thus all transported vectors counted by \(L_e\) are distinct elements of
the fibre \(\partial^{-1}(e)\), proving (2.2).  Double-counting used parent
edges gives the equality in (2.3), and the fibres partition
\(\mathcal D_r\), giving the final identity.  \(\square\)

More precisely, if \(S_{E,g}\) is the selected set of starting slot vectors
over passage \((E,g)\), then

\[
 S_{E,g}\subseteq\{\mathbf n:n_0=z_E(g)\},
 \qquad |S_{E,g}|\le K_r(E,g),                     \tag{2.4}
\]

and at every trace offset the corresponding transported sets must be
pairwise disjoint.  Equations (2.2)--(2.4) are the complete universal
one-level induction constraints.

They do not contract pointwise.  For

\[
 E_d=(10)^{d-2}1100
\]

the time-seven passage has \(k=d-1\) and \(z=0\), so

\[
 F_r(E_d)=\binom{r+1}{2d},
 \qquad K_r(E_d,7)=\binom r{2d-1},
 \qquad \frac{K_r(E_d,7)}{F_r(E_d)}=\frac{2d}{r+1}. \tag{2.5}
\]

For \(2d-1=r/2+O(1)\), a greedy selection on long parent quotient cycles
keeps at least \((1/18-o(1))F_r(E_d)\) mutually edge-disjoint lifts of this
single reduced passage.  Every one has the same complete two-level pruned
skeleton, since \(\partial E_d=10\).  Hence neither bounded projection
multiplicity nor an \(o(1)\) pointwise fibre contraction is true.

## 3. Two regions which the exact kernel eliminates

The one-level kernel nevertheless removes two regions at the required
\(B_r/N_r\) scale.

### Lemma 3.1 (low first-pruned rank)

The number of roots with \(|\partial D|=d\le r/4\) is

\[
 \exp(-c r)B_r=o(B_r/N_r)                          \tag{3.1}
\]

for an absolute \(c>0\).

#### Proof

The exact Narayana count is

\[
 \#\{D:|\partial D|=d\}
 =\frac1r\binom rd\binom r{d+1}.                  \tag{3.2}
\]

For \(d\le r/4\), the sum of (3.2) is at most
\(\exp(2r h(1/4)+o(r))\), where \(h\) is binary entropy.  Since
\(h(1/4)<\log2\) and \(B_r=\exp(r\log4-o(r))\), (3.1) follows. \(\square\)

### Lemma 3.2 (large terminal slot)

Condition on \(E\in\mathcal D_d\) with \(d\ge r/4\).  In its inverse
fibre,

\[
 \Pr(z_*\ge L)
 =\frac{\binom{y-L+2d}{2d}}{\binom{y+2d}{2d}}
 \le\left(\frac35\right)^L.                       \tag{3.3}
\]

Consequently, with \(L_r=\lceil3\log r\rceil\), all roots having
\(d\ge r/4\) and \(z_*\ge L_r\) have total mass

\[
 O\!\left(r^{-3\log(5/3)}B_r\right)=o(B_r/N_r).   \tag{3.4}
\]

#### Proof

Subtracting \(L\) units from the selected slot is a bijection onto weak
compositions of \(y-L\).  The ratio in (3.3) equals

\[
 \prod_{i=0}^{L-1}\frac{y-i}{y+2d-i}
 \le\left(\frac{y}{y+2d}\right)^L.
\]

Here \(y\le r-d\le3r/4\) and \(2d\ge r/2\), giving \(y/(y+2d)\le3/5\).
Summing over fibres and using \(\sum_EF_r(E)=B_r\) proves (3.4). \(\square\)

Thus, after deleting only \(o(B_r/N_r)\) possible starts, every surviving
return satisfies

\[
 d\ge r/4,
 \qquad z_*(D)\le3\log r+1,
 \qquad n_{-1}(g)\le6\log r+3.                    \tag{3.5}
\]

This is a genuine reduction: the predecessor makes only logarithmically
many prior moves.  It is not yet a packing bound.

## 4. The critical Pascal saddle

Let \(\mathsf N(d,k)=d^{-1}\binom dk\binom d{k-1}\) be the number of
rank-\(d\) Dyck cores with \(k\) peaks.  The total parent mass above cell
\((d,k)\) is

\[
 \boxed{
 \mathsf M_r(d,k)
 =\frac1d\binom dk\binom d{k-1}
  \binom{r+d-k}{2d}.}                              \tag{4.1}
\]

These cells sum to \(B_r\).  The entropy exponent of (4.1), with
\(x=k/r\), \(y=d/r\), is

\[
 \mathcal F(x,y)
 =2y h(x/y)
 +(1+y-x)h\!\left(\frac{2y}{1+y-x}\right).        \tag{4.2}
\]

It has its unique interior maximum at

\[
 (x,y)=(1/6,1/2),
 \qquad \mathcal F(1/6,1/2)=\log4.                \tag{4.3}
\]

Writing

\[
 u=\frac{k-r/6}{\sqrt r},
 \qquad v=\frac{d-r/2}{\sqrt r},                  \tag{4.4}
\]

Stirling expansion gives, uniformly for bounded \(u,v\),

\[
 \boxed{
 \frac{\mathsf M_r(d,k)}{B_r}
 =\frac{9\sqrt2}{2\pi r}
  \exp\!\left[-\frac{81u^2-18uv+33v^2}{8}\right]
  (1+o(1)).}                                      \tag{4.5}
\]

For an exact constant check, at \(r=6n,d=3n,k=n\),

\[
 \boxed{
 \frac{\mathsf M_{6n}(3n,n)}{B_{6n}}
 \sim\frac{3\sqrt2}{4\pi n}
 =\frac{9\sqrt2}{2\pi r}.}                       \tag{4.6}
\]

Although this cell is exponentially negligible relative to the uniform
Catalan measure at rank \(3n\), its parent mass is already the critical
order \(B_r/r\).  This proves that an unweighted lower-rank induction is
invalid.

Prescribing a slot value \(z\) retains the exact fraction

\[
 \frac{K_r(d,k,z)}{F_r(d,k)}
 =\frac{2d}{r+d-k}
  \prod_{a=0}^{z-1}
  \frac{r-d-k-a}{r+d-k-1-a}.                       \tag{4.7}
\]

At the saddle, for fixed \(z\),

\[
 \boxed{
 \frac{K_r(d,k,z)}{F_r(d,k)}
 \longrightarrow\frac34\,4^{-z}.}                \tag{4.8}
\]

Thus even a bounded prescribed slot has constant, rather than vanishing,
cost in the only cells which matter at the \(B_r/r\) scale.

The following moderate-deviation form is needed because bounded \(u,v\) in
(4.5) alone would not justify a \(\sqrt{\log r}\)-wide tube.  The least
eigenvalue of the negative Hessian at the saddle is

\[
 \lambda_*=\frac{57-3\sqrt{73}}4.                 \tag{4.9a}
\]

Uniform Stirling expansion for
\(|d-r/2|+|k-r/6|=O(\sqrt{r\log r})\) gives the
conservative per-cell bound

\[
 \frac{\mathsf M_r(d,k)}{B_r}
 \le \frac{C}{r}
 \exp\!\left[-\frac{\lambda_*}{4}(u^2+v^2)\right] \tag{4.9b}
\]

for all sufficiently large \(r\).  The third-order Taylor error is
\(O((\log r)^{3/2}/\sqrt r)=o(1)\).  Outside a fixed interior
neighbourhood of the saddle, compactness and the uniqueness in (4.3) give
a fixed exponential entropy gap.  It follows that for any

\[
 C_0>\frac4{\sqrt{\lambda_*}}
 \quad\text{(in particular, }C_0=2\text{)},        \tag{4.9c}
\]

the total mass of cells outside

\[
 |d-r/2|+|k-r/6|\le C_0\sqrt{r\log r}              \tag{4.9}
\]

is \(o(B_r/N_r)\).  Indeed, outside the tube
\(u^2+v^2\ge(C_0^2/2)\log r\); summing (4.9b) over at most \(r^2\) cells
and using (4.9c) beats the extra factor \(N_r\).  This proves (4.9) with
all moderate-deviation quantifiers stated.

There is also an unconditional scalar no-go.  At \(r=6n,d=3n\), a
rank-only weight which dominates every inverse fibre must be at least the
largest fibre, attained at \(k=1\):

\[
 w_{6n}(3n)\ge\binom{9n-1}{6n}.                   \tag{4.10}
\]

Its putative lower-rank Catalan budget then satisfies

\[
 \boxed{
 \frac{B_{3n}w_{6n}(3n)}{B_{6n}}
 \ge
 \exp\!\left[
  \left(\log\frac{3^9}{2^{12}}+o(1)\right)n
 \right],}                                      \tag{4.11}
\]

which is exponentially large because \(3^9>2^{12}\).  Conversely, any
rank-only weight with Catalan-sized total budget undercharges some peak
fibre by the reciprocal exponential factor.  Thus retaining the peak
coordinate is logically necessary for any fibre-dominating scalar
induction, not merely a sharpening of constants.
For completeness, (4.11) follows directly from Stirling's exponential
terms:
\(B_{3n}=\exp((6\log2+o(1))n)\),
\(\binom{9n-1}{6n}=\exp((9\log3-6\log2+o(1))n)\), and
\(B_{6n}=\exp((12\log2+o(1))n)\).

## 5. New exact multilevel tower formula

Let

\[
 D_j=\partial^jD_0,
 \qquad r_j=|D_j|                                  \tag{5.1}
\]

for \(0\le j\le L+1\), and assume \(D_{L+1}\) is defined.  Since the
number of peaks of \(D_{j+1}\) is \(r_{j+1}-r_{j+2}\), the number of free
leaves when lifting \(D_{j+1}\) to rank \(r_j\) is

\[
 y_j=r_j-2r_{j+1}+r_{j+2}\ge0.                    \tag{5.2}
\]

### Theorem 5.1 (tower fibre and prescribed seams)

Fix the bottom root \(D_L\), hence also \(r_{L+1}=r_L-\operatorname{pk}(D_L)\).
The number of towers

\[
 D_0\mapsto D_1\mapsto\cdots\mapsto D_L
\]

with the prescribed ranks is

\[
 \boxed{
 \mathcal F(\mathbf r;D_L)
 =\prod_{j=0}^{L-1}
  \binom{r_j+r_{j+2}}{2r_{j+1}}.}                 \tag{5.3}
\]

If the final root slot at level \(j\) is prescribed to equal \(z_j\), the
corresponding tower count is

\[
 \boxed{
 \mathcal K(\mathbf r,\mathbf z;D_L)
 =\prod_{j=0}^{L-1}
 \binom{r_j+r_{j+2}-z_j-1}{2r_{j+1}-1}.}          \tag{5.4}
\]

Here each factor is understood to be zero unless
\(0\le z_j\le y_j\).

In particular, for \(z_j=0\) at every level,

\[
 \boxed{
 \frac{\mathcal K(\mathbf r,\mathbf0;D_L)}
      {\mathcal F(\mathbf r;D_L)}
 =\prod_{j=0}^{L-1}
  \frac{2r_{j+1}}{r_j+r_{j+2}}.}                  \tag{5.5}
\]

#### Proof

Apply (1.2) to the inverse step \(D_{j+1}\mapsto D_j\).  Its core rank is
\(r_{j+1}\), and its core peak count is
\(r_{j+1}-r_{j+2}\).  Hence its fibre size is

\[
 \binom{r_j+r_{j+1}-(r_{j+1}-r_{j+2})}{2r_{j+1}}
 =\binom{r_j+r_{j+2}}{2r_{j+1}}.
\]

This depends only on the three ranks, so the successive choices multiply,
proving (5.3).  Fixing the final slot gives (1.7) with \(z=z_j\), proving
(5.4).  Finally

\[
 \frac{\binom{A-1}{q-1}}{\binom Aq}=\frac qA
\]

at each level, which proves (5.5). \(\square\)

For general \(z_j\), the level-\(j\) ratio is exactly

\[
 \frac{2r_{j+1}}{r_j+r_{j+2}}
 \prod_{a=0}^{z_j-1}
 \frac{y_j-a}{r_j+r_{j+2}-1-a}.                   \tag{5.6}
\]

### Corollary 5.2 (harmonic tower has no seam contraction)

Fix \(L\).  Choose \(R\) divisible by
\(\operatorname{lcm}(1,2,\ldots,L+2)\), and put

\[
 r_j=\frac{R}{j+1}
 \qquad(0\le j\le L+1).                           \tag{5.7}
\]

There exists a bottom Dyck root with ranks \(r_L,r_{L+1}\), and hence the
tower cells in Theorem 5.1 are nonempty.  On this tower,

\[
 \boxed{
 \frac{\mathcal K(\mathbf r,\mathbf0;D_L)}
      {\mathcal F(\mathbf r;D_L)}
 =\prod_{j=0}^{L-1}
  \frac{(j+1)(j+3)}{(j+2)^2}
 =\frac{L+2}{2(L+1)}.}                             \tag{5.8}
\]

Equivalently, the individual factor is

\[
 \frac{2r_{j+1}}{r_j+r_{j+2}}
 =1-\frac1{(j+2)^2}.                               \tag{5.8a}
\]

Thus the fraction decreases only from \(3/4\) at one level to the positive
limit \(1/2\), even if an empty seam is prescribed at every one of
arbitrarily many deletion levels.

#### Proof

The bottom peak count is

\[
 r_L-r_{L+1}=\frac{R}{(L+1)(L+2)},
\]

an integer between one and \(r_L\).  A Dyck path of rank \(n\) with any
prescribed number \(1\le k\le n\) of peaks exists, for example
\((10)^{k-1}1^{n-k+1}0^{n-k+1}\).  Nonnegativity of all inverse free-leaf
numbers follows from

\[
 y_j=\frac{2R}{(j+1)(j+2)(j+3)}>0.
\]

Substitution into (5.5) gives the first product in (5.8).  Its two factors
separately telescope:

\[
 \prod_{j=0}^{L-1}\frac{j+1}{j+2}=\frac1{L+1},
 \qquad
 \prod_{j=0}^{L-1}\frac{j+3}{j+2}=\frac{L+2}{2}.
\]

This proves (5.8). \(\square\)

The quantifiers can grow with the ambient rank.  Since
\(\operatorname{lcm}(1,\ldots,L+2)\le(L+2)!\), one may choose a sequence
\(L\to\infty\), then multiples \(R\to\infty\), with \(L=o(\sqrt R)\).
Thus the noncontraction persists through an unbounded number of levels
inside a Gaussian-size return window.  This remains only a fibre statement;
it does not assert passage admissibility of the chosen cores.

The harmonic profile begins

\[
 r_0=R,
 \qquad r_1=R/2,
 \qquad r_2=R/3,                                  \tag{5.9}
\]

which is exactly the two-dimensional saddle \(d=r/2,k=r/6\) of Section 4.
Thus (5.8) is not merely a thin low-rank curiosity: it is the natural
multilevel continuation of the critical Pascal cell.

At this profile the first extra unit in a nonempty prescribed slot has
asymptotic cost

\[
 \frac{y_j}{r_j+r_{j+2}}=\frac1{(j+2)^2}.          \tag{5.10}
\]

Therefore a potentially dangerous return tower must have \(z_j=0\) at
almost all moderately deep levels.  This is a sharper target, but it is not
a contradiction: the exact multiplicity calculation permits such towers
with total conditional fibre fraction approaching \(1/2\).

## 6. Two-child genealogy and the exact terminal-block kernel

Suppose \((E,g)\) satisfies the passage criterion (1.5).  Let

\[
 h=\min\{t>0:\kappa_t(E)=0\},
 \qquad
 t_- =\max\{t<g:\kappa_t(E)=-1\}.                 \tag{6.1}
\]

Then \([0,h]\) is the consecutive return interval of particle \(0\), and
\([t_-,g]\) is the consecutive return interval of particle \(-1\).  Both
are strict subintervals of the parent passage.  Applying peak deletion to
either child return gives another adjacent-particle passage, until the
child circumference is no larger than its gap.

There is a second exact Pascal equation when this genealogy is enumerated
one level deeper.  Let the present parent root be \(E\in\mathcal D_d\), put

\[
 F=\partial E\in\mathcal D_e,
 \qquad p=2e+1,
 \qquad M=2d+1,                                   \tag{6.2}
\]

and write the equality-particle word as \(w=0F\).  Label its particles
\(0,1,\ldots,p-1\).  The clockwise physical gap from particle \(a-1\) to
particle \(a\) has the unique form

\[
 q_a=1+\epsilon_a+2n_a,
 \qquad
 \epsilon_a=\mathbf1_{\{w_{a-1}\ne w_a\}},        \tag{6.3}
\]

where the \(n_a\)'s are the free Pascal slots; at the root seam
\(\epsilon_0=0\).  Normalize the initial omitted physical coordinate of
\(E\) to zero, and let \(\kappa_t(F)\) and

\[
 C_a(t)=|\{0\le u<t:\kappa_u(F)=a\}|              \tag{6.4}
\]

be the reduced selected particle and its prior selection count.

For \(j\ne0\), put

\[
 Q_j=\sum_{a=1}^{j}q_a,
 \qquad
 \mathcal B(j)=\{j+1,j+2,\ldots,p-1,0\},
 \qquad b(j)=p-j.                                  \tag{6.5}
\]

Before a full wrap, the physical omitted label emitted by particle \(j\)
at time \(t\) is \(Q_j+C_j(t)\pmod M\).  Hence

\[
 \boxed{
 \lambda_t(E)=-1
 \quad\Longleftrightarrow\quad
 \sum_{a\in\mathcal B(j)}q_a=C_j(t)+1.}           \tag{6.6}
\]

Now suppose the first child returns at time \(h\), and the physical
predecessor label needed by the parent passage is emitted at time \(g>h\).
The first child fixes

\[
 \kappa_h(F)=p-1,
 \qquad
 C_{p-1}(h)=q_0=1+2n_0,
 \qquad
 z:=n_0=\frac{C_{p-1}(h)-1}{2}.                   \tag{6.7}
\]

If \(j=\kappa_g(F)\ne0\), equation (6.6) fixes the terminal-block mass

\[
 \sum_{a\in\mathcal B(j)}n_a=s,
 \qquad
 s=\frac{C_j(g)+1-b(j)-
            \sum_{a\in\mathcal B(j)}\epsilon_a}{2}. \tag{6.8}
\]

In the intended saddle range \(g=O(\sqrt d)<M-1\), the case \(j=0\) is
impossible because it would require \(C_0(g)=M-1\).

### Lemma 6.1 (the second child contains a second slot)

Every genuine passage in (6.7)--(6.8) has

\[
 \boxed{b(j)\ge2.}                                 \tag{6.9}
\]

#### Proof

If \(b(j)=1\), then \(j=p-1\), and (6.6) gives
\(q_0=C_{p-1}(g)+1\).  But particle \(p-1\) is selected at time \(h<g\),
so

\[
 C_{p-1}(g)\ge C_{p-1}(h)+1=q_0+1,
\]

a contradiction. \(\square\)

Let

\[
 y=d-2e+|\partial F|                               \tag{6.10}
\]

be the total free slot mass in the inverse fibre over \(F\).  Once
\(F,h,g\) are fixed, the exact number of parent slot vectors satisfying
both child equations is

\[
 \boxed{
 K^{(2)}(F;h,g)
 =\binom{s-z+b-2}{b-2}
  \binom{y-s+p-b-1}{p-b-1},}                      \tag{6.11}
\]

where \(b=b(j)\), and an inadmissible binomial is zero.

#### Proof

The terminal block has \(b\) slots, contains slot \(0\), and has total
mass \(s\).  After fixing \(n_0=z\), distribute \(s-z\) among its other
\(b-1\) slots, giving the first factor.  Distribute the remaining
\(y-s\) units among the \(p-b\) outside slots, giving the second. \(\square\)

For the gap-seven core over \(F=10\), one has

\[
 p=3,
 \qquad j=1,
 \qquad b=2,
 \qquad s=z=0.                                    \tag{6.12}
\]

Formula (6.11) fixes the two terminal slots and places all free mass in the
single outside slot, recovering exactly the unique core
\((10)^{d-2}1100\) at every rank \(d\).

More generally, if a specified block of \(b\) slots is required to have
zero total mass, the exact retained fraction of a \(p\)-slot,
total-mass-\(y\) fibre is

\[
 \rho(p,y,b)
 =\frac{\binom{y+p-b-1}{p-b-1}}
        {\binom{y+p-1}{p-1}}
 =\prod_{i=0}^{b-1}
   \frac{p-1-i}{y+p-1-i}.                         \tag{6.13}
\]

Along a harmonic tower, \(y/p=\Theta(j^{-2})\).  Hence for every fixed
\(B\), uniformly for \(b\le B\),

\[
 \rho(p,y,b)=1-O_B(j^{-2}),                        \tag{6.14}
\]

and the product of these factors over all sufficiently deep levels is
strictly positive.  This makes the bounded-block obstruction quantitative.

This is the natural binary return genealogy.  However, a raw branch count
does not improve the capacity ledger.  Each parent creates two children,
but each reduced edge can be counted in both child subtraces, so its
universal load ceiling doubles from \(F\) to \(2F\).  Thus both the number
of charged objects and the permitted capacity are multiplied by two.

The cancellation is attained, not merely formal.  In the gap-seven family,
the two children are the gap-five intervals \([0,5]\) and \([2,7]\); they
overlap, wrap the same short reduced cycle, and all parent lifts have the
same two-level pruned skeleton.  Hence a bounded menu containing both child
returns still receives a constant fraction of the parent fibre.  Any useful
binary induction needs an additional decorrelation statement saying that
the two child passages consume genuinely different Pascal capacity on most
critical cores.  No such statement has been proved.

Lemma 6.1 and (6.11) do show that the dynamic recursion fixes more than one
seam coordinate.  Yet (6.13)--(6.14) show that a bounded number of fixed
zero slots per harmonic level still has positive cumulative fibre product.
Thus (6.11) can close
\((\mathrm{RP}_A)\) only if the block sizes \(b\), the prescribed masses
\(s\), or the number of independent block constraints grow often enough;
alternatively, the cores for which they stay bounded must be proved
Pascal-weightedly rare.

## 7. A sharp conditional falsification test at the saddle

The saddle calculation turns the remaining dynamic issue into a precise
test.  Fix \(A,a,\eta>0\) and an integer \(z_0\ge0\).  Put
\(H_A=A\sqrt r+O(1)\).  Suppose that, for every integer

\[
 |d-r/2|\le a\sqrt r,
 \qquad k=\lfloor r/6\rfloor,                     \tag{7.1}
\]

at least an \(\eta\)-fraction of the rank-\(d\), peak-\(k\) cores has some
predecessor passage of gap at most \(2H_A-1\) with prescribed slot at most
\(z_0\).  Then the variable-length interval conflict greedy bound gives

\[
 \boxed{
 \liminf_{r\to\infty}
 \frac{r\,\overline\nu_{H_A}}{B_r}
 \ge
 \frac{27\sqrt2\,\eta}
      {4\pi A\,4^{z_0+1}}
 \int_{-a}^{a}e^{-33v^2/8}\,dv>0.}                \tag{7.2}
\]

Indeed, (4.5) summed over the \(\Theta(\sqrt r)\) cells in (7.1), together
with (4.8), gives \(\Theta(B_r/\sqrt r)\) parent starts.  A residence-
\(H_A\) interval conflicts with starts at at most \(2H_A+1\) edge
positions.  The short parent quotient cycles contain only \(\exp(o(r))\)
roots and are negligible.  Dividing by \(2A\sqrt r+o(\sqrt r)\) yields
(7.2), including the displayed constant.

Since (0.1) requires \(r\overline\nu_{H_A}/B_r\to0\), (7.2) would refute
\((\mathrm{RP}_A)\).  Thus a positive bounded-slot passage density on even
one Gaussian saddle curve is fatal.

More generally, let \(R_{\le H_A}^{\mathrm{long}}(r)\) be the number of
short-return starts on long parent quotient cycles.  The maximum conflict
degree gives

\[
 \overline\nu_{H_A}
 \ge\frac{R_{\le H_A}^{\mathrm{long}}(r)}{2H_A+1}. \tag{7.3}
\]

Therefore \((\mathrm{RP}_A)\) necessarily implies the weighted
anticoncentration

\[
 \boxed{
 R_{\le H_A}^{\mathrm{long}}(r)
 =o_A\!\left(\frac{B_r}{\sqrt r}\right).}          \tag{7.4}
\]

Equation (1.8) makes (7.4) an exact Pascal-weighted statement about the
reduced PBBS itinerary.  It is much stronger than saying that the set of
bad lower cores is \(o(B_d)\): Section 4 shows that an exponentially small
lower-core class can carry critical outer mass.

## 8. Audited boundary

The following assertions are proved and integral:

* the exact passage criterion (1.5), Pascal kernel (1.7), and start identity
  (1.8);
* the arbitrary-family transported-fibre capacities (2.2)--(2.4);
* the \(o(B_r/N_r)\) removal of low first-pruned rank and large terminal
  slot, (3.1)--(3.5);
* the saddle position, Gaussian constant, and bounded-slot ratio,
  (4.3)--(4.8);
* the exact multilevel fibre products (5.3)--(5.6) and harmonic no-
  contraction constant (5.8);
* the two-child genealogy, terminal-block kernel (6.11), and raw capacity
  cancellation; and
* the conditional falsification theorem (7.2).

What remains unproved is either of the following genuinely dynamical
alternatives:

1. **weighted passage sparsity:** prove (7.4), uniformly over the saddle
   tube (4.9), while retaining peak and slot weights; or
2. **cross-cycle clustering:** allow more starts, but prove that their
   actual interval packing is \(o(B_r/N_r)\), far below the universal
   \((2H_A+1)\)-conflict bound.

The harmonic-tower theorem shows that multiplying seam-slot probabilities
cannot prove the first alternative: even empty seams at every level retain
asymptotic fraction \(1/2\).  The gap-seven fibre shows that bounded menus
of child returns cannot prove the second.  A successful induction must use
the PBBS order of the adjacent passages themselves—specifically, it must
show that the terminal blocks in (6.11) are often large/nontrivial, or prove
a decorrelation or rigidity theorem for the two child traces on the
peak-\(1/3\) saddle cores.

Accordingly, \((\mathrm{RP}_A)\), and hence constant one by this direct PBBS
route, is **not proved** here.  Nor is it disproved: the positive-density
hypothesis in (7.2) remains open.  The exact first missing implication is

\[
 \boxed{
 \text{high-rank, bounded-slot adjacent passages in the Pascal saddle}
 \Longrightarrow
 o(B_r/\sqrt r)\text{ weighted starts or stronger-than-greedy clustering}.}
 \tag{8.1}
\]

No rank-only or slot-only induction can supply (8.1).

The indices, integral realizability, telescoping constant (5.8), and the
two-child implication scope were independently checked in
`MATH_ATTACK_PBBS_HARMONIC_TOWER_FIBRE_AUDIT_20260725.md`.  The saddle
tail, conditional constant (7.2), exact passage definition, and boundary
normalization were independently checked in
`MATH_AUDIT_S_RPA_CAPACITATED_PEAK_DELETION_INDUCTION_20260725.md`.
