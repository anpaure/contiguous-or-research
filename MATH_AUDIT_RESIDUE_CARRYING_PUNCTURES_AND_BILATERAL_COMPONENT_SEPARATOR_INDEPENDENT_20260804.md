# Independent audit of residue-carrying punctures and the bilateral separator

**Date:** 2026-08-04  
**Verdict:** the arithmetic construction, punctured two-frame iff, bilateral
multicut and edge-connectivity corollaries, and one-puncture reduction are
correct under their stated hypotheses.  The theorem required notation and
scope repairs before its macro-residence handoff.  Those repairs have been
applied to the theorem source.

No internet search, external service, or H100 computation was used.

## 1. Audited sources

The target was read completely.  The two companion notes were read only to
check the boundaries inherited from the two-adic selector and macro-resident
theorems.

| role | file | SHA-256 |
|---|---|---|
| target before audit | `MATH_THEOREM_RESIDUE_CARRYING_PUNCTURES_AND_BILATERAL_COMPONENT_SEPARATOR_20260804.md` | `a53d8a562d9c78129f0ee86f7aa5bee758ffc7012c5c67a03706a731505874dd` |
| target after audit | same file | `bd0f567bcd91f09e6c40216d08c0463e7abbe495756392095e5839ea8d690fbd` |
| arithmetic/scope companion | `MATH_THEOREM_PAIR_CELL_TWO_ADIC_SELECTOR_OBSTRUCTION_20260804.md` | `4a0146a86d401405c5c6fd08c00f8e9d7f22e013689f27ae32ae8f3759226423` |
| macro/scope companion | `MATH_THEOREM_MACRO_RESIDENT_HALL_COLLAR_HOLONOMY_AND_SWITCH_TREES_20260804.md` | `8eda00a24bdebaf2b43e65a4e71e7564e25d3bdfcb5bbd3bff7bc7f208808eca` |

The hashes in this table are byte hashes, computed with `sha256sum`.  The
audit-note hash is necessarily reported outside this self-referential note.

## 2. Corrections made

1. The scalar modulus formerly denoted `Q=2^M` collided with the partition
   named `Q` in Theorem 3.1.  It is now `q_M=2^M` throughout the arithmetic
   and one-puncture statements.  This is a notation repair, not a change to
   any congruence.
2. Section 5 now explicitly assumes `q_M>=2D`.  Lemma 2.1 used this
   hypothesis, but the former one-puncture section only mentioned it after
   defining admissible lengths.  The explicit assumption guarantees both a
   nonempty admissible length set and the size bound needed for every
   available whole block.
3. Section 6 formerly inferred that every selected whole cell was an
   internally resident path merely from the owner partition.  It now
   separately assumes a cyclic `D`-resident Hamilton ordering on every
   selected whole cell, states that those orderings come from a separate
   local good-cell theorem, and records the exact convention: `D` vertices
   are `D-1` internal edges.
4. The multicut prose is now hypothesis-safe.  Corollary 4.1 concerns the
   full deleted set `U` under its survival convention.  When additional
   third-frame cells `S` are preselected, it does not imply that the interval
   alone is a multicut.  Theorem 3.1 remains the exact statement when a
   touched block is absent from the residual graph.

No changes were needed in the two companion notes.

## 3. Arithmetic verification

Write `W_r=2^s u` with `u` odd, where the companion theorem proves
`s=nu_2(W_r)=s_2(r)`.  Since `M>s`,

\[
 W_r\bmod 2^M
 =2^s\bigl(u\bmod 2^{M-s}\bigr).
\]

The parenthesized residue is odd and nonzero.  Therefore
`1<=omega<q_M` and `nu_2(omega)=s`.  If all selected blocks except one
proper block `B` have cardinality divisible by `q_M`, then

\[
 |B|\equiv W_r\equiv\omega\pmod {q_M},
\]

so the same factorization proves `nu_2(|B|)=s`.  Proposition 1.1 is the
same divisibility argument after support-neutral pieces are grouped by
source cell; no equality of individual path lengths is used.

For Lemma 2.1, `m>=M+1` gives `N=2^m>=2q_M`.

- If `omega>=D`, then `b=omega` has `b>=D` and
  \[
  N-b\ge2q_M-(q_M-1)=q_M+1\ge D.
  \]
- If `omega<D`, integrality gives `omega<=D-1`.  With
  `b=omega+q_M`,
  \[
  N-b\ge2q_M-q_M-(D-1)=q_M-D+1\ge D+1.
  \]

In both cases `b` has the required residue, `D<=b<=N-D`, and both cyclic
pieces are proper.  Restricting a cyclic resident transition word to either
contiguous piece preserves internal residence.  Every displayed arithmetic
inequality is therefore valid.

## 4. Punctured two-frame iff

For every owner remaining after deletion of `U`, with incident residual
blocks `A` and `B`, exact coverage is

\[
 x_A+y_B=1.
\]

