# Raw final report: ownership-overlay expansion and fragmentation (lane AB)

Date: 2026-07-24

## Verdict

This lane proves a genuine exact-factor ownership-overlay fragmentation
theorem, together with exact owner-graph and short-word overlay theorems.
It does **not** prove the remaining occurrence-pair heat gap.

The new structural fact is that every componentwise lower-rank occurrence
imbalance is exactly a difference of **noncyclic-containment leakages**.
This has strong consequences: in particular, a size-two transposition
component cannot contain two uncompensated copies of one target at any
depth, and at depth one the same is true for every component of size at
most three.  Thus small exact components really do separate same-target
duplicates.

The surviving obstruction is signed.  After opposite-target occurrences
inside each component are cancelled, residual component imbalances can
have both signs.  Their cross-component sign cancellation is not controlled
by owner-graph expansion, cycle rank, component number, or component size.
The fair occurrence-pair heat gap is exactly the positive correlation of
these leakage gradients.  A correlated component cut may still succeed
when the fair correlation is nonpositive, so the route-minimal open
statement remains the positive-cut/local-minimum lemma.

All constructions below remain integral inside one exact middle wreath
factor.  No fractional factor, separate rankwise factor, finite search, or
computational evidence is used.

## 1. Setting and implication scope

Put

\[
 n=2m+1,\qquad W=\binom{n}{m},\qquad
 B=\frac Wn=\operatorname{Cat}_m,
\]

\[
 N_q=\binom{n}{m-q},\qquad
 c_q=\left\lfloor\frac W{N_q}\right\rfloor,
 \qquad H_A=\lceil A\sqrt m\rceil
\]

for fixed \(A>0\).  Uniformly for \(q\le H_A\),

\[
 \log\frac W{N_q}
 =\frac{q(q+1)}m+O_A(m^{-1/2}),
\]

so \(c_q=O_A(1)\).

For an exact middle wreath factor \(F\), let \(\mu_q(S)\) be its
depth-\(q\) occurrence multiplicity and define the floor-corrected energy

\[
 Q_q(F)=\sum_S
   (\mu_q(S)-c_q)(\mu_q(S)-c_q-1),
\]

\[
 \mathcal Q_A(F)=
 \sum_{q\le H_A}\frac{Q_q(F)}{c_q}.
\]

The audited overload comparison is

\[
 Q_q(F)\ge 2O_q(F).
\]

Consequently \(\mathcal Q_A(F)=o(W)\) on every fixed window proves
fixed-window overload, then MWB by diagonalization, and hence the final
contiguous-OR asymptotic through the already audited literal transfer.

This implication is **unlabelled**.  Nothing in this report constructs one
common balanced nested resolution or proves labelled synchronization.

## 2. Exact transposition owner graph

Let \(\mathcal W_r(C)\) denote the family of cyclic \(r\)-intervals of a
wreath \(C\).  Fix a coordinate transposition

\[
 \tau=(u\ v).
\]

For \(C,D\in F\), define

\[
 a_{CD}=|\mathcal W_m(C)\cap\tau\mathcal W_m(D)|.
\]

### Theorem 2.1 (exact owner-orbit multigraph)

The matrix \(A=(a_{CD})\) is symmetric and every row has sum \(n\).
If \(d_C\in\{1,\ldots,m\}\) is the shorter cyclic distance between
\(u,v\) in \(C\), then

\[
 \boxed{
 a_{CC}=n-2d_C+2\mathbf 1_{\{d_C=m\}}.
 }
 \tag{2.1}
\]

Define the loopless multigraph \(\Gamma_\tau(F)\) on vertex set \(F\) by
placing \(a_{CD}\) parallel edges between \(C,D\) when \(C<D\).  Its
connected components are exactly the ownership-overlay components between
\(F\) and \(\tau F\).  Its degree at \(C\) is

\[
 \boxed{
 \deg_{\Gamma_\tau}(C)
 =n-a_{CC}
 =2d_C-2\mathbf1_{\{d_C=m\}}
 =2\min(d_C,m-1).
 }
 \tag{2.2}
\]

Consequently every component:

1. has at least two wreath owners;
2. is Eulerian;
3. has every cut of even multiplicity;
4. contains a cycle.

For a component \(K\),

\[
 |E(K)|=\sum_{C\in K}\min(d_C,m-1),
\]

and its cycle rank is exactly

\[
 \boxed{
 |E(K)|-|K|+1
 =1+\sum_{C\in K}(\min(d_C,m-1)-1).
 }
 \tag{2.3}
\]

For uniform \(\tau\),

\[
 \boxed{
 \mathbb E_\tau |E(\Gamma_\tau(F))|
 =B\left(\frac{m+1}{2}-\frac1m\right).
 }
 \tag{2.4}
\]

Hence some transposition has average off-diagonal degree at least

\[
 m+1-\frac2m
\]

and total cycle rank at least

\[
 B\left(\frac{m-1}{2}-\frac1m\right)+1.
\]

### Proof

For \(C\ne D\), applying \(\tau\) gives a bijection between the middle
sets counted by \(a_{CD}\) and those counted by \(a_{DC}\), proving
symmetry.  Since \(\tau F\) is an exact factor, every one of the \(n\)
middle intervals of \(C\) has one owner in \(\tau F\), proving the row
sum.

Across the \(n\) middle intervals of \(C\), exactly \(m-d_C\) contain
both \(u,v\), and exactly \(m-d_C+1\) contain neither.  These
\(n-2d_C\) intervals are fixed by \(\tau\).  Two moved middle intervals
of \(C\) can be exchanged by \(\tau\) and both remain in
\(\mathcal W_m(C)\) only if they are consecutive middle windows.  Their
exchanged boundary points then have cyclic distance \(m\).  Conversely,
when \(d_C=m\), exactly one such pair exists and contributes two further
members of the diagonal intersection.  This proves (2.1).

