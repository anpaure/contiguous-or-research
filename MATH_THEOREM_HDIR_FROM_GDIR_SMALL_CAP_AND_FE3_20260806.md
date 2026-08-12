# HDIR from GDIR, the small cap, and FE3

**Date:** 2026-08-06  
**Method:** exact Bonferroni decomposition, size-biased Young inequality,
and the authenticated first-two-hit change of variables; no computation or
search  
**Status:** proof-safe reduction for the root-omitted base pair family on
the common stopped good interval.  The conclusion is conditional only on
the already named `GDIR`, root-contraction, `PCAP`, `FE3`, slot, and
owner-mixture rows.  Marked/rooted variants still require their finite
occurrence-convention replay.

## 1. Precise theorem inputs

At one stopped state let

\[
 A=(Q,E,F),\qquad \mu_A=c_i(A)R_i(A)\ge0
\tag{1.1}
\]

be a base pair-potential row.  For one of the three incidence faces

\[
 V_A=E-Q,\qquad F-Q,\qquad\hbox{or}\qquad(E\cup F)-Q,
\tag{1.2}
\]

regard `V_A` as a **set of distinct physical resource vertices**, not as
a multiset of occurrences.  This convention is forced by the hit event:
two appearances of the same physical resource are one event.  Assume:

1. `|V_A|<=C_0d`; there are only constantly many non-slot resource
   types and constantly many slot vertices in one row.
2. On the good relation face, for distinct non-slot resources,

   \[
   Y_{x,y}\le {C_1\over d}\min(Y_x,Y_y)\le {C_2\over d}.
   \tag{1.3}
   \]

   Rigid, cross-half, owner-parallel, and slot-containing exceptions are
   in their named `FE3`/owner/slot ledgers.
3. The base first-two-hit row is available in the coefficient-faithful
   form

   \[
   \mathbb E\sum_{i<\tau}{1\over X_i}
     \sum_A\mu_A
     \sum_G a_G {j_A(G)\choose2}
      \le {C\over d}\mathsf A,
   \qquad
   j_A(G)=|G\cap V_A|,
   \tag{1.4}
   \]

   and the slot-containing analogue is included in the slot ledger with
   the same spare.  Equation (1.4) is exactly the dynamic form of
   `(FP9)` plus `(FE3)`, not a new hypothesis about independence.
4. On `PCAP`, for every non-slot type `T`,

   \[
   \beta_T\le {C_3\varepsilon_P\over d^2},
   \qquad
   g_x^\circ=\beta_TY_x+\zeta_x,
   \qquad
   \mathfrak G_T=\sum_{x\in T}{\zeta_x^2\over Y_x}.
   \tag{1.5}
   \]

5. The common rate stop gives

   \[
   h_i:=1-\rho_i^2\asymp X_i^{-1}.
   \tag{1.6}
   \]

The distinguished roots `Q` are deliberately absent from (1.2).  Their
hazards belong to the two-root service/root ledger.  This removal is
necessary: `g_x^circ` in (1.5) omits those roots.

Under these inputs the root-omitted base hazard Dirichlet budget satisfies

\[
 \boxed{
 \operatorname {HDIR}_{\rm base}^{\circ}
 \le C\theta\operatorname {GDIR}
   +C{\varepsilon_P\over\theta}\operatorname {ROOT}
   +C\mathsf A+o(\mathsf A)
 }
\tag{1.7}
\]

for every fixed `0<theta<1`.  Thus `theta` may be chosen first to absorb
the `GDIR` coefficient, and then `\varepsilon_P` may be chosen to absorb the
root coefficient.

## 2. Exact one-row Bonferroni decomposition

Fix `A` and one face `V=V_A`.  For a resource `x in V`, let

\[
 u_x=1-\rho_i\quad\hbox{or}\quad1-\rho_{s,i},
 \qquad \alpha_x=X_iu_x,
 \qquad a_x=\alpha_x-Y_x,
\tag{2.1}
\]

