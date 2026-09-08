# Lane K after the sector retraction: harmonic pruning and vanishing zero-winding density

Date: 2026-07-25

Method: pure mathematics only. No web search, computation, finite search,
solver, or long-running job is used.

## 0. Result and exact scope

Put

\[
 N=2r+1,
 \qquad B_r=\operatorname{Cat}_r,
 \qquad \tau=\phi^2.
\]

For fixed \(A>0\), let \(\mathcal Z_r(A)\) be the set of normalized Dyck
roots which start a **genuine zero-winding** consecutive omitted-label
return of gap \(2h+1\), where

\[
 1\le h\le A\sqrt r.
\]

Here \(h=\operatorname{ht}(D)\) by the audited zero-winding height
equality. In particular, a root contributes at most once: the strict
first-passage variable is strictly decreasing, so it has at most one
zero-winding hit.

Then

\[
 \boxed{|\mathcal Z_r(A)|=o_A(B_r).}
 \tag{0.1}
\]

This conclusion uses the exact dynamic \(\tau\)-chronology and the
audited Pascal fan. It does not use the false implication

\[
 d(D)=1\Longrightarrow
 \text{a return at gap }2\operatorname{ht}(D)+1.
\]

The proof has two new ingredients.

1. If \(R_j(D)=\tfrac12|\partial^jD|\) is the semilength (plane-tree
   edge rank) after \(j\) simultaneous
   peak deletions, then for every fixed \(j\), under the uniform Catalan
   measure,

   \[
    \boxed{R_j(D)/r\longrightarrow1/(j+1)}
    \tag{0.2}
   \]

   in probability. A bivariate plane-tree generating function proves
   this directly, including a sufficient second-moment bound.

2. For a genuine zero-winding return whose exact Pascal fan survives
   through \(k\) pruning levels, the fraction of any fixed rank-profile
   tower fibre which can carry that fan is at most

   \[
    Q_k(\mathbf r)
    \le
    \prod_{j=1}^k
    \left({2r_j\over r_{j-1}+r_{j+1}}\right)^j.
    \tag{0.3}
   \]

   On the formal harmonic profile \(r_j=r/(j+1)\), the right-hand
   envelope in (0.3) is exactly

   \[
    {(k+2)^k\over(k+1)^{k+1}}\le {e\over k+1}.
    \tag{0.4}
   \]

A slow diagonal \(k=k(r)\to\infty\) makes almost every Catalan root
harmonic through depth \(k\). The exact fan capacity then gives an
\(O(1/k)\) fraction on the good profiles; roots whose return reaches a
path core before depth \(k\), and roots of height below \(2k\), lie in a
vanishing exceptional set.

The implication boundary is essential. Equation (0.1) is a start-count
theorem, not the required quotient interval-packing theorem. The linear
dominance ledger admits the following weaker little-oh sufficient
hypothesis:

\[
 \overline\nu_{A\sqrt r}=o_A(B_r/\sqrt r),
 \tag{0.5}
\]

whereas (0.1) alone gives only \(o(B_r)\). Section 24 of the residence
reduction records the stronger convenient big-oh gate

\[
 \overline\nu_{A\sqrt r}=O_A(B_r/N).
\]

The two statements are compatible: for fixed \(A\),
\(H/N=O_A(r^{-1/2})\), so \(O_A(B_r/N)\) implies
\(o_A(B_r/H)\). The converse is not supplied by the ledger.

A sparse set of starts can be well separated on quotient cycles, so start
rarity and trace length may not be multiplied without a further
chronology-sensitive capacity or clustering lemma. Positive-winding
returns are also outside (0.1).

Thus global literal fusion is only a fallback. One possible density route
is to upgrade the dynamic theorem to the weaker little-oh packed scale
(0.5), including positive winding. The already isolated Section 24 gate
\(O_A(B_r/N)\) remains a stronger sufficient target and is not being
retracted or replaced.

## 1. Exact pruning-rank statistic

Use the plane-tree bijection for Dyck words. For a rooted ordered plane
tree \(T\), let

\[
 X_j(T)=|\partial^jT|
 \tag{1.1}
\]

be the number of edges remaining after \(j\) rounds of simultaneous leaf
deletion. Let \(C(z)=\sum_{r\ge0}B_rz^r\), and let \(C_q(z)\) count plane
trees of height at most \(q\). Thus

