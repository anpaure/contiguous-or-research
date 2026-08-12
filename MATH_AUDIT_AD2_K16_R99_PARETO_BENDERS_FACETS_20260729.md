# Independent audit of the radius-99 unique-provider Pareto and Benders facets

Date: 2026-07-29  
Lane: AD2 independent audit  
Computation scope: solver-free exact enumeration only; no SAT, CP-SAT, ILP, or remote job was run

## 1. Verdict

The corrected program

`scratch/audit_k16_r99_unique_provider_pareto_20260729.py`

at SHA-256

`558901cdc213a11b78f8616877a56e7a52d9019e0f59294656a39ab5362e854d`

is mathematically sound for its stated two-dimensional unique-provider-loss projection. In particular:

1. the delete branch now enforces every `required_edge_ids` field, including edge 22511 in component 5;
2. the complete Pareto frontiers are exactly the displayed frontiers below;
3. the diagonal bounds 113 and 111, and hence the cheap double-repair bounds 14 and 12, are valid;
4. the fixed seam censuses are
   \[
   |A_L|=23552,
   \quad |A_U|=23483,
   \quad |A_L\cap A_U|=20787;
   \]
5. the intersection has 2727 cross seams and 18060 same-shore seams;
6. the delete frontier has one additional nonredundant monotone-convex-hull facet,
   \[
   L+2U\ge160.
   \]

There is one harmless naming caveat. The audited program's field `pareto_state_count_before_final_prune`, equal to 54 and 87, counts states after safe per-grade dominance pruning. It is not the number of all reachable loss pairs. The independent unpruned counts are 1629 and 1817. This does not affect the Pareto frontier or any stated minimum.

## 2. Frozen objects and notation

Let \(S\) be the 858-edge source factor in

`scratch/k16_dynamic_cross_r147_round0_seed16822_20260729.json`,

SHA-256

`d1662b09981bbfe3fbd25e46bad045c628407eda9d1c52936ca39c721151a7c8`.

The exact cut-space certificate is

`scratch/threadD_k16_r99_cutspace_scope_20260729.audit.json`,

SHA-256

`b1b069fe61a871fea0c6929cd44dc88bbde0d5f68de77a6b1a7d22a82c6c642e`.

It has 147 current residence motifs, 85 edge-overlap components, a 390-edge motif union, and 468 exterior source edges. The two radius-99 branches are:

- `RETAIN_22511`: edge 22511 is not cut, local base 98, excess budget 1;
- `DELETE_AND_REPLACE_22511`: edge 22511 is cut, local base 97, excess budget 2.

For a source edge \(e\), define

\[
w_L(e)=
\begin{cases}
1,&\text{if }e\text{ is the sole selected source provider of its lower }q1\text{ colour},\\
0,&\text{otherwise},
\end{cases}
\]

and define \(w_U(e)\) analogously. For a cut \(D\subseteq S\), put

\[
L(D)=\sum_{e\in D}w_L(e),
\qquad
U(D)=\sum_{e\in D}w_U(e).
\]

The source has 675 sole-provider lower colours and 673 sole-provider upper colours. Its edge-weight histogram is

\[
\#(w_L,w_U)=(00:32,\ 01:151,\ 10:153,\ 11:522).
\]

Every quotient edge has one lower and one upper colour, so the sole-provider colours within either palette correspond injectively to their source edges. Consequently \(L(D)\) and \(U(D)\) are exactly additive.

## 3. Independent exact enumeration theorem

### Theorem 3.1 — complete unique-provider Pareto frontiers

Among all radius-99 motif-hitting source cuts in the retain branch, the coordinatewise minimal loss pairs are exactly

\[
\mathcal P_R=
\{(50+j,63-j):0\le j\le13\}.
\]

Among all radius-99 motif-hitting source cuts in the delete branch, they are exactly

\[
\mathcal P_D=
\{(49+j,62-j):0\le j\le13\}\cup\{(64,48)\}.
\]

The full numbers of reachable loss pairs, before any dominance pruning, are respectively 1629 and 1817.

#### Proof

Rebuild the 147 motifs from the frozen factor and connect two motifs precisely when they share a source edge. This gives 85 components. Distinct component edge unions are disjoint: a shared edge would itself join the two components. The 468 exterior source edges are disjoint from every component union.

In each component, enumerate every motif transversal of size

\[
\tau_i,\tau_i+1,\ldots,\tau_i+b,
\]

where \(b=1\) in the retain branch and \(b=2\) in the delete branch. In the component containing 22511, forbid 22511 in the retain branch and require 22511 in the delete branch. The aggregate exact local-option counts are

\[
\begin{array}{c|ccc}
\text{branch}&\text{grade }0&\text{grade }1&\text{grade }2\\ \hline
R&262&958&-\\
D&261&960&3442.
\end{array}
\]

