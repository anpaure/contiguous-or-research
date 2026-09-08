# Adversarial audit of the RSCD/rotor report

## Verdict

The principal conclusions of `MATH_ATTACK_S_RSCD_ROTOR_REPORT_RAW_20260724.md` survive:

1. a saturated symmetric-chain decomposition of the central band extends to a full integral SCD;
2. the optimized radius-class rotor path-cover problem has an exact ordered-Hall formula;
3. the cut-odd-wreath construction supplies a genuine physical rotor skeleton with formal toll `o(W)`;
4. every rotor path-forest whose selected arcs all use one fixed global coordinate matching has toll `Omega_A(W)`;
5. the route remains unproved at one jointly chosen, integral, two-sided, all-depth shadow labeling with `o(W)` run toll.

Four corrections are mandatory.

* In the Hall formula, the neighborhood must be taken in a split-copy bipartite graph, not as an external out-neighborhood in the original digraph.
* The nested binary system must include `x_(v,H+1)=0`; otherwise the radius-`H` labels and counts are undefined.
* In the Gaussian paragraph, the centered normal law belongs to the middle-source distribution and the shifted normal law belongs to the target distribution.  The displayed deficit constant is nevertheless correct.
* The statement that sparse surgery cannot repair a fixed-pair construction is too strong if "sparse" means merely `o(W)` changed arcs.  The proved lower bound is `Omega_A(W/sqrt(m))` exceptional arcs, or equivalently `Omega_A(W)` mixed `q`-window starts.

There are also two implication-scope qualifications.  The cut-path nested-shadow lemma is a sufficient structured route to `RSCD_A`, not an equivalent characterization of every possible SCD/rotor construction.  And `RSCD_A` is sufficient only for the direct even-dimensional OR route; it is not necessary for arbitrary OR words and implies neither odd MWB nor labelled common-owner synchronization.

Throughout this audit,

\[
W=\binom{2m}{m},\qquad N_q=\binom{2m}{m-q},\qquad
H=\lceil A\sqrt m\rceil
\]

for fixed `A>0`, with `H<=m-1` for all sufficiently large `m`.

## 1. The band-extension theorem is correct

The extension argument is valid for a saturated symmetric-chain decomposition of the band.  At an extension step put

\[
r=m-q,\qquad
X=\binom{[2m]}{r-1},\qquad
Z=\binom{[2m]}{2m-r+1}.
\]

Every set at rank `r` belongs to a unique chain meeting both boundary ranks.  Write its correlated endpoints as

\[
A_y\in\binom{[2m]}r,qquad
B_y\in\binom{[2m]}{2m-r}.
\]

On the bipartite sides `X disjoint-union Y^-` and `Z disjoint-union Y^+`, use the comparison edges

\[
x\sim y^+\iff x\subset A_y,qquad
y^-\sim z\iff B_y\subset z,
\]

and the identity edge `y^-y^+`.  With

\[
\alpha=m+q+1,qquad \beta=m-q,
\]

comparison-edge weight `1/alpha` and identity-edge weight

\[
1-\frac\beta\alpha=\frac{2q+1}{m+q+1}
\]

give every row and column sum one.  Indeed, every `x` and `z` has `alpha` comparison neighbors, while each `y^-` and `y^+` has `beta` comparison neighbors.  This is a fractional perfect matching on a square bipartite graph, so its support satisfies Hall and contains an integral perfect matching.

If `y^-y^+` is selected, that chain stops at its current symmetric endpoints.  Otherwise the perfect matching supplies a unique `x` below and a unique `z` above.  Every new outer set is used exactly once.  Iteration through `q=H,...,m-1` yields a full SCD.

The phrase "preserving every band chain" should mean that each original band chain is preserved as a contiguous subchain with all of its internal adjacencies unchanged.  Boundary chains may acquire new outer endpoints; they are not necessarily left as maximal chains in the extension.

Thus the full-SCD extension issue is genuinely resolved.  For a fixed clipped rotor objective, the full and central-band formulations of `RSCD_A` are equivalent.

## 2. Correct ordered-Hall theorem

The formula in the report is correct only with an explicit split-copy definition.

