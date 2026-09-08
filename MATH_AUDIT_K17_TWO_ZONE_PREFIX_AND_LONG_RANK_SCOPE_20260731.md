# Corrected audit of the `k=17` two-zone prefix and long-rank gates

Date: 2026-07-31  
Status: exact scoped audit after the mixed-width chronology correction.  The
current alternating prefix is **not disproved**.  The rank-plateau theorem
and its `3699` displacement bound apply only to an obsolete uniform
four-window prefix.  The live prefix gate is an occurrence-labelled
upper-rainbow path in `J(17,8)`, followed by two seam triples.  Tail
completion and ranks `10,...,17` remain open.

## 0. Correction and verdict

The scalar identity `7401` admits two different decompositions:

\[
 7398+3=7401,
 \qquad
 7399+2=7401.                                         \tag{0.1}
\]

The first is `7398` internal prefix **four-windows** plus three crossing
four-windows.  It is not the one-pivot schedule.  The actual schedule is the
second: `7399` internal prefix **triple windows** plus two crossing triples.
The tail contributes `16909` internal quadruples, so

\[
                    7399+2+16909=24310=\binom{17}{9}. \tag{0.2}
\]

This distinction reverses the urgent obstruction verdict:

* the four-window plateau theorem is correct on its stated face;
* its hypotheses are false for the current prefix;
* the `3699` lower bound is therefore irrelevant to the live two-zone
  architecture; and
* no authenticated theorem or finite certificate presently proves the
  entire alternating prefix impossible.

The exact prefix remains a difficult global rainbow/factorization gate.  It
is open, not constructed.

## 1. Exact mixed-depth lower and owner rows

Write the candidate as \(Q=P\Vert T\), with

\[
 |P|=7401,\qquad |T|=16912.                           \tag{1.1}
\]

The lower selected cells are unchanged:

* prefix letters and all `7400` prefix adjacent pairs;
* tail letters, all `16911` tail adjacent pairs, and all `16910` tail
  triples; and
* the one `P|T` adjacent pair.

These are intended to partition ranks `1,...,8` exactly.

Let \(q_0,\ldots,q_{7400}\) be the prefix letters and put

\[
 C_i=q_i\cup q_{i+1},\qquad0\le i<7400.               \tag{1.2}
\]

The internal prefix rank-nine owners are

\[
 H_i=q_i\cup q_{i+1}\cup q_{i+2}
    =C_i\cup C_{i+1},qquad0\le i<7399.               \tag{1.3}
\]

Two further triple windows cross `P|T`.  If
\(T=(t_0,t_1,\ldots)\), they are

\[
 q_{7399}\cup q_{7400}\cup t_0,qquad
 q_{7400}\cup t_0\cup t_1.                           \tag{1.4}
\]

The tail owners are its `16909` internal four-letter unions.  Equations
(1.3), (1.4), and the tail row are the complete mixed rank-nine chronology.

## 2. Exact prefix path reduction

### Theorem 2.1 (upper-rainbow Johnson path equivalence)

The `7400` prefix adjacent unions are distinct rank-eight masks and the
`7399` internal prefix owners are distinct rank-nine masks if and only if

\[
                         C_0,C_1,ldots,C_{7399}       \tag{2.1}
\]

is a vertex-simple path in `J(17,8)` whose edge-union labels
\(C_i\cup C_{i+1}\) are pairwise distinct.

At any position where the middle physical letter \(q_{i+1}\) is a
rank-seven separator,

\[
                         q_{i+1}=C_i\cap C_{i+1}.      \tag{2.2}
\]

#### Proof

By (1.3), \(|H_i|=9\) exactly when the distinct rank-eight sets
\(C_i,C_{i+1}\) are adjacent in `J(17,8)`.  Distinct adjacent-pair cells
make the vertices in (2.1) simple; distinct owner colours make the edge
unions rainbow.  Conversely, expanding such a path through the literal
letters gives exactly (1.2)--(1.3).  If \(|q_{i+1}|=7\), it is contained in
both adjacent rank-eight unions.  Their Johnson intersection has rank
seven, proving (2.2).  \(\square\)

Thus, after fixing the `7400` tail-complement rank-eight colours and
reserving two seam rank-nine colours, the trace gate is an upper-rainbow
Hamilton path on that residual vertex set, followed by literal
factorization into the prescribed blocks and separators.  This is necessary
and sufficient for the internal prefix trace, but not for the tail,
all-width upper tower, or full word.

The newer coloured-inventory certificate strengthens the input: all `2328`
two-letter blocks can be chosen with distinct low letters **and distinct
internal rank-eight unions**.  Its local separator graph is connected and
dense.  This removes an earlier inventory concern but does not solve (2.1).

## 3. Why the rank plateau does not apply

Define the prefix four-window

\[
 F_i=q_i\cup q_{i+1}\cup q_{i+2}\cup q_{i+3}
    =H_i\cup H_{i+1}.                                 \tag{3.1}
\]

If the live prefix condition holds, \(H_i\ne H_{i+1}\), and both rank-nine
sets contain the common rank-eight set \(C_{i+1}\).  Consequently

