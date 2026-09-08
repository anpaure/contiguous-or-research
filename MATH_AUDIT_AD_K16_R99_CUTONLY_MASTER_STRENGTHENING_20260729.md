# AD audit: cut-only strengthening for the portal-complete radius-99 master

Date: 2026-07-29

## Scope

This is a solver-free audit of the following frozen artifacts and their
generators:

- `scratch/k16_r99_critical_portal_benders_core_20260729.audit.json`;
- `scratch/k16_r99_fixed_cut_small_endpoint_hall_20260729.audit.json`;
- `scratch/k16_full_interaction_core_potential_20260729.audit.json`.

No statement below uses top residence, connectivity, voltage, or a remote
solve.  No active solver driver was edited.

Write \(F\) for the frozen loopless degree-two source factor, \(c_e\in\{0,1\}\)
for deletion of \(e\in F\), and \(a_f\in\{0,1\}\) for selection of a loopless
off-source seam.  Exact degree restoration gives

\[
 b_v(c):=\sum_{e\in F:e\ni v}c_e
       =\sum_{f\notin F:f\ni v}a_f.                 \tag{1}
\]

## 1. Exact critical portal projection

### Theorem 1 (critical lower-colour portal row)

Every integral completion satisfying (1) and lower-\(q1\) coverage obeys

\[
c_{4529}\ \le\
c_{3299}+c_{4560}+c_{4598}+c_{4936}+c_{5049}+c_{5463}+c_{7892}
+c_{9827}+c_{11485}+c_{12197}+c_{12207}+c_{14126}+c_{17805}+c_{22581}.
\tag{2}
\]

This row does not require \(\sum c=99\), the 147 motif rows, either branch
condition, upper-\(q1\), residence, connectivity, or voltage.

#### Proof

The lower colour \((0,1849)\) has the unique source provider
\(4529=\{88,316\}\).  Its 35 loopless off-source providers have endpoint graph
exactly \(K_9\) minus the edge \(\{88,316\}\), on

\[
\{88,316,89,99,109,263,288,355,613\}.
\]

Thus every replacement provider meets
\(Q=\{89,99,109,263,288,355,613\}\).  If \(c_{4529}=1\), lower-\(q1\) coverage
selects a replacement, so the added incidence at some vertex of \(Q\) is
positive.  Equation (1) forces positive deleted-source incidence in \(Q\).
The union of source edges incident with \(Q\) is exactly the 14-edge support
on the right of (2).  Hence at least one right-hand cut bit is one.  This is
(2).  In this instance no source edge has both endpoints in \(Q\), so summing
(1) over \(Q\) also proves (2) as a direct fractional consequence. \(\square\)

Exact census: source/addable edge counts are \(858/26570\); all 858 source
nodes have source degree two; the 35 alternatives meet \(Q\) once for 14
providers and twice for 21 providers.  All 29 canonical Pareto cuts (14
RETAIN and 15 DELETE) have \(c_{4529}=1\) and all 14 support bits zero.

### Audit conclusion

Equation (2) is **not a new master row**.  It occurs exactly once among the
already reconstructed 1,328 portal rows (667 lower and 661 upper, with 20
parallel-provider skips).  It is valuable as a human-readable regression and
as an explanation of all 29 old canonical failures, but adding it again to a
portal-complete master is redundant.

The artifact's eight-feature core is subset-minimal only in the subsystem
consisting of one lower-\(q1\) row, seven fixed right-hand-side-zero endpoint
upper bounds, and the 99-added-seam cardinality used for its deletion
witnesses.  It is not claimed or proved to be a minimum signed
cut-assumption core, a minimum-cardinality core, or a full-subproblem
core-minus-one feasibility theorem.  Within the narrower class “the one
q1 row plus individual zero-demand endpoint caps,” seven caps are minimum:
the base pair \(\{88,316\}\) is the unique maximum independent set of the
alternative-provider graph, so \(Q\) is its unique minimum vertex cover.
This still does not prove minimum size among arbitrary grouped Hall features
or facetness/irredundancy of all 14 coefficients of (2).

