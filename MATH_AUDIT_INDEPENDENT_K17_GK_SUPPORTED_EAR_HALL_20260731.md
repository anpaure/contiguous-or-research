# Independent audit of the all-length fixed-GK supported-ear Hall obstruction

## Verdict

The obstruction in
`MATH_THEOREM_H2_K17_GK_RAINBOW_EAR_ENDPOINT_HALL_OBSTRUCTION_20260731.md`
reconstructs independently.

On the immutable two-cut Greene--Kleitman forest, the greatest locally
supported ear-edge catalogue induces a bipartite relation from the (2224)
missing rank-six colours to (6530) fresh rank-eight unions.  Its exact
statistics are

\[
|E(B)|=33564,qquad \nu(B)=1780,qquad 2224-\nu(B)=444.
\]

There are 416 zero-provider rows.  The independently reconstructed
Dulmage--Mendelsohn witness has exactly

\[
|S|=584,qquad |N(S)|=140.
\]

The two mask lists agree literally with the H2 artifact, not only in size.

## Exact provider definition

Let (E) be the old degree-one rank-seven vertices and (U) the rank-seven
vertices absent from the GK forest.  A raw carrier edge is a Johnson edge
(xy) with (x,y\in E\cup U) satisfying all of the following:

1. (x\cup y) is not a retained GK rank-eight colour;
2. if an endpoint lies in (E), the forced turn through its retained old
   neighbour is a fresh rank-nine colour;
3. the two endpoint turns of an (E-E) edge are different; and
4. an (E-E) edge does not join the two ends of the same old component.

At (u\in U), two incident raw edges (ua,ub) support one another when

1. their rank-eight unions are distinct;
2. (a\cup u\cup b) is a fresh rank-nine colour;
3. this central turn and any forced endpoint turns are pairwise distinct;
   and
4. if (a,b\in E), they belong to different old components.

Starting from all raw edges, repeatedly delete an edge whenever it has an
unused endpoint at which it has no active compatible partner.  The resulting
greatest fixed point contains 145117 of the 148153 raw edges.  Direct
edge-only reconstruction deletes 3036 edges in its first pass and no more in
the second.  Recounting compatible pairs in the fixed point gives 4194675
supported wedges, exactly matching the producer's stored-wedge computation.

For a missing rank-six colour (c) and a fresh rank-eight colour (q), put

\[
c\sim q
\]

precisely when the unique Johnson edge with intersection (c) and union
(q) survives this support peel.  This is the provider graph audited above.

## Why arbitrary ear length cannot evade the obstruction

Consider any locally clean completion which leaves the GK forest untouched.
After splitting its new-edge paths whenever they meet an old endpoint, every
piece has the form

\[
E-U-\cdots-U-E.
\]

Every selected edge passes the raw edge tests.  At each internal unused
vertex, its two selected neighbours form a compatible support pair.  Hence
the selected edge set is a post-fixed point of the deletion operator.
Inductively, none of its edges can be deleted during the greatest-fixed-point
peel.  This argument has no bound on the number of (U)-vertices in a piece.

The completion must realize every one of the 2224 missing rank-six colours.
Choose one selected edge for each such colour.  All chosen edges survive the
peel.  Since the proposed tail uses distinct rank-eight edge unions, their
2224 upper colours are distinct.  They would therefore define a matching of
the provider graph saturating all 2224 left rows.  The exact matching rank
1780, or already the explicit inequality (584>140), rules this out.

Longer ears can create more internal slots, but they cannot create a provider
outside the greatest supported relation.  This is why the Hall obstruction
is genuinely all-length.

## Relationship to the earlier 294-core matching

The explicit matching of 294 all-unused rank-six cores is not contradicted.
That matching checked only disjoint unused rank-seven endpoints and fresh
rank-eight unions.  It did not require the chosen core edges to extend through
fresh rank-nine-supported paths to old endpoints.  Unsupported core edges are
removed by the fixed-point peel.

The simpler ledger obstruction is also independently valid: 674 missing
rank-six colours have no old endpoint superset, while the displayed
((4024,905,252,42)) ledger has only

\[
252+2\cdot42=336
\]

unused--unused slots.  Its deficiency is 338.  The all-length Hall no-go is
strictly stronger and does not assume this ledger.

## Scope

This closes only ears on the **immutable** GK forest.  Cutting an old edge,
exposing an old internal vertex, changing the retained palettes, or replacing
the base forest changes the provider relation and lies outside the theorem.
No unrestricted (k=17) no-go and no statement about the prefix or upper
continuation is made.

## Independent implementation

The audit implementation stores no wedge catalogue and does not read the
producer relation:

- `scratch/audit_independent_k17_gk_supported_ear_hall_20260731.cpp`,
  SHA-256
  `2782d53b6eea4085efd5a362c60e775ee25c11a1c285226c26cdc88f0327841c`;
- `scratch/independent_k17_gk_supported_ear_hall_20260731.audit.json`,
  SHA-256
  `abb87860e09986f51e3aaf986bfed041853a109cf695cf8ff18a57cec89660d2`.

The producer theorem/artifact hashes inspected were:

- theorem:
  `3f7db074d47843db90b5fcd7f2f5b01437010d0ec4545235744f6ec63d9d1fec`;
- producer C++:
  `31ad0118b6da29f16c86800427f7c22ff4a24a9cf00cded4b9184e4d83b25cf1`;
- emitted provider relation:
  `ff4eae65903fa0745d459354a38707b70140e28afcf2a2318533052f8e0dc63f`.
