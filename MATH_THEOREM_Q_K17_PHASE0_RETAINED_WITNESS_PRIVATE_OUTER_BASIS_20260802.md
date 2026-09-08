# Q theorem: a 1,748-ticket private retained-witness bank with exact outer extension

**Date:** 2026-08-02  
**Status:** exact finite positive theorem on the authenticated phase-0
retained-witness subbank, with an independent canonical physical `P1--P2`
five-cell replay of every selected ticket.  The selected short bank is a basis of
`M_short`, all requested predecessor/successor/host/token privacy rows hold
in a stronger pairwise-disjoint form, and every forced real-bottom edge
extends to a complete outer matching.  This is **not** a chronology,
reset/common-cap, residence, upper-deck, compiler, or K17-word certificate.

## 1. Frozen inputs

The authenticated origin table and phase-0 retained witness file are

```text
original.res1972.tsv
  SHA-256 db960ce5b51e0fdea7b048d35d48ca737096b16ee73a20df873beb0517e5f185
slot_witness.tsv
  SHA-256 1d78ed8411612c99cb7d9d92dfe4c0dfa84c7f71dc1a8f3afb58e31eb5d7dbfb
```

The witness file has `33,261` records.  It is the summary output of the
complete phase-0 local socket enumeration: for each positive short slot it
retains one exact literal record for every realized `(q,alpha,beta)` mode.
It supports `10,167` of the `18,646` eligible hard slots.  The other `8,479`
have zero local degree in the complete local enumeration.

A retained record is

\[
       g=(s,q,\alpha,\beta,p,u_p,h,u_h),                       \tag{1.1}
\]

where `s` is the short row, `p` and `h` are predecessor-tail and
successor-head hosts, and `u_p,u_h` are their real bottom tokens.  Token
`-1` denotes one of the 17 fixed soft-long rows.

The summary retention is important for negative scope: absence from this
file is not absence from the complete occurrence-labelled ticket bank.
Every record which *is* retained is nevertheless a replayed positive local
witness, so a positive construction using only retained records is valid on
its stated resource face.

## 2. The requested private compatibility system

For a selected ticket set `X`, impose:

1. short rows are distinct;
2. predecessor hosts are distinct;
3. successor hosts are distinct;
4. a physical host has one bottom-token assignment;
5. different physical hard hosts use different real bottom tokens;
6. no selected short row is used as a selected long host.

The certificate below satisfies the stronger condition

\[
 \{p(g):g\in X\}\cap\{h(g):g\in X\}=\varnothing,              \tag{2.1}
\]

and all `2|X|` long hosts are pairwise distinct.  Therefore cross-side
host-state equality is vacuous: no physical long host is shared by two
selected records.  Each short also has its own physical address bank.

This is a private packing for exactly the resources named above.  It is not
being silently promoted to privacy of any exterior chronology, cap, reset,
or upper-witness resource not represented in (1.1).

## 3. Exact positive theorem

### Theorem 3.1

The retained phase-0 witness bank contains a set `X` of `1,748` tickets
with the following exact census:

\[
\begin{array}{c|r}
\text{resource}&\text{distinct count}\\ \hline
\text{short rows}&1748\\
\text{predecessor hosts}&1748\\
\text{successor hosts}&1748\\
\text{long hosts across both sides}&3496\\
\text{movable real bottom tokens}&3495\\
\text{fixed soft-long endpoints}&1.
\end{array}                                                   \tag{3.1}
\]

The short and long host sets are disjoint.  Every real bottom token in
(3.1) is distinct and legally contained in its prescribed host.  Moreover,
all `3,495` forced host--token edges extend simultaneously to a matching of
all `18,646` real bottom tokens onto

\[
          1,748\text{ mandatory free receivers}
          \;\dot\cup\;
          16,898\text{ nonshort hard receivers}.              \tag{3.2}
\]

Consequently the `1,748` selected short slots form a basis of the
cotransversal outer matroid `M_short`, and the retained-witness private
face has common outer/socket cardinality exactly `1,748`.

#### Proof

The selected ticket list is the frozen file

