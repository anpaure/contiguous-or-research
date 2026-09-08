# Cross-audit of the marked carrier telescope and joint reset

Date: 2026-07-25

Audited report:
MATH_AUDIT_TWO_DIM_CARRIER_TRANSFER_AND_JOINT_RESET_20260725.md.

Method: pure mathematics only; no computation, search, or solver.

## 0. Verdict

The running-maximum transfer, marked physical telescope, common-atom
joint-reset telescope, and nonoverlap word-equation factorization are
correct.

Three scope/wording corrections are required.

1. Formula (0.6) begins **after** the initial first-passage reset.  If the
   incoming record before that reset is \(p\), the complete corridor has
   the additional deterministic marker \(y^{b-p}\).
2. Two phase resets accept every **realized** joint record state.  The set
   of realized pairs need not be the full Cartesian rectangle.
3. The converse in the nonoverlap theorem requires the collars
   \(A,C\) to be individually legal at their required baselines.  Cap
   validity alone is not stated strongly enough to imply this.

None of these corrections restores a Fourier or reset gain.

## 1. Marked physical telescope

In reverse corridor order, the first reset sends an incoming \(p\le b\)
to zero and contributes block displacement

\[
 b-p.
\]

Starting from the resulting state zero, the middle maximum-record
resolvent has entries

\[
 \widehat G_{0,0}=1,
\qquad
 \widehat G_{0,q}
 ={1\over1-\widehat\lambda_q}
 -{1\over1-\widehat\lambda_{q-1}},
\]

where

\[
 \widehat\lambda_q=zC_bC_{q-1},
\qquad
 \widehat\lambda_0=0.
\]

Ending the middle segment at state \(q\) contributes marker \(y^q\).
The final reset has depth \(A+1\), so it contributes

\[
 y^{A+1-q}.
\]

Therefore

\[
 \begin{aligned}
 e_0^{\!*}(I-\widehat{\mathsf R}(z;y))^{-1}
 (y^{A+1-q})_{q=0}^{A+1}
 &=y^{A+1}\sum_{q=0}^{A+1}\widehat G_{0,q}\\
 &=\boxed{{y^{A+1}\over1-zC_bC_A}.}
 \end{aligned}
\]

Formula (0.6) is exact for the post-initial-reset segment.  Including the
initial reset gives

\[
 \boxed{
 {y^{b-p+A+1}\over1-zC_bC_A}.}
\]

For fixed incoming \(p\), the total displacement is still deterministic.
Thus the correction strengthens, rather than weakens, the no-Fourier-decay
conclusion.

## 2. Joint reset states

Let \(\mathcal Q_{\rm real}\) be the set of joint record pairs produced
by words satisfying the transported equation.  Each phase reset accepts
its full coordinate range, so

\[
 \boxed{
 \text{joint reset intersection}=\mathcal Q_{\rm real}.}
\]

One only knows

\[
 \mathcal Q_{\rm real}
 \subseteq
 \{0,\ldots,B_1\}\times\{0,\ldots,B_2\}.
\]

Equality with the whole rectangle is not automatic: correlations or
interlacing can forbid pairs.  Replace display (4.3) by the realized-state
set above.

The mass identity

\[
 \sum_{q\in\mathcal Q_{\rm real}}
 \sum_{\omega\in\mathscr L_{t,u}(q)}w(\omega)
 =\sum_{\omega\in\mathscr L_{t,u}}w(\omega)
\]

remains tautologically exact.  Hence intersecting the complete reset
projectors removes no compatible word.

With a common atomization, the product-poset cumulative function has top
value equal to the total one-pair series.  Summing the full reset
rectangle, with zero mass assigned to unrealized states if necessary,
still gives

\[
 {1\over1-\rho}.
\]

Thus the common-atom telescope is unaffected.

## 3. Nonoverlap solution of the transported word equation

Let

\[
 d=u-t,\qquad
 A=\mathcal A_{t,u},\qquad C=\mathcal C_{t,u},
\]

so

\[
 \operatorname {net}(A)=\operatorname {net}(C)=-d.
\]

Assume

\[
 |R_u|\ge|A|,\qquad |R_t|\ge|C|.
\]

From

\[
 AR_t=R_uC,
\]

the first \(|A|\) bits force

\[
 R_u=AZ.
\]

Left cancellation then gives

\[
 \boxed{R_t=ZC.}
\]

The common word \(Z\) is unique.

Native legality of \(R_t\) implies

\[
 1-s\le H_Z\le0.
\]

Native legality of \(R_u\), where \(Z\) starts after the net-\(-d\)
collar \(A\), implies

\[
 1-(s-d)\le H_Z\le d.
\]

Therefore

\[
 -(s-d-1)\le H_Z\le0.
\]

Since \(R_t=ZC\), and the two sides have net \(1-s\) and \(-d\),

\[
 \operatorname {net}(Z)=-(s-d-1).
\]

Thus, with

\[
 S=s-d-1,
\]

\(Z\) is exactly a top-to-bottom corridor of height \(S\), with series

\[
 \boxed{G_S(x)={x^S\over F_{S+1}(x^2)}.}
\]

At the critical point,

\[
 {G_S(1/2)\over G_s(1/2)}
 ={s+2\over s-d+1}.
\]

For \(d\le(1-\varepsilon)s\), this ratio is bounded above and below by
positive constants.

The converse “every such \(Z\) is legal” is valid provided:

* \(A\) is legal from height \(s\) to height \(s-d\);
* \(C\) is legal from height \(d+1\) to height one.

Under these collar-legality hypotheses, the constraints on \(AZ\) and
\(ZC\) separate, so every height-\(S\) corridor \(Z\) works.  If “legal
collar” means only that its individual Dyck blocks obey their native caps,
the second baseline condition must be proved separately.

## 4. Exact scope

The nonoverlap sector is an exact sector of the transported free-monoid
equation with individually legal collars.  It retains a corridor of
height comparable to \(s\) whenever \(u-t\le(1-\varepsilon)s\), and hence
retains a central scalar Green factor of mass \(\Theta(s)\).

This does not prove that a Catalan-dense family of actual PBBS roots lies
in the nonoverlap sector.  Complete canonical chronology and packing
remain absent.  It proves that:

* complete reset intersections cannot help;
* a broad formal nonoverlap solution sector is still critical;
* any surviving two-phase gain must come from overlapping/interlaced
  transported solutions or additional actual-PBBS restrictions.

No coefficient-one conclusion follows.
