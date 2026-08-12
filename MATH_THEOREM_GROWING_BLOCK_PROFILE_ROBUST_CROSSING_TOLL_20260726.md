# Growing block profiles: the exact transverse crossing toll

Date: 2026-07-26

Method: pure mathematics only. No computation, search, solver, or web input
is used.

## 0. Result and scope

Partition the \(2m\) physical coordinates into blocks of size \(b=b(m)\),
apart from one residual block. Write

\[
 F_b(Y)=\#\{\text{full \(b\)-blocks in }Y\}.
\tag{0.1}
\]

The bounded-gadget obstruction used \(F_b(T)=F_b(X)\) between a middle
owner and its lower target. This note allows arbitrary transverse moves,
so that identity may fail. The replacement is an exact robust cut.

Let \(S_{m,b}(k)\) count middle owners with profile \(k\), and let
\(T_{m,b,q}(k)\) count rank-\((m-q)\) lower targets with profile \(k\).
Define

\[
 \Delta_{m,b,q}
 :=\sum_k\bigl(T_{m,b,q}(k)-S_{m,b}(k)\bigr)_+ .
\tag{0.2}
\]

For every exact or partial packet factor at depth \(q\),

\[
 \boxed{B^{\rm help}_{b,q}+M^-_{b,q}\ge\Delta_{m,b,q}.}
\tag{0.3}
\]

Here \(M^-_{b,q}\) is the number of unhit targets in the positive-deficit
profile classes, and \(B^{\rm help}_{b,q}\) is the number of selected owner
occurrences which start outside those classes and end inside them. Every
helpful occurrence changes \(F_b\), and every such occurrence contains a
physical axis crossing the fixed block partition. Consequently each of

\[
 B^\times_{b,q}
 \quad\text{and}\quad
 V_{b,q}:=\sum_X|F_b(T_X)-F_b(X)|
\tag{0.4}
\]

may replace \(B^{\rm help}_{b,q}\) on the left of (0.3). The same theorem,
with empty blocks, holds for upper targets, for the same option choice and
every \(q\le H\).

Thus transverse moves evade the immutable-profile identity at an exact
exchange rate: one selected crossing window repairs at most one unit of
the Hall deficit. A large jump of \(F_b\) cannot fill several literal
target holes.

In the growing-block moderate-deviation range

\[
 b\to\infty,\qquad 2^b=o(\sqrt m),\qquad
 q=A\sqrt m+O(1),\quad A>0,
\tag{0.5}
\]

the deficit has logarithmic size

\[
 \boxed{
 \log {\Delta_{m,b,q}\over W}
 =-\left({A^2\over4}+o(1)\right){2^b\over b}.}
\tag{0.6}
\]

For fixed \(b\), it is \(\Theta_{A,b}(W)\). Hence:

1. bounded \(b\) forces a positive density of transverse windows;
2. every \(b\to\infty\) makes this full-block deficit \(o(W)\), so this
   witness alone cannot forbid an \(o(W)\)-hole construction;
3. at the finer \(W/H\) ledger, with \(H=A\sqrt m+O(1)\), it still forces
   more than \(W/H\) transverse windows below
   \[
       {2^b\over b}\sim {2\over A^2}\log m.
   \tag{0.7}
   \]

The corresponding transition block size is

\[
 b=\log _2\log m+\log _2\log\log m
      +\log _2{2\over A^2\log 2}+o(1).
\tag{0.8}
\]

There is also a genuinely simultaneous-depth scale. If
\(2^b=o(\sqrt{bm})\), then

\[
 \sum_{q\le H}\Delta_{m,b,q}
 =\left({2\over3\sqrt\pi}+o(1)\right)
 W\sqrt m\left({b\over2^b}\right)^{3/2}.
\tag{0.9}
\]

Thus the aggregate occurrence toll changes from \(\omega(W)\) to
\(o(W)\) at \(2^b/b\asymp m^{1/3}\).

Thus a no-go for all \(b=o(m)\) is false at the level of the full-block
cut. In particular \(b\asymp\log m\), \(b\asymp m^\alpha\), and the
diverse-compiler scale \(b\asymp\sqrt{mH}\) are beyond this obstruction.

## 1. Exact counts

Assume first that \(b\mid2m\), and put \(n=2m/b\). Let

\[
 h_b(z)=(1+z)^b-z^b.
\tag{1.1}
\]

Then, exactly,

\[
\begin{aligned}
 S_{m,b}(k)
   &=\binom nk[z^{m-bk}]h_b(z)^{n-k},\\
 T_{m,b,q}(k)
   &=\binom nk[z^{m-q-bk}]h_b(z)^{n-k}.
\end{aligned}
\tag{1.2}
\]

If \(b\nmid2m\), freeze the residual block and sum (1.2) over its possible
ranks. Every inequality below remains literal after that summation.

Let

\[
 K^+_{m,b,q}=\{k:T_{m,b,q}(k)>S_{m,b}(k)\}.
\tag{1.3}
\]

Then

\[
 \Delta_{m,b,q}
 =\sum_{k\in K^+_{m,b,q}}
       \bigl(T_{m,b,q}(k)-S_{m,b}(k)\bigr).
\tag{1.4}
\]

