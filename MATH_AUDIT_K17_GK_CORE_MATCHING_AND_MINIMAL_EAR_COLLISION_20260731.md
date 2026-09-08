# K17 two-cut GK tail: the 294 cores match, but the 252/42 minimal-ear schedule does not

## Scope

This note audits only the fixed two-cut Greene--Kleitman forest in
`PROPOSED_K17_TWO_ZONE_GK_EAR_CONSTRUCTION_20260731.md`.  It does **not**
construct the remaining ears, the prefix, the upper witness bank, or a word of
length (24313).

## The core matching is feasible

Let (mathcal C) be the 294 missing rank-six colours all of whose eleven
rank-seven supersets are unused by the authenticated GK forest.  There is an
explicit choice

\[
  C\longmapsto (X_C,Y_C),\qquad X_C\cap Y_C=C,
\]

such that

1. the (588) vertices (X_C,Y_C) are all different;
2. every one is an unused rank-seven vertex; and
3. the (294) rank-eight unions (X_C\cup Y_C) are all different and avoid
   the (10152) GK rank-eight colours.

This is checked independently from the certificate, after reconstructing the
GK forest from the two pivot definitions.  Thus there is no Hall obstruction
at the bare core-edge level.

## Exact two-row endpoint obstruction

Call an ear *clean* when all of its new rank-eight edge unions and rank-nine
turns are fresh relative to the GK forest, its internal vertices are unused,
and its two old endpoints lie in different GK components.

For the missing rank-six colour

\[
  C_4=45571,
\]

complete enumeration gives no clean three-edge ear and exactly six oriented
clean four-edge ears.  Every one of the six uses the old GK endpoint

\[
  e=111122.
\]

For the different missing rank-six colour

\[
  C_3=111105,
\]

complete enumeration gives exactly two oriented clean three-edge ears.  Both
also use (e=111122).  No ear in either catalogue covers the other designated
rank-six colour on a second edge.

Consequently the two rows cannot be served simultaneously by distinct ears:
all (6\cdot2=12) candidate pairs collide at (e).  In particular,

> the per-colour split “252 colours have a clean three-edge ear and 42 first
> have a clean four-edge ear” cannot be promoted to a simultaneous
> resource-disjoint (252/42) ear schedule on this fixed GK forest.

This is a two-row exact obstruction, not a solver timeout.

The first two promotions do not remove this particular collision.  Colour
(111105) has no clean four-edge ear.  It has exactly 808 clean five-edge
ears, but every one contains rank-eight colours (111117,111123) and
rank-nine colours (111119,111127,111131,111133).  Every clean four-edge ear
for (45571) contains rank-eight colour (111123) (and overlapping forced
rank-nine colours), so all (6\cdot808) pairs still collide.

In fact, merely lengthening the (111105) ear can never suffice while the
(45571) ear remains minimal.  Any such ear has a central segment
(p-x-y-q) with (x\cap y=111105).  Exhausting all 5292 clean central
segments against the six fixed (45571) ears gives zero resource-compatible
pairs.  Additional path before (p) or after (q) cannot change that local
collision.

Lengthening **both** ears is not locally ruled out: their clean central
segments have 903744 resource-compatible pairs.  However, seeded pools of
1471 clean six-edge (45571) ears and 211 clean six-edge (111105) ears had
no compatible pair.  This last negative is diagnostic only and is **not**
used as a theorem.

The most literal local cut also does not suffice.  The component containing
(111122) is the three-vertex path

\[
45110-45590-111122.
\]

Deleting (45110,45590) leaves 8 clean four-edge candidates for (45571)
and 2 clean three-edge candidates for (111105), but zero compatible pairs.
Deleting (45590,111122) leaves 4 and 0 respectively.  This is an exact
two-cut census under the convention that an isolated retained carrier vertex
is not recycled as an ear-internal vertex.

## What remains open

The obstruction is scoped to the authenticated forest.  It may be removed by
lengthening both ears further, by a nonlocal cut/rethreading of the GK forest,
or by changing the base forest.  It says nothing against the proposed (k=17)
length or against another tail design.

## Reproducibility

- core producer:
  `scratch/search_k17_gk_special_ears_20260731.cpp`;
- core certificate:
  `scratch/k17_gk_294_core_matching_20260731.certificate.json`;
- independent audit:
  `scratch/audit_k17_gk_special_ears_20260731.py`;
- audit payload:
  `scratch/k17_gk_special_ears_20260731.audit.json`;
- non-rigorous length-six probe:
  `scratch/search_k17_gk_hard_pair_length6_20260731.py`;
- exact two-local-cut audit:
  `scratch/audit_k17_gk_hard_pair_local_cuts_20260731.py`.

At freeze time the core certificate SHA-256 was
`4cb61bd8205e880c02e18bd989d1922cfe06d012d9931986326a830d5c7eb508`.
The independent audit's canonical payload SHA-256 was
`399e82dd2ecea2eaac0d09c9e431e8ea0ae6c7dc5c5800c5794df3db3d961c41`.
