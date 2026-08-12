# Markov descent inside an exact owner fibre

Date: 2026-07-25

Pure mathematics only. No computation, solver, or web input is used.

## 0. Verdict

Complementary-segment rectangle flips do define genuine moves inside one
exact middle-owner fibre. For a separation \(r=m\pm q\), \(q>0\), every
flip preserves the complete middle-owner multiset and every point marginal
at rank \(r\), while changing the rank-\(r\) load by one elementary
rectangle.

There is, however, no unconditional Lyapunov, spectral, or convex-descent
theorem based only on those fixed point marginals.

1. The projection of the chain to the middle-owner multiset is constant.
   The nontrivial observable is the shallow rank load inside that owner
   fibre.
2. At each of the first shallow ranks \(m-1\) and \(m+1\), there are exact
   \(W\)-occurrence multisets whose point degrees differ from perfect balance
   by less than two, whose duplicate mass is \(W-O(m)\), and from which no
   elementary rectangle move is legal. Thus the load-fibre rectangle graph
   can have a high-energy isolated vertex.
3. A reversible spectral gap only drives the chain toward its stationary
   mean. Point margins do not make that mean small, and a Gibbs tilt cannot
   cross a disconnected load class.
4. There is an exact positive result under a much stronger *commuting packed
   hypercube* hypothesis. If \(K\) independently flippable physical
   rectangles have load vectors \(\tau_j\), all \(2^K\) choices preserve the
   same exact owner multiset, and \(b\) is their load barycenter, then the
   fair flip chain has stationary collision expectation

   \[
      \Phi_{\mathbb R}(b)+\frac K2.                       \tag{0.1}
   \]

   Hence a low-collision barycenter and \(K=o(W)\) give a deterministic
   choice with collision \(o(W)\), as well as a fair Markov chain which
   reaches that scale in expectation.

The phrase “many packed rectangles per top” therefore does not by itself
close the lane. What is needed is either:

* a product packing of \(K=o(W)\) rectangles whose barycenter already has
  \(o(W)\) shallow collision; or
* for a larger nonlinear packing, a genuine coercive drift/availability
  theorem not implied by point margins.

The first alternative is a rounding theorem, not a mechanism which repairs
a linear initial duplicate deficit. Every elementary rectangle can remove
at most two duplicate occurrences, so reducing duplicate mass
\(\Theta(W)\) to \(o(W)\) requires \(\Omega(W)\) net rectangle moves.

## 1. Loads, margins, and the arithmetic floor

Let \(V=[2m]\), let

\[
 \Omega_r=\binom Vr,
\]

and write \(x_S\in\mathbb Z_{\ge0}\) for the number of selected rank-\(r\)
occurrences with mask \(S\). Put

\[
 L=\sum_{S\in\Omega_r}x_S,
 \qquad
 d_i(x)=\sum_{S\ni i}x_S.                              \tag{1.1}
\]

The two collision statistics are

\[
 C(x)=\sum_S\binom{x_S}{2},
 \qquad
 D(x)=\sum_S(x_S-1)_+.                                 \tag{1.2}
\]

Here \(C\) is pair collision and \(D\) is the exact number of duplicate
occurrences after retaining one copy of every occupied mask.

For the unperturbed packet count \(L=W=\binom{2m}{m}\), the number of cells
at rank \(r=m\pm q\) is

\[
 N_q=\binom{2m}{m-q}
 =W\prod_{j=1}^q\frac{m-j+1}{m+j}.                    \tag{1.3}
\]

If \(q=o(\sqrt m)\), then

\[
 \log\frac{N_q}{W}=-\frac{q^2}{m}
   +O\left(\frac{q^2}{m^2}+\frac{q^4}{m^3}\right),     \tag{1.4}
\]

so \(W-N_q=(1+o(1))Wq^2/m\). In the range \(W<2N_q\),
convexity gives the exact unconstrained floor

\[
 \min_{\sum x_S=W} C(x)=W-N_q.                         \tag{1.5}
\]

