# Independent audit: the `k=17` GKS packet contraction is exact, the current-owner lift is automatic, and common cap is external-only

Date: 2026-08-01  
Lane: L, independent proof/scope audit  
Status: PASS with the one-endpoint and unguarded qualifications below; no
transition-compatible age cycle or optimal `k=17` word is claimed

## 1. Audited claims

This audit checks

* `MATH_THEOREM_L_GKS_K17_CHAIN_SPLITTING_AND_RESIDUAL_FLAG_HALL_GATE_20260801.md`;
* `MATH_THEOREM_L_K17_CYCLIC_AGE_ORBIT_HALL_FLAG_AND_COMMONCAP_GATE_20260801.md`;
* the controlled central surgery frozen in
  `MATH_THEOREM_A_K17_GKS_RANK678_CONTROLLED_SURGERY_AND_LOW_FLAG_GATE_20260801.md`;
* the direct-age-source/common-cap scope against
  `MATH_AUDIT_L_AGE_COMPOSITION_AND_TERMINAL_COMPILER_SCOPE_20260801.md`.

The primary-source claim was checked against Theorem 3 of Griggs--Killian--
Savage, *Venn Diagrams and Symmetric Chain Decompositions in the Boolean
Lattice*, EJC 11 (2004), R2.  The paper proves a prime-necklace representative
SCD and a chain-cover map: a nonroot starter covers a parent-chain element and
its terminator is covered by a parent-chain element.  It does not claim that
arbitrary interior fragments can be reassigned to arbitrary middle owners.

## 2. Exact arithmetic and the cover-ray obstruction

For ranks `1<=s<=16`, every nontrivial `Z_17` orbit is free and

\[
 N_s={1\over17}{17\choose s}.
\]

Together with the fixed empty orbit, this gives lower-half counts

\[
 (N_0,\ldots,N_8)=(1,1,8,40,140,364,728,1144,1430)
\]

and SCD birth counts

\[
 (1,7,32,100,224,364,416,286)
\]

at starts `0,2,...,8`.  The cap-three native overflow is

\[
 5+7(4)+32(3)+100(2)+224=553,
\]

while independent cap-three splitting creates 1802 fragments, 372 more than
the 1430 available roots.  These computations are exact.

The GKS parent formula sends a nonroot starter `z` to the chain beginning at
`alpha(z)`, with the rank-two special case attached to the root chain.  Thus
the literal start-cover atlas gives the root-interior targets of ranks two
through seven only the root owner.  Six non-rank-eight targets compete for
two remaining packet slots, so at least four off-atlas placements are
necessary.  This is a scoped obstruction to the cover-ray atlas, not to the
full necklace containment graph.

## 3. The automatic current-owner theorem

Let `O_8,O_9` be the two 1430-element orbit shores.  In the quotient
**multigraph** of aligned containments `Q subset T`, every node has
multidegree nine.  Hence for `X subset O_8`,

\[
 9|X|\leq9|N(X)|.
\]

The simple support satisfies Hall.  Bipartite edge colouring strengthens
this to a decomposition of the alignment multigraph into nine perfect
matchings.  Selecting one actual parallel edge retains the relative shift;
rotating a whole packet gives literal `Q subset T` in all 17 phases, and

\[
                         C_3=T\setminus Q
\]

is the unique oldest class.  Therefore an unguarded packetization whose
rank-eight roots are all distinct has no further current-owner Hall gate.

The qualifications are necessary:

1. regularity is a statement about the alignment multigraph, not necessarily
   its simple support;
2. packets must be freely rotatable and impose no owner/phase/transition/
   trace restriction beyond `Q subset T`; and
3. the matching assigns only the current owner.  It does not choose a
   successor, prove `Q=T intersection T'`, or construct a Johnson cycle.

## 4. Contracted exact cover and the authenticated central solution

The certificate shapes force 286 rank-six heads (`A,D,G`) and all 1144
rank-seven targets as heads (`B,C,E,F,H,I`).  The remaining marked low slots
are exactly