The diagonal overlap is always at least three.  Thus the left vertex
\(C\) and the right vertex \(\tau C\) lie in the same bipartite
ownership component and may be identified.  Off-diagonal ownership edges
then give exactly \(\Gamma_\tau(F)\), proving the component assertion.
Equation (2.2) follows from the row sum and (2.1).  Every degree is even
and at least two.  The Eulerian, cut-parity, non-singleton, and cycle-rank
claims follow immediately.

In one cyclic order, exactly \(n\) unordered coordinate pairs have each
cyclic distance \(d=1,\ldots,m\).  Since
\(\binom n2=nm\), the distance is uniform on \(\{1,\ldots,m\}\) for a
uniform coordinate transposition.  Averaging (2.2) and dividing the total
degree by two proves (2.4).  \(\square\)

### Scope

The theorem gives large cycle and multiplicity pressure, not
fragmentation.  Its conclusions permit one connected component, \(B/2\)
components, and every intermediate possibility.  No target-sensitive
heat statement follows from (2.1)--(2.4) alone.

## 3. Exact containment-leakage theorem

Fix

\[
 1\le q\le m-1,\qquad r=m-q,
\]

and let \(K\) be one ownership component with \(s=|K|\).  For an
\(r\)-set \(S\), define

\[
 x_K(S)=|\{C\in K:S\in\mathcal W_r(C)\}|,
\]

and, for one wreath \(C\),

\[
 h_C(S)=|\{X\in\mathcal W_m(C):S\subseteq X\}|.
\]

### Lemma 3.1 (cyclic containment bound)

For every \(C,S\),

\[
 \boxed{h_C(S)\le q+1,}
 \tag{3.1}
\]

with equality if and only if \(S\in\mathcal W_r(C)\).

### Proof

View \(C\) as a cycle on \(n\) positions.  A middle interval containing
\(S\) is complementary to a cyclic interval of length \(m+1\) contained
in the positional complement of \(S\).  The complement has

\[
 n-r=m+q+1<2(m+1)
\]

positions.  Decompose it into maximal consecutive runs of lengths
\(\ell_i\).  The number of length-\((m+1)\) intervals contained in these
runs is

\[
 h_C(S)=\sum_i(\ell_i-m)_+.
\]

At most one summand is nonzero, and it is at most

\[
 (m+q+1)-m=q+1.
\]

Equality forces the entire complement of \(S\) to be one run, equivalently
\(S\) itself to be one cyclic \(r\)-interval.  Conversely a cyclic
\(r\)-interval has exactly \(q+1\) middle extensions.  \(\square\)

Define the **noncyclic containment leakage**

\[
 e_K(S)=\sum_{C\in K}
 \left(
 h_C(S)-(q+1)\mathbf1_{\{S\in\mathcal W_r(C)\}}
 \right).
 \tag{3.2}
\]

### Theorem 3.2 (component leakage identity)

For every \(S\),

\[
 \boxed{
 0\le e_K(S)\le q(s-x_K(S)).
 }
 \tag{3.3}
\]

For \(T=\tau S\),

\[
 \boxed{
 (q+1)(x_K(S)-x_K(T))
 =e_K(T)-e_K(S).
 }
 \tag{L}
\]

The total leakage of one component is

\[
 \boxed{
 \sum_{S\in\binom{[n]}{m-q}}e_K(S)
 =ns\left(\binom mq-(q+1)\right).
 }
 \tag{3.4}
\]

Across all components,

\[
 \boxed{
 \sum_K e_K(S)
 =\binom{m+q+1}{q}-(q+1)\mu_q(S).
 }
 \tag{3.5}
\]

### Proof

Lemma 3.1 says that a genuine cyclic \(r\)-interval contributes zero to
(3.2), while every nongenuine target contributes an integer between zero
and \(q\).  This proves (3.3).

Let

\[
 U_K=\bigsqcup_{C\in K}\mathcal W_m(C)
\]

be the middle-root union owned by \(K\).  Component equivariance gives

\[
 U_K=\tau U_K.
\]

Therefore the number of roots in \(U_K\) containing \(S\) equals the
number containing \(T=\tau S\).  By (3.2), these two counts are

\[
 (q+1)x_K(S)+e_K(S),
 \qquad
 (q+1)x_K(T)+e_K(T),
\]

respectively.  Their equality proves (L).

For (3.4), each of the \(ns\) middle intervals owned by \(K\) contains
\(\binom mq\) rank-\((m-q)\) subsets.  The component contains \(ns\)
genuine cyclic \((m-q)\)-interval occurrences, and each subtracts
\(q+1\) in (3.2).  This proves (3.4).

For (3.5), the complete middle layer contains exactly
\(\binom{m+q+1}{q}\) middle supersets of a fixed \(S\).  Subtracting
\((q+1)\mu_q(S)\) proves the claim.  \(\square\)

## 4. Exact fragmentation consequences

Write

\[
 x=x_K(S),\qquad y=x_K(T),\qquad d_K=x-y.
\]

### Corollary 4.1 (component imbalance bound)

For every component,

\[
 \boxed{
 |x-y|
 \le
 \left\lfloor
 \frac{q(s-\min(x,y))}{q+1}
 \right\rfloor.
 }
 \tag{4.1}
\]

### Proof

Suppose \(x\ge y\).  From (L) and (3.3),

\[
 (q+1)(x-y)
 =e_K(T)-e_K(S)
 \le e_K(T)
 \le q(s-y).
\]

The case \(y\ge x\) is symmetric.  Integrality gives the floor.  \(\square\)

