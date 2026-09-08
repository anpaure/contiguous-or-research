# A bounded-support cross-cell gadget has an exact Gaussian Farkas obstruction

Date: 2026-07-26

Method: pure mathematics only.  No computation, search, solver, or web
input is used.

## 0. Result

This note tests the proposed route of constructing one finite transverse
status-cell gadget, tensoring it, and then using a correlated integral
selection or semigroup saturation.

Fix an integer \(b\ge2\).  Assume first that \(b\mid2m\), and partition
\([2m]\) into

\[
                         n={2m\over b}
\tag{0.1}
\]

labelled \(b\)-blocks.  In every tensor copy allow an arbitrary finite
library of status-cell resolutions, owner trades, compiler conjugates, and
correlated choices, subject only to the condition that every physical
Johnson axis has both endpoints in one \(b\)-block.  The library may be
transverse inside a block and its choices may be coupled across all blocks,
both signs, and all depths.

If \(b\nmid2m\), freeze the fewer than \(b\) residual coordinates and
apply the same argument in each residual-rank sector; this changes only
constant factors and none of the asymptotics below.

### Theorem 0.1 (finite-gadget tensor no-go)

Let \(q=A\sqrt m+O(1)\), where \(A>0\) is fixed.  Every factor assembled
from the preceding library misses \(\Omega_{A,b}(W)\) lower targets and
\(\Omega_{A,b}(W)\) upper targets, where

\[
                         W=\binom{2m}m.
\tag{0.2}
\]

The obstruction already holds in the fractional configuration polytope.
More precisely, there is an explicit nonnegative target weight \(w\),
supported on a \(\Theta_{A,b}(\sqrt m)\)-window of one full-block profile,
for which the exact Farkas inequality fails by \(\Omega_{A,b}(W)\):

\[
 \sum_i\max_{\ell}\langle w,a_{i\ell}^{-,q}\rangle
 \le \langle w,\mathbf1\rangle-\Omega_{A,b}(W).
\tag{0.3}
\]

The complemented weight gives the same failure on the upper side.  Hence
no integral semigroup theorem, absorber, Latin selection, or negative
covariance internal to a bounded gadget can repair this tensor construction.
For the floor-corrected energy at that depth one has, separately for both
signs,

\[
                         Q_q^\pm=\Omega_{A,b}(W).     \tag{0.4}
\]

The correct structural boundary is the following.  Form the graph on the
physical coordinates whose edges are all Johnson axes appearing in any
option of the proposed atlas.  A tensor of a fixed finite gadget has
uniformly bounded connected components.  To escape Theorem 0.1, those
components must grow with \(m\), or different tensor blocks must be joined
by genuine cross-block packet axes.  Merely adding more resolutions inside
each fixed gadget support cannot work.

## 1. Exact block-profile invariant

For a set \(Y\subseteq[2m]\), let

\[
 F_b(Y)=\#\{C:\ C\text{ is one of the }b\text{-blocks and }C\subseteq Y\}.
\tag{1.1}
\]

### Lemma 1.1

If \(T\) is the lower target of any return-free window whose physical axes
remain inside the fixed blocks, and \(X\) is any middle owner in that
window, then

\[
                         F_b(T)=F_b(X).
\tag{1.2}
\]

By complementation, the number of empty \(b\)-blocks is identical in an
upper target and its middle owner.

#### Proof

Every Johnson move exchanges two coordinates in one block and therefore
preserves the number of occupied coordinates in that block along the whole
owner window.  If a block is full in \(X\), no internal pair is split, so
no physical packet axis in that block is available; the block remains full
in the lower intersection.  If a block is not full in \(X\), every owner
in the window has local rank strictly below \(b\), and their intersection
cannot be full.  This proves (1.2).  Complementation exchanges full lower
blocks with empty upper blocks. \(\square\)

The proof uses neither a fixed matching nor a fixed status cell.  It is
uniform over every transverse resolution whose union of axes stays inside
the same bounded blocks.

## 2. Exact profile counts

Put

\[
 h_b(z)=(1+z)^b-z^b,
 \qquad D_b=2^b-1.
\tag{2.1}
\]

