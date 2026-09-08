# Diverse-order compiler packets: synthesis audit, cross-packet Fourier kernel, and exact floor boundary

Date: 2026-07-26

Method: pure mathematics only. No computation, finite search, solver, or
web input is used.

## L1 scope correction

For the exact constant-one target

\[
 \sum_{q\le H}\sum_{\epsilon\in\{-,+\}}M_q^\epsilon=o(W),
\]

the floor-energy and negative-Gram conclusions below are sufficient but
not necessary. A load vector can cover every target while having linear
floor excess, and pairwise packet intersections do not determine the union.
In particular:

* Sections 6.1 and 7 concern the stronger adjacent-floor-balanced
  objective;
* the independent-choice hole theorem in Section 6 remains a genuine
  product-distribution \(L^1\) obstruction, but not an every-assignment
  theorem;
* the localized invariant-fibre obstruction in Section 8 remains a
  deterministic every-assignment hole theorem;
* the claim in Section 2 that every positive-density common-order mixture
  is excluded is valid only for the stronger floor ledger. For \(L^1\)
  coverage the direct support cut has a positive-part threshold.

The complete correction, the exact invariant-tag theorem, and the sharp
hereditary \(L^1\) dispersion condition are in
MATH_REAUDIT_K_FOURIER_FLOOR_VS_L1_HEREDITARY_DISPERSION_20260726.md.
The original formulas are retained below with this corrected implication
scope.

## 0. Verdict

The core local statement of
MATH_THEOREM_DIVERSE_ORDER_COMPILER_PACKET_FACTOR_20260726.md is valid.
Let

\[
 H\to\infty,\qquad H=o(m),
\]

choose \(n=4\cdot2^t\) least with \(n\ge\sqrt{mH}\), and put \(R=2n\).
Then

\[
 H=o(R),\qquad R=o(m),\qquad H\le n/2-1
\]

for all sufficiently large \(m\). The recursive parity-complete paired
lift is one exact factor of \(Q_R\) into isometric \(C_{2R}\)'s. Under the
coordinate-disjoint split-pair Johnson realization, its literal lower and
upper depth-\(q\) trace maps are injective on every owner of the packet,
for both orientations and every \(q\le H\). The rank-twisted tiling gives
owner-disjoint physical \(Q_R\)-packets covering

\[
                         G=W-o(W/H),
 \qquad W=\binom{2m}{m}.
\]

Consequently every retained packet emits exactly \(2^R\) distinct lower
targets and \(2^R\) distinct upper targets at each protected depth, and
the exact number of cycle components is

\[
                         \frac{G}{2R}=o(W/H).
\]

There are three necessary corrections or qualifications.

1. The diverse-order factor contains no residual syndrome-map choice.
   A syndrome-kernel factor is an alternative whole factor of \(Q_R\), not
   a cyclewise layer which may be superposed on the diverse factor. The
   proved legal menu supplied by this construction is the whole-factor
   cube automorphism orbit

   \[
                  \Gamma_R=\mathbb F_2^R\rtimes S_R
   \]

   (and, if desired, whole-factor reversal). Other nonconjugate exact
   diverse compilers are not excluded. Independently changing the
   syndrome/order on individual cycles requires a new common-owner overlay
   theorem.

2. No globally unique packet tag has been constructed. Frozen inactive
   orientations separate parallel \(Q_R\)-fibres of one product cell, but
   a coordinate frozen in one cell can be active in another. Thus
   cross-product-cell target collisions remain open.

3. The component count alone does not justify every seam treatment. A
   proved prefix-copy or boundary-dummy fusion costing \(O(H)\) length per
   component has total cost \(o(W)\), and retaining the components as
   cyclic strips creates no seam. By contrast, deleting all starts within
   distance \(q\) of a raw cut costs \(O(q)\) at depth \(q\), hence
   \(O(H^2)\) per component through all depths. The assumptions give
   \(HM=o(W)\), not \(H^2M=o(W)\).

The cross-packet problem can nevertheless be computed exactly. This note
proves the following.

* There is an ambient Walsh formula for the intersection of any two
  physical packet images, including different status cells, active
  matchings, and frozen data.
* Uniform legal whole-factor conjugation has an exact first marginal and
  an exact statewise fixed-mass binary scatter. Its two-target covariance is
  governed by a finite pair-orbit spectrum not determined by trace
  injectivity.
* Independent affine/order choices are sharply negative. At
  \(q=a\sqrt m+o(\sqrt m)\), \(a>0\), they have linear expected floor
  excess and linear expected holes; indeed they have linear holes with
  probability tending to one.
* There are fully legal localized rank-twisted packet atlases, still with
  zero within-packet repeats and \(o(W/H)\) cycles, for which no assignment
  of compiler conjugates can cover more than \(o(N_q)\) targets in the
  typical fibres. Both signs miss

  \[
                       (1-o(1))N_q
                       =(e^{-a^2}-o(1))W.
  \]

