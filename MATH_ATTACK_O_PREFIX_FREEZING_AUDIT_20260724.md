# Cross-audit of Lane O: prefix freezing

Date: 2026-07-24

Audited source: `MATH_ATTACK_O_PREFIX_FREEZING_REPORT_RAW_20260724.md`.

## Overall verdict

The core result is **valid at the integral nested-Boolean-owner level**, after two necessary statement corrections and several scope qualifications.

1. The residual-flow theorem is valid, and `(U)` and `(L)` have the correct signs and are jointly sufficient. The network must explicitly impose terminal demand `R_K`, equivalently through a fixed return arc of value `R_K`; residual node-capacity arcs occur only at layers `1,...,K`, not at layer `0`.
2. The record-max lower bound is valid. In `O_q(L) <= e_q(L,Q) <= R_q`, the upper bound holds only when `Q` respects every frozen prefix. It is false for an arbitrary balanced resolution.
3. The rank-one construction, independent-set argument, overload and labelled calculations, exact minimum prefix cost, and asymptotic constants are valid.
4. Strict separation from labelled synchronization is proved only for arbitrary integral Boolean owner systems. It is not proved for exact wreath factors, `SYNC`, `CA_A`, or MWB.

## 1. Precise residual network

Fix the nested owner system `L` and stopping depths `a(X)`. Define

\[
g_q(S)=\#\{X:a(X)\ge q,\ L_q(X)=S\},
\qquad
\sigma_q(S)=\#\{X:a(X)=q,\ L_q(X)=S\}
\]

for `q<K`, and

\[
R_q=\sum_{j<q}\sigma_j(V_j)=\#\{X:a(X)<q\}.
\]

For `1<=q<=K`, put

\[
\ell_q(S)=(c_q-g_q(S))_+,
\qquad
u_q(S)=c_q+1-g_q(S),
\]

assuming `g_q(S)<=c_q+1`. Layer zero has no residual occupancy before its supplies are released, so `ell_0,u_0` are not used.

If `r_q(S)` is residual occupancy and `y_q(S,T)` is flow on the Boolean cover \(S\supset T\), the exact equations are

\[
\sum_{T\lessdot S}y_0(S,T)=\sigma_0(S),
\]

\[
r_q(S)=\sum_{U\gtrdot S}y_{q-1}(U,S),
\qquad
\sum_{T\lessdot S}y_q(S,T)=r_q(S)+\sigma_q(S)
\quad(1\le q<K),
\]

and

\[
r_K(S)=\sum_{U\gtrdot S}y_{K-1}(U,S),
\qquad
\ell_q(S)\le r_q(S)\le u_q(S).
\]

Conservation gives `r_q(V_q)=R_q`. Since `g_q(V_q)=W-R_q`, the completed load has total `W`; no separate layer-total constraint is missing.

The correct split circulation contains:

- post-only nodes at layer zero and pre/post nodes at layers `1,...,K`;
- arcs `pre(q,S) -> post(q,S)` with bounds `[ell_q(S),u_q(S)]`;
- unbounded Boolean arcs from post-layer `q` to pre-layer `q+1`;
- fixed arcs from a source `s` into `post(q,S)` of value `sigma_q(S)`;
- unbounded arcs from layer-`K` posts to a terminal `t`;
- the fixed return arc

  \[
  t\longrightarrow s\quad[R_K,R_K].
  \]

The return arc, or the equivalent terminal imbalance `-R_K`, is essential. The source report's phrase "drain layer `K` to one sink" is under-specified without it.

**Network verdict:** **CORRECTED**, with no change to the intended feasible-flow object.

## 2. Hoffman cuts

For a Hoffman cut, let `B_q` be its layer-`q` post-nodes, `P_q` its layer-`q` pre-nodes, and

\[
C_q=\partial B_{q-1}.
\]

Finite capacity forces \(P_q\supseteq C_q\). Before optimizing pre-node membership, Hoffman is

