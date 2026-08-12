# Audit of the protected Catalan--pivot born connector and prepared scaffold

**Date:** 2026-08-02  
**Audited file:**
`MATH_THEOREM_K_PROTECTED_CATALAN_PIVOT_CONNECTOR_BIRTH_AND_PREPARED_SCAFFOLD_GATE_20260802.md`  
**Audited SHA-256:**
`9fcafa30d5a1b63ae97a4dd89290cd8bb1d385d417365747fa2b0d4874b2434a`  
**Verdict:** PASS with the explicit scope qualifications below.  In
particular, Corollary 2.2 is a correct owner/immediate-upper statement, not
an all-width safe-opening theorem, and `PCPS(m,d)` remains essentially the
joint temporal Hamilton-scaffold construction.

## 1. Parameter and protected-seed audit

The collared pivot uses `m+3d` coordinates inside `[2m-1]`; this is
equivalent to

\[
                         m\ge 3d+1.                    \tag{1.1}
\]

Its predecessor phase has `3d` disjoint incidence edges.  Inequality (1.1)
gives `3d<=m-1`, exactly the range of the cited small-matching extension.
For every extension `M_0`, the successor edges contract as

\[
 I_0\to I_1\to\cdots\to I_{3d-1}\to M_0^{-1}(V_{3d}). \tag{1.2}
\]

The terminal preimage cannot equal an earlier `I_i`, since those earlier
vertices already have distinct images under the matching.  Proposition 1.1
is therefore correct.  It proves a protected common-independent path only;
it does not extend that path to a global upper transversal.

## 2. Born-connector theorem

Let `Q` satisfy Theorem 2.1.  Its `W-1` rooted links have indegree and
outdegree at most one.  Graphic independence gives a forest on `W` rooted
vertices with `W-1` edges, hence one spanning tree; under the degree bounds
that tree is a directed Hamilton path.

Choose one `Q` edge for every one of the `U` upper colours, forcing the
prescribed protected occurrence whenever its colour is one of the `3d`
protected colours.  Distinct colour classes cannot select the same edge.
The chosen set `Q_0` is a subset of a forest, has `U` edges, and therefore
has exactly

\[
                         W-U=C                          \tag{2.1}
\]

components.  The remaining `C-1` path edges use precisely the free ports of
those components and occur in their inherited order.  This proves all five
items and the converse.  No independent Catalan connector existence theorem
is hidden in the argument: the final Hamilton path `Q` is the prospective
input from which both pieces are extracted.

## 3. Corollary 2.2

Fix the alternating phase so the pivot predecessor shore lies in `M_0` and
its successor shore `P_1` lies in the other perfect matching `Q`.  The
rooted Hamilton cycle has `W` upper-turn occurrences but only `U` colours.
Let `s>=1` be the number of colours with multiplicity at least two.  The
total number of occurrences belonging to repeated colours is

\[
                         (W-U)+s=C+s\ge C+1.            \tag{3.1}
\]

For `m>=3`, `C=Cat_m>=m`.  Together with `m>=3d+1`,

\[
                         C+1>3d=|P_1|.                 \tag{3.2}
\]

Hence at least one occurrence of a repeated colour is a `Q` edge outside
`P_1`.  Removing that incidence edge opens the rooted cycle, avoids the
whole protected incidence path, and leaves another occurrence of its upper
colour.  The resulting `Q` has size `W-1`, is graphic-independent and is
still upper-surjective, so Theorem 2.1 applies.

This is exactly the claimed owner/immediate-upper conclusion.  It does not
show that the corresponding cut of a cyclic **source word** preserves a
higher-width occurrence: the unique occurrences of many nested upper
targets may all cross that cut.  The qualification immediately following
Corollary 2.2 is therefore necessary and correctly stated.

## 4. Closed-shore flow check

For completeness, Theorem 2.3's inequality direction is correct.  In the
network with source-to-root capacity two, root-to-containing-owner capacity
one and owner-to-sink capacity `c_T`, fix the owners `Y` on the source side.
A root contributes

\[
                 \min\{2,|N(L)-Y|\}                    \tag{4.1}
\]

