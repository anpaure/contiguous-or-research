# `k=17`: literal 7,612-piece extra-cut refinement and its exact projections

Date: 2026-08-01  
Status: living exact literal-rebuild ledger.  The first refined bank closes
all unoriented physical q1 singleton and pairwise projection gates, but has
187 common-orientation and 78 rank-ten singleton obstructions.  A later
cut-choice bank now has zero rows of both kinds while retaining all relaxed
physical q1 projections.  Its exact three-resource q1 matching is
bow-tie-UNSAT; no chronology or word is claimed.

## 1. Input witness and literal rebuild

The prospective support SAT witness in

```text
/home/amodo/or15/work/root_k17_joint_extra_cut_support_sat_20260801
```

selects 3,805 extra cuts, at most one in each of the 3,807 deterministic
anchor/rightmost-greedy base pieces.  The prospective formula is not itself a simultaneous-refinement
proof because a unary support may use a base state destroyed by another
selected split.

The present audit therefore ignores the prospective support assignments and
rebuilds the physical bank from scratch:

1. reconstruct the authenticated seven-component protected factor;
2. recompute the 3,807 deterministic anchor/rightmost-greedy minimum
   residence cuts and pieces (no global lex-minimality claim is made);
3. enumerate the 20,477 eligible internal extra cuts in the frozen order;
4. split each selected base piece at its selected gap;
5. rebuild both orientations, all selected lower colours, every atomic
   Johnson seam, and the residence/upper projections on the resulting bank.

The literal bank has

\[
  3,807+3,805=7,612\text{ pieces}
\]

and exactly 7,612 selected rank-eight cut colours.  The colours are distinct.

## 2. Exact q1 projection census

The raw atomic seam atlas has 331,716 triples.  Its literal projections are

```text
RAW triples=331716 zero_colours=0 colour_degree=2:15
    zero_tail_states=0 zero_head_states=0
    zero_tail_pieces=0 zero_head_pieces=0
    match_piece_TH=7612 match_piece_TC=7612 match_piece_CH=7612
    match_state_TH=15224 match_state_TC=7612 match_state_CH=7612
```

After the deliberately relaxed necessary two-block residence filter, 243,424
triples remain:

```text
RELAXED triples=243424 zero_colours=0 colour_degree=2:15
    zero_tail_states=187 zero_head_states=187
    zero_tail_pieces=0 zero_head_pieces=0
    match_piece_TH=7612 match_piece_TC=7612 match_piece_CH=7612
    match_state_TH=15036 match_state_TC=7612 match_state_CH=7612
```

Thus every physical piece has at least one viable outgoing and incoming
orientation, every selected rank-eight colour has at least two atoms, and
all three physical two-shore projection matchings are perfect:

\[
   T\leftrightarrow H,\qquad T\leftrightarrow C,\qquad C\leftrightarrow H.
\]

The 187 zero states on each oriented shore do not make any *unoriented*
physical piece zero; the opposite orientation survives in that one role.
However, incoming and outgoing roles must use the same orientation.  The
literal joint-orientation audit finds exactly 187 pieces of one of the forms

```text
positive: out=0,in=1; negative: out=1,in=0
positive: out=1,in=0; negative: out=0,in=1.
```

Thus neither orientation has both roles, and each such piece is an immediate
orientation-consistency obstruction.  The exact q1 CNF is consequently
UNSAT by unit propagation (zero search conflicts).  No subtler parity or
functional-Hall argument is needed to reject this particular bank.

### 2.1 The 187 failures are exactly dead old outer endpoints

The literal origin replay records whether a refined piece is the left or
right child of its base piece.  The complete pattern census is

```text
left child  (side 0): positive=10, negative=01    44
right child (side 1): positive=01, negative=10   143
```

For a left child in forward orientation, the first endpoint is the old left
outer endpoint and the last endpoint is the new internal split endpoint.
The pattern `positive=10, negative=01` says the internal endpoint has both
roles while the old outer endpoint has neither.  The right-child statement
is the reflected identity.  Therefore all 187 failures are old outer
endpoint sockets; none is a dead new split socket.

