# Exact Hall/DM audit of K16 split-pair chronology 229

Date: 2026-07-30  
Lane: AD, Hall-core repair  
Status: **proved finite theorem; supersedes pass1 as the active Hall base**

## Frozen input

The chronology is

`scratch/ad_k16_bad2_splitpair_exact_20260730/exact_229.targets`

with SHA-256

`cae23cfcedbc9d193ebd9191045edd0e5c14f56af5fc96a802b8cefa7cd7e974`.

The original Hall record

`scratch/ad_k16_bad2_splitpair_exact_20260730/exact_229.hall.k.audit.json`

has SHA-256

`85471243dcdd8a8ab6dc7530fc49b6629202b4403ad90a750961153afd0b1fb0`.

The independent replay

`scratch/ad_k16_splitpair_exact229_hall_dm_20260730/audit_exact229_hall_dm.py`

uses only the Python standard library and independently reconstructs maximal
source envelopes, forced-bit carriers, all proper-prefix cells, all
lower-target incidences, maximum matching, canonical alternating shore, and
its incidence components.  It imports neither the compiler implementation nor
the original Hall audit.

## Exact semantics

For the frozen rank-eight rows (T_i), the forced depth starts at three and
drops by one after each adjacent equality.  The equality starts are

\[
6320,\quad12869,\quad12871,
\]

and the depth histogram is

\[
d=3:6321,\qquad d=2:6549,\qquad d=1:2,\qquad d=0:1.
\]

Let

\[
P_p=\bigcap_{i:i\le p\le i+d_i}T_i
\]

be the maximal source envelope.  A right vertex is a proper-prefix cell
(J=[s,s+\ell)), (1\le\ell\le d_s).  Write

\[
E_J=\bigcup_{p\in J}P_p
\]

and let (M_J) contain a row bit whenever all positions on which that bit can
be supplied lie inside (J).  For a nonempty lower target (S) of rank below
eight, the exact one-cell incidence law is

\[
S\sim J
\iff
S\subseteq E_J,quad M_J\subseteq S,
\quad S\cap P_p\ne\varnothing\text{ for every }p\in J.
\tag{1}
\]

Necessity follows from envelope containment, nonempty source letters, and
forced row bits.  For sufficiency set (A_p=P_p\cap S) on (J) and
(A_p=P_p) off (J).  Condition (1) makes all letters on (J) nonempty and
their union exactly (S).  A required row bit either has a carrier outside
(J), where it is retained, or its whole carrier lies in (J), in which case
it belongs to (M_J\subseteq S) and is retained there.  Hence every row
equation remains exact.  This proves exact feasibility for one prescribed
cell; it does not assert simultaneous coexistence of all matched cells.

## Main theorem

### Theorem

The exact bipartite graph defined by (1) has

\[
|L|=26,332,\qquad |R|=32,063,\qquad |E|=347,875.
\]

Its maximum matching cardinality is exactly

\[
26,307,
\]

so its Hall deficiency is exactly

\[
25.
\]

The deterministic maximum matching leaves the following 25 targets
unmatched:

```
05ce 095d 1665 22cd 2665 27a4 28e9 291d 29a9 2f28
4879 48e9 4e70 5a29 6989 6a29 6c70 6cb0 6e28 72e0
8000 8cd8 a1a9 a91c d342
```

There is one rank-one unmatched target and 24 rank-seven unmatched targets.

### Exact certificate proof

The file

`scratch/ad_k16_splitpair_exact229_hall_dm_20260730/exact229_hall_dm.matching.tsv`

contains 26,307 pairwise-disjoint legal incidences.  Its SHA-256 is

`ec5214060e21620ab66764c0c2b46ad92007a022c854e0221955e8a0b5e56627`.

Alternating reachability from the unmatched left vertices gives an explicit
shore (X) and its full neighbourhood with

\[
|X|=212,qquad |N(X)|=187.
\]