\[
 H_i\cap H_{i+1}=C_{i+1},
 qquad |F_i|=10.                                     \tag{3.2}
\]

The plateau lemma instead assumes \(|F_i|=|F_{i+1}|=9\).  Under that
assumption it correctly forces consecutive four-windows to coincide.  In
the present schedule, however, (3.2) shows that the rank-nine premise is the
negation of the desired triple-rainbow behaviour.  The conditional path
capacity `3701` and displacement `7400-3701=3699` remain valid only for a
redesign that insists on rank-nine four-windows.

### Literal local counterexample to a triple-window plateau

Take the separator--block--separator fragment

\[
\begin{aligned}
B_0&=\{1,2,4,5,6,7,9\},\\
A  &=\{1,2,3\},\\
D  &=\{4,5,6,7,8\},\\
B_1&=\{1,2,4,5,6,7,10\},\\
A' &=\{1,4,5,11\}.
\end{aligned}                                        \tag{3.3}
\]

Here `(A,D)` is a legal disjoint `(3,5)` block.  The four adjacent unions
are distinct rank-eight sets.  The three triple owners are

\[
 \{1,\ldots,9\},\quad
 \{1,\ldots,8,10\},\quad
 \{1,2,4,5,6,7,8,10,11\},                            \tag{3.4}
\]

which are distinct rank-nine sets, while both four-letter windows have rank
ten.  This is a literal fragment of the proposed block geometry and directly
refutes any local triple-window plateau inference.

## 4. Reconciliation of the R and A reports

The R theorem is mathematically correct and explicitly scoped to a
saturated pair/**four-window** prefix.  Its `3699` bound should be retained
for that architecture but must not be cited against (1.3).

The current A audit gives the same corrected reduction as Theorem 2.1.  It
certifies `2328` distinct internal block colours and leaves the global
rainbow path open.  It does not contain a mixed-triple UNSAT certificate.
Any earlier A verdict obtained by imposing a uniform `D^3` row has the same
obsolete scope as the R theorem.  Moreover, UNSAT for one fixed block
inventory would not rule out all valid coloured inventories without an
additional inventory-independence proof.

Therefore the proof-safe verdict is

```text
CURRENT MIXED-WIDTH ALTERNATING PREFIX: OPEN, NOT DISPROVED.
```

## 5. Tail scope remains separate

The corrected prefix verdict does not repair the tail.  The direct/two-edge
ear schedule is impossible because `674` missing rank-six colours have no
original endpoint superset.  The first proposed short-ear repair has only
`336` internal--internal edge slots against those `674` demands.  Exact
local enumeration finds `266` demands with a clean three-edge ear, another
`128` with a clean four-edge ear, and `280` unresolved at that radius.

Thus tail completion still requires longer/shared ears or a consistent
cut-and-reroute construction with all physical palettes replayed.

## 6. Exact long-rank interface after the mixed-width correction

For a literal candidate word define the selected rank-nine row

\[
 R_i=\begin{cases}
 Q_i\cup Q_{i+1}\cup Q_{i+2},&0\le i\le7400,\\
 Q_i\cup Q_{i+1}\cup Q_{i+2}\cup Q_{i+3},&7401\le i\le24309.
 \end{cases}                                         \tag{6.1}
\]

Assume this is a bijection onto the rank-nine layer.  Consecutive intervals
of \(R\) represent every physical interval of rank at least ten except the
single boundary-gap family

\[
                G_a=\bigcup_{j=a}^{7403}Q_j,qquad0\le a\le7400. \tag{6.2}
\]

Indeed, an interval ending at most at `7402` is recovered from prefix
triples; one ending at least at `7404` is recovered from a consecutive
mixed-row interval.  Intervals ending exactly at `7403` are (6.2).  All
remaining shorter intervals have rank at most nine by the lower schedule.

Hence upper coverage is exactly

\[
 \operatorname{IntOR}(R)\ \cup\ \{G_a:0\le a\le7400\}.            \tag{6.3}
\]

For rank ten this specializes to adjacent unions of rank-nine rows together
with the rank-ten members of (6.2).  Neither the prefix path nor the GK base
forest makes (6.3) automatic.

## 7. Corrected literal verifier

The fail-closed verifier

```text
scratch/audit_k17_two_zone_prefix_long_rank_scope_20260731.py
```

now checks:

1. the literal alternating block decomposition and all low letters;
2. the complete rank-seven and rank-eight selected-cell partitions;
3. the mixed `7399+2+16909` rank-nine row; and
4. exact ranks `10,...,17` coverage by direct interval replay, cross-checked
   against (6.3).

The machine-readable audit is

```text
scratch/k17_two_zone_prefix_long_rank_scope_20260731.audit.json
```

No candidate word is present, so the verifier certifies scope only.  No
`k=17` upper bound follows.

## 8. Exact scope

Proved:

* the original and first short-ear tail schedules fail;
* the corrected prefix trace is exactly Theorem 2.1;
* the four-window plateau does not apply to it; and
* long-rank coverage is exactly (6.3).

Open:

* a global, physically factorable path (2.1) with its two seam colours;
* a tail completion matching the residual palettes;
* the all-width upper tower; and
* a literal length-`24313` word.