They occur in 182 base pieces, with both outer endpoints dead in five base
pieces.  Changing the split *inside the same piece* does not move its old
outer endpoint, although it may expose new compatible providers elsewhere.
This identifies the correct repair action: change some old residence cuts or
add provider sockets in other pieces, rather than merely sliding the 182
incumbent internal split points.

For comparison, the context-free conservative seam predicate is far too
strong for this bank:

```text
CONSERVATIVE triples=9586 zero_colours=4993
    zero_tail_pieces=5347 zero_head_pieces=5347
    match_piece_TH=2244 match_piece_TC=2243 match_piece_CH=2243
```

This does not refute a stateful chronology; it shows that all-one run carry
must be handled by the exact product automaton rather than a context-free
pairwise sufficient rule.

## 3. Exact rank-ten obstruction

The internal edges of the 7,612 pieces leave 5,094 rank-ten targets for the
new seams to redeliver.  Every one has a raw atomic provider, but after the
relaxed necessary residence filter exactly 78 have no provider:

```text
RANK10_ZERO raw=0 relaxed=78 conservative=3920
```

Because a rank-ten crossing target at one atomic seam is the union of its two
endpoint owners, no allocation of the existing atomic seams can repair these
78 rows.  This particular dense refinement is therefore not an upper-q1
complete resident reassembly.

## 4. What is gained

This is the first literal refinement of the protected factor in this route
for which all relaxed-residence lower-colour and *unoriented* physical
endpoint singleton rows vanish and every two-shore physical q1 projection is
perfect.  It proves that the old 1,289-colour/368-block failure is not stable
under simultaneous interior refinement, while exposing the next strictly
stronger local row: common orientation.

For this first bank, the remaining immediate finite target was:

\[
 \boxed{\text{choose/refine cuts so the 187 common-orientation and 78
 rank-ten zero rows vanish, then solve functional Hall}.}
\]

The later cut-choice descent in Sections 7--8 closes these two singleton
families.  The exact next row is the simultaneous tail/head/colour matching.
After that still come the subtour/graphic gate, the exact residence automaton,
the rank-11--17 deck, and the lower compiler.

## 5. Scope exclusions

For the first frozen bank, this audit does not prove:

* one common orientation of every piece (indeed this is disproved for the
  frozen bank by 187 literal singleton obstructions);
* a tail/head/colour perfect matching;
* a connected cycle or path;
* exact global residence (the relaxed predicate is necessary only);
* rank-ten completeness, because 78 literal zero rows remain;
* deeper upper coverage or a terminal compiler;
* `nu(17)=24313`.

The zero/zero bank of Section 8 removes the first and fifth bullets only at
the singleton-support level.  It still does not prove their simultaneous
three-resource matching or any later bullet.

## 6. Artifacts

```text
scratch/audit_k17_selected_extra_cut_literal_refinement_20260801.cpp
  SHA-256 88246fa75e63e41ff485bf6207a70c93a107f0c3c13f62bfad8566a75a3cb373
scratch/k17_selected_extra_cut_literal_refinement_20260801.audit.out
  SHA-256 ab5898b3b819e0e7257687d02418c66e41ccb3cfc204610c59b25abac94a5929
scratch/k17_dense_refinement_common_orientation_20260801.audit.out
  SHA-256 660586ce63c1a2f2ca693f0ad9df76b44e31109e09e08f366942633aff3e5ae8
scratch/k17_dense_refinement_origin_rows_20260801.audit.out
  SHA-256 5655837d063b54257066ec2c3ca9e6054d702fa927c4df0130103586cbb358b1
scratch/k17_joint_extra_cut_support_sat_20260801.selected_cuts.tsv
  SHA-256 805784da83833a537340e130e17d9cce32f61aa5e14efcd44e4c34d3829d10a5
```

Remote retained root:

```text
/home/amodo/or15/work/root_k17_joint_extra_cut_support_sat_20260801
```

