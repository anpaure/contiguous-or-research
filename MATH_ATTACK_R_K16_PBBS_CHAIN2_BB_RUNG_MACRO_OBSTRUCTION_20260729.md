# Lane R: the fixed chain2 PBBS B–B/rung macro has a 62-colour upper-q1 obstruction

Date: 2026-07-29

## 1. Result

The fixed 567-cut segmentation derived from
`scratch/k16_pbbs_component_trade_chain2_20260729.json` cannot be completed to
an upper-q1-complete degree-two factor using only:

1. retained A-rail and B-segment interior edges;
2. containment A–B rungs; and
3. nonfactor B–B Johnson joins.

No new A–A seam is allowed.  This is exactly the restricted B–B/rung macro
class requested in this lane; arbitrary rungs are not present.

The obstruction is local and integral.  Among the 567 B-upper colours removed
by the fixed cuts, exactly 62 have no legal replacement.  Therefore the class
already fails upper q1.  The conclusion is independent of lower q1,
length-three residence constraints, A-cut spacing, opening both A components,
and macro connectivity.

An exact H100 CP-SAT model corroborates this theorem: the full model returned
`INFEASIBLE` after 0.160291533 seconds, and the upper-only diagnostic returned
`INFEASIBLE` after 0.094952509 seconds.  The decisive proof below does not
depend on either solver result.

## 2. Exact input replay

Let \(z=15\) be the new coordinate.  The A shore consists of the rank-eight
subsets of \([15]\).  The B shore consists of \(\{z\}\cup R\), where
\(R\in\binom{[15]}7\).

The 27-trade chain changes 81 quotient labels and materializes a B factor with
21 physical components.  Its component-length multiset is

\[
15^2\,45^4\,75^7\,105^6\,195^1\,4875^1.
\]

It partitions all \(6435=\binom{15}7\) B states.  Before cutting, its lower-q1
support is all \(5005=\binom{15}6\) colours with load histogram

\[
1^{3645}2^{1290}3^{70},
\]

and its upper-q1 support is all \(6435=\binom{15}8\) colours with load one
each.  It has one repeat-edge-inaccessible component of length 15.  Its old-
coordinate short positive runs have histogram

\[
2^{195}3^{615}.
\]

The B cut artifact is marked `OPTIMAL` for its generating lexicographic cut
model; the independent replay here proves its certificate and counts, not that
optimization claim.  It has 567 cuts and 567 segments.  The minimum
segment length is three, and exactly 60 segments have length three.  All 810
old-coordinate short-run closures are hit.  The cuts lose exactly 17 B-lower
colours and 567 distinct B-upper colours.  The certificate supplies 17
vertex-disjoint nonfactor B–B joins whose lower colours are exactly those 17
lost lower colours.

The independent input audit also enumerates all 6981 nonfactor B–B candidates.
On the 60 length-three B segments, the 45 short–short candidates form exactly
15 disjoint copies of \(P_4\): the segment-degree histogram is
\(1^{30}2^{30}\), and the component-size histogram is \(4^{15}\).  Thus 30
B–B joins suffice and are necessary merely to give every length-three segment
a B–B neighbour.  No B–B candidate whose lower colour is one of the 17 lost
colours touches a length-three segment.  Consequently every restricted macro
would need at least

\[
30+17=47
\]

B–B joins.  Since port balance gives

\[
\#AB=2a,\qquad \#BB=567-a,
\]

where \(a\) is the number of A cuts, necessarily \(a\le 520\).  This bound is
valid but is not the decisive obstruction.

## 3. Restricted macro and its exact q1 ledger

Fix the 567 B segments.  Cut a set of A-factor edges, exposing the two
halfports of each cut.  A restricted macro is a perfect matching of all exposed
halfports with these allowed seam types:

- an AB seam joins \(X\in\binom{[15]}8\) to
  \(\{z\}\cup R\), where \(R\subset X\) and \(|R|=7\);
