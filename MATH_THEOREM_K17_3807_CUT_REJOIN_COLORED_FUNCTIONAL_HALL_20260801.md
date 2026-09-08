# The `k=17` 3,807-cut rejoin gate: colored endpoint matching, graphic connectivity, and residence automata

**Date:** 2026-08-01  
**Status:** exact raw reduction plus one authenticated finite endpoint-
expansion audit.  The former recommendation to contract the raw `795`-edge
forest is retracted in Section 9.  This note does **not** construct the final
rethreaded carrier and does not prove `nu(17)=24313`.

**Residence-filtered qualification.**  A later authenticated audit applies
the deliberately relaxed necessary two-block residence predicate from
`MATH_THEOREM_K17_H2_MINCUT_BLOCK_ENDPOINT_THREE_RESOURCE_NOGO_20260801.md`.
Only 13,174 oriented seams survive; 1,289 cut colours and 368 physical blocks
on each directed shore become dead.  Thus the 28,395-seam census below is
only the raw Boolean projection of Theorem 3.1.  It is not evidence that the
automaton condition (4.3) is feasible.  There is no contradiction: Corollary
4.1 always retained (4.3) as a separate necessary-and-sufficient gate.

## 0. Input and conclusion

Start from the authenticated protected rank-eight/rank-nine factor

```text
scratch/k17_reset_twin_ferrers_bank_ml9_factor_20260801.tsv
SHA256 7c022f4050d6358bc5047532113814fdb46412db0018a0254cc82e056720d8df
```

and the exact protected-avoiding residence-cut theorem in

```text
MATH_THEOREM_K17_H2_PROTECTED_FACTOR_ONECOPY_HALL_AND_RESIDENCE_CUT_20260801.md
```

The factor has `W=24310` rank-nine owners in seven cycles.  Its projected
owner adjacencies use every rank-eight lower colour once and cover every
rank-ten upper colour.  A minimum set of old adjacencies whose deletion
clips every positive coordinate run of length at most three has size

\[
                              C=3807.                         \tag{0.1}
\]

All 26 protected projected adjacencies can be forbidden as cuts without
increasing `C`.

Deleting one such minimum set gives exactly `C` internally
depth-three-resident paths.  Rejoining those paths into one carrier is
equivalent to a **rainbow upper-covering endpoint path problem with a
regular-language constraint**.  It is not plain Hall.  Its projections are:

1. endpoint matching;
2. a partition constraint on the 3,807 missing rank-eight colours;
3. graphic independence on the 3,807 path blocks;
4. coverage of rank-ten colours killed by the cuts;
5. simultaneous acceptance by 17 finite residence automata.

After orientations and the non-Hall resource rows have been fixed, the
remaining predecessor assignment is an ordinary functional-Hall problem.
The unconditioned problem is a colored functional-Hall problem intersected
with a graphic and automaton gate.

For one deterministic protected-avoiding minimum cut, an exact H100 audit
finds 28,395 raw unordered endpoint seams, equivalently 56,790 directed
atoms, with no dead endpoint slot, no dead cut colour, and no cut-killed
rank-ten colour without a raw replacement.  The graph is nevertheless
sparse: its average endpoint-slot and cut-colour degree is only 7.459.  In
particular, 282 cut colours have no nonincumbent realization.  Thus “dense
Boolean neighbourhoods” is false globally; what survives here is structured
raw expansion.

## 1. The cut path system

Let `F` be the projected owner two-factor.  For an old edge `e=TT'`, write

\[
        \kappa(e)=T\cap T'\in {[17]\choose 8},\qquad
        \rho(e)=T\cup T'\in {[17]\choose 10}.                 \tag{1.1}
\]

Let \(D\subset E(F)\) be a protected-avoiding minimum circular stabbing set,
\(|D|=C\).  Put

\[
 \mathcal K=\{\kappa(e):e\in D\}.                             \tag{1.2}
\]

Because the old lower palette is exact, \(|\mathcal K|=C\).  Removing `D`
from the seven cycles gives a family

\[
                    \mathcal P=\{P_1,\ldots,P_C\}             \tag{1.3}
\]

of `C` nonempty owner paths.  A singleton path has two distinct endpoint
**slots** at the same owner.  In all cases write the occurrence-labelled
endpoint slots of `P_i` as `p_i^- ,p_i^+`, with owner masks
`T(p_i^-),T(p_i^+)`.