Thus each fixed \(q=o(\sqrt m)\) permits \(C=o(W)\). If the energy is
summed over every \(1\le q\le Q=o(\sqrt m)\), however, its unavoidable
two-sided arithmetic floor is

\[
 \Theta\left(\frac{WQ^3}{m}\right).                    \tag{1.6}
\]

Consequently a total shallow-band collision target \(o(W)\) already
requires \(Q=o(m^{1/3})\). For larger \(Q\), only a floor-corrected energy
can reasonably be required to be \(o(W)\).

Segment overlaps replace \(L=W\) by \(W+o(W)\). This changes none of the
obstructions or little-oh criteria below.

## 2. Exact rectangle calculus inside the owner fibre

For \(|K|=r-2\) and distinct \(a,b,c,d\notin K\), an oriented elementary
rectangle is

\[
 \tau=e_{Kbc}+e_{Kad}-e_{Kac}-e_{Kbd}.                 \tag{2.1}
\]

It satisfies

\[
 \sum_S\tau_S=0,
 \qquad d_i(\tau)=0\quad(i\in V).                      \tag{2.2}
\]

The move \(x\mapsto x+\tau\) is legal in the load fibre precisely when
\(x_{Kac},x_{Kbd}\ge1\). Its pair-collision change is

\[
 \boxed{
 C(x+\tau)-C(x)
 =x_{Kbc}+x_{Kad}-x_{Kac}-x_{Kbd}+2.}                  \tag{2.3}
\]

Indeed, adding one to a cell of load \(u\) costs \(u\), while subtracting
one from a cell of load \(v\) gains \(v-1\).

The duplicate mass can decrease only at the two cells from which a unit is
removed. Therefore

\[
 D(x)-D(x+\tau)\le2.                                   \tag{2.4}
\]

In particular, any path from \(D(x)=\Theta(W)\) to \(D=o(W)\) uses
\(\Omega(W)\) rectangle steps.

For the top-segment absorber with swap-cut separation \(r=m\pm q\), \(q>0\),
the companion nonzero rank is \(M-r=H\mp q\), and the length-\(m\) mixed
difference is zero. The segment identity therefore gives, exactly,

\[
 \text{middle-owner multiset before flip}
 =\text{middle-owner multiset after flip}.             \tag{2.5}
\]

Thus the owner projection of the proposed Markov chain is a single point.
The genuine state variable is the packet realization, and \(x\) is a
shallow-load observable on that exact owner fibre.

If a Markov kernel chooses an available oriented rectangle \(\tau\) at
state \(x\), its exact one-step drift is obtained by averaging (2.3):

\[
 \mathcal LC(x)
 =\mathbb E_x\bigl[\langle x,\tau\rangle+2\bigr],       \tag{2.6}
\]

where every rectangle has \(\|\tau\|_2^2=4\). A Foster theorem would need
a bound of the form

\[
 \mathcal LC(x)\le-\eta C(x)+b,
 \qquad b/\eta=o(W).                                   \tag{2.7}
\]

Nothing in (2.2), by itself, controls the sign of (2.6).

## 3. A balanced frozen state at depth one

The positivity obstruction is present even with essentially ideal point
degrees.

### Theorem 3.1 (near-balanced isolated high-collision load)

Let \(m\ge4\), let \(r=m-1\), and let \(L\ge2m\). There is a rank-\(r\)
load \(x\) of total mass \(L\) such that:

1. every point degree differs from the average \(rL/(2m)\) by less than
   two;
2. no elementary rectangle move is legal from \(x\);
3. \(D(x)=L-2m\); and
4. if \(L/m\to\infty\), then

   \[
      C(x)=(1+o(1))\frac{L^2}{4m}.                     \tag{3.1}
   \]

The same statement holds at rank \(m+1\).

#### Proof

Partition \(V=X\sqcup Y\) with \(|X|=|Y|=m\), and take the \(2m\) blocks