Let \(\mathcal X_k\) be the middle owners with \(F_b(X)=k\), and let
\(\mathcal T_{q,k}\) be the lower rank-\((m-q)\) targets with
\(F_b(T)=k\).  Ignoring the bounded frozen remainder, which changes every
estimate by only a constant factor,

\[
\begin{aligned}
 |\mathcal X_k|
   &=\binom nk[z^{m-bk}]h_b(z)^{n-k},\\
 |\mathcal T_{q,k}|
   &=\binom nk[z^{m-q-bk}]h_b(z)^{n-k}.
\end{aligned}
\tag{2.2}
\]

Indeed, choose the \(k\) full blocks and put an arbitrary proper subset in
every remaining block.

Normalize the coefficients of \(h_b\) by the span-one random variable

\[
 \Pr(J=j)={\binom bj\over D_b},\qquad0\le j<b.
\tag{2.3}
\]

Write

\[
 \mu_b=\mathbb EJ,qquad
 \sigma_b^2=\operatorname {Var}J>0,qquad
 a_b=b-\mu_b={b2^{b-1}\over D_b},
\tag{2.4}
\]

and

\[
 v_b={2(1-2^{-b})\over b}\sigma_b^2>0.
\tag{2.5}
\]

Take

\[
 k_*={m\over b2^{b-1}}-{A\over a_b}\sqrt m+O(1).
\tag{2.6}
\]

If \(d=n-k_*\), the coefficient index in the source is a deviation
\(A\sqrt m+O(1)\) above \(\mu_bd\), while the target coefficient index is
\(O(1)\) from \(\mu_bd\).  Also

\[
                         \sigma_b^2d=v_bm+O(\sqrt m).
\tag{2.7}
\]

The lattice local central limit theorem therefore gives

\[
 { |\mathcal X_{k_*}|\over|\mathcal T_{q,k_*}|}
      \longrightarrow
                         \exp\!\left(-{A^2\over2v_b}\right)<1.
\tag{2.8}
\]

For completeness, the deviations follow directly from

\[
 m-bk-\mu_b(n-k)
 ={m\over D_b}-a_bk.
\tag{2.9}
\]

At \(k=m/(b2^{b-1})+y\sqrt m\), the right side is
\(-a_by\sqrt m\); substituting \(y=-A/a_b\) gives the claimed source
deviation, and subtracting \(q\) gives the target deviation.

## 3. Positive target mass

Under Bernoulli parameter

\[
                         p={m-q\over2m}={1\over2}+O_A(m^{-1/2}),
\tag{3.1}
\]

the vector consisting of one block's rank and its full-block indicator has
a nonsingular covariance matrix.  Indeed, the full-block indicator is not
an affine function of the rank for \(b\ge2\).  Conditioning the sum of the
block ranks to be \(m-q\) consequently leaves full-block variance
\(\Theta_b(m)\).  The bivariate lattice local central limit theorem now
implies that, for a sufficiently small fixed \(c_{A,b}>0\), the integer
window

\[
 \mathcal K_m={k:|k-k_*|\le c_{A,b}\sqrt m\}
\tag{3.2}
\]

contains \(\Theta_{A,b}(N_q)\) lower targets, where

\[
                         N_q=\binom{2m}{m-q}.
\tag{3.3}
\]

Shrinking \(c_{A,b}\) if necessary, the source/target ratio throughout
this window is at most a constant \(\rho_{A,b}<1\), by the uniform form of
the local limit estimate in Section 2.  Hence

\[
 \sum_{k\in\mathcal K_m}
   (|\mathcal T_{q,k}|-|\mathcal X_k|)
 \ge \delta_{A,b}N_q
 =\Omega_{A,b}(W),                                 
\tag{3.4}
\]

because \(N_q/W\to e^{-A^2}\).  Here \(\delta_{A,b}>0\).

## 4. The explicit Farkas witness

Define the nonnegative lower-target weight

\[
 w(T)=\mathbf1_{\{F_b(T)\in\mathcal K_m\}}.
\tag{4.1}
\]

