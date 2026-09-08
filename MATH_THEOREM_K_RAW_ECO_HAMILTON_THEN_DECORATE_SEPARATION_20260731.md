# Raw ECO Hamiltonization followed by terminal decoration repair

Date: 2026-07-31  
Status: exact two-stage implication for the middle-levels-resolvable central
CLMT route; exact project-\(m=5\) realization; no all-\(m\) raw disjoint ECO
bank, decorated-Hamilton theorem, residence/RSB preservation, or
coefficient-one conclusion

## 0. Verdict

For the **middle-levels-resolvable central Catalan linear matching route**,
a decoration need not be carried through the component glues.  There are
two logically separate stages.

* **Stage A: raw Hamiltonization.**  A pairwise-disjoint strict ECO
  incidence hypertree turns the starting factor into one Middle Levels
  Hamilton cycle.  No upper transversal, forced owner matching, or
  occurrence router is used.
* **Stage B: terminal decoration.**  After Stage A, an arbitrary
  alternating-circuit packet may move through degree-two factors to a final
  Hamilton cycle carrying one Catalan decoration on the binary-trace forest
  face.

The exact implication is

\[
 \boxed{\text{raw strict ECO Hamiltonization}
        +\text{ terminal decorated Hamilton cycle}
        \Longrightarrow\text{ central CLMT}.}          \tag{0.1}
\]

Moreover Stage B is independent of the particular Hamilton cycle emitted by
Stage A: the symmetric difference of two degree-two factors decomposes into
alternating circuits.  Thus once one terminal decorated Hamilton cycle
exists, every starting Hamilton cycle can be repaired to it.

This strictly weakens the **gluing interface** relative to a repair-first
private coherent collar.  It does not weaken the terminal decorated-
Hamilton gate, and it carries no residence, deeper-shadow, voltage, socket,
or compiler invariant unless those are separately imposed on the circuit
packet.

## 1. Decoration-free strict ECO Hamiltonization

Let \(F\) be a spanning degree-two factor of
\({\rm ML}(2m-1)\), with component set \(\mathcal V\).  For each ECO atom
\(t\), let \(O_t\subseteq F\) be its old three-edge matching, \(N_t\) the
opposite three-edge matching, and

\[
                         Z_t=O_t\mathbin\triangle N_t.             \tag{1.1}
\]

Let \(S_t\subseteq\mathcal V\) be the set of old components met by \(O_t\).
A selected family \(\mathcal T\) is a **raw strict ECO incidence
hypertree** when:

1. the six-vertex supports of distinct atoms are disjoint;
2. the component--atom incidence graph
   \(B(\mathcal V,\mathcal T)\) is a spanning tree; and
3. for every prefix of one declared atom order, the physical component
   partition is the connectivity partition of the corresponding incidence
   subforest.  Equivalently, the next atom meets \(|S_t|\) distinct current
   blocks, merges all of them, and splits none.

Condition 3 is a physical phase condition.  It is not implied by the
incidence tree: a two-touch incidence hex can reconnect its three cut paths
as a merge or as a four-cycle plus a two-cycle.

### Theorem 1.1 (raw hypertree Hamiltonization)

If \(\mathcal T\) is a raw strict ECO incidence hypertree, then

\[
                    C_0=F\mathbin\triangle
                         \mathop{\triangle}_{t\in\mathcal T}Z_t   \tag{1.2}
\]

is a Hamilton cycle.  Every prefix is a degree-two factor, and the declared
order is executable.  No turn decoration, owner matching, coherent external
label, or occurrence router is needed.

#### Proof

Disjoint six-vertex supports imply that the toggles commute, every pending
old edge survives until its atom is used, and every prefix remains
degree two.  Induct over the declared order.  By Item 3, earlier strict
toggles realize the connectivity classes of the earlier incidence
subforest.  If two vertices of \(S_t\) were already in one current block,
their earlier incidence path together with the two incidences through \(t\)
would form a cycle in \(B(\mathcal V,\mathcal T)\).  Hence the pending atom
meets \(|S_t|\) distinct current blocks, and its strict toggle lowers the
physical component count by exactly \(|S_t|-1\).

The incidence-tree edge count gives

\[
                 \sum_{t\in\mathcal T}(|S_t|-1)
                    =|\mathcal V|-1.                              \tag{1.3}
\]

Starting from \(|\mathcal V|\) components and applying the strict decrements
in (1.3) leaves exactly one degree-two component, namely the Hamilton cycle
\(C_0\).  None of these arguments mentions a decoration or router.
\(\square\)

The weighted forest cuts and one-anchor theorem give an exact combinatorial
test for Item 2.  On a component path, binary/ternary tile selection is a
unit-flow problem and hence integral.  The determinant-two \(K_{1,3}\)
fixture shows that the analogous naive branching relaxation need not be
integral.  These are Stage-A topology facts only.