This is the sharp one-dimensional profile cut.

## 2. Robust multiple-choice Farkas theorem

Partition the atomic middle-owner occurrences into regions
\(\mathcal O_i\). Region \(i\) has an arbitrary option menu
\(\mathcal L_i\). An option may prescribe both signs, every depth, and
arbitrary chronology jointly. At fixed lower depth \(q\), write
\(T_{i\ell}(X)\) for the literal target emitted from
\(X\in\mathcal O_i\). Target injectivity is not assumed.

For a set \(K\) of profile values, define

\[
 C_{i\ell}(K)
 =\#\{X\in\mathcal O_i:
       F_b(X)\notin K,\ 
       F_b(T_{i\ell}(X))\in K\}.
\tag{2.1}
\]

### Theorem 2.1 (exact robust Farkas cut)

For

\[
 w_K(T)=\mathbf1_{\{F_b(T)\in K\}},
\tag{2.2}
\]

the option columns obey

\[
 \sum_i\max_{\ell\in\mathcal L_i}
       \langle w_K,a_{i\ell}^{-,q}\rangle
 \le
 \sum_{k\in K}S_{m,b}(k)
 +\sum_i\max_{\ell\in\mathcal L_i}C_{i\ell}(K).
\tag{2.3}
\]

Consequently the multiple-choice Farkas condition for hitting all targets
implies

\[
 \sum_i\max_{\ell}C_{i\ell}(K)
 \ge
 \sum_{k\in K}
       \bigl(T_{m,b,q}(k)-S_{m,b}(k)\bigr).
\tag{2.4}
\]

Taking \(K=K^+_{m,b,q}\) gives

\[
 \sum_i\max_{\ell}C_{i\ell}(K^+_{m,b,q})
 \ge\Delta_{m,b,q}.
\tag{2.5}
\]

For actually selected options \(\ell(i)\), if \(M^-_{b,q}\) targets in
the positive-deficit classes are left unhit, then

\[
 \sum_iC_{i,\ell(i)}(K^+_{m,b,q})+M^-_{b,q}
 \ge\Delta_{m,b,q}.
\tag{2.6}
\]

#### Proof

For a fixed region and option, split its occurrences by whether the owner
profile belongs to \(K\). The first part contributes at most

\[
 \#\{X\in\mathcal O_i:F_b(X)\in K\}
\]

weighted emissions. Every weighted emission from the second part is
counted by \(C_{i\ell}(K)\). Hence

\[
 \langle w_K,a_{i\ell}^{-,q}\rangle
 \le
 \#\{X\in\mathcal O_i:F_b(X)\in K\}+C_{i\ell}(K).
\]

The first term is independent of \(\ell\). Maximize over \(\ell\), sum
over \(i\), and use that the regions partition the owner occurrences.
This proves (2.3). The target demand in \(K\) is
\(\sum_{k\in K}T_{m,b,q}(k)\), proving (2.4) and (2.5).

For selected options, the same argument bounds the number of distinct hit
targets in \(K\) by the number of emitted occurrences there. At least the
demand minus \(M^-_{b,q}\) must be hit, proving (2.6). Target collisions
only strengthen the inequality. \(\square\)

### Theorem 2.2 (Lipschitz transport dual)

For an option put

\[
 V_{i\ell}=\sum_{X\in\mathcal O_i}
 |F_b(T_{i\ell}(X))-F_b(X)|.
\tag{2.7}
\]

If \(u:\mathbb Z_{\ge0}\to\mathbb R_{\ge0}\) is \(1\)-Lipschitz, then

\[
 \sum_i\max_\ell\langle u\circ F_b,a_{i\ell}^{-,q}\rangle
 \le
 \sum_ku(k)S_{m,b}(k)+\sum_i\max_\ell V_{i\ell}.
\tag{2.8}
\]

Thus exact target coverage requires

\[
 \sum_i\max_\ell V_{i\ell}
 \ge
 \sup_{\substack{u\ge0\\ {\rm Lip}(u)\le1}}
 \sum_ku(k)\bigl(T_{m,b,q}(k)-S_{m,b}(k)\bigr).
\tag{2.9}
\]

#### Proof

The Lipschitz inequality gives, occurrence by occurrence,

\[
 u(F_b(T_{i\ell}(X)))
 \le u(F_b(X))
    +|F_b(T_{i\ell}(X))-F_b(X)|.
\]

Sum over a region, maximize over its option, and then sum over regions.
This proves (2.8); comparison with the target demand proves (2.9).
\(\square\)

The indicator of any set of integer profile values is \(1\)-Lipschitz.
Taking \(u=\mathbf1_{K^+}\) in (2.9) recovers the variation form of the
sharp deficit \(\Delta_{m,b,q}\).

### Corollary 2.3 (profile motion and physical crossings)

Let

\[
 V_{b,q}=\sum_X|F_b(T_X)-F_b(X)|
\tag{2.10}
\]

and let \(B^\times_{b,q}\) count selected depth-\(q\) windows containing
an axis whose endpoints lie in different \(b\)-blocks. Then