Convolve the exact sets of local \((w_L,w_U)\)-sums while retaining the exact total excess grade. Then choose exactly the unused part of the excess budget from the 468 exterior edges. Because the component unions and exterior are disjoint, every admissible radius-99 cut has exactly one such decomposition, and every enumerated decomposition is an admissible radius-99 motif hitter in its declared branch.

The independent verifier retains all reachable loss pairs; it does not apply the dominance pruning used by the audited program. Direct coordinatewise minimization of the resulting 1629 and 1817 pairs gives exactly \(\mathcal P_R\) and \(\mathcal P_D\). This independently proves both completeness and attainability of every displayed frontier point. ∎

## 4. The corrected component-5 scope

The locked component is component 5, with motifs

\[
M_5=\{22511,22520\},
\qquad
M_{66}=\{22511,22692,25634\}.
\]

In the delete branch, `required_edge_ids` is exactly \(\{22511\}\). The corrected grade counts are

\[
1,3,3
\]

at excess grades \(0,1,2\). Specifically, the options are

\[
\begin{array}{c|l}
0&\{22511\}\\
1&\{22511,22520\},\{22511,22692\},\{22511,25634\}\\
2&\{22511,22520,22692\},\{22511,22520,25634\},
\{22511,22692,25634\}.
\end{array}
\]

If the required-edge test is deliberately omitted, the spurious options are

\[
\{22520,22692\},\quad
\{22520,25634\},\quad
\{22520,22692,25634\}.
\]

The first two have loss pair \((1,2)\), already represented at grade 1 by corrected options; the last has loss pair \((2,3)\), already represented at grade 2. Therefore the omission was a genuine branch-scope error, but it happened not to change the loss-pair DP or the final Pareto frontier. The independent verifier recomputed both complete global frontiers with and without the required-edge condition and found them equal.

In the corrected audited code, line 103 reads the required set and lines 111–112 enforce it together with motif hitting.

## 5. Exact monotone-convex-hull facets

Let

\[
K_R=\operatorname{conv}(\mathcal P_R)+\mathbb R_{\ge0}^2,
\qquad
K_D=\operatorname{conv}(\mathcal P_D)+\mathbb R_{\ge0}^2.
\]

These are the exact monotone convex hulls of the two aggregate loss projections. Removing collinear intermediate points gives

\[
\operatorname{vert}_{\min}(K_R)=\{(50,63),(63,50)\},
\]

and

\[
\operatorname{vert}_{\min}(K_D)=\{(49,62),(62,49),(64,48)\}.
\]

Thus the complete irredundant nonnegative-normal facet systems are

\[
K_R:\qquad
L\ge50,
\quad U\ge50,
\quad L+U\ge113,
\]

and

\[
K_D:\qquad
L\ge49,
\quad U\ge48,
\quad L+U\ge111,
\quad L+2U\ge160.
\]

The last delete inequality is the previously unstated facet. It is exposed by the adjacent hull vertices \((62,49)\) and \((64,48)\). It is not implied by the other three inequalities: the integer point \((63,48)\) satisfies those three and violates \(L+2U\ge160\).

These are facets only of the two-coordinate monotone loss projection. No full cut-polytope facet claim is made.

## 6. Fixed seam census

Let \(A\) be the set of all off-source loopless quotient seams. Independently rebuilding the complete catalogue gives

\[
|A|=26570.
\]

Let \(C_L^*\) and \(C_U^*\) be the global sets of source colours with a unique selected source provider, and define

\[
A_L=\{a\in A:\operatorname{lower}(a)\in C_L^*\},
\qquad
A_U=\{a\in A:\operatorname{upper}(a)\in C_U^*\}.
\]

The exact partition census is

\[
\begin{array}{c|r}
\text{set}&\text{size}\\ \hline
A_L&23552\\
A_U&23483\\
A_L\cap A_U&20787\\
A_L\setminus A_U&2765\\
A_U\setminus A_L&2696\\
A\setminus(A_L\cup A_U)&322.
\end{array}
\]

Within \(A_L\cap A_U\), 2727 seams are cross and 18060 are same-shore. The verifier also freezes SHA-256 digests of the three sorted edge-ID sets.

## 7. Exact aggregate Benders rows

Let \(x_e\in\{0,1\}\) indicate that source edge \(e\) is cut and let \(y_a\in\{0,1\}\) indicate that off-source seam \(a\) is added. Define

\[
L(x)=\sum_{e\in S}w_L(e)x_e,
\qquad
U(x)=\sum_{e\in S}w_U(e)x_e.
\]

For every unique lower colour \(c\), its individual q1 row is

\[
1-x_{e(c)}+\sum_{a:\operatorname{lower}(a)=c}y_a\ge1.
\]

