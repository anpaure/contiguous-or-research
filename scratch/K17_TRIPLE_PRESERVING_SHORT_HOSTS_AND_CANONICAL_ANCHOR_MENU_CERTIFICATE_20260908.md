# Triple-preserving short hosts and one canonical k17 anchor catalogue

2026-09-08. Exact finite census by `exact_b_finite_frontier`, executed only on h100. **No covering choices were optimized or selected.** The output is one explicit finite catalogue for a subsequent feasibility decision.

The original canonical capped PBBS bank has H=min(height,3). Keep every H=1 and H=2 component unchanged. On H=3 components, retain every native three-letter OR of rank eight, while permitting two-letter ORs to change.

Two exact results were obtained:

1. Without an anchor restriction, every one of the 41,225 targets of ranks 1–7 has an individual legal one- or two-position host, or is already covered on a frozen component. Exactly 714 rank-six labels have no pair host, and therefore require a literal occurrence in this architecture.
2. With the single fixed anchor choice `0,3,6,...` on every canonical H=3 cycle, every lower target remains individually possible. The catalogue has 7,377 editable blocks and 2,346,272 options. It exposes 4,504 rank-seven labels requiring an internal pair, including 4,441 labels with just one provider block; 1,529 rank-six labels require an editable position to retain its full literal label.

These facts do not establish that one option can be selected per block to cover all targets simultaneously. Nor has this periodic bank been joined into a linear optimal word.

## 1. Fixed input, source windows, and independently recovered pins

Input: [the canonical cycle data](k17_height_adaptive_20260908/height_adaptive_canonical_cycles.json), SHA-256

`fed20c313c639740b089428c1d2b8b572fc7138de4c11c2203be554e4acfa2a3`.

The cycles retain their original minimum-mask cuts and forward g=f² orientation. No cut, orientation, order, or owner was searched or modified. Of the 146 components, 30 have H≤2 and are frozen. The remaining 116 components contain 22,134 H=3 positions.

For upper owners X_i, reconstruct

\[
D_i=X_i\cap X_{i+1}\cap X_{i+2}\cap X_{i+3}.
\]

All H=3 letters have rank six, all native pairs have rank seven, and all native triples

\[
R_j=D_j\cup D_{j+1}\cup D_{j+2}
\]

have rank eight. Every four-letter window was also checked to equal its prescribed rank-nine owner.

The required pin at position i was computed directly as the union of the deficits left by removing i from each of the three native triple windows that contains it. At all 22,134 positions this equals the earlier owner-endpoint formula

\[
\operatorname{Pin}_i=(X_i\setminus X_{i-1})\cup
(X_{i+3}\setminus X_{i+4}).
\]

Every pin is nonempty and lies in D_i. This verifies that the same pins can be used for triple preservation; the change of required window width was not silently assumed harmless.

## 2. The exhaustive individual-host census

For an interval I of length one or two define

\[
F_I=\bigcup_{i\in I}\operatorname{Pin}_i,\qquad
V_I=\bigcup_{i\in I}D_i.
\]

The verifier independently computes the exact triple deficit

\[
G_I=\bigcup_j\left(R_j\setminus
\bigcup_{i\in[j,j+2]\setminus I}D_i\right)
\]

and checks G_I=F_I for every interval. A cap on I, leaving other letters full, preserves all triples and realizes target S exactly if and only if

\[
F_I\subseteq S\subseteq V_I.
\]

Necessity follows from the exact deficits. Sufficiency is realized by `E_i=D_i intersect S` on I, with other letters unchanged. The nonempty pins guarantee nonempty new letters. The general proof and its stronger-deck specialization are in [the cap and matching reduction](PBBS_EXACT_SHORT_TARGET_CAPS_AND_CAPACITATED_MATCHING_REDUCTION_20260908.md), §§2–5.

This is exhaustive for individual lower targets in any triple-preserving cap: an interval of length at least three already contains a fixed rank-eight triple, so it cannot realize a target of rank at most seven. The verifier enumerates the complete Boolean interval between F_I and V_I, not merely a selected family of sufficient caps.

The frozen H≤2 components cover 1,887 distinct lower targets, all of rank seven. The census on H=3 checks 44,268 short intervals and enumerates 631,992 interval-target incidences. It directly replays 154,938 triple windows under minimum caps and checks 66,402 singleton exclusion windows.

| Rank | Covered targets after adding frozen components | Missing |
|---:|---:|---:|
| 1 | 17 | 0 |
| 2 | 136 | 0 |
| 3 | 680 | 0 |
| 4 | 2,380 | 0 |
| 5 | 6,188 | 0 |
| 6 | 12,376 | 0 |
| 7 | 19,448 | 0 |

Of the 12,376 rank-six labels, 11,662 have an individually legal two-letter host and 714 do not. The latter must have a one-letter witness. Since a cap of a rank-six original letter can have rank six only when it equals that full original letter, these 714 labels force literal reservations in any cap preserving all native triples with H≤2 frozen. This is a local necessary condition, not a count of mutually compatible reservations.

## 3. The one fixed anchor frame

In each canonical H=3 cycle of period v, retain the full letters at

\[
0,3,6,\ldots,3\lfloor(v-1)/3\rfloor.
\]

The cyclic distance between successive anchors is at most three. Nonempty editable blocks between them have length one or two. The fixed frame contains:

- 7,414 full anchor positions;
- 14,720 editable positions;
- 34 one-position blocks and 7,343 two-position blocks;
- 7,377 blocks in total.

Each editable position i may take every letter between Pin_i and D_i. The verifier found 13,011 positions with 16 cap choices and 1,709 positions with 32 choices. A block option is the Cartesian product of its position menus. Thus the exact option-count census is:

| Options in a block | Number of blocks |
|---:|---:|
| 16 | 34 |
| 256 | 5,745 |
| 512 | 1,487 |
| 1,024 | 111 |

All 2,346,272 options were enumerated for the local target catalogue. There was no attempt to choose compatible covering options.

## 4. Simultaneous preservation is certified for the entire menu

Form the single global minimum word on each component: full D_i at every anchor and Pin_i at every editable position. The verifier checks all 22,134 native triple windows in these minimum words against the originals. They all agree.

Any choice of options from the catalogue lies coordinatewise between that minimum word and the original word. Monotonicity of OR therefore proves that **every simultaneous combination of block options preserves every triple**, including windows crossing between blocks and across the canonical cyclic cut. This global minimum test is stronger than testing each block in isolation with all other letters full.

It also checks all 14,791 pair occurrences touching a full anchor: their minimum-word OR equals their original rank-seven OR. Consequently those boundary pairs are fixed for every option combination. Only the pairs lying inside two-position editable blocks may change.

All longer native windows are unions of consecutive triples, so their ORs are preserved as well. The frozen components remain unchanged. The unresolved issue is lower-target coverage, not preservation of those native windows.

## 5. Exact lower-target interface of the frame

The targets permanently covered by the frame are:

1. the frozen H≤2 targets;
2. full anchor letters, of rank six;
3. fixed pairs touching an anchor, of rank seven.

Their distinct census is 5,999 rank-six labels and 14,944 rank-seven labels, or 20,943 fixed targets.

For each editable block, the only additional lower targets are its chosen letter or letters, and, for a two-position block, their union. A longer interval contains a retained rank-eight triple. A pair crossing a block boundary is already among the fixed pairs. Thus the fixed targets together with these local option targets are the complete rank≤7 interface for this architecture.

The union over **all** block options contains every one of the 41,225 lower targets. This union is an individual-feasibility statement: different targets may require incompatible options in the same block.

The exact compulsory conditions exposed by the catalogue are:

- **Rank six:** 9,398 labels have an internal-pair host in the frame; 2,978 do not. Of those 2,978 mandatory literal labels, 1,449 already occur at fixed anchors and 1,529 must be supplied by a full letter at an editable position.
- **Rank seven:** 4,504 labels are absent from the fixed palette and must retain an internal pair. Of these labels, 4,441 have one provider block, 12 have two provider blocks, and 51 have three. No required rank-seven label lacks a provider.

A rank-seven target produced by an internal pair must equal that pair's original rank-seven union: caps cannot add coordinates, and no proper subset has rank seven. Therefore the 4,441 one-provider labels force preservation of their specific block's original pair OR, though they need not force either constituent letter to remain full.

One exact subsequent decision is now fully specified: choose one option per block so that every target outside the fixed palette occurs among the selected local option targets. The required-rank-seven provider lists and the mandatory editable-literal rank-six lists are included in the menu. No extra joins, boundary witnesses, or probabilistic assumptions belong to this decision.

## 6. Artifacts and execution

The [executable census](census_k17_triple_preserving_anchor_menus_20260908.py) was copied to

`h100:/home/amodo/census_k17_triple_preserving_anchor_menus_20260908.py`.

Its single run enforced 120 CPU seconds, 150 wall seconds, and 2 GiB address space. It returned PASS in approximately 3.00 seconds. No mathematical code ran locally and no optimization or random search was performed.

Local bundle: [k17_triple_anchor_menus_20260908](k17_triple_anchor_menus_20260908/).

- [Full compact certificate, missing lists, and compulsory-label lists](k17_triple_anchor_menus_20260908/triple_preserving_host_and_anchor_certificate.json).
- [Exact factorized anchor menu](k17_triple_anchor_menus_20260908/canonical_w3_anchor_factorized_menus.json).
- [One block option witnessing each locally possible target](k17_triple_anchor_menus_20260908/canonical_w3_anchor_target_first_options.json).
- [Individual unrestricted short-host witnesses](k17_triple_anchor_menus_20260908/individual_triple_preserving_first_hosts.json).
- [Exact singleton/pair host counts per target](k17_triple_anchor_menus_20260908/individual_triple_preserving_host_counts.json).

The menu is 4,315,847 bytes, below the requested 100 MiB cap, with SHA-256

`bf55d2ef90e32f7eac6148e1e889d87a4a0214e651adb62df543c2e7af04c642`.

Its representation is exact, not compressed by dropping options: each block lists every allowed mask at each of its one or two positions, and its options are the Cartesian product in `itertools.product` order. The menu also includes canonical sources, pins, anchor positions, fixed targets, original internal rank-seven labels, and the number of options retaining each such label.

Remote output directory: `/home/amodo/exact-b-k17-triple-anchor-menus-20260908/`.

The catalogue now makes one finite constructive feasibility decision available. It does not itself solve that decision or produce a new full-cube linear word.