to a minimum cut.  Relative to its required two units, the deficit is two
when `N(L) subseteq Y`, one when exactly one neighbour escapes `Y`, and zero
otherwise.  Thus max-flow/min-cut is precisely

\[
            2I_A(Y)+J_A(Y)\le\sum_{T\in Y}c_T.         \tag{4.2}
\]

The flow closes only the root/owner degree row.  The stated contracted
graphic-rank condition is still required to make the selected edges a
connector path.  In addition, the omitted lower root `o` must satisfy
`o subset s` or `o subset t` for one intended owner endpoint.  This is the
exact extra incidence needed to recover a perfect rooted phase from the
unrooted Hamilton path; without it the flow and graphic rows may both pass
while no perfect `M_0` follows.

## 5. Residence and all-width inheritance

The clipped residence state in Section 3 is exact for the positive-run
convention.  Every run after concatenation is either an old internal run or
a sum of a suffix run, any intervening all-one fragments, and a prefix run.
Lengths clipped at `D=d+1`, endpoint bits, the all-one flag and the internal
good bit retain exactly the information needed to reject a new short
internal run.  The product over coordinates is therefore exact.

Lemma 4.1 is also exact: a crossing interval already contains both adjacent
old letters, so the inserted `X` is redundant exactly under
`X subseteq A_-1 union A_1`.  This preserves every old interval value but
may increase its width by one.

Both results are chronology-relative.  They apply to the one prepared word
`A^- -> A^+`; neither survives an arbitrary later permutation of Catalan
components without a new occurrence/history audit.

## 6. Prepared-scaffold semantics

Theorem 5.1 is a valid composition theorem.  Its six defining conditions
already own the following load-bearing global work.

* Item 2 assumes complete all-width upper coverage in the preword.
* Item 4 assumes the final `W`-owner, upper-turn-surjective alternating
  Hamilton path and its one controlled nonowner boundary cell.
* Item 6 assumes the two clipped residence interfaces are accepted.
* The final compiler sentence assumes one common cap for the transported
  background and pivot rays.

The theorem then correctly derives the rooted Catalan forest and its
`C-1` connectors by Theorem 2.1, residence by the boundary-state lemma,
all-width inheritance by monotonicity, and zero local compiler damage by
the rank-`m` crossing-cell ledger.

Accordingly `PCPS(m,d)` is not proved by the note and is not a weak marginal
condition.  It is the prospective joint construction of a nonflat temporal
preimage and an integral protected upper-turn Hamilton chronology, plus the
upper, residence, compiler and regeneration rows.  The theorem is useful
because it shows that a separately selected rooted forest and connector are
unnecessary on this prospective face; it does not make the Hamilton
scaffold automatic.

## 7. Comparison with the factor-first safe-switch route

There are two proof-safe architectures.

1. **Prepared path first.**  Construct `PCPS(m,d)` directly.  The rooted
   Catalan forest and the entire Catalan connector path are then born as
   subsets of the final chronology.  There is no cycle opening after the
   insertion.
2. **Factor first.**  Construct an accepted cycle factor containing the
   pivot, then select a private or hereditary family of binary pulls and
   ternary Boolean hexes whose component footprints form a spanning
   incidence tree.  Their full exported state must include residence
   histories and occurrence-labelled upper witnesses with total increment
   zero.

The second route has two additional gates absent from the first: existence
of the compatible safe-switch incidence tree and a final opening which is
transparent to the entire upper atlas.  Immediate-upper redundancy from
Corollary 2.2 supplies the opening only at rank `m+1`.  Residual LKK/Ore
expansion supplies marginal factor existence only and proves neither gate.

The factor-first route may nevertheless permit looser component-local
source states than a single prepared Hamilton scaffold.  It is an
alternative sufficient architecture, not a consequence of the born-
connector theorem.

## 8. Final scope

The audited note correctly proves:

* the protected pivot seed for `m>=3d+1`;
* the exact prospective Hamilton-path/Catalan-forest/connector equivalence;
* the immediate-upper-safe owner-layer opening in Corollary 2.2;
* exact clipped residence composition; and
* conditional inheritance from a prepared scaffold.

It does not prove `PCPS(m,d)`, an all-width-safe cycle opening, the ambient
common compiler, same-parity regeneration, or an all-dimensional upper
bound.
