# K17 LLR470 global-selector preflight and exact Benders oracle

**Date:** 2026-08-02  
**Status:** proof-safe reduction and fail-closed launch audit.  No SAT,
selected-state, chronology, residence, upper-shadow, compiler, carrier, or
word claim is made.

## 1. Corrected finite input and scope

The current corrected LLR-transfer interface reports:

* `4,803` protected common-positive transfer edges;
* common-only matching rank `470`;
* protected structural matching rank `1,012/1,018`; and
* a materialized full-private `470` table which is being repriced.

These figures supersede the earlier `4,856/496` private screen.  The earlier
screen protected a weaker row-level projection and must not be used as an
input certificate for the global selector.

The intended protected bank has `1,748` short rows, `3,496` endpoint-host
occurrences, and `3,495` movable token occurrences.  A transfer is admissible
only after its complete changed-row/occurrence footprint is checked against
this bank.  The residual completion must retain the selected protected
placements, not merely the set of abstract short rows.

The corrected edge list, selected `470` matching, and materialized table
subsequently landed and were independently replayed at their advertised
**warm47-derived structural** scope.  A further parent-binding audit found a
load-bearing mismatch: the protected bank was materialized on table

```text
b268d1248e53d164d87bc83cf69fbd5ebd412451ac9e4a4313408167f1e637dc
```

whereas the LLR graph/table was generated from warm47.  The candidate differs
from the bank parent on `16,034` rows.  Of the bank's `7,213` distinct
protected occurrence rows, `6,479` have different literal row states; with
occurrence multiplicity, `7,437` of the `8,739` listed short/host/token
occurrences disagree, split as `1,564/2,946/2,927` across short rows,
endpoint hosts, and token occurrences.  Avoiding those row IDs while changing other rows is
therefore not a replay of the bank's tickets.  The current candidate is
rejected as a **combined** protected-bank input unless a regenerated ticket
and outer-matching certificate on that candidate is supplied.

The complete regenerated occurrence catalogues for the remaining
`3,899+1,748=5,647` roles are also absent.  Consequently a full exact launch
would have been semantically incomplete and was not made.

## 2. Exact LLR transfer master

Let `E` be the corrected occurrence-safe transfer catalogue.  A transfer
`e=(a,b)` uses one old direct `L-R` row `a` and one old `L-M-R` row `b`, and
performs

\[
 (L_b,M_b,R_b)+(U_a,Q_a)
 \longmapsto
 (M_b,R_b)+(L_b,U_a,Q_a).                    \tag{2.1}
\]

Use a bit `x_e` for every `e in E`.  The row-disjoint transfer face is exactly

\[
 \sum_{e\ni a}x_e\le1,\qquad
 \sum_{e\ni b}x_e\le1.                       \tag{2.2}
\]

For each physical row `i`, introduce one-hot row-state variables
`z_(i,0)` and `z_(i,e)` for its incumbent state and incident selected
transfer states.  Equations (2.2) give

\[
 z_{i,e}=x_e,\qquad
 z_{i,0}=1-\sum_{e\ni i}x_e.                  \tag{2.3}
\]

Thus a selected transfer matching materializes one unambiguous literal
table.  Target/root/owner/histogram replay is a mandatory child audit.  The
master may fix a cardinality, maximize common-positive transfers, or optimize
another declared objective, but no marginal score is a substitute for the
child audits below.

## 3. Complete occurrence-DNF child

For every one of the `5,647` residual fixed/free short roles `w`, let
`Gamma_w` be the **complete regenerated** catalogue of occurrence tickets.
A ticket `g` records:

1. all physical row states in its footprint;
2. its predecessor and successor hosts and their flags;
3. every required protected/unforced outer-placement literal;
4. its short address/history state; and
5. the identity of its selected parent primitive for supplier use.

Its exact activation is

\[
 \lambda_g\quad\Longleftrightarrow\quad
 \bigwedge_{(i,s)\in Z(g)}z_{i,s}
 \wedge\bigwedge_{p\in P(g)}p.                \tag{3.1}
\]

The role row is

\[
 \sum_{g\in\Gamma_w}y_g=1,\qquad y_g\le\lambda_g. \tag{3.2}
\]

If `Gamma_w` is empty under an incumbent, the proof-safe activation cut is

\[
             \sum_{g\in\Gamma_w}\lambda_g\ge1.       \tag{3.3}
\]

This is a DNF cut on actual row states and placement literals.  A cut only on
the selected short-row set, or on a marginal positive/zero screen, is not
valid for this child.

After the `1,748+5,647=7,395` tickets are selected, exactly `9,520` long--long
transitions remain.  Delete their consumed predecessor/successor ports and
run a bipartite perfect-matching oracle on the residual flag states.  A
failed child returns its ordinary Hall shore `X`:

\[
 \sum_{h\in X}o_h\le
 \sum_k \operatorname{OR}_{c:h\in X,\,c:h\to k}
       (\lambda_c\wedge o_h\wedge i_k).        \tag{3.4}
\]

