# Lane N: RP_A, phase-deck rigidity, and the exact Pascal-saddle boundary

Date: 2026-07-25

Method: pure mathematics only. No web search, computation, finite search,
solver, or long-running job is used.

## 0. Verdict

Put

\[
 N=2r+1,\qquad B=\operatorname {Cat}_r,
 \qquad H=\lceil A\sqrt r\rceil
\]

for fixed \(A>0\), and let \(P_r\) be the canonical PBBS factor. The
assertion

\[
 \boxed{\nu_H(P_r)=o_A(B)} \tag{RP_A}
\]

is **not proved or disproved** in this report. The precise quotient
normalization is

\[
 \boxed{
 \nu_H(P_r)=o_A(B)
 \quad\Longleftrightarrow\quad
 \overline\nu_H=o_A(B/N),}                          \tag{0.1}
\]

where \(\overline\nu_H\) is the maximum quotient-edge-disjoint packing on
the long quotient cycles. Thus the unconditional estimate

\[
 \overline\nu_H=O\!\left(B\sqrt{\frac{\log r}{r}}\right) \tag{0.2}
\]

is genuinely insufficient: it misses (0.1) by a factor of order
\(\sqrt{r\log r}\).

The new conclusions are the following.

1. The exact Kac identity for the next omitted-label gap \(g(D)\) is

   \[
    \boxed{\sum_{D\in\mathcal D_r}g(D)=NB.}          \tag{0.3}
   \]

   Hence the mean projected positive residence is exactly \(r+1\). This
   identity has no Gaussian lower-tail consequence.

2. The whole defect-one reduced passage class is explicitly soluble. If

   \[
    E(a,b,c)=(10)^a1(10)^b0(10)^c,
    \quad a,c\ge0,\ b\ge1,\ a+b+c=d-1,
   \]

   then its first root return is \(6c+5\), and its first subsequent
   predecessor passage is

   \[
    \boxed{g=6(b+c)+1,\qquad z_E(g)=0.}              \tag{0.4}
   \]

   All Gaussian-short outer lifts of all such cores have total start mass

   \[
    \boxed{O_A(r2^r)=o(B/N).}                        \tag{0.5}
   \]

   Therefore the gap-seven/defect-one three-cycle cannot be iterated into
   a critical counterexample.

3. A genuine reduced predecessor passage ending at time \(g\) has the
   exact phase localization

   \[
    \boxed{2\le p-\kappa_g\le g+1.}                 \tag{0.6}
   \]

   Componentwise phase homomesy gives only bistochastic lag matrices; it
   does not bound their cyclic diagonals and hence gives no useful bound on
   the mass in (0.6).

4. Row-coherently joining the positive and zero defects does not create
   the missing phase clustering. A signed packet arising from a gap
   \(g=2s+1\) occupies exactly \(K=g+2\) consecutive underlying PBBS
   transition positions. Its rotation deck contains at least

   \[
    \boxed{\frac{N}{2(g+2)}\ge\frac{N}{4H+2}}       \tag{0.7}
   \]

   pairwise edge-disjoint signed translates; on a nonwrapping quotient
   trace all \(N\) translates are disjoint.

5. The proposed local phase-deck splice is rigid on all but an
   exponentially negligible family of owners. If \(\rho\) is the
   coordinate rotation and a nonzero phase shift can create a Johnson
   seam between ports at Johnson distance at most \(L\), then the tail
   owner \(X\) satisfies

   \[
    |X\triangle\rho^sX|\le2L+2.                    \tag{0.8}
   \]

   For \(L=O_A(\sqrt N)\), the number of such owners, summed over all
   \(s\ne0\), is at most

   \[
    \boxed{2^{N/3+o_A(N)}.}                         \tag{0.9}
   \]

   Consequently an exponentially large, genuine mountain-tower family of
   Gaussian-short PBBS intervals has no nonzero-phase seam between two
   same-arm local ports, or more generally between ports whose unrotated
   owners have Johnson distance at most \(H+1\). This closes same-cut and
   same-arm local-packet phase permutation as a universal repair, but not
   cross-parity, cross-orbit, or distant mixed-orientation sewing.

