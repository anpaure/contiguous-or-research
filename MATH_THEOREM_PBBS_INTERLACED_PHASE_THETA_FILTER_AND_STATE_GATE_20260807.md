# Interlaced phases filter the PBBS theta alias, but require a new global chainization

**Date:** 2026-08-07
**Method:** Gaussian Poisson summation, roots-of-unity filtering, and exact
piece-census invariance
**Status:** unconditional analytic theorem and scope obstruction.  An ideal
uniform bank of \(Q\) slab phases changes

\[
4\sum_{a\ge1}e^{-4\pi a^2}
\quad\hbox{to}\quad
4\sum_{a\ge1}e^{-4\pi Q^2a^2}.
\]

Thus \(Q=O(\sqrt{\log d})=o(d)\) can make the positive Gaussian alias
\(o(1/d)\).  Merely colouring or reordering the existing two-endpoint
packets does not do this: it leaves the exact counts
\(P_{n,d},F_{n,d},g\) unchanged.  A genuine realization must rephase the
global deep-band fragmentation, handle integral cut ranks to better than
first order, and prove one common PBBS history.

There is no unconditional \(Q\)-state or \(Q\)-seam obstruction.  In a
shifted SCD fragmentation the phase can be recovered from the absolute cut
rank, so it need not be exported as a sidecar.  The physical status is
therefore open rather than negative.

The companion adaptive-phase fragmentation note proves a stronger exact
chain-level statement: for every \(Q\le d-2\), an almost-uniform integral
\(Q\)-grid of phases can be assigned by nested Hall to a positive-density
eligible chain bank, with no new pieces and no condition \(Q\mid d\).
That adaptive construction removes more than the whole theta deficit.  The
Fourier analysis below remains the exact answer for phase mixing
independent of chain remainders.

## 1. The theta constant is a lattice alias

Put

\[
G(x)=e^{-\pi x^2/4},
\qquad
\sigma=\sum_{a\ge1}G(a).
\]

The merged-piece rows give

\[
\frac{P_{n,d}}W\longrightarrow\sigma,\qquad
\frac{F_{n,d}}W\longrightarrow\sigma-G(1),\qquad
\frac gW\longrightarrow1-G(1).
\]

Since \(S_{n,d}=g-P_{n,d}\),

\[
\theta=\lim\frac{F_{n,d}-S_{n,d}}W=2\sigma-1.
\tag{1.1}
\]

Now \(G(0)=1\) and \(\int_{\mathbb R}G=2\).  Hence

\[
\boxed{
\theta=\sum_{a\in\mathbb Z}G(a)-\int_{\mathbb R}G(x)\,dx.}
\tag{1.2}
\]

Thus the theta barrier comes from the top-aligned slab lattice in the
piece census, not from collisions in the later two-endpoint packet
hypergraph.

## 2. Exact Fourier formula for arbitrary phases

Let \(\mu\) be a probability measure on \(\mathbb R/\mathbb Z\), with

\[
\widehat\mu(j)=\int e^{2\pi i j\phi}\,d\mu(\phi).
\]

Define

\[
\Theta(\mu)=
\int\left(\sum_{a\in\mathbb Z}G(a+\phi)-2\right)d\mu(\phi).
\tag{2.1}
\]

### Theorem 2.1 (phase Fourier law)

\[
\boxed{
\Theta(\mu)=
4\sum_{j\ge1}e^{-4\pi j^2}\operatorname {Re}\widehat\mu(j).}
\tag{2.2}
\]

#### Proof

The Fourier transform of \(G\) is

\[
\widehat G(\xi)=2e^{-4\pi\xi^2}.
\]

Poisson summation gives

\[
\sum_{a\in\mathbb Z}G(a+\phi)
=2\sum_{j\in\mathbb Z}e^{-4\pi j^2}e^{2\pi i j\phi}.
\]

The zero mode cancels the \(2\) in (2.1).  Integrate and pair \(j\) with
\(-j\). \(\square\)

This formula says exactly what phase interlacing must accomplish: it must
annihilate low Fourier modes of the slab lattice.

## 3. Uniform \(Q\)-phase filter

Let

\[
\mu_Q=\frac1Q\sum_{r=0}^{Q-1}\delta_{r/Q}.
\tag{3.1}
\]

Then

\[
\widehat\mu_Q(j)=\mathbf 1_{\{Q\mid j\}}.
\tag{3.2}
\]

### Theorem 3.1 (exact filtered theta)

\[
\boxed{
\theta_Q:=\Theta(\mu_Q)
=4\sum_{b\ge1}e^{-4\pi Q^2b^2}.}
\tag{3.3}
\]

Moreover,

