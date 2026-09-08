# Z20: coordinate-symmetrized cut barycenters and the outer-frame obstruction

Date: 2026-07-25

Method: pure mathematics only. No computation, search, solver, or web input
is used.

## 0. Outcome

Put

\[
 V=[2m],\qquad M=m+H,\qquad
 P=\binom{2m}{M}=N_H,
 \tag{0.1}
\]

where \(H\) is the calibrated first crossing, so that

\[
 PM=W-o(W),\qquad W=\binom{2m}{m},
 \qquad H\sim\sqrt{m\log m}.
 \tag{0.2}
\]

Let \(Q=o(H)\), with \(Q^2/M\to\infty\), and consider the Z19
radius-\(Q\) cut-space gadgets.

The full coordinate-symmetrized catalogue does have the required
**fractional** aggregate barycenter. More precisely, at every controlled
rank \(r\), if every catalogue option has \(s_r\) occurrences, then its
global barycenter is exactly

\[
 \boxed{\bar h_r^{\rm cat}
 =\frac{Ps_r}{\binom{2m}{r}}\mathbf 1.}
 \tag{0.3}
\]

For Z19, \(s_r=M+O(Q)\). Relative to the original \(M\)-state scalar
centre, the total squared displacement through \(|r-m|\le Q\) is

\[
 O\!\left(\frac{WQ^3\lambda_Q}{M^2}\right)=o(W).
 \tag{0.4}
\]

Thus catalogue averaging itself clears the **fractional scalar-centre**
bias scale. It does not by itself approach a prescribed integral
floor/ceiling vector at nonmiddle ranks, and it does **not** select one
literal fibre per carrier.

There are four exact obstructions to making that inference.

1. A nontrivial fixed integral owner fibre cannot be invariant under the
   full coordinate group. Coordinate symmetrization necessarily moves
   between Z19 cut fibres, whereas the low-variance cut signs move only
   inside one fibre.
2. Z19 cut signs preserve the complete middle-owner vector identically.
   Up to the \(O(PQ)=o(W)\) duplicated phases, an \(o(W)\)-hole Z19 owner
   selection exists if and only if the underlying one-cycle-per-carrier
   owner near-factor already exists.
3. Independent or bounded-dependency rounding of the outer frames has
   \(\Omega(W)\) expected floor energy. A marginally symmetric law with
   expected \(o(W)\) energy must have
   carrier dependency degree at least

   \[
    \Omega\!\left(\frac{\binom{M}{H-Q}}{H}\right)
    \tag{0.5}
   \]

   before \(o(W)\) expected energy is even possible. Equivalently it must
   create negative covariance of magnitude at least \(\Omega(W)\) at each
   hard row and \(\Omega(QW)\) across the window.
4. The newer middle-owner theorem

   \[
   O(E)=O(0)+\sum_{a=1}^K E_a d_a,qquad
   K=(1/16-o(1))M,qquad \|d_a\|_1\le8
   \tag{0.6}
   \]

   controls only an inner fixed-frame cube. Even after averaging all its
   signs, the outer coordinate orbit has variance at least

   \[
    \boxed{(2/3-o(1))M}
    \tag{0.7}
   \]

   per carrier. Moreover at least \((1/2-o(1))M\) occupied owners per
   owner-simple carrier are frozen throughout the inner cube.

There is also a literal shared-frame obstruction: globally relabeling one
ambient cyclic construction gives an exactly coordinate-symmetric law with
the correct fractional barycenter, while every realization covers only
\(o(W)\) middle owners. Z19 signs cannot alter this failure.

Accordingly, the proposed averaging argument succeeds fractionally and
fails exactly at the integral outer-frame step. The remaining possible
route is a genuinely global, carrier-dependent frame/bundle matching,
followed by correlated signs. No arbitrary complete-dependence selector is
ruled out here, and none is constructed.

## 1. Exact full-catalogue barycenter

Fix a controlled rank (r\le M), and write

\[
 B_r=\binom Mr,\qquad N_r=\binom{2m}{r}.
 \tag{1.1}
\]

For a carrier (U\in\binom VM), let \(\mathscr C_r(U)\) be a finite
catalogue of nonnegative integral load vectors on \(\binom Ur\). Assume:

1. every (x\in\mathscr C_r(U)) has the same mass
   \(\sum_Tx(T)=s_r\);
