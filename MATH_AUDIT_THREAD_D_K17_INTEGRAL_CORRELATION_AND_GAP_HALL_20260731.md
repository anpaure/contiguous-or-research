# Thread D: K17 integral-correlation and gap--Hall diagnostics

Date: 2026-07-31  
Status: exact reduction, exact lightweight instrumentation, and exact
partial-incumbent audits; no K17 carrier or all-dimension theorem

## 1. Authoritative rebase

Three preliminary existential questions are closed.

1. A clean-subgroup quotient of the complete diamond graph has a global
   quotient perfect matching. Its restriction supplies the exceptional
   Catalan filters. Residual-Kneser Hall is not an existential gate.
2. A Catalan linear diamond matching is exactly an ordered
   four-transversal

   \[
   L\longmapsto (U_L,T_L,H_L)
   \]

   with injective upper, tail, and head maps and an acyclic directed middle
   graph. The uniform fractional point satisfies matching, middle capacity,
   and every graphic inequality. The missing input is integral correlation,
   not fractional feasibility.
3. Inside the subclass supported by one fixed Hamilton cycle of
   \({\rm ML}(2m-1)\), the matching is exactly a two-turn decoration:
   both turn alphabets must be represented, the representatives must
   interlace, and one explicit binary-trace face must be avoided.

The third item is a sufficient architecture, not a normal form for every
Catalan linear matching. The forced support of an arbitrary matching must
first extend to a middle-levels Hamilton cycle. The audited \(m=3\)
counterexample shows that a genuine linear diamond matching need not have
such an extension.

No statement below uses the retracted claim that a Greene--Kleitman
projection has maximum linear-subforest size \(W/2\).

## 2. Gap--Hall is strictly stronger than two turn surjections

Write a middle-levels Hamilton cycle as

\[
 A_0,B_0,A_1,B_1,\ldots,A_{Q-1},B_{Q-1},A_0
\]

and put

\[
 \ell_i=A_i\cap A_{i+1},\qquad
 u_i=B_{i-1}\cup B_i.
\]

For a fixed upper SDR \(I\), the authoritative gap theorem says that lower
representatives exist if and only if the gap-vs-lower-colour graph
\(\Gamma_I\) has a perfect matching. Thus separate surjectivity of
\((u_i)\) and \((\ell_i)\) is only necessary.

The frozen \({\rm ML}(7)\) Hamilton cycle makes the distinction literal.
Both turn maps are surjective, but three consecutive unique upper turns
force two occurrences of the same intervening lower colour. Exhausting
all \(12{,}288\) upper SDRs gives best gap matching \(20/21\).
This is a cycle obstruction, not an \(m=4\) nonexistence result: one
standard incidence-hexagon toggle produces the decorable cycle below.

## 3. A simultaneous residual-cross-edge flow

The fixed-\(I\) Hall systems admit one compact simultaneous formulation.
For every upper turn colour \(U\) and lower turn colour \(L\), let

\[
 c_U=|\{i:u_i=U\}|,\qquad c_L=|\{j:\ell_j=L\}|.
\]

Assume both words are surjective. Form the layered network

\[
s\longrightarrow
\{\hbox{upper colours}\}\longrightarrow
\{A_i\}\longrightarrow
\{B_j\}\longrightarrow
\{\hbox{lower colours}\}\longrightarrow t,
\]

where:

* \(s\to U\) has capacity \(c_U-1\);
* \(U\to A_i\) has capacity one exactly when \(u_i=U\);
* \(A_i\to B_j\) has capacity one for \(j=i-1,i\), the two literal
  middle-levels cycle edges incident with \(A_i\);
* \(B_j\to L\) has capacity one exactly when \(\ell_j=L\); and
* \(L\to t\) has capacity \(c_L-1\).

### Theorem 3.1

Alternating bijective turn representatives exist if and only if this
network has flow

\[
 Q-P=\operatorname{Cat}_m.                         \tag{3.1}
\]

#### Proof

In an alternating decoration, delete the marked turn positions. Every
unmarked component of the alternating cycle is an even path, and its
unique residual cross matching covers every unmarked \(A\)- and
\(B\)-position. Exactly \(c_U-1\) occurrences of upper colour \(U\) and
\(c_L-1\) occurrences of lower colour \(L\) are unmarked. Orienting each
residual matching edge from its \(A\)-endpoint to its \(B\)-endpoint gives
a flow of value \(Q-P\).

