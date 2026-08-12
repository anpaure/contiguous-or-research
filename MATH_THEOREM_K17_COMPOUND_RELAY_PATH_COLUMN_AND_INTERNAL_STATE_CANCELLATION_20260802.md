# K17 compound relay-path columns and internal-state cancellation

**Date:** 2026-08-02  
**Status:** exact lower-table theorem and independently replayed round-21 to
round-23 witness.  The theorem repairs the row-disjoint atomic-column model
at the one authenticated serial overlap.  It does not turn the fixed
round-47 table into a feasible common-state `1S` configuration, and it makes
no residence, upper, topology, source, common-cap, compiler, or word claim.

## 1. What the obstruction actually says

The authenticated round-47 lower table has a perfect relaxed union-supplier
projection, but its exact relaxed-nine downward/neutral common-state census
has only `2188` five-cell socket hyperarcs and has `5969` short roles of socket
degree zero.  Hence that **fixed table** is solver-free infeasible for the
declared `1S` common-state subface.  This census alone is neither an
unrestricted-socket chronology no-go nor a no-go for a variable relay master.

There is also a separate representation obstruction.  In the accepted
lineage, physical row `520` is first the `A` row of the relay

\[
                         520\longrightarrow2117
\]

and is then the `D` row of

\[
                          29\longrightarrow520.
\]

The two uses are serial, not simultaneous.  They violate a model that
charges an entire physical row to at most one atomic relay, but they do not
violate literal table semantics.  The correct object is one compound path
column.

## 2. Donor-assignment graph

In an unrecoupled table, write every eligible hard donor row as

\[
                  v=(B_v,M_v,R_v)
\]

and every free singleton row as `f=(R_f)`.  Form a directed assignment graph
with

\[
 \begin{aligned}
   u\longrightarrow v &\quad\text{when}\quad B_u\subsetneq M_v,\\
   u\longrightarrow f &\quad\text{when}\quad B_u\subsetneq R_f.
 \end{aligned}                                                    \tag{2.1}
\]

A selected assignment sends each donor bottom `B_u` to exactly one host,
uses each donor host at most once, and uses each free host exactly once.  A
self-loop `u->u` is the unchanged assignment.  The resulting table is

\[
 \begin{array}{rcll}
  v&\mapsto&(M_v,R_v),&\deg^-(v)=0,\\
  v&\mapsto&(B_u,M_v,R_v),&u\to v,\\
  f&\mapsto&(B_u,R_f),&u\to f.
 \end{array}                                                     \tag{2.2}
\]

### Theorem 2.1 (exact assignment normal form)

Every assignment satisfying these degree conditions and (2.1) produces an
exact target partition with unchanged owners and roots.  Conversely, every
table obtained solely by transporting the original donor bottoms among
donor and free hosts has a unique assignment of this form.

After deleting stationary self-loops, the selected donor graph is a disjoint
union of directed paths ending at free rows and nontrivial directed donor
cycles.  A path

\[
               v_0\to v_1\to\cdots\to v_\ell\to f              \tag{2.3}
\]

is one compound column.  It maps

\[
 \begin{array}{rcl}
 v_0&\mapsto&(M_{v_0},R_{v_0}),\\
 v_i&\mapsto&(B_{v_{i-1}},M_{v_i},R_{v_i})\quad(1\le i\le\ell),\\
 f&\mapsto&(B_{v_\ell},R_f).
 \end{array}                                                     \tag{2.4}
\]

Its target-multiset boundary is exactly zero.  Its length current is always

\[
                    (\Delta x_1,\Delta x_2,\Delta x_3)=(-1,+2,-1), \tag{2.5}
\]

independent of the length of the path.

#### Proof

Every original bottom `B_u` occurs once on the left of (2.2) and, by the
outdegree equation, once on the right.  Host capacities make these
occurrences distinct.  Every middle and root stays on its original row.
Thus the target multiset is unchanged.  The strict containments (2.1) make
every displayed chain strict; owners and roots are untouched.  Reading the
host of each uniquely named bottom proves the converse.  A finite digraph
with donor outdegree one, donor indegree at most one, and free indegree one
has precisely the asserted path/cycle decomposition after stationary
self-loops are deleted.  On (2.3), only
`v_0` changes long to short and only `f` changes singleton to short, proving
(2.5).  QED.

This is an integral bipartite-assignment formulation.  It is strictly more
faithful than selecting pairwise row-disjoint `O/R` columns: a donor may have
one incoming and one outgoing assignment arc and hence be an internal path
vertex, while distinct **compound path columns** remain vertex-disjoint.

