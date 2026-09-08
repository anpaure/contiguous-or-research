# Fifth-wave AB: a productive MSW packet bridge and the height--capacity obstruction

Date: 2026-07-25

Status: theorem-level mathematical report. Every item labelled **Theorem**, **Lemma**,
**Proposition**, or **Corollary** is proved below. Every remaining hypothesis is marked
explicitly. All factors and all switches are integral exact middle wreath factors.
There is no finite search, signed-factor substitution, or appeal to a literal OR word.

---

## 0. Verdict

The full adaptive fresh-release gate \(AFR_A\) is still unproved. The fifth wave does,
however, produce a genuine fixed-window special-factor case at the correct
\(H_A\operatorname{Cat}_m\) scale, together with two quantitative invariant
obstructions that explain exactly why this case does not yet extend to an arbitrary
global minimizer.

Write

\[
 n=2m+1,\qquad W=\binom{n}{m},\qquad
 B=\operatorname{Cat}_m=\frac Wn,
 \qquad H=H_A=\lceil A\sqrt m\rceil .
\]

The new conclusions are as follows.

1. **A same-bridge, Catalan-many productive exact sequence.** For every fixed
   \(A>0\), and all sufficiently large \(m\), consider the canonical MSW factor and
   its \((2\,3)\)-cell. Among the two explicit endpoints obtained by either retaining
   or switching all
   \(\operatorname{Cat}_{m-2}\) canonical size-two packets, one endpoint
   \(F^\sharp\) has a balanced-half packet child satisfying

   \[
   \mathbb E\bigl[\mathcal Q_H(F^\sharp)-\mathcal Q_H(F_{\rm child})\bigr]
   >\frac18HB.
   \tag{0.1}
   \]

   Every child in the distribution switches more than \(B/32-1\) genuine
   ownership components. The switches may be executed one at a time, with the
   ownership overlay freshly recomputed after every switch. At the initial,
   edgeless-forest stage the same transposition has subgroup-profile release

   \[
   \Delta_{(2\,3)}^Q>\frac18HB.
   \tag{0.2}
   \]

   Thus high released floor, microscopic fragmentation, and positive exact gain
   occur on one and the same bridge.

2. **An AFR-scale conditional capture inequality.** If the larger components in
   that same cell satisfy the explicit residual-restoration bound (4.29) below,
   then for every \(0<\eta\le1\),

   \[
   \mathbb E\Gamma
   >\eta\Delta_{(2\,3)}^Q-\frac17HB.
   \tag{0.3}
   \]

   This has exactly the permitted AFR error scale. The residual-restoration bound
   is not proved. Its failure is itself an exact quantitative obstruction.

3. **A canonical endpoint dichotomy.** Without choosing the better endpoint, the
   canonical MSW factor itself either admits a Catalan-many packet sequence with
   gain \(>HB/16\), or the aggregate of its larger \((2\,3)\)-components has
   adverse alignment less than \(-HB/8\) and weighted squared norm greater than
   \(7HB/480\). Hence failure of the packet move cannot be blamed on a lack of
   fragmentation: it forces a macroscopic, oppositely aligned residual.

4. **A completely numerical fixed-depth case.** At depth \(q=6\), for every
   \(m\ge89\), one of the same two explicit exact endpoints has a balanced-half
   packet sequence with expected depth-six gain

   \[
   >\frac{65}{8192}B.
   \tag{0.4}
   \]

5. **A fresh height--capacity theorem.** If \(h(F)\) is the height of an exact
   factor above the global fixed-window minimum, then every fresh bridge obeys

   \[
   \rho_\tau\ge A_\tau-4h(F),\qquad
   V_\tau\ge A_\tau-4h(F).
   \tag{0.5}
   \]

   A high exposed release at low height therefore forces a quantitative
   component-size/cyclic-distance moment and, under a component-size cap, many
   active fresh components. At a global minimizer, however,
   \(\rho_\tau=A_\tau\): all of the released floor is restored by common-sign
   component noise.

6. **The no-recycling threshold is exactly visible.** Along an arbitrary sequence
   of freshly recomputed bridges with component size at most \(L\), exposed release
   forces many component-round incidences. But with only the trivial
   \(n-1\)-round revisit bound, it forces only \(\Omega(B/n)\) distinct carrier
   owners at the natural \(WH=nBH\) scale. This exactly matches the previously
   identified \(B/n\)-sized recycled-core obstruction. Component capacity alone
   cannot prove cumulative novelty.

7. **A short-word seam invariant.** A legal preparation by a transposition
   commuting with a future bridge and stabilizing a target pair rewires only the
   target bridge's seam edges, preserves every owner target weight, and has an even
   seam budget. Deleting \(b\) seams from one Eulerian bridge component creates at
   most \(b\) pieces, while the new seams may reconnect all pieces immediately.
   Thus unsigned seam expansion cannot control the decisive common-sign
   restitution \(\rho_\tau-\pi_\tau\).

The positive theorem is a one-fresh-cell theorem. Its many microsteps all use the
same coordinate transposition. They are not distinct subgroup bridges and do not
release the same profile floor repeatedly. Selecting the better of the two explicit
MSW endpoints is existential; it is not a free preparation from a prescribed or
globally minimizing factor. These scope restrictions are essential.

---

## 1. Exact normalization

At depth \(q\), put

\[
 r_q=m-q,\qquad N_q=\binom n{r_q},\qquad
 \lambda_q=\frac W{N_q},\qquad c_q=\lfloor\lambda_q\rfloor.
\]

For an exact factor \(F\), let \(\mu_q^F(S)\) be its number of cyclic occurrences
of the \(r_q\)-set \(S\). Define the full floor energy

\[
 Q_q(F)=\sum_{S\in\binom{[n]}{r_q}}
 (\mu_q^F(S)-c_q)(\mu_q^F(S)-c_q-1)
\]

and the weighted window energy

\[
 \mathcal Q_H(F)=\sum_{q=1}^H\frac{Q_q(F)}{c_q}.
 \tag{1.1}
\]

The associated Hilbert norm is

\[
 \|x\|_H^2=\sum_{q=1}^H\frac{\|x_q\|_2^2}{c_q}.
 \tag{1.2}
\]

Fix a transposition \(\tau\) and freshly compute the connected ownership
components \(K\) of the overlay of \(F\) and \(\tau F\). If \(a_K\) is the lower
histogram contributed by the old side of \(K\), put

\[
 d_K=a_K-\tau a_K,\qquad d=\sum_Kd_K,
\]

\[
 A_\tau=\|d\|_H^2,qquad
 V_\tau=\sum_K\|d_K\|_H^2,
 \tag{1.3}
\]

\[
 \rho_\tau=min_{\varepsilon_K\in\{\pm1\}}
 \left\|\sum_K\varepsilon_Kd_K\right\|_H^2.
 \tag{1.4}
\]

For an unordered moved target pair \(p=\{S,\tau S\}\), orient \(S\) once and
write