\[
\sum_{q<K}\sigma_q(B_q)
+\sum_{q=1}^{K}\ell_q(B_q\setminus P_q)
\le
\mathbf1_{\{t\text{ is in the cut}\}}R_K
+\sum_{q=1}^{K}u_q(P_q\setminus B_q).
\tag{2.1}
\]

For fixed `B_q,C_q`, the strongest intermediate choice is `P_q=C_q`.

If `t` is outside the cut, no terminal post-node is in the cut and `P_K=C_K`; (2.1) becomes exactly

\[
\sum_{q<K}\sigma_q(B_q)
+\sum_{q=1}^{K-1}\ell_q(B_q\setminus C_q)
\le
\sum_{q=1}^{K-1}u_q(C_q\setminus B_q)+u_K(C_K).
\tag{U}
\]

If `t` is inside, the strongest terminal choice includes every layer-`K` post-node and takes `P_K=C_K`; this gives exactly

\[
\sum_{q<K}\sigma_q(B_q)
+\sum_{q=1}^{K-1}\ell_q(B_q\setminus C_q)
+\ell_K(V_K\setminus C_K)
\le
R_K+\sum_{q=1}^{K-1}u_q(C_q\setminus B_q).
\tag{L}
\]

Cuts containing the source give the complementary forms of these inequalities because total injected supply is `R_K`. Thus `(U)` and `(L)` are complete.

For `K=1`, they reduce to

\[
\sigma_0(B_0)\le u_1(\partial B_0)
\]

and

\[
\ell_1(V_1\setminus\partial B_0)
\le\sigma_0(V_0\setminus B_0).
\]

Both signs are correct.

Taking suitable all/full staircases recovers all aggregate constraints, including

\[
\ell_q(V_q)\le R_q\le u_q(V_q).
\]

**Cut verdict:** **VALID** without algebraic correction.

For `1<=q<K`, the adjacent necessary cut

\[
\ell_{q+1}(\mathcal B)
\le u_q(N(\mathcal B))+\sigma_q(N(\mathcal B))
\]

is valid. For `q=0`, residual layer-zero occupancy is zero, and the correct sharper inequality is

\[
\ell_1(\mathcal B)\le\sigma_0(N(\mathcal B)).
\]

General adjacent feasibility does not replace multilevel staircase cuts. A strict irredundancy assertion restricted to the special `(g,sigma)` arising from actual stopping depths is not separately demonstrated in the report and is therefore **UNSUPPORTED** in that stronger reading.

## 3. Integrality

All bounds, injections, and demands are integral. The unprojected constraint matrix is the directed node-arc incidence matrix of the split network and is totally unimodular. Hence real feasibility implies integral feasibility.

Unbounded arcs may be capped at `R_K`, since no layer carries more flow. Integral path decomposition assigns suffix paths to individual released owners; concatenating them to frozen prefixes preserves roots and Boolean nesting.

**Integrality verdict:** **VALID.** Total unimodularity is a property of the split network, not an asserted property of the projected staircase inequalities.

## 4. Record-max lower bound

Tonelli summation gives

\[
\sum_X\Psi_{m,K}(a(X))
=\sum_{q=1}^{K}\frac{R_q}{c_q}.
\tag{4.1}
\]

An admissible completion `Q` must satisfy

\[
Q_q(X)=L_q(X)\qquad(q\le a(X)).
\tag{4.2}
\]

For every balanced `Q`, histogram coupling gives `O_q(L)<=e_q(L,Q)`. For a `Q` satisfying (4.2), only owners released before `q` may differ, so

\[
e_q(L,Q)\le R_q.
\]

This is the necessary quantifier correction to the source report.

Since `R_q` is nondecreasing,

\[
R_q\ge M_q:=\max_{s\le q}O_s(L),
\]

and therefore