The exact circular stabbing lemma implies:

### Lemma 1.1 (internal residence)

For every coordinate `x`, every positive `x`-run internal to a block
`P_i` has length at least four.

The boundary runs may be shorter.  Therefore arbitrary endpoint rejoining
does not automatically preserve residence.

## 2. Admissible seams

An admissible seam `a={p,q}` is a pair of endpoint slots belonging to
distinct blocks such that

\[
 |T(p)\cap T(q)|=8,
 \qquad \kappa(a):=T(p)\cap T(q)\in\mathcal K.                \tag{2.1}
\]

Its rank-ten union colour is

\[
                         \rho(a):=T(p)\cup T(q).               \tag{2.2}
\]

Let \(\mathcal A(D)\) be the set of admissible seams.  Let

\[
 \mathcal U_D=
 \{R\in {[17]\choose10}:\text{every old occurrence of }R
                              \text{ belongs to }D\}.          \tag{2.3}
\]

These are exactly the immediate upper colours lost on cutting.

## 3. Exact lower, upper, and topology reduction

For \(a\in\mathcal A(D)\), let `c_-(a),c_+(a)` denote its two path blocks.

### Theorem 3.1 (colored endpoint-graphic gate)

Ignoring residence for the moment, the blocks can be rejoined into one
Hamilton owner path which

* uses no rank-eight lower colour twice;
* uses every rank-eight lower colour except one boundary hole;
* and retains complete rank-ten immediate-upper support

if and only if there are binary variables `x_a` satisfying

\[
\begin{aligned}
 &\sum_{a\in\mathcal A(D)}x_a=C-1,                              &&\tag{3.1a}\\
 &\sum_{a\ni p}x_a\le1
       &&\text{for every endpoint slot }p,                     &&\tag{3.1b}\\
 &\sum_{a:\,\kappa(a)=K}x_a\le1
       &&\text{for every }K\in\mathcal K,                     &&\tag{3.1c}\\
 &\sum_{a:\,c_-(a),c_+(a)\in S}x_a\le |S|-1
       &&\text{for every nonempty }S\subseteq\mathcal P,      &&\tag{3.1d}\\
 &\sum_{a:\,\rho(a)=R}x_a\ge1
       &&\text{for every }R\in\mathcal U_D.                   &&\tag{3.1e}
\end{aligned}
\]

#### Proof

The old uncut edges already use every lower colour outside \(\mathcal K\)
exactly once.  Equations (3.1a) and (3.1c) therefore use exactly `C-1`
distinct members of \(\mathcal K\), leaving one and only one boundary hole.

Equation (3.1b) is endpoint-slot matching.  Equation (3.1d) says that the
contracted seams are graphic-independent.  There are `C-1` selected seams
on `C` block vertices, so they form a spanning tree.  Every block has two
endpoint slots, hence contracted degree at most two.  A spanning tree of
maximum degree two is a path.  Orienting the blocks along this path gives
one Hamilton owner chronology.

Every rank-ten colour outside \(\mathcal U_D\) still has an uncut old
occurrence.  Equation (3.1e) restores every colour in \(\mathcal U_D\).
This proves sufficiency.  Deleting the new seams from any chronology with
the stated properties gives (3.1a)--(3.1e), proving necessity.  \(\square\)

### Boundary-hole qualification

A linear path on all `W` owners has only `W-1` immediate intersections, so
one rank-eight colour must be absent from this row.  “Exact lower palette”
therefore means exact modulo this named linear boundary hole.  The Ferrers
boundary/compiler must supply that final target.  Equivalently, one may
first solve the cyclic version using all `C` cut colours and then open one
certified seam.

## 4. Exact residence is a finite-state gate

For a binary word `w`, let

\[
 \mathcal L_4=\{w:\text{no factor }0\,1^j\,0
                         \text{ occurs for }1\le j\le3\}.      \tag{4.1}
\]

A linear owner chronology is depth-three resident exactly when its
coordinate word lies in \(\mathcal L_4\) for every coordinate.  Prefix and
suffix positive runs may be short; internal ones may not.

The language \(\mathcal L_4\) is regular.  One deterministic automaton records
whether it is still in the initial positive prefix, is at a zero, or is in
a post-zero positive run of capped length `1,2,3,4`, together with a fail
state.  Let `M_4` be its finite transition monoid.

Each oriented block `P_i` therefore has a 17-coordinate summary