\[
 d_{K,p}=a_{K,q}(S)-a_{K,q}(\tau S),\qquad
 z_p=\sum_Kd_{K,p},\qquad
 \delta_p=z_p\pmod2\in\{0,1\}.
\]

The exact targetwise integral remainder is

\[
 \pi_\tau=2\sum_{q,p}\frac{\delta_p}{c_q}.
 \tag{1.5}
\]

Thus

\[
 A_\tau=2\sum_{q,p}\frac{z_p^2}{c_q}.
 \tag{1.6}
\]

The elementary pair-orbit release and the best common component-sign gain are

\[
 \boxed{
 \mathcal R_\tau=\frac{A_\tau-\pi_\tau}{4},\qquad
 \Gamma_\tau^*=\frac{A_\tau-\rho_\tau}{4}.
 }
 \tag{1.7}
\]

For a particular component signing \(\varepsilon\), the exact child satisfies

\[
 \boxed{
 \mathcal Q_H(F)-\mathcal Q_H(F_\varepsilon)
 =\frac14\left(
 A_\tau-\left\|\sum_K\varepsilon_Kd_K\right\|_H^2
 \right).
 }
 \tag{1.8}
\]

The distinction between \(\pi_\tau\) and \(\rho_\tau\) is fundamental.
The former permits an independent optimal parity choice on every moved target pair.
The latter permits only one common sign per ownership component across all targets
and depths. Always

\[
 0\le\pi_\tau\le\rho_\tau\le\min\{A_\tau,V_\tau\}.
 \tag{1.9}
\]

Fresh invariance of a \(\tau\)-cell does **not** imply
\(\rho_\tau=\pi_\tau\).

---

## 2. A corrected common-sign bounded-bundle theorem

The following lemma is the cleanest exact bridge from targetwise fragmentation to
one global component signing.

For a moved target pair \(p\), put

\[
 t_p=\sum_K|d_{K,p}|,
 \qquad L_p=\max_K|d_{K,p}|,
 \qquad M_p=\frac{t_p-|z_p|}{2}.
 \tag{2.1}
\]

Thus \(t_p=|z_p|+2M_p\), and \(M_p\) is the exact opposite-target mixing count.

### Theorem 2.1 (global bounded-bundle capture)

For every exact factor and fresh transposition,

\[
 \boxed{
 \rho_\tau
 \le
 2\sum_{q,p}\frac{L_p(|z_p|+2M_p)}{c_q}.
 }
 \tag{2.2}
\]

Consequently

\[
 \boxed{
 \Gamma_\tau^*
 \ge
 \frac12\sum_{q,p}
 \frac{z_p^2-L_p(|z_p|+2M_p)}{c_q}.
 }
 \tag{2.3}
\]

Equivalently,

\[
 \boxed{
 \mathcal R_\tau-\Gamma_\tau^*
 \le
 \frac12\sum_{q,p}
 \frac{L_p(|z_p|+2M_p)-\delta_p}{c_q}.
 }
 \tag{2.4}
\]

#### Proof

Give every freshly computed component an independent uniform sign. One common
random signing has

\[
 \mathbb E\left\|\sum_K\varepsilon_Kd_K\right\|_H^2
 =\sum_K\|d_K\|_H^2
 =2\sum_{q,p,K}\frac{d_{K,p}^2}{c_q}.
\]

For each \(p\),

\[
 \sum_Kd_{K,p}^2
 \le L_p\sum_K|d_{K,p}|=L_pt_p.
\]

The minimum common-sign norm is no larger than this expectation, proving (2.2).
Substitute (1.6) into (1.7) to get (2.3). Subtract (2.3) from the exact release
formula in (1.7) to obtain (2.4). \(\square\)

### Corollary 2.2 (same-sign nondominance)

Suppose that

\[
 M_p=0
 \quad\text{on every moved pair},
 \qquad
 L_p\le(1-\eta)|z_p|
 \quad\text{whenever }z_p^2>\delta_p
 \tag{2.5}
\]

for some \(0<\eta\le1\). Then

\[
 \boxed{\Gamma_\tau^*\ge\eta\mathcal R_\tau.}
 \tag{2.6}
\]

In particular, same-sign bundles of size at most \(|z_p|/2\) give

\[
 \Gamma_\tau^*\ge\frac12\mathcal R_\tau.
 \tag{2.7}
\]

#### Proof

On a release-carrying pair, (2.5) makes the corresponding summand on the right of
(2.3) at least \(\eta z_p^2/(2c_q)\). On a zero-release pair,
\(|z_p|\in\{0,1\}\). Because \(M_p=0\), the case \(z_p=0\) has every
\(d_{K,p}=0\), while the case \(|z_p|=1\) has \(L_p=1\); its summand in (2.3)
is therefore zero. Meanwhile

\[
 \mathcal R_\tau
 =\frac12\sum_{q,p:\,z_p^2>\delta_p}
 \frac{z_p^2-\delta_p}{c_q}
 \le\frac12\sum_{q,p:\,z_p^2>\delta_p}
 \frac{z_p^2}{c_q}.
\]

This proves (2.6). \(\square\)

If one target in a pair has load \(c_q\) and its mate has load \(c_q+z\), where
\(z\ge0\), then
the latter contributes the exact local floor token \(z(z-1)\). A sign-coherent
unit fragmentation contributes \((z^2-z)/(2c_q)\) to the weighted global lower
bound (2.3), or \((z^2-z)/2\) to the unweighted depth-\(q\) bound,
namely one half of that token. This is a **contribution to one common-sign global
bound**. It is not a separately optimizable pairwise child: other target pairs may
contribute negatively unless the hypotheses of Corollary 2.2 hold globally.

---

## 3. Commuting preparations: an exact seam invariant

The next theorem gives a rigorous short-word analysis. Its role is primarily
obstructive: it quantifies the number of seams needed to create fragmentation but
also identifies the fresh reconnection datum that seam counting misses.

Let \(\mathcal X=\binom{[n]}m\) be the middle layer. For an exact factor \(F\),
let \(o_F:\mathcal X\to F\) be its owner map. For a transposition \(\tau\), let
\(\Gamma_\tau(F)\) be the loopless owner-orbit multigraph with one edge for every
moved root orbit \(\{X,\tau X\}\) whose two owners are distinct, joining
\(o_F(X)\) to \(o_F(\tau X)\). Owner-self orbits are suppressed.

Fix a moved lower target pair

\[
 p=\{S,T\},\qquad T=\tau S\ne S,
\]

and define the owner atom

\[
 a_C(p)=
 \mathbf1_{\{S\text{ is a cyclic interval of }C\}}
 -\mathbf1_{\{T\text{ is a cyclic interval of }C\}}
 \in\{-1,0,1\}.
 \tag{3.1}
\]

### Theorem 3.1 (commuting target-stabilizer splice)

Let \(\sigma\) be a coordinate transposition satisfying

\[
 \sigma\tau=\tau\sigma,
 \qquad \sigma S=S,
 \qquad \sigma T=T.
 \tag{3.2}
\]

At the current exact factor \(F\), choose a union \(I\) of connected components of
the \(\sigma\)-overlay and perform the legal component-side switch. Let