Consequently:

1. \(x=s\) if and only if \(y=s\).
2. If \(x=0\), then
   \[
   y\le\left\lfloor\frac{qs}{q+1}\right\rfloor.
   \]
3. A component containing \(t\) copies of \(T\) and no copy of \(S\)
   must have
   \[
   \boxed{
   s\ge\left\lceil\frac{(q+1)t}{q}\right\rceil.
   }
   \tag{4.2}
   \]
4. A size-two component has \(|d_K|\le1\) at every depth.
5. At \(q=1\), every component of size at most three has
   \(|d_K|\le1\).
6. In particular, a \((0,2)\) pair cannot be concentrated in a
   size-two component at any depth, and at depth one it requires a
   component of size at least four.

### Corollary 4.2 (bounded-component hole--duplicate separation)

Assume globally

\[
 \mu_q(S)=0,\qquad \mu_q(T)=t,
\]

and every ownership component has size at most \(L\).  Put

\[
 b=\left\lfloor\frac{qL}{q+1}\right\rfloor,
 \qquad t=ab+r,\qquad 0\le r<b.
\]

Then

\[
 \boxed{
 P_T^{\rm sep}
 \ge
 \binom t2-a\binom b2-\binom r2.
 }
 \tag{4.3}
\]

In particular, if \(q=1\) and \(L\le3\), then every copy of \(T\)
lies in a different component and

\[
 P_T^{\rm sep}=\binom t2.
\]

### Proof

When \(S\) is globally absent, (4.1) bounds the number of \(T\)
occurrences in any component by \(b\).  For fixed total \(t\), the number
of within-component duplicate pairs is maximized by filling \(a\)
components with \(b\) copies and one with \(r\) copies.  Subtracting this
maximum from \(\binom t2\) gives (4.3).  \(\square\)

This is a genuine exact-factor fragmentation theorem.  It proves useful
same-target separation, but it does not yet compare that gain with
opposite-target mixing.

## 5. Exact residual occurrence-pair identity

Fix one moved target pair

\[
 p=\{S,T=\tau S\},
\]

and for every component put

\[
 x_K=x_K(S),\qquad y_K=x_K(T),
 \qquad d_K=x_K-y_K,
\]

\[
 z=\sum_Kd_K=\mu_q(S)-\mu_q(T).
\]

Define

\[
 P_S^{\rm sep}=\sum_{K<J}x_Kx_J,
 \qquad
 P_T^{\rm sep}=\sum_{K<J}y_Ky_J,
\]

\[
 C_{ST}^{\rm sep}=\sum_{K\ne J}x_Ky_J.
\]

### Theorem 5.1 (residual fragmentation/mixing identity)

Put

\[
 \mathsf B_p=\binom{|z|}{2},
\]

\[
 \mathsf M_p=
 \frac{\sum_K|d_K|-|z|}{2},
\]

\[
 \mathsf R_p=
 \sum_K\binom{|d_K|}{2}.
\]

Then

\[
 \boxed{
 D_p:=P_S^{\rm sep}+P_T^{\rm sep}-C_{ST}^{\rm sep}
 =\mathsf B_p-\mathsf M_p-\mathsf R_p.
 }
 \tag{R}
\]

Equivalently,

\[
 \boxed{
 D_p=rac12\left(z^2-\sum_Kd_K^2\right)
 =\sum_{K<J}d_Kd_J.
 }
 \tag{5.1}
\]

If

\[
 P=\sum_K(d_K)_+,
 \qquad N=\sum_K(-d_K)_+,
\]

then

\[
 \mathsf M_p=\min(P,N).
\]

Thus \(\mathsf M_p\) is the residual opposite-sign mass after opposite
occurrences have first been cancelled **inside** each component, while
\(\mathsf R_p\) counts residual same-sign duplicate pairs still trapped
inside components.

Equality

\[
 D_p=\mathsf B_p
\]

holds exactly when every nonzero \(d_K\) has the sign of \(z\) and
magnitude one.

### Proof

Expanding the three separated-pair quantities gives

\[
 \begin{aligned}
 2D_p
 &=(x^2-\sum_Kx_K^2)+(y^2-\sum_Ky_K^2)
      -2(xy-\sum_Kx_Ky_K)\\
 &=(x-y)^2-\sum_K(x_K-y_K)^2\\
 &=z^2-\sum_Kd_K^2,
 \end{aligned}
\]

which proves (5.1).

Let \(a=\sum_K|d_K|\).  Then

\[
 2\mathsf M_p=a-|z|,
\]

and

\[
 2\mathsf R_p
 =\sum_K(|d_K|^2-|d_K|)
 =\sum_Kd_K^2-a.
\]

Therefore

\[
 2(\mathsf B_p-\mathsf M_p-\mathsf R_p)
 =|z|(|z|-1)-(a-|z|)-(\sum_Kd_K^2-a)
 =z^2-\sum_Kd_K^2.
\]

This proves (R).  The equality characterization follows from
\(\mathsf M_p=\mathsf R_p=0\).  \(\square\)

### Consequences

The sharp targetwise bounds are

\[
 -\mu_q(S)\mu_q(T)
 \le D_p\le\binom{|\mu_q(S)-\mu_q(T)|}{2}.
\]

If the two global loads are equal, then

\[
 D_p=-\frac12\sum_Kd_K^2\le0,
\]

with equality exactly when every component contains equally many
occurrences of the two targets.

If the overlay is connected, it has one component, so

\[
 \mathsf M_p=0,\qquad
 \mathsf R_p=\mathsf B_p,
 \qquad D_p=0.
\]

If every component has size two, Corollary 4.1 gives
\(|d_K|\le1\), hence