\[
 \mathcal F_-=\{X-\{a\}:a\in X\}
       \cup\{Y-\{b\}:b\in Y\}.                        \tag{3.2}
\]

Write \(L=2mt+s\), \(0\le s<2m\). Give every block multiplicity \(t\),
and give one additional copy to \(s\) blocks, choosing
\(\lceil s/2\rceil\) of them from the \(X\)-family and
\(\lfloor s/2\rfloor\) from the \(Y\)-family.

For \(z\in X\), if \(\delta_z\in\{0,1\}\) records whether \(X-\{z\}\)
received an extra copy, then

\[
 d_z(x)=(m-1)t+\lceil s/2\rceil-\delta_z.              \tag{3.3}
\]

There is the analogous formula with \(\lfloor s/2\rfloor\) on \(Y\).
Comparison with

\[
 \frac{(m-1)L}{2m}=(m-1)t+\frac{(m-1)s}{2m}            \tag{3.4}
\]

shows that the discrepancy is less than two.

Two distinct blocks on the same side of (3.2) meet in \(m-2=r-1\)
points, while two blocks on opposite sides are disjoint. The two negative
cells of any elementary rectangle meet in exactly \(r-2=m-3\) points.
For \(m\ge4\), neither intersection type in (3.2) equals \(r-2\).
Therefore no rectangle can subtract from two occupied cells, and the state
is isolated.

All \(2m\) support cells are occupied for \(t\ge1\), whence

\[
 D(x)=L-2m.                                              \tag{3.5}
\]

Balancing \(L\) among \(2m\) cells gives (3.1).

Finally take complements of all blocks in (3.2). They have size \(m+1\),
the same symmetric differences, and complementary point degrees
\(L-d_z(x)\). The rank-\((m+1)\) rectangle source pairs would have
intersection \(m-1\); the complemented same-side pairs meet in \(m\)
points and the cross pairs in two points. These are different from
\(m-1\) for \(m\ge4\). This proves the upper-rank statement. \(\square\)

Taking \(L=W\) gives a frozen state with exact packet-scale mass, point
degrees within two of balanced, and

\[
 D(x)=(1-o(1))W,
 \qquad C(x)\asymp W^2/m.                              \tag{3.6}
\]

Hence elementary rectangles are not a positive Markov basis for the
nonnegative point-margin fibre. Their signed lattice span may equal the
entire zero-margin lattice while their nonnegative move graph is
disconnected, even at depth one.

This example need not itself be the projection of a calibrated packet
near-factor. Its role is exact: no theorem whose hypotheses mention only
total mass and point margins can prove descent for the physical subclass.
One must use a further packet-availability or packed-product hypothesis.

## 4. What a spectral gap can and cannot prove

Let \(P\) be a finite lazy reversible Markov kernel on one communicating
class \(\mathcal C\), with stationary law \(\pi\) and spectral gap
\(\gamma\). For every observable \(F\), the gap controls convergence to
\(\pi F\); for example,

\[
 |P^tF(x)-\pi F|
 \le(1-\gamma)^t
 \sqrt{\operatorname{Var}_\pi(F)\bigl(\pi(x)^{-1}-1\bigr)}.              \tag{4.1}
\]

Thus a gap estimate has energy content only after proving

\[
 \pi C=o(W).                                             \tag{4.2}
\]

Theorem 3.1 gives a one-state class with gap conventionally vacuous and
stationary collision (3.6). More generally, a Metropolis tilt
\(\pi_\beta(x)\propto e^{-\beta C(x)}\) concentrates near the minimum of
\(C\) inside the same class, but neither creates connectivity nor proves
that the class minimum is \(o(W)\). Spectral language therefore cannot
replace the positivity/communicating-class theorem.

## 5. Exact theorem for a commuting packed hypercube

There is a clean theorem when “packed” has a strong literal meaning.
Suppose \(K\) physical complementary-segment gadgets are independently
flippable. Assume:

1. every sign vector \(\sigma\in\{-1,+1\}^K\) is a genuine packet
   configuration;