according to its shore.  Put

\[
 q_i(V)=1-\prod_{x\in V}(1-u_x),
 \qquad
 \Lambda_i(V)=\sum_G a_G\mathbf1_{\{G\cap V\ne\varnothing\}},
 \qquad
 \mathcal H_i(V)=q_i(V)-{\Lambda_i(V)\over X_i}.
\tag{2.2}
\]

Define

\[
 \begin{aligned}
 D_i^{\rm prod}(V)&=\sum_{x\in V}\alpha_x-X_iq_i(V),\\
 D_i^{\rm act}(V)&=\sum_{x\in V}Y_x-\Lambda_i(V),\\
 \mathcal B_i(V)&=\sum_{\{x,y\}\subseteq V}Y_{x,y}.
 \end{aligned}
\tag{2.3}
\]

The two Bonferroni inequalities give

\[
 0\le D_i^{\rm prod}(V)
 \le X_i\sum_{\{x,y\}\subseteq V}u_xu_y,
 \qquad
 0\le D_i^{\rm act}(V)\le\mathcal B_i(V).
\tag{2.4}
\]

More importantly, there is the **exact signed identity**

\[
 \boxed{
 X_i\mathcal H_i(V)
   =\sum_{x\in V}a_x+D_i^{\rm act}(V)-D_i^{\rm prod}(V).}
\tag{2.5}
\]

Hence

\[
 \left|X_i\mathcal H_i(V)-\sum_{x\in V}a_x\right|
 \le\mathcal B_i(V)+D_i^{\rm prod}(V).
\tag{2.6}
\]

The deterministic term in (2.6) cannot be omitted: it may be positive
even when `B_i(V)=0`.  Since `|V|=O(d)` and `u_x=O(X_i^{-1})`,

\[
 D_i^{\rm prod}(V)\le {Cd^2\over X_i}.
\tag{2.7}
\]

On the central stopped interval, `X_i>=cM/d`, there are at most `CM`
steps, and `PCAP` implies `sum_A mu_A<=C X_i/d^2`.  Therefore

\[
 \mathbb E\sum_{i<\tau}{1\over X_i}
   \sum_A\mu_A\bigl(D_i^{\rm prod}(V_A)\bigr)^2
 \le {Cd^4\over M}=o(\mathsf A).
\tag{2.8}
\]

The last comparison uses the central exponential size of `M`; it is the
existing deterministic density-remainder ledger.

## 3. The first-order square

For one fixed non-slot type `T`, set `V_{A,T}=V_A\cap T`.  The finitely
many resource types are split before squaring, so this costs only an
absolute factor.  Row-size Cauchy and nonnegativity give

\[
 \begin{aligned}
 \sum_A\mu_A
   \left(\sum_{x\in V_{A,T}}a_x\right)^2
 &\le C d\sum_x g_{x,V}^\circ a_x^2\\
 &\le C d\sum_x g_x^\circ a_x^2,
 \end{aligned}
\tag{3.1}
\]

where

\[
 g_{x,V}^\circ=\sum_{A:x\in V_{A,T}}\mu_A
 \le \sum_{A:x\in(E\cup F)-Q}\mu_A=g_x^\circ.
\tag{3.2}
\]

On the good-load interval `|a_x|<=C`.  For any `theta in (0,1)`,

\[
 |\zeta_x|a_x^2
 \le {\theta\over2d\beta_T}{\zeta_x^2\over Y_x}
    +{d\beta_T\over2\theta}Y_xa_x^4,
\tag{3.3}
\]

with the zero convention when `beta_T=0`.  In that case nonnegativity of
`g_x^circ` implies `g_x^circ=0` for every `x`, so the row vanishes.
Multiplying (3.3) by `Cd`, using `a_x^4<=C a_x^2`, and applying (1.5)
gives

