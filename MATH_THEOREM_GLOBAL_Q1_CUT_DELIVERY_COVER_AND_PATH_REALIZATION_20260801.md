# Global q1 cut--delivery cover and path realization

Date: 2026-08-01  
Status: exact finite theorem.  It removes the recursive pre-atlas-provider
assumption from the immediate-upper selector.  It does not by itself supply
the ranks `q>=2` upper deck, one Hamilton path, or the lower compiler.

## 1. Setup

Let `F` be a disjoint union of oriented owner paths.  For an internal edge
`e=uv`, write

\[
                         c(e)=u\cup v .                 \tag{1.1}
\]

A construction chooses a set `K` of old edges to cut, a compatible family
of literal replacement packets, and a compatible family of new seams.  A
packet or seam `p` has:

* a Boolean selection variable `x_p`;
* an exact owner/cut/orientation survival condition;
* a literal owner path, hence a finite immediate-upper delivery deck

  \[
                            U(p)=\{a_i\cup a_{i+1}\};   \tag{1.2}
  \]

* two typed exposed ends when it is not already closed inside one packet.

All owner positions are assigned to exactly one surviving old fragment or
one selected packet.  Packet boundary cuts are forced and packet interiors
are not cut.  Thus every uncut old edge remains an adjacency in exactly one
literal fragment.

For a rank-`r+1` colour `y`, let

\[
 E_y=\{e\in E(F):c(e)=y\},\qquad
 P_y=\{p:y\in U(p)\}.                                  \tag{1.3}
\]

## 2. Exact colour clauses

### Theorem 2.1 (global q1 cut--delivery cover)

Under the setup above, the final literal path forest contains every required
immediate-upper colour if and only if, for every such colour `y`,

\[
 \boxed{
   \bigvee_{e\in E_y}\neg z_e
   \quad\vee\quad
   \bigvee_{p\in P_y}x_p
 }
                                                               \tag{2.1}
\]

holds.  Here `z_e=1` means that old edge `e` is cut.  The packet family in
`P_y` includes both multi-owner internal macros and optional external seam
witnesses, always with their complete survival implications.

#### Proof

If one literal in the first disjunction is true, the corresponding old edge
is not cut.  By the owner partition and packet-boundary assumptions its two
owners remain consecutive inside one final fragment, so they deliver `y`.
If one literal in the second disjunction is true, the selected literal path
of that packet has an adjacent owner pair whose union is `y`.

Conversely, every adjacency of the final forest is either an old adjacency
which was not cut, an adjacency internal to a selected replacement packet,
or a selected seam between two exposed packet/fragment ends.  Hence every
delivered `y` makes one literal of (2.1) true.  QED

When the old q1 deck is a bijection, as in the authenticated `k=17` SCD
owner factor, `E_y` is a singleton.  The clause is then simply

\[
              \neg z_{e_y}\vee\bigvee_{p\in P_y}x_p .           \tag{2.2}
\]

This is the exact replacement for the unsound rule "`y` occurred in the
pre-atlas, so it remains supported."

## 3. Simultaneous seam realization

Contract each already-literal packet and each surviving old fragment to one
oriented node.  A selected external witness is a directed arc from its left
node to its right node.

### Theorem 3.1 (typed seam forest realization)

Suppose the selected external witness arcs satisfy:

1. every node has selected indegree at most one and selected outdegree at
   most one;
2. no two selected arcs consume the same literal owner position;
3. every selected arc satisfies its boundary-cut, internal-noncut, and
   orientation implications, and every resulting directed chain is resident
   after its complete literal concatenation;
4. the selected directed graph is acyclic.

Then all selected witnesses are simultaneously realizable by concatenating
the corresponding literal fragments.  The result is a disjoint union of
oriented resident owner paths, and its immediate-upper deck is exactly the
union of the fragment decks and selected seam colours.

#### Proof

Conditions 1 and 4 make every weak component of the selected directed graph
a directed path.  Condition 2 makes the corresponding literal fragments
owner-disjoint.  Concatenate them in path order.  Condition 3 validates
each complete chain, not merely each pairwise join.  There are no other adjacencies, so
the displayed deck identity is exact.  QED

Pairwise residence of the selected arcs is **not** sufficient for condition
3.  If a short middle fragment is used once as a right endpoint and once as
a left endpoint, a coordinate can be boundary-clipped in both two-fragment
checks but become an internal run of length at most `h` in the three-fragment
concatenation.  A simple sufficient encoding is therefore