A block that is unavailable or meets `U` cannot be selected whole, so its
variable is fixed to zero.  Along a connected residual component, all
left-shore variables equal one bit `c` and all right-shore variables equal
`1-c`.  A forbidden left vertex forces `c=0`; a forbidden right vertex
forces `c=1`.  Thus a solution exists exactly when no component contains
forbidden vertices on both shores.  Components with neither kind of forced
vertex admit either binary orientation.

Blocks wholly contained in `U` have no residual owner and correctly receive
no residual variable.  The selected original whole blocks are disjoint from
`U` because every block meeting `U` is forced to zero.  Hence the proof
covers every owner exactly once in both directions and Theorem 3.1 is an
iff, not merely a necessary condition.

An exhaustive independent check generated every pair of set partitions of
universes of sizes one through four, every subset `U`, and every availability
pattern on both shores.  In all 145,400 instances, direct enumeration of
whole-block extensions agreed with the component criterion.

## 5. Bilateral multicut and edge connectivity

Under Corollary 4.1's explicit survival hypothesis, each endpoint of every
deleted owner edge remains a residual forbidden vertex.  If the two
endpoints were connected after deletion, their component would contain a
forbidden vertex on each shore, contradicting Theorem 3.1.  Consequently
every residual component has touched vertices on at most one shore, and
each deleted edge joins opposite component types.  The three listed types
are exhaustive.

For nonempty `U`, at least one deleted edge has separated endpoints, so
`Gamma(P,Q)-U` is disconnected.  If `Gamma(P,Q)` is
`lambda`-edge-connected, the definition of edge connectivity immediately
gives `|U|>=lambda`.  The connected-residual-graph no-go is the same
contrapositive.  Both corollaries are valid.

For additional reassurance, the exhaustive partition sweep above checked
all 138 nonempty extendible punctures satisfying the survival hypothesis;
every deleted edge had endpoints in different components and no component
contained touched blocks from both shores.

If one instead retains original blocks wholly contained in `U` as
zero-degree vertices of the edge-deleted multigraph, those vertices are
isolated and an analogous full-`U` endpoint-separation statement follows.
The theorem source conservatively uses its explicitly defined nonempty
residual graph and states the corollary only with survival.

## 6. One-puncture equivalence

Cells in the third frame form a partition, so the interval in `C` and the
other whole cells in `S` are pairwise disjoint.  For a fixed admissible
`(a,b)`, they are exactly the preselected pieces allowed by Theorem 3.1.
All other selected cells have dimension at least `M` and hence size
divisible by `q_M`.  Reduction of the owner count modulo `q_M` gives the
necessary congruence for `b`, while Lemma 2.1 supplies at least one length
obeying both boundary margins.

Theorem 3.1 is then precisely necessary and sufficient for filling the
remaining owners by whole available cells from the first two frames.
Existential quantification over `a` and the admissible `b` proves Theorem
5.1.  It does not prove that any such interval meets the component
criterion.  With `S` nonempty, the multicut conclusion concerns the full
set `U=I(a,b) dotcup union S`, not the interval by itself.

## 7. Residence convention and scope

The macro companion writes a path as
`P_i=(v_{i,0},...,v_{i,ell_i})` and assumes
`ell_i>=D-1`.  Thus its sharp threshold is `D` vertices, not `D` internal
edges.  In the corrected handoff:

- the interval has `b>=D` vertices;
- every whole available cell has at least `q_M>=2D` vertices; and
- opening an assumed cyclic resident Hamilton ordering deletes only its
  closing edge and preserves internal residence.

Therefore each resulting path has at least `D-1` internal edges, exactly
matching the macro theorem.  This licenses only an application of that
theorem after its remaining hypotheses are proved.  It does not prove
seam-safe connector Hall, collar holonomy, a loopless Hamilton cycle in the
seam graph, or protected switch ports.

The scope is consistent with both companion notes:

- the two-adic companion rules out an all-whole-cell selector but expressly
  leaves residue-carrying cuts open;
- the macro companion assumes literal vertex-disjoint resident paths and
  explicitly does not construct them from all pairing frames; and
- the audited theorem characterizes the owner-incidence row but proves no
  separator existence, macro Hall, holonomy, upper palette, or compiler.

Accordingly, the repaired theorem establishes the local arithmetic freedom
and the exact owner-incidence criterion only.  It does not establish a
resident spanning factor or Hamilton cycle.

## 8. Finite verification summary

A separate integer/partition harness, run locally without writing an
artifact, reported:

```text
arithmetic_cases=2839032
component_equivalence_cases=145400
extendible_surviving_punctures_checked=138
```

The arithmetic sweep covered `1<=r<=400`, `s_2(r)<M<=s_2(r)+6`, every
`1<=D<=2^{M-1}`, and `M+1<=m<=M+4`.  These computations are corroborative;
the proofs in Sections 3--7 above are the authoritative verification.