## 2. Terminal decorated-Hamilton repair

Write a Hamilton cycle as

\[
 A_0,B_0,A_1,B_1,\ldots,A_{Q-1},B_{Q-1},A_0
\]

in the two Middle Levels rails.  A **terminal CLMT decoration** consists of
index sets \(I,J\) such that:

1. the selected upper turns and lower turns are bijective on their complete
   colour alphabets;
2. their marked occurrences alternate cyclically, equivalently the residual
   incidence paths have perfect matchings; and
3. the binary trace is on the linear-forest side: some positive unmarked gap
   has length at least four or some maximal marked run has even length.

Items 1--2 are the Catalan decoration.  Item 3 excludes the unique
one-cycle face and is essential for a Catalan **linear** matching.

### Theorem 2.1 (terminal repair is independent of the Stage-A cycle)

Let \(C_0\) be any Hamilton cycle of \({\rm ML}(2m-1)\).  The following are
equivalent.

1. Some Hamilton cycle \(C_*\) admits a terminal CLMT decoration.
2. A finite packet of alternating circuits transforms \(C_0\), through
   degree-two factors, into such a decorated Hamilton cycle \(C_*\).

#### Proof

For any two degree-two factors on the same vertex set, colour the edges of
\(C_0\setminus C_*\) red and those of \(C_*\setminus C_0\) blue.  At every
vertex the red and blue degrees agree.  Pair red and blue half-edges at each
vertex and follow the pairings.  This decomposes
\(C_0\mathbin\triangle C_*\) into edge-disjoint closed alternating
circuits.  Toggling them successively preserves degree two and reaches
\(C_*\).  Intermediate factors need not be connected or decorated.

The reverse implication reads the terminal cycle.  Finally, the
decorated-middle-levels equivalence turns the terminal decoration, including
the binary-trace forest alternative, into the required Catalan linear
matching. \(\square\)

The theorem allows arbitrary alternating circuits.  Bounded circuit length,
Hamiltonian intermediate prefixes, or preservation of a residence/RSB
state are strictly stronger requirements and are not consequences.

## 3. Exact two-stage implication and comparison

### Corollary 3.1 (decoration-after-Hamiltonization)

If Stage A supplies a raw strict ECO incidence hypertree and Stage B supplies
one terminal decorated Hamilton cycle, then the canonical factor can be
converted to a central Catalan linear matching.

#### Proof

Apply Theorem 1.1 to obtain \(C_0\), Theorem 2.1 to reach \(C_*\), and the
decorated-cycle equivalence to lift \(C_*\) to the linear matching.
\(\square\)

The two architectures have different quantifiers.

\[
\begin{array}{c|c|c}
 &\text{repair-first private collar}&\text{decorate after glue}\\ \hline
\text{gluing input}&(F,I,M)\text{ and owner-aligned ports}&F\text{ only}\\
\text{gluing topology}&\text{private coherent collar/hypertree}
                      &\text{raw strict disjoint hypertree}\\
\text{router during glue}&\text{required by the recursive catalogue}
                         &\text{not required for an explicit family}\\
\text{decoration}&\text{preserved at every glue}
                 &\text{chosen only on }C_*\\
\text{downstream state}&\text{may be carried prefixwise}
                       &\text{must be repaired/reverified afterward}
\end{array}                                                       \tag{3.1}
\]

On a fixed source, a decoration-preserving private collar is stronger on
the gluing stage: its terminal repair may be the identity.  Conversely, a
post-glue circuit packet may overlap every former glue port and may pass
through split factors, so it need not define any private-collar cube.
Because the architectures may start from different repaired factors,
neither global all-\(m\) existence statement formally implies the other.

For the central CLMT, the minimal open Stage-B statement is simply:

> for every \(m\), some Hamilton cycle of
> \({\rm ML}(2m-1)\) admits a Catalan decoration on the binary-trace forest
> face.

Circuit realization is not a further existential gate.  Stage A remains a
useful canonical-factor compiler and a possible carrier for downstream
state, but it does not solve this terminal statement.

### Corollary 3.2 (the weakest exact central gate in this route)

Within the middle-levels-resolvable subclass, the existence of a central
Catalan linear matching is equivalent to

> **DHC(\(m\)).**  Some Hamilton cycle of
> \({\rm ML}(2m-1)\) has one joint alternating upper/lower turn SDR and lies
> on the binary-trace forest face.

The published Middle Levels theorem already supplies a starting Hamilton
cycle, so Stage A is not logically necessary for this bare existential
equivalence.  It is a canonical-factor construction scaffold and may be
valuable for carrying later state.  Theorem 2.1 removes dependence on which
starting Hamilton cycle it supplies.