Conversely, an integral flow of value \(Q-P\) saturates every colour
capacity because the source and sink capacity sums are both \(Q-P\).
The occurrence capacities make its \(A_iB_j\) arcs a matching. Declare
their endpoints unmarked and every other occurrence marked. Each colour
then has exactly one marked occurrence. Every cyclic block of unmarked
positions is covered by matching edges and therefore has even length, so
the marked rail types alternate. \(\square\)

Fixing the marked upper positions contracts this network to the
gap-vs-lower-colour matching of the authoritative theorem. Thus (3.1)
does not weaken gap--Hall; it resolves all upper-SDR choices in one
integral max-flow.

On the frozen \({\rm ML}(7)\) counterexample, the implementation returns

\[
 13<14=Q-P,
\]

the same deficiency one as the exhaustive best gap matching \(20/21\).
On its one-hexagon repair the same implementation returns \(14/14\).
The displayed representative sets have a zero-run of length six, so the
associated physical lift is a spanning \(\operatorname{Cat}_4=14\)-path
forest.

After a feasible flow, the binary trace is audited separately. A first
flow witness on the unique cycle face does not prove the forest subclass
infeasible; one must seek another flow or explicitly exclude that face.

### 3.2 Transparent hexagon transfer

The repair supplies the correct recursive state.  A fixed decoration
survives a standard incidence-hexagon toggle exactly when:

1. the selected local turn-colour multisets agree before and after the
   toggle, separately on the two shores; and
2. after reconnection, the last and first selected shore types on the three
   retained path fragments alternate across every new seam.

This is an exact six-port rule.  It is stronger than preserving both turn
surjections, and it is weaker than resolving gap--Hall from scratch after
every toggle.  The frozen \(m=4\) census has 31 alternating hexagons:
16 give Hamilton outputs, 10 of those outputs are decorable, and only 6
admit a decoration common to both sides.  Four Hamilton outputs require
changing representatives and six fail the decoration gate.

Hence the recursive target is a joint alternating-SDR relation propagated
along a transparent gluing tree.  Neither an arbitrary frozen SDR nor an
arbitrary published gluing tree is a valid invariant.  The K17 seam
incumbents below have not yet reached this layer because their lower turn
maps are not surjective.

The lightweight regression freezes one literal transparent row on the
repaired cycle.  For (H=10), ((a,b,c)=(0,2,4)), it replaces

\[
 (11,15),(14,30),(26,27)
 \quad\hbox{by}\quad
 (11,27),(14,15),(26,30).
\]

For the fixed common decoration, the old and new local palettes are both
([47,59,62]) on the rank-three shore and ([9,12,24]) on the rank-four
shore.  In the new orientation the retained fragments have signatures

\[
 9:(A,A),\qquad 16:(B,A),\qquad 45:(B,B),
\]

and all three new seams join opposite types.  This directly tests both
parts of the transparent criterion.  Globally, the marked sets are checked
to biject all 21 turn colours on each shore and to alternate on both the old
and new Hamilton cycles.  Both traces have zero-run histogram (6,2^{11})
and hence avoid the unique cycle face.  The regression separately checks
the displayed max-flow decoration's forest trace; the two decorations are
not conflated.

## 4. Exact K17 instrumentation

For K17 the old ground has size \(17\), the middle rail has rank nine, and

\[
 Q=\binom{17}{9}=24310,\qquad
 P=\binom{17}{10}=\binom{17}{7}=19448,\qquad
 Q-P=\operatorname{Cat}_9=4862.
\]

The diagnostic reconstructs every persisted
retained-source-plus-selected-seam graph. It records:

* rank-eight Johnson edge-colour multiplicities;
* rank-ten upper turns \(X\cup Y\);
* rank-seven lower turns
  \((X\cap Y)\cap(Y\cap Z)\) at every defined directed triple;
* path/cycle topology and undefined turn slots;
* an exact partial ordered-four-transversal ledger on the represented
  old-only rail; and
* the gap-flow test only when the input is literally one lower-rainbow
  \({\rm ML}(17)\) Hamilton cycle.

