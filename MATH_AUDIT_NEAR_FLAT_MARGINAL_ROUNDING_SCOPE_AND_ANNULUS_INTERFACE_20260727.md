# Audit of near-flat marginal rounding and its annulus interface

Date: 2026-07-27

Source audited:
MATH_THEOREM_NEAR_FLAT_MARGINAL_FIBRE_ROUNDING_20260727.md.

## 0. Verdict

The marginal-fibre theorem is a genuine load-space result:

\[
 {T\over W}\to1,\qquad
 \sum_i b_i=mT,\qquad
 \sum_i\left({b_i\over T}-{1\over2}\right)^2=o(1)
\]

imply the existence of an exact nonnegative integer middle load with

\[
 \sum_D L_D=T,\qquad \sum_{D\ni i}L_D=b_i,\qquad
 \Psi(L)=o(W).
\]

The exact legal common-core coordinate interval implies the displayed
aggregate hypothesis.  Coordinatewise \(b_i=W/2+o(W)\) without the
aggregate condition does not: a two-block marginal tilt has
\(\Psi=\Omega(W)\) throughout its fibre.

The theorem does **not** supply a correlated Gaussian-annulus leave.
It chooses abstract multiplicities on the middle \(m\)-sets and repairs
their singleton degrees by abstract Johnson-edge transfers.  It does not
choose cyclic packets, roots, paths, endpoint flags, or nested shadows.
Consequently it neither improves the rank-\(q_0\) nibble leave nor changes
the exact synchronized-hole identity

\[
 \mathfrak H(Q)=\Delta+k(N-|Q|).
\]

Its useful interface is conditional: if a physical routing theorem can
lift the theorem's \(o(W)\) abstract Johnson transfers while charging
only \(o(W)\) aggregate vertical damage, then the singleton-marginal
part of that routing problem is already solved.

## 1. Exact hypotheses and why the legal box supplies them

Let

\[
 \Omega=\binom{[2m]}m,\qquad W=|\Omega|,\qquad
 \varepsilon_i={b_i\over T}-{1\over2}.
\]

The theorem requires:

1. \(T/W\to1\) (in the common-core application \(T=W-K\), \(K=o(W)\));
2. \(b_i\in\mathbb Z\), \(0<b_i<T\);
3. \(\sum_i b_i=mT\), equivalently \(\sum_i\varepsilon_i=0\); and
4. \(\|\varepsilon\|_2^2=o(1)\).

The separately written \(\|\varepsilon\|_\infty=o(1)\) is redundant,
because it follows from item 4, but it records that the target lies in
the interior of the hypersimplex.

For the legal common-core interval, write

\[
 T=(M-\kappa)N,\qquad M=m+H,\qquad \kappa=4H-1,
\]

and \(\delta_i=b_i-T/2\).  The exact endpoint calculation is

\[
 -{\kappa HN\over2m}\le\delta_i\le{\kappa N\over2}.
\]

Since \(\sum_i\delta_i=0\), the total positive deviation is at most
\(\kappa HN\), and hence

\[
 \|\delta\|_2^2=O(\kappa^2HN^2).
\]

As \(T\asymp mN\), this gives

\[
 \|\varepsilon\|_2^2
 =O\left({H^3\over m^2}\right)
 =O\left({(\log m)^{3/2}\over\sqrt m}\right)=o(1)
\]

at calibrated height.  The asymmetric endpoint and the zero-sum identity
are both essential.

## 2. Proof audit

The proof has three logically separate parts.

### 2.1 Positive exact fractional load

The maximum-entropy family on the hypersimplex is

\[
 p_\theta(D)
 ={e^{\langle\theta,\mathbf1_D\rangle}
   \over\sum_{E\in\Omega}e^{\langle\theta,\mathbf1_E\rangle}}.
\]

On the coordinate-sum-zero space, the Hessian of its log partition
function at zero has eigenvalue

\[
 {m\over2(2m-1)}\asymp1.
\]

Sampling-without-replacement subgaussianity makes this Hessian uniformly
bounded above and below in a fixed Euclidean ball.  Therefore a marginal
perturbation of norm \(o(1)\) has a parameter \(\theta=o(1)\), and

\[
 \chi^2(p_\theta\|U)=O(\|\varepsilon\|_2^2)=o(1).
\]

Scaling \(p_\theta\) by \(T\) gives a positive real load \(y\) with the
exact total and singleton marginals and

\[
 \sum_D(y_D-T/W)^2=o(W),\qquad
 \sum_D|y_D-1|=o(W).
\]