\[
               \sigma(P_i)\in M_4^{17}.                       \tag{4.2}
\]

The summary of a concatenation is the product of the summaries.  Thus the
additional exact residence condition on a solution of (3.1) is:

\[
  \text{for the unique oriented block order induced by the selected path,}
  \quad \sigma(P_{i_1})\cdots\sigma(P_{i_C})
  \text{ is accepting in all 17 coordinates}.                \tag{4.3}
\]

This condition is necessary and sufficient by (4.1).  Pairwise seam tests
alone are not sufficient: a short all-one block can transport an unfinished
boundary run across two seams.  State expansion is the exact way to retain
the functional-Hall language without this error.

### Corollary 4.1 (exact immediate-palette/positive-run rejoin reduction)

There is a resident Hamilton owner path with the desired lower and immediate
upper palettes if and only if (3.1) has a solution whose induced order
satisfies (4.3).

Deeper upper shadows, the full flag table, and the terminal lower compiler
remain separate gates.

## 5. Where ordinary Hall does and does not apply

For fixed block orientations and a fixed head--owner attachment, admissible
predecessors form a bipartite graph.  Completion of unused tails to unused
heads is then exactly Hall:

\[
                |N(X)|\ge |X|\quad\text{for every residual tail set }X.
                                                                    \tag{5.1}
\]

This is the same functional contraction as the protected one-copy Hall
criterion in the source note.  But (5.1) alone does not enforce:

* distinct lower colours;
* graphic independence/no subtour;
* restoration of cut-killed upper colours;
* or the 17 residence automata.

Accordingly, the clean classification is:

\[
 \boxed{\text{functional Hall}
        +\text{endpoint/lower partition rows}
        +\text{graphic rows}
        +\text{upper cover}
        +\text{finite-state residence}.}                      \tag{5.2}
\]

The seam identity is functional once its two endpoint slots are chosen:
both `kappa(a)` and `rho(a)` are forced.  It is not a freely coloured
bipartite edge.

## 6. Exact endpoint-expansion audit for one minimum cut

The deterministic audit

```text
scratch/audit_k17_h2_cut_rejoin_endpoint_expansion_20260801.cpp
```

reconstructs one lexicographically selected protected-avoiding minimum
stabbing set by retaining the rightmost-endpoint greedy witnesses in the
exact circular algorithm.  It then builds all path blocks, all
occurrence-labelled endpoint slots, and every seam satisfying (2.1).

It was compiled and run on H100 with

```text
g++ -std=c++20 -O3 -DNDEBUG
```

against the authenticated factor.  The retained output is

```text
scratch/k17_h2_cut_rejoin_endpoint_expansion_20260801.out
```

The exact census is:

| quantity | value |
|---|---:|
| cuts / resident paths | 3,807 |
| endpoint slots | 7,614 |
| admissible seams | 28,395 |
| distinct block pairs supporting a seam | 28,129 |
| dead endpoint slots | 0 |
| dead cut colours | 0 |
| cut colours with no nonincumbent seam | 282 |
| rank-ten colours killed by the cuts | 2,423 |
| killed rank-ten colours with no replacement seam | 0 |
| killed rank-ten colours with a unique replacement seam | 560 |

The average endpoint-slot degree and average cut-colour degree are both

\[
          \frac{2\cdot28395}{7614}
        = \frac{28395}{3807}
        \approx 7.459.                                        \tag{6.1}
\]

The number of endpoint owners above a cut colour has distribution

```text
2:282, 3:854, 4:1203, 5:907, 6:435, 7:109, 8:17
```

and mean `15982/3807 = 4.198`.  Every cut colour has its two incumbent
endpoint owners, but only a structured subset of the seven other possible
rank-nine supersets appears at cut endpoints.

The replacement multiplicity of the 2,423 killed upper colours is

```text
1:560, 2:590, 3:510, 4:329, 5:206, 6:108, 7:62,
8:34, 9:11, 10:7, 11:1, 12:3, 15:2.
```

Most encouragingly, the 560 unique-upper seams are already mutually
compatible at the three elementary rows:

* no endpoint-slot collision;
* no lower-colour collision;
* no block degree above two.

Adding the 281 lower colours having exactly one candidate produces a union
of 795 distinct forced seams.  That union has:

```text
slot conflicts = 0
lower-colour conflicts = 0
block overdegree = 0
graphic cycles = 0
```