\[
 U=\bigsqcup_{C\in I}\mathcal W_m(C)\subseteq\mathcal X
\]

be its \(\sigma\)-invariant middle-root support, and identify the new row
\(\sigma C\) with \(C\) on \(I\). Then the freshly recomputed \(\tau\)-owner graph
is obtained from the old one by performing exactly

\[
 \boxed{
 b_\tau(U)=\frac12|U\triangle\tau U|
 =|\delta_{\Gamma_\tau(F)}(I)|
 }
 \tag{3.3}
\]

crossing-orbit deletion/reinsertion operations, including multiplicity. A
reinserted edge may have the same endpoint pair as the deleted edge, so
\(b_\tau(U)\) is a replacement budget rather than necessarily the size of the
final graph symmetric difference. All owner atoms are unchanged:

\[
 \boxed{a_{\sigma C}(p)=a_C(p).}
 \tag{3.4}
\]

In particular, the two target loads and their exposed difference are unchanged.

#### Proof

A \(\tau\)-orbit wholly outside \(U\) has the same two owners. A \(\tau\)-orbit
wholly inside \(U\) becomes the \(\sigma\)-image of an old \(\tau\)-orbit; because
\(\sigma\tau=\tau\sigma\), the canonical row identification gives precisely the
corresponding old owner edge. Only a \(\tau\)-orbit crossing \(U\) is rewired.
Every crossing orbit contributes its two roots to \(U\triangle\tau U\), proving
(3.3).

For (3.4), the occurrence of \(S\) in \(\sigma C\) equals the occurrence of
\(\sigma^{-1}S=S\) in \(C\), and likewise for \(T\). \(\square\)

Every owner vertex of \(\Gamma_\tau(F)\) has even degree

\[
 2\min\{d_C,m-1\},
 \tag{3.5}
\]

where \(d_C\) is the shorter cyclic distance between the two letters of \(\tau\)
in row \(C\). Hence every cut has even size.

### Corollary 3.2 (quantized fragmentation and immediate collapse)

In Theorem 3.1, either \(b_\tau(U)=0\), in which case the weighted
\(\tau\)-overlay is only relabelled and no new fragmentation occurs, or

\[
 \boxed{b_\tau(U)\ge2.}
 \tag{3.6}
\]

If \(b_K>0\) deleted seam edges lie in one old connected \(\tau\)-component
\(K\), deletion creates at most \(b_K\) pieces. After deleting all seams in the
whole old graph, let the new seam edges induce a multigraph on all resulting
deletion pieces, including unchanged old components. The fresh
\(\tau\)-components are exactly the connected components of this global
seam-incidence multigraph.

#### Proof

Evenness gives (3.6). Delete the \(b_K\) old seam edges. Every resulting proper
piece has positive even boundary in the old Eulerian component. If there are
\(s\) pieces, the sum of their old boundaries is \(2b_K\), so \(2s\le2b_K\).
Adding the new seam edges can only join deletion pieces. Their global incidence
graph records exactly which joins occur, including joins from a piece of \(K\) to
a different old component. \(\square\)

For a sequence of such preparations with seam budgets \(b_1,\ldots,b_t\), put
\(B_{\rm seam}=\sum_i b_i\). Repeated edge deletion and insertion gives the safe
lineage bounds

\[
 \boxed{
 \text{one initial component has at most }1+B_{\rm seam}
 \text{ final descendant pieces},
 }
 \tag{3.7}
\]

\[
 \boxed{
 \text{one final component contains owners from at most }1+B_{\rm seam}
 \text{ initial components}.
 }
 \tag{3.8}
\]

Indeed, deleting \(b_i\) edges increases component count by at most \(b_i\), and
inserting \(b_i\) edges merges at most \(b_i\) previously unrelated ancestry
classes.

Thus a single commuting preparation that splits one connected block of \(z\)
same-sign unit packets into \(k\) packet-bearing pieces needs \(b\ge k\). A
multi-preparation sequence needs at least \(B_{\rm seam}\ge k-1\). Yet the new
seam-incidence graph may reconnect every one of those pieces immediately. At the
sparsest nonzero floor token \(z=2\), the smallest nontrivial seam budget is already
two, large enough both to split and to reconnect the entire token. Seam size and
Eulerian expansion therefore do not control \(\rho_\tau-\pi_\tau\).

The theorem is deliberately narrow: every preparation must commute with the future
bridge and stabilize the target pair. Simultaneous use on many targets requires
stabilizing that whole target family.

---

## 4. A full-window productive bridge in the canonical MSW cell

### 4.1 The exact packet pile

Let \(F^{\rm MSW}_m\) be the canonical MSW factor and fix

\[
 \tau=(2\,3).
\]

The exact MSW component hierarchy supplies the genuine size-two components

\[
 J=
 \bigl\{
 \{1100R,1010R\}:R\in\mathcal D_{m-2}
 \bigr\},
 \qquad
 k:=|J|=C_{m-2},
 \tag{4.1}
\]

where \(C_j=\operatorname{Cat}_j\). These packets are pairwise owner-disjoint and
independently switchable.

Let \(d_R\) be the full fixed-window effect of packet \(R\), and set

\[
 D=\sum_{R\in\mathcal D_{m-2}}d_R,
 \qquad
 E=\sum_{K\notin J}d_K,
 \tag{4.2}
\]

\[
 V=\sum_{R\in\mathcal D_{m-2}}\|d_R\|_H^2,
 \qquad
 \Lambda=\|D\|_H^2-V.
 \tag{4.3}
\]

The audited four-arm formula gives

\[
 \|d_{R,1}\|_2^2=4,
 \qquad
 \|d_{R,q}\|_2^2=8
 \quad(2\le q\le H\le m-2).
\]

Therefore the exact packet variance is

\[
 \boxed{
 V=C_{m-2}\left(
 \frac4{c_1}+8\sum_{q=2}^H\frac1{c_q}
 \right)
 \le(8H-4)C_{m-2}.
 }
 \tag{4.4}
\]

The inequality in (4.4), not equality with \((8H-4)C_{m-2}\), is the correct
statement when some \(c_q>1\).

### Lemma 4.1 (one-depth Catalan pile)

Put \(M=m-2\). For every \(1\le q\le M\),

\[
 \boxed{
 \|D_q\|_2^2
 \ge2C_{M-q}C_q^2.
 }
 \tag{4.5}
\]

#### Proof

Use the exact four-arm depth formula for the packet indexed by \(R\in\mathcal D_M\).
Restrict to the Catalan subfamily

\[
 R=UV,qquad U\in\mathcal D_q,quad V\in\mathcal D_{M-q}.
\]

For fixed \(V\), all \(C_q\) choices of \(U\) contribute the same positive
\(\mathsf E\)-suffix dipole. Its core contains the distinguished coordinate
\(n\). None of the three other arms with the opposite sign contains \(n\), so this
coefficient cannot cancel. Distinct \(V\)'s give distinct cores. Thus there are
\(C_{M-q}\) disjoint dipoles, each with coefficient \(C_q\) and squared norm
\(2C_q^2\). Discarding all other coordinates proves (4.5). \(\square\)

