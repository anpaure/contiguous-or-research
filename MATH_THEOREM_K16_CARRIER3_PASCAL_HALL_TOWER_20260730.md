# K16 carrier-3: the Hall-22 shore is an exact Pascal compiler tower

Date: 2026-07-30  
Status: exact theorem for the authenticated carrier-3 chronology; constructive
diagnostic, not yet a K16 completion.

## 1. Frozen object

Let `Q` be the authoritative length-12,873 rank-eight chronology

```text
scratch/k16_authoritative_carrier3_hall22_20260730/
  authoritative_carrier3.targets
```

with SHA-256

```text
6d1f85644ed71212d29405d2595cb538e386cb8055632f0797fa5350b4b339e0.
```

Its generalized `COMP3` graph has 26,332 lower targets, 31,512 physical
proper-prefix cells, 350,892 incidences, and maximum matching 26,310.  The
canonical alternating Hall shore is

\[
    X\subseteq L,\qquad Y=N(X),\qquad |X|=519,\quad |Y|=497.
\]

Put \(z=2^{15}\).  The following exact structure was independently
reconstructed twice.

## 2. Pascal-tower theorem

For `s=5,6,7`, let

\[
 A_s=\{S\in X:|S|=s,\ z\notin S\}.
\]

Then

\[
 |A_5|=19,\qquad |A_6|=94,\qquad |A_7|=293,
\]

and the whole left shore is the disjoint union

\[
 X=A_5\ \sqcup\ (A_6\sqcup(z+A_5))\ \sqcup\
                  (A_7\sqcup(z+A_6)).                 \tag{2.1}
\]

Equivalently, deleting the top bit from the top-containing rank-six members
of `X` gives exactly `A5`, and deleting it from the top-containing rank-seven
members gives exactly `A6`.

The right shore has no other envelope ranks.  Its physical cells split as

| envelope palette | cell count | exact palette |
|---|---:|---|
| base rank 6 | 93 | \(A_6\setminus\{\mathtt{4c29}\}\) |
| top rank 6 | 19 | \(z+A_5\) |
| base rank 7 | 291 | \(A_7\setminus\{\mathtt{4879},\mathtt{4c39}\}\) |
| top rank 7 | 94 | \(z+A_6\) |

Each displayed envelope occurs on exactly one cell in `Y`.  Therefore

\[
 |X|-|Y|=
 \underbrace{|A_5|}_{19}+\underbrace{1}_{\mathtt{4c29}}+
 \underbrace{2}_{\mathtt{4879},\mathtt{4c39}}=22.       \tag{2.2}
\]

The two rank-seven exceptions have no candidate cell at all.  The rank-six
exception `4c29` has candidates only in rank-seven envelope cells.  Every
member of `A5` has candidates only in rank-six or rank-seven envelope cells.
Thus (2.2) is not merely a cardinality coincidence: adjoining one private
abstract diagonal cell for each of these 22 masks raises the shore matching
from 497 to 519, and no smaller diagonal augmentation can do so.

## 3. These are exactly lost K15 compiler deliveries

In the verified optimum `answers/k15.word`, every mask in the 22-element
diagonal has exactly one literal short occurrence.  Its widths are

```text
19 rank-five masks:  width 1;
4c29:                 width 2;
4879:                 width 1;
4c39:                 width 3.
```

The same 22 masks also each have exactly one short provider in the independent
repeat-free optimum `scratch/k15_repeatfree_parents_20260730/k15seed_5.word`
(there `4879` has width three).  For the canonical answer, the three exceptional
providers are located at

```text
4879  -> [0,1)
4c39  -> [5728,5731)
4c29  -> [5729,5731).
```

All nineteen singleton `A5` deliveries begin between positions 5747 and
6354.  These are precisely in the large parent block affected by the
carrier-3 rethread.  Hence carrier 3 has not developed diffuse lower Hall
damage: the even lift has shifted a unique K15 short-delivery diagonal one
rank upward, while its three seam exceptions have been deleted.

## 4. Constructive consequence

Repairing only the two zero-candidate masks is insufficient.  A Hall-zero
descendant must create at least 22 net exterior ports for the old shore (or
destroy/recombine the shore itself).  The exact target is now finite and
labelled:

1. restore the nineteen unique rank-five singleton-capable providers;
2. restore one rank-six provider for `4c29`;
3. restore rank-seven providers for `4879` and `4c39`;
4. preserve enough of the old 497-cell neighbourhood for all 519 targets to
   match.

This changes the search prescription.  The relevant operation is not a
sequence of independent root repairs.  It is a parent/rail rethread which
breaks the Pascal copy correlation, or a collar which transports the full
22-cell compiler diagonal.  This also explains why flat relocation alone
does not help: it changes scalar placement without recreating the missing
diagonal.

The theorem is scoped to carrier 3.  It proves neither that every even lift
has such a tower nor that `nu(16)>12873`.

## 5. Authentication

Primary replay:

```text
scratch/audit_k16_carrier3_pascal_hall_tower_20260730.py
  SHA f0974ae93b07aef7a0186b1c2565ab926b39ea84a3b8e5eaef384c1e689e6a6c
scratch/k16_carrier3_pascal_hall_tower_20260730.audit.json
  SHA 5c0dda1c914781a1eb88a269294913bb611c107793b577b78d4b81aa8a5a5efc
  payload 20c7c7c2c8143801283803236be8e910d333a4f82e6772b93437af239ad9594b
```

Independent provider replay:

```text
scratch/k16_authoritative_carrier3_hall22_20260730/
  authoritative_carrier3.pascal_tower.audit.json
  SHA 89a307f4f166f9d38b8cbcbf2e4edf742e22d5536a284fa42c1cca45d010e139
  payload 5f48b28a8f91c95f75d7a390e508e49249cd20a275edf5a32e2db3b7ef030b4a
  authoritative_carrier3.diagonal22_parent_providers.tsv
  SHA eceb571594ac753f2823facebf1ebc02c85b554229620e81a34dd9b514f939bc
```

Both audits return PASS.