\[
4e^{-4\pi Q^2}
\le \theta_Q
\le \frac{4e^{-4\pi Q^2}}{1-e^{-12\pi Q^2}},
\tag{3.4}
\]

and therefore

\[
\boxed{
\theta_Q=o(1/d)
\quad\Longleftrightarrow\quad
4\pi Q^2-\log d\longrightarrow+\infty.}
\tag{3.5}
\]

In particular, one may take

\[
Q^2=\frac{\log d+\omega(1)}{4\pi},
\qquad
\omega(1)\longrightarrow\infty.
\tag{3.6}
\]

#### Proof

Equations (3.2)--(3.3) follow from Theorem 2.1.  The first summand gives
the lower bound.  Since \(b^2\ge1+3(b-1)\) for \(b\ge1\), comparison with
a geometric series gives the upper bound. \(\square\)

The proposed dilution is therefore analytically valid and exponentially
stronger than the inverse-deadline scale.

## 4. Finite critical scale

For \(\beta>0\), the same calculation gives the exact Gaussian formula

\[
\boxed{
D_Q(\beta)
:=\frac1Q\sum_{r=0}^{Q-1}\sum_{a\in\mathbb Z}
e^{-\beta(a+r/Q)^2}-2
=\sqrt{\frac\pi\beta}-2
+2\sqrt{\frac\pi\beta}
\sum_{b\ge1}e^{-\pi^2Q^2b^2/\beta}.}
\tag{4.1}
\]

At \(\beta=\pi/4\), this is (3.3).  At the finite binomial scale put

\[
\beta_n=\frac{2d^2}{n}.
\tag{4.2}
\]

For \(n=2m+1\), let

\[
R_n=\frac{2^{n-1}-1}{\binom n m}.
\tag{4.3}
\]

The deadline definition yields

\[
d=R_n+\varepsilon_n,\qquad
-\frac{\binom{d+1}2}{W}\le\varepsilon_n<1.
\tag{4.4}
\]

Stirling expansion gives

\[
R_n^2=\frac{\pi n}{8}+\frac{3\pi}{16}+O(n^{-1}),
\tag{4.5}
\]

so

\[
\beta_n=\frac\pi4+\frac{\pi\varepsilon_n}{2d}+O(d^{-2}),
\qquad
\sqrt{\frac\pi{\beta_n}}-2
=-\frac{2\varepsilon_n}{d}+O(d^{-2}).
\tag{4.6}
\]

Thus the leading finite zero-mode correction is nonpositive, apart from
the exponentially small possible undershoot in (4.4).  For
\(Q^2=O(\log d)\), the Gaussian surrogate satisfies

\[
\boxed{
\bigl(D_Q(\beta_n)\bigr)_+
\le (1+o(1))\theta_Q+O(d^{-2}).}
\tag{4.7}
\]

This is not yet a finite PBBS census theorem.  The exact \(P\)- and
\(F\)-sums have half-integer centering and one-rank offsets.  The existing
notes prove only an \(o(1)\) local limit, whereas the filtered claim needs
a uniform second-order error \(o(1/d)\).

## 5. Post hoc packet phases do not change theta

### Theorem 5.1 (fixed-chainization invariance)

Fix the merged endpoint bank and the top-aligned length-\(d\) splitting
of the deep-band SCD.  Assign its pieces and endpoint chains to any number
\(Q\) of sectors, and reorder or interlace those sectors arbitrarily.  If
the set of pieces and the set of full pieces are unchanged, the exact
private-reset deficit remains

\[
\boxed{
F_{n,d}-S_{n,d}=F_{n,d}+P_{n,d}-g.}
\tag{5.1}
\]

In particular, adding phase labels to the existing fixed-coordinate,
multiseparator, or two-endpoint star packets does not replace \(\theta\)
by \(\theta_Q\).

#### Proof

Every piece consumes one of the \(g\) endpoint chains, leaving
\(S_{n,d}=g-P_{n,d}\).  Every full piece consumes one further private
reset under the audited rule.  Sector labels and chronological order
change none of \(P_{n,d},F_{n,d},g\). \(\square\)

Consequently the Fourier gain requires a new global statement:

> Partition the deep target band among \(Q\) chain families whose cut
> offsets have aggregate phase measure \(\mu_Q\), while preserving the
> exact per-rank census and one common literal PBBS history.

This is a rechainization theorem, not a refinement of the solved static
two-rail target packing.

## 6. Integral cut ranks

If an integral cut has within-slab displacement \(\delta\), its normalized
phase is \(\delta/d\).  For equal sectors with integral offsets
\(\delta_0,\ldots,\delta_{Q-1}\), Theorem 2.1 gives