Let `D=(V,A)` be a finite directed graph and `n=|V|`.  For a strict total order `prec` on `V`, form the bipartite graph

\[
B_\prec=(V_L,V_R,E_\prec),
\]

where

\[
u_Lv_R\in E_\prec
\quad\Longleftrightarrow\quad
(u,v)\in A\ \hbox{ and }\ u\prec v.
\]

For `S subseteq V_L`, let `Gamma_prec(S)` be its neighborhood in the full right copy `V_R`, including right-copy vertices whose underlying physical vertex also belongs to `S`.  Define

\[
\delta(\prec)
=\max_{S\subseteq V_L}
\bigl(|S|-|\Gamma_\prec(S)|\bigr),
\]

with the empty set allowed.

### Theorem 2.1

If `pc(D)` is the minimum number of components in a spanning vertex-disjoint directed path forest in `D`, singletons included, then

\[
\boxed{
pc(D)=\min_\prec\delta(\prec).
}
\]

There is no additive constant and no rounding term.

### Proof

For fixed `prec`, Hall deficiency gives

\[
\nu(B_\prec)=n-\delta(\prec).
\]

A matching in `B_prec` chooses directed arcs having indegree and outdegree at most one.  Every chosen arc strictly increases `prec`, so directed cycles are impossible.  Under the degree bounds, an undirected cycle would force every cycle vertex to have one chosen incoming and one chosen outgoing arc and hence would itself be a directed cycle.  Thus a maximum matching gives a spanning directed path forest with

\[
n-\nu(B_\prec)=\delta(\prec)
\]

components.

Conversely, a spanning directed path forest with `p` components has `n-p` arcs.  Any topological order of that forest makes all its arcs forward, and those arcs form a matching in the corresponding split-copy graph.  Hence `delta(prec)<=p`.  Minimize over forests and orders.  This proves the theorem.

Equivalently,

\[
pc(D)\le k
\quad\Longleftrightarrow\quad
\exists\prec\ \forall S\subseteq V_L:
|\Gamma_\prec(S)|\ge |S|-k.
\]

The quantifier order is essential: it is `exists order, for every cut`, or `min_prec max_S`.  It is neither an all-orders statement nor a `max_S min_prec` statement.  For the directed path `1->2->...->n`, the natural order has deficiency one, whereas the reverse order has deficiency `n`.

Two notation failures would make the original display false.

* `N_prec^+(S)` cannot mean the external neighborhood `N^+(S) setminus S`.  For `1->2`, the set `S={1,2}` has split-copy neighborhood `{2_R}` and deficiency one; the external neighborhood is empty and would give the false value two.
* The matching must use independent tail and head copies.  In `1->2->3`, an ordinary undirected matching has size one, while the split-copy matching uses both arcs and gives the correct one-component directed path.

Parallel rotor arcs do not affect this support theorem.  At radius zero the graph must use the corrected ordinary bottom/top swap, not the positive-radius rotor-successor formula.

## 3. Optimized toll and topological-order quantifiers

Fix one integral band SCD `Dcal` before any radius-class optimization.  Let `R_d(Dcal)` be its radius-`d` rotor graph.  Radius classes are disjoint, so their forest choices and total orders may be optimized independently after this common SCD is fixed:

\[
\boxed{
\Phi_{\rm PF}(\mathcal D,H)
=\sum_{d=0}^H(2d+1)
 \min_{\prec_d}
 \max_{S\subseteq V_{d,L}}
 \bigl(|S|-|\Gamma_{d,\prec_d}(S)|\bigr).
}
\]

The coefficient is exact.  A rotor component containing `t` radius-`d` chains has literal length

\[
t+2d+1.
\]

Summing `t` over all components and radii gives the `W` chain centers, while every component contributes the extra `2d+1` entries.

The only cross-depth coupling is the SCD itself.  Therefore the correct global optimization is

\[
\min_{\mathcal D}
\sum_d(2d+1)p_d^*(\mathcal D),
\]

not

\[
\sum_d(2d+1)
\min_{\mathcal D}p_d^*(\mathcal D).
\]

The latter would illegally choose a different SCD at each depth.

For selected forests, put

\[
P_q=\sum_{d=q}^Hp_d.
\]