```text
scratch/k17_phase0_retained_witness_private_basis_20260802/
  selected_tickets.tsv
SHA-256 d02e01d0e56beec82633b280bf9011760c273a31994431bd62db52c3662d0ef1
```

An independent verifier first parses all `33,261` retained input records
and checks that every selected row occurs literally in that input.  It then
checks all six compatibility rows and the stronger global long-host
disjointness (2.1), giving the census (3.1).

The complete outer matching certificate is

```text
complete_outer_matching.tsv
SHA-256 179270d1d01f6c14a7b47b5eb390e634aca33ac16e5ec82d54a93b589b8d850e
```

The verifier checks every one of its `18,646` real-token rows directly
against the Boolean containment relation in the origin table.  It checks
that every real token is used once, every free receiver is occupied once,
exactly the complement of the selected short bank among hard receivers is
occupied, and every prescribed movable ticket edge occurs in the matching.
Thus (3.2) is a literal matching certificate.

By the short-set dual theorem, a `1,748`-set is a basis of `M_short` exactly
when its hard-slot complement together with all free receivers is matched
by the real tokens.  The displayed certificate proves precisely that
condition.  Since `r(M_short)=1748`, no common outer/socket set can be
larger on this outer face. \(\square\)

### Corollary 3.2 (zero private-face deficiency)

The global admissible-bank result was not merely a marginal Hall positive.
On the retained witness subbank, after enforcing all resource rows listed in
Section 2 and the actual real-bottom extension, the target deficiency is

\[
                              1748-|X|=0.                      \tag{3.3}
\]

This removes the static private-ticket/outer-matching gate for phase 0.

## 4. Search formulation and independent replay

The search used one binary choice per retained witness and the set-packing
rows in Section 2.  It deliberately imposed the stronger global
predecessor/successor-host disjointness.  After reaching `1,748`, it fixed
all prescribed real host--token edges and solved the residual exact
containment matching.  The first deterministic seed already gave

```text
private tickets          1748 / 1748
forced movable edges     3495
residual matching       15151 / 15151
```

The search heuristic is not proof-bearing.  The selected TSV and the
separately implemented verifier are.

Frozen artifacts:

```text
search source
  28aa0b08b7d78c0208f1b68659086c78b12a0f658dae03b00acda95c56663f76
independent verifier source
  16868a9a716933cc14b723ac3e94c07ec636bad9f8dd1b47332aee9eca7ccdd8
independent audit JSON
  dfaa7a5682861945f2de680076e86ce70fac2be5f35b3fe9783916c3903eec92
```

The independent replay reports

```text
PASS_K17_PHASE0_RETAINED_WITNESS_PRIVATE_BASIS_INDEPENDENT
selected=1748 long_hosts=3496 forced_real=3495 soft=1
```

## 5. Canonical physical P1--P2 replay and exact reset boundary

The retained menu was generated in the nine-address relaxation, so a
separate physical replay is necessary.  The nine strict interval pairs are
enumerated in the order induced by

```text
1, 2, 4, 12, 23, 123
```

on the three source positions.  In that enumeration,

```text
q=7 : inner 12, outer 123
q=8 : inner 23, outer 123.
```

These are exactly the two canonical physical `P1--P2` addresses for a
rank-seven-to-rank-eight short row.  In the first, cells 1 and 2 have union
the rank-seven target and cell 3 contains the one-element outer difference;
in the second the analogous statements hold for cells 2,3 and cell 1.

### Theorem 5.1 (every selected ticket is physically canonical)

Every one of the `1,748` selected tickets has `q in {7,8}` and passes the
literal canonical physical five-cell equations.  Their address and flag
histogram is

\[
\begin{array}{c|c|c|r}
q&\alpha&\beta&\text{count}\\ \hline
7&0&0&424\\
7&1&0&498\\
7&1&1&443\\
8&2&2&150\\
8&3&2&104\\
8&3&3&129.
\end{array}                                                   \tag{5.1}
\]

Thus `q=7` occurs `1,365` times and `q=8` occurs `383` times.

#### Proof