\[
 O_2\to C_7,quad
 O_3\to D_6\sqcup E_7,quad
 O_4\to F_7,quad
 O_5\to G_6\sqcup H_7,quad
 O_6\setminus H_6\to I_7.
\]

These counts are respectively `8,40,140,364,442`; they exhaust every target
orbit of ranks two through six once.  Conversely, containment bijections on
these rows plus a head-to-root bijection reconstruct every nested packet,
so the two-layer model is an iff, not merely a relaxation.

The authenticated 286-edge controlled surgery has payload status
`PASS_K17_GKS_RANK678_CONTROLLED_SURGERY` and exact split

\[
                 442\ (6<7<8),\qquad286\ (6<8),\qquad702\ (7<8).
\]

It therefore supplies the head-to-root layer and the rank-six low/head row.
The residual unguarded static gate is precisely the simultaneous choice of
type bins for the four rank-two--five containment matchings.  No packet--
owner variables are needed.

## 5. Compiler scope

If those packets are placed on a transition-compatible age cycle, their
suffixes are literal letters of the final source.  There is then no separate
lower common-cap rounding.

For an external pre-existing carrier, common cap remains independent.  If
`M` is the selected occurrence-labelled target/cell family and
`Ebar_p` is the carrier envelope, the maximal cap is

\[
 A_p(M)=\overline E_p\cap
        \bigcap_{(S,C)\in M:\ p\in C}S.
\]

Every cap must be nonempty and reproduce all protected owner/upper rows and
selected lower cells.  Cyclic equivariance only rotates these equations.
It neither proves trace guards nor maximal-cap reproduction.

## 6. Verdict

The corrected hierarchy is

\[
\boxed{
\begin{array}{c}
\text{GKS SCD and controlled central surgery}\quad\text{proved}\\
\Downarrow\\
\text{four coupled rank-two--five low/head Hall systems}\quad\text{open}\\
\Downarrow\\
\text{static current-owner lift}\quad\text{automatic}\\
\Downarrow\\
\text{successor/transition/voltage and upper-safe opening}\quad\text{open}.
\end{array}}
\]

The static simplification is exact.  It does not imply the chronological
flag cycle, and it does not create an external-carrier common cap.

## 7. Frozen hashes

```text
MATH_THEOREM_L_PINNED_TRIANGULAR_ROOTED_TRACE_AND_PRIVATE_COMMONCAP_20260801.md
  bc15e1681dd31306a83640d6269109d6413d588535bd701c0782459c12e8ce7c
MATH_AUDIT_L_AGE_COMPOSITION_AND_TERMINAL_COMPILER_SCOPE_20260801.md
  991b7577bed3f07852c2abc272c88c5c9000f978a30d928ccc04eb32e4fc3479
MATH_THEOREM_L_K17_CYCLIC_AGE_ORBIT_HALL_FLAG_AND_COMMONCAP_GATE_20260801.md
  eb095d124e67e069a169367e9a9408b9c089a43ce1e482bd687173c8374415f5
MATH_THEOREM_L_GKS_K17_CHAIN_SPLITTING_AND_RESIDUAL_FLAG_HALL_GATE_20260801.md
  0bdf3eea355b5f5149bc0ba111aa7a13a48ab09a5704e93c6bd7a8ab43092c11
MATH_THEOREM_A_K17_GKS_RANK678_CONTROLLED_SURGERY_AND_LOW_FLAG_GATE_20260801.md
  e81937e57d3efebacb00aae8737a3e394ff895147d064aaf912d43c242ea833b
scratch/threadA_k17_gks_rank678_surgery_20260801.tsv
  921691cb12940fd05ef5d68938cd6fa3bdc953f5b12226ca0a39357315265baa
scratch/threadA_k17_gks_rank678_surgery_20260801.audit.json
  4270becd566084776e7046532322068a92d1b78def4853f3692d21e661f55771
```