### 4.2 Uniform coherence at Gaussian height

Fix \(A>0\), put \(H=\lceil A\sqrt m\rceil\), and define

\[
 L_A=\exp\bigl(2(A+1)(A+2)\bigr).
 \tag{4.6}
\]

Choose \(m_A\) so that, for every \(m\ge m_A\),

\[
 H\le\frac m2,qquad H\le m-2,qquad m\ge23,
 \qquad 4^H\ge288L_AH^5.
 \tag{4.7}
\]

Such an \(m_A\) exists because \(H\to\infty\) and an exponential dominates a
fixed polynomial.

### Lemma 4.2 (macroscopic packet coherence)

For every fixed \(A>0\) and every \(m\ge m_A\),

\[
 \boxed{\Lambda>\frac12HB.}
 \tag{4.8}
\]

Moreover,

\[
 \boxed{k>\frac1{16}B,\qquad V<\frac47HB.}
 \tag{4.9}
\]

#### Proof

First,

\[
 \lambda_H=\frac W{N_H}
 =\prod_{j=0}^{H-1}
 \frac{m+2+j}{m-j}
 =\prod_{j=0}^{H-1}
 \left(1+\frac{2+2j}{m-j}\right).
\]

Using \(1+x\le e^x\),

\[
 \lambda_H
 \le
 \exp\left(\frac{H(H+1)}{m-H+1}\right)
 \le
 \exp\left(\frac{2H(H+1)}m\right)
 \le L_A.
 \tag{4.10}
\]

Hence \(c_H\le L_A\).

The central binomial coefficient is the largest of the \(2H+1\) coefficients in
\((1+1)^{2H}\). Therefore, for \(H\ge2\),

\[
 C_H=\frac1{H+1}\binom{2H}{H}
 \ge\frac{4^H}{(H+1)(2H+1)}
 \ge\frac{4^H}{4H^2}.
 \tag{4.11}
\]

Every successive Catalan ratio is strictly less than four, so

\[
 C_{m-H-2}>\frac{C_m}{4^{H+2}}=\frac B{4^{H+2}}.
 \tag{4.12}
\]

Apply Lemma 4.1 at \(q=H\):

\[
 \|D\|_H^2
 \ge\frac{\|D_H\|_2^2}{c_H}
 \ge\frac{2C_{m-H-2}C_H^2}{c_H}
 >\frac{B4^H}{128L_AH^4}
 \ge\frac94HB.
 \tag{4.13}
\]

Next,

\[
 \frac{k}{B}
 =\frac{C_{m-2}}{C_m}
 =\frac{m(m+1)}{4(2m-1)(2m-3)}.
 \tag{4.14}
\]

For \(m\ge3\), this is at most \(7/32\), since the equivalent inequality

\[
 20m^2-64m+21\ge0
\]

holds at \(m=3\) and is increasing thereafter. Equations (4.4) and (4.13) give

\[
 \Lambda=\|D\|_H^2-V
 >\frac94HB-8H\frac7{32}B
 =\frac12HB,
\]

which proves (4.8).

The strict lower bound \(k>B/16\) follows directly from (4.14). For \(m\ge23\),

\[
 \frac{B}{k}
 =\frac{4(2m-1)(2m-3)}{m(m+1)}\ge14,
 \tag{4.15}
\]

because this is equivalent to \(m^2-23m+6\ge0\). Hence

\[
 V<(8H)k\le\frac47HB.
\]

This proves (4.9). \(\square\)

### 4.3 Balanced-half signs

The next elementary calculation is the exact source of Catalan-many
fragmentation.

Define

\[
 \kappa=
 \begin{cases}
 k-1,&k\text{ even},\\
 k,&k\text{ odd}.
 \end{cases}
 \tag{4.16}
\]

If \(k\) is even, choose a sign vector uniformly among those having \(k/2\) plus
and \(k/2\) minus signs. If \(k\) is odd, append one zero dummy vector and balance
the \(k+1\) signs. In both cases, for the real packet indices,

\[
 \mathbb E\varepsilon_i=0,
 \qquad
 \mathbb E(\varepsilon_i\varepsilon_j)=-\frac1\kappa
 \quad(i\ne j).
 \tag{4.17}
\]

Consequently,

\[
 \boxed{
 \mathbb E\left\|\sum_{i=1}^k\varepsilon_i d_i\right\|_H^2
 =V-\frac\Lambda\kappa.
 }
 \tag{4.18}
\]

Indeed, expand the square and use

\[
 \Lambda=2\sum_{i<j}\langle d_i,d_j\rangle_H.
\]

The quantity in (4.18) is automatically nonnegative. Every outcome switches
exactly \(k/2\) packets if \(k\) is even and either \((k-1)/2\) or \((k+1)/2\)
if \(k\) is odd. The dummy vector creates no fictitious switch.

### Theorem 4.3 (one fresh productive bridge with Catalan-many exact microsteps)

For every fixed \(A>0\) and every \(m\ge m_A\), one of the two explicit exact
factors

\[
 F_m^{\rm MSW},qquad (F_m^{\rm MSW})^J
 \tag{4.19}
\]

has the following property. Declare that factor \(F^\sharp\) to be the initial
factor at the edgeless-forest stage, and take \(\tau=(2\,3)\) as the first bridge.
There is a distribution on exact children such that

\[
 \boxed{
 \mathbb E\bigl[
 \mathcal Q_H(F^\sharp)-\mathcal Q_H(F_{\rm child})
 \bigr]
 >\frac18HB.
 }
 \tag{4.20}
\]

Every child in the distribution is reachable by sequentially switching more than

\[
 \boxed{\frac{B}{32}-1}
 \tag{4.21}
\]

genuine size-two ownership components, freshly recomputed after every switch.
The initial subgroup-profile release of the same bridge satisfies

\[
 \boxed{\Delta_\tau^Q>\frac18HB.}
 \tag{4.22}
\]

In particular, some deterministic balanced-half child has the gain in (4.20).

#### Proof

At the two endpoints (4.19), the total anti-invariant vectors are

\[
 E+D,qquad E-D.
\]

Choose the endpoint with larger \(\mathcal Q_H\). Reorient all packet vectors
simultaneously so that its packet aggregate is \(D^\sharp=\pm D\). Then

\[
 \langle D^\sharp,E\rangle_H=|\langle D,E\rangle_H|.
 \tag{4.23}
\]

Only this simultaneous orientation is used; the packet vectors are not
independently reoriented.

Apply the balanced distribution of Section 4.3. Its expected child residual norm is

\[
 \|E\|_H^2+V-\frac\Lambda\kappa.
\]

The initial residual norm is \(\|E+D^\sharp\|_H^2\). By the exact cell identity
(1.8), the expected gain is

