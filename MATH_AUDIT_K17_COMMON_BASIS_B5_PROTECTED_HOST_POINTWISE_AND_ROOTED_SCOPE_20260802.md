# Audit: K17 common-basis `B_5` host, pointwise scope, and rooted gate

**Date:** 2026-08-02  
**Status:** PASS for one complete static 22-atom module on a
compressed-normal common-basis host, with all four resource decks disjoint
from the 5,244 frozen private-ticket rows.  Protected clone signatures,
common-phase occurrence witnesses, endpoint aperture, rooted same-signature
Hall, supplier Hall, and every global chronology row remain **UNPROVED**.

## 1. Corrected verdict

The tail-filtered artifact

```text
scratch/k17_common_basis_b5_protected_host_20260802/
  constructed_common_basis_b5_host.tsv
```

contains one literal incumbent old phase of the complete 22-atom
one-socket module

\[
        5C_4+2K_2\longrightarrow C_{20}+2K_2
                    \longrightarrow P_{22}+P_2.       \tag{1.1}
\]

The table is compressed-normal with histogram `(0,7395,16915)`, its
common-basis shores have sizes

\[
              (|C_M|,|C_R|,|B|)=(16915,4862,19448),   \tag{1.2}
\]

and every one of the 5,244 physical short/predecessor/successor rows in the
selected private-H bank is byte-for-byte unchanged from the incumbent.
The alternate local phase changes exactly eight physical root rows and is
another exact compressed-normal table on the identical common-basis and
root/owner skeleton.

The full four-resource replay is load-bearing.  For each atom written as

\[
                  (L,U,T,H),                         \tag{1.3}
\]

both modes have 22 distinct entries in each of the lower, upper, tail, and
head rows; their four resource decks agree; and

\[
                  T=L\cup(U-H)                       \tag{1.4}
\]

holds atomwise.  None of the four resource decks meets any target occurring
in a frozen private-ticket row.

This last sentence is a correction to an intermediate certificate.  The
pre-filter host of SHA `b3aa8b7a...` froze the 5,244 target chains but used
tail mask `44169`, the middle target of protected predecessor row `8907`,
inside a changed opener atom.  The old/new atoms were

```text
(35977,44201,44169,36009)
(35977,48265,44169,40073).
```

Thus row freezing alone did not imply protected-resource disjointness.  The
constructor was repaired to reject a candidate whenever **any** of
`low/up/tail/head` occurs in a frozen row.  The final tail-filtered host has
zero such overlaps.

## 2. Independent static replay

The independent verifier does not run or import the constructor.  It reads
the emitted table and audit coordinates, reconstructs both 22-atom modes,
and checks:

1. all 65,535 nonempty rank-at-most-eight targets occur exactly once;
2. both representing matchings and the common-basis shore sizes (1.2);
3. exact equality of all 5,244 frozen target rows in both modes;
4. all 22 old atoms occur literally as `L-H-U` chains at their physical
   roots;
5. replacing the eight changed atoms by the alternate phase gives another
   exact table;
6. the four resource-deck identities and zero protected-resource overlap;
7. old topology `5C4+2K2` and new topology `P22+P2`; and
8. the same static root skeleton is legal under both authenticated s7 owner
   maps.

The topology component profiles are exactly

```text
old: (4,4) x 5, (2,1) x 2
new: (22,21), (2,1),
```

where each pair is `(vertices,edges)`.  The 4-vertex components are cycles
and the two new components are paths.

This proves a **single static protected-resource-clean module**, not an
extensive bank and not an occurrence-labelled module.

## 3. Exact pointwise ledger

Index old and new atoms by their common physical upper/root target.  On the
eight changed rows the exact field comparison is

\[
\begin{array}{c|rrrr}
 &L&T&H&U\\ \hline
\text{number changed pointwise}&8&8&0&0.
\end{array}                                             \tag{3.1}
\]

Thus the construction does preserve every fixed `(head,upper)` suffix
occurrence pointwise, as required by its bottom-relay interpretation.  It
does **not** preserve the named lower or co-middle/tail address at any moved
slot.  Their decks agree only after transport.