\[
 \boxed{\text{no literal segment is selected in both provider roles}}.       \tag{3.1}
\]

Under (3.1), every witness is an isolated two-fragment path, so the audited
pairwise residence test is complete.  The less restrictive exact alternative
is a chain-state automaton or lazy clauses blocking every selected arc chain
whose full literal concatenation fails residence.

The acyclicity row may be enforced lazily: whenever a SAT assignment contains
a directed cycle `C`, add

\[
                         \bigvee_{p\in C}\neg x_p .              \tag{3.2}
\]

If a bounded number of cycles is affordable as later opening seams, replace
acyclicity by the corresponding component/cycle budget rather than silently
assuming it.

### Exact `k=17` counterexample to pairwise residence composition

The first SAT assignment of the global-q1 master selected 1,815 external
provider seams.  Every selected provider passed the individual joined-path
residence audit.  Endpoint replay gave 3,148 range nodes, indegree and
outdegree at most one, and no directed cycle.  Nevertheless, concatenating
the resulting 1,333 complete chains produced

```text
143 chains with a residence defect;
172 short internal coordinate runs in total.
```

Thus pairwise residence, endpoint capacities, and acyclicity do not imply
whole-chain residence.  The SAT assignment remains a valid
immediate-upper **palette** assignment for Theorem 2.1, but it is not a
resident owner-path construction.

## 4. Consequence for the current `k=17` lane

The previous postbank CEGAR selected sockets, materialized the pieces, found
new q1 holes, and then protected witnesses for only those holes.  That loop
can create another hole because a newly selected cut may destroy a colour
which was merely present in the previous materialization.

The exact master instead does the following once:

1. create a cut variable for every old owner edge;
2. compute the literal q1 deck of every socket and fixed alternating macro;
3. export optional, one-seam-facing external witnesses with their full
   survival footprints;
4. add (2.1) for all `19,448` rank-ten colours;
5. impose typed endpoint capacities and lazy directed-cycle clauses;
6. replay the chosen literal paths and check all `19,448` colours directly.

The corrected fixed-`r3` provider threshold of eighteen is a restriction of
this formulation after the `r3` socket/cut choice is frozen.  It is useful
as a calibration and lower-bound core, but it is not the optimum of the
joint global master because the master may rechoose the socket and cut
variables.

### Exact finite calibration

The first integrated `r4` attempt kept the staged rule that every new cut
child had to belong to the previously priced target universe.  It is
propagation-UNSAT for the smallest possible reason.  Provider target `8154`
has two orientation-reversed witness variables `p_0,p_1`; both require cut
`z=z_(282,2)`.  That cut deletes the old unique provider of colour `73626`,
which the staged universe did not price, so it asserted `not z`.  The entire
verified DRAT core is

\[
       (p_0\vee p_1),\quad
       (\neg p_0\vee z),\quad
       (\neg p_1\vee z),\quad
       \neg z .                                           \tag{4.1}
\]

Thus the failure is not evidence against the socket geometry.  It is an
exact certificate that recursive prepricing is not closed under provider
cuts.  Clause (2.1) replaces the last unit by the correct obligation

\[
       \neg z\vee
       \bigvee_{p:\,73626\in U(p)}x_p .                    \tag{4.2}
\]

The colour `73626` has no clean external witness in the audited global
one-facing atlas, so any solution using this `8154` provider must retain its
old edge by another choice or deliver `73626` inside a literal socket/macro.

### First global-SAT replay and correction

A cap-256 socket / cap-32 provider instance of (2.1) returned SAT in
`108.47` seconds.  It selected `67` socket rows, `1815` provider seams, one
fixed fusion macro, and `1890` cuts; all `19,448` q1 clauses were satisfied.
The provider digraph was acyclic, with `1333` paths and maximum seven seams.
However, `482` segments were used in both provider roles.  Exact literal
concatenation found `143` nonresident chains containing `172` internal
positive runs of length two or three.  The assignment is therefore rejected.

This finite counterexample is the reason condition 3 above is stated for
whole chains.  The next exact-positive lane adds (3.1); the former SAT result
is not a q1-closed resident construction.

## 5. Scope boundary

Theorem 2.1 is exact only for the immediate-upper row.  Longer accumulated
unions depend on the order in which the resulting path pieces are joined.
They require the existing accumulated-union automaton or a literal final
path replay.  Likewise, lower q1 scalar credit and the occurrence-labelled
lower compiler are separate gates.