\[
 \mathsf R_p=0
\]

for every target pair.  Small exact components therefore eliminate the
same-sign concentration error completely.  The opposite-sign term
\(\mathsf M_p\) remains.

## 6. Leakage form of the heat gap

With

\[
 g_K=e_K(T)-e_K(S),
\]

the leakage identity (L) gives

\[
 d_K=\frac{g_K}{q+1}.
\]

Substitution into (5.1) yields the exact formula

\[
 \boxed{
 D_p
 =\frac1{2(q+1)^2}
 \left[
 \left(\sum_Kg_K\right)^2-
 \sum_Kg_K^2
 \right].
 }
 \tag{HG-L}
\]

Thus the occurrence-pair heat gap is precisely a positive
cross-component correlation theorem for leakage gradients.

Owner-graph expansion does not determine this sign.  A connected component
has maximal internal graph connectivity but gives \(D_p=0\).  At the
opposite extreme, two size-two components with residual patterns
\((1,0)\) and \((0,1)\) give \(d=(1,-1)\) and therefore \(D_p=-1\).
The latter pattern is an algebraic audit, not a claimed independently
constructed whole-factor counterexample.

The total leakage reservoir is also too large for a crude absolute bound:
already at \(q=1\), (3.4) equals

\[
 ns(m-2).
\]

Only signed alignment, not leakage cardinality, can prove the desired gap.

## 7. Integer parity floor and fair heat

Let

\[
 \epsilon_p=|z|\bmod2\in\{0,1\}.
\]

The ideal integral pair gain and the component-bundling excess are

\[
 G_p=\frac{z^2-\epsilon_p}{2},
\]

\[
 C_p=\frac{\sum_Kd_K^2-\epsilon_p}{2}.
\]

The residual identity gives the exact decompositions

\[
 \boxed{
 G_p
 =\mathsf B_p+left\lfloor\frac{|z|}{2}\right\rfloor,
 }
 \tag{7.1}
\]

\[
 \boxed{
 C_p
 =\mathsf M_p+\mathsf R_p+
   \left\lfloor\frac{|z|}{2}\right\rfloor.
 }
 \tag{7.2}
\]

Hence the parity term cancels exactly:

\[
 \boxed{G_p-C_p=D_p.}
 \tag{7.3}
\]

This independently checks the local parity floor from the first-wave heat
audit.

For a fixed transposition, let \(K\) run through the ownership components
and let

\[
 \Delta_{K,q}=\tau a_{K,q}-a_{K,q}
\]

be the depth-\(q\) component effect.  Define the weighted quantities

\[
 A_\tau=\sum_{q\le H_A}\frac1{c_q}
 \left\|\sum_K\Delta_{K,q}\right\|_2^2,
\]

\[
 V_\tau=\sum_{q\le H_A}\frac1{c_q}
 \sum_K\|\Delta_{K,q}\|_2^2.
\]

Put

\[
 \mathscr D_A(F,\tau)
 =\sum_{q\le H_A}\frac1{c_q}
   \sum_{p=\{S,\tau S\}}D_p,
\]

where every unordered moved pair is counted once.

### Theorem 7.1 (exact fair heat identity)

Choosing every component side independently and fairly produces an
integral exact factor \(F_\varepsilon\), and

\[
 \boxed{
 A_\tau-V_\tau=4\mathscr D_A(F,\tau),
 }
 \tag{7.4}
\]

\[
 \boxed{
 \mathbb E_\varepsilon\mathcal Q_A(F_\varepsilon)
 =\mathcal Q_A(F)-\mathscr D_A(F,\tau).
 }
 \tag{7.5}
\]

For the collision energy

\[
 \Psi_A=\mathcal Q_A/2,
\]

the expected decrease is \(\mathscr D_A/2\), not
\(\mathscr D_A\).

### Proof

On one moved pair, the component effect is \((-d_K,d_K)\).  Hence its
contribution to \(A_\tau\) is \(2z^2\), and its contribution to
\(V_\tau\) is \(2\sum_Kd_K^2\).  Equation (5.1) therefore gives

\[
 A_\tau-V_\tau=4\sum_{q,p}\frac{D_p}{c_q}.
\]

Writing the random child as its midpoint plus independent centered
component noise gives

\[
 \mathbb E\mathcal Q_A(F_\varepsilon)
 =\mathcal Q_A(F)-\frac14A_\tau+rac14V_\tau,
\]

which proves (7.5).  \(\square\)

## 8. The exact fair theorem still needed

The scale-correct well-chosen-transposition hypothesis is:

\[
 \boxed{
 \begin{aligned}
 \max_\tau
 \sum_{q\le H_A}\frac1{c_q}\sum_p
 \bigl(
 \mathsf B_p-\mathsf M_p-\mathsf R_p
 \bigr)
 \ge{}&
 \frac{\eta_A}{n}\mathcal Q_A(F)\\
 &-\frac{C_A}{n}H_A\operatorname{Cat}_m.
 \end{aligned}
 }
 \tag{RF_A}
\]

Here \(\eta_A>0\) and \(C_A<\infty\) must depend only on fixed \(A\),
and the statement is only required when \(\mathcal Q_A(F)\) is above a
constant multiple of \(H_A\operatorname{Cat}_m\).

### Conditional implication

Under \((RF_A)\), (7.5) and conditional expectation give one integral
exact child \(G\) with

\[
 \boxed{
 \mathcal Q_A(G)
 \le
 \left(1-\frac{\eta_A}{n}\right)\mathcal Q_A(F)
 +\frac{C_A}{n}H_A\operatorname{Cat}_m.
 }
 \tag{8.1}
\]

At a global minimizer \(F_*\) of \(\mathcal Q_A\), every exact child has
energy at least \(\mathcal Q_A(F_*)\).  Applying (8.1) gives

