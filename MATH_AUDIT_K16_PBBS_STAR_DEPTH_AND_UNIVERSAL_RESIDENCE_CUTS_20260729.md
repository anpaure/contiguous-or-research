# K16 PBBS star depth and universal residence-cut audit

Date: 2026-07-29  
Status: exact star-radius census and solver-free validity proof for the
residence rows.  The radius-three catalogue is infeasible; the unrestricted
full-graph model has not been proved infeasible.

## 0. Verdict

The new radius-three result is real and broad, but it is not yet a global
architecture no-go.

* The augmented depth-three catalogue contains `330,628` of the `411,840`
  edges of `J(16,8)` and is exactly infeasible.
* Star depth four does **not** equal the full Johnson graph.  The raw star has
  `407,410` edges; after adjoining the saved q1 and resident factors the
  model has `407,675` edges, still `4,165` short of the universe.  Its
  300-second CP-SAT run returned `UNKNOWN`, not infeasible.
* The raw star first equals the full graph at depth six.  Depth five has all
  vertices but misses four edges.
* The `2,222` initial rows used with the failed-literal-zero q1 factor are
  necessary for **every** cyclic residence-at-least-four spanning 2-factor,
  even a factor completely unrelated to that q1 factor.  This has a short
  solver-free proof below.

Thus the strongest current theorem is a radius-three catalogue no-go.  A
global no-go would require the full `411,840`-edge model to be proved
infeasible or an independent combinatorial argument.

## 1. Exact star census

Let `V0` be the 143 rank-eight vertices incident with a provider edge for
one of the 8 lower or 13 upper colours in the deletion-minimal core.  The
builder starts with the 732 literal provider edges and, at each positive star
depth, adds every Johnson edge incident with the previous vertex frontier.

The distance census from `V0` is

| Johnson distance | vertices |
|---:|---:|
| 0 | 143 |
| 1 | 2,254 |
| 2 | 6,287 |
| 3 | 3,762 |
| 4 | 420 |
| 5 | 4 |

The raw edge catalogue is therefore:

| star depth | edges | missing from `J(16,8)` |
|---:|---:|---:|
| 0 | 732 | 411,108 |
| 1 | 8,224 | 403,616 |
| 2 | 112,283 | 299,557 |
| 3 | 325,353 | 86,487 |
| 4 | 407,410 | 4,430 |
| 5 | 411,836 | 4 |
| 6 | 411,840 | 0 |

The four distance-five vertices are

\[
 2033,\quad5609,\quad5617,\quad34289,
\]

with supports

\[
\begin{split}
&0456789,10,\qquad035678,10,12,\\
&045678,10,12,\qquad045678,10,15.
\end{split}
\]

At depth five the four missing edges are

\[
 (2033,5617),\ (2033,34289),\ (5609,5617),\ (5617,34289).
\tag{1.1}
\]

Neither saved failed-literal q1 factor nor the resident factor contains any
edge in (1.1).  Hence adjoining those factors does not make depth five full;
depth six remains the first full augmented catalogue as well.

The machine-readable census is
`scratch/k16_pbbs_star_depth_universe_audit_20260729.json`.

## 2. The residence cuts are universal

Let `Q` be any cyclic 2-factor and suppose coordinate `x` has a maximal run

\[
 v_1,v_2,\ldots,v_\ell,\qquad 1\le\ell\le3,
\]

in one component of `Q`.  Let `v_0` and `v_(ell+1)` be its two bordering
vertices.  Thus `x` is absent from the endpoints and present at every
interior vertex.  Define the closed path

\[
 P=(v_0v_1,v_1v_2,\ldots,v_\ell v_{\ell+1}).
\tag{2.1}
\]

### Lemma 2.1 (universal bordered-path inequality)

Every spanning 2-factor `F` whose coordinate runs all have length at least
four satisfies

\[
 \sum_{e\in P}x_e\le |P|-1,
\tag{2.2}
\]

where `x_e` is the indicator that `e` belongs to `F`.

#### Proof

Suppose instead that every edge of `P` belongs to `F`.  Each interior vertex
`v_i`, `1<=i<=ell`, is incident with its two path edges, so its degree two
in `F` is exhausted.  Consequently the `F`-component must traverse the
entire path (2.1), in one orientation or the other.  The coordinate is
absent at both endpoints and present at precisely its `ell` interior
vertices.  It is therefore a maximal `F`-run of length `ell<=3`, a
contradiction.  QED.

The proof uses no overlap, switch, distance, PBBS, or ancestry relation
between `F` and `Q`.  `Q` merely generates a list of concrete bordered
paths.  Therefore all 2,222 distinct failed-literal-zero rows are universal
valid inequalities for the desired factor class.

