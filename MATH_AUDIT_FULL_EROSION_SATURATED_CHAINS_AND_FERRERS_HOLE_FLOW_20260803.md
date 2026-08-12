# Independent audit: full erosion, Ferrers holes, and triangular inversion

**Date:** 2026-08-03  
**Audited source:** MATH_THEOREM_FULL_EROSION_SATURATED_CHAINS_AND_FERRERS_HOLE_FLOW_20260803.md  
**Audited source SHA-256:** fd32c23229cefda74f1b729833fb2fd1d2d5b25bb25cff029a48c8a01f6b8ad6  
**Verdict:** **PASS after three proof-safety corrections.**  The source now
states completeness explicitly, supplies the previously implicit union step
in the maximal-aperture identity, and distinguishes aggregate row totals
from individual cell ranks and named-target assignment.  No computation is
used in this audit.

## 1. Scope

The theorem is correct for

\[
 1\le d<r<k,\qquad W={k\choose r},
\]

and a complete cyclic rank-\(r\) Johnson carrier

\[
 T_{i+1}=T_i-\{\alpha_i\}+\{\beta_i\}
\]

whose positive coordinate runs have length at least \(d+1\).  Completeness
is needed for the universal lower-ideal comparison and also excludes a
coordinate which is present around the entire carrier.  The local erosion
identities themselves need only the Johnson and residence hypotheses,
provided all-cyclic coordinate runs are treated separately.

## 2. Exact full-erosion formulas

Fix a coordinate \(x\).  A positive owner run \([a,b]\) of \(x\) contributes
the erosion run

\[
 [a+d,b].
\]

Indeed, a source position \(h\) can contain \(x\) exactly when all owners
\(T_{h-d},\ldots,T_h\) contain it.  Therefore

\[
 E_h=\bigcap_{i=h-d}^{h}T_i.
\]

For an owner interval \([u,j]\) of at most \(d+1\) owners,

\[
 \bigcap_{i=u}^{j}T_i
 =T_j\setminus\{\beta_u,\ldots,\beta_{j-1}\}.
\]

The displayed arrivals are distinct: two equal arrivals inside at most
\(d\) transitions would enclose a positive run of length at most \(d\).
At \(u=h-d\), this gives

\[
 E_h=T_h\setminus\{\beta_{h-d},\ldots,\beta_{h-1}\},
\qquad |E_h|=r-d.
\]

Sliding one position gives the strict Johnson recurrence

\[
 E_{h+1}=E_h-\{\alpha_h\}+\{\beta_{h-d}\}.
\]

Residence guarantees that \(\alpha_h\in E_h\), that
\(\beta_{h-d}\in E_{h+1}\), and that they are distinct.  Iterating the
recurrence from \(h=j\) to \(j+q-1\) yields

\[
\begin{aligned}
 C^*_{j,q}
 &=\bigcup_{h=j}^{j+q-1}E_h\\
 &=T_j\setminus
   \{\beta_{j+q-1-d},\ldots,\beta_{j-1}\}\\
 &=\bigcap_{i=j+q-1-d}^{j}T_i,
\end{aligned}
\]

and hence

\[
 |C^*_{j,q}|=r-d+q-1.
\]

For fixed \(j\),

\[
 C^*_{j,q+1}
 =C^*_{j,q}\cup\{\beta_{j+q-1-d}\},
\]

so the column is a saturated chain.  For fixed \(q\),

\[
 C^*_{j+1,q}
 =C^*_{j,q}-\{\alpha_j\}
              +\{\beta_{j+q-1-d}\},
\]

so the row is a strict rank-\((r-d+q-1)\) Johnson walk.  All indices and
off-by-one counts check.

## 3. Unavoidable defect and the Gaussian constant

The cyclic full factor has no short cell below rank \(r-d\).  A linear
opening has only

\[
 \sum_{q=1}^{d}(d-q+1)={d+1\choose2}
\]

additional short cells.  Even if every such boundary cell is assigned an
arbitrary missing value, the lower-compiler defect is at least

\[
 \left[
 \sum_{s=1}^{r-d-1}{k\choose s}-{d+1\choose2}
 \right]_+.
\]

For \(r=\lceil k/2\rceil\),