On a successful gap flow the literal unmarked occurrence pairs are retained,
not merely their digest.  They are the marks needed by a later transparent
hex census.  Such a census must first expand every directed Johnson edge
(B\to B') through its physical rank-eight incidence vertex
(B\cap B'): a hexagon changes three incidence half-edges and can reverse
whole retained fragments.  A successor-edge delta by itself does not test
boundary alternation.

For a non-Hamilton or non-rainbow path cover the SDR field is
`NOT_APPLICABLE_NON_HAMILTON_OR_NONRAINBOW`. This is deliberate. The
componentwise turn multiplicities remain exact diagnostics, but they are
not promoted to a middle-levels-decoration theorem.

Likewise, the direct four-transversal ledger is marked
`PARTIAL_OLD_ONLY_RAIL_NOT_A_CLMT_CERTIFICATE`. Current K17 seam
files do not export the infinity rail or cross-rail diamond atoms. A full
four-transversal PASS requires literal typed \((L,U,T,H)\) records for
every diamond.

The canonical seam producer now embeds this diagnostic immediately in
every persisted `candidate_roundN.json`. The independent incumbent replay
recomputes it and rejects a mismatch.

## 5. Frozen finite data

All rows below use the same independently hashed \(11\)-cycle PBBS source
factor. `A holes/dup` refers to rank-eight Johnson edge colours,
`upper holes/dup` to rank-ten turns, and `lower holes/dup` to
rank-seven turns.

| incumbent | edges | paths | cycles | A holes/dup | upper holes/dup | lower holes/dup | undefined turn slots |
|---|---:|---:|---:|---:|---:|---:|---:|
| source factor | 24310 | 0 | 11 | 0 / 0 | 0 / 4862 | 3826 / 8688 | 0 |
| hard361 | 23678 | 632 | 1 | 1695 / 1063 | 0 / 4230 | 4411 / 8035 | 1238 |
| hard323 | 23665 | 645 | 2 | 1743 / 1098 | 0 / 4217 | 4442 / 8038 | 1266 |
| quick650 | 23375 | 935 | 1 | 2133 / 1198 | 0 / 3927 | 4611 / 7662 | 1811 |
| soft437 | 23588 | 722 | 2 | 1812 / 1090 | 0 / 4140 | 4442 / 7899 | 1405 |
| active2649 | 23107 | 1203 | 1 | 3087 / 1884 | 0 / 3659 | 4929 / 7533 | 2258 |

Two conclusions are exact for these literal banks.

1. Every row keeps the rank-ten upper turn map surjective.
2. Every row fails the lower turn surjection, before gap--Hall is even
   reached.

There is also a sharp fixed-internal-turn ledger. If one merely fills the
currently undefined turn slots while retaining all already-defined turns,
then at least

\[
\max(0,\ \#\hbox{missing lower colours}
          -\#\hbox{undefined turn slots})
\]

already-defined turn positions must still be rewritten. This number is
3826 for the source and respectively \(3173,3176,2800,3037,2671\) for the
five persisted rows above. It is not an unrestricted edit-distance lower
bound, because releasing one old edge can alter multiple nearby turn
positions. It is an exact obstruction to boundary completion with all
defined turns frozen.

Thus the current upper-cover objective is not measuring the new integral
gate: the source has lower-turn deficit 3826, while the active2649 hint has
deficit 4929. Future K17 scoring should lexicographically expose

1. rank-eight edge-colour exactness;
2. lower-turn missing colours;
3. upper-turn missing colours;
4. when one Hamilton cycle is present, residual-flow/gap--Hall deficiency;
5. the binary trace face;
6. for recursive hex moves, local palette-multiset and boundary-type
   transparency; and
7. the full typed ordered-four-transversal defect after all rails are
   materialized.

## 6. Reproduction and scope

The primary files are

```text
scratch/threadD_audit_k17_integral_correlation_20260731.py
scratch/test_threadD_k17_integral_correlation_20260731.py
scratch/threadD_audit_ordered_four_transversal_20260731.py
scratch/test_threadD_ordered_four_transversal_20260731.py
```

The first tiny regression replays the \({\rm ML}(7)\) flow deficit
\(13/14\), the repaired value (14/14), the literal transparent hex row,
the protected forest trace, and the frozen K17 source turn census. The
second independently checks complete and partial ordered-four-transversal
schemas.

The authoritative mathematical dependencies are

```text
MATH_THEOREM_CATALAN_LINEAR_MATCHING_EXACT_REDUCTIONS_20260731.md
MATH_THEOREM_CATALAN_MIDDLE_LEVELS_TRACE_DECORATION_EQUIVALENCE_20260731.md
MATH_THEOREM_CATALAN_ALTERNATING_TURN_SDR_HALL_AND_M4_COUNTEREXAMPLE_20260731.md
MATH_THEOREM_CATALAN_DECORABLE_ML7_AND_HEXAGON_TRANSFER_20260731.md
MATH_THEOREM_CATALAN_FILTERS_FROM_GLOBAL_QUOTIENT_MATCHING_20260731.md
```

No finite row above is a K17 carrier, no arbitrary Catalan linear matching
is asserted to be middle-levels-resolvable, and no all-\(m\) existence
claim is made.
