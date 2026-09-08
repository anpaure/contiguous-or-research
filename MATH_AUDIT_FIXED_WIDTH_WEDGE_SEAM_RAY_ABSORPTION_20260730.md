# Independent audit of fixed-width wedge-seam ray absorption

**Date:** 2026-07-30  
**Status:** local theorem and Corollary 3.2 are sound in their stated
fixed-width upper-shadow scope; exact factor replay completed

## 1. Verdict

`MATH_THEOREM_ROOT_FIXED_WIDTH_WEDGE_SEAM_RAY_ABSORPTION_20260730.md`
is correct.  No cyclic-index or geodesic counterexample was found, and the
local proof can be made completely explicit as follows.

Let the selected witness have `q` edges.  If it contains the right wedge
flank and is geodesic, then it cannot contain the left flank: the two wedge
transitions add only one new coordinate to the interval union.  Such a
witness also has `q<N`; otherwise it traverses every cycle edge and hence
both flanks.  A cyclic interval containing the right flank, avoiding its
immediate predecessor, and having fewer than `N` edges must start at the
wedge centre.  The socket identity

```text
B union S = E union S
```

then replaces its first vertex without changing its union.  This handles
wrapped indices as well as ordinary indices.

The first distinguished cut in Corollary 3.2 need not itself be a wedge
flank.  Its selected witnesses merely have to avoid that cut.  Only the
later, socketed components require wedge-flank cuts.  This is a harmless
strengthening of the corollary's inherited setup, and it matters for the
retained `k=15` factor because its small component is wedge-free.

## 2. Exhaustive small-cycle check

The independent script

```text
scratch/audit_root_fixed_width_wedge_seam_literal_20260730.py
```

enumerates every simple cycle of `J(4,2)` and both directions.  It checks
every fixed-width geodesic witness crossing a right wedge flank and every
legal facet socket.  The exact census is

```text
undirected simple cycles                         63
directed simple cycles                          126
geodesic right-flank crossings                  360
facet-socket union identities                   720
crossings also containing the left flank          0
crossings not starting at the wedge centre        0
```

Thus the smallest complete cyclic test contains no counterexample.

## 3. Exact assignment quantifier

For a component `C`, target `Y`, and fixed width `q=|Y|-r`, let

```text
K_C(Y) = intersection of the edge spans of all fixed-width Y-witnesses on C.
```

For two components, put the distinguished component first and the socketed
component second.  The maximum-flexibility safe-cut set is

```text
Safe(C1 | C2)
  = {c : c notin K_C1(Y) for every Y having no fixed-width witness on C2}.
```

Targets present on `C2` are assigned to `C2`; only targets absent from `C2`
must be assigned to an avoiding witness on `C1`.  Therefore the clean
necessary-and-sufficient condition for **the Corollary 3.2 construction** is

```text
there exist c in Safe(C1 | C2) and a directed wedge option w on C2
such that E(c) union S(w) = U(w),
```

or the same condition with the component order reversed.  This is not a
necessary condition for every conceivable splice; a seam can sometimes
replace a witness lost at the first cut as well.

For more than two components, the exact interface is a component-coloured
directed path problem.  Cut options are vertices, an arc `x -> y` exists
when `E(x) union S(y)=U(y)`, one option must be selected from each component,
and the first option must be safe relative to all later provider components.
An ordinary bipartite matching is insufficient because a middle option
couples its incoming wedge socket to its outgoing endpoint.

## 4. Literal replay on the known factors

The script reconstructs the middle factors directly from the authenticated
optimal words and tests every oriented socket arc by concatenating the two
opened paths and enumerating every exact-width upper target.

### `k=13`, component lengths `1547+169`

The components have `104` and `13` wedges.

* Big first, small socketed: `208` socket arcs; `130` are assignment-safe,
  and all `130` literally retain every upper target.  The other `78` miss
  exactly one target.
* Small first, big socketed: `156` socket arcs; `52` are assignment-safe,
  and all `52` literally retain every upper target.  Of the remaining arcs,
  `78` miss one target and `26` miss two.

Thus Corollary 3.2 is not merely formal at `k=13`: it gives `182` oriented
literal all-upper splices across the two component orders.

### `k=15`, component lengths `6390+45`

The components have `330` and `0` wedges.

* Big first, small socketed: no socket is possible because the small cycle
  has no wedge.
* Small first, big socketed: `120` facet sockets exist, but all `45` physical
  small-cycle cuts lie in the unique-provider forbidden set, so none meets
  the assignment-safe hypothesis.  Literal replay finds no all-upper splice:
  `90` socket splices miss exactly one depth-3/rank-11 target, and the other
  `30` miss one depth-1 target plus one depth-3 target.

The best `k=15` socket examples are therefore genuinely close but do not
restore the whole upper tower.  This is a factor-specific negative, not a
counterexample to the theorem.

## 5. Scope

The audit proves only the fixed-width upper-shadow statement.  It does not
establish residence, lower-colour eligibility, lower COMP matching, or a
universal word after splicing.  It also does not claim that every upper mask
must be represented by a fixed-width carrier interval in an arbitrary
construction.

The machine-readable replay is

```text
scratch/root_fixed_width_wedge_seam_literal_20260730.audit.json
```

with status

```text
PASS_LOCAL_THEOREM_AND_SCOPED_FACTOR_REPLAY
```
