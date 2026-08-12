# Diverse-order packets: exact cross-packet configuration and multilinear rounding

Date: 2026-07-26

Method: pure mathematics only.

## 0. Outcome

The diverse-order compiler theorem changes the grouped integral problem.
Inside every retained physical packet \(P\), for each sign and every
\(q\le H\), the trace image is a set

\[
                         I_{P,c}^{\omega}\subseteq{\cal T}_c,
 \qquad c=(\sigma,q),\qquad
                         |I_{P,c}^{\omega}|=|P|=2^R,              \tag{0.1}
\]

not a multiset. Here \(\omega\) is the physical axis/context/compiler
option. Thus all repeated targets are intersections of image sets belonging
to **different packets**.

The common-order syndrome columns, shore-class multiplicities, and
within-packet collision rows are obsolete. The exact grouped column is

\[
                         v_{P,\omega}
  =\bigl(\mathbf1_{I_{P,c}^{\omega}}\bigr)_{c,T}
  \in\{0,1\}^{\bigsqcup_c{\cal T}_c}.                              \tag{0.2}
\]

One chooses one whole column \(v_{P,\omega_P}\) per packet. This preserves
the complete diverse-order chronology automatically.

There is an exact positive rounding theorem. Give every packet a
fractional distribution \(x_{P,\omega}\), sample the packet options
independently, and evaluate any nonnegative additive penalty of the
resulting literal loads. Its expectation is a multi-affine function of
the packet distributions. Hence some deterministic choice of one whole
option per packet has cost no larger than that expectation. Sequential
conditional expectations give the choice simultaneously for both signs
and every depth.

In particular, if the fractional packet distributions have expected
cross-packet collision energy within \(o(W)\) of the convex minimum, then
one integral whole-packet choice has \(o(W)\) total target holes. No TU,
integer-decomposition, normality, Graver, or parity theorem is required.

The new surviving gate is therefore entirely fractional:

\[
\boxed{\text{construct packet-option distributions with
near-minimal cross-packet covariance at every signed depth}.}     \tag{0.3}
\]

The positive Gaussian **first-marginal** profile flow does not yet prove
(0.3). If its coverage mass is diffusely spread over many packets, its
independent product rounding leaves a constant target fraction uncovered.
The fractional flow must be polarized into near-deterministic
target-to-packet images, or it must directly satisfy the covariance bound.

## 1. Packet image columns

Let \(\mathfrak P\) be the retained packet family supplied by
MATH_THEOREM_DIVERSE_ORDER_COMPILER_PACKET_FACTOR_20260726.md. Put

\[
                         s=2^R,\qquad
                         G=s|\mathfrak P|=W-o(W/H).                \tag{1.1}
\]

Every packet has \(s/(2R)\) cyclic components, so the total component
count is \(G/(2R)=o(W/H)\). This interface cost is already outside the
target-selection ledger.

For a packet option \(\omega\in\Omega_P\), let

\[
                         v_{P,\omega}^{c}(T)
  =\mathbf1_{\{T\in I_{P,c}^{\omega}\}}.                           \tag{1.2}
\]

The diverse-order injectivity theorem is exactly

\[
                         v_{P,\omega}^{c}(T)\in\{0,1\},\qquad
                         \sum_Tv_{P,\omega}^{c}(T)=s.             \tag{1.3}
\]

The choice variables are

\[
                         x_{P,\omega}\in\{0,1\},\qquad
                         \sum_{\omega\in\Omega_P}x_{P,\omega}=1.  \tag{1.4}
\]

The literal load is

\[
                         L_c(T)=\sum_{P,\omega}
                               x_{P,\omega}v_{P,\omega}^{c}(T).   \tag{1.5}
\]

Thus \(L_c(T)\) counts packets whose image contains \(T\). It never counts
two starts from one packet.

If physical axis selection couples several parallel packets, treat their
common axis-selection cell as one choice group. Its column is the sum of
the constituent \(0/1\) packet-image columns. Every assertion below holds
with “packet” replaced by this larger choice group. The atomic packet form
is exact after one owner packetization is fixed.

## 2. Exact cross-packet ledger

Fix \(c=(\sigma,q)\), and write \(N_c=N_q\). Define

\[
\begin{aligned}
 {\cal E}_c(L)&=\sum_T(L_c(T)-1)_+,\\
 {\cal H}_c(L)&=\#\{T:L_c(T)=0\}.
\end{aligned}                                                     \tag{2.1}
\]

Because the total occurrence mass is \(G\),

\[
                         \sum_TL_c(T)=G.                           \tag{2.2}
\]

Consequently

\[
 \boxed{
 {\cal H}_c(L)=N_q-G+{\cal E}_c(L).}                              \tag{2.3}
\]

There is no within-packet correction in (2.3). Moreover