Thus the local synthesis plus affine averaging proves neither the integer
floor reserve nor the weaker summed-\(L^1\) coverage target. For the latter,
the necessary architecture test is hereditary target-support dispersion,
and the remaining construction is a correlated grouped set cover. An
order-\(W\) negative cross-packet Gram term is required only by the stronger
floor-balanced route. Whether a specially dispersed atlas admits an
\(o(W)\)-hole common choice remains open.

## 1. Audit of the synthesis

### 1.1 Scale

Successive admissible values \(4\cdot2^t\) differ by a factor two, so

\[
 \sqrt{mH}\le n<2\sqrt{mH},
 \qquad
 2\sqrt{mH}\le R<4\sqrt{mH}.
\]

Therefore

\[
 \frac RH\ge2\sqrt{\frac mH}\longrightarrow\infty,
 \qquad
 \frac Rm<4\sqrt{\frac Hm}\longrightarrow0.
\]

Also \(H/(n/2)\le2\sqrt{H/m}\to0\), so eventually
\(H\le n/2-1\). These are precisely the inequalities required by the
local compiler.

### 1.2 Exact local factor and literal trace recovery

The construction in
MATH_ATTACK_S_PARITY_COMPLETE_MAPPING_TRACE_ENTROPY_CUT_20260726.md
gives neighbour permutations \(F_{n,p}\) on \(Q_n\), indexed by
\(p\in Q_n\), with pointwise parity-complete column maps. Restricting to
even contexts and applying the paired-order lift gives one neighbour
permutation of all of

\[
                         Q_n\times Q_n\cong Q_R.
\]

Every component is an isometric \(C_{4n}=C_{2R}\). The literal half-step
theorem recovers every start, from both signs and both orientations,
through physical length \(n/2-1\).

An older paired-lift note correctly warns that the augmented code
\((J,x|_{J^c},p|_{J^c})\) need not be recoverable from an unlabelled raw
cube target. That warning is not fatal here. In the physical Johnson
embedding each cube direction is a known disjoint ground-coordinate swap
pair. Inside one packet, a lower target has neither endpoint of a moved
pair and one endpoint of every untouched active pair; an upper target has
both endpoints of a moved pair and one endpoint of every untouched active
pair. Equality of two literal packet targets therefore forces equality of
their moved-direction sets \(J\), after which the audited augmented-code
injectivity recovers the start. Pre-existing frozen empty/full pairs are
constant throughout the packet.

Thus, for every retained packet \(P\), sign
\(\epsilon\in\{-,+\}\), and \(q\le H\),

\[
 I_{P,q}^{\epsilon}:=\operatorname {Im}\tau_{P,q}^{\epsilon},
 \qquad |I_{P,q}^{\epsilon}|=2^R.                 \tag{1.1}
\]

This includes all cycles and intervals crossing a chosen display origin.

### 1.3 Owner tiling and components

The rank-twisted construction partitions each local rank layer into
orientation cubes, tensors them, and subdivides every \(Q_S\), \(S\ge R\),
into parallel \(Q_R\)'s. Its low-dimensional leave is

\[
                         2^{m+o(m)}=o(W/H).
\]

Every retained owner belongs to one packet, and every packet is factored
completely. Since each component contains \(2R\) owners, the component
count is exactly \(G/(2R)\).

Parallel fibres cut from the same \(Q_S\) share active axes but differ in
a frozen orientation on at least one inactive split pair. Every signed
\(q<R\) trace retains that endpoint. Their trace images are therefore
disjoint for every compiler state. Cross-packet collisions can only come
from different active-axis choices, product cells, or rank-twisted frames.

### 1.4 Exact repeat identity

Put

\[
 N_q=\binom{2m}{m-q}=\binom{2m}{m+q}.
\]

By (1.1),