\[
 \boxed{
 V_{b,q}+M^-_{b,q}\ge\Delta_{m,b,q},\qquad
 B^\times_{b,q}+M^-_{b,q}\ge\Delta_{m,b,q}.}
\tag{2.11}
\]

#### Proof

Every helpful crossing in (2.6) has distinct integer initial and final
profiles, so it contributes at least one to \(V_{b,q}\). If a window has
no cross-block axis, local rank in each block is constant throughout the
window. The immutable-profile argument then gives
\(F_b(T_X)=F_b(X)\). Thus every helpful crossing is counted by
\(B^\times_{b,q}\). Apply (2.6). \(\square\)

### Corollary 2.4 (both signs and all depths)

For upper targets let \(E_b(Y)\) count empty \(b\)-blocks.
Complementation identifies the rank-\((m+q)\) upper profile counts with
the lower counts in (1.2). Thus

\[
 B^{\times,+}_{b,q}+M^+_{b,q}\ge\Delta_{m,b,q}.
\tag{2.12}
\]

Equations (2.11) and (2.12) hold simultaneously for the same selected
option at every \(q\le H\). One physical crossing window may help both
signs, so no factor two is asserted.

### Corollary 2.5 (leave and floor-corrected energy)

Suppose \(L\) owner occurrences are omitted, and complete the partial
factor by adding at most those \(L\) missing occurrences. Then

\[
 B^\times_{b,q}+L+M^-_{b,q}\ge\Delta_{m,b,q}.
\tag{2.13}
\]

If the retained-mass floor at depth \(q\) is \(c_q\ge1\), its
floor-corrected energy satisfies

\[
 Q_q^-\ge
 c_q(c_q+1)\bigl(\Delta_{m,b,q}-B^\times_{b,q}-L\bigr)_+
 \ge
 2\bigl(\Delta_{m,b,q}-B^\times_{b,q}-L\bigr)_+.
\tag{2.14}
\]

The identical upper bound holds after complementation.

#### Proof

The completion supplies at most \(L\) additional helpful occurrences, so
(2.13) follows from (2.11). Hence at least
\((\Delta-B^\times-L)_+\) hard-profile targets have load zero. A zero-load
target contributes
\[
 (0-c_q)(0-c_q-1)=c_q(c_q+1)
\]
to the floor-corrected quadratic form. Sum these contributions. \(\square\)

## 3. Exact dispersed-axis consequence

Suppose a selected packet \(P\) is a cyclic word of length \(2r\), with
every physical axis occurring twice. Mark the occurrences of axes crossing
the \(b\)-block partition, and let their cyclic gaps be

\[
 g_1(P),\ldots,g_{2s(P)}(P),\qquad
 \sum_jg_j(P)=2r.
\tag{3.1}
\]

The exact fraction of cyclic starts whose depth-\(q\) window sees a marked
axis is

\[
 \phi_{P,q}
 ={1\over2r}\sum_{j=1}^{2s(P)}\min\{g_j(P),q\}.
\tag{3.2}
\]

Consequently, if \(|P|\) is the owner-occurrence mass represented by the
packet bank,

\[
 \sum_P|P|\phi_{P,q}+M^-_{b,q}\ge\Delta_{m,b,q}.
\tag{3.3}
\]

Since \(\phi_{P,q}\le qs(P)/r\),

\[
 \boxed{
 {1\over W}\sum_Ps(P)|P|
 \ge {r\over q}
 \left({\Delta_{m,b,q}\over W}-{M^-_{b,q}\over W}\right).}
\tag{3.4}
\]

#### Proof

A complementary cyclic gap of length \(g\) contributes \((g-q)_+\)
starts whose length-\(q\) arc avoids every marked occurrence. Hence the
number of starts seeing a marked occurrence is

\[
 2r-\sum_j(g_j-q)_+
 =\sum_j\min\{g_j,q\},
\]

which proves (3.2). Sum over packets and use Corollary 2.3. Finally,
\(\min(g_j,q)\le q\), and there are \(2s(P)\) marked occurrences, proving
(3.4). \(\square\)

The count \(s(P)\) is therefore insufficient without dispersion: (3.2)
is the exact necessary statistic.

## 4. Growing-\(b\) size of the deficit

Put

\[
 \lambda_b={2m\over b2^b}.
\tag{4.1}
\]

For a uniformly random middle owner, \(F_b\) has mean
\(\lambda_b(1+o(1))\) and conditional variance
\(\lambda_b(1+o(1))\), uniformly in (0.5). To see the variance, before
conditioning total rank one block's full indicator \(I\) and rank \(R\)
satisfy

\[
 p_b=2^{-b},\quad
 \operatorname{Var}I=p_b(1-p_b),\quad
 \operatorname{Cov}(I,R)={bp_b\over2},\quad
 \operatorname{Var}R={b\over4}.
\tag{4.2}
\]

The Schur-complement variance in the Gaussian conditioning is

\[
 p_b\bigl(1-(b+1)p_b\bigr),
\tag{4.3}
\]