For `q=7`, the relaxed equations say that the first two short cells are
subsets of `L`, have union exactly `L`, and all three short cells have union
`U`.  Since the first two cells are contained in `L`, the outside cell must
contain `U-L`.  This is exactly the canonical physical first address.  The
same argument with the order reversed proves equivalence for `q=8`.

The independent verifier reconstructs the predecessor long family, the
short physical family and the successor long family from the frozen table,
including both owner-increment cells.  It builds five nonempty literal
cells and replays all envelope and exact-cover equations for all `1,748`
rows.  Every row passes. \(\square\)

Frozen physical replay:

```text
verify_k17_phase0_private_bank_physical_p1p2_20260802.cpp
  SHA-256 7947c32afc8609cd4da7de9759f79cd3aaf1c15b8d629f407a66971add5d9287
physical_cells.tsv
  SHA-256 465d8813600ffc12ba3383a86f7cddf07dcaa6cc7af19d23172825a0a8247062
physical.audit.json
  SHA-256 1dd0d9d1c4e6a9690bc84bf00b0bd938403335c5ec659cde7a1acca814389b48
```

This strengthens “relaxed-nine retained witness” to **canonical physical
local socket** for the selected bank.

### Corollary 5.2 (exact threshold-reset vector)

Order the four long flags as

\[
      0=12/1<1=12/2<2=23/2<3=23/3.                \tag{5.2}
\]

A socket from predecessor flag `alpha` to successor flag `beta` crosses
threshold `t` downward exactly when

\[
                          \beta\le t<\alpha.                    \tag{5.3}
\]

Equation (5.1) therefore gives the exact downward vector

\[
\boxed{R=(R_0,R_1,R_2)=(498,0,104).}                           \tag{5.4}
\]

The predecessor/out and successor/in flag counts are respectively

\[
 A=(424,941,150,233),\qquad B=(922,443,254,129).                \tag{5.5}
\]

Suppose these sockets are completed to a directed cycle cover and every
remaining long--long arc is nondecreasing in (5.2), as required by the
physical long-state theorem.  Conservation across each flag cut forces its
upward long-arc load to equal (5.4).  Since the middle-threshold load is
zero, no selected long arc may cross `1|2`.  Hence the only nonneutral
long--long arcs are necessarily

\[
             498\text{ arcs }0\to1,
             \qquad104\text{ arcs }2\to3.                     \tag{5.6}
\]

If `n_i` is the final number of long roles assigned flag `i`, the complete
direct-arc count matrix is forced to be