\[
                         {\cal E}_c(L)
   =\sum_T\left(\#\{P:T\in I_{P,c}^{\omega_P}\}-1\right)_+        \tag{2.4}
\]

is exactly the cross-packet repeat count.

The coefficient-one target is

\[
                         \sum_{c}{\cal H}_c(L)=o(W).               \tag{2.5}
\]

All owner, component, and interface errors have already been charged by
the diverse-order packet theorem.

## 3. Zero integrality gap for the multilinear extension

Let

\[
                         x_{P,\omega}\ge0,\qquad
                         \sum_\omega x_{P,\omega}=1               \tag{3.1}
\]

be arbitrary packet distributions. Independently choose
\(\boldsymbol\omega=(\omega_P)_P\) from their product distribution.

Let \(J(\boldsymbol\omega)\ge0\) be any cost of the resulting common
all-depth loads. Examples include:

* total holes \(\sum_c{\cal H}_c\);
* total cross repeats \(\sum_c{\cal E}_c\);
* factorial collision energy;
* floor/ceiling overload; or
* any weighted sum of these quantities.

Define its multilinear extension

\[
                         \widetilde J(x)
                         =\mathbb E_xJ(\boldsymbol\omega).         \tag{3.2}
\]

### Theorem 3.1 (whole-packet conditional-expectation rounding)

For every fractional packet distribution \(x\), there is an integral
choice \(\widehat\omega_P\in\Omega_P\) for every packet such that

\[
                         J((\widehat\omega_P)_P)
                              \le\widetilde J(x).                  \tag{3.3}
\]

Hence

\[
 \min_{\omega_P\in\Omega_P}J((\omega_P)_P)
   =\min_{x\in\prod_P\Delta(\Omega_P)}\widetilde J(x).            \tag{3.4}
\]

#### Proof

Equation (3.2) is an average of the costs of integral choices, so one
choice has cost at most the average. More constructively, expose the
packets one at a time. Conditional expectation is the convex combination
of the conditional expectations obtained by fixing the next packet to
each possible option. Choose an option attaining at most that average.
Iteration never increases conditional expectation and ends at an integral
choice satisfying (3.3). \(\square\)

The same option is fixed for all depths and both signs. Therefore the
rounding preserves the entire diverse-order compiler chronology.

The theorem is elementary but decisive. The determinant-two minors belong
to the exact prescribed-load matrix. They create no integrality gap for
the correct multilinear cross-packet objective.

## 4. Explicit uncovered-target functional

Put

\[
                         p_{P,c}(T)
   =\sum_\omega x_{P,\omega}
                 \mathbf1_{\{T\in I_{P,c}^{\omega}\}}.            \tag{4.1}
\]

Under independent packet sampling, \(T\) is uncovered precisely when no
packet image contains it. Hence

\[
 \boxed{
 \widetilde{\cal H}(x)
   =\sum_{c,T}\prod_{P\in\mathfrak P}
                          (1-p_{P,c}(T)).}                         \tag{4.2}
\]

Formula (4.2) is the exact fractional grouped objective. By Theorem 3.1,

\[
                         \widetilde{\cal H}(x)=o(W)                \tag{4.3}
\]

is sufficient for an integral common all-depth packet selection with
\(o(W)\) target holes.

This is stronger than feasibility of the mean-load inequalities

\[
                         \sum_Pp_{P,c}(T)\ge1.                    \tag{4.4}
\]

Indeed, if

\[
                         \max_Pp_{P,c}(T)=o(1),\qquad
                         \sum_Pp_{P,c}(T)=\lambda+o(1)             \tag{4.5}
\]

with bounded \(\lambda\), then

\[
                         \prod_P(1-p_{P,c}(T))
                              =e^{-\lambda+o(1)}.                 \tag{4.6}
\]

Thus a diffuse Gaussian profile flow with constant load leaves a positive
fraction uncovered under product rounding.

More sharply, fix \(\varepsilon>0\) and \(\Lambda<\infty\). If

\[
                         p_{P,c}(T)\le1-\varepsilon
                         \quad\text{for every }P,\qquad
                         \sum_Pp_{P,c}(T)\le\Lambda,               \tag{4.7}
\]

then

\[
                         \prod_P(1-p_{P,c}(T))
 \ge\varepsilon^{\,\lceil\Lambda/(1-\varepsilon)\rceil+1}.        \tag{4.8}
\]

To minimize the product at fixed bounded sum, concentrate mass at the
upper bound \(1-\varepsilon\). This proves (4.8).

Consequently (4.3), at Gaussian depths where the total load remains
bounded, requires near-polarization: outside \(o(W)\) targets, some packet
must carry coverage probability tending to one. First-marginal profile
Hall does not provide this.

## 5. Cross-packet covariance formulation

Define the factorial collision energy

\[
                         {\cal C}_c(L)
   =\sum_T\binom{L_c(T)}2.                                       \tag{5.1}
\]

Using the packet injectivity (1.3),

\[
 \boxed{
 {\cal C}_c(L)
   =\sum_{\{P,Q\}\subseteq\mathfrak P}
      |I_{P,c}^{\omega_P}\cap I_{Q,c}^{\omega_Q}|.}               \tag{5.2}
\]

There is no diagonal or within-packet term.

For fractional packet distributions, the expected energy is the explicit
cross-packet covariance

\[
 \widetilde{\cal C}_c(x)
 =\sum_{P<Q}\sum_{\omega,\eta}
    x_{P,\omega}x_{Q,\eta}
    |I_{P,c}^{\omega}\cap I_{Q,c}^{\eta}|.                        \tag{5.3}
\]

Let \(G=aN_q+r_q\), \(0\le r_q<N_q\). Discrete convexity gives the exact
minimum among all integer load vectors of mass \(G\):

\[
                         {\cal C}_{c,\min}
     =N_q\binom a2+r_qa.                                         \tag{5.4}
\]

### Theorem 5.1 (fractional covariance implies integral coverage)

If packet distributions \(x\) satisfy

\[
 \sum_c\left(
   \widetilde{\cal C}_c(x)-{\cal C}_{c,\min}
 \right)=o(W),                                                   \tag{5.5}
\]

then there is one integral whole-packet/compiler choice per packet with

\[
                         \sum_c{\cal H}_c=o(W).                   \tag{5.6}
\]

#### Proof

Apply Theorem 3.1 to
\(J=\sum_c{\cal C}_c\). The integral choice has total collision energy at
most its fractional expectation, hence excess above (5.4) equal to
\(o(W)\).

If two target loads differ by at least two, moving one occurrence from the
larger to the smaller reduces \({\cal C}_c\) by at least one. Therefore
energy excess above (5.4) bounds the number of unit moves needed to reach a
floor/ceiling load vector.

When \(G\ge N_q\), every balanced load is positive, so every hole costs at
least one such move. When \(G<N_q\), one has

\[
                         N_q-G\le W-G=o(W/H),                     \tag{5.7}
\]

and \({\cal C}_{c,\min}=0\); every repeated occurrence creates at least one
collision pair. In both cases the number of holes is the forced
\((N_q-G)_+\) plus \(o(W)\). Summing over \(c\) proves (5.6).
\(\square\)

Thus the source theorem's “cross-packet covariance estimate” can be stated
exactly as (5.5). Once (5.5) is fractional, grouped integral rounding is
automatic.

## 6. What became obsolete

The following rows should be removed from the grouped rounding model:

1. common cyclic-order syndrome classes;
2. within-packet repeated-trace penalties;
3. shore-class or kernel-translate multiplicities used only to repair
   those repeats;
4. semigroup normality of fixed common-order columns; and
5. Graver moves which only exchange common-order phase classes.

They no longer describe the diverse-order compiler.

The still-relevant design variables are:

1. the physical \(R\)-axis packet embedding;
2. the diverse-order compiler conjugate/context; and
3. any product-cell choice which couples several packet embeddings.

Their only target data are the literal image sets \(I_{P,c}^{\omega}\)
and their cross intersections.

## 7. Relation to approximate integer decomposition

The rank-controlled basic-point theorem remains true for the linear mean
loads

\[
                         \sum_{P,\omega}
                              x_{P,\omega}v_{P,\omega}.            \tag{7.1}
\]

At packet scale its largest group mass is only

\[
                              |P|=2^R=2^{o(m)},                    \tag{7.2}
\]

so every subexponential profile quotient can be rounded with \(o(W)\)
linear discrepancy.

But this linear theorem is neither necessary nor sufficient for literal
coverage. It is unnecessary because Theorem 3.1 gives exact
objective-preserving integralization of the multilinear extension. It is
insufficient because a balanced diffuse mean can have the constant
uncovered probability (4.6).

Normality remains relevant only if one prescribes one exact literal load
vector. Coefficient one asks for \(o(W)\) total holes, for which the
multilinear and covariance formulations are the correct objects.

## 8. Exact surviving gate

The diverse-order packet theorem has closed:

* owner packing;
* component count;
* seams and interface toll;
* within-packet trace injectivity;
* common-order support entropy; and
* grouped integral rounding, once a fractional cross-packet cost bound is
  supplied.

The remaining positive theorem is either:

1. construct packet distributions with

   \[
                             \widetilde{\cal H}(x)=o(W),           \tag{8.1}
   \]

   which requires near-polarized packet coverage; or
2. prove the cross-packet covariance bound (5.5).

Both conditions already include every sign and depth through the same
packet distributions. By conditional expectations they yield one common
integral diverse-order compiler selection.

The positive Gaussian first-marginal flow is useful input, but it must be
strengthened from mean profile balance to one of (8.1) or (5.5). This is
the sole remaining grouped target-selection gate.
