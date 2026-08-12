# Hall 20 to Hall 19: a neutral root merge followed by remote component discharge

Date: 2026-07-28

Status: exact two-braid descent theorem, independently audited.  The theorem
is literal at the middle-deck, Johnson-path, depth-three-residence, all-upper,
and occurrence-labelled compiler levels.  Its common-`Q` conclusion is the
simultaneous native lift of the final positive DM shore; no common-word lift
of the exterior residual matching is asserted.

## 1. Exact descent theorem

Let `X_20` be the certified Hall-20, zero-six carrier in
`scratch/k15_segment_braid_hall20_zero6.json`.  Define

\[
 X_{20}\xrightarrow{\operatorname{RF}(180,2764,4210)}X_{20}^{\rm merge}
 \xrightarrow{\operatorname{FR}(123,722,4710)}X_{19}.          \tag{1.1}
\]

Here `RF(a,u,v)` and `FR(a,u,v)` have their literal three-cut meanings in the
native segment-braid verifier.  The normalized artifacts are

```text
X20:       scratch/k15_segment_braid_hall20_zero6.json
X20merge:  scratch/k15_h20_h19_root8216_chain/router/candidate_0000.json
X19:       scratch/k15_h20_h19_root8216_chain/final/candidate_0000.json
```

### Theorem 1.1

Every state in (1.1) is a permutation of all
\(\binom{15}{8}=6435\) rank-eight masks, and every consecutive pair differs
in exactly two coordinates.  Every state is depth-three resident.  Every
upper support layer `q=1,...,7` is complete.  The lower hole vector is exactly

\[
                    (4,18,11,1,0,0,0)                         \tag{1.2}
\]

at all three states.  The zero-target set is exactly

\[
       \{5801,13616,13620,17738,21641,29776\}.                 \tag{1.3}
\]

The occurrence-labelled compiler ranks are

\[
                  16363,\quad 16363,\quad 16364,              \tag{1.4}
\]

so the exact Hall deficiencies are

\[
                         20,\quad20,\quad19.                  \tag{1.5}
\]

The positive DM shores have sizes

\[
                 677/657,\quad677/657,\quad516/497.           \tag{1.6}
\]

The cross-state DM gap matrix, with rows indexing the occurrence bank and
columns indexing the target shore, is

\[
 \begin{pmatrix}
 20&20&19\\
 20&20&19\\
 18&18&19
 \end{pmatrix}.                                                \tag{1.7}
\]

In particular, the matching lower bound in (1.4) and the final gap-19 shore
in (1.7) agree, proving the last equality in (1.5).

#### Proof

The two declared segment transformations reproduce the stored child arrays
entry for entry.  Their old and new seam positions are respectively

\[
 (180,2764,4211)\longmapsto(180,1627,4211),
\]

and

\[
 (123,722,4711)\longmapsto(123,4112,4711).                    \tag{1.8}
\]

All twelve displayed old/new seam pairs have symmetric difference two.
Direct traversal of the three arrays gives 6435 distinct rank-eight masks
and no bad Johnson edge.  The interval-residence checker finds no defect.
Direct enumeration of lower intersections and upper unions gives (1.2) and
upper hole vector zero at every depth; it also gives (1.3).

An independently implemented augmenting-path matcher gives (1.4).  Its
positive DM decomposition gives (1.6) and the component data below.  Applying
each of the three target shores to each of the three physical occurrence
banks gives (1.7).  Thus the final deficiency is both at most and at least
19.  No production search or production verifier is imported in this
recomputation.  \(\square\)

## 2. The neutral braid is an exact gap-preserving root merge

In `X20`, the relevant positive DM components are

\[
 C_{8217}:161/160,
 \qquad
 C_{8218}:160/159.                                             \tag{2.1}
\]

The first braid leaves the full target shore unchanged but replaces these
two components by the single component

\[
                         C_{8216}:321/319.                     \tag{2.2}
\]

Thus its total gap remains two.  On the union of the old target sets, the
induced matching rank is `319` before and after.  After cancelling complete
restricted occurrence profiles with multiplicity, 317 copies are common.
The old-only profiles are

\[
 \begin{split}
 &\{8218,8222,8282,8286,9242,9246,9306,9310\},\\
 &\{8219,8223,9243,9247\},
 \end{split}                                                   \tag{2.3}
\]

and the new-only profiles are

\[
 \begin{split}
 &\{8282,8286,9306,9310\},\\
 &\{8218,8219,8222,8223,9242,9243,9246,9247\}.
 \end{split}                                                   \tag{2.4}
\]

The two old physical rows are cells `13056` and `15638`; the two new rows
are cells `14503` and `17085`.  The complete-profile common bank has rank
16354, while the contracted exceptional bank has rank `9` on both shores.
Therefore the first braid is exactly matching-neutral, not merely neutral in
the scalar Hall score.