The toll identity is purely algebraic and correct:

\[
\boxed{
\Phi=P_0+2\sum_{q=1}^HP_q.
}
\]

At rank `q`, the selected forest arcs from all classes `d>=q` give an inclusion matching of size

\[
\sum_{d=q}^H(\gamma_d-p_d)=N_q-P_q.
\]

These rankwise inclusion matchings are only necessary projections.  They must come from the same SCD and the same selected rotor arcs; independently selected rankwise matchings are insufficient.

For the direct one-SCD construction, concatenating the path components charges each component initialization once and gives the exact central-band length `W+Phi`.  If instead one imports the coordinate-orbit/Euler circulation theorem from the first wave, the weighted run-start bound `Q Phi` and the separate physical circuit-initialization bound

\[
Q\sum_d(2d+2)p_d\le2Q\Phi
\]

must not be silently identified.  The forests are chosen first; the connector pairing and macrograph chronology are constructed afterward.  A balanced macrograph may have several Euler circuits, and every circuit is initialized separately.  No theorem recolors an arbitrarily frozen Euler tour.

## 4. Odd-cut chronology and the nested system

The odd-cut skeleton is valid.  Cutting an exact odd wreath factor at `infinity` gives

\[
B=\operatorname{Cat}_m=\frac{W}{m+1}
\]

disjoint complementary Johnson paths of `m+1` middle vertices, hence `mB=N_1` path edges.  Their edge unions partition rank `m+1`: they are precisely the length-`m+1` odd cyclic intervals avoiding `infinity`, equivalently complements of the exact factor's length-`m` intervals containing `infinity`.

Along each cut path, every consecutive constant-radius run is a genuine directed rotor path.  No transition is asserted across different cut paths; each such break is already a separate component.  If the `B` paths are placed consecutively as blocks of length `m+1`, a global interval of `n_d` labels meets at most

\[
\frac{n_d}{m+1}+2
\]

path blocks.  Hence

\[
p_d\le\frac{n_d}{m+1}+2
\]

and

\[
\Phi_{\rm cut}
\le
\frac{1}{m+1}\sum_{d=0}^H(2d+1)n_d
+2\sum_{d=0}^H(2d+1)
=\frac{U_H}{m+1}+2(H+1)^2
=o(W).
\]

This proves only

\[
\exists\hbox{ a radius labeling with low run toll}.
\]

It does not prove that this labeling is a band SCD.  The missing assertion is one joint labeling having both the low-toll run property and all lower/upper shadow bijections.

The binary nested system needs the following repaired boundary condition:

\[
x_{v,0}=1,\qquad
x_{v,H+1}=0,\qquad
x_{v,q+1}\le x_{v,q}quad(0\le q\le H),
\]

with every `x_(v,q)` binary, and, for `1<=q<=H`,

\[
\sum_{v:L_q(v)=S}x_{v,q}=1,
\qquad
\sum_{v:U_q(v)=T}x_{v,q}=1.
\]

Then

\[
z_{v,d}=x_{v,d}-x_{v,d+1}
\]

is a genuine one-hot radius label:

\[
z_{v,d}\in\{0,1\},\qquad
\sum_{d=0}^Hz_{v,d}=1.
\]

Summing the shadow constraints gives

\[
\sum_vx_{v,q}=N_q,
\]

and hence

\[
\sum_vz_{v,d}=N_d-N_{d+1}\quad(d<H),
\qquad
\sum_vz_{v,H}=N_H.
\]

Without `x_(v,H+1)=0`, `z_(v,H)`, the one-hot property, and the radius-`H` count are incomplete.

For a one-hot labeling, the chosen cut-skeleton forest has

\[
p_d=n_d-
\#\{(X_t,X_{t+1}):
z_{X_t,d}=z_{X_{t+1},d}=1\}.
\]

Thus the same-label cut-path edges determine the component count of this chosen skeleton forest exactly.  They need not determine the globally optimized `p_d^*` if additional rotor arcs between labeled chains are available; those additional arcs can only improve the toll.

The unproved cut-path lemma must retain the joint quantifiers