and multiplication by \(n=2m/b\) gives the asserted conditional
asymptotic. The bivariate local saddle makes the Gaussian conditioning
uniform in (0.5).

Define the exact real saddle crossing

\[
 \kappa_{m,b,q}
 ={m/(2^b-1)-q/2\over b2^{b-1}/(2^b-1)}
 ={m\over b2^{b-1}}-{q(2^b-1)\over b2^b}.
\tag{4.4}
\]

It is the unique solution of
\[
 {m\over2^b-1}-{b2^{b-1}\over2^b-1}k={q\over2},
\]
which places the source and target coefficient indices symmetrically
about their common mean. Exact TP2 monotonicity, proved in Section 5,
then shows that the last deficit profile is
\(\kappa_{m,b,q}+o(\sqrt m/b)\). In particular, the source/target
likelihood crosses one at

\[
 k_c=\lambda_b-{A\sqrt m\over b}(1+o(1)).
\tag{4.5}
\]

More precisely, uniformly for fixed \(x>0\) and

\[
 k=\lambda_b-{x\sqrt m\over b}+o(\sqrt m/b),
\tag{4.6}
\]

coefficient extraction in (1.2) gives

\[
 \log {S_{m,b}(k)\over T_{m,b,q}(k)}
 =A^2-Ax+o(1).
\tag{4.7}
\]

Here is the saddle calculation. Normalize the coefficients of \(h_b\) by

\[
 \Pr(J=j)={\binom bj\over2^b-1},\qquad0\le j<b.
\]

At (4.6), the source coefficient index differs from
\((n-k)\mathbb EJ\) by

\[
 {x\over2}\sqrt m+o(\sqrt m),
\]

whereas the target index differs by

\[
 \left({x\over2}-A\right)\sqrt m+o(\sqrt m).
\]

Also

\[
 (n-k)\operatorname{Var}J={m\over2}+o(m).
\]

The exponent difference of the two coefficient saddles is therefore

\[
 -{x^2\over4}+\left({x\over2}-A\right)^2
 =A^2-Ax.
\]

The relative profile displacement is
\(O(2^b/\sqrt m)=o(1)\), so the triangular-array saddle remainder is
relative \(o(1)\) in the moderate-deviation rate.

The threshold (4.5) lies

\[
 d_b={A\sqrt m\over b}(1+o(1))
\tag{4.8}
\]

below the profile mean. Its moderate-deviation cost is

\[
 {d_b^2\over2\lambda_b}
 =\left({A^2\over4}+o(1)\right){2^b\over b}.
\tag{4.9}
\]

The positive-deficit profiles lie below (4.5), up to an
\(o(\sqrt m/b)\) displacement. Exponential tilting of the block vector
\((R,I)\) gives the upper bound in (0.6). For the lower bound, choose
\(\eta_m\downarrow0\) so slowly that
\[
 |\log\eta_m|=o(2^b/b),
\]
and take a profile band centered
\(\eta_m\sqrt m/b\) below \(k_c\), with smaller width tending to infinity.
Equation (4.7) makes \(T-S\) an
\(\exp(A\eta_m+o(\eta_m))-1\) fraction of \(S\). The logarithm of this
factor is negligible compared with (4.9), while the shifted band's tilted
mass has the same logarithmic cost. This proves (0.6).

This is a fixed-rank bivariate saddle argument; no unconditioned
independence approximation is used.

## 5. Exact critical and supercritical regimes

The coefficient array in (1.2) is totally positive of order two in rank
and profile. Equivalently,

\[
 {S_{m,b}(k)\over T_{m,b,q}(k)}
\quad\text{is nondecreasing in }k.
\tag{5.1}
\]

Thus \(K^+_{m,b,q}\) is an initial interval. The same saddle, now at a
nonquadratic tilt, yields the following sharp extension. Let

\[
 {2^b\over\sqrt m}\longrightarrow c\in(0,\infty),
\qquad
 I(u)=1-u+u\log u.
\tag{5.2}
\]

If \(c<2/A\), then

\[
 \log{\Delta_{m,b,q}\over N_q}
 =-\left({2\over c}
 I\!\left(1-{Ac\over2}\right)+o(1)\right){\sqrt m\over b}.
\tag{5.3}
\]

If \(c>2/A\), then

\[
 \Delta_{m,b,q}=0
\tag{5.4}
\]

for all sufficiently large \(m\). At \(c=2/A\),
\(\Delta_{m,b,q}=o(N_q)\). If \(2^b/\sqrt m\to\infty\), (5.4) again
holds eventually.

For completeness, the threshold in the critical regime is

\[
 k_c=\lambda_b\left(1-{Ac\over2}+o(1)\right).
\tag{5.5}
\]

When \(c<2/A\), the lower tail at this fixed relative displacement has
Poisson rate \(\lambda_b I(1-Ac/2)\), and
\(\lambda_b=(2/c+o(1))\sqrt m/b\), proving (5.3). When \(c>2/A\), the
formal crossing lies below zero. Monotonicity (5.1) then makes the raw
target/source ratio at \(k=0\) the largest one; its logarithm tends to

\[
 -A^2+{2A\over c}<0.
\tag{5.6}
\]

