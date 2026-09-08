# K17 GKS central (2\times2) switches: exhaustive single-switch hits

Date: 2026-08-01  
Lane: A, dynamic GKS seed for the incidence/deletion-spine master

## 1. Scope and result

This note considers one precisely delimited move class on an authenticated
1,430-row static GKS flag system.  It does **not** claim a changing-owner cycle
cover or a Hamilton carrier.

For each skip packet (p), write

\[
L_p=C^p_0,\qquad B_p=C^p_0\sqcup C^p_1,\qquad
Q_p=C^p_0\sqcup C^p_1\sqcup C^p_2,
\]

where (L_p,B_p,Q_p) have ranks (1,3,5), (6), and (8), respectively as
appropriate for the row type.  The 286 orbit classes \([B_p]\) are pairwise
distinct.

### Theorem 1 (exact central (2\times2) move)

Let (p\ne q) be skip packets.  A central alternating (2\times2) switch is
specified by:

1. aligned copies
   \[
   B'_p\in[B_q],\quad B'_p\subset Q_p,qquad
   B'_q\in[B_p],\quad B'_q\subset Q_q;
   \]
2. either assignment of the two existing lower items
   \([L_p],[L_q]\) to (p,q);
3. arbitrary aligned copies (L'_p\subset B'_p) and
   (L'_q\subset B'_q) of the assigned items.

Replace only the two rows by

\[
(C'_0,C'_1,C'_2,C'_3)
=(L',B'\setminus L',Q\setminus B',C_3).
\]

Then the new 1,430-row system has exactly the same:

- middle-owner and rank-8 rows;
- multiset of 286 rank-6 suffix orbits;
- multiset of lower item orbits and hence the nine age-type masses;
- complete suffix-orbit sets at every rank (2,\ldots,8).

In particular it is a valid static GKS age-flag certificate with a switched
central matching.

#### Proof

The two new bases lie in their stated (Q)'s and the two new lower copies lie
in their bases, so each displayed four-block row is a disjoint partition of
the unchanged owner.  The move interchanges the two right vertices
\([B_p],[B_q]\) of the central matching; consequently it preserves right
injectivity and the complete rank-6 suffix-orbit set.  It merely permutes the
two lower item orbits, so it preserves every lower quota and the type masses.
The rank-7 and rank-8 suffixes and the owner are unchanged row by row.  These
observations prove every assertion.  □

### Theorem 2 (exhaustive hit from switched seed 2512)

Take the authenticated low-switched seed

```
scratch/threadA_k17_gks_dynamic_switched_seed2512_20260801.tsv
```

of SHA-256

```
908651cb50f5a6e8d8f9fead205d252ed67efc95c36a220ec4e052bb089b2451
```

and form the exact changing-owner compatibility graph using all nine rank-9
attachments per packet and all recorded cyclic alignments.  The initial
packet-support bipartite graph has

\[
\nu=1158,qquad (z^+,z^-)=(202,191),
\]

where (z^+,z^-) are the numbers of zero out- and zero in-rows.

Exhausting every move of Theorem 1 gives:

- 135 cross-containment packet pairs;
- 179 admissible base/low-assignment shapes;
- 2,622 aligned phase choices before deduplication;
- 1,578 distinct two-row outputs;
- 8 outputs with packet-support matching larger than 1,158;
- 10 outputs with fewer zero packet out-rows;
- 16 outputs with fewer zero packet in-rows.

In particular, the switch on packets (1282,1295)

\[
(B_{1282},B_{1295})=(27657,26649)
  \longmapsto (26649,27657)
\]

and the crossed lower-item assignment

\[
(5,1163),(1,1)\longmapsto(1,1),(5,1163)
\]

with aligned phases (6,7) produces a literal static certificate with

\[
\nu=1159,quad (z^+,z^-)=(202,191),quad
(z^+_{\rm state},z^-_{\rm state})=(2227,10787).
\]

Thus one central (2\times2) switch strictly improves the exact packet-support
matching and reduces zero attachment-state in-rows by two.  Its packet-edge,
legal-turn, and labelled-state-arc counts are respectively

\[
3828,qquad3829,qquad30632.
\]

The literal candidate is

```
scratch/threadA_k17_gks_central_2x2_lexbest_seed2512_20260801.tsv
```

with SHA-256

```
0a5addd1c30a83aa4614b41b057c8c027a80e07e83dd8e566ddc90fed484f241
```

#### Exhaustiveness proof