\[
 C(z)=1+zC(z)^2,
 \qquad
 C_q(z)={1\over1-zC_{q-1}(z)},
 \qquad C_0(z)=1.
 \tag{1.2}
\]

For fixed \(j\ge1\), define the bivariate generating function

\[
 F_j(z,u)=\sum_Tz^{|T|}u^{X_j(T)}.
 \tag{1.3}
\]

### Lemma 1.1 (exact bivariate pruning equation)

Put \(A_j(z)=C_{j-1}(z)\). Then

\[
 \boxed{
 F_j(z,u)
 ={1\over1-z\{uF_j(z,u)-(u-1)A_j(z)\}}.}
 \tag{1.4}
\]

#### Proof

A plane tree is an ordered sequence of child subtrees. Consider one child
subtree \(U\), including the edge from the present root to the root of
\(U\). After \(j\) leaf-deletion rounds, the connecting edge survives if
and only if \(\operatorname{ht}(U)\ge j\). The surviving edges below it
are counted by \(X_j(U)\). Therefore the marked generating function of one
child subtree is

\[
 z\sum_Uz^{|U|}u^{X_j(U)+\mathbf1_{\{\operatorname{ht}(U)\ge j\}}}
 =z\{uF_j-(u-1)A_j\}.
\]

Taking an arbitrary ordered sequence gives (1.4). \(\square\)

At \(u=1\), (1.4) gives \(F_j(z,1)=C(z)\). Write

\[
 M_j(z)=\left.\partial_uF_j(z,u)\right|_{u=1},
 \qquad
 V_j(z)=\left.\partial_u^2F_j(z,u)\right|_{u=1}.
 \tag{1.5}
\]

### Lemma 1.2 (first two factorial moments)

One has the exact identities

\[
 \boxed{
 M_j(z)={(C-1)(C-A_j)\over2-C},}
 \tag{1.6}
\]

and

\[
 \boxed{
 V_j(z)
 ={2zC\over2-C}
  \left(M_j(z)^2+(2C-A_j)M_j(z)\right).}
 \tag{1.7}
\]

Consequently, for a uniform semilength-\(r\) Dyck root,

\[
 \mathbb E X_j={r\over j+1}+O_j(\sqrt r),
 \qquad
 \operatorname{Var}(X_j)=O_j(r^{3/2}).
 \tag{1.8}
\]

In particular, (0.2) holds.

#### Proof

Equation (1.4) is equivalently

\[
 zuF_j^2-\{1+z(u-1)A_j\}F_j+1=0.
 \tag{1.9}
\]

Implicit differentiation at \(u=1\), using \(F_j=C\) and

\[
 2zC-1={C-2\over C},
 \]

gives (1.6). Differentiating a second time gives (1.7).

Put \(t=\sqrt{1-4z}\). Then

\[
 C(z)={2\over1+t},
 \qquad
 C_{j-1}(1/4)={2j\over j+1}.
 \tag{1.10}
\]

Since \(C_{j-1}\) is analytic beyond \(z=1/4\) for fixed \(j\),
(1.6)--(1.7) give

\[
 M_j(z)={1\over(j+1)t}+O_j(1),
 \tag{1.11}
\]

and

\[
 V_j(z)
 ={1\over2(j+1)^2t^3}+O_j(t^{-2}).
 \tag{1.12}
\]

The elementary coefficient estimates

\[
 [z^r](1-4z)^{-1/2}\sim{4^r\over\sqrt{\pi r}},
 \qquad
 [z^r](1-4z)^{-3/2}\sim{2\,4^r\sqrt r\over\sqrt\pi},
 \tag{1.13}
\]

together with

\[
 B_r\sim{4^r\over\sqrt\pi r^{3/2}},
\]

prove the mean and factorial-second-moment estimates in (1.8). Their
leading quadratic terms agree, and the remainder is
\(O_j(r^{3/2})\), proving the stated variance bound. Chebyshev's
inequality proves (0.2). \(\square\)

### Corollary 1.3 (fixed-depth harmonic concentration)

For every fixed \(K\) and every \(\varepsilon>0\), the proportion of
Dyck roots satisfying

\[
 \left|{(j+1)X_j(D)\over r}-1\right|\le\varepsilon
 \qquad(1\le j\le K+1)
 \tag{1.14}
\]

tends to one as \(r\to\infty\).

#### Proof

Apply Lemma 1.2 at each of the finitely many depths and take a union
bound. \(\square\)

## 2. The exact fan-capacity estimate on harmonic profiles