6. On any positive-mass two-dimensional Pascal saddle tube, let
   \(\alpha_{A,r}\) be the outer-fibre-weighted fraction of roots produced
   by bounded-slot predecessor passages of time at most \(2H-1\). Then

   \[
    \boxed{
    \frac{\nu_H(P_r)}B
      \ge c_A\sqrt r\,\alpha_{A,r}-o_A(1).}         \tag{0.10}
   \]

   Thus \((\mathrm{RP}_A)\) requires

   \[
    \boxed{\alpha_{A,r}=o_A(r^{-1/2}).}             \tag{0.11}
   \]

   Phase-uniform scale \(\Theta(r^{-1/2})\) is exactly critical and would
   refute \((\mathrm{RP}_A)\), not prove it.

7. A single two-edge row-coherent atom has a diagonal-only q1
   lower/upper containment graph. Any two seams preserving its two lower
   colors and its two upper colors are exactly the old edges. Thus a
   productive q1-neutral splice must transport colors through other atoms;
   atomwise repair is impossible.

The exact unresolved input is therefore a PBBS-specific two-point or
action-variable theorem: either prove the subcritical passage density
(0.11), together with enough quotient clustering to reach (0.1), or
construct a critical saddle family and disprove \((\mathrm{RP}_A)\).
Neither phase marginals, row-coherent atoms, Pascal slot factors, nor local
phase-deck splicing supplies that theorem.

## 1. Quotient normalization and the best unconditional upper bound

Let \(Z_H\) denote the quotient edges on step-two quotient cycles of
length at most \(H+1\). The exact deck sandwich is

\[
 N\overline\nu_H
 \le\nu_H(P_r)
 \le\tau_H(P_r)
 \le2N\overline\nu_H+NZ_H.                         \tag{1.1}
\]

Moreover

\[
 Z_H\le(2H+2)N^{2H+2}.                             \tag{1.2}
\]

For fixed \(A\) and \(H=\lceil A\sqrt r\rceil\), (1.2) is
\(\exp(o_A(r))\), while \(B=\exp(r\log4-O(\log r))\). Hence
\(NZ_H=o_A(B)\), and (1.1) proves (0.1) in both directions.

For completeness, the optimized height/volume split gives (0.2). Choose

\[
 L=\left\lfloor\frac\pi4
                 \sqrt{\frac r{\log r}}\right\rfloor.
\]

Every packed interval of residence at most \(L\) starts at a Dyck root of
height at most \(L-1\), so there are at most

\[
 \left(2\cos\frac\pi{L+1}\right)^{2r}
 \le4^r r^{-9}=O(Br^{-7})                          \tag{1.3}
\]

such starts for all sufficiently large \(r\). Every remaining packed
interval uses at least \(L+2\) of the \(B\) quotient edges, giving at most
\(B/(L+2)\) members. This proves

\[
 \overline\nu_H
 =O\!\left(B\sqrt{\frac{\log r}{r}}\right)          \tag{1.4}
\]

uniformly in \(H\). It is a real improvement over the earlier
\(B\log r/\sqrt r\) estimate, but it does not approach (0.1).

## 2. The exact Kac identity

Represent a physical PBBS transition by \((u,D)\in\mathbb Z_N\times
\mathcal D_r\), where \(u\) is its omitted physical coordinate and
\(D\) is the normalized Dyck root. Fix a coordinate \(x\), and let

\[
 \mathcal A_x=\{(u,D):u=x\}.
\]

Coordinate rotation identifies \(\mathcal A_x\) bijectively with
\(\mathcal D_r\), so \(|\mathcal A_x|=B\). Every PBBS component meets
\(\mathcal A_x\): on a component of length \(N\ell\), each omitted
coordinate occurs exactly \(\ell\) times by componentwise coordinate
homomesy.

### Theorem 2.1 (Kac tower identity)

If \(g(D)\) is the first positive return time from the state in
\(\mathcal A_x\) indexed by \(D\) to \(\mathcal A_x\), then

\[
 \sum_{D\in\mathcal D_r}g(D)=NB.                  \tag{2.1}
\]

#### Proof

On one PBBS component, the successive occurrences of \(x\) split the
entire component into disjoint return towers. The sum of their heights is
the component length. Summing over all components gives the total number
\(NB\) of physical PBBS transitions. Under the rotation identification of
\(\mathcal A_x\) with \(\mathcal D_r\), those tower heights are precisely
the values \(g(D)\). \(\square\)

The corresponding projected positive residence is
\(\ell(D)=(g(D)+1)/2\). Therefore

\[
 \sum_D\ell(D)=\frac{NB+B}{2}=(r+1)B.              \tag{2.2}
\]