2. the uniform catalogue measure is invariant under
   \(\operatorname{Sym}(U)\).

The second assumption holds after taking all coordinate relabelings of any
fixed literal carrier gadget. Occurrences are counted with multiplicity.

### Theorem 1.1 (exact local and global barycenters)

For every carrier (U),

\[
 \boxed{
 \bar x_{U,r}
 =\frac{s_r}{B_r}\mathbf1_{\binom Ur}.}
 \tag{1.2}
\]

After summing over all (P) carriers,

\[
 \boxed{
 \bar h_r^{\rm cat}
 =\sum_U\bar x_{U,r}
 =\frac{Ps_r}{N_r}\mathbf1_{\binom Vr}.}
 \tag{1.3}
\]

#### Proof

The group \(\operatorname{Sym}(U)\) is transitive on \(\binom Ur\), so
the local mean is constant. Its total mass is (s_r), proving (1.2).

A fixed global target (T\in\binom Vr) is contained in
\(\binom{2m-r}{M-r}\) carriers. Therefore its aggregate mean is

\[
 \binom{2m-r}{M-r}\frac{s_r}{B_r}.
\]

Double-counting pairs ((U,T)) gives

\[
 P B_r=N_r\binom{2m-r}{M-r},
 \tag{1.4}
\]

which turns the preceding display into (Ps_r/N_r). \(\square\)

If (Ps_r=k_rN_r+b_r), (0\le b_r<N_r), the vector (1.3) is the
barycenter of the balanced integral vectors having (b_r) coordinates
(k_r+1) and the rest (k_r). It is generally not itself integral.

### Corollary 1.2 (the (O(Q))-state adjustment is (o(W)))

Let

\[
 b_r^{(M)}=\frac{PM}{N_r}\mathbf1.
 \tag{1.5}
\]

If one common occurrence count (s) is used at every controlled rank,
then exactly

\[
 \sum_{|r-m|\le Q}
 \|\bar h_r^{\rm cat}-b_r^{(M)}\|_2^2
 =
 \frac{P^2(s-M)^2}{W}
 \left(1+2\sum_{q=1}^Q\lambda_q\right),
 \tag{1.6}
\]

where

\[
 \lambda_q=\frac{W}{\binom{2m}{m-q}}
 =\frac{W}{\binom{2m}{m+q}}.
 \tag{1.7}
\]

In particular, if (|s-M|=O(Q)), then

\[
 \boxed{
 \sum_{|r-m|\le Q}
 \|\bar h_r^{\rm cat}-b_r^{(M)}\|_2^2
 =O\!\left(\frac{WQ^3\lambda_Q}{M^2}\right)=o(W).}
 \tag{1.8}
\]

#### Proof

At rank (r), the squared norm is

\[
 N_r\left(\frac{P(s-M)}{N_r}\right)^2
 =\frac{P^2(s-M)^2}{N_r}.
\]

Summing the reciprocal layer sizes gives (1.6). Since (P=(1+o(1))W/M),
monotonicity of (lambda_q) gives the first bound in (1.8).

The central-binomial expansion gives, uniformly for (q\le Q=o(H)),

\[
 \log\lambda_q=\frac{q^2}{m}
 +O\!\left(\frac qm+\frac{q^3}{m^2}\right)=o(\log m).
\]

Hence \(\lambda_Q=m^{o(1)}\). Also
\(Q=o(\sqrt{m\log m})\), so

\[
 \frac{Q^3\lambda_Q}{M^2}=m^{-1/2+o(1)}=o(1).
\]

This proves (1.8). \(\square\)

For Z19, every cut deployment has

\[
 s=M+D,\qquad D=|O|=O(Q).
 \tag{1.9}
\]

For the unpadded one-path rectangular compiler,

\[
 s=(2t-1)(4Q+2),\qquad 0\le M-s<8Q+4.
 \tag{1.10}
\]

Thus both catalogues satisfy (1.8). This is the positive part of the
attack: the full fractional catalogue really does meet the scalar-centre
bias scale. If a nonmiddle scalar mean has fractional part bounded away
from zero and one, its distance to every balanced integral quota vector
still contains the quantization baseline
\(N_r\theta_r(1-\theta_r)=\Theta(N_r)\). Section 4 subtracts that baseline
exactly; (1.8) alone is not an integral rounding theorem.