\[
 \boxed{
 \mathcal Q_A(F_*)
 \le\frac{C_A}{\eta_A}H_A\operatorname{Cat}_m.
 }
 \tag{8.2}
\]

Since

\[
 \operatorname{Cat}_m=\frac Wn,
 \qquad
 H_A\operatorname{Cat}_m=O_A(W/\sqrt m)=o(W),
\]

(8.2) proves fixed-window overload.  Diagonalization then proves MWB and
the final unlabelled OR asymptotic.

If (8.1) is iterated from a worst initial factor, the contraction rate is
only \(1-\eta_A/n\).  Reaching the Catalan scale can require

\[
 O_A(n\log W)=O_A(n^2)
\]

steps.  The global-minimizer argument avoids this iteration.

### Separated sufficient form

Write

\[
 \mathsf B_A
 =\sum_{q\le H_A}\frac1{c_q}\sum_p\mathsf B_p,
\]

\[
 \mathsf L_A
 =\sum_{q\le H_A}\frac1{c_q}
   \sum_p(\mathsf M_p+\mathsf R_p).
\]

A sufficient pair of estimates, for the **same** transposition, is

\[
 \mathsf B_A
 \ge
 \frac{\kappa_A}{n}\mathcal Q_A(F)
 -\frac{C_A^E}{n}H_A\operatorname{Cat}_m,
\]

\[
 \mathsf L_A
 \le
 (1-\delta_A)\mathsf B_A
 +\frac{C_A^F}{n}H_A\operatorname{Cat}_m.
\]

These imply \((RF_A)\) with

\[
 \eta_A=\delta_A\kappa_A,
 \qquad
 C_A=\delta_A C_A^E+C_A^F.
\]

Neither estimate is proved.  In particular, ordinary Johnson/Specht
quadratic smoothing controls \(z^2\), not the nonlinear quantity
\(\binom{|z|}{2}\), and does not control the leakage losses
\(\mathsf M_p,\mathsf R_p\).

## 9. Fair heat versus the weaker Max-Cut route

The fair theorem \((RF_A)\) is not the weakest legal selector statement.
Define

\[
 w_{KJ}
 =\sum_{q,p}\frac{d_{K,p}d_{J,p}}{c_q}.
\]

If \(I\) is a union of ownership components and \(F_I\) switches exactly
the components in \(I\), then

\[
 \boxed{
 \mathcal Q_A(F_I)-\mathcal Q_A(F)
 =-2\sum_{\substack{K\in I\\J\notin I}}w_{KJ}.
 }
 \tag{9.1}
\]

A random cut has expected energy decrease

\[
 \sum_{K<J}w_{KJ}=\mathscr D_A(F,\tau),
\]

but a correlated cut can be positive even when this total is nonpositive.
Thus the route-minimal theorem remains:

> **UNPROVED positive-cut/local-minimum lemma \(LM_A\).**  For every fixed
> \(A\), every exact factor that is locally minimal under every legal
> transposition-component cut satisfies
> \[
> \mathcal Q_A(F)=O_A(H_A\operatorname{Cat}_m).
> \]

Finite strict descent would then prove fixed-window overload.

## 10. Exact cube-orientation obstruction

For fixed \(F,\tau\), all vertices of the transposition component cube have
the same component partition.  Switching a component reverses the sign of
its effect but does not change its size or its orientation-blind local
data.  Fair resampling from any cube vertex returns the uniform law on the
same cube.  Therefore

\[
 \boxed{
 \mathscr D_A(F,\tau)
 =\mathcal Q_A(F)
 -\operatorname{avg}_{G\text{ in the cube}}\mathcal Q_A(G).
 }
 \tag{10.1}
\]

Averaging (10.1) over all cube vertices gives zero.  Hence component size,
cycle rank, absolute component imbalance, or any other orientation-blind
fragmentation statistic cannot force a positive fair gap on every cube
vertex.

If \(F_*\) globally minimizes \(\mathcal Q_A\) over all exact factors,
then every component-cube child is exact and has at least its energy.  Thus

\[
 \boxed{
 A_\tau(F_*)-V_\tau(F_*)\le0
 \quad\text{for every transposition }\tau.
 }
 \tag{10.2}
\]

This does not refute the thresholded alternative \((RF_A)\); rather,
applying \((RF_A)\) to \(F_*\) would force (8.2).  It does prove that an
unconditional assertion of a strictly positive well-chosen-transposition
gap for every exact factor is false.

## 11. Direct overlays for a short permutation

Let

\[
 \sigma=\tau_L\cdots\tau_1
\]

be any coordinate permutation, and consider the direct ownership overlay
between \(F\) and \(\sigma F\).  For a direct component \(K\), let
\(a_K(S)\) and \(b_K(S)\) be its left- and right-side occurrence counts,
and put

\[
 \Delta_K=b_K-a_K.
\]

Every independent component-side choice is again an integral exact factor.

### Theorem 11.1 (general endpoint heat identity)

Put

\[
 A_{\sigma,q}=\|f_q-\sigma f_q\|_2^2,
 \qquad
 V_{\sigma,q}=\sum_K\|\Delta_{K,q}\|_2^2.
\]

Then

\[
 \boxed{
 \mathbb E Q_q(F_\varepsilon)
 =Q_q(F)-\frac14(A_{\sigma,q}-V_{\sigma,q}).
 }
 \tag{11.1}
\]

Define

\[
 P_S^L=\sum_{K<J}a_K(S)a_J(S),
 \qquad
 P_S^R=\sum_{K<J}b_K(S)b_J(S),
\]

\[
 C_S^{LR}=\sum_{K\ne J}a_K(S)b_J(S).
\]