The identity cannot control the Gaussian lower tail. Long gaps can pay
for arbitrarily many short gaps. The genuine defect-one three-cycle is an
actual PBBS example with two short gaps and one compensating long gap per
label, while the mountain core \(1^d0^d\) has no predecessor passage
before its full particle circumference. Thus even inside PBBS, equal
phase marginals do not determine short-time behavior.

## 3. Complete solution of the defect-one passage class

For \(d\ge2\), every defect-one Dyck root has a unique representation

\[
 E(a,b,c)=(10)^a1(10)^b0(10)^c,
 \quad a,c\ge0,\quad b\ge1,\quad a+b+c=d-1.         \tag{3.1}
\]

Put \(p=2d+1\), and normalize the reduced omitted particle at time zero to
zero.

### Lemma 3.1 (affine three-phase itinerary)

For every \(j\in\mathbb Z\), before reduction modulo \(p\),

\[
 \boxed{
 \begin{aligned}
  \kappa_{3j}&=j,\\
  \kappa_{3j+1}&=j+2(a+1),\\
  \kappa_{3j+2}&=j-1-2c
 \end{aligned}}
 \pmod p.                                          \tag{3.2}
\]

#### Proof

Direct substitution in the rooted-Dyck PBBS map gives

\[
 \phi E(a,b,c)=E(b-1,c+1,a),                       \tag{3.3}
\]

and hence

\[
 E(a,b,c)\mapsto E(b-1,c+1,a)
 \mapsto E(c,a+1,b-1)\mapsto E(a,b,c).             \tag{3.4}
\]

The three root displacements are respectively

\[
 2(a+1),\qquad2b,\qquad2(c+1),
\]

whose sum is \(p+1\equiv1\pmod p\). Summing these displacements from
phase \(3j\) proves (3.2). \(\square\)

### Theorem 3.2 (first return and first predecessor passage)

For the root (3.1), the next return of particle zero occurs at

\[
 h_E=6c+5,                                          \tag{3.5}
\]

and the first subsequent selection of its predecessor occurs at

\[
 g_E=6(b+c)+1.                                      \tag{3.6}
\]

There is exactly one earlier selection of the predecessor before time
\(g_E\), so

\[
 n_{-1}(g_E)=1,\qquad z_E(g_E)=0.                  \tag{3.7}
\]

#### Proof

In phase \(3j+2\), equation (3.2) equals zero first at \(j=2c+1\),
which gives (3.5). The possible phase-\(3j+1\) zero occurs later by
\(6b-1\), and the phase-\(3j\) zero occurs at time \(3p\), so (3.5) is
the first root return.

The phase-\(3j+2\) predecessor occurrence is at \(j=2c\), namely time
\(6c+2<h_E\). The next predecessor occurrence is in phase \(3j+1\),
where

\[
 j+2(a+1)\equiv-1\pmod p
 \quad\Longleftrightarrow\quad j=2(b+c),
\]

giving (3.6). The phase-\(3j\) predecessor occurs later. Thus exactly one
predecessor selection is counted before the endpoint, proving (3.7).
\(\square\)

Now lift a core of rank \(d\) to an outer root of semilength \(r\). Since
\(\operatorname{pk}(E)=d-1\), prescribing the empty final root slot leaves
exactly

\[
 K_r(E,0)=\binom r{2d-1}                            \tag{3.8}
\]

outer roots. Put \(T=\lfloor(H-1)/3\rfloor\). The condition
\(g_E\le2H-1\) is \(b+c\le T\). For a fixed
\(t=b+c\), there are exactly \(t\) choices of \((b,c)\), and then
\(d\ge t+1\). Hence the total Gaussian-short outer start mass arising
from all defect-one cores is at most

\[
 \begin{aligned}
 \sum_{t=1}^{T}t
 \sum_{d=t+1}^{\lfloor(r+1)/2\rfloor}\binom r{2d-1}
 &\le \left(\sum_{t=1}^{T}t\right)2^{r-1}\\
 &=O_A(r2^r).
 \end{aligned}                                      \tag{3.9}
\]

Since \(B/N\asymp4^r/r^{5/2}\), (3.9) is \(o(B/N)\). This proves (0.5)
and closes the obvious attempt to amplify the exact gap-seven family by
varying its defect-one phase parameters.

## 4. The Pascal saddle and the exact critical density

For a one-step peak-deletion core \(E\in\mathcal D_d\), put
\(k=\operatorname{pk}(E)\). The outer inverse-fibre mass of the complete
\((d,k)\)-cell is