## 2. Coordinate symmetry is transverse to a fixed cut fibre

### Theorem 2.1 (no nontrivial symmetric fixed-owner fibre)

Let \(U\) be one carrier and put

\[
 B=\binom Mm=\binom MH.
\]

There is no nonempty \(\operatorname{Sym}(U)\)-invariant catalogue of
positive literal objects which all have the same integral middle-owner
vector \(o\in\mathbb Z_{\ge0}^{\binom Um}\) of mass \(s\), when

\[
 0<s<B.
 \tag{2.1}
\]

#### Proof

If every object has owner vector (o), invariance of the catalogue gives
\(\sigma o=o\) for every \(\sigma\in\operatorname{Sym}(U)\).
Transitivity on \(\binom Um\) forces (o=c\mathbf1). Integrality gives
(c\in\mathbb Z_{\ge0}), while (s=cB), contradicting (2.1). \(\square\)

Every Z19 cut space has one fixed middle-owner vector. Theorem 2.1 says
that its full coordinate symmetrization necessarily ranges over many
different cut fibres. Therefore (1.3) is an **outer-frame average**, not
the barycenter of the low-variance sign fibre installed in Z19 Theorem
5.1.

This distinction is exact. It cannot be removed by choosing a more
ingenious probability law on the same signs.

## 3. Exact Z19 owner-fibre equivalence

Fix one Z19 scaffold \((\pi,\Gamma,O,A,B)\) in a carrier. Recall

\[
 A\cup B=\mathbb Z_M,\qquad A\cap B=O,
 \tag{3.1}
\]

and

\[
 \mathcal D_\chi
 =\Delta_\chi\pi|_A
 \sqcup\Gamma\Delta_\chi\pi|_B.
 \tag{3.2}
\]

Z19 Theorem 4.1 proves that the complete middle-owner vector is independent
of \(\chi\).

### Proposition 3.1 (exact base necklace plus (D) extras)

Let \(O_{\rm base}(\pi)\) be the owner vector of all (M) cyclic phases
of \(\pi\), and let \(I_m(\rho|_J)\) denote the middle-owner incidence
vector of the phases \(J\) on track \(\rho\). Then, for every cut sign
\(\chi\),

\[
 \boxed{
 O(\mathcal D_\chi)
 =O_{\rm base}(\pi)
 +I_m(\Gamma\pi|_O).}
 \tag{3.3}
\]

The second term is nonnegative and has mass (D=|O|=O(Q)).

#### Proof

It is enough to take \(\chi=0\), because the owner vector is
\(\chi\)-independent. Outside (O), exactly one of the two tracks in
(3.2) is present. By definition of (O), no middle interval notices any
installed adjacent swap there, so its owner equals the corresponding
owner of \(\pi\). At every phase in (O), both tracks are present: the
\(\pi\)-owner supplies the base phase and the \(\Gamma\pi\)-owner supplies
one extra occurrence. Summing over phases proves (3.3). \(\square\)

Now install one scaffold in each of the (P) carriers. Let
\(H_{\rm base}\) and \(H_{\rm cut}\) be the numbers of missing global
middle owners for the aggregate base necklaces and aggregate cut gadgets.
Adding nonnegative occurrences cannot create a hole, and (PD) extra
occurrences can fill at most (PD) holes. Hence

\[
 \boxed{
 0\le H_{\rm base}-H_{\rm cut}\le PD
 =O(WQ/M)=o(W).}
 \tag{3.4}
\]

### Corollary 3.2 (owner gate equivalence)

There is an (o(W))-hole selection of the installed Z19 cut gadgets if
and only if, up to an (o(W)) change in the leave, their underlying
one-cycle-per-carrier base necklaces have (o(W)) owner holes.

Thus cut signs do not attack the owner near-transversal at all. They can be
used only after the outer frames have already solved it.

## 4. Orbit dispersion and the required global covariance

The next statements quantify the failure of independent or locally
dependent outer-frame rounding. They apply at every hard rank and include
the exact floor correction.

Fix (r=m\pm q), (q\le Q), and suppose a selected catalogue object in
carrier (U) has a nonnegative integral rank-(r) load (X_U) of fixed
mass (s). Assume the marginal law of (X_U) is
\(\operatorname{Sym}(U)\)-invariant. Put