## 7. First literal cut-choice descent

A subsequent literal cut-choice search kept the same 3,805-extra-cut shape
but optimized the exact pair

\[
  (\text{common-orientation zero pieces},\ 
    \text{relaxed rank-ten zero targets}).
\]

An independent replay of its current incumbent gives

```text
refined_pieces=7612 cut_colours=7612 missing_rank10=5071
RELAXED triples=234272 zero_colours=0
    zero_tail_pieces=0 zero_head_pieces=0
    match_piece_TH=7612 match_piece_TC=7612 match_piece_CH=7612
COMMON_ORIENTATION_ZERO relaxed=94
RANK10_ZERO relaxed=28
```

Thus the combined literal singleton objective fell from

\[
                  187+78=265
       \quad\hbox{to}\quad
                   94+28=122                         \tag{7.1}
\]

without losing any physical q1 projection.  This is not closure, but it
proves that both obstruction families are highly sensitive to cut choice.
It supports solving them jointly rather than treating either family as a
fixed defect of the protected factor.

```text
scratch/k17_dense_refinement_persistent122_bank_20260801.tsv
  SHA-256 f9f7997bcdb1d65281a2877c437f23d3451849d3d725ede4fa9103be6e271d4d
scratch/k17_dense_refinement_persistent122_20260801.audit.out
  SHA-256 e7bc80e4c0b50176f69576887ca8c608b874e5cf77559afe333487bf35150c01
```

## 8. Local singleton closure; matching now load-bearing

The continuing literal cut-choice search has produced a 7,612-piece bank
whose independent root replay gives

```text
zero q1 physical pieces/colours
match_piece_TH=match_piece_TC=match_piece_CH=7612
COMMON_ORIENTATION_ZERO relaxed=0
RANK10_ZERO relaxed=0
```

The full cut bank and both literal replay outputs are now synchronized:

```text
scratch/k17_dense_refinement_zerozero_bank_20260801.tsv
  SHA-256 5b4fe2d1a0125ea25f6fbb4b9259a6d2ee2007cd4ba55ac0aa4a6f23aa6bad8f
scratch/k17_dense_refinement_zerozero_search_audit_20260801.out
  SHA-256 199ab8864d35586dd7e7c97f5131562165c63bdeb47d36b0d23e45f2b8695cef
scratch/k17_dense_refinement_zerozero_literal_audit_20260801.out
  SHA-256 2a5966273d09664752457a007ab1fc4a6625ee5006f7487ac17f9dbfcfa7f2e1
```

The bank is a list of 3,805 selected extra-cut catalogue rows, not a seam
selection.  Together with the authenticated protected factor
`7c022f4050...` and the 20,477-row candidate catalogue `fa1133f5...`, it
deterministically reconstructs the 7,612 path pieces and the 228,730-edge
relaxed seam atlas.  No selected tail/head/colour matching, cycle cover,
component order, or linear chronology is present in these artifacts.

The matching payload was generated from the model builder:

```text
scratch/build_r2_k17_zero_bank_functional_rank10_cnf_20260801.cpp
  SHA-256 9d70b525ae29f2b6c5557d2ee02fe021162fd9b07f0b187ec0024d64963ae0dc
```

It encodes one incoming and outgoing seam per piece, one use of every cut
colour, one common orientation per piece, and survival of every missing
rank-ten row.  The resulting exact q1 formula is UNSAT.  Its independently
verified 14-clause/five-lemma core is the two-colour/four-directed-seam
bow-tie in
`MATH_THEOREM_K17_DENSE_ZERO265_Q1_BOWTIE_UNSAT_CORE_20260801.md`.
Thus the zero/zero result closes the two local singleton obstruction
families but this fixed bank fails the simultaneous tail/head/colour
selection.  Cut CEGAR must alter one of the two core colour/socket incidences.
Connectivity, the exact residence automaton, ranks 11--17, the compiler, and
a literal word remain open even after a future q1-SAT bank is found.
