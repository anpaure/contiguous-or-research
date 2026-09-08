# K17 private-face static `B_5` planting and the pointwise-address no-go

**Date:** 2026-08-02  
**Status:** exact finite static planting and dimension-uniform address
obstruction.  No phase-common occurrence-labelled actuator bank, state
completion, supplier matching, chronology, residence, upper/source deck,
compiler, or contiguous-OR word is claimed.

## 1. Outcome and scope

The frozen-suffix census `C10=0` is not invariant under the newly proved
three-level common-basis recoupling.  Starting from the authenticated K17
compressed-normal private-H table, one can retain the complete **static
chain footprint** of all 1,748 selected private H tickets and recouple only
unprotected rows so that the resulting table contains the eight fixed
`(rank 7, rank 8)` suffix slots of one canonical

\[
       \text{saturated }B_5\ C_{10}
       \quad+\quad\text{its prescribed rooted opener }C_6.
\]

The eight old bottom-to-slot edges and the eight fixed suffix edges extend
to one full augmented perfect matching.  Replacing the old five- and
three-cycles by their alternate halves gives a second full augmented
perfect matching with the same exterior matching.  Both reconstruct exact
compressed-normal K17 tables with histogram

\[
                         (0,7395,16915).
\]

This closes the pure target/root common-basis prerequisite for **one changed
`C10+C6` shore** while keeping the protected private-H target chains fixed.
It does not prove that the other unchanged atoms of the 22-atom local
absorber occur with the required carrier topology, nor that any of the
eight slots has a common occurrence-labelled state.  Accordingly this note
does not call the object a protected or clone-good actuator.

There is also a sharp negative theorem.  A nonidentity bottom relay cannot
preserve the named co-middle address at a fixed physical suffix slot.  In
the planted `C10+C6` all eight co-middle addresses change pointwise, even
though the two co-middle **decks** agree.  Thus the requested protected
lift cannot require literal pointwise equality of a column which includes
that named address.  Its viable replacement is an explicitly declared
internal address transport/equivariance, followed by pointwise equality of
the exported exterior columns.

## 2. The augmented common-basis matching

Put

\[
 L=\bigcup_{j=1}^6{[17]\choose j},\qquad
 M={[17]\choose7},\qquad R={[17]\choose8}.
\]

Use the augmented bipartite graph

\[
 \mathcal G^+=(L\mathbin{\dot\cup}M\mathbin{\dot\cup}\Delta,
               M\mathbin{\dot\cup}R),\qquad |\Delta|=2533,
\]

with all strict containment edges from `L` to `M union R`, all containment
edges from `M` to `R`, and every dummy adjacent to every right copy of `M`.
Perfect matchings of this graph are exactly labelled-dummy
compressed-normal tables.

The incumbent is

```text
scratch/k17_phase0_retained_witness_private_basis_20260802/
  private_h_outer_materialized.tsv
```

and the selected private bank is

```text
scratch/k17_phase0_retained_witness_private_basis_20260802/
  selected_tickets.tsv
```

For each of the 1,748 selected H-short hosts, freeze its dummy-to-middle and
middle-to-root edges.  For each of the 3,496 pairwise distinct endpoint
hosts, freeze its low-to-middle and middle-to-root edges.  The short and
endpoint host shores are disjoint, so this is a 10,488-edge partial
matching.  Freezing these edges fixes all 5,244 protected target chains at
their original physical roots.  It proves preservation only of their
static chain footprint; occurrence state and the supplier row are separate.

## 3. Canonical planted shore

Use coordinates `0,...,16`.  Let

\[
 C=\{0,1,2,3\},\quad K=(4,5,6,7,8),\quad
 (a,b,c,q)=(14,9,16,0).
\]

For indices modulo five, the `C10` slots are

\[
\begin{aligned}
 B_i&=C+a+k_i,\\
 B_i'&=C+a+k_{i+2},\\
 M_i&=C+a+k_i+k_{i+2},\\
 U_i&=C+a+k_i+k_{i+1}+k_{i+2}.
\end{aligned}                                                    \tag{3.1}
\]

Thus the two bottom phases are `B_i -> M_i` and `B_i' -> M_i`, while every
suffix edge `M_i -> U_i` is fixed.

For the rooted opener put

\[
 X=\{k_0,k_2\},\qquad L_0=C+X,\qquad S=L_0-q.
\]

Its old and new bottom triples are

\[
 (L_0,S+b,S+c),\qquad(S+b,S+c,L_0),                 \tag{3.2}
\]

on the three fixed middle/root slots

\[
\begin{array}{c|cc}
 &M&U\\ \hline
0&L_0+b&L_0+a+b\\
1&S+b+c&S+a+b+c\\
2&L_0+c&L_0+a+c.
\end{array}                                                    \tag{3.3}
\]

All eight bottom masks, eight middle masks, and eight root masks are
separately distinct.  They avoid every left and right endpoint of the
10,488 protected edges.  The audit additionally checks every old/new
co-middle.  None of the changed lower, fixed-middle, co-middle, or upper
targets occurs in any of the 5,244 protected target chains.

### Theorem 3.1 (exact static extension)

The sixteen old edges in (3.1)--(3.3) extend the protected partial matching
to a perfect matching of all `43,758` vertices on each shore of
`G+`.  The alternate `C10` and `C6` halves extend with the identical
exterior matching.

#### Proof

Start with the authenticated incumbent perfect matching.  Insert each of
the eight fixed suffix edges and then each of the eight old bottom edges.
For a desired edge `lr`, delete the incumbent edges at `l` and `r`, insert
`lr`, and search the residual alternating graph from the newly unmatched
left vertex to the newly free right vertex, forbidding every previously
frozen edge.  Such a path is necessary and sufficient for the insertion:
its symmetric difference repairs the perfect matching, while the symmetric
difference of any repaired matching with the incumbent supplies such a
path.