\[
 \begin{aligned}
 G^\sharp
 &=\frac14\left(
 \|E+D^\sharp\|_H^2
 -\|E\|_H^2-V+\frac\Lambda\kappa
 \right)\\
 &=\frac{\Lambda+2|\langle D,E\rangle_H|+\Lambda/\kappa}{4}
 >\frac18HB,
 \end{aligned}
 \tag{4.24}
\]

using Lemma 4.2.

Every balanced outcome switches \(\lfloor k/2\rfloor\) or
\(\lceil k/2\rceil\) packets. Since \(k>B/16\), this exceeds \(B/32-1\).
The packets are pairwise owner-disjoint and have disjoint, \(\tau\)-invariant
middle-root supports. Switching any processed packet leaves every unprocessed
packet exactly a component of the freshly recomputed \(\tau\)-overlay. Hence each
balanced child has the claimed sequential exact realization.

At the first, edgeless-forest bridge, the subgroup orbit-profile release equals the
elementary integer pair release:

\[
 \Delta_\tau^Q=\mathcal R_\tau.
 \tag{4.25}
\]

Every exact child captures at most this targetwise integral optimum. Thus
\(\Delta_\tau^Q\ge G^\sharp>HB/8\). Averaging also implies the existence of one
deterministic child attaining at least (4.20). \(\square\)

The microsteps in Theorem 4.3 all lie inside the one intrinsic \(\tau\)-cell.
After the first bridge has been added to the coordinate subgroup, further uses of
the same \(\tau\) do not create fresh subgroup releases. The theorem is therefore
not a disguised repetition of a release identity. “Productive sequence” refers to
the positive net gain of the final child; individual packet microsteps are not
claimed to be downhill.

### 4.4 Exact restitution and the remaining MSW obstruction

Let

\[
 A^\sharp=\|E+D^\sharp\|_H^2,
\]

and let \(\pi_{\tau,H}\) be the targetwise integer remainder for this initial
factor. Put

\[
 \overline S
 =\|E\|_H^2+V-\frac\Lambda\kappa.
 \tag{4.26}
\]

Every balanced child is an integral signing with the same target-pair totals, so
its residual squared norm is at least \(\pi_{\tau,H}\). Averaging gives

\[
 \overline S-\pi_{\tau,H}\ge0.
 \tag{4.27}
\]

Equations (4.24)--(4.25) give the exact identity

\[
 \boxed{
 G^\sharp
 =\Delta_\tau^Q
 -\frac{
 \|E\|_H^2+V-\Lambda/\kappa-\pi_{\tau,H}
 }4.
 }
 \tag{4.28}
\]

Thus the packet construction has reduced the same-bridge problem to one explicit
residual aggregate.

### Corollary 4.4 (AFR-scale capture under residual control)

Let \(0<\eta\le1\). If

\[
 \boxed{
 \|E\|_H^2-\pi_{\tau,H}
 \le4(1-\eta)\Delta_\tau^Q,
 }
 \tag{4.29}
\]

then

\[
 \boxed{
 G^\sharp
 >\eta\Delta_\tau^Q-\frac17HB.
 }
 \tag{4.30}
\]

#### Proof

Substitute (4.29) into (4.28):

\[
 G^\sharp
 \ge
 \eta\Delta_\tau^Q
 -\frac{V-\Lambda/\kappa}{4}
 \ge
 \eta\Delta_\tau^Q-\frac V4.
\]

Use \(V<4HB/7\) from Lemma 4.2. \(\square\)

Condition (4.29) is **unproved**. Its failure is the exact alternative

\[
 \|E\|_H^2-\pi_{\tau,H}
 >4(1-\eta)\Delta_\tau^Q.
 \tag{4.31}
\]

Thus this special factor cannot fail by hiding the release on a different bridge or
by lacking microscopic packets. It can fail only because the aggregate of the
larger components restores a macroscopic share of the released floor.

### 4.5 The canonical endpoint: descent or adverse alignment

Return to the canonical endpoint itself and put

\[
 a=\langle D,E\rangle_H.
\]

Its balanced-half expected gain is

\[
 G_0=\frac{\Lambda+2a+\Lambda/\kappa}{4}.
 \tag{4.32}
\]

### Corollary 4.5 (canonical productive-or-collapse dichotomy)

For every fixed \(A>0\) and every \(m\ge m_A\), at least one of the following
holds:

1. the canonical MSW factor has a balanced-half, freshly recomputed packet sequence
   with

   \[
   \boxed{G_0>\frac1{16}HB;}
   \tag{4.33}
   \]

2. the larger-component aggregate satisfies

   \[
   \boxed{
   \langle D,E\rangle_H<-\frac\Lambda4<-\frac18HB,
   }
   \tag{4.34}
   \]

   and

   \[
   \boxed{\|E\|_H^2>\frac7{480}HB.}
   \tag{4.35}
   \]

#### Proof

If \(a\ge-\Lambda/4\), then (4.32) gives

\[
 G_0>\frac\Lambda8>\frac1{16}HB.
\]

Otherwise (4.34) holds. Cauchy--Schwarz and
\(\|D\|_H^2=\Lambda+V\) give

\[
 \|E\|_H^2
 >\frac{\Lambda^2}{16(\Lambda+V)}.
\]

The right side is increasing in \(\Lambda\) and decreasing in \(V\). Using
\(\Lambda>HB/2\) and \(V<4HB/7\),

\[
 \frac{\Lambda^2}{16(\Lambda+V)}
 >
 \frac{(HB/2)^2}{16(HB/2+4HB/7)}
 =\frac7{480}HB.
\]

This proves (4.35). \(\square\)

There is a stronger lock for a prescribed coherent endpoint.

### Proposition 4.6 (packet-local stability forces macroscopic cancellation)

Suppose the canonical endpoint has no decreasing child obtained by switching any
subset of \(J\). Then

\[
 \boxed{\langle D,E\rangle_H\le-\Lambda<-\frac12HB,}
 \tag{4.36}
\]

\[
 \boxed{\|E\|_H^2>\frac7{30}HB,}
 \tag{4.37}
\]

and

\[
 \boxed{
 \|E\|_H^2-\pi_{\tau,H}
 \ge4\Delta_\tau^Q-V
 >4\Delta_\tau^Q-\frac47HB.
 }
 \tag{4.38}
\]

#### Proof

Select every packet independently with probability \(p\). The exact expected gain
is

\[
 p\bigl((1-p)\Lambda+a\bigr).
\]

It is nonpositive for every \(p>0\) by the stability hypothesis. Divide by \(p\)
and let \(p\downarrow0\) to get \(a\le-\Lambda\), proving (4.36).

Cauchy gives

\[
 \|E\|_H^2\ge\frac{a^2}{\Lambda+V}
 \ge\frac{\Lambda^2}{\Lambda+V}
 >\frac7{30}HB,
\]

using the same extremal substitution as in Corollary 4.5 but without the factor
\(16\). Finally,

\[
 4\Delta_\tau^Q-V
 =\|E+D\|_H^2-\pi_{\tau,H}-V
 =\|E\|_H^2-\pi_{\tau,H}+\Lambda+2a.
\]

Since \(a\le-\Lambda\), the last two terms are nonpositive. Rearrangement and
\(V<4HB/7\) prove (4.38). \(\square\)

