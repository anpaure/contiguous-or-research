# Hostile audit of the thirteen-universal-port MSW common-history theorem

**Date:** 2026-08-14  
**Verdict:** **PASS after repair.**  The frozen theorem proves the claimed
zero-added-position fusion under the exact hypothesis
\(2m+1\ge13(d+1)\).  The audit rejects the earlier, broader reading that an
arbitrary `001` or `011` packet always moves at most five flip positions;
the repaired theorem uses only the residue-case-selected packets.

**Audited source:**
`MATH_THEOREM_THIRTEEN_UNIVERSAL_PORTS_CLOSE_MSW_COMMON_HISTORY_ARBORESCENCE_20260814.md`  
**Prerequisites:**
`MATH_THEOREM_MSW_HIGHEST_VALLEY_FOUR_PACKET_MONOTONE_CONNECTIVITY_20260813.md`
and
`MATH_THEOREM_COALESCED_MULTIINCIDENCE_COMMON_HISTORY_EULER_FUSION_20260814.md`.

## 1. Repair that was required

The packet table in the four-packet theorem has support sizes

\[
 4,\ 5,\ 5,\ 6
\]

only for the selected residue cases

\[
 (L,Q)=(0,0),\quad Q=0<L,\quad L=0<Q,\quad L,Q>0,
\]

respectively.  It is false to attach the five-position bound to every
`001` or `011` move independently of its residue case.  The source was
repaired to choose exactly those four case-selected parents.

The direct `0011` rail has one exception,
\((L,Q,O)=(d,d,d-1)\).  There \(m=3d+1\) and \(n=6d+3\), whereas the
present hypothesis gives \(n\ge13(d+1)\).  Since

\[
 6d+3<13(d+1)\qquad(d\ge1),
\]

the crossed exceptional construction is never invoked.  Every selected
edge in the theorem's range is a direct same-start edge with global support
at most six.

## 2. Canonical orientation and the \(\iota\) indexing

Let \(\rho_u,\rho_v\) be the two endpoint flip orders in their one fixed
global canonical orientations, and define the actual global old-position
map by

\[
 \rho_v(r)=\rho_u(\pi(r)).
\]

The canonical tight orders are \(w^u_j=\rho_u(2j)\) and
\(w^v_j=\rho_v(2j)\).  Multiplication by two is a bijection of
\(\mathbb Z_n\), with inverse \(\iota=2^{-1}\), because \(n\) is odd.
Consequently

\[
 w^v_j=\rho_u(\pi(2j))=w^u_{\iota(\pi(2j))}.
\]

Thus the nonfixed **source positions** are exactly

\[
 C_e=\iota(\operatorname{supp}(\pi-\mathrm{id})).
\]

This is not a mere cardinality comparison: it proves the source-index map
used by the bad-set test.  Avoiding \(C_e\) on
\([a,a+d-1]\) fixes every first-rail source position \(a+j\); avoiding
\(C_e-(s-1)\) fixes every second-rail source position
\(a+s-1+j\).  Therefore the same numerical source start \(a\), in the two
already-fixed canonical endpoint orientations, satisfies

\[
 F_j(u,a)=F_j(v,a)\qquad(0\le j<d).
\]

Lemma 2.1 of the packet theorem transports the local permutation to the
global roots only by dihedral conjugacy plus fixed positions.  This preserves
the support bound.  The conjugacy is already included in the actual global
\(\pi\) above; the construction never rotates or reflects either endpoint
after selecting a universal start.  Hence the same fixed starts
\(a_t=t(d+1)\) are genuine physical source starts in every canonical row.

## 3. Hitting and separated-port checks

For every edge,

\[
 \mathcal B_e=C_e\cup(C_e-(s-1)),\qquad
 |\mathcal B_e|\le 2|C_e|\le12.
\]

Under \(n\ge13(d+1)\), the thirteen blocks

\[
 I_t=[t(d+1),t(d+1)+d-1],\qquad0\le t\le12,
\]