Hence no positive-deficit profile remains. The same argument gives the
supercritical assertion. At equality the leading logarithm vanishes, but
the total deficit is still \(o(N_q)\).

The TP2 statement and the uniform critical saddle, including the
convolution-of-TP2-arrays proof and the marked two-variable tilt, are
proved independently in
MATH_THEOREM_GROWING_BLOCK_PROFILE_SADDLE_THRESHOLD_20260726.md.

## 6. The two useful escape thresholds

### 6.1 Linear-hole scale

For fixed \(b\), the fixed-block local limit theorem gives

\[
 \Delta_{m,b,q}=\Theta_{A,b}(W).
\tag{6.1}
\]

For every \(b\to\infty\) in (0.5), (0.6) gives

\[
 \Delta_{m,b,q}=o(W).
\tag{6.2}
\]

Sections 5 and the critical formula show the same conclusion in all larger
block regimes. Thus the minimum growth which escapes a positive-density
full-block crossing toll is simply \(b\to\infty\). There is no uniform
\(\Omega_A(W)\) full-block cut over all growing \(b\).

### 6.2 The \(W/H\) exceptional ledger

Let \(H=A\sqrt m+O(1)\). From (0.6), for each fixed
\(\varepsilon>0\),

\[
 {2^b\over b}\le
 \left({2\over A^2}-\varepsilon\right)\log m
 \quad\Longrightarrow\quad
 \Delta_{m,b,H}\gg {W\over H},
\tag{6.3}
\]

whereas

\[
 {2^b\over b}\ge
 \left({2\over A^2}+\varepsilon\right)\log m
 \quad\Longrightarrow\quad
 \Delta_{m,b,H}\ll {W\over H}.
\tag{6.4}
\]

Both implications lie inside \(2^b=o(\sqrt m)\). Solving the equality
gives (0.8). Therefore a construction with only \(o(W/H)\) crossing
windows and holes is excluded below (6.3), even though \(b\to\infty\).
Above (6.4), the full-block cut is too small at that ledger.

### 6.3 Larger scales

Let
\[
 b=\beta\log_2m+o(\log m).
\]
If \(0<\beta<1/2\), then (0.6) reads
\[
 \log{\Delta_{m,b,q}\over N_q}
 =-\left({A^2\over4\beta}+o(1)\right)
 {m^\beta\over\log_2m}.
\tag{6.5}
\]
This is nonzero but much smaller than \(W/H\). If \(\beta>1/2\), then
\(\Delta_{m,b,q}=0\) eventually. At
\[
 b={1\over2}\log_2m+\gamma+o(1),
\]
formula (5.3) applies when \(2^\gamma<2/A\), and the deficit is zero
eventually when \(2^\gamma>2/A\).

For \(b=m^\alpha\), \(0<\alpha<1\), Section 5 gives
\(\Delta_{m,b,q}=0\) eventually. The same holds at
\(b\asymp\sqrt{mH}\). In particular, when \(H\asymp\sqrt m\),

\[
 \sqrt{mH}\asymp m^{3/4}.
\]

The exact robust theorem (2.6) remains true, but its right side is zero or
too small to constrain coefficient one. Any obstruction there must resolve
subblocks, ordered traces, or another profile whose fluctuations remain
macroscopic at that scale.

## 7. Precise surviving constructive statement

For any growing transverse atlas, the full-block test reduces to

\[
\begin{aligned}
 B^{\times,-}_{b,q}+M^-_{b,q}&\ge\Delta_{m,b,q},\\
 B^{\times,+}_{b,q}+M^+_{b,q}&\ge\Delta_{m,b,q},\\
 \sum_P|P|\phi_{P,q}+M^-_{b,q}&\ge\Delta_{m,b,q}
\end{aligned}
\tag{7.1}
\]

at every protected \(q\). For bounded \(b\), these force linear crossing
density. For growing \(b\) in (0.5), the exact required density is

\[
 {\Delta_{m,b,H}\over W}
 =\exp\!\left[-\left({A^2\over4}+o(1)\right){2^b\over b}\right].
\tag{7.2}
\]

A construction realizing that many helpful, correctly oriented crossings
escapes this particular dual. Merely listing that many cross-block axes
does not suffice unless their cyclic gaps pass (3.3), and no negative
floor-covariance conclusion follows from crossing density alone.

This is the proved boundary: transverse moves burn the full-block shield
only by paying the literal profile-transport mass in (7.1). That payment
tends to zero as a fraction of \(W\) for every growing block size, so a
new multiscale cut is needed to obstruct all \(b=o(m)\).

## 8. The sharp all-depth crossing toll

The single endpoint \(q=H\) is not the largest aggregate source of
crossing demand when \(b\to\infty\). Define

\[
 D_{\rm all}(H):=\sum_{q=1}^{H}\Delta_{m,b,q},
 \qquad
 \gamma_b:=\sqrt{{2b\over2^b}}.
\tag{8.1}
\]

Assume

\[
 b\to\infty,\qquad 2^b=o(\sqrt{bm}),\qquad
 H=A\sqrt m+O(1).
\tag{8.2}
\]

