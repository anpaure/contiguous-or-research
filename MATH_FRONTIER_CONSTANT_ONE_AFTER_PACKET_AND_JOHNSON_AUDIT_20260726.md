# Constant one after the packet and Johnson audits: the exact live frontier

Date: 2026-07-26

## 0. Status

Put

\[
 W=\binom{2m}{m},\qquad N_q=\binom{2m}{m-q}=\binom{2m}{m+q}.
\]

The local consecutive-window problem is solved.  There are explicit
isometric cube factors whose lower and upper depth-\(q\) trace maps are
injective simultaneously through a positive fraction of the cube
dimension.  The factor-blind compilation and the product-SCD tail are also
proved.  Consequently the remaining problem is entirely an **outer
integral chronology problem**.

Three distinctions are now theorem-level and must not be conflated.

1. Averaging complete coordinate frames gives an exact simultaneous
   fractional target cover at every depth.
2. Rounding by choosing one whole status-cell option on each common-owner
   component is impossible: the complete frame atlas has one owner
   component and a linear fixed-frame Gaussian deficit.
3. Selecting owner-disjoint subcube packets from incompatible frames is a
   strictly finer integral model.  It is not covered by the preceding
   no-go, and already has exact mixed-frame mosaics on \(J(4,2)\).

No proof of constant one is claimed here.  This note records the two exact
positive successor theorems and the quantitative obstructions that any
proof must cross.

## 1. The false model: whole-component frame rounding

For the complete quartet atlas, coordinate conjugation gives, for one
common option at all depths,

\[
 \mathbb E_\sigma\,\mu_{q,\sigma}(T)=\frac{W}{N_q}>1.
\]

Thus the simultaneous fractional Hall deficit is zero.  But quartet
switches connect all perfect matchings, and their coordinate union is
\(K_{2m}\).  The status-cell overlap therefore has one middle-owner
component.  An integral component selector chooses one global frame.  At
\(q=\lfloor A\sqrt m\rfloor\), every such option has

\[
 M_q^-+M_q^+\ge (2\delta_A-o(1))W,
 \qquad
 \delta_A=e^{-A^2}\Phi(A/2)-\Phi(-3A/2)>0.
\]

Hence

\[
 \eta_H^{\rm frac}=0,
 \qquad
 \eta_H^{\rm int}\ge(2\delta_A-o(1))W.
\]

This rules out the whole-component rounding theorem itself, not merely a
TU proof of it.  Edge-marginal transportation is even weaker: it contains
the determinant-two triangle minor and omits perfect-matching blossom
inequalities.

## 2. Live successor A: colored packet matching

For \(1\le r\le m\), let \({\cal H}_{m,r}\) have vertex set
\(\binom{[2m]}m\).  A packet is

\[
 P(F,M)=\{F\cup Z:Z\text{ chooses one endpoint of every edge of }M\},
\]

where \(|F|=m-r\) and \(M\) is an \(r\)-matching outside \(F\).  It has
\(2^r\) owners.  The exact incidence census is

\[
 D_{m,r}=\binom mr^2r!,
 \qquad
 |E({\cal H}_{m,r})|=\frac{(2m)!}{2^rr!(m-r)!^2}.
\]

If two owners have Johnson distance \(a\), their codegree is zero for
\(a>r\), and otherwise

\[
 \lambda_a=a!(r-a)!\binom{m-a}{r-a}^{\!2},
 \qquad
 \frac{\lambda_a}{D_{m,r}}
 =\frac{\binom ra}{\binom ma^2}.
\]

For \(r=o(m)\), the maximum nontrivial owner codegree is

\[
 \frac{\Delta_2}{D_{m,r}}=\frac r{m^2}.
\]

One fixed frame already partitions all but \(2^{-m+o(m)}W\) owners into
such packets.  Thus owner packing is not the gate.

Install one proved simultaneous trace factor in each packet.  Its literal
images \({\cal T}_{e,q}^{\pm}\) have size \(2^r\).  The exact open packet
statement is:

> **CPM.**  There exist \(H_m,r_m\) with
> \[
> H_m/\sqrt m\to\infty,\qquad H_m/r_m\to0,\qquad r_m=o(m),
> \]
> and an owner-disjoint family of compiler-labelled packets for which the
> owner leave is \(o(W)\) and
> \[
> \sum_{q\le H_m}\sum_{\epsilon\in\{-,+\}}
> \left(N_q-\left|\bigcup_e{cal T}_{e,q}^{\epsilon}\right|\right)
> =o(W).
> \]

`CPM` implies the exterior-moving strip theorem and hence constant one.
It is genuinely outside the whole-component model: already on \(J(4,2)\),

\[
 \{12,13\},\qquad\{14,24\},\qquad\{23,34\}
\]

are three disjoint packets from three frames whose coordinate union is
connected, yet they partition all six owners.

### 2.1 Exact fractional point and the nibble barrier

Quota-mark each signed depth-\(q\) trace with marginal \(N_q/W\), take the
full \(S_{2m}\)-orbit, and clear denominators.  Every owner and every typed
mandatory target then has the same degree.  Thus the augmented packet
hypergraph has an exact fractional perfect matching.