Checker-hardening only: the critical-core generator pins the portal-audit
file hash and status but does not separately compare its `critical_row` field
or embedded payload digest, and it does not explicitly assert the (in fact
zero) source-loop count.  One diagnostic says a canonical cut “retains” edge
4529 when membership in the cut means “deletes.”  None of these affects the
frozen mathematical replay.

## 2. General same-palette endpoint Hall rows

### Theorem 2 (cut-only endpoint-cover Hall inequality)

Fix one palette \(\sigma\in\{\mathrm{lower},\mathrm{upper}\}\).  For a colour
\(x\), let \(P_F(x)\) be its source-provider set and let

\[
\ell_x(c)=\prod_{e\in P_F(x)}c_e
\]

be the exact Boolean indicator that \(x\) is lost from the retained source.
Let \(Z\) be a vertex set and let \(C\) be a family of \(\sigma\)-colours such
that every loopless off-source provider of every \(x\in C\) meets \(Z\).
Every exact completion satisfies

\[
 \sum_{x\in C}\ell_x(c)
 \ \le\ \sum_{v\in Z}b_v(c)
 \ =\ \sum_{v\in Z}\sum_{e\in F:e\ni v}c_e.       \tag{3}
\]

#### Proof

Each lost colour requires a selected off-source provider.  Distinct colours
in one palette require distinct seams, because a seam carries exactly one
colour in that palette.  Every required seam meets \(Z\), so their number is
at most the total selected-seam incidence in \(Z\).  Equation (1) changes this
incidence to the right side of (3).  An internal \(Z\)-seam is counted twice,
which only enlarges the valid upper bound. \(\square\)

The lower and upper palettes may not be pooled in (3): one seam can repair
one colour in each palette simultaneously.

For a cut-only CP master, \(\ell_x\) must be an exact AND of all source
provider cut bits.  Merely upper-bounding an auxiliary \(\ell_x\), or treating
the artifact's strings `lost_colour_AND` and `endpoint_le` as already-linear
expressions, is unsound.  Exact AND reification is

\[
\ell_x\le c_e\quad(e\in P_F(x)),\qquad
\ell_x\ge \sum_{e\in P_F(x)}c_e-|P_F(x)|+1.
\]

The symbolic feature no-good using `endpoint_le(v,t)` likewise needs exact
two-way reification if it is used instead of (3).

### Exhausted size-at-most-two census

The frozen small-endpoint audit considered all singleton and pair covers for
every lost colour on each of the 29 canonical cuts and found

\[
\boxed{0\text{ cuts with a small endpoint Hall core}}.
\]

Thus that artifact emits no new generalized Benders no-good.

An independent global census over all 764 colours in each palette gives:

- no colour with zero loopless off-source providers;
- no singleton provider-graph cover;
- exactly two lower and two upper colours with a two-vertex cover;
- each of those four colours has exactly three covering pairs, hence 12
  universal rows of form (3).

The four colours/source providers and their cover pairs are

\[
\begin{array}{c|c|c|c}
\sigma&x&P_F(x)&Z\\ \hline
L&(1,3171)&\{26016\}&\{744,745\},\{744,747\},\{745,747\}\\
L&(1,5285)&\{27388\}&\{841,843\},\{841,845\},\{843,845\}\\
U&(0,7399)&\{9827\}&\{215,263\},\{215,355\},\{263,355\}\\
U&(0,11627)&\{14681\}&\{231,378\},\{231,399\},\{378,399\}.
\end{array}
\]

Every displayed pair contains at least one endpoint of its unique source
provider.  Therefore its right side already contains its left cut bit, and
all 12 rows are tautological consequences of the definition of \(b_v\) and
nonnegativity.  The two triangles in each palette are vertex-disjoint, so no
pair supports a multi-colour row.  These are exactly four of the 20
parallel-provider exceptions (each has two off-source providers parallel to
its source edge).  They add no strength to the current cut master.

## 3. Full-interaction potential artifact

No inequality from
`k16_full_interaction_core_potential_20260729.audit.json` can presently be
added to the radius-99 cut master.  Its variables are red/blue physical-edge
overlay choices between a resident factor and another \(q1\) factor; its rows
combine overlay degree balance, palette slack, and 2,250 short-run motifs.
It supplies no proved projection to the 858 current source cut bits.

Its exact replayed potential data are:

\[
\begin{array}{c|c|c|c|c|c}
\text{state}&\text{unit cores}&\text{row union}&\text{packed motifs}
 &\text{saturation cores}&\text{components}\\ \hline
Q3&30&554&43&3&5\\
beam1&29&548&42&2&5\\
beam2&27&461&36&1&5\\
beam3&27&501&39&0&3.
\end{array}
\]

All four states have 2,250 motifs and zero static blockers.  The comparison
scores are \(c4=(29,551,0,2251,4)\),
\(c6=(30,594,0,2250,4)\), and
\(c6x2=(30,571,0,2251,4)\).  Across the two five-target strict-C4 censuses
there are respectively 48 and 53 raw radius-two target/trade incidences, but
zero strict-token trades and hence zero saved-motif breakers.  The first two
old beam moves are not token-identities; only the third is.

The unsound proxy is to interpret `unit_core_count`,
`unit_core_row_union_size`, or the lexicographic `score` as a radius-99 Hall
deficiency, a cut lower bound, or a Benders inequality.  The cores are found
by order-dependent greedy unit-propagation peeling.  The artifact explicitly
disclaims equality with canonical Hall deficiency, and the stale saved
row-union 517 replaying as 501 demonstrates that the row-union coordinate is
not an invariant.  Individual contradictions are exact only in their frozen
overlay model; transporting them requires a separate proved variable/row
embedding that is currently absent.

Its provenance is also weaker than the two r99 audits: the JSON has no
canonical payload hash, the generator hashes its 13 data inputs but not the
three imported implementation modules, and the compact JSON omits the unit
cores' actual row tags.  A current byte-identical replay is a consistency
check, not a standalone future-proof certificate from the JSON alone.

## 4. Net action from the three pre-hierarchy artifacts

For the already portal-complete radius-99 master:

1. retain all 1,328 portal rows;
2. do not add (2) a second time;
3. the size-\(\le2\) endpoint Hall artifact contributes zero violated cores,
   and its 12 globally materializable rows are tautologies;
4. do not use the full-interaction score or core counts as master cuts.

Consequently these three artifacts yield **zero new nonredundant cut-only
inequalities** beyond the existing portal family.  This conclusion is scoped
to those artifacts and to the globally exhausted endpoint-cover sets of size
at most two.  It does not exclude larger portal unions.

## 5. Subsequent strict level-2 Hall update

The later artifact
`scratch/k16_r99_portal_hall_strictness_20260729.audit.json` supplies exactly
the larger-union strengthening left open above.  It gives portal-first-order
feasible cuts in both locked branches for which a lower five-colour family has
cut endpoint incidence three and an upper eight-colour family has incidence
four.  Thus the exact same-palette Hall inequalities (3) have deficits two and
four.  Four branch-labelled certificates deduplicate to three nonredundant
rows, with portal unions of sizes 32, 51 and 52.

More generally, maximum violation of (3) over source-unique nonparallel
colours is a maximum-weight closure/min-cut problem: colour profit is its sole
provider cut weight, selecting a colour forces every node in its portal set,
and portal-node cost is cut endpoint degree.  The exact separator and its
parallel-provider scope are proved in
`MATH_AUDIT_AD_K16_R99_PORTAL_COMPLETE_BENDERS_CEGAR_20260729.md`.
Accordingly, “zero new rows” above must not be quoted after adding the level-2
artifact; it remains only the exact negative audit of the three files named in
the Scope section.

## Frozen hashes audited

- critical-core generator: `efd337ea9d26a84a179e115c25029723f0e34e2bd53300df338eabee790fe56b`;
- critical-core JSON: `9bf97cdbbecabddf042dc506ae87543f3a4ba5de50dfe782948549416c9082e7`;
- small-endpoint generator: `1d4786a82765c17726af203c6dcd7a141797a3440236398dc02e6252d045a97a`;
- small-endpoint JSON: `333501eca2fca68ea4f9d1f3ff77b37eee2f5f11287997abfd29352414c3601b`;
- full-interaction generator: `e69bf0fc25e01f50aa0b7a82573e66569080e2e54af90e05c3b499b2ea53e8c7`;
- full-interaction JSON: `95b484d4804bc31a27c1cbf6ccc50b38da95a58dcb2577a94ad4c4259b986639`.