This is a merge rather than a compression to a smaller component: it
deliberately packages two unit defects into one gap-two root.  That packaging
is the legality router for the second move; it is not the component later
discharged.

## 3. The improving braid discharges a remote component

The second braid leaves the gap-two component `C_8216` in the final positive
DM shore.  Its gain is instead carried by the unrelated component

\[
                         C_{24610}:161/160.                    \tag{3.1}
\]

That component is absent from the final positive DM shore.  Restricted to
its fixed 161-target set, the pair

\[
  (\hbox{matching rank},\,\hbox{number of physical neighbours})
\]

changes exactly as

\[
                         (160,160)\longmapsto(161,162).        \tag{3.2}
\]

After cancelling 159 complete profile copies, the old-only profile is

\[
                            \{26146,26402\},                  \tag{3.3}
\]

while the new-only profiles are

\[
                   \{24610,25634\},\quad
                   \{26146\},\quad\{26402\}.                 \tag{3.4}
\]

There are two copies of the first profile in the new physical bank, at cells
`1212` and `4713`; one is the continuation of a pre-existing copy and one is
new.  The literal exceptional rows are

```text
old cell 1811:  depth 0, start 1811, P=(25634),
                shore={24610,25634};
old cell 12998: depth 2, start 123, P=(9986,10016,25376),
                shore={26146,26402};

new cell 1212:  depth 0, start 1212, P=(25634),
                shore={24610,25634};
new cell 4713:  depth 0, start 4713, P=(25634),
                shore={24610,25634};
new cell 11150: depth 1, start 4712, P=(26144,25634),
                shore={26146};
new cell 17586: depth 2, start 4711, P=(25376,26144,25634),
                shore={26402}.
```

The full common-profile bank for the second transition has rank 16343.
The contracted old and new boundary ranks are respectively 20 and 21.
Consequently the global rank rises by exactly one.  Equation (3.2) explains
where the unit comes from, while the survival of (2.2) proves that it is a
genuinely remote discharge rather than a refinement of the routed root.

### Corollary 3.1 (remote-discharge criterion)

Let a matching-neutral literal router merge or rearrange positive DM
components without changing the target shore.  Suppose a subsequent literal
move has a complete-profile common bank of rank \(\mu\), contracted ranks
\(b,b+1\), and an endpoint target shore of gap one less than the starting
deficiency.  Then the second endpoint has exactly that smaller deficiency.
The improved contracted unit may lie in a component disjoint from the
router's changed root.

#### Proof

Complete-profile cancellation retains every physical copy, so the two
global ranks are \(\mu+b\) and \(\mu+b+1\).  The endpoint shore supplies the
matching upper bound with the same one-unit improvement.  Nothing in the
argument identifies the contracted rank unit with the router's focal DM
component; (3.1)--(3.4) show that such an identification would be false.
\(\square\)

## 4. Exact common-`Q` scope

The final positive DM graph has 18 components: seventeen have gap one and
the root-8216 component has gap two.  Its shore is `516/497`.

Every one of the 497 right-hand physical cells has a native controller trace
which

1. is incident to that cell;
2. belongs to the 516-target shore; and
3. differs from the native trace of every other right-hand cell.

One nonzero maximal erosion controller realizes all 497 native pins
simultaneously.  There are no central-owner failures, native-trace failures,
or empty controller positions.  The trace digest in increasing
physical-cell-index order is

```text
cd4e5c0b5f010d3d248d58c9fb4314ccd78b7f07dccd3ae02d09fdf6aaeb68b8
```

After reserving these 497 target-cell pairs, the exterior incidence graph has
rank 15867, and

\[
                         497+15867=16364.                      \tag{4.1}
\]

Hence the native critical-shore atlas extends to a global maximum matching
at the incidence level.  The residual 15867 pairs in (4.1) have **not** been
shown to occur under the same erosion word.  The literal common-`Q` theorem
is exactly the simultaneous 497-pin statement, not a global universal-word
compiler.

There is also a stronger, differently scoped literal certificate on the
*former* 677-target Hall-20 shore.  In the final physical bank, the removed
root-24610 component has 162 available cells for its 160 nonroot native
targets.  Exactly two native targets are duplicated:

\[
 25634\text{ at cells }1212,4713,
 \qquad
 26146\text{ at cells }11150,11671.                            \tag{4.2}
\]

Either depth-zero `25634` copy can be shrunk literally to the exposed root
`24610` by deleting the single mask `1024` at that controller position.  A
direct interval check shows that every central window and every other
reserved native pin survives.  Combining this exceptional root pin with the
497 final-DM native pins and 160 native pins on the removed component gives

\[
                         497+160+1=658                        \tag{4.3}
\]

simultaneous pins on the former 677-target shore, hence the exact literal gap
19.  The two possible modified-word digests are