Index the owner-disjoint tensor regions by \(i\), and let \(\ell\) be any
legal local status resolution/compiler option on region \(i\).  By Lemma
1.1, every weighted target occurrence emitted by this option starts at an
owner whose full-block count lies in the same window.  Therefore, outcome
by outcome,

\[
 \sum_i\max_\ell\langle w,a_{i\ell}^{-,q}\rangle
 \le\sum_{k\in\mathcal K_m}|\mathcal X_k|.
\tag{4.2}
\]

The one-sided demand which asks merely to hit every target in the weighted
window is

\[
                         b(T)=w(T).
\tag{4.3}
\]

Thus (3.4) gives

\[
 \sum_i\max_\ell\langle w,a_{i\ell}^{-,q}\rangle
 <\langle w,b\rangle-\Omega_{A,b}(W),
\tag{4.4}
\]

which is the advertised exact violation of the weighted Hall/Farkas
criterion.  The actual floor quota at Gaussian depth is at least one, so
the coefficient-one demand is no weaker than (4.3).

An owner leave of size \(L=o(W)\), or an exceptional family of \(L\)
cross-block occurrences, can increase the left side by at most \(L\).
Thus the same linear separation survives all currently admissible
\(o(W/H)\) owner leaves and aggregate \(o(W)\) repair ledgers.

Indeed, with retained mass \(W_0=W-o(W)\), the Gaussian-depth floor
\(c_q=\lfloor W_0/N_q\rfloor\) is at least one.  Every missed target
contributes \(c_q(c_q+1)\ge2\) to

\[
 Q_q^-=\sum_T(Z_T-c_q)(Z_T-c_q-1).
\]

The linear hole bound therefore proves (0.4); complement gives the upper
identity.

Complement every target and owner.  Empty blocks replace full blocks, and
the same proof gives a nonnegative upper-target witness with the identical
gap.  Thus the obstruction is genuinely two-sided, although either signed
witness alone already excludes a simultaneous all-depth construction.

## 5. Consequence for semigroup saturation

Let \(\mathsf S\) be the integer semigroup generated by all complete
all-depth columns of the finite gadget library.  Equation (4.4) separates
the desired balanced vector not merely from \(\mathsf S\), but from the
whole convex Minkowski sum of the local configuration polytopes.  It follows
that:

1. normality or integer decomposition of \(\mathsf S\) is irrelevant;
2. no bounded absorber can repair the \(\Omega(W)\) gap;
3. correlating choices across tensor copies cannot help; and
4. adjoining finitely many further options whose axes remain in the same
   blocks leaves the witness unchanged.

The finite local gadget route is therefore closed with the quantifiers
requested: arbitrary integral grouping, both signs, and one common choice
for all \(q\le H\) are allowed, yet the witness at the single protected
depth \(q=A\sqrt m+O(1)\) gives a linear failure.

This is genuinely a cone/Farkas obstruction, not an arithmetic artefact.
The companion theorem
`MATH_THEOREM_CROSS_CELL_COMPILER_SEMIGROUP_NORMALITY_AND_UNIFORM_CONDUCTOR_20260726.md`
shows that every two-state gadget, every three-state binary gadget, and
indeed every affinely independent whole-column library has an exactly
normal homogenized semigroup.  Such normality cannot help here because the
desired vector is already outside the fractional cone by (4.4).

## 6. Exact next constructive statement

For an arbitrary packet atlas, let \(\Gamma\) be the graph on physical
coordinates whose edges are all coordinate pairs used by at least one
packet option.  Every move preserves rank inside each connected component
of \(\Gamma\).  The preceding proof applies whenever the atlas is a tensor
of linearly many uniformly bounded components.

Accordingly, a surviving cross-cell theorem must satisfy both of the
following before its joined target Gram or semigroup can matter:

* the union graph of its available physical axes has components whose size
  tends to infinity with \(m\); and
* actual selected packets cross the boundaries of every bounded terminal
  block decomposition on \(\Omega_A(W)\) Gaussian-depth occurrences.

Only after this growing-transversality condition is met is it meaningful to
seek negative floor covariance and semigroup saturation.  A finite gadget
may still serve as a local generator inside such a growing hierarchy, but
its independent tensor power cannot be the final construction.