Then

\[
 \boxed{
 D_{\rm all}(H)
 =\left({2\over3\sqrt\pi}+o(1)\right)
 W\sqrt m\left({b\over2^b}\right)^{3/2}.}
\tag{8.3}
\]

Thus the aggregate is concentrated at depths

\[
 q\asymp \sqrt m\,\gamma_b
 =\sqrt{{2mb\over2^b}}=o(H),
\tag{8.4}
\]

not at \(q=H\).

Writing \(L_b=2^b/b\), (8.3) is
\[
 {D_{\rm all}(H)\over W}
 =\left({2\over3\sqrt\pi}+o(1)\right)
 {\sqrt m\over L_b^{3/2}}.
\]
Therefore the sharp aggregate occurrence transition is
\[
 L_b\asymp m^{1/3}.
\tag{8.4a}
\]
Equivalently,
\[
 b={1\over3}\log_2m+\log_2\log m+O(1).
\tag{8.4b}
\]
Below this scale the all-depth deficit is \(\omega(W)\); above it the
deficit is \(o(W)\). This is distinct from both the single-depth
\(W/H\) threshold (0.7) and the disappearance threshold
\(2^b\asymp\sqrt m\).

### Proposition 8.1 (local Gaussian-testing kernel)

Let \(\phi\) and \(\Phi\) be the standard normal density and distribution
function, and put

\[
 g(x)=x\phi(x)-x^2\Phi(-x),\qquad x\ge0.
\tag{8.5}
\]

Uniformly for \(x\) in compact subsets of \([0,\infty)\), if

\[
 q=x\sqrt m\,\gamma_b+O(1),
\tag{8.6}
\]

then

\[
 {\Delta_{m,b,q}\over W}
 =\gamma_b^2g(x)+o(\gamma_b^2).
\tag{8.7}
\]

#### Proof

Write

\[
 a={q\over\sqrt m}=x\gamma_b+o(\gamma_b).
\]

The source full-block profile has variance

\[
 \sigma_b^2={2m\over b2^b}(1+o(1)).
\tag{8.8}
\]

Lowering the rank by \(q\) decreases its mean by

\[
 d_b={2q\over2^b}(1+o(1)).
\tag{8.9}
\]

Hence the standardized mean displacement is

\[
 \eta_b={d_b\over\sigma_b}
 =x\gamma_b^2+o(\gamma_b^2).
\tag{8.10}
\]

Also

\[
 {N_q\over W}
 =\exp(-a^2+o(\gamma_b^2))
 =\exp(-x^2\gamma_b^2+o(\gamma_b^2)).
\tag{8.11}
\]

Let \(K\) have the target profile distribution
\[
 \Pr(K=k)={T_{m,b,q}(k)\over N_q},
\]
and standardize it as
\[
 Z_b={K-\mathbb EK\over\sigma_b}.
\tag{8.12}
\]
The marked bivariate saddle gives \(Z_b\Rightarrow Z\), where
\(Z\) is standard normal, together with uniform exponential tails.

Put
\[
 L_b(k)=\log{S_{m,b}(k)\over T_{m,b,q}(k)}.
\]
The coefficient-ratio saddle from Section 4, now expanded on the scale
(8.6), gives uniformly for bounded \(Z_b\)
\[
 {L_b(K)\over\gamma_b^2}
 =x^2+xZ_b+o(1).
\tag{8.13}
\]
Indeed \(x^2\gamma_b^2\) is the total-mass logarithmic ratio from
(8.11), while shifting the profile mean by \(\eta_b=x\gamma_b^2+o
(\gamma_b^2)\) contributes \(x\gamma_b^2Z_b\); the
\(\eta_b^2/2\) term is \(o(\gamma_b^2)\). The coefficient saddle error is
\(O(\sqrt{b/m})+O(\gamma_b^3)=o(\gamma_b^2)\) under (8.2).

Using the exact identity
\[
 {\Delta_{m,b,q}\over W}
 ={N_q\over W}\,
 \mathbb E\bigl[(1-e^{L_b(K)})_+\bigr],
\tag{8.14}
\]
divide by \(\gamma_b^2\). Equations (8.11) and (8.13), plus the uniform
exponential tails, permit dominated convergence and give
\[
\begin{aligned}
 \lim {1\over\gamma_b^2}{\Delta_{m,b,q}\over W}
 &=\mathbb E\bigl[-x(x+Z)\mathbf1_{\{Z<-x\}}\bigr]\\
 &=x\phi(x)-x^2\Phi(-x)=g(x).
\end{aligned}
\]
This proves (8.7). Exact TP2 ensures that the positive part in (8.14)
is one initial profile segment, although the expectation identity itself
already incorporates the correct sign. \(\square\)

### Proof of (8.3)

The mesh in the \(x\)-variable is

\[
 \Delta x={1\over\sqrt m\,\gamma_b}.
\tag{8.15}
\]

The same exponential tilt as in Section 4 gives, uniformly outside compact
\(x\)-sets,

\[
 {\Delta_{m,b,q}\over W}
 \le C\gamma_b^2(1+x^2)e^{-c x^2}
\tag{8.16}
\]