\[
 \mathsf M_r(d,k)
 =\frac1d\binom dk\binom d{k-1}
   \binom{r+d-k}{2d}.                               \tag{4.1}
\]

Its saddle is

\[
 d=r/2,\qquad k=r/6.                                \tag{4.2}
\]

Uniformly for bounded

\[
 u=\frac{k-r/6}{\sqrt r},\qquad
 v=\frac{d-r/2}{\sqrt r},
\]

one has

\[
 \frac{\mathsf M_r(d,k)}B
 =\frac{9\sqrt2}{2\pi r}
   \exp\!\left[-\frac{81u^2-18uv+33v^2}{8}\right]
   (1+o(1)).                                        \tag{4.3}
\]

If the passage prescribes a fixed final slot \(z\), its exact retained
fraction is

\[
 \frac{K_r(d,k,z)}{P_r(d,k)}
 =\frac{2d}{r+d-k}
  \prod_{j=0}^{z-1}
  \frac{r-d-k-j}{r+d-k-1-j},                       \tag{4.4}
\]

and therefore

\[
 \frac{K_r(d,k,z)}{P_r(d,k)}\longrightarrow
 \frac34\,4^{-z}                                   \tag{4.5}
\]

through every bounded saddle tube. Thus a bounded slot costs a constant,
not an entropy factor.

The saddle localization can be made sharp at the required \(B/N\) scale.
Let

\[
 \lambda_*=\frac{57-3\sqrt{73}}4
\]

be the least eigenvalue of the negative Hessian of the entropy exponent at
the saddle. Uniform Stirling expansion gives, throughout
\(|d-r/2|+|k-r/6|=O(\sqrt{r\log r})\),

\[
 \frac{\mathsf M_r(d,k)}B
 \le \frac Cr
 \exp\!\left[-\frac{\lambda_*}{4}(u^2+v^2)\right]  \tag{4.5a}
\]

for all sufficiently large \(r\). Outside a fixed interior neighborhood,
strict concavity supplies a fixed exponential gap. Therefore, for every

\[
 C_0>\frac4{\sqrt{\lambda_*}}
 \quad\text{(in particular, }C_0=2\text{)},
\]

the total outer mass outside

\[
 |d-r/2|+|k-r/6|\le C_0\sqrt{r\log r}               \tag{4.5b}
\]

is \(o(B/N)\). Indeed, outside the tube
\(u^2+v^2\ge(C_0^2/2)\log r\); summing (4.5a) over at most \(r^2\)
cells still gives \(o(B/r)\). The third-order Taylor error in this range is
\(O((\log r)^{3/2}/\sqrt r)=o(1)\).

Likewise, conditional on \(d\ge r/4\), the exact weak-composition tail is

\[
 \Pr(z_*\ge L)
 =\frac{\binom{y-L+2d}{2d}}{\binom{y+2d}{2d}}
 \le\left(\frac35\right)^L,
 \qquad y=r-d-k.                                    \tag{4.5c}
\]

Taking \(L=\lceil3\log r\rceil\), and using the exponentially negligible
mass with \(d<r/4\), shows that all starts outside (4.5b) or with
\(z_*>3\log r+1\) have total mass \(o(B/N)\). Thus the expanding Pascal
saddle tube with logarithmic predecessor multiplicity is not merely a
heuristic location: it contains every potentially critical start up to the
full error allowed by (0.1).

Iterating the slot restriction does not create a hidden contraction. For a
pruning tower with ranks \(r_j\), prescribing the final root slot to be zero
at level \(j\) retains the exact fraction

\[
 q_j=\frac{2r_{j+1}}{r_j+r_{j+2}}.                 \tag{4.5d}
\]

On the harmonic profile \(r_j=R/(j+1)\),

\[
 q_j=1-\frac1{(j+2)^2},\qquad
 \prod_{j=0}^{L-1}q_j
 =\frac{L+2}{2(L+1)}\longrightarrow\frac12.        \tag{4.5e}
\]

For each finite \(L\), taking \(R\) to be a sufficiently large multiple
of \(\operatorname{lcm}(1,\ldots,L+2)\) realizes these ranks by an actual
ordered plane tree, with zero final slot at every displayed level. Thus
even an arbitrarily long compatible list of empty seam slots can retain
positive fibre mass. This is a no-go for slot-product arguments only: it
does not assert that the same trees satisfy compatible PBBS predecessor
passages.