```text
cell 1212: 96d50becdfd5f9aede1fac5059b7cca295df6b37dcacbd70a8c91d88f9d63855
cell 4713: ec74223c038d38784059aae7ac801a2bce7297b90fa4503b34b3a252f343107a
```

This stronger shore-local statement still does not realize all 16364 global
matching pairs under one word.

## 5. Frozen artifacts and digests

The canonical normalized files have the following SHA-256 digests.

```text
9dd192d50e2e94dccb109fdc649fa5e13d2e4f17bac687d30547bd1bb6ddfcf1
  scratch/k15_segment_braid_hall20_zero6.json
eabc8c63d5c8ae1b63e95118be620cb2e94507dafb1d11a1b10a46de41dc2e51
  scratch/k15_h20_h19_root8216_chain/router/candidate_0000.json
86dcb9f16739b0a75eca8cde6bc9c824876453ab3b8fc70f01144da517dd4c0b
  scratch/k15_h20_h19_root8216_chain/final/candidate_0000.json
```

The byte-for-byte raw H100 exports are also frozen locally.

```text
d193eca46f8e29696e9c39854b42fe253e4ddc5975383457b236c345a4f3d36d
  scratch/k15_h20_h19_root8216_chain/raw_h100/candidate_0495.json
5c0d8125253440283769a89019400170457adb659ae63d570bf110cac417a2ec
  scratch/k15_h20_h19_root8216_chain/raw_h100/h19_from_c0495_candidate_0000.json
```

The raw and normalized copies differ only in their stored `parent` pathname.
Their 6435-entry `middle_path` arrays agree exactly.  The ordered-path SHA-256
digests, computed from the comma-separated decimal masks, are respectively

```text
e284533230910e234f657093a9966db27387f926e18c89d377e193d0c3c55be1
97429bb3f25ccf921e794c1d20ed361684116823d0a14787634dc22af820e441
```

for `X20merge` and `X19`.

The primary structural audit and the independent audit package are

```text
0c2dbba05a07da6ce133135e88437bf4bdf79fd528a6c8858388ca177ba11987
  scratch/audit_k15_h20_to_h19_root8216_chain.json
9e5353c6ca9092358043a174ddecfd900cefbbfd42b121628f1935ebd04fa24f
  scratch/audit_k15_h19_root8216_chain_independent.py
71207dcfb6f02d7f5ac5e91bbf28863ca2831edd82b6a7de87ff39001ccd4c5d
  scratch/audit_k15_h19_root8216_chain_independent.json
d0bc469b9e53222c7088005b3508b67a89df76403afda79adcffb2497a94e260
  scratch/audit_k15_h20_h19_exposed_roots_common_q.py
1596c84c23556ed9d3bfa6e01f9cc5d05ab5333625d36325ee5d7288ff2fa5a2
  scratch/k15_h20_h19_exposed_roots_common_q_certificate.json
```

The independent checker uses the independently maintained core
`scratch/audit_k15_h21_zero6_independent.py`, whose digest is

```text
595e2b9a3cafc73812c9129b4d8ab9dc84db996b7f16b932633d283f210c88e8
```

and imports neither the search engine nor the production verifier.

The completed direct one-braid scan from the raw `X19` file has the frozen
summary digest

```text
5f6b0a29838976bc83c974018c1836b7b4d0343d699f024e2ec84848f32e6394
  /dev/shm/k15_rotation/h19_scan_20260728/scan.out
```

It considered 548377 Johnson candidates, of which 11957 were resident and
9164 were upper-safe.  Its complete score census is

```text
Hall 19 / zero 6: 7124     Hall 19 / zero 7: 2
Hall 20 / zero 6:  114     Hall 20 / zero 7: 8
Hall 21 / zero 6:   43     Hall 21 / zero 7: 1
Hall 22 / zero 6:    4
Hall 23 / zero 6:    6
Hall 24 / zero 6:    1
```

Thus there is no direct Hall-18 three-cut neighbour of `X19`.  The scan
executable digest is

```text
2ddea75b76e2dfae40b382ceea9c8669dab47f3cc1dc0cd5e725fa3b192fe376
```

and the empty `scan.err` digest is the standard SHA-256 of the empty file.

## 6. Sharp remaining boundary

This theorem proves a new literal Hall descent and a protected
critical-shore common-`Q` lift.  It does not prove Hall zero, does not reduce
the six literal zero targets, and does not globally compile the exterior
15867 matching pairs.  The direct three-cut neighbourhood has no Hall-18
state, so the exact continuation is the now-running neutral-state emission
followed by both raw DM-compression ranking and fixed-shore/complete-profile
ranking.  The independently discovered
double-compressed Hall-20 packet ladder remains a separate branch and is not
used in Theorem 1.1.