\[
 \boxed{
 {1\over X_i}\sum_A\mu_A
   \left(\sum_{x\in V_{A,T}}a_x\right)^2
 \le {C\theta\over\beta_TX_i}\mathfrak G_T
   +{C\varepsilon_P\over\theta X_i}
      \sum_xY_xa_x^2.}
\tag{3.4}
\]

The harmless smaller term `C\varepsilon_P/(dX_i)` has been absorbed into
the displayed root term.  Summing (3.4) over time and the fixed resource
types is exactly the `GDIR + ROOT` part of (1.7).  Owner-parallel means
and slot first-order terms are not hidden in this line; they remain in
their named ledgers.

## 4. The nonlinear remainder and exact FE3 multiplicity

Split `B_i(V)` into non-slot pairs and slot-containing pairs.  There are
`O(d^2)` non-slot pairs, each of load `O(1/d)` by (1.3), hence their total
is `O(d)`.  There are only `O(d)` slot-containing pairs in a row and
their loads are bounded, so their total is also `O(d)`.  Thus, separately
on the base and slot faces,

\[
 \mathcal B_i(V)\le Cd,
 \qquad
 \mathcal B_i(V)^2\le Cd\,\mathcal B_i(V).
\tag{4.1}
\]

There is no occurrence-multiplicity loss.  By the definition
`Y_{x,y}=\sum_{G\supseteq\{x,y\}}a_G` and because `V_A` is a set of
distinct resource vertices,

\[
 \begin{aligned}
 \sum_{\{x,y\}\subseteq V_A}Y_{x,y}
 &=\sum_G a_G
   \sum_{\{x,y\}\subseteq V_A}
       \mathbf1_{\{x,y\}\subseteq G}\\
 &=\sum_G a_G{|G\cap V_A|\choose2}.
 \end{aligned}
\tag{4.2}
\]

Therefore

\[
 {1\over X_i}\sum_A\mu_A\mathcal B_i(V_A)
 ={1\over X_i}\sum_A\mu_A
   \sum_G a_G{j_A(G)\choose2},
\tag{4.3}
\]

which is precisely (1.4).  If the pair potential stores `(E,F)` in both
orders while static `FE3` stores it unordered, the multiplicity is exactly
two.  Choosing one of the two sides or the union contributes at most
another factor three.  Distinguished roots were removed before (4.2).
Hence the comparison has an absolute multiplicity, never an `O(d)`
occurrence multiplicity.

Combining (4.1), (4.3), and `FE3` gives

\[
 \boxed{
 \mathbb E\sum_{i<\tau}{1\over X_i}
   \sum_A\mu_A\mathcal B_i(V_A)^2
 \le C d\,{\mathsf A\over d}=C\mathsf A.}
\tag{4.4}
\]

The displayed factor `d` is exactly the one paid by the authenticated
`1/d` first-two-hit spare.  Rigid/cross-half and slot classes are included
only through their separately proved parts of (1.4); (4.4) does not infer
them from the non-slot pair-ratio stop.

## 5. HDIR normalization and conclusion

Write

\[
 D_i(V)=X_i\mathcal H_i(V).
\tag{5.1}
\]

By (1.6),

\[
 {1\over h_i}\mathcal H_i(V)^2
 ={1\over h_iX_i^2}D_i(V)^2
 \asymp {1\over X_i}D_i(V)^2.
\tag{5.2}
\]

Use (2.5), `(u+v+w)^2<=3(u^2+v^2+w^2)`, (2.8),
(3.4), and (4.4), and then sum over the fixed incidence faces and
resource types.  This proves (1.7).

The theorem deliberately does **not** prove `GDIR`; it proves that `HDIR`
is not a second independent dynamic gate after `GDIR`, `ROOT`, `PCAP`,
and `FE3` are placed in one stopped Lyapunov.  Marked/rooted families need
the same finite root-omission and ordered-occurrence replay before they can
be added to the displayed base conclusion.