The available-port variables in (3.4) are load-bearing; omitting them counts
already-consumed ports.

## 4. Exact supplier-rank Benders cut

For a fixed materialized table, the complete row-pair projection has an
ordinary maximum matching and an alternating Hall shore.  This is a useful
necessary preflight, but the global selector requires the stricter
selected-parent graph.

For every occurrence-labelled supplier record `r`, let `parent(r)` be the
ticket or direct long transition which owns the supplier source occurrence.
Set

\[
 \kappa_r\Longleftrightarrow
       \lambda_r\wedge\pi_{parent(r)},          \tag{4.1}
\]

where `pi` is the selected ticket/direct-transition bit.  For supplier
identity `u` and hard head `v`, define

\[
 a_{uv}\Longleftrightarrow
   \operatorname{OR}_{r:\,sup(r)=u,\,head(r)=v}\kappa_r. \tag{4.2}
\]

If exact matching on `(a_uv)` returns a deficient head shore `Q`, the global
Benders row is

\[
 \boxed{
 |Q\setminus S_H|\le
 \sum_u \operatorname{OR}_{v\in Q}a_{uv}} .   \tag{4.3}
\]

This is the sharp proof-safe way to optimize the LLR transfer choice against
supplier rank.  In particular, the contribution of a transfer is not
additive: `a_uv` depends on the final states of both the supplier row and the
head row, on their flags/placements, and on the selected parent primitive.
Two transfers on different rows can therefore activate or destroy one
supplier edge jointly.  Any transfer-weight objective based on independent
supplier deltas is only a heuristic seed.

At the weaker complete-row-pair projection, the same statement holds with
`kappa_r` replaced by the exact compatibility of the source-row and head-row
states.  Since each row is one-hot by (2.3), this compatibility has the exact
finite expansion

\[
 a^{proj}_{uv}\Longleftrightarrow
 \operatorname{OR}_{(s,t)\in A_{uv}}
       (z_{u,s}\wedge z_{v,t}),                 \tag{4.4}
\]

where `A_uv` is obtained by literal `6/9/4` replay.  Equation (4.4) gives an
exact projection-level Benders cut, but it does not imply (4.3).

## 5. Exact oracle order and certificates

A fail-closed global run must use this serial oracle order:

1. **transfer master:** enforce (2.2), the full protected occurrence
   footprint, and the declared LLR cardinality/objective;
2. **literal table replay:** verify all targets, row roots/owners, chain
   types, and protected placements;
3. **role-DNF child:** enforce (3.1)--(3.3) on all `5,647` regenerated roles;
4. **long-state child:** enforce the `9,520` residual transitions and return
   (3.4) on failure;
5. **selected-parent supplier child:** compute the graph (4.1)--(4.2), return
   (4.3) on failure, and require rank `16,898`; and
6. independently rebuild and replay every accepted table and matching.

Every failure certificate must name the master hash, the complete catalogue
hashes, and either an empty role DNF, a residual-port Hall shore, or a
selected-parent supplier Hall shore.  Resource exhaustion, missing catalogue
rows, SSH failure, or a timeout is `UNKNOWN`, never `UNSAT`.

## 6. Literal parent audit and launch audit

The first H100 resource probe failed before reaching the host, but a later
probe succeeded.  It reported `64` CPUs, load average `1.14/1.69/2.85`,
`205 GiB` available memory, and `22 GiB` free in the work filesystem.  The
unique root was created and received preflight source/input staging:

```text
/home/amodo/or15/work/k_llr470_selector_20260802
```

No remote executable was compiled and no solve/audit job was launched after
the parent mismatch was found.

The local fail-closed preflight independently returns

```text
REJECT_K17_LLR470_BANK_PARENT_MISMATCH
bank/candidate row differences       16034
protected unique rows                 7213
protected unique-row mismatches       6479
protected occurrence mismatches       7437
  short / host / token             1564 / 2946 / 2927
```

The exact launch blockers are semantic:

* the warm47-derived `470` table does not literally inherit the `b268...`
  protected occurrence bank, and no regenerated joint bank is supplied; and
* the complete regenerated `5,647`-role ticket/direct/supplier catalogues did
  not exist.

Accordingly the current combined-bank verdict is

```text
REJECT_K17_LLR470_BANK_PARENT_MISMATCH
```

The unrestricted/global selected-state decision remains `UNKNOWN`.  The
corrected positive `4,803/470/1,012` static transfer result and the complete
row-pair supplier projection of the warm47-derived table remain valid at
their own scopes.  The latter has rank `16,872/16,898`, deficiency `26`,
`23` zero heads, and Hall shore `36 -> 10`; it is not a selected-parent or
protected-bank certificate.  A live continuation must either regenerate all
protected tickets/placements on this candidate, or rebuild the LLR catalogue
on the actual `b268...` parent, before invoking Sections 3--5.