\[
 B_r=\binom Mr,qquad p_r=\frac{s}{B_r},qquad
 S=Ps,qquad \mu_r=\frac{S}{N_r}=k_r+\theta_r,
 \tag{4.1}
\]

where (k_r=\lfloor\mu_r\rfloor) and (0\le\theta_r<1). For a global
target (T), let

\[
 Z_T=\sum_{U\supseteq T}X_U(T),
 \tag{4.2}
\]

and define the exact floor energy

\[
 F_r=\sum_T(Z_T-k_r)(Z_T-k_r-1).
 \tag{4.3}
\]

For integral loads, (F_r\ge0), and (F_r=2\Psi_r), where \(\Psi_r\)
is factorial collision energy above its balanced integer minimum.

### Lemma 4.1 (one-carrier orbit dispersion)

For every fixed nonnegative integral local vector (x) of mass (s),

\[
 \boxed{
 \left\|\sigma x-\frac{s}{B_r}\mathbf1\right\|_2^2
 =\|x\|_2^2-\frac{s^2}{B_r}
 \ge s-\frac{s^2}{B_r}}
 \tag{4.4}
\]

for every coordinate permutation \(\sigma\). Consequently independent
outer-frame rounding has aggregate variance at least

\[
 P\left(s-\frac{s^2}{B_r}\right).
 \tag{4.5}
\]

#### Proof

The first equality follows by expanding the square, using invariance of
the norm and \(\sum x=s\). Since (x) is nonnegative and integral,
\(\sum x(T)^2\ge\sum x(T)=s\). Independent centered carrier vectors have
zero cross inner products in expectation, proving (4.5). \(\square\)

At middle rank, (B_r=\binom MH\) is superpolynomial and
\(s=(1+o(1))M\), so (4.5) is ((1-o(1))Ps=(1-o(1))W\).

### Theorem 4.2 (exact covariance identity and bounded-dependency no-go)

Define

\[
 D_r=\sum_U\sum_T\operatorname{Var}X_U(T),
 \qquad
 C_r=\sum_{U<V}\sum_T
 \operatorname{Cov}(X_U(T),X_V(T)).
 \tag{4.6}
\]

Then

\[
 \boxed{
 \mathbb EF_r=D_r+2C_r-N_r\theta_r(1-\theta_r).}
 \tag{4.7}
\]

Moreover,

\[
 D_r\ge P\left(s-\frac{s^2}{B_r}\right).
 \tag{4.8}
\]

For distinct carriers (U,V), writing (h=M-r),

\[
 \sum_T\operatorname{Cov}(X_U(T),X_V(T))
 \ge-\frac{h s^2}{M B_r}.
 \tag{4.9}
\]

If the carrier variables have a dependency graph of maximum degree
\(\Delta\), then

\[
 \boxed{
 \mathbb EF_r
 \ge
 P\left(s-\frac{s^2}{B_r}\right)
 -N_r\theta_r(1-\theta_r)
 -P\Delta\frac{h s^2}{M B_r}.}
 \tag{4.10}
\]

Uniformly in the calibrated hard window, \(\mu_r\ge1/2\) and
\(s/B_r=o(1)\). For all sufficiently large \(m\), if

\[
 \Delta\le\frac{M B_r}{8hs},
 \tag{4.11}
\]

then

\[
 \boxed{\mathbb EF_r\ge\frac14 Ps=\Omega(W).}
 \tag{4.12}
\]

#### Proof

For one target,

\[
 \mathbb E(Z_T-k_r)(Z_T-k_r-1)
 =\operatorname{Var}(Z_T)-\theta_r(1-\theta_r).
\]

Summing and expanding the variance gives (4.7). Local symmetry gives
\(\mathbb EX_U(T)=p_r\) for (T\subseteq U). Therefore

\[
 D_r
 =\sum_U\left(\mathbb E\|X_U\|_2^2-\frac{s^2}{B_r}\right),
\]

and integrality proves (4.8).

For (U\ne V), positivity gives

\[
 \sum_T\operatorname{Cov}(X_U(T),X_V(T))
 \ge-\binom{|U\cap V|}{r}p_r^2.
\]

Distinct (M)-carriers satisfy \(|U\cap V|\le M-1\), and

\[
 \binom{M-1}{r}
 =\frac{M-r}{M}\binom Mr
 =\frac hM B_r.
\]