- a BB seam joins \(\{z\}\cup R\) to \(\{z\}\cup S\), where
  \(|R\mathbin\triangle S|=2\), the endpoints lie on distinct fixed
  segments, and the seam is not the deleted original B-factor edge;
- no AA seam is admitted.

For an edge \(P-Q\), its lower and upper q1 colours are \(P\cap Q\) and
\(P\cup Q\).  The four physical palettes split as follows:

- lower colours without \(z\): retained AA interiors and AB seams;
- lower colours with \(z\): retained BB interiors and BB seams;
- upper colours without \(z\): retained AA interiors only;
- upper colours with \(z\): retained BB interiors, AB seams, and BB seams.

The third row is the rigidity responsible for the no-go: an A edge whose
no-\(z\) upper colour has global load one cannot be cut, because every allowed
replacement seam has \(z\) in its upper colour.

### Exact seam-residence interface

The unexecuted fixed-segment successor model includes full old-coordinate seam
residence, not merely the length-three \(z\) rows.  Its criterion is as follows.
For an oriented port \(p\) of a segment and a coordinate \(x\), let
\(r_p(x)\) be the length of the positive prefix seen when reading inward from
that port, and let \(e_p(x)\) say that the entire segment contains \(x\).
Every fixed segment has length at least three, and the cut certificate has no
positive run of length below four sealed strictly inside a segment.

For a proposed seam \(p-q\), reject it if either of these conditions holds:

1. exactly one of \(r_p(x),r_q(x)\) is positive, that positive terminal piece
   is not an entire-segment piece, and its length is below four; or
2. both terminal pieces are positive, neither is an entire-segment piece, and
   their sum is below four.

In addition, for every coordinate that fills an entire segment of length
three, require at least one of the segment's two selected seam neighbours to
contain that coordinate.  For a length-three B segment and coordinate \(z\),
this is exactly the requirement that the segment have an incident BB seam.

These local candidate tests plus the entire-length-three rows are necessary
and sufficient for residence at least four after a port-perfect matching is
selected.  Indeed, every final positive run is either sealed in an interior,
crosses one seam between two non-entire terminal pieces, or passes through an
entire segment.  The first case is safe by the fixed-cut audit, the second is
exactly covered by the two rejection rules, and an entire segment of length at
least four is already safe.  The only remaining case is an entire length-three
segment, handled by its explicit continuation row.

The selected seam matching makes the contracted segment graph 2-regular.
Standard subtour rows requiring at least two selected seams across every
proper current component force it to be one cycle when separation is continued
to convergence.  Thus, conditional on a feasible q1 scaffold, the mathematical
successor formulation is an exact integral Hamilton/residence model for this
restricted class.  The implementation has a finite `--rounds` cap: a replayed
`PASS` is exact, whereas exhausting that cap would not prove infeasibility.
The upper-q1 obstruction below prevents any scaffold from reaching the
successor here.

## 4. Local upper-colour obstruction theorem

### Theorem 4.1

Let \(C\in\binom{[15]}8\) be a B-upper colour whose unique B-factor edge was
deleted by the fixed cut certificate.  Suppose:

1. no allowed nonfactor BB seam between exposed B halfports has old-coordinate
   union \(C\); and
2. both A-factor edges incident with the A state \(C\) have no-\(z\) upper
   colours of global A-load one.

Then no restricted macro covers the child upper-q1 target \(\{z\}\cup C\).

### Proof

The original B factor used every old rank-eight upper colour exactly once, so
deleting its unique edge of colour \(C\) removes the only retained B-interior
witness for \(\{z\}\cup C\).

An AA interior or seam cannot have upper colour \(\{z\}\cup C\), because it
does not contain \(z\).  By hypothesis 1, no allowed BB seam has that colour.
Hence a replacement would have to be an AB seam.  Every AB seam with upper
colour \(\{z\}\cup C\) has A endpoint exactly \(C\).  Installing it requires
cutting one of the two A-factor edges incident with \(C\).  By hypothesis 2,
that cut deletes the sole witness of a no-\(z\) rank-nine A-upper colour.  No
AB or BB seam can restore a no-\(z\) upper colour, and AA seams are forbidden.
Thus upper q1 cannot remain complete.  This contradiction proves the theorem.
\(\square\)