Thus no matching can cover more than
(26,332-(212-187)=26,307) left vertices.  The explicit matching attains this
bound, proving both the maximum and deficiency exactly.

The entire left shore, every neighbour cell identifier, every neighbour
cell's start/length/allowed/mandatory data, and every DM component are frozen
in

`scratch/ad_k16_splitpair_exact229_hall_dm_20260730/exact229_hall_dm.audit.json`.

Its internal stable payload SHA-256 is

`be6e38425c722e112040efb0a6e02be1f3753155c6082450704e43f0e71ae819`.

The left-shore rank histogram is

\[
1:1,\qquad5:6,\qquad6:44,\qquad7:161.
\]

## Zero-degree targets

Exactly 12 lower targets have no candidate cell:

```
2665 28e9 291d 29a9 2f28 4879 48e9 4e70 6989 6a29 6c70 8000
```

Here `8000` has rank one and the other 11 have rank seven.  Every one is a
singleton (1/0) DM component.

## Full component decomposition

The shore incidence graph has exactly 25 connected components, all of
deficiency one.  The 12 zero-degree components are the singleton components
listed above.  The 13 nontrivial components are:

| component | left/right | unmatched root |
|---:|---:|---|
| 0 | 15/14 | `22cd` |
| 1 | 34/33 | `05ce` |
| 2 | 35/34 | `8cd8` |
| 3 | 18/17 | `27a4` |
| 4 | 7/6 | `1665` |
| 5 | 4/3 | `095d` |
| 6 | 3/2 | `a1a9` |
| 9 | 3/2 | `a91c` |
| 12 | 6/5 | `6e28` |
| 14 | 44/43 | `72e0` |
| 17 | 4/3 | `5a29` |
| 19 | 23/22 | `d342` |
| 22 | 4/3 | `6cb0` |

Unlike pass1, exact229 has no gap-two component: all 25 deficit units are
separated componentwise.

## Exact change from detached-7 pass1

The deficiency falls from 34 to 25.  At the zero-degree level, exact229 gives
new candidates to nine old singleton debts

```
4339 4378 5439 5670 583c 5c70 6a38 6a70 6b21
```

but creates two new zero-degree targets

```
291d 2f28
```

for a net reduction of seven zero-degree components.  The remaining two units
of the total Hall improvement come from the nontrivial alternating shore,
including removal of pass1's unique (10/8) gap-two component.  This
comparison is exact set subtraction between the two independently replayed
graphs; it does not attribute the improvement to a unique local edit.

## Collar-role test against the actual shore

The three advertised loss-robust collar roles remain exactly relevant:

* `8000` is a zero-degree singleton (1/0) component;
* `2665` is a zero-degree singleton (1/0) component;
* `0665` lies in the unchanged (7/6) component

  ```
  {0665,066d,0675,06e5,0765,1665,8665}.
  ```

Consequently, a globally embeddable exact+upper-preserving collar whose three
advertised role cells are new and distinct would enlarge the current
neighbourhood in three different deficiency-one components.  This is the
correct direct screening criterion.

The catalogue is not by itself a repair theorem.  Before accepting a collar,
one must still prove that after global embedding:

1. all three cells remain literal proper-prefix cells with the advertised
   masks;
2. the three cell identifiers are distinct and absent from the current
   187-cell neighbourhood;
3. no old neighbour in those or other components is destroyed;
4. the middle chronology and every upper target remain covered.

## Authentication and scope

The independent replay agrees exactly with the authenticated original Hall
record on all 347,875 incidences, the matching cardinality, the 25 unmatched
targets, all 212 left-shore masks, and all 187 neighbour cells.

The chronology itself contains every one of the 12,870 rank-eight owners,
with only the three forced repeated owners `4e71`, `cc63`, and `ce61`, and its
rank-eight interval word has no upper-rank hole.

This note proves only the exact common-compiler Hall obstruction for this
fixed chronology.  It neither constructs a simultaneous source-letter
assignment nor a literal universal length-12,873 OR word.