Assume now that \(D\) starts a genuine zero-winding return of duration
\(h\), so its odd gap is \(2h+1<N\). Let

\[
 D^{(j)}=\partial^jD,
 \qquad r_j={1\over2}|D^{(j)}|,
 \tag{2.1}
\]

Thus \(r_j\) is the semilength, equivalently the number of remaining
plane-tree edges; in particular \(r_j=X_j(D)\) in the notation of
Section 1.

and let

\[
 \ell=\min\{j:r_j=h-j\}
 \tag{2.2}
\]

be its first path-core level. The audited tight-return Pascal fan says
that, for every

\[
 k\le\min(\ell,\lfloor h/2\rfloor),
\]

the inverse tower has \(j\) distinct prescribed child-slot variables at
level \(j\), \(1\le j\le k\). For a fixed rank profile and a fixed
level-\(k\) bottom core, its compatible outer-tower capacity is at most
the unrestricted tower capacity times

\[
 Q_k(\mathbf r)
 =\prod_{j=1}^k\prod_{i=0}^{j-1}
 {2r_j-i\over r_{j-1}+r_{j+1}-i}.
 \tag{2.3}
\]

The rank sequence is discretely convex:

\[
 r_{j-1}+r_{j+1}\ge2r_j.
 \tag{2.4}
\]

Therefore

\[
 {2r_j-i\over r_{j-1}+r_{j+1}-i}
 \le{2r_j\over r_{j-1}+r_{j+1}}
 \tag{2.5}
\]

for \(0\le i<j\), proving (0.3).

### Lemma 2.1 (uniform good-profile bound)

There is an absolute \(K_0\) with the following property. Let
\(K\ge K_0\), and suppose

\[
 r_j={r\over j+1}(1+\theta_j),
 \qquad
 |\theta_j|\le K^{-4}
 \qquad(0\le j\le K+1).
 \tag{2.6}
\]

Then

\[
 \boxed{Q_K(\mathbf r)\le {2e\over K+1}}.
 \tag{2.7}
\]

#### Proof

Put

\[
 q_j={2r_j\over r_{j-1}+r_{j+1}},
 \qquad
 q_j^*={j(j+2)\over(j+1)^2}.
\]

Equation (2.6) gives

\[
 q_j\le q_j^*\exp(3K^{-4}).
\]

Using (0.3), summing \(j\le K\), and applying the exact telescoping
product gives

\[
 \begin{aligned}
 Q_K(\mathbf r)
 &\le \exp\!\left(3K^{-4}\sum_{j=1}^Kj\right)
       \prod_{j=1}^K(q_j^*)^j\\
 &=\exp(O(K^{-2}))
   {(K+2)^K\over(K+1)^{K+1}}\\
 &\le {2e\over K+1}.
 \end{aligned}
\]

This proves (2.7). \(\square\)

## 3. A slow diagonal and exclusion of early path cores

For each integer \(K\ge2\), Corollary 1.3 permits a threshold \(R_K\)
such that, for all \(r\ge R_K\), all but at most \(B_r/K^2\) roots
satisfy (2.6) through depth \(K+1\). Increase the thresholds so that

\[
 R_{K+1}>R_K,
 \qquad
 R_K\ge K^{12},
 \tag{3.1}
\]

and so that the number of roots of height below \(2K\) is at most
\(B_r/K^2\) whenever \(r\ge R_K\). The last condition follows from the
path-graph spectral-radius estimate

\[
 \#\{D:\operatorname{ht}(D)<2K\}
 \le
 \left(2\cos{\pi\over2K+1}\right)^{2r}.
 \tag{3.2}
\]

Define \(K(r)=K\) on

\[
 R_K\le r<R_{K+1}.
 \tag{3.3}
\]

Then

\[
 K(r)\longrightarrow\infty,
 \qquad K(r)\le r^{1/12}.
 \tag{3.4}
\]

Call a root **good** if it satisfies (2.6) through depth \(K(r)+1\),
and call it **tall** if its height is at least \(2K(r)\).

### Lemma 3.1 (a good Gaussian return carries a depth-\(K\) fan)

Fix \(A>0\). For all sufficiently large \(r\), if a good, tall root
starts a genuine zero-winding return of duration \(h\le A\sqrt r\), then

\[
 K(r)\le\min(\ell,\lfloor h/2\rfloor).
 \tag{3.5}
\]

#### Proof