\[
\exists(F,x):
\quad F\hbox{ is one exact odd factor},
\quad x\hbox{ satisfies every two-sided nested equation},
\quad \Phi(F,x)=o(W).
\]

Bare nested feasibility, a separately constructed low-toll labeling, or independently optimized depthwise matchings do not suffice.

The optional anchoring `r(X_0)=0` on every cut path is arithmetically consistent because

\[
n_0=W-N_1=\frac{W}{m+1}=B.
\]

Conditional on that anchoring, the upper depth-one map is indeed the edge-union bijection

\[
U_1(X_t)=X_{t-1}\cup X_t,
\qquad1\le t\le m.
\]

It does not make the lower depth-one map injective; that remains the first genuine rainbow constraint.

## 5. Exact fixed-coordinate-matching obstruction

Fix one perfect matching `Pcal` of the `2m` coordinates.  Consider selected rotor path forests such that every selected rotor arc uses one pair of this same global matching.

For a rank-`m-q` target having `f` full pairs, `f+q` empty pairs, and `m-2f-q` split pairs, the number of targets is

\[
T_{f,q}
=\frac{m!}{f!(f+q)!(m-2f-q)!}
 2^{m-2f-q}.
\]

The number of middle starts with `f` full pairs, `f` empty pairs, and `m-2f` split pairs is

\[
V_f
=\frac{m!}{f!^2(m-2f)!}
 2^{m-2f}.
\]

Let

\[
D_{m,q}=\sum_f(T_{f,q}-V_f)_+.
\]

### Theorem 5.1

For every such fixed-frame forest and every `1<=q<=H`,

\[
\boxed{qP_q\ge D_{m,q}.}
\]

### Proof

Across classes `d>=q`, the path forests contain `N_q` vertices and `P_q` path components.  A component on `t` vertices has `(t-q)_+` starts followed by `q` selected arcs.  Therefore the number of such starts is at least

\[
\sum_i(t_i-q)=N_q-qP_q.
\]

Along `q` consecutive rotor transitions in a radius class `d>=q`, the inserted endpoint of a used fixed pair remains in the rotor state word long enough to prevent that pair from being reused.  Hence the `q` arcs use `q` distinct pairs of `Pcal`.  The corresponding lower depth-`q` member is a `q`-face shadow: it empties those `q` split pairs and preserves the number `f` of full pairs.

These starts have distinct lower members because they are members of one SCD and each chain is used at most once as a start.  Type `f` supplies at most `V_f` starts and has only `T_(f,q)` possible targets, so at most `min(V_f,T_(f,q))` distinct targets of that type can arise.  Thus

\[
N_q-qP_q
\le\sum_f\min(V_f,T_{f,q})
=N_q-D_{m,q},
\]

which proves the theorem.

This obstruction is one-sided; the lower layer already suffices.  Complementation gives the analogous upper statement.

## 6. Gaussian type-capacity calculation

The numerical constant in the report is correct, but the probability law attached to `X` must be repaired.

Let

\[
\mathbb P_V(F=f)=\frac{V_f}{W},
\qquad
\mathbb P_{T,q}(F=f)=\frac{T_{f,q}}{N_q}.
\]

For

\[
q=x\sqrt m+o(\sqrt m),\qquad
X_m=\frac{F-m/4}{\sqrt m},
\]

the two local central limit laws are

\[
X_m\Rightarrow N(0,1/16)
\quad\hbox{under }\mathbb P_V,
\]

and

\[
X_m\Rightarrow N(-x/2,1/16)
\quad\hbox{under }\mathbb P_{T,q}.
\]

The target saddle is

\[
f_*=\frac m4-\frac q2+\frac{q^2}{4m}+O(1),
\]

whereas the middle-source center is `m/4+O(1)`.

The exact likelihood ratio is

\[
\frac{T_{f,q}}{V_f}
=\prod_{i=0}^{q-1}
 \frac{m-2f-i}{2(f+1+i)}.
\]

Uniformly for bounded `X` and `x` in a fixed compact subinterval of `(0,infinity)`,

\[
\log\frac{T_{f,q}}{V_f}
=-8xX-3x^2+o(1).
\]

The ratio is decreasing in `f` and crosses one at

\[
X=-\frac{3x}{8}+o(1).
\]