### Proposition 3.1 (pointwise-address obstruction)

For any fixed consecutive suffix `H subset U`, put `h=U-H`.  The co-middle
induced by a legal bottom `L` is

\[
                         \chi(L)=L+h.                \tag{3.2}
\]

The map `L -> chi(L)` is injective, because `chi(L) intersect H=L`.
Consequently every slot whose bottom changes also changes its named
co-middle pointwise.  In particular, a nonidentity saturated `C10` changes
five of five such addresses and its opener `C6` changes three of three.

Hence a protected theorem cannot identify four-row deck equality with
pointwise address equality.  It must either:

* declare the lower/tail occurrences internal and supply an explicit
  transport under which every exterior consumer is equivariant; or
* prove that the relevant exported column ignores those names.

Neither assertion is represented in the current artifact.

## 4. A concrete two-phase slot sub-signature

For a physical root slot `v` and owner phase `epsilon`, let

\[
       \omega_\epsilon(v)=T_\epsilon(v)-U(v)          \tag{4.1}
\]

be its one-point owner increment.  This is an exactly available
slot-inherited sub-signature; it is not asserted to be the full protected
signature.

On the five `C10` slots, the ordered phase pairs are

```text
(14,14), (9,9), (5,10), (15,14), (9,12).
```

On the three rooted-opener slots they are

```text
(14,14), (4,4), (14,14).
```

Neither list is constant on its slot cycle.  Therefore, **if** the complete
exported receiver column retains the literal owner-increment pair, the
cyclewise clone condition of the mode-transparent theorem fails for this
module.  This is a conditional obstruction, not a claim that (4.1) alone is
the actual protected signature.  A proof may instead supply a transported
owner/address interface, but it must state and verify that transport.

## 5. Rooted `C6` scope

The local module contains the structural opener through its prescribed
target edge, with the single uncoloured third-coordinate witness `c=6`.
For this one-target uncoloured family, the rooted Hall condition is
tautologically satisfied.

This does **not** prove the required protected statement.  No artifact here
assigns signatures to the three opener slots or proves that the third
coordinate has the same protected signature as the target edge.  No
endpoint-aperture occurrence, common state DNF, or simultaneous Hall family
for several opener targets is represented.  Accordingly the following are
all **UNPROVED**:

1. clone-goodness of the five `C10` slots;
2. protected rooted-`C6` positivity for the named opener;
3. protected rooted Hall for two or more openers;
4. pointwise address/history/reset/residence/upper/source/compiler equality;
5. selected-state supplier Hall after the 150 matching-edge recoupling;
6. a disjoint extensive module bank and its bounded relay-chain cover; and
7. a common chronology or K17 word.

The weakest next finite task is to generate, on this exact 22-row module and
its recoupled ambient table, the complete two-phase occurrence columns for
the eight changed slots.  The accept condition must name one internal
low/tail transport and then compare every exterior column pointwise.  A
positive marginal socket count in each phase is insufficient.

## 6. Frozen evidence

```text
constructor
  scratch/search_k17_common_basis_b5_protected_host_20260802.cpp
  SHA-256 6911987e0792dce0d087a462c87e9d8a784e6bf742d6a713eca529fa3156b7ca

constructed host
  scratch/k17_common_basis_b5_protected_host_20260802/
    constructed_common_basis_b5_host.tsv
  SHA-256 d00a9138e211c49071c5a8848d433850764461a5d8e3bc8e8c359840e6bec78f

producer audit
  scratch/k17_common_basis_b5_protected_host_20260802/audit.json
  SHA-256 5a346b04933da36932cc3f708e1db437879bd2433e6e1242bade8136f17212dd

independent verifier with the all-four-row and pointwise checks
  scratch/audit_k17_common_basis_b5_protected_host_independent_20260802.py
  SHA-256 949fe40089f2c5362caa5297b942de0ab17b254caec3925063b1aabad7674b3e
```

The authenticated phase-table inputs used by the independent replay are
`ac52c0f1...` and `736fc30c...`; the incumbent and ticket inputs are
`b268d124...` and `d02e01d0...`.  No external computation was used for this
independent audit.