The zero-winding height equality gives \(h=\operatorname{ht}(D)\), so
tallness gives \(K(r)\le h/2\). If \(\ell<K(r)\), then by the definition
of the first path core,

\[
 r_\ell=h-\ell\le A\sqrt r.
 \tag{3.6}
\]

Goodness instead gives

\[
 r_\ell\ge(1-K^{-4}){r\over\ell+1}
 \ge {r\over2K}.
 \tag{3.7}
\]

Since \(K\le r^{1/12}\), the right side of (3.7) exceeds
\(A\sqrt r\) for all sufficiently large \(r\), contradicting (3.6).
Thus \(\ell\ge K\). \(\square\)

## 4. Vanishing density of genuine zero-winding starts

### Theorem 4.1

For every fixed \(A>0\), equation (0.1) holds.

#### Proof

The roots of height below \(2K(r)\), and the roots which are not good,
contribute at most

\[
 {2B_r\over K(r)^2}.
 \tag{4.1}
\]

Consider the remaining zero-winding starts. Lemma 3.1 lets us apply the
exact fan-capacity theorem through depth \(K=K(r)\).

Fix one good rank profile

\[
 r_0,r_1,\ldots,r_{K+1}
\]

and one level-\(K\) bottom root. The unrestricted inverse tower capacity
is the product of the exact conditional fibre sizes. The number of outer
towers which carry the required zero-winding Pascal fan is at most this
capacity times \(Q_K(\mathbf r)\). Lemma 2.1 bounds that fraction by
\(2e/(K+1)\).

There is no hidden union over return durations or marked bottom phases in
this conditional estimate. The return duration is the height of the outer
root, hence is determined by the height of the bottom root plus \(K\); the
level-\(K\) Dyck root is already a rooted phase, and the fan starts at its
time-zero phase. Thus the prescribed consecutive slot variables in the
multislot theorem are determined during the conditional inverse expansion.

Now sum over all good profiles and all bottom roots. Every semilength-
\(r\) Dyck root has one unique pruning profile and one unique level-
\(K\) bottom root. The unrestricted tower capacities over the good
profiles therefore sum to at most \(B_r\) (and the capacities over all
profiles sum to exactly \(B_r\)). Therefore

\[
 |\mathcal Z_r(A)|
 \le {2e\over K(r)+1}B_r+{2\over K(r)^2}B_r
 =o(B_r).
 \tag{4.2}
\]

This proves the theorem. \(\square\)

## 5. Consequence for the corrected coefficient-one route

The audited linear dominance seam gives a central-band word of length

\[
 L_H\le W+2HB_r+2(5H-1)\nu_H(P_r),
 \qquad W=NB_r.
 \tag{5.1}
\]

After the deck reduction, use the audited comparison

\[
 N\overline\nu_H\le \nu_H(P_r)
 \le 2N\overline\nu_H+NZ_H,
 \tag{5.2a}
\]

where the exceptional short-period term satisfies \(HZ_H=o(B_r)\) in
every fixed Gaussian window. A sufficient quotient packing
hypothesis---and the weakest one obtained by requiring each nonnegative
error term displayed in (5.1) and (5.2a) to be \(o(W)\)---is

\[
 \boxed{
 \overline\nu_H=o_A(B_r/H)
 =o_A(B_r/\sqrt r).}
 \tag{5.2}
\]

Indeed, direct substitution of (5.2a) into (5.1) gives

\[
 {L_H-W\over W}
 \le {2H\over N}
   +{4(5H-1)\over B_r}\,\overline\nu_H
   +{2(5H-1)\over B_r}\,Z_H.
\tag{5.3}
\]

For fixed \(A\), the first term is \(o_A(1)\), hypothesis (5.2) makes
the second \(o_A(1)\), and Theorem 17.1--(17.2) gives

\[
 Z_H\le(2H+2)N^{2H+2},
\qquad {HZ_H\over B_r}=o_A(1),
\tag{5.4}
\]

because \(H=O_A(\sqrt r)\). Hence (5.2) genuinely implies
\(L_H=W+o_A(W)\).

The stronger Section 24 big-oh gate

\[
 \overline\nu_H=O_A(B_r/N)
\]

also suffices. More precisely, it is not required by the displayed ledger:
for fixed \(A\),

\[
 O_A(B_r/N)\subset o_A(B_r/H)
\tag{5.5}
\]