Fix a bounded two-dimensional saddle rectangle with positive Gaussian
mass, and let \(S_{A,r}\) be the total number of outer roots in that
rectangle which start a predecessor passage of time at most \(2H-1\) and
have \(z\le z_0\), counted with the exact weights (4.4). Define

\[
 \alpha_{A,r}=S_{A,r}/B.                            \tag{4.6}
\]

There is at most one next return starting at a quotient edge. Circular
greedy packing of intervals of at most \(H+1\) edges, followed by the
full \(N\)-deck lift, gives

\[
 \nu_H(P_r)
 \ge\frac{N}{2H+1}(S_{A,r}-Z_H).                   \tag{4.7}
\]

Since \(Z_H=o_A(B/\sqrt r)\), (4.7) is exactly (0.10), with any fixed
constant \(c_A<1/A\) for all sufficiently large \(r\). In particular,
\((\mathrm{RP}_A)\) implies (0.11).

For comparison, the direct sufficient start-count condition is much
stronger:

\[
 R_H=o_A(B/N)\quad\Longrightarrow\quad
 \overline\nu_H=o_A(B/N).                          \tag{4.8}
\]

The interval between the necessary scale \(o(B/\sqrt r)\) and the
sufficient scale \(o(B/r)\) is exactly where a quotient clustering theorem
could operate. No such theorem is proved here.

## 5. Exact phase localization, and why homomesy stops there

Apply one further peak deletion to a reduced passage. Let the next particle
system have \(p=2e+1\) particles, selected itinerary \(\kappa_t\), and
selection counts

\[
 C_a(t)=\#\{0\le u<t:\kappa_u=a\}.
\]

Write its physical particle spacings as

\[
 q_a=1+\epsilon_a+2n_a,
\]

and let \(j=\kappa_g\), \(b=p-j\), and
\(\mathcal B(j)=\{j+1,\ldots,p-1,0\}\). The exact terminal-block equation
for a predecessor endpoint is

\[
 \sum_{a\in\mathcal B(j)}q_a=C_j(g)+1.             \tag{5.1}
\]

Since every \(q_a\ge1\),

\[
 b\le C_j(g)+1\le g+1.                             \tag{5.2}
\]

The case \(b=1\) is impossible: it would make \(j=p-1\), but that same
predecessor was already selected at the earlier root return, forcing its
count at time \(g\) to exceed the right side of (5.1). Hence

\[
 2\le p-\kappa_g\le g+1,                           \tag{5.3}
\]

which proves (0.6).

This is only a phase band, not a probability estimate. On a reduced PBBS
component of length \(L=p\ell\), let

\[
 M_t(a,b)=\#\{u:\kappa_u=a,\ \kappa_{u+t}=b\}.
\]

Componentwise phase homomesy gives the exact identities

\[
 \sum_bM_t(a,b)=\ell,
 \qquad
 \sum_aM_t(a,b)=\ell,                              \tag{5.4}
\]

and

\[
 \sum_{t=0}^{L-1}M_t(a,b)=\ell^2.                 \tag{5.5}
\]

Thus \(M_t/\ell\) is bistochastic. But the endpoint displacement in
(5.3) is measured by the cyclic diagonal

\[
 \sum_aM_t(a,a+j),                                 \tag{5.6}
\]

not by a row or column marginal. A bistochastic matrix may put all its
mass on one cyclic diagonal. Consequently (5.4)-(5.5) give neither an
\(O(g/p)\) band estimate nor the required \(o(g/p)\) estimate. This is
the exact point at which bare phase symmetry stops.

## 6. Row-coherent signed packets retain a large phase packing

Let an omitted label have consecutive gap \(g=2s+1\). On one projected
parity it produces a positive interval of \(s+2\) transition edges; on the
opposite parity it produces the synchronized zero interval of \(s+1\)
transition edges. Their union in the underlying one-step PBBS cycle is one
consecutive packet of exactly

\[
 K=g+2=2s+3                                           \tag{6.1}
\]

transition positions.

Let the physical PBBS component containing the packet have length \(M\),
and let its coordinate-rotation stabilizer have order \(h\). Put

\[
 d=M/h.
\]

There are \(N/h\) rotated components, while the \(h\) rotations which
remain on one component shift the packet start by exactly \(d\) positions.

### Theorem 6.1 (exact signed translate packing)

If \(K<M\), the maximum number of pairwise edge-disjoint coordinate
rotations of the complete signed packet is