Then

\[
 \boxed{
 A_{\sigma,q}-V_{\sigma,q}
 =2\sum_S(P_S^L+P_S^R-C_S^{LR}).
 }
 \tag{11.2}
\]

### Proof

The random child load is its endpoint midpoint plus centered independent
component noise:

\[
 \mu'_q
 =\frac{\mu_q+\sigma\mu_q}{2}
 +\frac12\sum_K\varepsilon_K\Delta_{K,q}.
\]

Since \(\sigma\) is orthogonal and the integer floor is
factor-independent,

\[
 \left\|\frac{f_q+\sigma f_q}{2}\right\|_2^2
 =\|f_q\|_2^2-rac14\|f_q-\sigma f_q\|_2^2.
\]

The noise variance is \(V_{\sigma,q}/4\), proving (11.1).  Direct
expansion of the scalar left/right component counts proves (11.2).
\(\square\)

Without component equivariance, the negative term in (11.2) concerns
left/right copies of the same target.  It cannot automatically be
reinterpreted as mixing between \(S\) and \(\sigma^{-1}S\) inside one
common owner subset.

## 12. General endpoint parity floor

Put

\[
 b_{\sigma,q}
 =\frac14\#\{S:
 \mu_q(S)-\mu_q(\sigma^{-1}S)\text{ is odd}\}.
\]

Then

\[
 G_{\sigma,q}=\frac14A_{\sigma,q}-b_{\sigma,q}\ge0,
\]

\[
 C_{\sigma,q}=\frac14V_{\sigma,q}-b_{\sigma,q}\ge0,
\]

and

\[
 \boxed{
 \mathbb E Q_q(F_\varepsilon)
 =Q_q(F)-G_{\sigma,q}+C_{\sigma,q}.
 }
 \tag{12.1}
\]

If

\[
 \delta_S=\mu_q(\sigma^{-1}S)-\mu_q(S),
\]

then

\[
 \boxed{
 G_{\sigma,q}
 =\sum_S\left\lfloor\frac{\delta_S^2}{4}\right\rfloor.
 }
 \tag{12.2}
\]

Moreover,

\[
 \boxed{0\le G_{\sigma,q}\le Q_q(F).}
 \tag{12.3}
\]

### Proof of the upper bound

For integers \(x,y\), put

\[
 a=x-c_q,\qquad b=y-c_q.
\]

Then

\[
 2\left\lfloor\frac{(x-y)^2}{4}\right\rfloor
 \le a(a-1)+b(b-1).
 \tag{12.4}
\]

If \(a-b\) is even, the right side minus the left side equals

\[
 \frac{(a+b)(a+b-2)}2\ge0,
\]

because \(a+b\) is even.  If \(a-b\) is odd, the difference is

\[
 \frac{(a+b-1)^2}{2}\ge0.
\]

Sum (12.4) with \(x=\mu_q(S)\) and
\(y=\mu_q(\sigma^{-1}S)\).  Each floor-energy term is counted twice,
giving (12.3).  \(\square\)

The inequality \(C_{\sigma,q}\ge0\) follows because the component noise
at a coordinate with half-integral midpoint has variance at least \(1/4\).

## 13. Failure of direct equivariance beyond one transposition

For a single transposition, every component has sides

\[
 R_K=\tau L_K.
\]

The proof uses a fixed middle interval in every wreath.  This mechanism does
not extend automatically to a short permutation.

For example, in the cyclic order

\[
 0,1,\ldots,2m,
\]

let

\[
 \sigma=(0\ m)(1\ m+1).
\]

Each transposed pair has cyclic distance \(m\) and therefore has a unique
middle interval containing neither member.  The two unique intervals are
different, and no middle interval contains both members of either pair.
Thus no length-\(m\) interval is fixed by \(\sigma\).  Since any cyclic
wreath occurs in a relabelling of an exact factor, the one-transposition
fixed-edge proof genuinely fails inside the exact-factor universe.

This example does not by itself prove that a whole direct endpoint
component is nonequivariant; it proves only that the universal ownerwise
identification argument is unavailable.

## 14. Layered short-word coarsening theorem

There is an exact equivariant replacement for a fixed word, but it only
coarsens components.

Put

\[
 \sigma_0=1,\qquad
 \sigma_i=\tau_i\sigma_{i-1},
 \qquad F_i=\sigma_iF.
\]

Build the layered graph with vertex layers \(F_0,\ldots,F_L\), adding all
middle ownership edges between consecutive layers.

### Theorem 14.1 (layered endpoint bundles)

For a global layered component \(\Omega\), let

\[
 K_i=\Omega\cap F_i.
\]

Then

\[
 \boxed{
 K_i=\tau_iK_{i-1},
 \qquad
 K_L=\sigma K_0.
 }
 \tag{14.1}
\]

Every \(K_i\) owns exactly the same collection of middle sets.  Therefore,
independently for each \(\Omega\), choosing either endpoint side \(K_0\)
or \(K_L\) produces an integral exact factor supported on
\(F\sqcup\sigma F\).

Let

\[
 \rho_i=\sigma_{i-1}^{-1}\tau_i\sigma_{i-1},
\]

and let \(\mathcal P_i\) be the transposition-component partition of
\(F\) for \(F\) versus \(\rho_iF\).  The endpoint bundle partition is
exactly

\[
 \boxed{
 \mathcal P_w
 =\mathcal P_1\vee\cdots\vee\mathcal P_L,
 }
 \tag{14.2}
\]

the join of these equivalence relations.  Hence appending letters can only
merge bundles:

\[
 \#\mathcal P_w\le\min_i\#\mathcal P_i.
\]