because \(H/N=O_A(r^{-1/2})\). No converse is claimed, and the report does
not assert that an actual PBBS packing violating the stronger gate exists.
Accordingly, Section 24's phrase “sharp remaining input” should be read as
the isolated Catalan-order **big-oh** gate for physical packing. Equation
(5.2) is a different, weaker **little-oh** quotient condition extracted
from the same ledger; it does not retract the \(CP_A\) formulation.

If (5.2) holds for every fixed \(A\), the usual diagonalization is
legitimate. Choose integers \(A_j\uparrow\infty\) and thresholds
\(R_j\uparrow\infty\) so that for every \(r\ge R_j\), with
\(H_j=\lceil A_j\sqrt r\rceil\),

\[
 {H_j\over N}
 +{H_j\overline\nu_{H_j}\over B_r}
 +{H_jZ_{H_j}\over B_r}\le {1\over j},
\tag{5.6}
\]

and enlarge \(R_j\) so that

\[
 {A_j\log N\over\sqrt r}\le {1\over j}
\]

and the standard product-SCD tail outside depth \(H_j\) has the prescribed
error tending to zero with \(j\). Put \(A(r)=A_j\) on
\(R_j\le r<R_{j+1}\). Then \(A(r)\to\infty\),
\(H(r)\log N=o(r)\), (5.3) has \(o(W)\) excess, and the outer-rank tail is
\(o(W)\). Thus the same trimmed parity lift used in Theorems 22.2 and 24.3
gives coefficient one.

Theorem 4.1 rules out a Catalan-positive family of genuine zero-winding
starts. It does **not** imply (5.2): an \(o(B_r)\) set of interval starts
may still contain \(\Theta(B_r/H)\) pairwise edge-disjoint intervals.
Multiplying the \(O(1/K)\) fan-density gain by the trace-length gain is
not valid without a joint capacity theorem.

The exact remaining chronology-sensitive alternatives are:

1. prove that the harmonic-profile zero-winding starts cluster enough on
   quotient cycles to give (5.2);
2. strengthen the aggregate fan-capacity fraction from \(o(1)\) to
   \(o(1/H)\); or
3. prove a trace-wide transported-slot capacity which legitimately
   tensorizes the fan and interval ledgers.

Positive-winding returns need a parallel estimate at scale (5.2). The
winding ledger gives the correct critical big-oh order but no vanishing
factor.

A global dynamic-frame literal braid would bypass (5.2), but it is only a
fallback. Nothing in the retracted primitive-sector argument forces such a
braid.

## 6. Adversarial audit

1. **No false converse.** The fan theorem is invoked only after a genuine
   zero-winding return is assumed. No root is declared a return merely
   because \(d(D)=1\).

2. **The bivariate statistic is exact.** A child edge survives \(j\)
   pruning rounds exactly when the child subtree has height at least
   \(j\); its remaining internal edges contribute \(X_j\). This gives
   (1.4) without independence assumptions.

3. **The second moment is sufficient, not optimized.** The
   \(O_j(r^{3/2})\) variance already gives fixed-depth convergence in
   probability. No uniform-in-\(j\) estimate is silently assumed; growth
   of \(K(r)\) is obtained only by diagonalization.

4. **The diagonal has the required quantifiers.** For each fixed \(K\),
   all thresholds are chosen before passing to the next \(K\). Enlarging
   \(R_K\) enforces \(K\le r^{1/12}\) and the low-height deletion.

5. **Early path cores are not discarded heuristically.** On a good
   profile they contradict the exact equality \(r_\ell=h-\ell\) and the
   Gaussian upper bound on \(h\).

6. **Tower capacities form a partition.** Once the rank profile and the
   level-\(K\) bottom root are fixed, the inverse tower fibres are
   disjoint. Summing over all profiles gives exactly \(B_r\); summing only
   over the good profiles used in Theorem 4.1 gives at most \(B_r\).
   Zero-winding height equality and the rooted bottom phase prevent any
   extra union over durations or fan origins.

7. **The finite-slot factors have the correct direction.** Discrete
   convexity makes the denominator in (2.5) at least the numerator, and
   subtracting the same \(i\) can only decrease the ratio relative to its
   \(i=0\) value.

8. **No invalid rarity-times-length multiplication.** Section 5 states
   explicitly why (0.1) does not prove the packing gate.

9. **Implication scope.** The theorem concerns genuine zero winding only.
   Its start-count conclusion has no \(o(B_r/H)\) rate. It does not settle
   positive winding, \((RP_A)\), coefficient one, MWB, or labelled
   synchronization.