2. all these configurations have the same exact middle-owner multiset;
3. gadget \(j\) has a fixed shallow-load effect
   \(\tau_j\), independent of all other signs; and
4. in the observed direct sum of shallow ranks, each \(\tau_j\) is one
   rank-isolated rectangle. Its companion effect lies outside the observed
   band.

Then the aggregate shallow load is

\[
 x(\sigma)=b+\frac12\sum_{j=1}^K\sigma_j\tau_j,          \tag{5.1}
\]

where \(b\) is the barycenter. Every \(x(\sigma)\) is integral and
nonnegative by physicality, although \(b\) may be half-integral. Since
\(\partial\tau_j=0\), all point marginals are independent of \(\sigma\).

For several ranks, define the aggregate pair energy and its real quadratic
extension by

\[
 \Phi(x)=\sum_{q,S}\binom{x_{q,S}}2,
 \qquad
 \Phi_{\mathbb R}(y)=\frac12\|y\|_2^2
       -\frac12\sum_q L_q,                             \tag{5.2}
\]

where \(L_q=\sum_Sx_{q,S}\) is fixed. Every rectangle has squared norm
four in this direct sum.

### Theorem 5.1 (exact fair-chain energy formula)

Run independent sign-flip clocks, each at rate \(1/K\), starting at a
deterministic \(\sigma^0\). Put

\[
 \rho_t=e^{-2t/K},
 \qquad y_0=x(\sigma^0)-b.
\]

Then

\[
 \boxed{
 \mathbb E\Phi(x(\sigma_t))
 =\Phi_{\mathbb R}(b+\rho_ty_0)
   +(1-\rho_t^2)\frac K2.}                            \tag{5.3}
\]

In particular the chain has spectral gap \(2/K\), its stationary law is
uniform on the sign cube, and

\[
 \boxed{
 \mathbb E_\pi\Phi
 =\Phi_{\mathbb R}(b)+\frac K2.}                       \tag{5.4}
\]

Consequently

\[
 \min_{\sigma}\Phi(x(\sigma))
 \le\Phi_{\mathbb R}(b)+\frac K2.                      \tag{5.5}
\]

#### Proof

At time \(t\), the signs are independent, with

\[
 \mathbb E\sigma_j(t)=\rho_t\sigma_j^0,
 \qquad \operatorname{Var}\sigma_j(t)=1-\rho_t^2.
\]

Equation (5.1) gives

\[
 \mathbb Ex(t)=b+\rho_ty_0
\]

and

\[
 \operatorname{tr}\operatorname{Cov}(x(t))
 =\frac{1-\rho_t^2}{4}\sum_j\|\tau_j\|_2^2
 =(1-\rho_t^2)K.                                       \tag{5.6}
\]

Insert (5.6) into the quadratic extension (5.2). This proves (5.3).
Letting \(t\to\infty\) proves (5.4), and averaging proves (5.5).
\(\square\)

### Corollary 5.2 (conditional shallow smoothing)

If a physical commuting packing satisfies

\[
 K=o(W),
 \qquad
 \Phi_{\mathbb R}(b)+K/2=o(W),                         \tag{5.7}
\]

then some exact sign choice has aggregate shallow collision \(o(W)\), with
the middle-owner multiset and every shallow point marginal unchanged. The
fair chain approaches the same \(o(W)\) expected scale after
\(O(K\log W)\) time.

The \(K/2\) term is exact, not a proof loss. If \(K=\Theta(W)\), fair
spectral mixing has a linear noise floor even when the barycenter itself is
collision-free. A biased chain or deterministic signing may do better,
but that requires additional discrepancy or positive-drift structure.

## 6. Why many rectangles per top do not yet imply the theorem

At calibrated depth,

\[
 N_H=(1+o(1))W/m.                                      \tag{6.1}
\]

If \(p=O(Q)\) genuinely independent rectangles can be packed at each top,
then

\[
 K=O(QN_H)=O(WQ/m)=o(W)                                \tag{6.2}
\]