\[
\boxed{
\Theta(\delta_0,\ldots,\delta_{Q-1})
=4\sum_{j\ge1}e^{-4\pi j^2}
\operatorname {Re}\left(
\frac1Q\sum_{r=0}^{Q-1}e^{2\pi i j\delta_r/d}
\right).}
\tag{6.1}
\]

The exact root-of-unity filter is available when \(Q\mid d\), by taking

\[
\delta_r=\delta_0+\frac{rd}{Q}.
\tag{6.2}
\]

Conversely, suppose \(Q\) equal-weight points on the \(d\)-th root lattice
annihilate the modes \(1,\ldots,Q-1\).  If
\(z_r=e^{2\pi i\delta_r/d}\), their first \(Q-1\) power sums vanish.
Newton's identities imply

\[
\prod_{r=0}^{Q-1}(z-z_r)=z^Q-c.
\]

The points are a rotated set of all \(Q\)-th roots.  Since their ratios
are also \(d\)-th roots, necessarily

\[
\boxed{Q\mid d.}
\tag{6.3}
\]

For arbitrary \(d\), rounding \(rd/Q\) to the nearest integer gives only

\[
\left|
\frac1Q\sum_re^{2\pi i j\delta_r/d}
-\frac1Q\sum_re^{2\pi i jr/Q}
\right|
\le\frac{\pi |j|}{d}.
\tag{6.4}
\]

Equation (6.1) then gives an \(O(1/d)\), not an \(o(1/d)\), error.
This is not a universal lower bound, but it proves that naive cut rounding
does not establish the desired scale.  Balanced dithering between adjacent
cut ranks can cancel the first-order error fractionally; an integral
common-chainization version is missing.

## 7. Physical position and state quantifier

There is no valid unconditional theorem that \(Q\) phases force \(Q\)
components, \(Q\) seams, or a \(Q\)-valued exported sidecar.

Indeed, color the chains of one global SCD by their chosen phase and split
each chain at that offset.  This remains one global SCD factor.  Moreover,
if a piece has top cut rank \(r\) and the reference top is \(t-1\), then

\[
\boxed{\delta\equiv t-1-r\pmod d.}
\tag{7.1}
\]

Thus the phase is recoverable from the absolute cut rank.  It need not be
stored in an auxiliary coordinate or exported automaton state.  A compiled
finite word can also hard-code the phase order.

What is true is the following conditional audit.

- If phases are realized as \(Q\) separately concatenated regions, there
  are \(Q\) boundary transitions; without a zero-length splice theorem
  this route pays an unbounded seam charge.
- If a local compiler is required to be phase-blind and its observable
  state omits the absolute cut rank, then \(Q\) distinct successor rules
  require \(Q\) internal states by the pigeonhole principle.
- Binary coordinate tags use \(\lceil\log_2Q\rceil\) bits and one-hot tags
  use \(Q\) coordinates.  These are sufficient sidecars, not proved
  necessities.  The multiseparator SCD theorem has static room for them
  when \(Q=o(d)\), but does not glue their overlapping histories.

Therefore zero added positions and \(O(1)\) exported state are not ruled
out.  The unresolved issue is constructive: can the differently cut chain
families be serialized in one PBBS owner chronology while their phase is
read intrinsically from rank?

## 8. One-bite consequence

One isolated rank-two owner-ring bite has proved coverage scale

\[
\Theta(W/d).
\tag{8.1}
\]

The ideal phase estimate

\[
\theta_QW=o(W/d)
\tag{8.2}
\]

therefore removes the density-scale reason one bite could not pay the old
fixed positive theta demand.

It does not yet prove owner--source frame recoupling.  The one-bite theorem
is for the regular owner-copy hypergraph.  Restricting to target-disjoint
moment/Kirkman frames gives the separate unequal-degree recoupling
hypergraph, for which no corresponding bite theorem is proved.  Higher
target depths and physical fusion also remain.

## 9. Verdict

The analytic answer is yes:

\[
\boxed{
\theta_Q=4\sum_{a\ge1}e^{-4\pi Q^2a^2}=o(1/d)
}
\]

when \(4\pi Q^2-\log d\to\infty\).

The physical answer is open, not obstructed by a proved sidecar lower
bound.  The existing two-endpoint constructions do not change the census
which creates \(\theta\).  A proof still needs:

1. a \(Q\)-phase partition of the whole deep-band chainization;
2. integral phase balancing with Fourier error \(o(1/d)\) for every \(d\);
3. a second-order finite-binomial census;
4. a zero-length common-history serialization using the intrinsic rank
   phase (7.1); and
5. a one-bite theorem on the target-clean owner--source recoupling
   hypergraph.

Until those are supplied, phase dilution is a valid Fourier mechanism but
not a PBBS construction.