### 4.6 A numerical depth-six theorem

The Gaussian-height argument has a fixed-depth numerical shadow with no asymptotic
constant hidden in \(A\).

### Theorem 4.7 (depth-six special-factor case)

For every \(m\ge89\), one of the two exact endpoints (4.19) has a balanced-half,
freshly recomputed packet sequence whose expected depth-six gain is

\[
 \boxed{G_6>\frac{65}{8192}B.}
 \tag{4.39}
\]

#### Proof

At \(q=6\),

\[
 \lambda_6
 =\prod_{j=0}^5
 \left(1+\frac{2+2j}{m-j}\right)
 \le
 \exp\left(\frac{42}{m-5}\right)
 \le e^{1/2}<2.
\]

Since \(\lambda_6>1\), this gives \(c_6=1\). Also \(C_6=132\). Lemma 4.1 and
the exact packet variance at depth six give

\[
 \Lambda_6
 \ge2C_{m-8}C_6^2-8C_{m-2}
 =34848C_{m-8}-8C_{m-2}.
\]

Successive Catalan ratios are less than four, so

\[
 C_{m-2}<4^6C_{m-8},
 \qquad B=C_m<4^8C_{m-8}.
\]

Therefore

\[
 \Lambda_6>2080C_{m-8}>\frac{65}{2048}B.
\]

The higher-endpoint balanced-sign calculation gives

\[
 G_6>\frac{\Lambda_6}{4}>\frac{65}{8192}B.
\]

Fresh sequential realizability is the same as in Theorem 4.3. \(\square\)

---

## 5. The universal height--capacity obstruction

The positive MSW theorem begins at a specially chosen high endpoint. The next
result explains what changes at a prescribed factor close to a global minimum.

Let

