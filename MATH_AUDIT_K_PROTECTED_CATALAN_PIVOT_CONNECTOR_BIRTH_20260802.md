# Audit: protected Catalan--pivot connector birth and factor-first scope

**Date:** 2026-08-02  
**Audited theorem:**
`MATH_THEOREM_K_PROTECTED_CATALAN_PIVOT_CONNECTOR_BIRTH_AND_PREPARED_SCAFFOLD_GATE_20260802.md`  
**Verdict:** PASS after three load-bearing corrections: the omitted lower
root is contained in a designated owner endpoint, the final opening is
rank-typed by its literal lower root, and all-width changes are computed on
the actual sequential chronologies.  The theorem still requires its
explicit prepared-source and occurrence-lifted switch hypotheses.  The
unrooted closed-shore theorem is not a fixed-`M_0` connector theorem.

## 1. Parameter and protected-phase audit

The sharp collar uses `m+3d` coordinates inside `[2m-1]`.  Its embedding
condition is exactly

\[
                         m+3d\le2m-1
                    \quad\Longleftrightarrow\quad m\ge3d+1.     \tag{1.1}
\]

The predecessor incidence bank then has `3d<=m-1` edges, so the cited
small-matching extension theorem applies.  Consecutive protected successor
incidences contract as

\[
 I_i\longrightarrow I_{i+1},                           \tag{1.2}
\]

and the last head is new by perfect-matching injectivity.  Their upper
labels are exactly `V_i union V_(i+1)`, which the sharp collar proves
distinct.  Thus Proposition 1.1 has no hidden head, graphic, or upper-label
assumption.

## 2. Born-connector count and topology

A matching `Q` of size `W-1` has rooted indegree and outdegree at most one.
If its links are graphic-independent, they are a tree on `W` vertices and
hence a directed path.  Choosing one of its occurrences for each of the
`U` upper colours gives a subforest `Q_0` with

\[
                         W-U=C                           \tag{2.1}
\]

components.  The complement has exactly

\[
                         W-1-U=C-1                      \tag{2.2}
\]

edges and appears in the order of the ambient rooted path, so it is the
free-port component Hamilton path.  This proves both directions of
Theorem 2.1.

For a Hamilton cycle, total upper multiplicity excess is `W-U=C`.
Occurrences belonging to repeated colours number `C+s>=C+1`, where `s` is
the number of repeated colours.  Since `C>=m` for `m>=3` and
`m>=3d+1`, more than `3d` redundant occurrences exist.  Therefore one can
open outside the protected successor bank while retaining every immediate
upper colour.  This audit confirms only the owner-layer opening; a cyclic
source cut still needs an all-width occurrence row.

## 3. Closed-shore scope

Theorem 2.3 is correctly stated on the **unrooted** prospective Johnson
forest `F_0` only with its endpoint-containment guard.  A residual lower
root in `A` is free to choose two distinct containing owners.  The network

```text
source --2--> root --1--> owner --c_T--> sink
```

therefore applies, and rootwise minimization gives precisely

\[
 2I_A(Y)+J_A(Y)\le\sum_{T\in Y}c_T.                    \tag{3.1}
\]

The total degree identity is correct:

\[
 \sum_Tc_T=(2W-2)-2U=2(C-1)=2|A|.                    \tag{3.2}
\]

For a forest, degree summation gives

\[
 \sum_{T\in Y}c_T
 =2\kappa(F_0[Y])-|\partial_{F_0}Y|
  -\mathbf1_{s\in Y}-\mathbf1_{t\in Y}.              \tag{3.3}
\]

The flow supplies only owner degrees.  Contracted graphic rank `C-1` is
still necessary and sufficient for the chosen `C-1` residual edges to join
the `C` old components as a tree.

There is one further load-bearing endpoint row.  The owner path uses only
`W-1` distinct lower intersections and omits one rank-`m-1` root `o`.  Its
incidence lift visits all `2W` Middle Levels vertices if and only if `o` can
be appended at an owner endpoint, namely

\[
                         o\subset s\quad\hbox{or}\quad o\subset t.       \tag{3.4}
\]

The corrected theorem states (3.4).  Without it the unrooted owner path is
valid but its incidence lift misses `o`, so no perfect alternating matching
phase follows.

Before the graphic row is imposed, every feasible degree completion is one
`s`--`t` path plus cycles.  This follows because `s,t` are the only
degree-one owners.  A protected incidence-tree family of degree-preserving
maximum mergers can absorb those cycles while leaving (3.4) intact; the
closed-shore flow alone supplies no such merger.

