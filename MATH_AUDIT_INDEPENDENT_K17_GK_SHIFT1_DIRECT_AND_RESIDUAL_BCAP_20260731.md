# K17 shift-one: direct exceptional ears and residual b-capacity

Date: 2026-07-31  
Status: **GO** for the 572 direct-ear packet and for a residual 8,164-provider
b-capacity transversal. **OPEN** for wedge/rank-nine repair and the 4,534-edge
repeat f-factor.

## 1. Why the no-EE schedule is impossible

In the authenticated shift-one post-fixed provider graph, exactly 572 of the
8,736 missing rank-six colours have no EU or UU provider. Every provider for
each of those rows is endpoint--endpoint. Their degree histogram is

```text
degree 3: 42, 4: 42, 5: 45, 6: 56, 7: 90, 8: 297,
```

for 3,861 total BB options. Thus forbidding endpoint--endpoint edges creates
572 literal zero rows. The no-EE model is infeasible before any nontrivial
capacity or SAT reasoning.

## 2. Forced scalar correction

Let `x_j` denote the number of `j`-edge ears. Assign the 572 exceptional
colours to direct one-edge ears. The exact completion ledger is then

\[
  (x_1,x_4,x_5)=(572,2637,430).
\]

Indeed,

\[
 572+2637+430=3639,
 \qquad 3(2637)+4(430)=9631,
\]

and

\[
 572+4(2637)+5(430)=13270.
\]

The corresponding edge types are

\[
 (EE,EU,UU)=(572,6134,6564),
\]

with exactly 7,278 base-endpoint incidences and 19,262 unused-vertex
incidences.

## 3. A stronger 572-ear certificate

An exact CP model chooses one BB provider for each exceptional colour while
requiring simultaneously:

* 572 distinct rank-eight unions;
* 1,144 pairwise distinct base endpoints; and
* 1,144 pairwise distinct boundary rank-nine turns.

It solved in 0.028 seconds. A dependency-free replay verifies every provider
against the full active relation and checks the identities

\[
 D=L\cap R,qquad Q=L\cup R,
\]

and both boundary turns against the fixed old mates. Thus all 572 direct ears
are already locally and palette clean.

The certificate is

```text
scratch/independent_k17_gk_shift1_exceptional_bb_20260731.tsv
SHA-256 7abcbd84c926a4b6fb7154b2b2554d07282508eae10e7b411e2b9a2217231b8d
```

## 4. Residual ordinary Hall remains full

After deleting the direct ears' q8, endpoint, and boundary-h9 resources, the
remaining provider graph has

```text
rows                 8164
zero rows               0
rank-eight resources 11906
incidences          242771
EU incidences         57008
UU incidences        185763
ordinary matching rank 8164.
```

The stronger demand that the 8,164 designated providers themselves use all
6,134 eventual EU slots is impossible: only 4,531 residual base endpoints
occur in any provider option. Therefore at least 1,603 EU edges must come
from the later repeat/decorated bank. This is a literal resource cut, not a
solver timeout.

## 5. Residual b-capacity certificate

Removing that unnecessary equality, an exact model imposes:

* one provider for each remaining rank-six colour;
* distinct rank-eight unions;
* capacity one at every unused base endpoint;
* capacity two at every unused rank-seven vertex;
* all EU boundary rank-nine turns distinct and disjoint from the direct-ear
  turns; and
* at least 1,600 EU provider edges, the necessary repeat-budget floor.

With no starting hint, CP-SAT found a certificate in 53 seconds:

```text
selected providers 8164
EU / UU             3065 / 5099
base degrees 0 / 1  3071 / 3065
unused degrees 0/1/2 4416 / 2241 / 5511
distinct boundary h9 including direct ears 4209.
```

The certificate is

```text
scratch/independent_k17_gk_shift1_residual_cap_20260731.tsv
SHA-256 7e5706b65996e6d303108114c69f41c381a8743799da048c928eb9b2e50a47ff
```

## 6. Exact remaining f-factor debt

The full schedule needs 6,134 EU and 6,564 UU edges. Hence the 4,534 repeat
edges must split as

\[
  (EU_{\rm repeat},UU_{\rm repeat})=(3069,1465).
\]

The provider selection currently touches 7,752 unused vertices. Select a
further 1,879 zero-degree unused vertices to reach the required 9,631. The
residual unused-degree demand is

\[
 2241+2(1879)=5999=3069+2(1465).
\]

Among the 3,071 unused base endpoints, 3,069 must receive repeat EU edges,
leaving exactly two global terminals. Thus every scalar and degree row closes
exactly.

## 7. Remaining local defects

The b-capacity model does not force the two selected provider edges at a
degree-two unused vertex to form a legal wedge. Literal replay finds:

```text
unused degree-two vertices       5511
illegal selected wedge pairs       17
compatible selected wedge pairs  5494.
```

The compatible central turns use only 3,991 distinct rank-nine values, so
there are 1,503 repeated central-turn units. Another 261 central values
collide with the already unique boundary-turn bank. The current provider
selection therefore has 1,764 rank-nine collision units.

These numbers diagnose this certificate; they are not lower bounds for all
b-capacity transversals. The next model must choose providers, wedges, central
rank-nine colours, and the residual repeat f-factor together.

## 8. Scope and artifacts

Nothing here proves the 4,534 repeat-edge f-factor, one component path, the
prefix, upper ranks, or a length-24,313 word.

Independent artifacts:

* `scratch/solve_independent_k17_gk_shift1_exceptional_bb_20260731.py`
* `scratch/audit_independent_k17_gk_shift1_exceptional_bb_20260731.py`
* `scratch/independent_k17_gk_shift1_exceptional_bb_replay_20260731.audit.json`
* `scratch/solve_independent_k17_gk_shift1_residual_cap_20260731.py`
* `scratch/audit_independent_k17_gk_shift1_residual_cap_20260731.py`
* `scratch/independent_k17_gk_shift1_residual_cap_replay_20260731.audit.json`