for absolute \(C,c>0\). Thus (8.7) may be summed by dominated Riemann
convergence through \(H\), since \(H/(\sqrt m\gamma_b)\to\infty\). We get

\[
 {D_{\rm all}(H)\over W}
 =(1+o(1))\sqrt m\,\gamma_b^3
 \int_0^\infty g(x)\,dx.
\tag{8.17}
\]

Now

\[
 \int_0^\infty x\phi(x)\,dx={1\over\sqrt{2\pi}},
\]

while Tonelli's theorem gives

\[
\begin{aligned}
 \int_0^\infty x^2\Phi(-x)\,dx
 &=\int_0^\infty\phi(t)
       \left(\int_0^t x^2\,dx\right)dt\\
 &={1\over3}\int_0^\infty t^3\phi(t)\,dt
 ={2\over3\sqrt{2\pi}}.
\end{aligned}
\]

Therefore

\[
 \int_0^\infty g(x)\,dx={1\over3\sqrt{2\pi}}.
\tag{8.18}
\]

Since

\[
 \gamma_b^3=2^{3/2}\left({b\over2^b}\right)^{3/2},
\]

substitution in (8.17) proves (8.3).

### Corollary 8.2 (cross-transition count)

Let \(E^\times_b\) be the total number of selected directed transition
occurrences whose physical axis crosses the \(b\)-block partition. A fixed
directed transition occurrence lies in at most \(q\) cyclic length-\(q\)
windows (exactly \(q\) when \(q\) is below the row-cycle length). Hence,
even after overlaps,

\[
 B^\times_{b,q}\le qE^\times_b,
 \qquad
 \sum_{q=1}^{H}B^\times_{b,q}
 \le {H(H+1)\over2}E^\times_b.
\tag{8.19}
\]

Summing (2.11) over \(q\le H\) yields the exact all-depth toll

\[
 \boxed{
 {H(H+1)\over2}E^\times_b
 +\sum_{q=1}^{H}M^-_{b,q}
 \ge D_{\rm all}(H).}
\tag{8.20}
\]

The same inequality holds for upper holes. Because the same transitions
may serve both signs, no factor two is forced.

If the aggregate lower holes are \(o(D_{\rm all}(H))\), then (8.3) gives

\[
 {E^\times_b\over W}
 \ge
 \left({4\over3A^2\sqrt\pi}+o(1)\right)
 {1\over\sqrt m}\left({b\over2^b}\right)^{3/2}.
\tag{8.21}
\]

This is the minimal necessary total transition density demanded by this
complete family of full-block cuts; it is not a sufficiency statement.
It is stronger than using \(q=H\) alone, but still tends to zero for every
\(b\to\infty\), so it does not restore an all-\(b=o(m)\) no-go.

## 9. Stronger directed \(F_b\)-drop transport

The occurrence cut counts one helpful window once. A lower target is the
intersection of the states in its window, hence

\[
 F_b(T_X)\le F_b(X).
\tag{9.1}
\]

This one-sided geometry gives a stronger toll when a window crosses many
profile boundaries.

Define the cumulative raw deficit and its directed transport mass by

\[
 A_{b,q}(j)=\sum_{k=0}^{j}
       \bigl(T_{m,b,q}(k)-S_{m,b}(k)\bigr),
 \qquad
 \mathcal W_{b,q}=\sum_{j\ge0}A_{b,q}(j)_+.
\tag{9.2}
\]

### Theorem 9.1 (exact directed earth-mover cut)

For a complete selected factor,

\[
 \boxed{
 \sum_X\bigl(F_b(X)-F_b(T_X)\bigr)
 \ge\mathcal W_{b,q}.}
\tag{9.3}
\]

If \(\mathcal M^-_q\) is a family of unhit lower targets, then

\[
 \sum_X\bigl(F_b(X)-F_b(T_X)\bigr)
 +\sum_{T\in\mathcal M^-_q}\bigl(n-F_b(T)\bigr)
 \ge\mathcal W_{b,q}.
\tag{9.4}
\]

#### Proof

Choose one preimage occurrence for every hit target. For an integer
boundary \(j\), owners with profile at most \(j\) can cover at most
\(\sum_{k\le j}S_{m,b}(k)\) targets below that boundary. Therefore at
least

\[
 \left(
 A_{b,q}(j)
 -\#\{T\in\mathcal M^-_q:F_b(T)\le j\}
 \right)_+
\]

chosen occurrences cross downward from \(F_b(X)>j\) to
\(F_b(T_X)\le j\). Sum over \(j\). One occurrence is counted exactly
\(F_b(X)-F_b(T_X)\) times. Also

\[
 \sum_{j\ge0}\mathbf1_{\{F_b(T)\le j<n\}}=n-F_b(T).
\]

Using \((a-h)_+\ge a_+-h\) proves (9.4); the case with no holes gives
(9.3). \(\square\)

Every full block lost from \(X\) to the intersection \(T_X\) requires a
transition deleting a coordinate from that block and inserting outside
it. Such a transition crosses the \(b\)-block partition, and one
transition can witness at most one lost full block. Thus the left side of
(9.3) is at most the total number of cross-block transition appearances
inside the depth-\(q\) windows.