for \(Q=o(m)\). This is exactly the favorable range of Corollary 5.2:
the random-sign penalty is negligible.

But (6.2) also shows the limitation. The entire sign cube changes at most
\(2K=o(W)\) duplicate occurrences relative to any one vertex, by (2.4).
It cannot turn a state with a linear duplicate deficit into an \(o(W)\)
state. A \(p=O(Q)\) packing is therefore a final rounding/absorbing device,
not a replacement for the owner-only or shallow-load near-factor.

To obtain \(\Theta(W)\) net smoothing from rectangle moves one needs
\(\Theta(W)\) effective moves, hence \(p=\Theta(m)\) on average. At that
scale three new facts would have to be proved:

1. the many local four-order choices coexist in one physical packet rather
   than only as separate signed identities;
2. all choices retain the same exact middle-owner multiset; and
3. their interacting sign system has either a low-energy barycenter with a
   sublinear rounding penalty, or a coercive biased drift.

Pairwise rank isolation does not imply this product compatibility. Shared
adjacent swaps need not commute, and a single pair of long segment orders
does not automatically encode one independent bit for every algebraic
rectangle visible in its interval incidence.

## 7. The exact missing Markov gate

For a product packing, flipping bit \(j\) at state \(\sigma\) changes the
load by \(-\sigma_j\tau_j\). Equation (2.3) becomes

\[
 \Phi(\sigma^{(j)})-\Phi(\sigma)
 =-\sigma_j\langle x(\sigma),\tau_j\rangle+2.           \tag{7.1}
\]

A direct Lyapunov route would follow from the packet-specific inequality

\[
 \frac1K\sum_{j=1}^K
 \left[-\sigma_j\langle x(\sigma),\tau_j\rangle+2\right]
 \le-\frac\eta K\Phi(\sigma)+\frac{o(W)}K              \tag{7.2}
\]

above the desired floor. Standard stopping-time iteration would then drive
the expected energy to \(o(W)\).

Theorem 3.1 proves that (7.2) cannot be deduced from point margins on the
full nonnegative load fibre. Theorem 5.1 proves that for a fair product
chain the exact substitute is the barycenter condition (5.7). Thus the
honest new gate is:

> Construct, inside the owner near-transversal, a commuting physical packet
> packing whose barycenter has floor-corrected shallow collision \(o(W)\),
> or prove the statewise coercive inequality (7.2) for a biased selection of
> its available flips.

This gate includes availability, positivity, exact-owner preservation, and
quantitative descent. None of these follows from the already-proved signed
rectangle lattice theorem.

## 8. Audit ledger

### Proved

1. Rectangle flips preserve exact point margins and, for separation
   \(m\pm q\) with \(q>0\), the exact middle-owner multiset.
2. The exact collision increment is (2.3); one move removes at most two
   duplicate occurrences.
3. Point-margin load fibres can contain near-balanced, high-collision
   isolated states already at ranks \(m\pm1\).
4. Spectral convergence alone only reaches the communicating-class
   stationary mean.
5. A commuting physical sign cube has the exact energy evolution (5.3) and
   stationary penalty \(K/2\).
6. A low-energy barycenter plus \(K=o(W)\) yields an exact \(o(W)\)-collision
   choice while preserving all fixed marginals.
7. For \(p=O(Q)\) gadgets per calibrated top, \(K=O(WQ/m)=o(W)\), so this
   conditional rounding theorem has the correct coefficient-one scale.

### Not proved

1. Existence of a commuting product packing with many independent physical
   rectangle choices per top.
2. Low shallow collision of its barycenter.
3. A biased coercive drift such as (7.2) when the fair \(K/2\) floor is too
   large.
4. Any theorem that repairs a linear shallow duplicate deficit using only
   \(o(W)\) rectangle choices.

The Markov reformulation is therefore useful but sharply conditional. It
turns a low-energy fractional packet midpoint into a genuine exact choice;
it does not manufacture that midpoint from fixed point marginals.