Thus the most rigid singleton requirements form a raw protected forest
rather than an immediate resource conflict.  This statement precedes both
canonical cancellation and residence.

## 7. Expansion verdict

The Boolean endpoint graph is not dense in the sense needed for a trivial
Hall proof.  A naive ambient calculation gives 72 Johnson neighbours per
rank-nine owner, but imposing both

* endpoint ownership, and
* membership of the intersection in the 3,807-colour cut set

reduces the exact average slot degree to 7.459.  There are 168 degree-one
endpoint slots and 282 cut colours with no nonincumbent realization.

On the other hand, the raw singleton audits are unexpectedly favourable:

* every endpoint slot and every required colour has a provider;
* every cut-killed upper colour has a provider;
* all unique upper restorers are resource-compatible;
* the combined 795-edge raw forced core is already a linear forest.

This forest is not a resident forced core.  Every minimum collar transversal
is inclusion-minimal, so every cut edge has a private short-run collar.
Reinserting its incumbent endpoint edge recreates that forbidden run (or its
reversal).  All 281 raw unique-lower members of the 795-edge union are
incumbent-only; 46 of them are also the sole raw restorers of a cut-killed
rank-ten colour.

After the 3,807 incumbent cancellation edges are removed, 24,588 unordered
nonincumbent pairs remain and 282 cut colours already have no candidate.
The subsequent necessary-residence filter strengthens this to 1,289 zero-
colour rows and 368 dead physical blocks on each directed side.  Thus this
deterministic rightmost-greedy emitted path partition is dead.  The missing theorem must optimize the cut
and the state-expanded coloured endpoint system jointly.  Aggregate raw
degree counts cannot substitute for that joint choice.

## 8. Reproducibility hashes

```text
scratch/audit_k17_h2_cut_rejoin_endpoint_expansion_20260801.cpp
SHA256 eed8f3867ee557d8211d4880fd1fd019f02543913432757d5d06c158b2612622

scratch/k17_h2_cut_rejoin_endpoint_expansion_20260801.out
SHA256 b36c8f5526bca9038b8bf74af493ffd4bb7434c1f69697be861d8d9e979ecdf2
```

The final output line is

```text
PASS_K17_H2_CUT_REJOIN_ENDPOINT_EXPANSION
```

## 9. Exact next finite/mathematical gate

The forced-`795` contraction is retracted.  The next finite model must choose
a protected short-run transversal and its nonincumbent replacement seams
jointly.  In canonical symmetric-difference form, with
`D=E(F)\E(H)` and `A=E(H)\E(F)`, every lower colour satisfies

\[
 \mathbf 1_{e_K\in D}=\mathbf 1_{K=K_*}
      +|\{a\in A:\kappa(a)=K\}|.                            \tag{9.1}
\]

Owner degrees, upper multiplicities, connectivity and the exact residence
product automaton must use those same variables.  The
inclusion-minimal-transversal specialization is recorded in

```text
MATH_THEOREM_K17_JOINT_CUT_SELECTION_RESIDENCE_ENDPOINT_AND_LEXFIRST_DM_OBSTRUCTION_20260801.md
```

The corresponding mathematical target is:

> **Joint protected cut/seam selection.**  Among the minimum, or explicitly
> priced nonminimum, protected collar transversals, choose one whose
> nonincumbent state-expanded seam system extends integrally to a spanning
> linear tree, restores the named upper rows, and is accepted by the product
> residence automaton.

For a priced nonminimum refinement this is a genuine extension of the cited
specialization: its pre-cancellation cut set can be redundant, selected old
cut edges may be reused as seams, and the private-collar exclusion is not
available automatically.

Proving only ordinary endpoint Hall would leave the colour, graphic, upper,
and automaton rows unresolved.

The subsequent extra-cut atlas removes singleton nonemptiness in the
lex-rooted support-two union projection: every one of the `2025` old zero
colour/tail/head rows has a unary or support-two column.  This is a
union-of-menus statement only.
The dense prospective SAT witness may use a unary provider block destroyed
by another selected split; no literal `7612`-block rebuild or simultaneous
matching follows from that formula.  The selected cut set has since been
rebuilt literally: all three unoriented lower/endpoint projections are
perfect, but `187` pieces force opposite incoming/outgoing orientations and
make the common-orientation q1 CNF unit-UNSAT; `78` rank-ten rows also have
no relaxed-resident provider.  Hence the target above remains joint integral
cut/seam selection, not contraction of a newly “closed” bank.