\[
 \frac d{\sqrt{k}}\longrightarrow\sqrt{\frac{\pi}{8}}.
\]

If \(X_k\sim\operatorname{Bin}(k,\tfrac12)\), then

\[
 \frac{r-d-1-k/2}{\sqrt{k}/2}
 \longrightarrow-\sqrt{\frac{\pi}{2}},
\]

while the strict lower ideal has asymptotic mass \(1/2\).  The polynomial
boundary allowance is negligible.  Therefore the omitted proportion tends
to

\[
 \frac{\Phi(-\sqrt{\pi/2})}{1/2}
 =2\Phi(-\sqrt{\pi/2})=0.210\ldots .
\]

This is a lower bound on named-target defect.  Additional collisions or
nonsurjectivity inside the represented rank band can only increase it.

## 4. Zero blocks and Ferrers triangles

Inside one erosion run \(R=[u,v]\), a factor is specified by retained
positions containing \(u,v\) and having consecutive gaps at most \(d+1\).
Equivalently its deleted positions form disjoint internal hole blocks of
length at most \(d\), separated by retained positions.

For a length-\(\ell\) hole block \(B\), coordinate \(x\) disappears from
the \(q\)-cell starting at \(j\) exactly when

\[
 [j,j+q-1]\subseteq B.
\]

Thus its footprint is the Ferrers triangle

\[
 \mathcal F(B)
 =\{(j,q):[j,j+q-1]\subseteq B,\ 1\le q\le\ell\}.
\]

It has \(\ell-q+1\) cells in row \(q\) and
\({\ell+1\choose2}\) cells in total.  Distinct erosion runs of one
coordinate are separated by more than \(d\) source positions, so a short
cell cannot meet two such runs.  This makes the deletion count literal,
not an inclusion-exclusion approximation.

Let \(N_\ell\) be the number of length-\(\ell\) blocks and let

\[
 \Delta_q=(r-d+q-1)W-\sum_j|C_{j,q}(A)|.
\]

Then exactly

\[
 \Delta_q=\sum_{\ell=q}^{d}(\ell-q+1)N_\ell,
\qquad
 N_q=\Delta_q-2\Delta_{q+1}+\Delta_{q+2},
\]

with \(\Delta_{d+1}=\Delta_{d+2}=0\).  Hence the aggregate deficit is
nonnegative, nonincreasing, and discretely convex.

This inversion is only the aggregate rank-mass statement.  Literal
placement additionally requires counts \(n_{R,\ell}\) satisfying

\[
 \sum_Rn_{R,\ell}=N_\ell,\qquad
 \sum_{\ell=1}^{d}(\ell+1)n_{R,\ell}\le n_R-1
\]

for every erosion run of length \(n_R\).  The inequality is exact: hole
length plus one retained separator per hole must fit between the two
retained endpoints.  It is also sufficient by laying the blocks in order.

Neither aggregate inversion nor placement assigns named Boolean targets.
Named assignment is a third, global coupling problem.

## 5. Path-flow and nonintegrality scope

On one erosion run, list retained positions as a path whose arcs have
length at most \(d+1\).  An arc \(a\to b\) creates the hole
\([a+1,b-1]\).  Its additive deletion weight is exactly the sum over the
Ferrers triangle contained in that hole.  Valid schedules are therefore
in bijection with one-unit paths in an acyclic graph, so every separable
one-coordinate schedule problem is integral.

This does not imply integrality after named-target variables are coupled
across coordinates.  Once a complete signature is fixed, target allocation
is an ordinary bipartite/star matching.  Before signatures are fixed, the
literal depth-three odd cover cycle gives a genuine fractional gap in the
combined occurrence/assignment formulation.  The theorem correctly limits
its network-flow claim to the per-coordinate schedule product and does not
claim a TU theorem for the global compiler.

## 6. Final boundary

The audited theorem proves

\[
\boxed{
\text{full erosion = saturated rank columns}
\quad+\quad
\text{all other factors = integral Ferrers-hole paths}
}
\]

and proves that full erosion itself misses a positive asymptotic fraction
of the strict lower ideal.  It does **not** prove that an aggregate
Ferrers profile is physically placeable unless the run inequalities hold,
and it does **not** prove that any placeable profile covers the required
named targets.