are cyclically disjoint and consecutive blocks, including the last and
first, have start gap at least \(d+1\).  If all thirteen met
\(\mathcal B_e\), disjointness would require thirteen distinct bad points,
contradicting \(|\mathcal B_e|\le12\).  Therefore each edge has a direct
universal start.  At any row, distinct used starts have cyclic distance at
least \(d+1\), exactly the separated-port hypothesis.

## 4. Transitive history classes

Assign each edge one index \(t\) and use \(a_t\) at both endpoints.  An
edge equality therefore preserves \(t\).  A row coalesces only incidences
using the same physical start; the thirteen \(a_t\) are distinct modulo
\(n\), because \(0\le a_t\le12(d+1)<n\), so row coalescence also preserves
\(t\).  Hence \(t\) is invariant under the transitive closure defining a
history class.  No class can force equality between distinct starts.

At a row-start \((v,a_t)\), every incidence requests the identical forced
word \((F_j(v,a_t))_{j<d}\).  A direct edge identifies that word with the
same word at its other endpoint.  Thus the entire transitive history class
has one literal word, and the multiway union/intersection criterion holds
automatically.

This argument is stronger than checking pairwise common histories: it binds
the complete generated class required by the coalesced Euler theorem.

## 5. Arborescence and scope

The selected parent raises area strictly.  Repeated parents end at the
unique valley-free Dyck root, the mountain, so the selected edges form an
arborescence.  Sections 2--4 give one global orientation per row, one
jointly feasible word per history class, and separated distinct ports.
The coalesced Euler theorem therefore applies without adding source
positions and preserves the occurrence-labelled literal deck through width
\(d+1\).

The conclusion is limited to the owner ledger and strict-lower cells whose
source width is at most \(d\).  It does not produce or preserve proper-upper
intervals wider than \(d+1\), an upper actuator, a terminal opening cap, or
unrelated protected ticket banks.

## 6. Independent H100 replay

The audit verifier reconstructs canonical MSW flip and tight orders from
each Dyck root, chooses the leftmost-highest case-selected parent, computes
the global flip permutation \(\pi\), and independently computes the tight
old-position map.  For every tested edge it checks the exact identity

\[
 q_j=\iota(\pi(2j)),
\]

support at most six, bad-set size at most twelve, existence of a universal
port, and equality of both physical source rails at that same start in the
two canonical rows.

All compilation, execution, and hashing were performed on H100 (`arboghast`),
never on the local Mac.  Results:

| regime | scope | failures | \(\iota\)-index failures | max support | max bad set |
|---|---:|---:|---:|---:|---:|
| \((m,d)=(13,1)\) | all 742,899 parent edges | 0 | 0 | 6 | 11 |
| \((19,2)\) | first 4,999,999 parent edges | 0 | 0 | 6 | 12 |
| \((26,3)\) | first 4,999,999 parent edges | 0 | 0 | 6 | 12 |

The finite replay is corroboration only.  The PASS verdict rests on the
symbolic arguments in Sections 1--5.

## 7. Frozen artifacts

The exact SHA-256 digests are recorded below after the final H100 freeze.

| artifact | SHA-256 |
|---|---|
| theorem source | `fa14802d3974578f96ec673f3074c9c399ce6675ea8907a508573b1406762a30` |
| verifier source | `d329fe3e8b0edfc1f22ff463b9f0c7fb324b7bc05f6496ca5b3b764affb5f370` |
| verifier binary | `040d149485694f0c52f18fc4c70f297ebb7734edddcfcad7b6ad8855375ae3cb` |
| exhaustive \((13,1)\) output | `1f9b1e110589c7097c0c4e076679ebac18cdc2bb69766936a29bd2a91ea63d4d` |
| first-five-million \((19,2)\) output | `9789dba758c6b5c6840e54193c65cd0705fbc45f913a5733a1c314703871288c` |
| first-five-million \((26,3)\) output | `67650933ec0f5145ab59055b120b8572bdb77b4a26406c291945ae2579c36e9a` |

The audit file's own digest is reported externally, because inserting it in
this table would change the bytes being hashed.