This proves (4.9). A dependency graph has at most \(P\Delta/2\) dependent
pairs, proving (4.10).

Finally, \(N_r\theta_r(1-\theta_r)\le N_r/4\le Ps/2\), because
\(\mu_r=Ps/N_r\ge1/2\). Also \(s/B_r=o(1)\). Thus the first two terms in
(4.10) are at least \((1/2-o(1))Ps\). Under (4.11), the last term is at
most \(Ps/8\). For large \(m\), the remainder exceeds \(Ps/4\), proving
(4.12). \(\square\)

Let \(h_*=H-Q\). Since \(h/\binom Mh\) decreases for
\(h\in[h_*,H+Q]\), (4.11) holds at every controlled row if

\[
 \Delta\le
 \frac{M\binom M{h_*}}{8h_*s}
 =(1+o(1))\frac{\binom M{H-Q}}{8(H-Q)}.
 \tag{4.13}
\]

Consequently any marginally symmetric \(o(W)\)-energy rounding law must
use genuinely global dependence on the scale (0.5). Polynomial-degree,
bounded-range, pairwise-independent, and ordinary local-resampling laws
are excluded.

The theorem does not exclude a rare deterministic selector. Globally
relabeling such a selector would give complete dependence, outside the
hypothesis (4.13).

### Floor-baseline audit

At middle rank, \(\mu_0=S/W=1+o(1)\), because (s=M+O(Q)),
(PM=W-o(W)), and (Q=o(H)). Hence

\[
 W\theta_0(1-\theta_0)=o(W).
 \tag{4.14}
\]

Thus the (Omega(W)) raw frame dispersion is genuinely
(Omega(W)) middle floor energy unless cancelled globally. At a generic
nonmiddle row the quantization baseline may itself be (Theta(W)), so
raw variance alone is insufficient. Equation (4.10), which subtracts the
baseline exactly, is the valid nonmiddle statement.

## 5. Incorporating the bounded-influence middle-owner theorem

For the unpadded rectangular one-path compiler, let

\[
 O(E)=O(0)+\sum_{a=1}^{K}E_a d_a,
 \qquad K=pt=(1/16-o(1))M,
 \tag{5.1}
\]

with

\[
 \|d_a\|_1\le8,qquad \|d_a\|_2^2\le64.
 \tag{5.2}
\]

Every (d_a) is integral and has coordinate sum zero. The second constant
can therefore be sharpened internally:

\[
 \boxed{\|d_a\|_2^2\le32.}
 \tag{5.3}
\]

Indeed the total positive and total negative masses are equal and at most
four; concentrating each sign on one coordinate maximizes the squared
norm and gives (4^2+4^2=32).

Let

\[
 s=(2t-1)(4Q+2)=M-O(Q)
 \tag{5.4}
\]

be the unpadded owner mass, and let

\[
 \bar O=2^{-K}\sum_EO(E)
 \tag{5.5}
\]

be the inner-sign barycenter.

### Theorem 5.1 (macroscopic outer variance after inner averaging)

The vector \(\bar O\) is supported on at most

\[
 s+8K=(3/2+o(1))M
 \tag{5.6}
\]

middle owners. Consequently

\[
 \|\bar O\|_2^2\ge\frac{s^2}{s+8K}
 =(2/3-o(1))M.
 \tag{5.7}
\]

If \(\sigma\) is uniform in \(\operatorname{Sym}(U)\), then

\[
 \boxed{
 \mathbb E_\sigma
 \left\|\sigma\bar O-\frac{s}{\binom Mm}\mathbf1\right\|_2^2
 \ge(2/3-o(1))M.}
 \tag{5.8}
\]

#### Proof

All cube vertices are supported inside

\[
 \operatorname{supp}O(0)\cup\bigcup_a\operatorname{supp}d_a.
\]

The first support has size at most its nonnegative integral mass (s).
Since each integral (d_a) has support size at most \(\|d_a\|_1\), the
union has size at most (s+8K). The barycenter is nonnegative and has mass
(s), so Cauchy--Schwarz proves (5.7).

Outer symmetrization has mean
\((s/\binom Mm)\mathbf1\). Expanding the centered norm gives exactly

\[
 \|\bar O\|_2^2-\frac{s^2}{\binom Mm},
\]

and the second term is (o(1)). This proves (5.8). \(\square\)