\[
 \boxed{
 \frac Nh
 \left\lfloor
 \frac{h}{\lceil K/d\rceil}
 \right\rfloor.}                                   \tag{6.2}
\]

In particular it is at least \(N/(2K)\). If \(d\ge K\), it equals \(N\).

#### Proof

Rotations in distinct rotated components are automatically disjoint. On
one component, consecutive stabilizer rotations start \(d\) positions
apart. A packet of length \(K\) occupies
\(q=\lceil K/d\rceil\) consecutive start blocks, so the independence
number of the cyclic \(q\)-interval system on the \(h\) starts is exactly
\(\lfloor h/q\rfloor\). This proves (6.2).

Since \(K<M=hd\), one has \(q\le h\). Thus
\(\lfloor h/q\rfloor\ge h/(2q)\), and \(q\le K\), proving the uniform
lower bound. If \(d\ge K\), then \(q=1\), giving all \(N\) rotations.
\(\square\)

For a radius-\(H\) defect, \(g\le2H-1\), so \(K\le2H+1\), and (6.2)
gives (0.7). Therefore synchronizing the two signs does not collapse a
phase deck to bounded capacity. On every nonwrapping quotient trace it
does not collapse it at all.

## 7. Phase-deck Johnson rigidity

Let \(\rho\) be cyclic coordinate rotation on \([N]\). For an integer
\(K\ge0\), define

\[
 \mathcal E_{N,K}
 =\{X\subseteq[N]:
   |X\triangle\rho^tX|\le K
   \text{ for some }t\not\equiv0\pmod N\}.         \tag{7.1}
\]

### Lemma 7.1 (small rotational-boundary count)

For odd \(N\),

\[
 \boxed{
 |\mathcal E_{N,K}|
 \le (N-1)2^{N/3}
       \sum_{j=0}^{K}\binom Nj.}                   \tag{7.2}
\]

Consequently, for \(K=O_A(\sqrt N)\),

\[
 |\mathcal E_{N,K}|\le2^{N/3+o_A(N)}.              \tag{7.3}
\]

#### Proof

Fix \(t\ne0\), and put \(\sigma=\rho^t\). The permutation \(\sigma\)
has \(c=\gcd(t,N)\) cycles, all of odd length at least three. Hence
\(c\le N/3\).

For a subset \(X\), the set of transition positions

\[
 T_X=\{x:1_X(x)\ne1_X(\sigma x)\}
\]

has size \(|X\triangle\sigma X|\). Once \(T_X\) and one initial bit on
each \(\sigma\)-cycle are given, all of \(X\) is determined. Therefore
the number with \(|T_X|\le K\) is at most

\[
 2^c\sum_{j=0}^{K}\binom Nj
 \le2^{N/3}\sum_{j=0}^{K}\binom Nj.
\]

Sum over the \(N-1\) nonzero shifts to get (7.2). If
\(K=O_A(\sqrt N)\), the logarithm of the binomial sum is
\(O_A(\sqrt N\log N)=o_A(N)\), proving (7.3). \(\square\)

### Theorem 7.2 (local nonzero-phase seam obstruction)

Let \(X\) be a tail port and \(Y\) a head port of the same rank, with
Johnson distance at most \(L\). If

\[
 \rho^uX\longrightarrow\rho^vY
\]

is a Johnson seam with nonzero phase difference
\(t=v-u\), then

\[
 X\in\mathcal E_{N,\,2L+2}.                        \tag{7.4}
\]

#### Proof

Johnson adjacency of the seam gives
\(|X\triangle\rho^tY|=2\). Rotation preserves symmetric difference, so

\[
 |X\triangle\rho^tX|
 \le |X\triangle\rho^tY|
    +|\rho^tY\triangle\rho^tX|
 =2+|Y\triangle X|
 \le2L+2.                                          \tag{7.5}
\]

This is (7.4). \(\square\)

For one original quotient cut \(X\to Y\), take \(L=1\). If
\(X\notin\mathcal E_{N,4}\), the bipartite Johnson graph between the two
phase decks

\[
 \{\rho^uX:u\in\mathbb Z_N\},
 \qquad
 \{\rho^vY:v\in\mathbb Z_N\}
\]

has only the original phase edges \(u=v\). Hence its unique perfect
matching is the identity. This excludes not only a uniform shift but an
arbitrary phase matching at that cut.