\[
\begin{array}{c|rrrr}
 &0&1&2&3\\ \hline
0&n_0-922&498&0&0\\
1&0&n_1-941&0&0\\
2&0&0&n_2-254&104\\
3&0&0&0&n_3-233.
\end{array}                                                   \tag{5.7}

In particular scalar feasibility needs

\[
                n\ge(922,941,254,233).                         \tag{5.8}
\]

The selected private endpoints themselves already force at least

\[
                     A+B=(1346,1384,404,362),                  \tag{5.9}
\]

so there is no flag-population shortage.  What remains is the exact
physical matching of the direct arcs in (5.6)--(5.7), not another scalar
reset inequality.

## 6. Coordinate-normalized motif census

For each ticket, form the ordered eleven-set tuple

```text
pred bottom, middle, root, owner;
short inner, root, owner;
succ bottom, middle, root, owner.
```

Counting the 17 coordinate membership words is a complete orbit invariant
for this ordered tuple under coordinate relabelling.  The same construction
on the five emitted physical cells gives a physical-word orbit invariant.

The exact census is:

```text
q/flag classes                                      6
semantic eleven-set coordinate orbits              72
physical five-cell coordinate orbits               47
six basic intersection-profile classes             18
owner-marker relation classes                       1
```

All `1,748` tickets have the same owner-marker relation: the short
owner-drop, predecessor-root drop and successor-owner addition are three
distinct coordinates.  Thus the bank has a clean uniform three-marker
skeleton; variation is confined to a finite intersection/membership atlas.

The atlas is fairly concentrated but not a single orbit.  The six largest
semantic orbits cover `1,037/1,748` tickets and the twenty largest cover
`1,560/1,748`.  For physical words the corresponding figures are
`1,177/1,748` and `1,678/1,748`.

Frozen census:

```text
analyze_k17_phase0_private_bank_motifs_20260802.cpp
  SHA-256 265305d6681f5bfe14dc8c5519071f368d803b9cc3253c6fb6a9da16d7226e75
motif_groups.tsv
  SHA-256 b7059824779d57afad18263ff498ed433192321f8f5b785cfd09838bbaa26bee
motif.audit.json
  SHA-256 617562d1b56675c5fdf9fe7bbca02a7de22b5ad0de2e0373cb19a8aa46373321
```

This is evidence for a finite motif construction, not yet an all-k orbit
rule.  A uniform theorem must show that enough copies of the required motif
classes can be planted with the direct reset arcs (5.6).

## 7. Exact scope after this positive

Proved:

- a full-rank private compatible ticket selection inside the retained
  phase-0 summary bank;
- pairwise-disjoint short, predecessor, successor, and bottom-token
  resources, in a stronger form than requested;
- an exact outer bottom matching containing all selected ticket edges;
- hence a common `M_short` basis and zero deficiency on this declared
  private resource face.

Not proved:

- that these isolated private socket paths extend to the required directed
  chronology or canonical cycle cover;
- reset balance, exterior histories, common-cap compatibility, residence,
  arbitrary-width upper coverage, the full compiler, or a word;
- any no-go from the summary bank.  Only one witness per
  `(q,alpha,beta)` was retained, so failure of a different restricted
  search would remain subbank-only.

The next exact gate is no longer selection of 1,748 locally private sockets
or their bottom-table extension.  It is **global directed-history/reset
completion around this frozen private basis**, followed by the independent
residence/upper/compiler rows.

## 8. Marker58 portfolio disposition

The separate exact directed-history CNF

```text
marker58_directed_history_v537.cnf
SHA-256 be93c2b1b8af993c0e5ecab17f32880e2564c9481aa2a2b1d0a660789b77691c
```

was run for four hours in each of four lanes: Kissat seeds `101,202,303`
on cores `24,25,26`, and CaDiCaL seed `404` on core `27`.  All four ended
with timeout exit `124`; none printed a SAT or UNSAT line.  Their exact
status is therefore

\[
                           \boxed{\text{UNKNOWN}}.             \tag{6.1}
\]

This is no evidence for or against marker58 feasibility.  The frozen
machine-readable disposition is

```text
scratch/k17_phase0_retained_witness_private_basis_20260802/
  marker58_portfolio_timeout.audit.json
SHA-256 0bb1b2b4a87d050edfd649bb136a63d9ebcc03e86232d8d48bd7cf92f22045ca
```

## 9. Exact reset-monotone motif-substitution census

The selected bank has `47` projected physical-word orbits, but a physical
word projection omits the endpoint root/owner boundary.  After adjoining
the ordered eleven boundary sets to the five deterministic physical cells,
the bank has `72` complete coordinate orbits.  These complete motifs do
**not** form a reusable local atlas for the remaining immutable short roles
of this frozen outer table.

Materialize the complete outer bottom matching from Section 4.  For each of
the `3,899` fixed `P2` roles and `1,748` free roles, enumerate every exact
canonical five-cell socket with nonincreasing/reset-admissible flags
`beta <= alpha` whose predecessor and successor hosts avoid all `3,496`
long hosts already frozen by the private `H` bank.  Classify a socket by

```text
(short address, predecessor flag, successor flag,
 coordinate-membership census of the ordered sixteen-set tuple:
 eleven boundary sets plus five physical cells).
```

The coordinate-membership census is a complete invariant under permutation
of the seventeen coordinates.  Therefore one class is exactly one complete
boundary-plus-word motif orbit, not merely a coarse statistic.  For
comparison the audit also records the `72` boundary-only and `47`
physical-word-only projections.

The exact marginal census is

```text
immutable short roles                                      5,647
roles with any reset-monotone physical socket                884
roles with endpoints private from the frozen H bank          653
roles hit by the existing 72 complete motifs                  41
roles hit by the 47 physical-word projections                 42

frozen round47 zero roles                                  4,688
zero roles with a private-endpoint socket                     302
zero roles hit by the existing 72 complete motifs              21
zero roles hit by the 47 physical-word projections             22
candidate complete coordinate-normalized signatures           532
```

There is also a free rank obstruction.  Every orbit in the existing atlas
is a `P1--P2` socket with rank-seven inner target.  Coordinate relabelling
preserves rank, so these orbits can never cover a free role or a fixed role
of rank four, five or six.

Treating all existing complete motif orbits as zero-cost sets, the exact
complete-signature set-cover optima are

```text
universe                                      free-covered  residual  new orbits
all 653 marginally private-coverable roles              41       612         350
302 private-coverable frozen-zero roles                  21       281         203
```

The first incidence graph splits into `306` connected components, with
largest role shore `22`; the second splits into `197`, with largest role
shore `10`.  Exhaustive branch-and-bound visits only `323` and `198` nodes,
respectively.  An independent verifier supplies disjoint-role packings of
sizes `350` and `203`: no candidate orbit covers two roles in the relevant
packing.  These packings give matching lower bounds for the displayed
covers, so the minima are certified without trusting the optimizer.

This is a negative reuse result on the reset-monotone face, not a physical
packing no-go.  It says that even the roles which individually admit
fresh-endpoint reset sockets would require hundreds of new complete motif
orbits.  It does not test whether those marginal sockets can be selected
simultaneously, and the `4,994` roles outside the private-coverable universe
may still require upward flag changes, endpoint rethreading or a new outer
table.  If the reset inequality is dropped, the broader all-flag socket
universe is larger; it is not the object certified here.

The `frozen_zero` label is bound to the round47 reset catalogue

```text
/home/amodo/or15/work/ad_v5r_res1921_1s_rots_019fc04bf4d7_20260802/
  out/round047_calibration/short_reset_triples.tsv
SHA-256 381a29b7d83dec652ac0da7bf63f7ae9b5bdb515ab325ac66ffe2d1409ea1e97
```

and is not recomputed from the newly materialized outer matching.

Frozen artifacts:

```text
analyze_k17_phase0_private_motif_substitution_20260802.cpp
  SHA-256 5612bb700f26eb0f310762d86cab2f7faad1ccfc7a08b5a44933afdd60f4d742
motif_substitution_roles.tsv
  SHA-256 1ebde64c5becd8e72024f12e08e2984ac71003a99f893f14bcfaff9322c49519
motif_substitution_signatures.tsv
  SHA-256 034ad3ca4d2c9ecb80a52fc974f99401a0bdeea8dcaa2a539df7591d2cb686b3
motif_substitution.audit.json
  SHA-256 fca1044829bec7b8f1ffab1aa24293e4b05d67836342ae95e28cbeb892bdb063
solve_k17_phase0_motif_signature_cover_20260802.cpp
  SHA-256 396db3c0f0245c9c93610b241505bda5c0a5321db2089f2fda7248c0177a5d97
motif_signature_cover_selected.tsv
  SHA-256 291df8b76f69a4c9fec4554ffea26c836b0dcb8373fe7617c4d45a7e3f2b24f7
motif_signature_cover.audit.json
  SHA-256 50b121fe4d9acb0df4a9771762372f9d699af54ec4ef622e25ea3cefa8f7a67c
verify_k17_phase0_motif_signature_cover_independent_20260802.cpp
  SHA-256 02df37365926d95e80da325acdd13639552fa9095b61577d4bd6ab8e9d87a3ae
motif_signature_cover_packing.tsv
  SHA-256 7b1c3d1e58df5ae4e6bd77975ec3ef3696b8f127da82246ab3b60a22c543dd28
motif_signature_cover_independent.audit.json
  SHA-256 a3b990ddbe545c3fa4e7b59aaf394832e41aa3aa9648ed8bec9c68f015f60883
```