Therefore

\[
\begin{aligned}
\frac{D_{m,q}}W
&=\frac{N_q}{W}
  \mathbb P_{T,q}
  \left(X_m\le-\frac{3x}{8}+o(1)\right)
 -\mathbb P_V
  \left(X_m\le-\frac{3x}{8}+o(1)\right)\\
&\longrightarrow
e^{-x^2}\Phi_{\rm G}(x/2)
-\Phi_{\rm G}(-3x/2).
\end{aligned}
\]

Equivalently, if

\[
\Delta(x)
=\Phi_{\rm G}(x/2)
-e^{x^2}\Phi_{\rm G}(-3x/2),
\]

then

\[
\boxed{
\frac{D_{m,q}}W
\longrightarrow
e^{-x^2}\Delta(x).
}
\]

This quantity is positive for every `x>0`.  The convergence is uniform for

\[
a\le q/\sqrt m\le A
\]

with fixed `0<a<A`; that uniformity, or an equivalent uniform lower bound, is required before replacing the sum by a Riemann integral.

Combining Theorem 5.1 with

\[
\Phi=P_0+2\sum_{q=1}^HP_q
\]

gives

\[
\liminf_{m\to\infty}\frac\Phi W
\ge
2\int_a^A
\frac{e^{-x^2}\Delta(x)}x\,dx.
\]

The report's displayed integral is therefore correct.  Since

\[
\frac{e^{-x^2}\Delta(x)}x
\longrightarrow\sqrt{\frac2\pi}
\quad(x\downarrow0),
\]

one may let `a` decrease to zero and write the sharper constant

\[
\boxed{
\kappa_A
=2\int_0^A
\frac{e^{-x^2}\Delta(x)}x\,dx>0,
\qquad
\liminf\frac\Phi W\ge\kappa_A.
}
\]

This is an `Omega_A(W)` bound: the positive constant depends on the fixed window parameter `A`.

The report's line

\[
X\Rightarrow N(-x/2,1/16)
\]

is thus correct only when explicitly attributed to the normalized target law `T_(f,q)/N_q`.  Under the source weights `V_f/W`, the limiting mean is zero.

## 7. Correction to the sparse-surgery claim

The pure fixed-frame theorem does not rule out every `o(W)` family of exceptional arcs.

Suppose `s_q` selected arcs among the radius classes `d>=q` do not use pairs of the fixed matching.  A single exceptional arc lies in at most `q` length-`q` path windows.  Hence at least

\[
N_q-qP_q-qs_q
\]

of the `q`-window starts remain pure fixed-frame windows.  Applying the same type-capacity bound to those pure starts gives

\[
\boxed{
q(P_q+s_q)\ge D_{m,q}.
}
\]

At `q=x sqrt(m)` with fixed `x>0`, `D_(m,q)=Theta_x(W)`.  Moreover,

\[
\Phi\ge 2\sum_{j=1}^qP_j\ge2qP_q,
\]

so `Phi=o(W)` forces `P_q=o(W/sqrt(m))`.  The exceptional-window inequality therefore requires

\[
s_q=\Omega_x(W/\sqrt m).
\]

Equivalently, `Omega_x(W)` length-`q` window starts must contain an exceptional arc.  But only `Omega_x(W/sqrt(m))` exceptional arcs are forced, because one arc can contaminate up to `q=Theta(sqrt(m))` starts.

Therefore the report's sentence

> sparse surgery cannot repair them: a linear number of centers must be rebundled

is valid only if "centers" means the affected `q`-window starts or owner flags.  It is false if interpreted as requiring `Omega(W)` exceptional rotor arcs or block edits.  The safe statement is:

> `o(W/sqrt(m))` exceptional-arc surgery cannot repair a fixed-frame forest; any low-toll repair must mix `Omega_A(W)` Gaussian-window starts, which may be caused by only `Omega_A(W/sqrt(m))` exceptional arcs.

The fixed-pair obstruction applies exactly when all selected arcs use one global matching.  It excludes the native Bender--Knuth and stationary pair-coordinate constructions only to the extent that their usable forest arcs are proved to stay in that one frame.  It does not exclude cellwise-changing pair frames, phase-dependent mixed frames, or a recursion that deliberately introduces the exceptional arcs just quantified.

