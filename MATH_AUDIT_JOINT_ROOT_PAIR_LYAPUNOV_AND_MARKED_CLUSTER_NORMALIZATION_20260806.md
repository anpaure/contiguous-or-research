# Audit of the joint root--pair Lyapunov and marked-cluster normalization

**Date:** 2026-08-06  
**Audited source:**
`MATH_THEOREM_JOINT_ROOT_PAIR_LYAPUNOV_AND_MARKED_CLUSTER_NORMALIZATION_20260806.md`  
**Method:** independent replay of the future-weight exponents, centered
root baseline, incidence-operator duality, and anchored marked FIFO fibres;
no computation or search  
**Verdict:** **PASS FOR THE EXACT IDENTITIES AND MARKED STATIC REPLAY;
FAIL FOR THE ORIGINAL SCALAR SPECTRAL CLAIM.**  The centered root potential
and its drift identities are exact.  The proposed row `(SG4-false)` is
refuted in the pristine complete orbit by a factor `Theta(d)`, first by a
coordinate-star mode and, after a near-antipodal redesign, by an even
degree-two mode.  The corrected local target is the Johnson-sector stopped
comparison `(JSEC)`.  Its unmarked pristine Eberlein tail and resolvent trace pass;
the adaptive perturbation `(JRES)`/`(JSW)` is not proved.  The finite marked size-two/three
product normalizations and first-two-hit rows pass the anchored FIFO
replay.  The integral packing theorem remains open.

## 1. Centered root potential

For two `h`-edges through a lower root `v`, their two rate rescalings have
non-slot exponent `2(N_h-1)`.  If `m` is their common count outside `v` and
`u` their union count outside `v`, then

\[
                         2(N_h-1)=u+m.
 \tag{1.1}
\]

The future weight changes by `rho^m`; hence the net deterministic factor is
`rho^-u`.  Avoidance of the full union under ideal product survival has
factor `rho^(u+1)`.  Their product is `rho`, exactly the survival factor of
the one distinguished root.  Slots give the identical cancellation because
`4=u_S+m_S`.  This verifies (2.5).

Every surviving `h`-edge contributes to exactly `2d` lower loads, so
`L_h=2dX_h`.  Its rate rescales by
`s_h=rho^(-(N_h-1))rho_s^-2`; ideal survival of all `N_h` non-slots and two
slots leaves `rho`.  This verifies (2.7).  Since the live lower count also
changes by `n'=rho n`, the three terms

\[
                         \mathcal Q_h-2\lambda_hL_h+lambda_h^2n
 \tag{1.2}
\]

have the same ideal multiplier.  There is no uncontrolled subtraction of
two unrelated order-`M` quantities.

The future weights are at least one, so `Q_h>=sum_v(Y_v^h)^2`; completing
the square proves positivity and domination of the actual root variance.
At time zero, the excess over `M lambda_h^2` is the `h`-restricted product
variance at `p_*`, hence `O(M/(cd))` by `(ROc)`.  Scaling by `d^-3` matches
the pair budget `M/d^4`.

## 2. Direct root contraction

If the selected edge hits `v`, the centered square disappears.  Its
conditional expected contribution is exactly

\[
                         -X^{-1}Y_v(Y_v^h-\lambda_h)^2.
 \tag{2.1}
\]

On a miss, the increment is
`(s_h-1)Y_v^h-s_hD_v^h(G)`.  Expanding its centered square gives precisely
the linear drift `2Z beta` and square injection `nu` in (3.5).  Thus the
source has neither omitted a hit-square term nor counted it twice.  Before
the bad stop, (2.1) supplies fixed root-energy contraction.

## 3. The centered incidence operator and the failed scalar row

For one pair-potential cross-term, incidences of the distinguished pair
roots must be removed before asking for centered control; their hazards are
the two-root service term.  The same applies to the single distinguished
root of a root-potential term.  On the remaining incidences, the weighted
adjoint identity is still exact:

\[
                         (K^*1)_x=g_x^\circ/Y_x.
 \tag{3.1}
\]

Projection away from constants subtracts
`beta=(sum_xg_x^circ)/(sum_xY_x)`, so the adjoint norm is precisely the
normalized gradient defect `mathfrak G`.  Therefore the source's
counterfactual calculation is correct: if

\[
                         \|K\|^2\le(1+\epsilon_c)\beta,
 \tag{3.2-false}
\]

then duality would give `(XG4)` and the same row would absorb the
first-order part of `(HDIR)`.  The error is not in that implication; it is
that (3.2-false) fails.

Take a central Johnson layer and the degree-one harmonic

\[
                         f_a(S)={\bf1}_{\{a\in S\}}-q/k.
 \tag{3.3}
\]