### Proposition 9.2 (local and all-depth directed-drop asymptotics)

Under (8.2), put

\[
 h(x)=\int_{-\infty}^{\infty}
       \bigl(x\phi(z)-x^2\Phi(z)\bigr)_+\,dz.
\tag{9.5}
\]

Uniformly for compact \(x\)-sets and
\(q=x\sqrt m\,\gamma_b+O(1)\),

\[
 {\mathcal W_{b,q}\over W\sigma_b\gamma_b^2}
 \longrightarrow h(x),
 \qquad
 \sigma_b=\sqrt{{2m\over b2^b}}.
\tag{9.6}
\]

Furthermore,

\[
 \boxed{
 \sum_{q=1}^{H}\mathcal W_{b,q}
 =\bigl(4J+o(1)\bigr)W\,{mb\over4^b},}
\tag{9.7}
\]

where the absolute constant

\[
 J=\int_0^\infty h(x)\,dx
 ={1\over6}\int_{-\infty}^{\infty}
        {\phi(z)^3\over\Phi(z)^2}\,dz
 \in(0,\infty).
\tag{9.8}
\]

#### Proof

With \(K,Z_b,L_b\) as in Proposition 8.1, the cumulative signed profile
mass at a boundary \(K\le\mathbb EK+\sigma_bz\) equals

\[
 {N_q\over W}
 \mathbb E\!\left[
 (1-e^{L_b(K)})
 \mathbf1_{\{Z_b\le z\}}\right].
\tag{9.9}
\]

Divide by \(\gamma_b^2\) and use (8.11), (8.13), and dominated
convergence. The limit is

\[
\begin{aligned}
 \mathbb E[-x(x+Z)\mathbf1_{\{Z\le z\}}]
 &=x\phi(z)-x^2\Phi(z).
\end{aligned}
\tag{9.10}
\]

One unit in the profile coordinate is \(1/\sigma_b\) in \(z\), so
Riemann summation of the positive cumulative mass proves (9.6).
Uniform exponential tilting gives an integrable envelope in \(x,z\).
Summing over \(q\), whose \(x\)-mesh is
\((\sqrt m\gamma_b)^{-1}\), gives

\[
 {1\over W}\sum_{q\le H}\mathcal W_{b,q}
 =(J+o(1))\sqrt m\,\gamma_b\,\sigma_b\gamma_b^2
 =(4J+o(1)){mb\over4^b}.
\]

It remains to calculate \(J\). For fixed \(z\), the integrand in (9.5)
is positive exactly when
\[
 0<x<{\phi(z)\over\Phi(z)}.
\]
Tonelli's theorem therefore gives

\[
\begin{aligned}
 J
 &=\int_{-\infty}^{\infty}
   \int_0^{\phi(z)/\Phi(z)}
       x\bigl(\phi(z)-x\Phi(z)\bigr)\,dx\,dz\\
 &={1\over6}\int_{-\infty}^{\infty}
       {\phi(z)^3\over\Phi(z)^2}\,dz.
\end{aligned}
\]

As \(z\to-\infty\), the integrand is
\(O(z^2\phi(z))\); as \(z\to+\infty\), it is \(O(\phi(z)^3)\).
Thus \(0<J<\infty\). \(\square\)

### Corollary 9.3 (strong all-depth transition toll)

Let

\[
 \mathfrak M^-_{\rm wt}
 =\sum_{q=1}^{H}\sum_{T\in\mathcal M^-_q}
       \bigl(n-F_b(T)\bigr).
\tag{9.11}
\]

Since one directed transition appears in at most \(q\) depth-\(q\)
windows, (9.4) gives

\[
 \boxed{
 {H(H+1)\over2}E^\times_b+\mathfrak M^-_{\rm wt}
 \ge\sum_{q=1}^{H}\mathcal W_{b,q}.}
\tag{9.12}
\]

If

\[
 \mathfrak M^-_{\rm wt}=o\!\left(W{mb\over4^b}\right),
\tag{9.13}
\]

then

\[
 \boxed{
 {E^\times_b\over W}
 \ge\left({8J\over A^2}+o(1)\right){b\over4^b}.}
\tag{9.14}
\]

Compared with (8.21), this is stronger by the profile standard-deviation
factor

\[
 \sqrt{{2m\over b2^b}}\to\infty.
\]

Its hypothesis is correspondingly stronger: ordinary \(o(W)\) holes do
not automatically imply the weighted condition (9.13), because one
missing low-profile target can erase many cumulative boundary demands.
Thus (9.14) is the sharp full-\(F_b\)-drop toll, while (8.21) is the
unconditional occurrence toll under an unweighted aggregate-hole bound.

By complementation, every statement in this section holds for upper
targets with
\[
 E_b(X)-E_b(U_X)\ge0
\]
in place of \(F_b(X)-F_b(T_X)\). The constants and cumulative deficits
are identical. The same physical cross transition may pay the lower and
upper inequalities, so, again, no factor two is asserted.