\[
 \mathcal Q_H^{\min}
 =\min\{\mathcal Q_H(F'):F'\text{ is an exact factor}\},
\]

and define the exact height

\[
 h(F)=\mathcal Q_H(F)-\mathcal Q_H^{\min}\ge0.
 \tag{5.1}
\]

### Theorem 5.1 (fresh height lock)

For every exact factor \(F\) and every freshly computed transposition cell,

\[
 \boxed{
 \rho_\tau\ge A_\tau-4h(F),
 \qquad
 V_\tau\ge A_\tau-4h(F).
 }
 \tag{5.2}
\]

Equivalently,

\[
 \boxed{
 \frac{\rho_\tau-\pi_\tau}{4}
 =\mathcal R_\tau-\Gamma_\tau^*
 \ge\mathcal R_\tau-h(F).
 }
 \tag{5.3}
\]

At a global minimizer,

\[
 \boxed{\rho_\tau=A_\tau,\qquad \Gamma_\tau^*=0}
 \tag{5.4}
\]

for every \(\tau\), and every component signing has residual norm at least
\(A_\tau\).

#### Proof

No exact child can lie more than \(h(F)\) below \(F\). Hence

\[
 \Gamma_\tau^*=\frac{A_\tau-\rho_\tau}{4}\le h(F),
\]

which proves the first inequality in (5.2). A uniform random component signing has
expected residual norm \(V_\tau\), so \(\rho_\tau\le V_\tau\), proving the second.
Equation (5.3) is (1.7).

At a minimizer, \(h(F)=0\), so \(\rho_\tau\ge A_\tau\). The all-old signing has
residual norm \(A_\tau\), giving equality. \(\square\)

Thus an \(\eta\)-productive bridge at height \(h\) necessarily satisfies

\[
 h\ge\eta\Delta_\tau^Q.
 \tag{5.5}
\]

Any adaptive proof beginning at a global minimizer must therefore account explicitly
for the height created by its preparatory moves. Fragmentation alone cannot make a
fresh bridge descend below the exact minimum.

### 5.1 Exact cyclic-distance capacity

Put

\[
 S_H=\sum_{q=1}^H\frac1{c_q},
 \tag{5.6}
\]

and assume \(H\le m-2\), so every controlled rank \(r_q=m-q\) is at least two.

For one cyclic row \(C\), let \(w_{C,r}\) be the indicator vector of its cyclic
\(r\)-intervals. If the letters of \(\tau\) have shorter cyclic distance
\(d\in\{1,\ldots,m\}\) in \(C\), define

\[
 \ell_r(d)=4\min(r,d)-4\mathbf1_{\{d=r\}}.
 \tag{5.7}
\]

### Lemma 5.2 (exact row displacement)

For \(2\le r\le m\),

\[
 \boxed{
 \|\tau w_{C,r}-w_{C,r}\|_1
 =\|\tau w_{C,r}-w_{C,r}\|_2^2
 =\ell_r(d).
 }
 \tag{5.8}
\]

In particular,

\[
 \boxed{\ell_r(d)\le4(m-1)=2(n-3).}
 \tag{5.9}
\]

#### Proof

There are \(\min(r,d)\) cyclic \(r\)-intervals containing the first transposed
letter but not the second, and the same number with the roles reversed. If
\(d\ne r\), none of these \(2\min(r,d)\) intervals is carried by \(\tau\) to
another old interval. They are lost and the same number are gained, giving
\(4\min(r,d)\) entries in the symmetric difference.

If \(d=r\), exactly two of those old intervals are exchanged with one another and
remain in the interval family. Removing their two lost and two gained counts
subtracts four. Since the difference vector has entries in \(\{-1,0,1\}\), its
\(\ell_1\)-norm equals its squared \(\ell_2\)-norm.

The only way \(\min(r,d)=m\) is \(r=d=m\), when the subtraction in (5.7) applies.
This proves (5.9). \(\square\)

Let \(K\) be a fresh \(\tau\)-component with \(s=|K|\) old-side owners. The exact
two-sided containment-leakage identity gives, at depth \(q\),

\[
 \|d_{K,q}\|_\infty
 \le b_q(s):=\left\lfloor\frac{qs}{q+1}\right\rfloor.
 \tag{5.10}
\]

For completeness, this follows by counting, on the two sides of the component, the
same middle roots containing a fixed \((m-q)\)-target. A genuine lower interval is
contained in exactly \(q+1\) middle intervals; every nongenuine occurrence contributes
between zero and \(q\). Their difference is \((q+1)d_{K,q}\), giving (5.10).

### Lemma 5.3 (component size--distance capacity)

For every fresh component \(K\),

\[
 \boxed{
 \|d_{K,q}\|_2^2
 \le
 b_q(|K|)
 \sum_{C\in K}\ell_{m-q}(d_C).
 }
 \tag{5.11}
\]

#### Proof

The component effect is the sum of the row differences
\(w_{C,m-q}-\tau w_{C,m-q}\). Therefore Lemma 5.2 and the triangle inequality give

\[
 \|d_{K,q}\|_1
 \le\sum_{C\in K}\ell_{m-q}(d_C).
\]

Now use

\[
 \|d_{K,q}\|_2^2
 \le\|d_{K,q}\|_\infty\|d_{K,q}\|_1
\]

and (5.10). \(\square\)

Define the exact fresh capacity

\[
 \mathsf{Cap}_H(F,\tau)
 =\sum_{q,K}\frac{b_q(|K|)}{c_q}
 \sum_{C\in K}\ell_{m-q}(d_C).
 \tag{5.12}
\]

### Theorem 5.4 (release forces owner--distance capacity)

For every exact factor and fresh bridge,

\[
 \boxed{
 \mathsf{Cap}_H(F,\tau)
 \ge V_\tau
 \ge A_\tau-4h(F)
 \ge4\bigl(\mathcal R_\tau-h(F)\bigr).
 }
 \tag{5.13}
\]

#### Proof

Sum Lemma 5.3 over components and depths to get
\(\mathsf{Cap}_H\ge V_\tau\). Apply Theorem 5.1. Finally,
\(A_\tau=4\mathcal R_\tau+\pi_\tau\ge4\mathcal R_\tau\). \(\square\)

### 5.2 Quantitative fresh fragmentation under a size cap

Call a fresh component active if its effect is nonzero somewhere in the controlled
window. Let \(Z_\tau\) be the total number of owners in active components and let
\(k_\tau\) be the number of active components.

### Corollary 5.5 (active owner and component lower bounds)

Suppose every active component has at most \(L\) owners, where \(L\ge2\). Then

\[
 \boxed{
 Z_\tau
 \ge
 \frac{2(\mathcal R_\tau-h(F))_+}
 {(n-3)(L-1)S_H},
 }
 \tag{5.14}
\]

\[
 \boxed{
 k_\tau
 \ge
 \frac{2(\mathcal R_\tau-h(F))_+}
 {(n-3)L(L-1)S_H}.
 }
 \tag{5.15}
\]

If the same bridge satisfies the exposure estimate

\[
 \mathcal R_\tau\ge\alpha\Delta_\tau^Q-\xi,
 \tag{5.16}
\]

then the numerators in (5.14)--(5.15) may be replaced by

\[
 2(\alpha\Delta_\tau^Q-\xi-h(F))_+.
 \tag{5.17}
\]

#### Proof

For \(s\le L\), (5.9) and
\(b_q(s)\le s-1\) give

\[
 V_\tau
 \le2(n-3)S_H\sum_{K\text{ active}}s_K(s_K-1).
\]

Hence

\[
 V_\tau\le2(n-3)(L-1)S_HZ_\tau
\]

and

\[
 V_\tau\le2(n-3)L(L-1)S_Hk_\tau.
\]

Combine these inequalities with
\(V_\tau\ge4(\mathcal R_\tau-h(F))\) from Theorem 5.4. Exposure (5.16) gives
(5.17). \(\square\)

This is a genuine fragmentation theorem: at low height, a same-bridge exposed
release either produces a component larger than \(L\) or is spread across the
quantified number of freshly recomputed active components. It does not assert that
their signs are favourable. At a global minimizer, Theorem 5.1 says the best common
signing still captures zero.

### 5.3 Multistep incidence and the exact no-recycling threshold

Consider any finite exact sequence in which a bridge \(\tau_t\) is chosen at the
current factor \(F_{t-1}\) and its components are freshly recomputed. Put

\[
 h_{t-1}=h(F_{t-1}),
 \qquad \mathcal R_t=\mathcal R_{\tau_t}(F_{t-1}),
\]

and let \(Z_t,k_t\) be its active owner mass and active component count.

### Theorem 5.6 (multistep capacity ledger)

If every active fresh component at every round has size at most \(L\), then

\[
 \boxed{
 \sum_t Z_t
 \ge
 \frac{2\left(\sum_t\mathcal R_t-\sum_t h_{t-1}\right)_+}
 {(n-3)(L-1)S_H},
 }
 \tag{5.18}
\]

\[
 \boxed{
 \sum_t k_t
 \ge
 \frac{2\left(\sum_t\mathcal R_t-\sum_t h_{t-1}\right)_+}
 {(n-3)L(L-1)S_H}.
 }
 \tag{5.19}
\]

If every round has exposure

\[
 \mathcal R_t\ge\alpha\Delta_t^Q-\xi_t,
 \tag{5.20}
\]

then the common numerator may be replaced by

\[
 2\left(
 \alpha\sum_t\Delta_t^Q
 -\sum_t\xi_t
 -\sum_t h_{t-1}
 \right)_+.
 \tag{5.21}
\]

#### Proof

Apply the two upper bounds on \(V_{\tau_t}\) from the proof of Corollary 5.5 at
each freshly recomputed round. Theorem 5.4 gives

\[
 4(\mathcal R_t-h_{t-1})\le V_{\tau_t}.
\]

Sum and rearrange. Then insert (5.20). \(\square\)

The theorem tracks current owner identities only; it assumes no persistence of
component partitions.

Now suppose \(T\le n-1\) rounds are used and every active component throughout the
sequence is supported on one recycled owner carrier \(Z\) of size \(s\). Then the
proof above gives, round by round,

\[
 \mathcal R_t
 \le h_{t-1}
 +\frac{n-3}{2}(L-1)S_Hs.
\]

Hence

\[
 \boxed{
 \sum_t\mathcal R_t
 \le
 \sum_t h_{t-1}
 +\frac{T(n-3)}2(L-1)S_Hs.
 }
 \tag{5.22}
\]

Suppose now that \(\Delta_t^Q\) denotes the current subgroup-profile release along a
fresh coordinate-forest sequence, and invoke the previously audited identity
\(\sum_t\Delta_t^Q=\mathcal Q_H(F_0)\). If \(T\le n-1\), all exposures (5.20)
hold, and all active components throughout the sequence lie in the same fixed
cross-round carrier \(Z\), then

\[
 \boxed{
 s\ge
 \frac{
 2\left(
 \alpha\mathcal Q_H(F_0)
 -\sum_t\xi_t
 -\sum_t h_{t-1}
 \right)_+
 }
 {(n-1)(n-3)(L-1)S_H}.
 }
 \tag{5.23}
\]

At the natural scale

\[
 \mathcal Q_H(F_0)\asymp WH=nBH,
 \qquad S_H\le H,
\]

and with fixed \(L,\alpha\) and a positive constant margin after subtracting the
total exposure error and height area, (5.23) gives

\[
 s=\Omega(B/n).
 \tag{5.24}
\]

For the fixed Gaussian window, (4.10) applies to every \(q\le H\), so
\(H/L_A\le S_H\le H\). Thus the lower bound furnished by this capacity ledger is
of order \(B/n\), not larger, under the trivial \(n-1\)-fold revisit bound. This is
exactly the scale of the carried core left open by the previous owner-Schreier
turnover theorem. A genuine AFR proof needs a new no-recycling or signed-routing
input.

---

## 6. A fixed-depth minimizer obstruction

The height lock has a particularly sharp consequence at depth one.
Throughout this section set \(H=1\), and write \(\mathcal R_{\tau,1}\) for the
depth-one elementary release. For \(m\ge3\), \(c_1=1\); equivalently, the formulas
below may be read first for the unweighted objective \(Q_1\), whose minimizers are
the same as those of \(\mathcal Q_1=Q_1/c_1\).

For a fresh transposition at depth one, define

\[
 \mathsf B_\tau
 =\sum_p\binom{|z_p|}{2},
 \tag{6.1}
\]

\[
 \mathsf M_\tau
 =\frac12\sum_p\left(\sum_K|d_{K,p}|-|z_p|\right),
 \tag{6.2}
\]

\[
 \mathsf R_\tau^{\rm in}
 =\sum_{p,K}\binom{|d_{K,p}|}{2}.
 \tag{6.3}
\]

The exact fair expected gain is

\[
 \mathsf B_\tau-\mathsf M_\tau-\mathsf R_\tau^{\rm in}.
 \tag{6.4}
\]

### Theorem 6.1 (size-three depth-one lock)

Let \(F_*\) globally minimize the depth-one objective \(\mathcal Q_1\). Fix a
transposition \(\tau\), and suppose every fresh \(\tau\)-component has at most
three owners. Then

\[
 \boxed{\mathsf R_\tau^{\rm in}=0,\qquad
 \mathsf M_\tau\ge\mathsf B_\tau.}
 \tag{6.5}
\]

If the component effects are targetwise sign-aligned, then

\[
 \boxed{\mathsf B_\tau=0,\qquad \mathcal R_{\tau,1}=0.}
 \tag{6.6}
\]

#### Proof

At depth one, the leakage bound (5.10) gives

\[
 |d_{K,p}|
 \le\left\lfloor\frac{|K|}{2}\right\rfloor\le1.
\]

Thus every term in (6.3) vanishes. At a global minimum, the fair average of exact
children cannot have lower energy. Equation (6.4) therefore gives
\(\mathsf M_\tau\ge\mathsf B_\tau\).

Under targetwise sign alignment, \(\mathsf M_\tau=0\), so
\(\mathsf B_\tau=0\). Hence \(|z_p|\le1\) for every pair. Both the duplicate term
and the parity-restoration term vanish, so the entire elementary release is zero.
\(\square\)

Thus microscopic fragmentation through components of sizes two or three does not
by itself create depth-one heat at a global minimizer. Every gain-capable duplicate
is cancelled by opposite-target mixing.

---

## 7. Independent audit

The decisive MSW argument was independently rederived after the proof was assembled.
The following corrections and checks are incorporated above.

1. **Weighted packet variance.** The exact identity is (4.4). Replacing it by
   \(V=(8H-4)C_{m-2}\) would be false when some \(c_q>1\).

2. **The \(c_H\) product.** The correct factor is

   \[
   \frac{m+2+j}{m-j}
   =1+\frac{2+2j}{m-j},
   \]

   leading to (4.10). A constant numerator \(H+1\) is not an identity.

3. **Pile constants.** Equations (4.11)--(4.13) give
   \(\|D\|_H^2>9HB/4\); (4.14) gives \(V<7HB/4\), hence
   \(\Lambda>HB/2\). No asymptotic equality is used.

4. **Balanced odd packet count.** The zero dummy is used only to define a balanced
   distribution. It creates no component and no switch. Pair correlation is
   \(-1/k\), exactly as used in (4.18).

5. **Orientation scope.** Choosing the higher endpoint reverses all packet vectors
   together. It gives \(D^\sharp=\pm D\), not independent choices of packet
   orientations.

6. **Floor normalization.** Both \(\pi_{\tau,H}\) and the child residual norm use
   the full Hilbert normalization. Equation (4.28) has no missing factor two or
   four.

7. **Fresh recomputation.** Sequential packet legality follows from their disjoint,
   \(\tau\)-invariant root supports. It does not assume that unrelated future
   component partitions persist.

8. **First-bridge scope.** The first-edge identity (4.25) applies after
   \(F^\sharp\) has been declared the initial factor. Moving from the canonical
   endpoint to \(F^\sharp\) is not counted as a free preparation.

9. **Release fraction.** The unconditional absolute gain \(>HB/8\) does not imply
   a fixed fraction of \(\Delta_\tau^Q\), because that release need not be
   \(O(HB)\). The fractional conclusion is only Corollary 4.4 under the explicitly
   unproved residual bound (4.29).

10. **One cell, not repeated release.** The Catalan-many microsteps use the same
    intrinsic \(\tau\)-cell. They provide a genuine recomputed exact path but only
    one fresh subgroup bridge.

11. **Common signs across targets.** The local floor-token discussion after
    Corollary 2.2 is only a contribution to one global random-sign estimate. It is
    not a targetwise independent optimization.

12. **Distance factor.** The row symmetric difference in Lemma 5.2 counts both
    lost and gained targets. The correct value is \(4\min(r,d)\), with the
    \(d=r\) subtraction of four, not half that amount.

13. **Zero-release sign conflicts.** Corollary 2.2 requires \(M_p=0\) on every
    moved pair, not only on pairs with positive elementary release. A balanced
    \(z_p=0\) pair with nonzero opposing component effects can otherwise force
    signs that destroy the gain on a different pair.

14. **Loop and seam convention.** The owner graph suppresses owner-self orbits.
    With that convention its degree is (3.5), cuts are even, and (3.3) counts
    crossing-orbit replacement operations rather than necessarily distinct final
    multiedge changes. The fresh seam-incidence graph is taken on all deletion
    pieces, including unchanged old components.

15. **Multistep and depth-one scope.** The sharper exposure substitutions in
    (5.17) and (5.21) retain the leading factor two. Equation (5.23) explicitly
    assumes the fresh-forest release identity and one fixed cross-round carrier.
    Section 6 sets \(H=1\); its zero-release conclusion is not a claim about deeper
    ranks.

All constants in Theorems 4.3, 4.7, 5.4, 5.6, and Corollary 4.5 survive these
checks.

---

## 8. Exact remaining gate

This report proves a nontrivial fixed-window special-factor case and a quantitative
invariant obstruction. It does not prove \(AFR_A\).

The surviving theorem must combine, on a prescribed factor near a global minimum:

1. **same-bridge exposure** of a fixed share of the subgroup-profile release;
2. **signed fragmentation** controlling both the maximum target bundle and
   opposite-target mixing across one common component signing;
3. **height-area control** for any uphill preparations, in view of Theorem 5.1;
4. **fresh seam routing** preventing the new incidence graph from immediately
   reconnecting all deletion pieces; and
5. **a no-recycling estimate** improving the \(B/n\) carrier threshold in (5.24).

The MSW packet theorem shows that the desired scale and a Catalan number of exact
microcomponents can coexist on one high-release bridge. The canonical dichotomy
shows that failure then forces a macroscopic adverse residual. The height--capacity
theorem shows that unsigned fragmentation at a minimizer is not enough, while the
multistep ledger proves exactly how far it gets before owner recycling becomes the
only remaining obstruction.

No exact high-energy counterexample to \(AFR_A\), no arbitrary-start productive
bridge sequence, and no fixed-window balancing theorem are claimed.