\[
 \left|\bigcup_P I_{P,q}^{\epsilon}\right|
 =G-\sum_T\left(\#\{P:T\in I_{P,q}^{\epsilon}\}-1\right)_+.
\]

Hence

\[
 M_q^{\epsilon}
 =N_q-G+\mathcal R_{q,\mathrm{cross}}^{\epsilon}    \tag{1.2}
\]

is exact. There is no hidden within-packet term.

## 2. The legal map space

Fix \(P\cong Q_R\) and let \(F\) be the diverse compiler. A legal local
state is

\[
                         F^g=gFg^{-1},
                         \qquad g\in\Gamma_R.
\]

The translation part reverses selected endpoints of active split pairs;
the \(S_R\)-part identifies compiler directions with physical axes. This
whole-factor conjugation preserves ownership and trace injectivity.

A syndrome map cannot be chosen in addition. The old syndrome construction
factors \(Q_R\) by translating one common-order cycle. Using it as an
alternative complete packet factor is legal, but mixing its cycles with
the already complete diverse factor is not licensed. Moreover, a
common-order packet has internal pair collision at least

\[
                  2^{R-1}\left(\frac{2^q}{R}-1\right)_+.       \tag{2.1}
\]

If such packets carry owner fraction \(\alpha\), their internal collisions
are at least

\[
 \frac{\alpha G}{2}\left(\frac{2^q}{R}-1\right)_+.
\]

At \(q=a\sqrt m\), compatibility with an \(O(W)\) floor ledger forces

\[
                         \alpha=O(R/2^q)=o(1).       \tag{2.2}
\]

Thus syndrome states cannot provide positive-density cross-packet
covariance in this floor-balanced architecture. This is not an \(L^1\)
hole conclusion. If common-order packets carry owner mass
\(G_{\rm co}=\alpha W\), their direct support cap forces holes at
\(q=a\sqrt m+o(\sqrt m)\) only when
\(\alpha>1-e^{-a^2}+o(1)\).

## 3. Exact ambient Walsh kernel

Write the ambient target Boolean group as

\[
                         \mathcal A=\mathbb F_2^{2m}.
\]

For a packet \(P\), let \(C_P\subset[2m]\) be the fixed set present
outside its active pairs, let

\[
 e_{P,i}=\{\iota_P(i,0),\iota_P(i,1)\},
 \qquad i\in[R],
\]

be its disjoint active physical pairs, let
\(\alpha_P\in\mathbb F_2^R\) record endpoint reversal, and let
\(J_{P,q}^{\epsilon}(z)\subset[R]\) be the selected \(q\)-support at
start \(z\in Q_R\). The lower and upper targets are

\[
 \Theta^-_{P,q}(z)
 =C_P\ \dot\cup\
   \{\iota_P(i,z_i+\alpha_{P,i}):i\notin J_{P,q}^-(z)\},       \tag{3.1}
\]

\[
 \begin{aligned}
 \Theta^+_{P,q}(z)
 ={}&C_P\ \dot\cup\
   \{\iota_P(i,z_i+\alpha_{P,i}):i\notin J_{P,q}^+(z)\}\\
 &\dot\cup\bigcup_{i\in J_{P,q}^+(z)}e_{P,i}.
 \end{aligned}                                                \tag{3.2}
\]

Define the unnormalised Walsh amplitude

\[
 \mathcal F_{P,q}^{\epsilon}(\xi)
 =\sum_{z\in Q_R}
       (-1)^{\langle\xi,1_{\Theta_{P,q}^{\epsilon}(z)}\rangle},
 \qquad \xi\in\mathcal A.                                  \tag{3.3}
\]

### Theorem 3.1 (physical cross-packet Parseval identity)

For arbitrary packets, frames, frozen statuses, and legal compiler states,

\[
 \boxed{
 |I_{P,q}^{\epsilon}\cap I_{Q,q}^{\epsilon}|
 =2^{-2m}\sum_{\xi\in\mathcal A}
       \mathcal F_{P,q}^{\epsilon}(\xi)
       \mathcal F_{Q,q}^{\epsilon}(\xi).}           \tag{3.4}
\]

#### Proof

Let \(Z_P(T)\) be the occurrence multiplicity from packet \(P\). Its
ambient Walsh transform is

\[
 \widehat Z_P(\xi)
 =\sum_TZ_P(T)(-1)^{\langle\xi,1_T\rangle}
 =\mathcal F_{P,q}^{\epsilon}(\xi).
\]

Trace injectivity makes \(Z_P\) binary, so
\(\langle Z_P,Z_Q\rangle=|I_P\cap I_Q|\). Walsh Parseval proves
(3.4). Without injectivity, the same formula gives the occurrence Gram.
\(\square\)

Let \(A_P=\bigcup_i e_{P,i}\). Formula (3.4) includes the exact tag
filter. In particular,

\[
 C_P\mathbin\triangle C_Q\not\subseteq A_P\cup A_Q
 \quad\Longrightarrow\quad
 I_{P,q}^{\epsilon}\cap I_{Q,q}^{\epsilon}=\varnothing.        \tag{3.5}
\]

Indeed some coordinate is frozen to different values and neither packet
can change it.

## 4. Same-atlas Fourier reduction

Suppose \(P,Q\) share active pairs and exterior core. Put

\[
 f_{P,J}^{\epsilon}(z)
 =\mathbf1_{\{J_{P,q}^{\epsilon}(z)=J\}},
 \qquad |J|=q,
\]

\[
 \widehat f_{P,J}^{\epsilon}(\eta)
 =\sum_{z\in Q_R}f_{P,J}^{\epsilon}(z)(-1)^{\eta\cdot z}.
\]

### Proposition 4.1 (diverse support-fibre kernel)

\[
 \boxed{
 |I_{P,q}^{\epsilon}\cap I_{Q,q}^{\epsilon}|
 =2^{-(R-q)}
   \sum_{|J|=q}
   \sum_{\operatorname {supp}\eta\subseteq J^c}
   (-1)^{\eta\cdot(\alpha_P+\alpha_Q)}
   \widehat f_{P,J}^{\epsilon}(\eta)
   \widehat f_{Q,J}^{\epsilon}(\eta).}              \tag{4.1}
\]

#### Proof

Two traces in the common atlas agree exactly when their supports agree and
their starts agree outside that support after endpoint reversal. The latter
indicator is

\[
 2^{-(R-q)}
 \sum_{\operatorname {supp}\eta\subseteq J^c}
 (-1)^{\eta\cdot(z+w+\alpha_P+\alpha_Q)}.
\]

Sum over \(z,w,J\). \(\square\)

This is the diverse-order replacement for the syndrome kernel. All order
diversity resides in the support-fibre spectra
\(\widehat f_{P,J}^{\epsilon}\), which the injectivity theorem does not
estimate.

## 5. Affine marginal and exact two-target covariance

Let \(\mathcal C_{P,q}^{\epsilon}\) be the cylinder of all signed physical
\(q\)-faces compatible with packet \(P\). Put

\[
 F_{R,q}=\binom Rq2^{R-q},\qquad
 B=2^R,\qquad
 p_q=\frac{B}{F_{R,q}}=\frac{2^q}{\binom Rq}.       \tag{5.1}
\]

The group \(\Gamma_R\) is transitive on local signed face labels, so for
uniform \(g\in\Gamma_R\),

\[
 \boxed{
 \mathbb E_g Z_{P,q}^{g,\epsilon}
 =p_q\mathbf1_{\mathcal C_{P,q}^{\epsilon}}.}       \tag{5.2}
\]

One draw of \(g\) selects the whole factor, so depths have not been
reselected independently.

### Lemma 5.1 (statewise affine scatter)

For every \(g\),

\[
 \boxed{
 \left\|Z_{P,q}^{g,\epsilon}
       -p_q\mathbf1_{\mathcal C_{P,q}^{\epsilon}}\right\|_2^2
 =B(1-p_q).}                                        \tag{5.3}
\]

#### Proof

The selected vector is binary of mass \(B\), its cylinder has size
\(F_{R,q}\), and \(p_qF_{R,q}=B\). Thus

\[
 B-2p_qB+p_q^2F_{R,q}=B(1-p_q).
\]

\(\square\)

The lower and upper cylinders are equivariantly identified by replacing
the \(q\) empty active pairs with full active pairs. Their local affine
noise is paired, not independently sampled. Under this canonical local
identification the two base pair spectra agree exactly:

\[
                         n_{a,h}^-(I_q)=n_{a,h}^+(I_q).          \tag{5.3a}
\]

The same group action has a compact exact pair spectrum. Represent a local
face by its star support \(J\) and outside word. Two ordered faces lie in
one orbit according to

\[
 a=|J\cap J'|,\qquad
 h=d_H(\eta,\eta')
\]

on the \(R-2q+a\) coordinates outside both supports. For a fixed first
face, the number of second faces of type \((a,h)\) is

\[
 N_{a,h}
 =\binom qa\binom{R-q}{q-a}2^{q-a}
   \binom{R-2q+a}{h}.                               \tag{5.4}
\]

The admissible ranges are

\[
 \max(0,2q-R)\le a\le q,\qquad
 0\le h\le R-2q+a,                                  \tag{5.4a}
\]

with out-of-range binomial coefficients interpreted as zero.

Let \(n_{a,h}^{\epsilon}(I_q)\) be the number of ordered pairs in the
base compiler image having this type.

### Proposition 5.2 (exact two-target covariance)

For a fixed ordered pair \(T,T'\) of type \((a,h)\),

\[
 \boxed{
 \Pr_g(T,T'\in gI_q^{\epsilon})
 =\frac{n_{a,h}^{\epsilon}(I_q)}
        {F_{R,q}N_{a,h}},}                         \tag{5.5}
\]

\[
 \boxed{
 \operatorname {Cov}_g
  (\mathbf1_{T\in gI_q^{\epsilon}},
   \mathbf1_{T'\in gI_q^{\epsilon}})
 =\frac{n_{a,h}^{\epsilon}(I_q)}
        {F_{R,q}N_{a,h}}-p_q^2.}                  \tag{5.6}
\]

#### Proof

The ordered-pair orbit has size \(F_{R,q}N_{a,h}\), and \(\Gamma_R\)
is transitive on it. Double count a conjugate together with an ordered
base-image pair mapped to \((T,T')\). \(\square\)

For the diagonal \(a=q,h=0\), one has \(N_{q,0}=1\) and
\(n_{q,0}=B\), recovering probability \(p_q\). The numbers
\(n_{a,h}^{\epsilon}\) are not determined by trace injectivity, component
count, or first marginals.

## 6. Independent legal maps are sharply negative

Fix the physical packet atlas and put

\[
 d_T^{\epsilon}
 =|\{P:T\in\mathcal C_{P,q}^{\epsilon}\}|.          \tag{6.1}
\]

Choose \(g_P\in\Gamma_R\) independently and uniformly. For a fixed target,
the packet hit events are independent, and

\[
 \boxed{
 L_T^{\epsilon}\sim\operatorname {Bin}(d_T^{\epsilon},p_q).}  \tag{6.2}
\]

Consequently

\[
 \begin{aligned}
 \mathbb EL_T^{\epsilon}&=p_qd_T^{\epsilon},\\
 \operatorname {Var}L_T^{\epsilon}&=p_q(1-p_q)d_T^{\epsilon},\\
 \mathbb E\binom{L_T^{\epsilon}}2
     &=p_q^2\binom{d_T^{\epsilon}}2,\\
 \Pr(L_T^{\epsilon}=0)&=(1-p_q)^{d_T^{\epsilon}}.
 \end{aligned}                                                \tag{6.3}
\]

The total candidate degree is

\[
 \sum_Td_T^{\epsilon}
 =\frac{G}{B}F_{R,q}
 =\frac G{p_q}.                                      \tag{6.4}
\]

Since \(d\mapsto(1-p_q)^d\) is convex, Jensen gives

\[
 \boxed{
 \mathbb E M_q^{\epsilon}
 \ge N_q(1-p_q)^{G/(p_qN_q)}.}                     \tag{6.5}
\]

Now suppose

\[
 q=a\sqrt m+o(\sqrt m),\qquad a>0,\qquad q\le H.
\]

Because \(q/R=\Theta(H^{-1/2})\to0\),

\[
 p_q=\frac{2^q}{\binom Rq}=o(1),
\qquad
 \frac{N_q}{W}\to e^{-a^2},
\qquad
 \frac G{N_q}\to e^{a^2}.
\]

Therefore

\[
 \boxed{
 \mathbb E M_q^{\epsilon}
 \ge\bigl(e^{-a^2-e^{a^2}}+o(1)\bigr)W.}           \tag{6.6}
\]

Changing one packet state changes the number of holes by at most \(2B\).
There are \(G/B\) independent packet variables. McDiarmid's inequality
therefore gives, for every fixed \(c>0\),

\[
 \Pr\bigl(|M_q^{\epsilon}-\mathbb EM_q^{\epsilon}|>cW\bigr)
 \le2\exp\{-\Omega_c(W/B)\}=o(1),                  \tag{6.7}
\]

because \(B=2^R=2^{o(m)}=o(W)\). Applying this to both signs proves that
independent legal affine/order choices have linear holes in both signs
with probability tending to one.

### 6.1 Exact integer-floor normalization

Use the retained mass \(G\), and put

\[
 \lambda_q=\frac G{N_q}=c_q+\theta_q,\qquad
 c_q=\lfloor\lambda_q\rfloor,\qquad 0\le\theta_q<1.
\]

For an integral load vector \(L\) of mass \(G\), let
\(\Delta_q^{\epsilon}\) be its pair-collision excess above the
adjacent-integer minimum. Then

\[
 \boxed{
 2\Delta_q^{\epsilon}
 =\left\|L-\lambda_q\mathbf1\right\|_2^2
  -N_q\theta_q(1-\theta_q)
 =\sum_T(L_T-c_q)(L_T-c_q-1).}                    \tag{6.8}
\]

Taking expectations in (6.8) gives the exact identity

\[
 \boxed{
 2\mathbb E\Delta_q^{\epsilon}
 =\left\|p_qd^{\epsilon}-\lambda_q\mathbf1\right\|_2^2
  +G(1-p_q)-N_q\theta_q(1-\theta_q).}              \tag{6.9}
\]

At a fixed positive Gaussian depth,
\(N_q\le(1+o(1))G\), \(\theta_q(1-\theta_q)\le1/4\), and \(p_q=o(1)\).
Thus

\[
 \boxed{
 \mathbb E\Delta_q^{\epsilon}\ge(3/8-o(1))G.}       \tag{6.10}
\]

Even a perfectly flat fractional candidate mean leaves nearly one
Bernoulli unit of variance per owner. The floor reserve absorbs at most
\(N_q/4\). The leave \(W-G=o(W/H)\) can repair only that many holes at one
depth, so the hole conclusion survives completion. At integer walls the
exact \(G/N_q\) normalization in (6.8) should be retained.

## 7. Exact deterministic cross-Gram quota

For a deterministic state assignment, put

\[
 Z_T=\sum_P\mathbf1_{\{T\in I_{P,q}^{\epsilon}\}}.
\]

Since packet images are binary,

\[
 \sum_TZ_T(Z_T-1)
 =\sum_{P\ne Q}|I_{P,q}^{\epsilon}\cap I_{Q,q}^{\epsilon}|.   \tag{7.1}
\]

Substitution into (6.8) gives

\[
 \boxed{
 2\Delta_q^{\epsilon}
 =\sum_{P\ne Q}|I_{P,q}^{\epsilon}\cap I_{Q,q}^{\epsilon}|
  -\bigl(2c_qG-c_q(c_q+1)N_q\bigr).}              \tag{7.2}
\]

Exact floor balance is equivalent to equality of the ordered cross-packet
intersection count and the displayed quota.

For a centered version, put

\[
 \overline Z_{P,q}^{\epsilon}
 =p_q\mathbf1_{\mathcal C_{P,q}^{\epsilon}},\qquad
 Y_{P,q}^{\epsilon}=Z_{P,q}^{\epsilon}
                    -\overline Z_{P,q}^{\epsilon},
\]

\[
 b_q^{\epsilon}
 =\sum_P\overline Z_{P,q}^{\epsilon}
  -\lambda_q\mathbf1.
\]

Lemma 5.1 gives
\(\|Y_{P,q}^{\epsilon}\|_2^2=B(1-p_q)\) statewise. Therefore

\[
 \boxed{
 \begin{aligned}
 2\Delta_q^{\epsilon}={}&
 \|b_q^{\epsilon}\|_2^2+G(1-p_q)
 +2\sum_{P<Q}\langle Y_{P,q}^{\epsilon},Y_{Q,q}^{\epsilon}\rangle\\
 &+2\left\langle b_q^{\epsilon},
                  \sum_PY_{P,q}^{\epsilon}\right\rangle
 -N_q\theta_q(1-\theta_q).
 \end{aligned}}                                               \tag{7.3}
\]

If

\[
 \|b_q^\epsilon\|_2=o(\sqrt W)
\]

and the deterministic choice succeeds in the sense
\(\Delta_q^\epsilon=o(W)\), then
\(\|\sum_PY_{P,q}^\epsilon\|_2=O(\sqrt W)\). Consequently the mixed
term in (7.3) is \(o(W)\), and success requires

\[
 \sum_{P<Q}\langle Y_{P,q}^{\epsilon},Y_{Q,q}^{\epsilon}\rangle
 =-\frac12\bigl(G(1-p_q)-N_q\theta_q(1-\theta_q)\bigr)+o(W),   \tag{7.4}
\]

simultaneously for both signs and all protected depths. This is a negative
term of order \(W\). The local theorem gives no estimate or sign for it.
Proposition 5.2 shows that even its common-atlas average requires the
unproved pair spectrum \(n_{a,h}^{\epsilon}\).

Equivalently, with

\[
 K_{P,Q}^{q,\epsilon}
 =|I_{P,q}^{\epsilon}\cap I_{Q,q}^{\epsilon}|-\frac{B^2}{N_q},
\]

one has

\[
 \left\|Z-\lambda_q\mathbf1\right\|_2^2
 =\sum_{P,Q}K_{P,Q}^{q,\epsilon}.                  \tag{7.5}
\]

Subtracting \(N_q\theta_q(1-\theta_q)\) gives the floor excess; (3.4)
is the full physical Fourier expansion of every term.

## 8. A legal atlas on which every map fails

The independent-map theorem does not rule out a specially correlated
choice. The local synthesis nevertheless does not imply such a choice
exists: a legal packet atlas can fail before compiler maps are chosen.

Assume

\[
 a\sqrt m\le H=o(m),\qquad
 q=\lfloor a\sqrt m\rfloor,\qquad a>0.
\]

At \(R=\Theta(\sqrt{mH})\), choose a union \(E\) of the first complete
rank-twisted macroblocks with

\[
 16R\le e:=|E|<16R+2d,\qquad d=\Theta(\log m).       \tag{8.1}
\]

All but \(o(W)\) middle owners lie in product cells with at least \(R\)
split axes supported in \(E\). This must be proved unconditionally, not by
fixing an arbitrary local-rank vector (an extreme rank vector can have no
split axes).

For a macroblock \(B_j\), let

\[
 K_j=|X\cap B_j|,
 \qquad
 Y_j=\#\{\hbox{split edges of }M_{j,K_j}\hbox{ in }X\}.
\]

Under the product Bernoulli-\(1/2\) owner law, the variables \(Y_j\) on
different blocks are independent, \(0\le Y_j\le d\), and

\[
 \mathbb E(Y_j\mid K_j=k)
 =\frac{k(2d-k)}{2d-1},
 \qquad
 \mathbb EY_j=\frac d2.                            \tag{8.1a}
\]

Indeed, conditional on \(K_j=k\), the local set is a uniform \(k\)-set,
and the displayed expectation is the split-edge incidence count for any
fixed perfect matching. There are \(\ell=e/(2d)\) complete blocks in
\(E\), so the total split count \(S_E=\sum_{j\le\ell}Y_j\) has

\[
 \mathbb ES_E=\frac e4\ge4R.
\]

Hoeffding's inequality gives

\[
 \Pr(S_E<R)
 \le
 \exp\left\{-\frac{2(3R)^2}{\ell d^2}\right\}
 =
 \exp\left\{-\frac{36R^2}{ed}\right\}
 =
 \exp\{-\Omega(R/d)\}.                              \tag{8.1b}
\]

Conditioning on \(|X|=m\) costs only \(\Theta(\sqrt m)\). Since
\(R/d\gg\log m\), the conditioned exceptional middle-owner proportion is
still \(o(1)\), in fact \(o(1/H)\).

Choose all retained axes inside \(E\) on every normal cell. This is a
legal parallel-\(Q_R\) tiling. Every normal compiler trace changes only
coordinates of \(E\), so its exterior subset in \(E^c\) is a literal
invariant for both signs and every conjugate.

For a lower target \(T\), put \(t=|T\cap E|\). Under the uniform
rank-\((m-q)\) target law,

\[
 \mathbb Et=\frac{e(m-q)}{2m},\qquad
 \operatorname {Var}t\le e/4.
\]

Moreover,

\[
 \frac{q^2}{e}
 =\Theta\!\left(\sqrt{\frac mH}\right)\to\infty,
 \qquad \frac qe\to0.                               \tag{8.2}
\]

Thus all but \(o(N_q)\) lower targets obey

\[
                         |t-\mathbb Et|\le q/10.     \tag{8.3}
\]

Fix \(T\cap E^c\). The fibre has \(\binom et\) lower targets, whereas
every localized middle source in it has \(t+q\) coordinates in \(E\), so
there are at most \(\binom e{t+q}\) source occurrences. Uniformly on
(8.3), write \(t=e/2-r\). Since
\(e q/(2m)=o(q)\), one has \(|r|\le q/8\) for all sufficiently large
\(m\). The exact ratio is

\[
 \frac{\binom e{t+q}}{\binom et}
 =\prod_{j=1}^q
   \frac{e/2+r-j+1}{e/2-r+j}.                       \tag{8.3a}
\]

Here every logarithmic increment is \(O(q/e)=o(1)\), while the sum of
its linear numerators is

\[
 \sum_{j=1}^q(2r-2j+1)=2rq-q^2\le-\frac34q^2.
\]

The total quadratic Taylor error is \(O(q^3/e^2)=o(q^2/e)\).
Consequently, for an absolute \(c>0\),

\[
 \frac{\binom e{t+q}}{\binom et}
 \le\exp\left(-c\frac{q^2}{e}\right)=o(1)           \tag{8.4}
\]

for an absolute \(c>0\). One source hits at most one target, regardless
of compiler state. Summing over exterior fibres and restoring the
\(o(W)\) exceptional owners proves

\[
 \boxed{
 M_q^-\ge(1-o(1))N_q=(e^{-a^2}-o(1))W.}            \tag{8.5}
\]

For an upper target \(U\), put \(u=|U\cap E|\). Its source fibre has
\(\binom e{u-q}\) owners and its target fibre has \(\binom eu\) targets.
Writing \(u=e/2+r\), the same product calculation gives

\[
 \frac{\binom e{u-q}}{\binom eu}
 \le\exp\left(-c\frac{q^2}{e}\right)=o(1)
\]

and hence

\[
 \boxed{
 M_q^+\ge(1-o(1))N_q=(e^{-a^2}-o(1))W.}            \tag{8.6}
\]

This is a cross-packet physical-tag obstruction. The compiler still has
zero within-packet repeats, and the component count remains \(o(W/H)\).
Equations (8.5)-(8.6) hold for every dependent or deterministic assignment
of legal whole-factor maps.

### 8.1 Hereditary dispersion condition

The same argument gives a quantitative necessary condition. Let
\(E\subset[2m]\) satisfy

\[
 |E|=e=o(m),\qquad q=o(e),\qquad q^2/e\to\infty,
\]

and let \(G_E\) be the covered owner mass in packets all of whose active
axes are supported inside \(E\). On typical target fibres, localized
sources cover at most

\[
                         \rho_EN_q,\qquad
 \rho_E\le e^{-cq^2/e}=o(1)
\]

distinct targets. All other owners cover at most \(W-G_E\) more. Hence,
for either sign,

\[
 \boxed{
 M_q^{\epsilon}
 \ge N_q-(W-G_E)-\rho_EN_q-o(W).}                  \tag{8.7}
\]

At \(q=a\sqrt m\), the condition \(M_q^{\epsilon}=o(W)\) forces

\[
 \boxed{
 \frac{G_E}{W}\le1-e^{-a^2}+o(1)}.                 \tag{8.8}
\]

A dispersed-selector theorem is therefore a genuine missing hypothesis.

## 9. Statewise degree-one identity

Fix a ground coordinate \(x\). Let \(G_x\) be the covered owner mass
containing \(x\), and let \(A_x\) be the covered owner mass in packets
where \(x\) is an endpoint of an active split-pair axis.

On an isometric \(C_{2R}\), every active direction appears twice, and
exactly \(2q\) cyclic length-\(q\) starts touch it. Antipodal starts have
the same support and complementary active orientations, so exactly half
of the untouched starts select endpoint \(x\). Summing packet cycles gives

\[
 \boxed{
 \sum_{T\ni x}Z_q^-(T)=G_x-\frac{qA_x}{2R},\qquad
 \sum_{U\ni x}Z_q^+(U)=G_x+\frac{qA_x}{2R}.}       \tag{9.1}
\]

Equivalently,

\[
 S_x^++S_x^-=2G_x,\qquad
 S_x^+-S_x^-=\frac{qA_x}{R}.                       \tag{9.2}
\]

These are exact degree-one Fourier marginals for every legal assignment.
They are a useful necessary test for axis dispersion, especially near
integer quota walls, but not by themselves a universal obstruction.

## 10. Literal integrality is not the obstruction

### Proposition 10.1 (simultaneous floor-balanced nested flags)

Ignoring packet grouping and global cycle closure, there are integral
nested lower deletion flags and integral nested upper addition flags,
one of each rooted at every middle owner, whose loads at every \(q\le H\)
are floor/ceiling balanced.

#### Proof

Form the layered deletion DAG from rank \(m\) to rank \(m-H\), with arcs
deleting one element. Give each middle vertex supply one. At level \(q\),
give every rank-\((m-q)\) vertex throughput bounds

\[
 \left[
 \left\lfloor\frac W{N_q}\right\rfloor,
 \left\lfloor\frac W{N_q}\right\rfloor+1
 \right].                                                \tag{10.1}
\]

The uniform deletion law gives every level-\(q\) vertex load \(W/N_q\).
After vertex splitting, the constraint matrix is a directed node-arc
incidence matrix and is totally unimodular. The feasible fractional flow
therefore has an integral realization, decomposing into one nested deletion
path from every middle owner.

Apply the complementary construction upward to get integral nested
addition paths. Pair the two paths at their root \(X\). If their deleted
and added coordinates are \(d_1,d_2,\ldots\) and \(a_1,a_2,\ldots\), then

\[
 X_j=X\setminus\{d_1,\ldots,d_j\}
        \cup\{a_1,\ldots,a_j\}
\]

is a literal Johnson geodesic. Its depth-\(q\) intersection and union are
the two selected nested flags. \(\square\)

This proposition does not group the paths into one compiler factor on
each \(Q_R\), nor make their successors globally consistent cycles. It
shows that set inclusion and integer floors are not the remaining
obstruction; the obstruction is whole-packet grouping plus successor
closure.

## 11. Proved and conditional boundary

The following are proved.

1. The diverse-order synthesis is a valid near-spanning owner factor with
   zero within-packet signed trace repeats and exactly
   \(G/(2R)=o(W/H)\) cycles.
2. Raw all-depth seam quarantine costs \(O(H^2)\), not \(O(H)\), per cut
   component.
3. The legal map menu is the whole-factor affine/order orbit. Equations
   (2.1)-(2.2) exclude positive-density common-order use only for the
   stronger floor-balanced route. For \(L^1\) coverage, the direct support
   cut has the threshold stated in the scope correction.
4. Equations (3.4), (4.1), and (5.5)-(5.6) are exact physical, same-atlas,
   and orbitwise two-target covariance formulas.
5. Independent legal map averaging has the exact binomial law (6.2),
   linear holes (6.6), and linear floor excess (6.10); it fails with
   probability tending to one.
6. Deterministic floor balance is equivalent to the cross-packet quota
   (7.2), or the negative Gram requirement (7.3). Neither is necessary for
   summed-\(L^1\) coverage.
7. The localized legal atlas of Section 8 defeats every map assignment
   and forces linear holes in both signs. Any positive atlas must satisfy
   the hereditary dispersion condition (8.8).
8. Without packet grouping, simultaneous integral floor-balanced nested
   flags exist by Proposition 10.1.

What is not proved is that every dispersed rank-twisted atlas fails, or
that some dispersed atlas succeeds. For such an atlas the exact missing
theorem is:

> Choose one whole-factor compiler conjugate in every owner-disjoint
> \(Q_R\)-packet, with one common choice through both signs and all
> \(q\le A\sqrt m\), so that the total number of uncovered physical targets
> is \(o(W)\), while packet supports obey every hereditary Hall/fibre cut.

The local trace theorem supplies neither the pair spectrum
\(n_{a,h}^{\epsilon}\) nor this grouped cross-product-cell cover. Therefore
constant one does not follow from the present synthesis, but the surviving
gate is narrower than the former syndrome-kernel problem: it is a
dispersed, grouped, whole-factor \(L^1\) cover, not a local compiler,
owner-factor, or necessary floor-Gram problem.