The scope warning is load-bearing.  Relative to a previously fixed
`M_0`, one endpoint of the residual edge on root `L` is already
`M_0(L)`; the two-endpoint flow is then too relaxed.  The theorem avoids
this error by choosing the unrooted owner path first and deriving `M_0`
from its alternating incidence lift afterward.

## 4. Physical inheritance

The monotone insertion condition

\[
                         X\subseteq A_{-1}\cup A_1      \tag{4.1}
\]

preserves an old crossing occurrence because its new convex hull gains only
`X`, already contained in the old OR.  Noncrossing intervals are literal
copies.  Hence all-width inheritance is occurrencewise, although a crossing
occurrence changes width by one.

For residence, every changed maximal run is either an internal fragment run
or a concatenation of clipped suffix/prefix runs.  Endpoint bits, clipped
run lengths, the all-one flag, and the internal-good bit are therefore an
exact finite composition state.  The theorem correctly treats signed/dual
residence as a separate application to complemented traces.

The temporal compiler ledger also checks: exactly the `d-1` old crossing
cells at maximal strict-lower width leave the band; their values are the
internal rank-`m` owners.  Thus a strict-lower matching uses none of them.
The transport complement is exactly the singleton and two nested rays.
Zero matched damage still requires the declared common-cap hypothesis.

## 5. Factor-first audit

`Q_0` plus a perfect free-port matching `R` is a perfect short-shore
matching; with `M_0` it forms an upper-surjective two-factor.  Since all
designated upper representatives lie in `Q_0`, connector-only switches and
an `R_fin` opening preserve the immediate-upper bank.

For a switch family, the component--packet incidence graph has

\[
 |\mathcal C(F)|+|\mathcal T|\text{ vertices},\qquad
 \sum_z|e_z|\text{ edges}.                             \tag{5.1}
\]

Equations (6.2)--(6.3) in the theorem are exactly its spanning-tree and
subforest inequalities.  A rooted order makes every packet meet one merged
component and introduce `|e_z|-1` new components; maximum-merger semantics
therefore leaves one cycle.  For ternary packets this specializes to a
loose hypertree and exposes the parity obstruction.

The physical hypotheses cannot be dropped.  A factor records adjacent
owners but not the common length-`d+1` source windows producing them.  A
new seam can close a clipped short run, and a long upper target can have its
only occurrence across that seam.  Thus a source antecedent, depth-`d`
boundary history, residence state, all-width occurrence ledger, and a safe
final linearization are genuine additional rows.  Residual Ore/LKK supplies
none of them.

The corrected sequential ledger is exact.  With literal intermediate
chronologies `A_i`, the increments

\[
 \Delta_i(S)=\mu_{A_i}(S)-\mu_{A_{i-1}}(S)             \tag{5.2}
\]

telescope, whereas deltas independently scored against the initial factor
need not.  Final coverage is the pointwise inequality

\[
 \mu_{A_0}(S)+\sum_i\Delta_i(S)
       +\Delta_{\rm open}(S)\ge1,                     \tag{5.3}
\]

where `Delta_open=mu_(Open_e(A_q))-mu_(A_q)`.  For a pure cut this is
`-L_e`; the signed form also covers a typed linearization creating declared
boundary occurrences.

If an intermediate certificate consumes a named occurrence, hereditary
applicability must preserve that occurrence; (5.3) alone certifies only the
final output.

Finally, the opening edge must be typed.  For
`e=oV in R_fin`, one has `|o|=m-1`, `|V|=m` and `o subset V`; the retained
matching edge is `oS` with `S=M_0(o)`, so `o subset S cap V`.  Hence `o` is
the literal lower-shore endpoint.  The accepted source linearization must
also expose its controlled boundary nonowner cell with value exactly `o`;
the graph cut alone does not manufacture that source cell.  It may be paid
by the pivot bank only if one reserved cell has value **equal** to `o`;
rank agreement or an abstract ray label is insufficient.

## 6. Audited frontier

The proved composition leaves one exact direct-path lemma:

* construct `PCPS(m,d)`, the prepared temporal Hamilton scaffold of the
  theorem;

or one exact factor-first lemma:

* construct an upper-exact `Q_0`, a free-port factor `R`, and a compatible
  source-lifted spanning switch basis with a safe `R_fin` opening.

Neither statement follows from the fractional pull clock, marginal
Ore/LKK expansion, or a scalar component bound.  Upper widths, residence,
and the terminal common cap remain literal acceptance rows; no
`B+1`, `O(1)`, or equality conclusion is inferred.