## 3. Why serial row reuse is legal

The path (2.3) has the following canonical realization.  First apply the
ordinary terminal move `O(f,v_ell)`.  Then, in decreasing index order, apply

\[
                R(v_i,v_{i+1}),\qquad i=\ell-1,\ldots,0.        \tag{3.1}
\]

After the terminal move `v_ell` is short.  Inductively, immediately before
`R(v_i,v_{i+1})`, row `v_i` is still long and row `v_{i+1}` is short.  The
relay shortens `v_i` and regrows `v_{i+1}` with bottom `B_{v_i}`.  Therefore
every primitive is applied to the row types it requires, every prefix has
the same target multiset, and all chains remain strict.

Let `L_v,S_v` denote only the long/short **mode** of donor `v`, and let
`N_f,T_f` denote the singleton/short mode of the free row.  The mode
boundaries are

\[
 \begin{aligned}
 \partial O(f,v_\ell)
   &=(T_f-N_f)+(S_{v_\ell}-L_{v_\ell}),\\
 \partial R(v_i,v_{i+1})
   &=(S_{v_i}-L_{v_i})+(L_{v_{i+1}}-S_{v_{i+1}}).
 \end{aligned}                                                   \tag{3.2}
\]

Summing gives

\[
 \partial P=(T_f-N_f)+(S_{v_0}-L_{v_0}).                       \tag{3.3}
\]

Thus every internal row has coefficient zero: its short output state is
exactly the short input state of the next relay.  After subtracting the
universal one-free/one-source column signature on the right of (3.3), the
reduced state boundary is zero.  The unprojected target boundary is already
zero by Theorem 2.1.

There is an important literal qualification.  An internal donor generally
changes from `L_v(B_v)` to `L_v(B_u)`.  Its boundary is not zero if the
bottom label is retained as part of the row state.  What cancels exactly is
the glued short interface and the long/short mode; the transported bottom is
retained in (2.4), while the global bottom-target current sums to zero.  Any
additive palette, cap, aperture, or voltage ticket must likewise be carried
on the primitive interfaces and have its declared boundary; nonlinear
history and topology states must pass at every prefix and equal the declared
regenerated endpoint interface.  The lower artifacts audited here do not
contain those additional labels.

More explicitly, write `L_v(b)=(b,M_v,R_v)` and
`T_f(b)=(b,R_f)`.  In the complete row-labelled chain basis the exact
boundary is

\[
 \begin{split}
 \partial_{\rm row}P={}&T_f(B_{v_\ell})-N_f
     +S_{v_0}-L_{v_0}(B_{v_0})\\
 &+\sum_{i=1}^{\ell}
   \left(L_{v_i}(B_{v_{i-1}})-L_{v_i}(B_{v_i})\right),
 \end{split}                                                    \tag{3.4}
\]

which is generally nonzero even though its named-target-multiset projection
is zero.  This is the exact distinction between interface cancellation and
full table-state closure.

## 4. The exact round-21 to round-23 compound column

The unique length-two internal path in the reconstructed round-47 assignment
is

\[
                  29\longrightarrow520\longrightarrow2117
                     \longrightarrow F_{15856},                 \tag{4.1}
\]

carrying bottoms

\[
                        158,\quad4174,\quad330.                  \tag{4.2}
\]

The original rows are

```text
29       (158,446,958)
520      (4174,4318,4574)
2117     (330,12622,12638)
F15856   (79178)
```

and (2.4) gives

```text
29       (446,958)
520      (158,4318,4574)
2117     (4174,12622,12638)
F15856   (330,79178).
```

By round 21 the terminal assignment `2117->F15856` had already been made.
The remaining suffix is exactly

```text
round21 -> round22:  A520 -> D2117
round22 -> round23:  A29  -> D520
```

with literal states

```text
row     round21                 round22                 round23
29      158,446,958             158,446,958             446,958
520     4174,4318,4574          4318,4574               158,4318,4574
2117    12622,12638             4174,12622,12638        4174,12622,12638
```

Hence row `520` follows

\[
               L_{520}(4174)\to S_{520}\to L_{520}(158).        \tag{4.3}
\]

The intermediate `S_520` interface cancels exactly.  The two long states do
not coincide, and the audit records this rather than calling (4.3) a zero
boundary in the fully bottom-labelled state.

