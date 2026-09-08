# `k=17`: exact marker-path q1 extension and the 43,128-variable upper quotient core

Date: 2026-08-02  
Status: unconditional theorem and independently replayed finite factor.  The
owner/rank-eight q1 extension gate is closed for the frozen first-58/open-3
marker bank.  Rank-ten completeness, connectivity, source binding,
residence, deeper upper shadows and the compiler remain open.

## 1. The frozen positive object

Take the first 58 base orbits of
`scratch/k17_marker_orbit_packing_20260802/k17_marker_orbit.witness.tsv`,
develop them under `Z_17`, and open native edge type 3 in every module.  This
gives

\[
  986=58\cdot17
\]

pairwise owner/named-target-disjoint five-owner paths, with 3,944 protected
rank-eight edges on 4,930 rank-nine owners.

The factor

```text
scratch/k17_marker58_q1_extension_20260802/marker58_q1_factor.tsv
```

contains all 3,944 protected edges and extends them to an exact rank-eight
rainbow two-factor on all 24,310 rank-nine owners.  Its current completion is
not the desired chronology: it has 1,179 components and covers only 13,307 of
the 19,448 rank-ten caps.

## 2. Exact b-flow extension theorem

Let `O` be the rank-nine owner layer and `F` the rank-eight facet layer; here
`|O|=|F|=24310`.  Let `P` be a protected simple edge family.  Every edge of
`P` has the form