Thus the (8/32) theorem does not control the outer frame. Independent
outer-frame rounding still contributes at least
\((2/3-o(1))W\) middle squared discrepancy after all inner signs have
already been averaged.

### Proposition 5.2 (frozen owner bundles)

Put

\[
 A_U=\bigcup_{a=1}^K\operatorname{supp}d_a.
 \tag{5.9}
\]

Then

\[
 |A_U|\le8K=(1/2+o(1))M.
 \tag{5.10}
\]

Every owner coordinate outside (A_U) has the same multiplicity in every
cube vertex, under arbitrary dependence among all signs and all carriers.
If (O(0)) is owner-simple, the set

\[
 F_U=\operatorname{supp}O(0)\setminus A_U
 \tag{5.11}
\]

has

\[
 |F_U|\ge s-8K=(1/2-o(1))M,
 \tag{5.12}
\]

and every owner in (F_U) occurs in every cube vertex.

Therefore any owner-near-factor made from these cubes must already choose
outer frames for which the frozen bundles \(F_U\) have only \(o(W)\)
aggregate overlaps. The variable support must then cover the residual
owner set compatibly. Inner signs cannot repair one frozen collision.
This is a coefficient-scale bundle-packing gate, not an \(o(W)\) cleanup;
the frozen bundles alone are not required to cover almost all owners.

Independent fair inner bits satisfy only

\[
 \operatorname{tr}\operatorname{Cov}O(E)
 =\frac14\sum_a\|d_a\|_2^2
 \le8K=O(M).
 \tag{5.13}
\]

After (P) carriers this is (O(W)), not (o(W)), and (5.13) contains no
negative cross-carrier covariance. The bounded-influence theorem is fully
compatible with a successful global coupling, but it does not construct
one.

## 6. A genuine literal symmetric-law counterexample

Fix one ambient cyclic order \(\omega\) on (V=[2m]). For every carrier
\(U\), restrict \(\omega\) to (U) and take the ordinary cyclic
one-path owner necklace.

Every middle owner (X) occurring in this system has the following
property: the (H) carrier coordinates of (U\setminus X) are consecutive
in \(\omega|_U\). The corresponding ambient arc contains a consecutive
ambient block of at least (H) coordinates, all outside (X). Therefore
the global owner support is at most

\[
 2m\binom{2m-H}{m}.
 \tag{6.1}
\]

In fact,

\[
 \frac{\binom{2m-H}{m}}{\binom{2m}{m}}
 =\prod_{j=0}^{H-1}\frac{m-j}{2m-j}
 \le2^{-H},
 \tag{6.2}
\]

so the support in (6.1) is \(o(W)\). Every path is literal and is internally
rainbow at middle rank, but the aggregate system misses \(W-o(W)\) owners.

Now choose a uniform global coordinate permutation \(\sigma\) and relabel
the entire construction. The resulting law is invariant under
\(\operatorname{Sym}(V)\). Transitivity on the global middle layer and
the fixed total mass \(PM\) give its exact fractional owner barycenter
\((PM/W)\mathbf1\). Nevertheless every realization is merely another
ambient cyclic frame and still has support \(o(W)\).

Finally install any Z19 cut signs on these shared-frame scaffolds. By
Proposition 3.1 their aggregate middle support is at most

\[
 o(W)+PD=o(W).
 \tag{6.3}
\]

This remains true for every, even completely dependent, sign choice.
Thus exact coordinate symmetry in law, exact fractional barycenter,
literal realizability, and arbitrary multi-carrier dependence of the Z19
signs can coexist with catastrophic owner failure.

The ambient cyclic construction is genuinely one path per carrier. Its
Z19 signed extension is the audited union of \(O(1)\) literal pieces per
carrier, with total reset overhead \(O(PQ)=o(W)\); no one-path signed Z19
compiler is asserted here.

This is not a counterexample to carrier-dependent outer-frame matching. It
is an exact counterexample to deriving such a matching from the symmetric
barycenter plus the inner sign structure alone.

## 7. A nonmiddle invariant of the cut rectangles

At its exceptional rank, every elementary adjacent-swap rectangle has the
form

\[
 \rho=
 e_{K\cup\{a,c\}}+e_{K\cup\{b,d\}}
 -e_{K\cup\{a,d\}}-e_{K\cup\{b,c\}},
 \tag{7.1}
\]