The scanner loops over all unordered pairs of the 286 skip packets.  For each
pair it loops over all 17 rotations of each base orbit and retains exactly the
cross-containment copies.  It then loops over both bijections of the two lower
items and all 17 rotations of each assigned lower item, retaining exactly
those contained in its new base.  A candidate is deduplicated only by

\[
(p,q,B'_p,B'_q,L'_p,L'_q),
\]

which determines both complete changed rows.  Hence no distinct move in
Theorem 1 is omitted.

The rank-8 roots do not change.  Therefore a dynamic turn can change only if
its source is (p) or (q), or its target packet is (p) or (q).  The
scanner recomputes precisely those source rows and leaves all other rows
unchanged.  For each candidate it repairs a retained valid matching and runs
Hopcroft--Karp to exhaustion; starting from a valid partial matching does not
change the maximum obtained.  An independent full reconstruction of all
12,870 attachment states and all legal turns reproduces

```
PASS packets=1430 states=12870 turns=3829 state_arcs=30632
packet_matching=1159 zero_out=202 zero_in=191
```

Finally, an independent invariant replay checks that exactly packets 1282 and
1295 changed, that the 286 base orbits remain distinct with the same multiset,
that the lower-item multiset is unchanged, and that the rank-2--8 suffix counts
remain

\[
(8,40,140,364,728,1144,1430).
\]

This proves the finite theorem.  □

## 2. Earlier seed-2510 face

For provenance, the same exhaustive scan was run on seed 2510.  It found 135
cross-containment pairs and 1,865 distinct outputs; seven improve the matching.
The lexicographic packet-support hit swaps bases (31745,31760) at packets
1415,1419 and changes

\[
(1131,224,219)\longmapsto(1132,224,218).
\]

This face is retained as an independent calibration, but seed 2512 plus the
switch of Theorem 2 is the primary combined seed.

## 3. Exact boundary of the result

The number 1,159 is the maximum matching size of the **packet-support
relaxation for the emitted candidate**, not a feasible cycle packing.  A
changing-owner cycle cover must additionally choose:

1. one attachment state per packet;
2. one state per rank-9 owner orbit;
3. the same selected state for its incoming and outgoing turns;
4. the required cycle/subtour and voltage conditions.

The exhaustive catalogue here contains only alternating central 4-cycles.
It excludes alternating paths to unused rank-6 rights and central alternating
cycles of length at least six.  It also says nothing yet about the deletion
spine.  Consequently the theorem is a constructive dynamic **seed**, not a
K17 carrier.

## 4. Frozen artifacts

Primary seed-2512 artifacts:

| artifact | SHA-256 |
|---|---|
| `scratch/audit_threadA_k17_gks_central_2x2_single_switch_20260801.cpp` | `3d1a6c3597f24950b3d6f7cf0604624c0ec6ddac17a96d9f6664ef1312c9eeff` |
| `scratch/verify_threadA_k17_gks_central_2x2_single_switch_20260801.py` | `ce9db3f937311358b5e999c98a24e822e03116ba0255022fb906782b8bd9bee9` |
| `scratch/threadA_k17_gks_central_2x2_seed2512_single_switch_20260801.audit.json` | `34b5f88c572be5b7982d211ec884f05973f3c21aa4c20c1dc3a2175ab5c4119d` |
| `scratch/threadA_k17_gks_central_2x2_lexbest_seed2512_20260801.tsv` | `0a5addd1c30a83aa4614b41b057c8c027a80e07e83dd8e566ddc90fed484f241` |
| `scratch/threadA_k17_gks_central_2x2_lexbest_seed2512_20260801.switch.tsv` | `74a6816303aa0ef9f992dd48ea8201d25c4504a50f48bf081e48247bd1dfc866` |
| `scratch/threadA_k17_gks_central_2x2_lexbest_seed2512_turns_20260801.tsv` | `3fcaa7ebcbb679e598ba95ce53c0cf615be2c1c381f63f335a16fbf21862b2de` |
| `scratch/threadA_k17_gks_central_2x2_lexbest_seed2512_dynamic_20260801.audit.json` | `7d3eca56357c4597ce4b6ae3b81750e9b44b5c56a9b2e8eecbb52e1683c3a7fd` |
| `scratch/threadA_k17_gks_central_2x2_lexbest_seed2512_independent_20260801.audit.json` | `bc85204a1a2c18a4b6864824a6916adc013eadbe351a4021f211421f2e08bfa2` |

The exhaustive O3 C++ run used H100 CPU only.  It exited 0 in 0.18 seconds
with maximum resident set size 9,216 KiB.

Seed-2510 calibration artifacts remain under the parallel
`threadA_k17_gks_central_2x2_*seed2510*` names.