This is an equivalence only for the middle-levels-resolvable class of the
decorated-cycle theorem.  It does not assert that every abstract Catalan
linear matching extends to a Middle Levels Hamilton cycle.

The joint qualifier is load-bearing.  At \({\rm ML}(7)\), the authenticated
counterexample cycle has both turn maps surjective but no alternating
occurrence SDR: all \(12{,}288\) upper SDRs fail residual gap Hall.  One
standard incidence-hex toggle repairs it.  Among the 31 alternating
hexagons around the repaired positive cycle, 16 give Hamilton outputs, 10
of those are decorable, and six Hamilton toggles have a source/output pair
admitting at least one common forest-side decoration.  Their common-
decoration multiplicities are \(576,576,144,144,432,540\); every one is
linear/forest-trace and each of the six pairs has a leaf-peelable common
decoration.  For a fixed decoration, the exact transparent criterion is:

1. the selected local turn-colour multisets agree separately on both
   shores; and
2. the retained-fragment boundary mark types alternate after reconnection.

That criterion is indispensable in the repair-first route because the same
decoration is transported through the toggle.  It is not a necessary
condition on an arbitrary post-glue repair packet, whose terminal
decoration may be chosen afresh.

## 4. Exact project-\(m=5\) post-glue realization

At project \(m=5\), the canonical factor has component orders

\[
                              36,\quad72,\quad144.                 \tag{4.1}
\]

The two fixed-rotation ECO atoms

\[
                         D=101010,\qquad D=101100                  \tag{4.2}
\]

are the two authenticated standard glues.  Their physical supports are
disjoint; together they form a strict incidence hypertree and toggle the
canonical factor to the standard Hamilton cycle of order \(252\).

Starting from that Hamilton cycle, the three vertex-disjoint \(C_{10}\)
circuits in the synchronized repair theorem give another Hamilton cycle
with:

* complete \(84+84\) turn occurrence palettes;
* a gap forest with one unique perfect matching; and
* a forest binary trace.

Thus (4.2) is Stage A and the three-\(C_{10}\) packet is Stage B.  This is
an unconditional finite realization of Corollary 3.1.

The ECO supports in (4.2) are also vertex-disjoint from all three
\(C_{10}\) supports.  Hence the five toggles commute as physical symmetric
differences, explaining why the same fixture also has the repair-first
interpretation proved in the private-ECO integration theorem.  The two
interpretations have different intermediate factors and different
invariants; commutation of this finite packet is not an all-\(m\) theorem.

## 5. Sharp remaining all-\(m\) alternatives

For the central CLMT alone, one may pursue:

1. **Stage A:** a uniform pairwise-disjoint strict ECO incidence hypertree
   (or the state-expanded component-path bank) Hamiltonizing the canonical
   factor; and
2. **Stage B:** a terminal decorated-Hamilton theorem.

The all-dimension coherent ECO two-section does not prove Stage A: it gives
connected static incidence but not a disjoint strict hypertree.  The exact
path-flow theorem proves integrality only after a component path and its
literal atom transitions are exported.

For exact contiguous-OR applications, central CLMT is not the whole state.
If residence, all-depth shadows, sockets/voltage, or the common-\(Q\)
compiler must survive, then Stage B must end in—and, where the downstream
argument requires it, carry—the corresponding RSB state.  The arbitrary
circuit decomposition of Theorem 2.1 gives no such preservation.  The
repair-first private collar remains stronger precisely in that coordinate.

No all-\(m\) Stage A, Stage B, RSB-preserving packet, compiler, or
coefficient-one theorem is claimed.

## 6. Authoritative inputs

* MATH_THEOREM_CATALAN_POSTGLUE_REPAIR_AND_PERIOD3_SUPPORT_GATE_20260731.md;
* MATH_THEOREM_CATALAN_MIDDLE_LEVELS_TRACE_DECORATION_EQUIVALENCE_20260731.md;
* MATH_THEOREM_CATALAN_DECORABLE_ML7_AND_HEXAGON_TRANSFER_20260731.md;
* MATH_THEOREM_CATALAN_STANDARD_M5_THREE_C10_PRIVATE_REPAIR_20260731.md;
* MATH_THEOREM_CATALAN_M5_REPAIR_FIXED_ROTATION_ECO_INTEGRATION_20260731.md;
* MATH_THEOREM_CATALAN_ECO_COMPATIBLE_HYPERTREE_PRIVATE_COLLAR_20260731.md;
* MATH_THEOREM_AD_ECO_OWNER_ROUTED_HYPERTREE_GATE_20260731.md; and
* MATH_THEOREM_K_COHERENT_EDGE_SUPPLY_FORCED_PORT_HALL_ROUTER_CATALOGUE_20260731.md.