Along a length-`d` fresh FIFO path, coordinate `a` is exposed among the
deletion/insertion labels with probability `O(d/k)=O(1/d)`.  On the
complementary event every summand equals its initial value.  Hence

\[
 \mathbb E\left(\sum_{j<d}f_a(S_j)\right)^2
                   \ge c d^2\mathbb E f_a(S_0)^2.
 \tag{3.4}
\]

In the parent template the two header incidence vectors are
macroscopically separated but bounded a fixed distance away from exact
complementation, so their `E_1` sum has fixed positive norm; the constantly
many track contributions cannot cancel (3.4).  The transitive incidence
degree normalizes the right side of (3.2-false) by only one factor `d`.
Thus

\[
                         \|Kf_a\|_\mu^2
                   \ge c d\,\beta\|f_a\|_2^2.
 \tag{3.5}
\]

This is a pristine-orbit counterexample by `Theta(d)`.  Centering removes
`E_0`, not the star sector `E_1`.

A near-antipodal choice of the two headers does cancel (3.3): paired
coordinates contribute opposite signs, and a gap `g=Theta(d)` gives
normalized degree-one covariance `O(1+g/d)=O(1)`.  Complementation acts by
`(-1)^s` on primitive sector `E_s`, however.  A pure degree-two harmonic
is even, so the two path sums add on a `1-O(g/k)` fraction of coordinates.
Its normalized covariance is again `Omega(d)`.  Near-antipodality therefore
repairs only the first odd obstruction and cannot validate a scalar row.

## 4. Johnson sectors and the corrected gap

For the normalized one-exchange operator on `q`-subsets, direct replay of
the Bernoulli--Laplace spectrum gives

\[
 \lambda_s=1-{s(k-s+1)\over q(k-q)},
 \qquad
 \vartheta_s=1-\lambda_s={s(k-s+1)\over q(k-q)}.
 \tag{4.1}
\]

A fresh FIFO word has distance `|i-j|` between its `i`-th and `j`-th
states.  Since complete-orbit averaging of the normalized distance-`ell`
operator is scalar on `E_s`, with scalar the normalized Eberlein polynomial
`phi_s(ell)`, its exact multiplier is

\[
 \widehat\chi_{s,r}
   =1+2\sum_{j=1}^{r-1}(1-j/r)\phi_s(j).
 \tag{4.2}
\]

The with-replacement benchmark replaces `phi_s(j)` by `lambda_s^j` and is
`asymp min{d,k/s}`.  More importantly, the source does not use that
benchmark as a proof for the fresh word.  A standard pure `E_s` harmonic
has `O(s)` witness coordinates.  For `s<=c k/d`, none is touched during the
word with fixed positive probability, so the path sum stays `d` times its
initial value.  Association-scheme scalarity and Cauchy--Schwarz give

\[
                         \widehat\chi_{s,r}=Theta(d),
                  \qquad 1\le s\le c k/d.
 \tag{4.3}
\]

Thus `Theta(k/d)=Theta(d)` sectors are rigorously slow.  Complementarity
only changes their parity sign.  If greedy root removal contracts sector
`s` at gap scale `vartheta_s`, the counterterm must have weight at least
`beta widehat chi_s/vartheta_s`; omitting any slow sector cannot work
uniformly.  A sharp high-sector upper comparison remains part of `(JSEC)`.

The source's `(JSEC)` states the remaining assertion without hiding this
loss: the low-sector weighted energy must pay the forward and adjoint
Dirichlet faces, while the high-sector tail, sector mixing caused by the
stopped residual, slot errors, and owner-ledger errors must have cumulative
injection `O(M/d^4)`.  Summing `(JSEC)` would close `(GDIR)` and the
first-order part of `(HDIR)` because its terminal counterterm is
nonnegative.  The audit does not prove the needed stopped sector drift or
the high-sector injection bound.

The actual-vector resolvent is a valid sharpening.  With
`B_0=sum_s widehat chi_s Pi_s`, `L_0=sum_s vartheta_s Pi_s`, and
`R_0=L_0^dagger B_0`, one has the exact identity
`<f,R_0L_0f>=<f,B_0f>` on constants-perp.  Thus only the vector generated by
the process is tracked; no norm supremum or union over `dim(E_s)` occurs.
The deterministic tail estimate `(JT)` also passes.  For the standard
paired-coordinate `E_s` witness, correlation at Johnson distance `ell` is
zero unless the deletion and insertion restrictions choose the same
witness subfamily.  If that subfamily has size at least half its mean, the
cost of including its specified labels is `e^{-Omega(s ell/k)}`; otherwise
the cost of avoiding the remaining labels is the same.  Thus
`|phi_s(ell)|<=e^{-c s ell/k}` for `ell=O(d)`, and summing along a fresh
path gives `widehat chi_s<=C min(d,k/s)`.  Same-header track pairs obey the
same estimate, while the macroscopically separated cross-half pairs cost
`e^{-cs}`.  The union form follows from `(u+v)^2<=2u^2+2v^2` and the
transitive pristine side marginals.  This proves `(JT)` for the template
actually used in the unmarked aggregate families.  A fixed marked cluster
has a smaller stabilizer; its anchored spectral replay remains inside
`(JRES)` and is not supplied by the static normalization alone.