### Theorem 4.2: exact chain2 count

Exactly 62 of the 567 deleted B-upper colours satisfy Theorem 4.1.  They are

```text
3279, 4925, 4943, 6558, 6627, 6777, 6873, 6972, 7707, 7731,
7827, 9423, 9699, 9850, 10131, 12907, 13116, 13251, 13254,
13266, 13554, 15177, 15414, 15462, 15509, 15514, 15654,
15658, 17255, 18023, 18071, 18846, 18855, 19132, 19697,
19700, 19772, 20237, 20249, 20262, 20297, 21085, 21095,
23009, 24133, 24138, 25395, 25419, 26232, 26508, 26532,
26931, 27000, 27108, 27888, 29081, 29093, 29849, 30924,
30930, 31028, 31308
```

The independent enumeration gives the following histogram for the number of
locally upper-safe replacement candidates over all 567 deleted colours:

\[
0^{62},2^{167},4^{18},5^{99},8^{53},9^{41},13^{27},14^{33},
19^{63},20^1,26^3.
\]

### Canonical one-colour witness

Take \(C=3279\), so the child target is
\(\{z\}\cup C=36047\).  The fixed cut deletes B edge

\[
3271-3278,
\]

whose lower and upper old colours are 3270 and 3279.  The two exposed B subset
ports of \(C\) are exactly 3271 and 3278.  Their original edge is forbidden,
and there is no other nonfactor exposed BB seam with union 3279.

The A state 3279 occurs between

\[
3294-3279-19599.
\]

The incident A-edge upper colours are respectively 3295 and 19663, and each
has global A-load one.  Therefore neither incident A edge can be cut in an
upper-q1-complete no-AA macro.  No AB seam can enter state 3279, and target
36047 is impossible.

## 5. Exact model and H100 corroboration

The exact scaffold model contains 6435 A-cut variables and 25,125 seam
variables:

\[
18,144\text{ AB} + 6,981\text{ BB}.
\]

It enforces every B-port equation, every active A-port equation, all
\(\binom{16}7\) lower-q1 rows, all \(\binom{16}9\) upper-q1 rows, the 60
length-three B–B incidence rows, A spacing, both A-component opening rows, and
the exact port-count identities.  The full H100 run returned `INFEASIBLE`
after 0.160291533 seconds.  A diagnostic retaining upper q1 but
dropping lower q1 also returned `INFEASIBLE` in 0.094952509 seconds.

These solver artifacts are corroboration only.  The independent audit in
Theorem 4.2 reconstructs the palettes and all legal local replacements without
importing the CP-SAT model and gives a literal finite obstruction.

## 6. Comparison with the direct quotient benchmark

The benchmark
`scratch/k16_connected_q1_lower2_hamilton_20260729.json` has file SHA-256
`16fc3739b8b4df5bed71c44b2f2e148f4839753cab6b9ea308e78d17ee9c32d8`
and status `PARTIAL_Q1_PHYSICAL_HAMILTON`.
Its internal canonical payload hash replays as
`78f59c566d3cc86b960978540b3d778f4de281745e07012e22050b0e7a64e407`.
The physical audit replays exactly:

- one Hamilton cycle of length 12,870;
- two quotient lower-q1 holes and zero quotient upper-q1 holes;
- residence short-run histogram \(1^{375}2^{1635}3^{1410}\), totaling 3420;
- 89 lower-q2 orbit holes; and
- 129 all-upper orbit holes.

Thus the direct quotient construction currently wins connectivity and is close
to q1, but is far from residence and deeper-shadow completion.  The PBBS input
has the desired correlated shadow structure and admits residence-safe segment
staging, but the present fixed no-AA braid cannot even pass upper q1.  Hence no
completed PBBS carrier from this class exists to claim an advantage over the
benchmark.

