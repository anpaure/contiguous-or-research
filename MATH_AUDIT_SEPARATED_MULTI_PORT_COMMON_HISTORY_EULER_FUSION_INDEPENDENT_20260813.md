# Independent audit: separated multi-port common-history Euler fusion

**Date:** 2026-08-13  
**Audited source:**
`MATH_THEOREM_SEPARATED_MULTI_PORT_COMMON_HISTORY_EULER_FUSION_20260813.md`  
**Audited source SHA-256:**
`06f0c6713ecd6aa9575b8e01106129bee69987fb23d5485c307bbe1447499049`  
**Method:** hostile symbolic audit; no computation  
**Verdict:** **PASS at the stated hypotheses.**

The source now cleanly separates two logically different assertions:

1. separated length-`d` antecedent modifications can be realized
   simultaneously on each resident Johnson component; and
2. once the resulting occurrence-labelled order-`d` de Bruijn circuits
   exist and their union is connected, Euler fusion is automatic and
   preserves the literal short deck.

The second assertion does not follow merely from connectivity of an
abstract pairwise-compatibility graph.  The simultaneous separated-port
hypothesis is a valid sufficient realization condition for the first
assertion.

## 1. Audit of simultaneous multi-block freedom

For a nonconstant coordinate `x`, unwrap one positive owner run as
`[a,b]`.  Its maximal depth-`d` source carrier is

\[
                         E_x=[a+d,b].
\]

Both endpoints of `E_x` are members of the forced sets `F_j`, so every
allowed replacement retains them.  All positions outside `B` retain the
maximal letter.  Hence every consecutive run of positions at which `x` is
removed is contained in one cyclic component of `B` and has length at
most `d`.  Consecutive retained support positions are therefore at
distance at most `d+1`, which is precisely the bounded-gap antecedent
criterion.  Endpoint retention handles the two ends of a nonconstant
carrier.

For a constant-one coordinate, the same statement is cyclic: the retained
support meets every cyclic interval of `d+1` positions.  The assumptions
`L>=d+1` and that no cyclic component of `B` has more than `d` positions
ensure that the whole carrier cannot be removed.  Finally, `1<=d<r`
gives

\[
                          |P_j|\ge r-d>0,
\]

so the unaltered maximal letters are valid nonempty source letters.  These
are exactly the boundary hypotheses needed by the proof.

Thus Theorem 1.1 is valid.  In particular, pairwise disjoint length-`d`
ports separated, including cyclically across the last/first port, by at
least one unaltered position coexist.  Packing blocks of size `d+1`
around the cycle proves the sufficient capacity

\[
                         \left\lfloor {L\over d+1}\right\rfloor.
\]

All ports on one component must be read in one fixed global traversal
orientation, as the audited source now states.

## 2. Audit of the connected Euler theorem

Treat every source position as a distinct occurrence-labelled edge of the
order-`d` de Bruijn multigraph.  Parallel copies of the same underlying
transition are allowed.  Each component word is a closed directed walk,
so its occurrence-edge multigraph is balanced.  The literal equality of
the two length-`d` port words on every selected component-graph edge makes
the corresponding two walks share an actual de Bruijn vertex.  Since the
component graph is connected, the union is weakly connected on its
nonisolated vertices and balanced.  It consequently has an Euler circuit.

This remains true when:

* a source circuit revisits a history vertex;
* several circuit pairs share different history vertices;
* several circuits share the same history vertex; or
* two labelled occurrence edges induce the same underlying de Bruijn arc.

The required disjointness is at the occurrence level: every old source
position contributes one edge copy and is used exactly once.  Identifying
two genuinely shared edge occurrences, rather than retaining parallel
copies, would change the ledger and is outside the theorem.

Every order-`d` de Bruijn edge carries its complete literal
`(d+1)`-letter context.  Therefore **any** Euler circuit of the realized
connected union has exactly the old occurrence-labelled multiset of
length-`d+1` words.  A word of length `ell<=d` ending at an edge is the
length-`ell` suffix of that same edge context, giving a bijection at every
shorter width.  This proves Theorem 2.1 and the stronger `any Euler tour`
form requested in the audit.

The occurrence label here is the old terminal de Bruijn edge, equivalently
the old owner-window occurrence.  Across a splice, the preceding physical
source-position occurrences can come from another component.  The theorem
preserves their literal letter word and the terminal-edge occurrence tag;
it does not preserve the tuple of constituent source-position identities.

## 3. Explicit spanning-tree splice

The existence proof can alternatively be made as a sequence of legal
successor transpositions.  Start with the successor permutation whose
cycles are the original source circuits.  Choose a spanning tree of the
component-intersection graph.  At a tree edge joining two current cycles
at a shared history vertex `H`, choose one incoming occurrence edge from
each cycle ending at `H` and swap their successors.  Both successors leave
the same vertex `H`, so the result is still a legal de Bruijn successor
permutation.  A successor swap between two distinct permutation cycles
merges them into one.

Process the tree outward from a root.  At each step the child circuit is
still outside the accumulated root cycle, so the swap reduces the number
of cycles by one.  After `|V|-1` swaps there is one Euler circuit.  Shared
vertices and even chosen incoming occurrences may be reused: at the next
step that occurrence lies in the accumulated cycle, and swapping its
current successor with a successor in a new child cycle again merges two
distinct cycles.  Thus neither distinct cut vertices nor a single common
history for all components is necessary.

## 4. Exact scope retained

The theorem transports:

* every owner-window occurrence of width `d+1`;
* every literal source-cell occurrence of width at most `d`; and
* any occurrence-labelled lower assignment whose validity depends only on
  such a preserved cell.

It does not by itself transport intervals longer than `d+1`, proper-upper
witnesses using those intervals, an eventual linear opening, or guards
depending on the new adjacency of two owner occurrences.  Nor does the
finite connectivity observed for MSW pairwise compatibility prove the
separated simultaneous incidence-port assignment.  The final paragraph
of the audited source states these remaining gates accurately.