The independent auditor verifies all `24,310` rows at all three prefixes,
the exact `65,535`-target partition, the histogram `(0,7395,16915)`, the
changed-row supports `{520,2117}` and `{29,520}`, and the direct compound
endpoint.  The table produced by applying the suffix once to round 21 is
byte-identical to the authenticated round-23 table:

```text
SHA-256 3bd462908bd8df71684a53c42d6e6698ab9ba638245e72f28b21ea1a588da900
```

The already frozen complete `6/9/4` lower projections at the same prefixes
are

| state | edges | matching | deficiency | zero heads |
|---|---:|---:|---:|---:|
| round 21 | 72,045 | 16,871 | 27 | 16 |
| round 22 | 72,054 | 16,872 | 26 | 15 |
| round 23 | 72,057 | 16,874 | 24 | 13 |

Thus both serial prefixes strictly improve that lower projection, and the
direct macro endpoint has exactly the projection of the successful
round-23 transaction because it is the same table.  These are projection
claims, not common-state `1S` claims.

The independent global assignment reconstruction strengthens the scope of
this example.  Round 47 decomposes into `1748` donor paths and no donor
cycles.  It has `48` nontrivial internal arcs: `1701` paths have none, `46`
have one, and exactly one has two.  The last is (4.1).  Therefore a
path-column master represents the whole authenticated lower endpoint without
the false atomic collision at row `520`.

## 5. Relation to a strict commuting fan

A compound path column is an indivisible fan arm.  A family of such arms
commutes at the lower-table level when their external donor/free vertex sets
are disjoint: applying any subset merely transports disjoint sets of named
bottoms, so every subset endpoint is order independent.  Internal overlap
inside one arm is legal by Section 3 and must not be charged twice.

For the full guarded factor/product-state graph, this lower commutation is
only the first gate.  A proof-safe **strict path-column fan** at state `x`
must additionally satisfy:

1. each arm has a fixed serial ordering, and from every completed-arm subset
   context in which it may be scheduled, every microscopic transition is
   actual-tail applicable and has its head in the literal hard face;
2. its additive palette/cap/aperture/voltage tickets have the declared zero
   boundary, while its nonlinear opened-history and topology states pass at
   every prefix and equal the declared regenerated endpoint interface;
3. arms have disjoint nonlinear guard/short-run halos, or every overlap
   interaction is explicitly replayed; and
4. each subset endpoint returns to the declared regeneration domain.

Under these four conditions the ordinary commuting/subset-fan proof applies
with path columns in place of primitive circuits.  In particular, if every
nonterminal state in an endpoint-closed domain has such a fan containing an
arm or finite selected subset with integer Lyapunov change at most `-1`, and
that Lyapunov function is bounded below on the endpoint-closed domain,
repeated descent terminates.  This is the state-relative expansion hypothesis
actually sufficient for renewal.

Neither positive defect, perfect union matching, connectedness, nor the
counts `2188/5969` imply this expansion.  The fixed round-47 downward/neutral
census proves exactly why: a scalar-perfect lower endpoint can still have
`5969` empty literal socket rows in the declared face.  A global theorem now needs either a
state-lifted path-column catalogue satisfying the four conditions, or a
closed accepting-shore/Farkas certificate in that lifted graph.  The present
artifact proves the missing column algebra and one exact lower witness; it
does not assert either global alternative.

The path extension therefore bypasses only the **scope** of the static
`2188/5969` obstruction: an outer path choice changes which rows are long or
short and which bottom labels they carry, so the complete common-socket bank
must be regenerated and the fixed-table empty rows are not a valid global
no-good.  It does not bypass the obstruction at the unchanged round-47 table,
which remains exactly infeasible in the audited downward/neutral face, and it
does not prove that any other path selection has a full `1S` lift.

## 6. Frozen audit

New audit bundle:

```text
scratch/k17_round47_compound_relay_path_column_20260802/
  audit_k17_round47_compound_relay_path_column_20260802.cpp
  direct_round21_to_round23.table.tsv
  round21_23.rows.tsv
  round21_23.audit.json
  INPUT_SHA256SUMS
  MANIFEST.sha256
```

The new source compiles cleanly with
`clang++ -std=c++20 -O2 -Wall -Wextra -pedantic`.  It performs no search.
The manifest binds the original table, all three prefix tables, both relay
choice audits, all three complete lower-projection audits, the independent
round-47 donor-flow reconstruction, and the exact relaxed-nine no-go
manifest.