\[
\boxed{
\sum_X\Psi_{m,K}(a(X))
\ge\sum_{q=1}^{K}\frac{M_q}{c_q}.
}
\tag{RM}
\]

The record decomposition

\[
\sum_{q=1}^{K}\frac{M_q}{c_q}
=\sum_{s=1}^{K}(M_s-M_{s-1})
\sum_{q=s}^{K}\frac1{c_q}
\]

is exact.

For `K=ceil(A sqrt(m))`, fixed `A>0`, and `c_q<=C_A`,

\[
\max_{q\le K/2}O_q(L)
\le\frac{2C_A}{K}
\sum_X\Psi_{m,K}(a(X)).
\]

Thus `o(W)` prefix cost forces `O_q=o(W/sqrt(m))` uniformly for `q<=K/2`. For a general window the analogous rate is `o(W/K)` after inserting the relevant capacity bound.

Fixed-window MWB is the weighted-sum condition, not merely the collection of pointwise assertions `O_q=o(W)`.

**Record-bound verdict:** **VALID AFTER QUANTIFIER AND UNIFORMITY CORRECTIONS.**

## 5. Rank-one counterexample

At depth one,

\[
c_1=1,
\qquad
\frac{W}{N_1}=\frac{m+2}{m}.
\]

Thus a balanced `P` has load one or two. The exact number of low targets is

\[
v=2N_1-W=N_1\left(1-\frac2m\right).
\]

For each low target `S`, swap the first two distinct deletion letters of its unique owner. The new target `A_S` is different from `S`, and the path rejoins `P` at depth two.

On the low targets, join `S` to `A_S` whenever `A_S` is low. The resulting simple graph has at most `v` edges. Caro--Wei and Jensen give

\[
\alpha(G)
\ge\frac{v^2}{v+2e(G)}
\ge\frac v3.
\]

For large `m`, this contains an independent set of size

\[
R=\left\lfloor\frac{N_1}{\sqrt m}\right\rfloor.
\]

Swapping those owners makes every selected low target empty, and independence prevents any selected target from receiving a selected owner. Therefore

\[
D_1^-=R.
\]

Only selected targets lose occurrences, while total gain is `R`, so `D_1^+<=R`. The exact identity `O_1=max(D_1^-,D_1^+)` yields

\[
O_1(L)=R.
\]

All paths rejoin at depth two, hence

\[
O_q(L)=0\quad(q\ge2),
\qquad
e_1(L,P)=R,
\qquad
e_q(L,P)=0\quad(q\ge2).
\]

The minimum labelled objective is also `R`: every balanced `Q` has `e_1>=O_1=R`, while `P` attains it.

Since `M_q=R` for every `q>=1`, `(RM)` proves

\[
\text{prefix cost}\ge R\sum_{q=1}^{K}\frac1{c_q}.
\]

Stop exactly the selected owners at depth zero, freeze all others through `K`, and route the selected owners along their `P` paths. This integral completion is `P` and attains equality. Thus

\[
\boxed{
\min\text{ permanent-prefix cost}
=R\sum_{q=1}^{K}\frac1{c_q}.
}
\]

The same witness proves that all residual Hoffman cuts are feasible.

**Counterexample verdict:** **VALID.**

## 6. Asymptotic constants

Exactly,

\[
\frac{W}{N_q}
=\prod_{i=0}^{q-1}\frac{m+2+i}{m-i}.
\]

Therefore

\[
\log\frac{W}{N_q}
\le\frac{q(q+1)}{m-q+1}.
\]

For fixed `A`, `K=ceil(A sqrt(m))`, and large `m`, this is at most `2(A+1)(A+2)`. Hence

\[
c_q\le C_A:=\exp(2(A+1)(A+2)).
\]

Also

\[
R\sim\frac{N_1}{\sqrt m}\sim\frac W{\sqrt m},
\qquad
R\ge\frac{W}{2\sqrt m}
\]

eventually. Consequently