The same conclusion holds for any pair of ports in an \(H\)-local packet
whose unrotated owners have Johnson distance at most \(H+1\), whenever its
tail avoids \(\mathcal E_{N,2H+4}\). In particular this covers ports on
one projected parity arm. It does not cover a cross-parity pair: consecutive
underlying odd-graph owners can have Johnson distance \(r\). By (7.3), the
exceptional owner set has size \(2^{N/3+o_A(N)}\).

Now use the genuine mountain-tower quotient packing with
\(d=L\asymp r^{1/3}\). For every fixed \(A>0\), its intervals have
residence below \(H\) and contain an edge-disjoint subfamily of size

\[
 B\exp[-C r^{1/3}+o(r^{1/3})].                     \tag{7.6}
\]

Because the intervals in (7.6) are quotient-edge-disjoint, at most two of
them can meet a fixed exceptional quotient owner through an interval
boundary (and at most one can contain its chosen outgoing edge).
Equations (7.3) and (7.6) show that deleting every interval which meets an
exceptional owner changes (7.6) by a negligible relative amount. Every
remaining interval has no nonzero-phase Johnson seam between same-arm
\(H\)-local ports, or between any other local ports whose unrotated owners
have Johnson distance at most \(H+1\).

This is an exact obstruction to the proposed local phase-permutation
absorber. It is not a counterexample to \((\mathrm{RP}_A)\), because
(7.6) is still \(o(B/N)\).

There is also an ownerwise color rigidity which is independent of the
exception count. Work inside the \(N\) spatial phases of one fixed quotient
cut, and write its phase-\(j\) old edge as

\[
 A_j\longrightarrow B_j=A_j-r_j+a_j,
\]

with lower color \(S_j=A_j-r_j\) and upper color
\(U_j=B_j+r_j\). If a forward-polarized seam
\(A_j\to B_k\) is required to retain the pair \((S_j,U_k)\), then
\(r_j=r_k\), hence \(j=k\). Indeed \(r_j\) is the unique member of
\(U_k\setminus B_k\), and the rotated departure labels in this one deck
are distinct. The reverse-polarized statement similarly forces
\(a_j=a_k\) and again \(j=k\). Thus every same-sign, ownerwise
q1-preserving phase-deck matching is the original matching. Global
multiset trades mixing signs, cross-parity ports, or different quotient
cuts are outside this ownerwise statement; distant PBBS edges can share a
departure label.

### Proposition 7.3 (one row-coherent atom has no q1-neutral repair)

Let \(A_i\) be the rank-\(r\) PBBS odd states on a ground set \(Q\) of
size \(2r+1\), let

\[
 \lambda_i=Q\setminus(A_i\cup A_{i+1}),
 \qquad X_i=Q\setminus A_i,
\]

and let the projected step-two edge be

\[
 E_t=X_{t-1}X_{t+1}.
\]

Write its lower and upper colors as

\[
 L_t=X_{t-1}\cap X_{t+1},
 \qquad U_t=X_{t-1}\cup X_{t+1}.
\]

For \(r\ge2\), the containment graph from the two lowers
\(\{L_t,L_{t+1}\}\) to the two uppers
\(\{U_t,U_{t+1}\}\) consists of exactly the two diagonal edges. Hence any
two Johnson seams whose lower-color multiset and upper-color multiset equal
those of \(\{E_t,E_{t+1}\}\) are precisely the two old edges
\(E_t,E_{t+1}\).

#### Proof

The PBBS recurrence

\[
 A_{i+2}=A_i-\lambda_{i+1}+\lambda_i
\]

gives

\[
 \begin{aligned}
 L_t&=X_{t+1}\setminus\{\lambda_t\}=A_t,\\
 U_t&=X_{t+1}\cup\{\lambda_{t-1}\},\\
 L_{t+1}&=X_t\setminus\{\lambda_t\}=A_{t+1},\\
 U_{t+1}&=X_t\cup\{\lambda_{t+1}\}.
 \end{aligned}                                      \tag{7.7}
\]

The diagonal containments hold because each old Johnson edge has its own
lower contained in its own upper. On the cross pairs,

\[
 A_t\cap U_{t+1}=\{\lambda_{t+1}\},
 \qquad
 A_{t+1}\cap U_t=\{\lambda_{t-1}\}.                 \tag{7.8}
\]

Since \(|A_t|=|A_{t+1}|=r\ge2\), neither cross lower is contained in the
opposite upper. This proves the diagonal-only assertion.