The relevant growing-rank small-codegree hypothesis nevertheless fails.
A mandatory depth-one target occurs with the two packet owners containing
it, so

\[
 \frac{\Delta_2}{D}\ge\frac2{m+1}.
\]

An all-depth packet column has rank at least \(2^{\Omega(H)}\), and on a
Gaussian window its mandatory rank is \(\Theta(2^r\sqrt m)\).  Therefore

\[
 K\frac{\Delta_2}{D}
 \ge \Omega\!\left(\frac{2^r}{\sqrt m}\right)\to\infty.
\]

Moreover, for every fixed residual density \(z<1\),

\[
 |E({\cal H}_{m,r})|z^{2^r}=o(1)
 \qquad(\log m\ll r=o(m)).
\]

So a random-like residual contains no packet after deleting even a fixed
positive owner fraction.  This does not refute `CPM`; the deterministic
fixed-frame near-tiling is a counterexample to that inference.  It proves
that `CPM` needs a structured resolution/trade construction, not a standard
regenerating nibble.

## 3. Live successor B: unrestricted Johnson memory circulation

Let \(P\) be a permutation of the middle layer whose edges lie in
\(J(2m,m)\).  It is \(H\)-safe if every first \(j\le H\) transitions from
every start form a geodesic.  Then

\[
 P^jX=X\setminus A_j(X)\cup B_j(X),
 \quad
 L_j(X)=X\setminus A_j(X),
 \quad
 U_j(X)=X\cup B_j(X),
\]

with nested deletion and insertion sets of size \(j\).

Let \(\Gamma_H\) be the safe length-\(H\) Johnson paths.  Variables
\(z_\gamma\) satisfy:

* one selected root path at each middle owner;
* equality of the selected prefix and suffix memory flows; and
* the signed target quota rows at every depth.

Integral solutions are exactly \(H\)-safe spanning cycle factors.  The
full coordinate orbit of one wreath gives an exact symmetric fractional
solution with load \(W/N_j\) on every signed target.  Thus this formulation
also has no fractional Hall obstruction.

Its chronology is not a direct product of the depthwise flag flows.  If
prescribed nested flags induce middle maps \(R_j\), one owner permutation
realizes them if and only if

\[
 R_j=R_1^j\qquad(0\le j\le H).
\]

There is also one common coordinate-run vector \((R_v)_{v\in[2m]}\),
\(\sum_vR_v=W\), and every integral solution obeys

\[
 \sum_{S\ni v}\mu_j^-(S)=\frac W2-jR_v,
 \qquad
 \sum_{T\ni v}\mu_j^+(T)=\frac W2+jR_v.
\]

Hence the high-quota designs at all depths must be chosen on one common
affine integer line.  Exact quota balance is not universally feasible
(already \(m=3,H=2\) gives a parity contradiction), although this finite
obstruction does not preclude asymptotic \(o(W)\) deficit.

At \(H=2\), the transition digraph has an exact symmetric circulation and
an Euler resolution into \((m-1)^2\) arc-state cycle covers.  The direct
depth-two conflict augmentation fails sharply: a fixed depth-two color has
\(\Theta(m^4)=\Theta(D^2)\) resource-disjoint competing wedges.  The live
gate is therefore an integral root-transversal of the memory circulation,
not a sparse-conflict nibble.

## 4. Bounded frame-changing primitives

There is an exact two-sided \(Q_8\) primitive whose actual cycle alternates
between two different ambient adjacent-direction matchings.  Its four
phase reflections form a closed frame carousel.  This proves that exact
successor/predecessor frame holonomy is locally possible.

Two boundaries are also exact.

1. One isometric \(C_{2h}\) has direction word \(\pi\pi\), and therefore
   carries only the two adjacent-pair frames determined by start parity.
2. On the minimal 24-owner quartet trade, any two-sided trace-injective
   2-factor is confined to one frame sector.  Every mixed hub creates a
   distinct repeated lower intersection or upper union.

Thus a bounded primitive is a valid frame-changing seed but cannot by
itself supply coefficient-one density.  A positive recursive composition
must either dilute its mixed hubs inside long payloads while preserving all
seam windows, or use it to construct the structured packet mosaic in
`CPM`.

## 5. Exact completion interface

Either of the following would now finish the theorem.

* Prove `CPM`.
* Construct an integral \(H_m\)-safe Johnson cycle factor with
  \(H_m/\sqrt m\to\infty\), total signed target holes \(o(W)\), and
  \(o(W/H_m)\) cycles (or with a larger safety scale so cycle merging has
  \(o(W)\) seam cost).

The proved factor-blind compiler then gives

\[
 \nu(2m)\le W+o(W),
\]

the product-SCD tail removes the exterior ranks, and the trimmed lift gives
the odd dimensions.  Sperner supplies the matching lower bound.

The remaining work is therefore not local trace coding, fractional Hall,
or tail control.  It is one structured integral chronology theorem in
either Section 2 or Section 3.