where (a,b,c,d) are distinct and disjoint from (K). Define the point
degree map

\[
 (A_rx)(z)=\sum_{S\ni z}x(S).
 \tag{7.2}
\]

### Proposition 7.1 (point-degree quotient is frozen)

For every elementary rectangle,

\[
 \boxed{A_r\rho=0.}
 \tag{7.3}
\]

Consequently all vertices of any installed Z19 cut fibre have exactly the
same point-degree vector at every rank. This remains true after arbitrary
multi-carrier dependent signing.

#### Proof

Each of (a,b,c,d) occurs once with positive and once with negative
coefficient in (7.1). Every element of (K) occurs in all four corners,
whose coefficients sum to zero. All other elements occur nowhere. This is
(7.3). \(\square\)

The operator norm is exact:

\[
 \|A_r\|_{2\to2}^2
 =r\binom{2m-1}{r-1}.
 \tag{7.4}
\]

Indeed (A_rA_r^T) has diagonal
\(\binom{2m-1}{r-1}\), off-diagonal
\(\binom{2m-2}{r-2}\), and largest eigenvalue equal to the row sum in
(7.4). Hence every desired vector (b_r) obeys the deterministic lower
bound

\[
 \boxed{
 \|h_r-b_r\|_2^2
 \ge
 \frac{\|A_r(h_r-b_r)\|_2^2}
 {r\binom{2m-1}{r-1}}.}
 \tag{7.5}
\]

The numerator in (7.5) is fixed before the cut signs are chosen. Full
coordinate averaging makes its **average** uniform, but inner signs cannot
move a selected scaffold in this quotient. This is the nonmiddle analogue
of exact owner freezing.

## 8. Audit and precise boundary

The decisive estimates were independently rederived after the first draft.
That audit confirmed (1.6), (4.7)--(4.13), the \(32\) direction constant,
and the \(2/3\) outer-frame constant. It also forced three scope
qualifications already incorporated above: (1.8) concerns the fractional
scalar centre, the frozen bundles need low overlap rather than near-cover
by themselves, and the universally forced covariance magnitude is
\(\Omega(W)\), not necessarily \(O(W)\), without a multiplicity bound.

### Proved

1. The full coordinate catalogue has the exact scalar barycenter (1.3).
2. Its (O(Q))-state adjustment from the original (M)-state centre has
   total squared size (o(W)), with the exact formula (1.6).
3. Full coordinate symmetry cannot occur inside one nontrivial fixed
   integral owner fibre.
4. Z19 middle owners equal the base necklace plus (D=O(Q)) positive
   extras, independently of every cut sign; the owner near-factor gate is
   therefore unchanged up to (o(W)).
5. The orbit-dispersion formula (4.4), exact floor-covariance identity
   (4.7), pair lower bound (4.9), and dependency threshold (4.13).
6. The sharpened owner-direction constant \(\|d_a\|_2^2\le32\), the
   ((2/3-o(1))M) between-frame lower bound, and the frozen bundle of
   size ((1/2-o(1))M) per owner-simple carrier.
7. A literal fully coordinate-symmetric law whose every shared-frame
   realization has only (o(W)) owner support, unchanged by arbitrary
   Z19 sign dependence.
8. The exact point-degree invariant of every elementary cut rectangle.

### Not proved

1. An arbitrary complete-dependence selection of genuinely
   carrier-dependent outer frames.
2. A low-overlap packing of the frozen owner bundles \(F_U\), compatible
   with coverage of the residual owner set by the variable part.
3. Negative covariance of magnitude at least \(\Omega(W)\) at each hard
   row, synchronized
   through all rows by one literal path choice per carrier.
4. The Z19 aggregate barycenter condition for one installed integral
   fibre per carrier. It is proved only for the fractional union of all
   outer frames.
5. SCC, GCC, TRP, MWB, or the coefficient-one contiguous-OR theorem.

The exact surviving gate is therefore

\[
 \boxed{
 \begin{array}{c}
 \text{choose carrier-dependent outer frames whose frozen owner bundles}\\
 \text{have }o(W)\text{ overlap, fit the variable residual, and then couple}\\
 \text{the inner signs with global negative covariance across all rows.}
 \end{array}}
 \tag{8.1}
\]

Coordinate-symmetric averaging proves the fractional target of this gate.
It supplies no integral rounding of it.