## 8. Implication scope

The report's final nonimplications are correct, with one additional distinction.

### General rotor/SCD theorem

For every fixed `A`, the general sufficient statement is

\[
\exists\hbox{ one full integral SCD }\mathcal D_{m,A}:
\quad
\Phi_{\min}(\mathcal D_{m,A})=o(W).
\]

The ordered-Hall formula exactly characterizes its classwise path-forest statistic.

### Cut-path sufficient sublemma

The cut-odd-wreath nested-shadow lemma asks for one exact odd factor and one radius labeling which simultaneously has two-sided nested shadow bijections and `o(W)` cut-run toll.  It implies the general theorem after band extension, but it is not necessary for `RSCD_A`: another band SCD may have small ordered-Hall toll without arising from a cut odd factor.

Thus the final boxed phrase "one integral nested two-sided shadow matching" is the missing theorem for the cut-skeleton sublane, not a logically equivalent description of all possible rotor/SCD solutions.

### OR implication

For one fixed `A`, `RSCD_A` gives a central-band literal word of length `W+o(W)`.  Adding the audited tails yields

\[
\limsup_{m\to\infty}
\frac{\nu(2m)}W
\le
1+O\bigl((1+A^2)e^{-A^2}\bigr).
\]

Proving `RSCD_A` for every fixed `A`, and then choosing `A` arbitrarily large before taking `m` large, gives coefficient one in even dimension.  The standard trimmed lift then gives odd dimension.

This is a direct literal-word route.  It does not prove fixed-window overload MWB, odd labelled `CA_A`, labelled synchronization, or any overload-to-labelled converse.  Conversely, the contiguous-OR conjecture could hold through a nonrotor or cross-radius architecture even if `RSCD_A` failed.  The ordered-Hall statistic is necessary and sufficient only inside the defined classwise rotor path-forest architecture.

## 9. Corrected theorem ledger

### Accepted as proved

1. Every saturated central-band SCD extends integrally to a full SCD, embedding every band chain unchanged inside its extension.
2. For a fixed radius digraph, the split-copy ordered-Hall formula gives the exact minimum number of path-forest components.
3. For one fixed integral SCD, the optimized toll is the weighted sum of the independently optimized radius-class deficiencies.
4. The identity `Phi=P_0+2 sum_(q>=1)P_q` is exact.
5. Cutting an exact odd factor supplies legal rotor chronology and an unconstrained radius labeling with formal toll `o(W)`.
6. A pure one-global-matching rotor forest has toll at least `kappa_A W-o(W)`, with the explicit `kappa_A>0` above.

### Mandatory repairs or qualifications

1. Define Hall neighborhoods in the split right copy and retain the quantifier order `min_prec max_S`.
2. Fix the common SCD before optimizing any radius class.
3. Use the ordinary swap at radius zero.
4. Add `x_(v,H+1)=0` to the nested system.
5. Attribute `N(0,1/16)` to the middle-source law and `N(-x/2,1/16)` to the target law.
6. Require compact-uniform Gaussian estimates before the Riemann-sum passage.
7. Replace the `Omega(W)` exceptional-arc surgery claim by `Omega_A(W/sqrt(m))`; `Omega_A(W)` applies to contaminated `q`-window starts.
8. Treat the cut-path nested-shadow theorem as sufficient, not equivalent, for general `RSCD_A`.
9. Keep the direct even-word implication separate from odd MWB and labelled synchronization.

### Still unproved

* For the general lane: one full integral SCD with `Phi_min=o(W)` in every fixed Gaussian window.
* For the cut skeleton: one jointly chosen integral radius labeling satisfying every lower and upper shadow equation and having `o(W)` same-label run toll.
* For any attempted repair of the fixed-pair constructions: a mixed-frame expansion or absorption theorem beyond the quantified `Omega_A(W/sqrt(m))` exceptional-arc threshold.

The report is therefore substantially correct after these repairs.  Its decisive open step remains integral, jointly multidepth, two-sided, and support-feasible; neither the ordered-Hall reformulation nor the Gaussian obstruction supplies that missing construction.