For the earlier failed-literal-two q1 factor the corresponding count is
2,221, not 2,222.  This is a source-factor difference, not a duplicated-row
bug.  Any report must name the q1 artifact hash when quoting the count.

## 3. Scope of the exact radius-three UNSAT

The saved radius-three model imposes, over its 330,628-edge catalogue:

1. degree exactly two at all 12,870 middle vertices;
2. coverage of all 11,440 rank-seven intersection colours;
3. coverage of all 11,440 rank-nine union colours;
4. all 2,222 universal inequalities (2.2).

It returned `INFEASIBLE` before any dynamic CEGAR round, in 7.17 seconds and
under 0.9 GB RSS.  Consequently:

> There is no cyclic spanning 2-factor contained in the augmented
> radius-three catalogue that is both-q1-complete and residence-at-least-four.

Because (2.2) is only necessary, not sufficient, this conclusion is fully
sound: weakening residence to those 2,222 rows was already infeasible.

What it does **not** prove is the same claim over depth four, depth five, the
full Johnson graph, arbitrary linear paths, or the original `nu(16)` word
problem.

## 4. Independent full-graph model

The standalone audit

`scratch/audit_k16_full_johnson_biresident_q1_nogo_20260729.py`

has no resident/PBBS reconstruction dependency.  It enumerates all 411,840
Johnson edges, independently rebuilds the q1 factor's cycles and bordered
paths, and imposes precisely the four families in Section 3.  A literal
factor replay is mandatory on SAT.

Two independent 600-second runs returned `UNKNOWN`:

* failed-literal-two source: 2,221 paths, 3.73 GB RSS;
* failed-literal-zero source: 2,222 paths, 3.74 GB RSS.

The second is the correctly matched global test for the new radius-three
result.  Neither run is SAT or UNSAT, so there is presently no global
architecture verdict.

Frozen result/resource pairs:

* `scratch/k16_full_johnson_biresident_q1_failedlit0_20260729.json`;
* `scratch/k16_full_johnson_biresident_q1_failedlit0_20260729.resource.txt`;
* `scratch/k16_full_johnson_biresident_q1_failedlit2_20260729.json`;
* `scratch/k16_full_johnson_biresident_q1_failedlit2_20260729.resource.txt`.

## 5. If the full model is eventually infeasible

The strongest correct architecture theorem would be:

> **No cyclic bi-resident double-rainbow factor at K=16.**  There is no
> spanning cyclic 2-factor of `J(16,8)` which simultaneously covers every
> rank-seven intersection colour, covers every rank-nine union colour, and
> has every coordinate run of length at least four.

That would refute the exact cyclic factor input gate used by the dual-rail
K16 architecture, independent of equivariance, PBBS ancestry, component
count, voltage, and edge-search radius.

It still would not refute:

* linear carriers whose boundary runs are exempt;
* sufficiently many opened path components, whose endpoints absorb short
  runs;
* a construction that does not demand both q1 palettes on the parent
  factor;
* a non-flat compiler; or
* `nu(16)=12873` itself.

## 6. Proof/certificate route

CP-SAT currently supplies an exact computational verdict but no retained
independently checkable proof log.  The recommended hierarchy is:

1. **Guard and minimize the core.**  Put assumption literals on every
   palette and bordered-path row (and, if useful, degree rows), extract
   `SufficientAssumptionsForInfeasibility`, then deletion-minimize it.
2. **Test the LP relaxation.**  If the minimized linear relaxation is
   infeasible, extract rational Farkas multipliers.  Their nonnegative
   weighted sum is a short solver-free certificate.
3. **If integrality is essential, emit OPB with proof logging.**  The rows
   are native pseudo-Boolean constraints:

   \[
   \sum_{e\ni v}x_e=2,\qquad
   \sum_{e:\,\ell(e)=L}x_e\ge1,\qquad
   \sum_{e:\,u(e)=U}x_e\ge1,\qquad
   \sum_{e\in P}x_e\le |P|-1.
   \]

   Run a proof-producing PB solver and verify with `VeriPB`; alternatively
   use a cardinality CNF with LRAT/DRAT proof checking.
4. **Humanize the core.**  Group the retained degree, colour, and path rows
   by coordinate/permutation symmetry and seek one capacity inequality of
   Hall/Farkas form.  If the plain LP is feasible, add the necessary
   2-matching blossom inequalities before repeating the dual extraction.

This separates three standards cleanly: CP-SAT evidence, a mechanically
verified PB proof, and a human solver-free weighted inequality.