\[
 (f; o,o'),\qquad f=o\cap o',quad |f|=8,quad |o|=|o'|=9.
\]

Assume that no facet is repeated and every owner has protected degree at most
two.  Put

\[
 F_0=F-F(P),\qquad b(o)=2-\deg_P(o).
\]

Build the network

\[
 s\longrightarrow f\longrightarrow o\longrightarrow t
\]

with capacities `2`, `1`, and `b(o)` respectively, where `f -> o` exists
exactly when `f subset o`.

### Theorem 2.1

`P` extends to a rank-eight-rainbow two-factor on `O` if and only if this
network has flow value `2|F_0|`.

#### Proof

A full integral flow chooses two distinct incident owners for every residual
facet.  Add the corresponding owner edge at that facet.  Because

\[
 \sum_o b(o)=2|O|-2|P|=2(|F|-|P|)=2|F_0|,
\]

full flow saturates every owner capacity.  The resulting graph uses every
facet once and gives every owner total degree two, so it is the required
two-factor.

Conversely, every extension sends one unit from a residual facet to each of
its two endpoints.  The facet-owner arc has capacity one and the owner uses
exactly its residual degree budget, giving a full flow.  QED.

Equivalently, the exact Gale inequalities are

\[
 2|A|\le \sum_{o\in O}\min\{b(o),\deg_A(o)\}
 \qquad(A\subseteq F_0).                                \tag{2.1}
\]

The minimum cuts retained for opening types 0, 1, 2 and 4 are therefore
literal q1 extension certificates, not solver heuristics.  Their flow
deficits are respectively 34, 34, 17 and 17.  Opening type 3 has full flow.

## 3. Independent finite replay

The independent O3 C++ audit reconstructs the first-58/open-3 paths from the
frozen witness, parses the completed factor without using its generator, and
checks:

* every factor row is a literal rank-eight Johnson edge;
* every rank-eight facet occurs exactly once;
* every rank-nine owner has degree exactly two;
* the protected edge set is exactly the developed marker-path set;
* component and rank-ten cap counts;
* the physical and quotient repeat ledgers below.

It returns

```text
PASS_K17_MARKER58_Q1_UPPER_CORE_INDEPENDENT
```

with 1,179 components, largest component 16,643, and 6,141 missing rank-ten
caps.

## 4. Correct immediate-upper ledger

The four retained edges of one opened marker path all have the same rank-ten
cap.  They therefore consume **three**, not four, repeat units.  The protected
bank has exactly

\[
 3944-986=2958=3\cdot986                            \tag{4.1}
\]

repeat units.  Since the global repeat budget is

\[
 {17\choose9}-{17\choose10}=4862,
\]

the residual factor has an exact allowance of

\[
 4862-2958=1904                                      \tag{4.2}
\]

repeat units.  Equivalently, its 20,366 residual facet edges must cover all
18,462 unprotected caps, leaving 1,904 repetitions.

The arbitrary b-flow completion instead has 8,045 residual repeat units.
The exact identity

\[
 8045-1904=6141                                     \tag{4.3}
\]

explains its 6,141 missing caps: every excess repetition pays for one absent
cap.

This corrects the earlier source-state/repeat-unit conflation.  For the full
96-orbit bank, opening one edge per module gives repeat debt
`3*1632=4896`, only 34 above the global budget; `4*1632` is the debt of the
unopened five-edge cycles.

## 5. Smallest exact upper-aware completion problem

The b-flow forgets which pair of owners is selected at a facet.  Retain that
pair explicitly.  For every residual physical facet `f` and every unordered
pair of distinct outside coordinates `{a,b}`, introduce

\[
 x_{f,a,b}\in\{0,1\}.
\]

The choice represents the edge

\[
 f\cup\{a\}\ --\ f\cup\{b\}
\]

with rank-ten cap `f union {a,b}`.  Then the following system is exact:

\[
 \sum_{\{a,b\}\subseteq[17]-f}x_{f,a,b}=1
       \qquad(f\in F_0),                               \tag{5.1}
\]

\[
 \deg_P(o)+
 \sum_{f,a,b:\ o\in\{f+a,f+b\}}x_{f,a,b}=2
       \qquad(o\in O),                                 \tag{5.2}
\]

and, for every rank-ten cap `U` not already protected,

\[
 \sum_{f\subset U,\ |f|=8}x_{f,U-f}\ge1.              \tag{5.3}
\]

### Theorem 5.1

Solutions of (5.1)--(5.3) are in bijection with upper-complete rank-eight
rainbow two-factors containing the protected marker paths.

#### Proof

Equation (5.1) chooses the unique edge carried by each residual rank-eight
facet.  Equation (5.2) gives every owner degree two after the protected
paths are included.  The cap of the chosen edge is exactly `f union {a,b}`,
so (5.3) is precisely rank-ten coverage.  Conversely, every such factor has
one unique outside-coordinate pair at every residual facet and hence defines
one solution.  QED.

This is the smallest fail-closed physical q1/upper model: no source-state,
component, residence or compiler claim is hidden in it.

## 6. The cyclic quotient core

The protected bank is `Z_17`-equivariant.  On the quotient it uses

\[
 290\text{ owner orbits},\quad232\text{ facet orbits},
 \quad58\text{ cap orbits}.
\]

Thus an equivariant upper completion has

\[
 1198=1430-232
\]

residual facet-orbit choices and must cover

\[
 1086=1144-58
\]

previously uncovered cap orbits.  It has exactly

\[
 1198-1086=112                                      \tag{6.1}
\]

quotient repeat units.  Each residual facet has 36 unordered pairs of its
nine outside coordinates, so the raw quotient model has only

\[
 1198\cdot36=43128                                  \tag{6.2}
\]

binary pair variables before owner-capacity filtering.

For a quotient option `e`, let `d_o(e) in {0,1,2}` be its endpoint
multiplicity at owner orbit `o`, let `kappa(e)` be its cap orbit, and let
`eta(e) in Z_17` be its voltage.  Equations (5.1)--(5.3) descend exactly to

\[
 \sum_{e\in E(f)}x_e=1,
 \qquad
 \deg_P(o)+\sum_e d_o(e)x_e=2,
 \qquad
 \sum_{e:\kappa(e)=u}x_e+\mathbf1_{u\in\kappa(P)}\ge1. \tag{6.3}
\]

This quotient system is a sufficient symmetric subclass of the physical
problem, not a consequence of the current non-equivariant flow witness.

If the selected quotient graph is one cycle, its regular lift is one physical
cycle exactly when the cycle voltage is nonzero modulo 17.  Hence a complete
q1 chronology in this subclass requires, in addition to (6.3), a quotient
spanning-tree/connectivity certificate and one nonzero voltage row.

## 7. What the 6,528 count means

The 6,528 objects in the full 96-orbit reservoir are

\[
 1632\cdot4
\]

literal source-state occurrences: one primitive `H` and three short buffers
per module.  They are not four native factor edges and cannot be matched
independently.  A valid source binding selects one joint five-state atlas
entry including the primitive `P` state and replays adjacency, the fixed
root matching, collars and protected reservations.

The present factor closes only the owner/rank-eight path extension.  It does
not bind those source states.  In particular, a rolewise matching of 6,528
source masks would be an unsound relaxation unless a rectangularity theorem
for the joint atlas were proved.

## 8. Artifacts

Primary factor and audits:

```text
0eab1f3cb25d0704e86e614850b95dec7a14e5b3c12b69254e2a90b2af0bf09e
  scratch/k17_marker58_q1_extension_20260802/marker58_q1_factor.tsv
6e1598c481ff41cde4fc99159acf0737bd30ba9585c4261fe213fff2b29060c6
  scratch/k17_marker58_q1_extension_20260802/marker58_q1_factor.audit.json
```

Independent upper-ledger replay:

```text
dfb5626bd09bf412d992c6f75c8f9f14afe6ed72adf6001592ac9d2df18242be
  scratch/audit_k17_marker58_q1_upper_core_20260802.cpp
7afd27dc3489b20654216642b45ab84bbd0ce69ac95cee98fb4bed495db9786a
  scratch/k17_marker58_q1_extension_20260802/marker58_q1_upper_core.independent.audit.json
e74bd7747133a9405558cd04afdd4ddc09344a8acd46d4b9a2791ca10712388e
  scratch/k17_marker58_q1_extension_20260802/marker58_q1_upper_core.independent.run.out
```

The independent run used O3 C++ on H100 at

```text
/home/amodo/or15/work/mr_k17_marker58_q1_upper_core_20260802
```

No search or factor regeneration was duplicated.

## 9. Exact next gate

The next sharply bounded finite decision is (6.3) plus quotient connectivity
and nonzero voltage.  A positive witness would close the owner/q1/rank-ten
host for the 986 protected paths.  It would still leave joint source-state
binding, residence, ranks 11--17 and the lower compiler.

The current progress is therefore real but localized:

\[
 \boxed{\text{named reservoir}\;\Longrightarrow\;
        \text{exact protected q1 two-factor}}
\]

is now proved at `k=17`; the upper-aware connected refinement is not.