If any one adjacent overlay is connected, the entire layered endpoint
partition is connected.  Its endpoint cube then contains only \(F\) and
\(\sigma F\), so

\[
 \boxed{
 V_\sigma=A_\sigma,
 \qquad G_\sigma=C_\sigma,
 }
 \tag{14.3}
\]

and its restricted fair heat gap is zero.

### Proof

For every \(C\in K_{i-1}\), the one-transposition fixed-edge theorem joins
\(C\) to \(\tau_iC\) in the next layer, so

\[
 \tau_iK_{i-1}\subseteq K_i.
\]

All adjacent ownership edges incident with either side remain within the
same global component, making the induced adjacent graph \(n\)-regular on
both sides.  Thus the two sides have equal cardinality and the inclusion is
an equality.  This proves (14.1).  The same ownership edges show that the
middle-root unions are identical in consecutive layers.

Pulling the \(i\)-th interface back by \(\sigma_{i-1}^{-1}\) gives the
transposition \(\rho_i\) on \(F\).  A global layered path is exactly a
chain generated by these pulled-back component equivalences, proving the
join formula (14.2).  The remaining conclusions follow immediately.
\(\square\)

Each layered endpoint bundle is a union of direct \(F\)-versus-\(\sigma F\)
components.  Thus the direct endpoint overlay may have additional
nonequivariant switches; connectedness of the layered overlay does not imply
connectedness of the direct endpoint overlay.

## 15. Equivariant word occurrence formula

For a layered endpoint bundle, let \(x_K(S)\) be its left occurrence count.
Equation (14.1) gives

\[
 b_K(S)=x_K(\sigma^{-1}S),
\]

\[
 \Delta_K(S)=x_K(\sigma^{-1}S)-x_K(S).
\]

Define

\[
 P_S^{\rm sep}=\sum_{K<J}x_K(S)x_J(S),
\]

\[
 C_{S,T}^{\rm sep}=\sum_{K\ne J}x_K(S)x_J(T).
\]

Then

\[
 \boxed{
 A_{\sigma,q}-V_{\sigma,q}
 =4\sum_SP_S^{\rm sep}
 -2\sum_SC_{S,\sigma^{-1}S}^{\rm sep}.
 }
 \tag{15.1}
\]

Equivalently,

\[
 \boxed{
 G_{\sigma,q}-C_{\sigma,q}
 =\sum_SP_S^{\rm sep}
 -\frac12\sum_SC_{S,\sigma^{-1}S}^{\rm sep}.
 }
 \tag{15.2}
\]

Every bundle preserves each \(\sigma\)-orbit total.  When \(\sigma\) is
one transposition, (15.2) reduces to

\[
 P_S^{\rm sep}+P_{\sigma S}^{\rm sep}
 -C_{S,\sigma S}^{\rm sep}.
\]

Merging two endpoint bundles \(U,V\) changes the fair gap by

\[
 \begin{aligned}
 &-\sum_Sx_U(S)x_V(S)\\
 &\quad+\frac12\sum_S
 \left[
 x_U(S)x_V(\sigma^{-1}S)
 +x_V(S)x_U(\sigma^{-1}S)
 \right]\\
 &=-\frac12\langle\Delta_U,\Delta_V\rangle.
 \end{aligned}
 \tag{15.3}
\]

Thus coarsening can help or hurt.  Fragmentation count alone has no sign.

The containment-leakage theorem also extends verbatim to every layered
bundle: its middle-root union is \(\sigma\)-invariant, so (L) holds with
\(T=\sigma^{-1}S\).  The difficulty is that the join operation in
(14.2) only enlarges these bundles.

## 16. Fixed-word signed-space obstruction

Suppose a fixed word has length \(L\) and

\[
 2L\le n-4.
\]

Choose four coordinates \(a,b,c,d\) untouched by every transposition in
the word.  On rank \(r=m-q\), define

\[
 v(S)=
 (\mathbf1_{a\in S}-\mathbf1_{b\in S})
 (\mathbf1_{c\in S}-\mathbf1_{d\in S}).
\]

Then \(v\ne0\), has zero total and zero point marginals, and every letter
of the word fixes \(v\).  Thus neither the endpoint permutation nor the
sequential midpoint projections contract this admissible \(U_2\) signed
direction.

In particular, a fixed word of \(o(\sqrt m)\) transpositions has no
universal coherent spectral gap on the full signed discrepancy space.

This is not an exact-factor counterexample.  The signed-lattice surjectivity
theorem supplies neither nonnegativity nor a packing-compatible realization
of \(v\) inside one exact factor.

## 17. Endpoint bundles versus sequential recomputation

The layered endpoint construction and a sequential heat chain are different
objects.

The endpoint bundle heat has coherent mean

\[
 \frac{I+\sigma}{2}f.
\]

A sequential word with components recomputed after each random choice has
coherent operator

\[
 \frac{I+\tau_L}{2}\cdots\frac{I+\tau_1}{2}
\]

plus propagated martingale component noise.  The join theorem applies only
to the fixed endpoint-bundle cube.  Sequential noise identities require the
word to be fixed before component signs are exposed.

Therefore the only viable short-word escape is genuinely noncommutative:

1. switch components in the current factor;
2. recompute the next overlay in the changed factor;
3. allow neutral routing steps;
4. eventually expose a positive correlated cut.

No theorem establishing this state-dependent sequence is known.

## 18. Independent audit corrections and caveats

The decisive algebra and constants were independently audited.  The
following scope corrections are essential.

1. **Correct Gaussian exponent.**  The fixed-window expansion is
   \(q(q+1)/m+O_A(m^{-1/2})\), not merely \(q^2/m\).