A Johnson edge is uniquely determined by its intersection \(L\) and union
\(U\): its endpoints are the two intermediate sets between \(L\) and
\(U\). Preserving the two lower and two upper inventories therefore
permits only a perfect matching in the displayed containment graph, which
is the identity. Thus the two replacement seams are the old edges.
\(\square\)

More generally, let \(D\) be any deleted edge set with injective lower and
upper colors, and replace it by the same number of q1-inventory-preserving
seams. The new seams pair the deleted lowers with the deleted uppers by a
permutation. A fixed point restores its old edge; every productive part is
a color-transport cycle of length at least two. Proposition 7.3 says that
the two members of one row-coherent atom cannot be consecutive in such a
cycle. Hence every active atom must transport color to another atom.
Cross-atom and distant transport remain possible and require separate
Johnson, \(H\)-collar, and higher-depth tests.

### Corollary 7.4 (what a q1-neutral resewing can change)

Start with a PBBS forest having \(p\) directed path components. Delete
\(c\) old directed edges and add \(s\) seams. Exact preservation of either
complete q1 occurrence histogram forces

\[
 s=c.                                                \tag{7.9}
\]

If the seam set is acyclic, the final number of paths is therefore exactly

\[
 p+c-s=p.                                           \tag{7.10}
\]

Indeed every old or new edge contributes one lower and one upper q1
occurrence, so equality of either total histogram mass gives \(s=c\).
Deleting \(c\) forest edges creates \(p+c\) paths, and every acyclic seam
reduces their number by one. Thus q1-neutral resewing can absorb all
cut-created components, but it cannot reduce the original path count.

This is only a ledger theorem. A matching of admissible port pairs must
still satisfy the Johnson containment conditions and signed \(H\)-memory.
When every inter-seam retained fragment has at least \(H\) transitions,
the usual seam collars are sufficient; for shorter fragments, a forbidden
residence pair may cross several seams, so pairwise Hall feasibility alone
is not sufficient.

## 8. Independent audit and precise open boundary

The decisive constants were rederived independently.

1. A residence-\(H\) quotient interval has at most \(H+1\) edges. Its
   circular conflict neighborhood has at most \(2H+1\) possible starts,
   which is the denominator in (4.7). There is no missing parity factor.

2. In Lemma 3.1, the three displacements sum to \(p+1\), not \(p\).
   This is why the affine phase advances by one every three PBBS steps.
   The phase-\(3j+2\) predecessor occurrence at \(6c+2\) is before the
   root return \(6c+5\); the next one at \(6(b+c)+1\) is therefore the
   first admissible passage endpoint and has slot exactly zero.

3. The signed packet size is \(g+2\), not \(g+1\). This gives the uniform
   translate bound \(N/(4H+2)\) in (0.7).

4. In Lemma 7.1, every nontrivial rotation of an odd \(N\)-cycle has at
   most \(N/3\) cycles. The free initial-bit factor is therefore
   \(2^{N/3}\), and the remaining transition-set entropy is only
   \(\exp(O_A(\sqrt N\log N))\).

5. The phase-deck obstruction is local in Johnson distance. It closes a
   matching of the phases of one cut, and same-arm packet splices whose
   unrotated port owners stay within Johnson distance \(H+1\). It does not
   close a cross-parity local seam, a seam between unrelated distant
   quotient cuts, a three-port color trade, or a mixed-orientation
   cross-orbit construction.

6. Proposition 7.3 is atomwise only. It proves that a q1-neutral repair
   cannot close inside one two-edge row atom; it does not rule out a
   color-transport cycle using three or more ports from different atoms.

7. Corollary 7.4 is a component ledger, not an existence theorem for a
   safe seam matching. Short inter-seam fragments retain associative
   \(H\)-memory constraints which are invisible to pairwise Hall tests.

The final theorem boundary is therefore:

* proved: (0.1)--(0.10), including the optimized quotient upper bound,
  exact Kac identity, complete defect-one passage formula, phase
  localization, signed-deck packing, and the local phase-splice
  obstruction;
* necessary for \((\mathrm{RP}_A)\): subcritical
  \(o_A(r^{-1/2})\) weighted bounded-slot passage density in every
  positive-mass Pascal saddle tube; any successful direct clustering proof
  must imply this necessity, and must additionally reach the quotient
  packing scale in (0.1);
* sufficient by direct counting: \(R_H=o_A(B/N)\);
* unproved: the passage-density estimate, the intervening clustering
  theorem, and \((\mathrm{RP}_A)\) itself.

No constant-one theorem is claimed.