The local Hessian bound is the only analytic input.  It is proved in the
source using Hoeffding comparison and bounded tilted third cumulants;
no fixed-dimension compactness is used.

### 2.2 Integer rounding

Round each \(y_D\) independently to its adjacent integers with the right
expectation.  The total rounding variance is at most
\(\sum_D|y_D-1|=o(W)\), while

\[
 \mathbb E\Psi(Z)
 \le\sum_D\big((y_D-1)_+ +(y_D-1)_+^2\big)=o(W).
\]

Because \(W\) is exponential in \(m\), all \(2m+1\) total/marginal
rounding errors have aggregate expected size \(o(W)\).

### 2.3 Exact correction

Correct the total on fresh load-one cells.  The remaining integer
singleton-degree error has coordinate sum zero.  Pair every positive
unit with a negative unit and use an oriented Johnson edge

\[
 X\longmapsto X-\{j\}+\{i\}.
\]

For each ordered pair \(j\to i\), there are

\[
 \binom{2m-2}{m-1}=(1/4+o(1))W
\]

candidate edges.  Only \(o(W)\) cells have nonunit load, so fresh
load-one source and target cells remain available through all \(o(W)\)
corrections.  Each correction costs exactly one collision.  This also
settles every integer parity/congruence issue.

Quantitatively, if

\[
 \eta=\sum_i\varepsilon_i^2,\qquad K=W-T,
\]

the proof gives, before harmless exponentially smaller rounding terms,

\[
 \Psi(L)
 =O\big(W\sqrt\eta+K+m\sqrt{W\sqrt\eta+K}\big).
\]

At the legal calibration this is

\[
 O\left({WH^{3/2}\over m}+K\right)=o(W)
\]

up to the exponentially smaller last term.

## 3. Why this is not a shared-leave theorem

The first-annulus packet problem has vertices at rank
\(r=m-q_0\), edges equal to full cyclic interval packets, and a selected
root family \(\mathcal F\).  Its deeper rank-\(r-s\) loads obey the
grouped extension identity

\[
 \operatorname{Ext}_s(R)=(s+1)\mu_{q_0+s}^{\mathcal F}(R).
\]

The marginal-rounding construction has none of this data:

* its cells are middle \(m\)-sets, not root packets;
* its exponential-family coordinates are chosen independently of cyclic
  residence and endpoint flags;
* its integer corrections replace one abstract \(m\)-set by a
  Johnson-adjacent one, not one legal packet by another; and
* it has no common owner index whose omission could define a leave shared
  by several ranks.

At the entrance rank the singleton test is in fact essentially vacuous.
Every cyclic rank-\(r\) packet contains each ground coordinate in exactly
\(r\) of its \(2m\) interval targets.  Hence any selected packet family
already has perfectly equal singleton marginals there.  Choosing an
abstract near-simple rank-\(r\) load with those marginals does not factor
that load into cyclic packets; the latter is precisely the hard matching
condition.

Even a rankwise analogue would only produce a separate abstract load at
each depth.  It would not make those loads the shadows of one selected
packet family.  Summing \(o(N_q)\) with no uniform rate over
\(\Theta(\sqrt m)\) ranks also does not give \(o(W)\).

Most decisively, in the synchronized common-core configuration model,
the ranks are already coupled by one root choice and

\[
 \mathfrak H(Q)=\Delta+k(N-|Q|),\qquad
 k=(\sqrt\pi+o(1))m^{3/2},\qquad N=(1+o(1)){W\over m}.
\]

A common root leave of order \(N/\sqrt m\) still costs
\(\Theta(W)\).  The marginal theorem neither lowers \(N-|Q|\) nor lowers
the per-root coefficient \(k\).

## 4. The only valid interfaces

There are two conditional uses.

1. **Terminal middle-load target.**  After a physical construction has
   fixed legal singleton marginals, the theorem proves that those
   marginals themselves do not force linear collision energy.

2. **Target for boundary-swap routing.**  The proof outputs an abstract
   correction by \(o(W)\) oriented Johnson edges.  Every such edge is
   realizable by a one-root common-core boundary swap.  To lift the
   correction, however, one must place the required old path at the
   required root and control the \(O(H)\) altered signed traces.  Paying
   \(O(H)\) independently for the theorem's
   \(O(WH^{3/2}/m)\) possible corrections is far larger than \(W\).
   A shared compiler or cancellation theorem is therefore still needed.

Accordingly, near-flat marginal rounding closes the **abstract
singleton-marginal fibre** and nothing stronger.  It gives no correlated
annulus leave and does not weaken the catalogue-specific slow-bite or
absorber theorem.