\[
\frac{A}{2C_A}W
\le R\sum_{q=1}^{K}\frac1{c_q}
\le R\,K=O_A(W).
\]

Thus the exact minimum is `Theta_A(W)`.

**Asymptotic verdict:** **VALID**, for fixed `A>0` and sufficiently large `m`.

## 7. Logical scope

### Valid conclusions

At the level of arbitrary integral nested Boolean owner systems, the example proves:

- small fixed-window overload does not imply low permanent-prefix cost;
- even labelled mismatch `R=o(W)` need not imply low permanent-prefix cost;
- satisfying every residual Hoffman cut and integrality does not remove the obstruction;
- irreversible release charges a rank-isolated repair throughout the remaining window;
- for the same owner system used by a permanent-prefix scheme, low cost requires

  \[
  \sum_{q\le K}
  \frac{\max_{s\le q}O_s(L)}{c_q}=o(W).
  \]

### Corrected scope

"Prefix freezing is strictly stronger than labelled synchronization" is valid only pointwise/asymptotically in the Boolean-owner class. It is **UNSUPPORTED** as a strict separation of the existential exact-factor theorems.

The record-max condition is necessary only for permanent-prefix freezing applied to the same owner system or oriented exact factor. It is not necessary for `CA_A`, `SYNC`, MWB, adjacent rank-isolated swaps, or any repair that permits later resynchronization.

The record inequality itself is Boolean, not intrinsically wreath-specific. Wreath specificity would enter through constructing an exact factor that satisfies it and admits a low-cost stop vector satisfying every staircase cut.

### Missing exact-factor constraints

An oriented exact wreath factor satisfies the point-margin identity

\[
\sum_{S\ni x}\mu_q(S)=\frac{(m-q)W}{n}
\qquad\text{for every }x,q,
\]

and bundles its owners into `W/n` cyclic orders. The construction checks neither property: `P` is an arbitrary balanced resolution, independent rank-one swaps may change coordinate margins, and no cyclic bundling is supplied.

Thus the exact-factor caveat is substantive.

### What is not ruled out

The audit finds no counterexample to:

- exact-factor prefix freezing;
- labelled `SYNC` or `CA_A`;
- unlabelled MWB;
- the contiguous-OR theorem;
- adjacent-swap or other rank-isolated repair;
- release followed by re-freezing;
- a wreath-specific theorem forcing small record maxima.

The phrase "no theorem using only" the Boolean hypotheses can succeed is valid only as a countermodel statement: those hypotheses alone do not logically imply low permanent-prefix cost. It says nothing about arguments using additional point-margin, cyclic-bundling, exact-factor, or transport structure.

## Final ledger

### Valid

- `(U)`, `(L)`, and their `K=1` signs.
- Integral feasibility once all staircase cuts pass.
- The cost identity, `(RM)`, and record decomposition.
- The rank-one graph construction and overload calculation.
- The exact minimum prefix cost.
- The explicit `C_A` and `Theta_A(W)` bounds.
- The Boolean-level irreversible-release obstruction.

### Corrected

- Add the fixed terminal demand/return arc `R_K`.
- Use residual capacity arcs only at layers `1,...,K`.
- Restrict `e_q<=R_q` to completions respecting frozen prefixes.
- Remove `u_0` from the `q=0` adjacent cut.
- State the `o(W/sqrt(m))` rate uniformly for fixed `A`.
- Restrict strictness and record-max necessity to the permanent-prefix architecture.

### Unsupported

- Any reading as an exact-wreath-factor counterexample.
- Any separation of existential `SYNC`, `CA_A`, or MWB.
- Necessity of the record-max condition for repairs that allow rejoining.
- Strict irredundancy of multilevel cuts inside the special stopping-depth subclass, absent a dedicated example.

With these corrections, Lane O is a rigorous negative theorem about irreversible Boolean prefix release, not a negative theorem about exact wreath factors or synchronization itself.