## 7. Separate 226-motif deletion obstruction

A second exact certificate, on the distinct source
`scratch/k16_qfactor_q1_topresident_hamilton_20260729.json`, shows why
residence and q1 cannot be repaired sequentially by a palette-safe deletion
phase.

That source selects 858 edge orbits.  Its current residence obstruction is a
family of 226 edge-set motifs.  In the deletion relaxation, one chooses current
edges to remove, must hit every motif, and for each of the 764 current lower-q1
provider rows and 764 current upper-q1 provider rows must leave at least one
provider.  The exact model deliberately omits replacement edges, degree two,
connectivity, voltage, and newly created residence motifs.

The palette-safe hitting artifact returns `INFEASIBLE`.  When provider holes
are allowed and the objective lexicographically minimizes total provider holes
and then removals, the artifact is marked `OPTIMAL` with

\[
148\text{ removals},\qquad 88\text{ lower holes},\qquad
92\text{ upper holes},
\]

so the minimum reported palette loss is 180.  An independent replay verifies
that the saved 148-edge set hits all 226 motifs and destroys exactly 88 current
lower provider rows and 92 current upper provider rows.  The replay verifies
the witness and counts; the solver artifact supplies the optimality claim.

This is not a no-go for a joint rethread, because new edges may replace the
lost providers while removing old residence motifs.  It is a precise no-go for
the strategy “delete to residence first while preserving every present q1
provider.”  Together with the chain2 62-colour obstruction, it makes the next
valid object a joint global residence-plus-q1 rethread, not a deletion phase
followed by an independent palette repair.

## 8. Sharp remaining alternatives

This report rules out only the fixed chain2 567-cut, no-AA restricted macro.
It does not rule out any of the following:

1. a different B cut certificate for which every deleted B-upper colour has a
   nonempty upper-safe repair set;
2. an AA replacement library that restores the no-\(z\) A-upper colours spent
   by AB ports;
3. a larger exact packet that changes B segment interiors, rather than merely
   reconnecting their exposed endpoints; or
4. a different A factor whose two incident upper loads at the blocked states
   are not both one.

For any future fixed-cut no-AA attempt, the exact first filter is:

> For every deleted B-upper colour \(C\), either an allowed nonfactor BB seam
> has union \(C\), or some exposed B endpoint is contained in \(C\) and at
> least one A edge incident with state \(C\) can be cut without deleting the
> last no-\(z\) upper witness.

Passing this pointwise filter is necessary, not sufficient; the surviving
candidates must still satisfy the global port matching, both q1 ledgers,
residence, connectivity, deeper shadows, opening-edge survival, and COMP_3.

## 9. Audited artifacts and hashes

- Chain:
  `scratch/k16_pbbs_component_trade_chain2_20260729.json`,
  SHA-256 `5c6de82ca63900686f8aeb30c6817c702f34b846f5fdcbe3cb853ecd4d2d401a`.
- Materialized B factor:
  `scratch/k16_pbbs_component_trade_27_factor_20260729.json`,
  SHA-256 `91c434654d38466790dd373d26ff4e88f115d7cab1c29f71520a99cc4b349985`.
- 567-cut certificate, marked `OPTIMAL` by its generating model:
  `scratch/k16_pbbs_component27_bbrestorable_cuts_20260729.json`,
  SHA-256 `3ed33e6a32cbf3e93beccd183f85deb439f3bac43d015422e14bbb260ccf5f27`.
- A factor:
  `scratch/k15_two_component_a_cycles_20260729.json`,
  SHA-256 `bc58e466e72c0b418aa24929d45640dcfe6ffbe567caae480939e76367533738`.
- Independent factor/cut/BB input replay:
  `scratch/k16_pbbs_chain2_bb_rung_input_20260729.independent.audit.json`,
  SHA-256 `61d8b48d7edcd88c24d4819bbd4d92446b42d2f780ccb20bdd1f5b16df14fc10`.