The exhaustive searches have lengths

```text
2,2,3,3,3,4,3,4,1,1,2,0,3,1,3,2
```

and hence all sixteen insertions succeed; the maximum path length is four.
The final old matching changes 45 augmented-left edges from the incumbent.
The program then deletes the eight old bottom edges and inserts the two
cyclic alternate halves on exactly the same local shores.  This is a
perfect matching without another search and changes 46 augmented-left
edges from the incumbent.

The verifier checks every matching edge directly against containment (or
the dummy rule), both right and left degrees, the protected pins, all local
identities, and the reconstructed chain census.  The deterministic matching
fingerprints are

```text
old  0x810d245638a6b75e
new  0x61135fb9e74b3336.
```

This proves the theorem.  \(\square\)

### Corollary 3.2 (the frozen `C10=0` obstruction is face-local)

The current bottom-relocation fibre has no saturated `C10`, but the
compressed-normal common-basis face containing the same protected private-H
static chains has a table with the prescribed saturated `C10` suffix shore.
Therefore a suffix/root recoupling is genuinely sufficient to escape that
particular zero; the zero cannot be used as a cut on the full common-basis
face.

This corollary is only about suffix geometry.  It says nothing about
clone signatures or state compatibility.

## 4. Pointwise co-middle obstruction

For a fixed consecutive suffix `M subset U`, write `h=U-M`.  A legal
rank-one-lower bottom `B subset M` induces

\[
                         \chi(B;M,U)=B+h.            \tag{4.1}
\]

### Theorem 4.1 (pointwise named-address no-go)

If `B` and `B'` are distinct legal bottoms for the same fixed suffix, then

\[
                      \chi(B;M,U)\ne\chi(B';M,U).   \tag{4.2}
\]

Consequently every moved slot of a nonidentity bottom circuit changes its
named co-middle address pointwise.  A saturated `C10` changes five of five;
a hub/rooted `C6` changes three of three.  The planted composite changes
eight of eight.

#### Proof

The unique point `h` lies outside `M`.  Intersecting (4.1) with `M` recovers
`B`.  Hence the map `B -> B+h` is injective.  Every slot of either cyclic
phase receives a different bottom in the alternate phase, proving all
counts.  \(\square\)

Thus any protected column containing the pair

\[
                  (\text{physical slot},\text{named }\chi)
\]

cannot be literally pointwise mode-invariant.  This does not refute a
protected lift whose internal occurrences are transported by a fixed
bijection, nor a consumer proved invariant under that transport.  It does
refute silently treating deck equality as occurrencewise address equality.

## 5. Exact remaining gate

The following are **PROVED** here.

1. One canonical `C10` plus its prescribed rooted `C6` changed shore is
   compatible with an exact compressed-normal K17 common-basis table.
2. The same construction retains all 5,244 target chains in the selected
   phase-zero private-H bank.
3. The two local bottom modes use one common exterior augmented matching.
4. The fixed-suffix `C10=0` census does not extend to the full common-basis
   face.
5. Literal pointwise preservation of a named co-middle address is
   impossible for every nonidentity bottom relay.

The following are **UNPROVED**.

1. That the unchanged atoms needed by the complete 22-atom one-socket
   topology have compatible occurrence-labelled carrier roles on this
   recoupled table.
2. Any common phase-zero/phase-one state DNF on the eight planted slots.
3. Equality, or a proved equivariant transport, of the actual address,
   aggregate-history, reset, residence, upper/source, and compiler columns.
4. Clone-good `C10` signatures for the planted five slots.
5. The rooted same-signature `C6` condition for the prescribed opener,
   and Hall for several opener targets.
6. Preservation or recovery of the selected-state supplier rank after the
   45/46-edge recoupling.
7. A disjoint extensive bank, its bounded relay-chain cover, one chronology,
   or a K17 word.

The weakest exact next test is therefore no longer static common-basis
extension.  It is to regenerate the complete two-phase occurrence columns
of this explicit 45-edge recoupling and test one fixed internal address
transport.  If that transport is selected first, common exterior allocation
is an ordinary paired-shore Hall test; marginal per-phase positivity is not
sufficient.

## 6. Audit binding

```text
scratch/audit_k17_common_basis_open_b5_planting_20260802.cpp
  SHA-256 db19d6e4a3df41bf28d5fd22cd862720fbf1b06fb9de172e077d27b5adb362af

scratch/k17_common_basis_open_b5_planting_20260802.certificate.tsv
  SHA-256 ef82da94af2508df3806b5ea833db96e5e07ee09addc453a2680fcc041eda4c6

scratch/k17_common_basis_open_b5_planting_20260802.audit.txt
  SHA-256 c03e49be5cb3da67ae6debd3e28407279f3c50cdd73ff68850e43b414f6c1bf8

private_h_outer_materialized.tsv
  SHA-256 b268d1248e53d164d87bc83cf69fbd5ebd412451ac9e4a4313408167f1e637dc

selected_tickets.tsv
  SHA-256 d02e01d0e56beec82633b280bf9011760c273a31994431bd62db52c3662d0ef1
```

The existing independent local audits were rerun unchanged:

```text
PASS mode-transparent B5 carry audit ... hall_erosion_cases=334575
PASS B5 cross-core exterior relay ... carried_P2=1 chains=210
PASS frozen K17 suffix census ... raw_saturated_B5_C10_sockets=0
```

The first two independently recheck the B5 relay/interface algebra; the
third is consistent with Corollary 3.2 because it scans only the unchanged
suffix fibre.