The multiplicity trace is consequently `O(1)`: sectors below
`epsilon k/2` have exponentially small total dimension even after the
maximum polynomial resolvent weight, while all later weights are
`O_epsilon(1)`.  Schur orthogonality turns the projection energy of each
unmarked pristine FIFO noise word into this multiplicity fraction times
its sector multiplier, which `(JT)` bounds polynomially.  This verifies
the pristine trace calculation in (5.34),
but not the stopped perturbation row `(JRES)`.

The proposed leave-one-root martingale shortcut fails conditionally.  Once
the deletion set is fixed, the current-minus-pristine operators are already
predictable.  After a single allowed macro deletion, surviving states in
the first Johnson shell and states outside it lose different exchange
degrees, so the operator difference is nonzero.  A coordinate switch pairs
two different prefixes; it does not give conditional cancellation inside
one prefix.  Only changes of the perturbation have a Doob decomposition.
Their bracket is resolvent-weighted and contains cross-track four-edge
terms, so it is not literally the existing pair future potential.  The
remaining switching statement is `(JSW)`: its predictable compensator and
weighted bracket must have total `O(M/d^4)`.

Expanding the adjoint square still shows why this is fourth order:

\[
 \sum_x{g_x^2\over Y_x}
 =\sum_{A,A'}\mu_A\mu_{A'}
       \sum_{x\in U_A^\circ\cap U_{A'}^\circ}{1\over Y_x}.
 \tag{4.4}
\]

Each `A` contains two macro edges, whereas `(ROc)` and `(FE3)` control
degree two and degree three.  The Johnson decomposition makes `(GDIR)` and
first-order `(HDIR)` sectorwise adjoint/forward faces of one gap; it does
not deduce their stopped perturbation from those lower moments.

## 5. Marked cluster normalization

For a compatible marked cluster `A` of size `m`, conditioning its owner
roots live leaves mean `p^(1-m)D_A`; multiplying by `p^(m-1)` gives `D_A`.
For a pair of incident edges, the two additional factors
`p^(2m-2)` cancel every conditioned-root survival factor.  Each common
resource outside `A` leaves exactly one inverse survival factor.  This
replays (6.5).

It remains to check that conditioning on two or three marked level-two
states does not destroy the FIFO overlap entropy.  In the atomic normal
form

\[
                         T_2^c=H\cup(R_c-\{x_2^c\}).
 \tag{5.1}
\]

One anchored state leaves a `Theta(d^2)` membership pool for its private
split.  Two states in the same half determine at most `H union {a}`; each
track retains its missing head and `(d-2)!` remaining queue orders, and the
lower continuation banks remain.  Three marked states still fix only a
constant number of tracks.  Hence:

* synchronized common levels obey Lemma 5.8 on the remaining intervals;
* entry into an unanchored track retains a `Theta(d^2)` private pool and
  Lemma 5.9;
* forced lower/owner, owner/owner, and singleton entries are exactly
  `(MT3)`, `(MT4)`--`(MT5)`, and the fan row;
* if a macro half remains unrooted, macroscopic header entropy applies;
  if both halves are rooted, the surviving queue orders and continuation
  banks supply the normalized anchored moments instead.

There are constantly many role patterns.  Normalizing by `D_A^2` cancels
the fixed companion-entry atoms, and the remaining moments are bounded.
This validates `Gamma_A=O(1)` through `m=3`.

For the marked first-two-hit row, choose the first two resources where the
deleting edge meets `E union F`.  There are `O(d^2)` role pairs and each
has base codegree `O(d^-3)`, giving `O(1/d)`.  Conditional further overlap
is the just-audited anchored cluster moment.  This verifies (7.3).

## 6. Remaining scope

The local stopped transfer is conditional precisely on `(JSEC)` (or its
actual-vector resolvent/switching form `(JRES)`--`(JSW)`) for the
pair-, root-, and marked-cluster future-potential families.  The scalar
alternative `(SG4-false)` cannot be used.  Even after `(JSEC)` is proved,
two nonlocal requirements remain:

1. prefix-uniform deterministic cleanup, or proof that expected cleanup is
   sufficient downstream; and
2. connectivity of the selected macro component graph, or a
   separator-scale connector bank.

Accordingly neither this note nor its parent note proves the final
`O(M/d)` balanced-doublet integral packing.