2. **Full energy versus collision energy.**  The fair decrease in
   \(\mathcal Q_A\) is \(\mathscr D_A\); the decrease in
   \(\Psi_A=\mathcal Q_A/2\) is \(\mathscr D_A/2\).

3. **All heat factors.**  For one transposition,
   \(A_\tau-V_\tau=4\mathscr D_A\), and the fair drift is
   \(-(A_\tau-V_\tau)/4\).

4. **Per-step versus terminal residue.**  The one-step error in
   \((RF_A)\) is
   \[
   \frac{C_A}{n}H_A\operatorname{Cat}_m.
   \]
   The terminal scale is
   \[
   O_A(H_A\operatorname{Cat}_m),
   \]
   with no extra \(1/n\).

5. **Fair versus signed heat.**  The residual identity controls fair
   component resampling.  A correlated Max-Cut can descend even when the
   fair correlation is nonpositive.  Thus \((RF_A)\) is stronger than
   \(LM_A\).

6. **Component fragmentation is color-sensitive.**  Small components
   eliminate \(\mathsf R_p\) but not \(\mathsf M_p\).  The latter is the
   exact opposite-sign leakage cancellation still requiring proof.

7. **Connected overlays.**  A connected overlay gives exactly zero fair
   gap, not positive smoothing.  Its covariance cancels the entire coherent
   midpoint contraction.

8. **Short permutations.**  Direct component equivariance is not available
   for a general permutation.  Layered equivariance is available only at
   the cost of joining, hence merging, the intervening transposition
   partitions.

9. **Fixed words.**  The untouched-\(U_2\) example is a signed-space
   obstruction only, not an exact-factor counterexample.

10. **Minimizer obstruction.**  At a global exact-factor minimizer, every
    fair transposition or endpoint cube has nonpositive gap.  A valid theorem
    must therefore have the explicit Catalan-floor alternative.

11. **Iteration length.**  A one-step rate \(1-\eta_A/n\) requires
    \(O_A(n\log W)=O_A(n^2)\) steps from a worst starting factor.  One
    \(O(n)\) block supplies only constant coherent contraction.

12. **No labelled conclusion.**  Even a proof of \((RF_A)\) or \(LM_A\)
    gives fixed-window overload and MWB, not a nearby common balanced nested
    owner resolution.  Labelled synchronization remains strictly stronger.

13. **Abstract pair patterns.**  The algebraic patterns
    \(d=(1,-1)\) and \(d=(1,1)\) demonstrate the sign issue but are not
    asserted as independently realized complete exact-factor examples.

14. **Integrality.**  Every component-side child and every layered endpoint
    bundle child used in the positive statements is a literal integral exact
    factor.  No fractional averaging is used to assert existence; fair
    expectations are converted to an actual child by conditional
    expectation or minimization.

## 19. Final proved/open ledger

### Proved

1. The exact owner-orbit graph formulas (2.1)--(2.4), including even
   degrees, Eulerian components, cycle rank, and averaged edge count.
2. The cyclic containment bound (3.1).
3. The exact component leakage identity (L), total leakage (3.4), and
   global leakage formula (3.5).
4. The component imbalance and duplicate-fragmentation bounds
   (4.1)--(4.3).
5. The residual occurrence identity (R), its equality cases, and the sharp
   targetwise bounds.
6. The leakage-correlation form (HG-L).
7. Exact parity cancellation (7.1)--(7.3).
8. The fair integral heat identities (7.4)--(7.5).
9. The conditional implication
   \[
   (RF_A)\Longrightarrow
   \mathcal Q_A=O_A(H_A\operatorname{Cat}_m)
   \Longrightarrow\text{fixed-window overload}
   \Longrightarrow\text{MWB}.
   \]
10. The exact Max-Cut law (9.1).
11. The cube-orientation obstruction (10.1)--(10.2).
12. The arbitrary-permutation endpoint heat and parity theorems.
13. The layered short-word join/coarsening theorem (14.1)--(14.3).
14. The equivariant word occurrence formula (15.1)--(15.3).
15. The fixed-word untouched-\(U_2\) signed-space obstruction.

### Unproved

1. **Fair leakage-alignment theorem \((RF_A)\):** a well-chosen
   transposition must make
   \[
   \sum_{q,p}\frac{
   \mathsf B_p-\mathsf M_p-\mathsf R_p}{c_q}
   \]
   positive at scale \(\mathcal Q_A/n\), up to the per-step Catalan
   residue.
2. A nonlinear load-expansion estimate for
   \(\sum\binom{|\mu(S)-\mu(\tau S)|}{2}\) at the required scale.
3. A bound suppressing the opposite-sign leakage cancellation
   \(\mathsf M_p\).
4. A bound suppressing residual concentration \(\mathsf R_p\) in the large
   components not covered by the size-two theorem.
5. The weaker positive-cut/local-minimum lemma \(LM_A\) when fair total
   correlation is nonpositive.
6. A sequential noncommutative short-word theorem with components recomputed
   after every state-dependent switch.
7. Any overload-to-labelled common-owner stability theorem.

## Conclusion

The ownership-overlay lane does contain a real positive theorem:
transposition-invariant middle ownership forces lower occurrence imbalances
to be leakage gradients, and this quantitatively separates duplicate
residuals in small components.  In particular, size-two exact components
have perfect residual fragmentation at every depth.

That is not enough for the occurrence-pair heat gap.  The exact remaining
quantity is the cross-component sign alignment of the leakage gradients.
Graph expansion, cycle rank, component number, raw fragmentation, and fixed
short words do not control it.  A successful continuation must prove either
the thresholded fair inequality \((RF_A)\), the weaker positive-cut lemma
\(LM_A\), or a genuinely sequential state-dependent routing theorem.

This is the genuine endpoint of lane AB.