- Its verifier:
  `scratch/audit_k16_pbbs_chain2_bb_rung_macro_20260729.py`,
  SHA-256 `913071d1832af5ab3eff82edd55bb35ba4b5912889fdbbc917be1f42e5a9763c`.
- Restricted joint-q1 formulation:
  `scratch/solve_k16_pbbs_joint_q1_rewire_20260729.py`,
  SHA-256 `20f4c08801173f0a3b13c734102f8a63a4c914833c7a1bee479a94102adc9082`.
- Exact fixed-segment residence/connectivity successor:
  `scratch/solve_k16_pbbs_fixed_segments_q1_residence_20260729.py`,
  SHA-256 `55b6a0fd7c6cc896685b91845dca4ec05c323ef17b33985e12a54233eeb21d7c`.
- Independent 62-colour obstruction audit:
  `scratch/k16_pbbs_chain2_restricted_upper_q1_local_obstruction_20260729.audit.json`,
  SHA-256 `e7a84a349ccf0043e7995845f42034ea117b40f3c4e52e46992f8d3f6c87dc54`.
- Its verifier:
  `scratch/audit_k16_pbbs_chain2_upper_q1_local_obstruction_20260729.py`,
  SHA-256 `c36db4ee1d561a6c81d707ff277c6cd2b9b274d0764571d6f5eed7eccb1dcae5`.
- Full H100 restricted-model result:
  `scratch/k16_pbbs_chain2_restricted_q1_scaffold_s20260729.json`,
  SHA-256 `ab588bd5d6fbc0d1a106c93d7a426464abb585e80785a0a9eef8c2487d089c11`.
- H100 upper-only diagnostic:
  `scratch/k16_pbbs_chain2_restricted_upperonly_diagnostic_20260729.json`,
  SHA-256 `dc632bad8f6e5ebd6f3b8031060ac5d6563e1ff6298d085d535e59cbacacedc2`.
- Residence-motif palette-safe hitting result:
  `scratch/k16_residence_motif_palette_safe_hitting_20260729.json`,
  SHA-256 `9c451d60839ba1085c64a37807d041c4fe2d0062ecc4285faded33f24e803780`,
  canonical payload hash
  `090a605843d3fd6680a7b2ede60c8dbd167657007f2257241ab59ea80f720e32`.
- Residence-motif minimum-hole hitting result:
  `scratch/k16_residence_motif_minholes_hitting_20260729.json`,
  SHA-256 `7afddc14dfbd0daa825c6a19045e7d95c9e9bb745165bfb1145a2df76a354827`,
  canonical payload hash
  `c2886461637a714b96102b1db93d14ab2a5847e729a8ece3840cc28b24fce533`.
- Residence-motif hitting formulation:
  `scratch/solve_k16_residence_motif_palette_safe_hitting_20260729.py`,
  SHA-256 `0d87153ebba4577add71c376aeca94a181cb449483dc582550fd68db72be838d`.
- Independent residence-motif witness replay:
  `scratch/k16_residence_motif_hitting_20260729.independent.audit.json`,
  SHA-256 `0403de55c60e7f5f362b068edebda3a68f2859441b34a55227565cba12f987ab`.
- Its verifier:
  `scratch/audit_k16_residence_motif_hitting_20260729.py`,
  SHA-256 `94e988589d437af99c2b416ac912ac3e2795ef92a7cfdea15b66d7a0152e9710`.

## 10. Claim boundary

Proved: the chain2 B factor, the 567-cut segmentation, the 17 lower restorers,
the exact \(15P_4\) length-three BB graph, the 47-join lower bound, the 62
pointwise upper-q1 obstructions, and infeasibility of the fixed no-AA
B–B/rung macro.  Also verified: the saved 148-edge residence-motif transversal
hits all 226 motifs and has the stated 88/92 provider losses.

Not proved: infeasibility for a different B cut certificate, for an AA-enabled
macro, or for a packet that changes interiors.  No Hamilton carrier, deeper-
shadow carrier, literal k16 word, opening seam, or COMP_3 certificate is claimed
from the obstructed class.