Summing over all unique lower colours, and analogously over all unique upper colours, gives the exact joint aggregate rows

\[
\boxed{\sum_{a\in A_L}y_a\ge L(x)},
\qquad
\boxed{\sum_{a\in A_U}y_a\ge U(x)}.
\tag{7.1}
\]

They are redundant consequences of the individual q1 rows, but they expose the cut/seam coupling directly. Combining (7.1) with the branch facets yields the fixed seam rows

\[
\begin{array}{c|l}
R& y(A_L)\ge50,\ y(A_U)\ge50,\ y(A_L)+y(A_U)\ge113,\\[2mm]
D& y(A_L)\ge49,\ y(A_U)\ge48,\ y(A_L)+y(A_U)\ge111,\\
 & y(A_L)+2y(A_U)\ge160.
\end{array}
\tag{7.2}
\]

The last row is the lifted form of the extra delete facet.

### Exact cut-dependent double-repair row

For a fixed cut \(D\), let \(C_L(D)\) and \(C_U(D)\) be the unique-provider colours actually lost by \(D\), and put

\[
B(D)=\{a\in A:
\operatorname{lower}(a)\in C_L(D),\ 
\operatorname{upper}(a)\in C_U(D)\}.
\]

Any 99-seam q1 completion satisfies

\[
\boxed{y(B(D))\ge L(D)+U(D)-99.}
\tag{7.3}
\]

Indeed, a selected seam outside \(B(D)\) covers at most one of the \(L(D)+U(D)\) lost rows, while a selected seam in \(B(D)\) covers at most two. Hence 99 seams cover at most \(99+y(B(D))\) lost rows. This proves (7.3). It remains valid in the presence of duplicate colours or endpoint conflicts, since those can only reduce effective coverage.

The set \(B(D)\) depends on the cut and would require cut-colour coupling indicators or a fixed-cut Benders cut for an exact single master row. However,

\[
B(D)\subseteq A_L\cap A_U=:A_{\rm both}.
\]

Using the two branch diagonal bounds in (7.3) therefore gives the cheap fixed rows

\[
\boxed{y(A_{\rm both})\ge14\quad(R)},
\qquad
\boxed{y(A_{\rm both})\ge12\quad(D)}.
\tag{7.4}
\]

This proves exactly the proposed `A_both` constraints. They are necessary, not sufficient.

### Stronger signed forms when exactly 99 seams are added

Let

\[
A_0=A\setminus(A_L\cup A_U).
\]

Since \(y(A)=99\), the identity

\[
y(A_L)+y(A_U)=99+y(A_{\rm both})-y(A_0)
\]

turns the diagonal rows into

\[
y(A_{\rm both})-y(A_0)\ge14\quad(R),
\qquad
y(A_{\rm both})-y(A_0)\ge12\quad(D).
\tag{7.5}
\]

These signed rows are strictly stronger than (7.4) whenever a selected seam lies in \(A_0\). They are algebraically identical to the corresponding aggregate rows in (7.2), so no extra assumption is used.

For the delete branch, the additional facet has the category form

\[
\boxed{
y(A_U\setminus A_L)+2y(A_{\rm both})-y(A_0)\ge61.
}
\tag{7.6}
\]

This follows by subtracting \(y(A)=99\) from

\[
y(A_L)+2y(A_U)\ge160.
\]

It strengthens the delete presolve without changing the feasible set. It does not improve the branch-uniform cardinality lower bound \(y(A_{\rm both})\ge12\) by itself.

## 8. Scope boundary

The proved statements concern only:

- radius-99 cuts of the frozen 858-edge source;
- exact hitting of the current 147 residence motifs;
- the declared retain/delete branch on edge 22511;
- sole-provider lower/upper q1 losses;
- additions from all 26570 off-source loopless seams.

They do not prove a degree-balanced completion, connectivity, unit voltage, deeper-shadow coverage, or dynamic top/complement-top residence. Nonunique q1 colours may also be lost when all of their source providers are cut; therefore \(L(D),U(D)\) are exact for the sole-provider subsystem but only lower bounds on total q1 loss. All rows above remain valid under those additional losses.

The rows are redundant strengthening constraints, so adding them to a live exact model cannot remove a feasible solution. No running solve was interrupted or duplicated for this audit.

## 9. Reproducible artifacts

Independent verifier:

`scratch/audit_ad2_k16_r99_pareto_benders_facets_20260729.py`

Machine-readable PASS certificate:

`scratch/ad2_k16_r99_pareto_benders_facets_20260729.audit.json`

The verifier is fail-closed on the frozen source, scope certificate, audited-program, and catalogue hashes. It reconstructs the motifs, components, all local grades, all reachable loss pairs, seam sets, convex-hull facets, and the corrected/omitted component-5 comparison without invoking a solver.
