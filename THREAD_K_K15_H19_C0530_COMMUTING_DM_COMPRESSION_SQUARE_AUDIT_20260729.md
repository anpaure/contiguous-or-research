# Exact audit of the H19 c0440/c0520 commuting compression square

Date: 2026-07-29

Status: **PASS**.  The two frozen neutral braids commute literally, their
signed all-depth shadow currents add exactly, and their positive-DM component
replacements coexist without interaction.  The double-compressed corner has
DM shore `349/330`, matching rank 16,364, and Hall deficiency 19.  The
root-960 duplicate-child common-`Q` witness survives the second braid, but no
final positive component has a duplicate native child.  No H18 or other braid
search was launched by this audit.

## 1. The frozen square

Put

\[
 A=\operatorname{FR}(3814,4556,5539),\qquad
 B=\operatorname{RF}(688,2636,2650).
\]

The audited square is

\[
\begin{array}{ccc}
X&\xrightarrow{A}&X_A\\
\scriptstyle B\downarrow&&\downarrow\scriptstyle B\\
X_B&\xrightarrow{A}&X_{AB}.
\end{array}
\tag{1.1}
\]

The four frozen carrier files and SHA-256 values are

```text
X     scratch/k15_segment_braid_hall19_zero6.provisional.json
      5c0d8125253440283769a89019400170457adb659ae63d570bf110cac417a2ec
X_A   scratch/k15_h19_profile_20260728/candidate_0440_root9104.json
      a51f8631a9b2394405b8304c949bf9606d3b43f897f51ad9474de725df34584a
X_B   scratch/k15_h19_profile_20260728/candidate_0520_split8216.json
      897ab99092552874c0b66203bc4bbe1a4e4b68e349d58521b53ebf21dd126c39
X_AB  scratch/k15_h19_commuting_square_20260729/candidate_0530.json
      79a4d1dbf5b8c40fea6086d1cd7820f74ccd058518b53f35a2e6d830fa163451.
```

The move supports are the inclusive intervals

\[
       I_A=[3814,5539],\qquad I_B=[688,2650].
\]

They are disjoint, with 1,163 untouched positions strictly between them.
Both moves preserve the length and positions outside their displayed
interval.  Direct materialization proves

\[
             B(A(X))=A(B(X))=X_{AB}
\]

as an equality of all 6,435 middle states, not merely an equality of scores.
The final middle-sequence digest is

```text
43c8029e981235210896a47b3d8161b3e96112fcd68912eed645b8753ab01742.
```

## 2. Exact checker and reproducibility

The search-free checker is

```text
scratch/audit_k15_h19_commuting_square_c0530.py
SHA-256 49686d28b64b9f86822643902ba568def51f3a701cfacd176d1ca2477c951daf.
```

Its full raw certificate is

```text
scratch/k15_h19_commuting_square_20260729/audit_k15_h19_commuting_square_c0530.json
SHA-256 9024d8c61b8ffc6d3b7c50d439cdb3709ce278606a0183b58c04ad09fdc4e27e.
```

The helper and core checker hashes used in the final H100 run are

```text
scratch/audit_k15_h19_c0440_root9104.py
54f95f21081aedc310c39971c0a7a436dd913118c8b562e3e1e42a9aa8ab798f
scratch/audit_k15_segment_braid_descent.py
1e2ad82979d747853fcf0b2a2c4e87aa1101a144ee2201474e7688f7cc3ebfdf
scratch/audit_k15_h23_component_root_common_q.py
716a9f387f48de193353a623b63447662cc285497a1329daaf68f7f85570c62c.
```

An independent physical-readiness pass used

```text
scratch/score_k15_h19_physical_readiness.py
SHA-256 93939e9d01a7efe2a8749bdabbb481734f07c0b6c93958e8b3abaf5114a23883
```

and produced

```text
scratch/k15_h19_commuting_square_20260729/candidate_0530.physical_readiness.json
SHA-256 011d5edf542b2a823fe2c626c67a7c5651c63ca09e74a3d39c2c145fc1f993f6.
```

Both exact computations ran on H100 CPU.  They reconstruct compiler graphs;
they do not enumerate braid candidates.

## 3. Deck, residence, and shadow ledgers

At every corner, the middle path is a permutation of all

\[
                         \binom{15}{8}=6435
\]

rank-eight states, every consecutive pair is a Johnson edge, and the
depth-three residence scan has no defect.  The matching rank is 16,364, the
Hall deficiency is 19, and the zero set is always

\[
 \{5801,13616,13620,17738,21641,29776\}.
\]

The complete hole ledgers are

| corner | lower holes q=1,...,7 | upper holes q=1,...,7 |
|---|---|---|
| `X` | `(4,18,11,1,0,0,0)` | `(0,0,0,0,0,0,0)` |
| `X_A` | `(4,18,13,1,0,0,0)` | `(0,0,0,0,0,0,0)` |
| `X_B` | `(4,18,11,1,0,0,0)` | `(0,0,0,0,0,0,0)` |
| `X_AB` | `(4,18,13,1,0,0,0)` | `(0,0,0,0,0,0,0)` |

Thus move `B` preserves every support set through all seven depths.  Move
`A` retains the previously audited qualification: at lower depth three it
loses exactly targets `9104` and `10688`, with no gained support.

### 3.1 Exact signed-counter additivity

Let \(C_q^\pm(T)\) be the full occurrence-multiplicity Counter at lower or
upper depth \(q\), and write

\[
 \Delta_A=C(A(T))-C(T),\qquad
 \Delta_B=C(B(T))-C(T).
\]

For each shore and every \(1\le q\le7\), the checker proves

\[
\begin{aligned}
 C_q^\pm(X_{AB})-C_q^\pm(X)&=\Delta_A+\Delta_B,\\
 C_q^\pm(X_{AB})-C_q^\pm(X_B)&=\Delta_A,\\
 C_q^\pm(X_{AB})-C_q^\pm(X_A)&=\Delta_B.
\end{aligned}
\tag{3.1}
\]

These are equalities of signed target Counters.  The corresponding
multiplicity \(L^1\) values `(A,B,total)` are

| q | lower | upper |
|---:|---:|---:|
| 1 | `(0,0,0)` | `(0,0,0)` |
| 2 | `(0,0,0)` | `(0,0,0)` |
| 3 | `(4,0,4)` | `(4,0,4)` |
| 4 | `(8,0,8)` | `(7,0,7)` |
| 5 | `(13,0,13)` | `(4,0,4)` |
| 6 | `(11,3,14)` | `(3,2,3)` |
| 7 | `(4,4,8)` | `(1,1,0)` |

The nonadditivity of scalar \(L^1\) at upper depths six and seven is genuine
cancellation on common target values, not an interaction of physical
supports.  In particular, the upper depth-seven signed currents cancel
exactly.

## 4. Additive positive-DM compression

The exact positive-DM shore matrix is

\[
\begin{array}{c|cc}
 &|L^+|&|R^+|\\ \hline
X&516&497\\
X_A&380&361\\
X_B&485&466\\
X_{AB}&349&330.
\end{array}
\tag{4.1}
\]

Move `A` subtracts 136 vertices from each shore, move `B` subtracts 31 from
each shore, and the composite subtracts their sum, 167.  The gap remains 19
at every corner.

More strongly, on each edge of the square every shared positive component
retains its exact target shore, type, induced rank, and complete physical
restricted-profile Counter.  The only component changes are

\[
 (161/160)_{960}\xrightarrow{A}(25/24)_{9104},                 \tag{4.2}
\]

and

\[
 (321/319)_{8216}\xrightarrow{B}
 (129/128)_{8217}\mathbin{\dot\cup}(161/160)_{8218}.           \tag{4.3}
\]

Both replacements occur identically in either order.  Thus (4.1) is a
componentwise direct sum, not merely a numerical coincidence.

Neither replacement is a nested target-subset operation.  In (4.2), the old
and new shores meet only at target `13264`.  In (4.3), the two new shores are
disjoint and have total size 290; their union meets the old 321-target shore
in 285 targets, leaving 36 old-only and five new-only targets.  Exact lists
and digests are frozen in the raw certificate.

### 4.1 The five focal rank matrices

In corner order `(X,X_A,X_B,X_AB)`, the induced ranks on fixed target shores
are

\[
\begin{array}{c|cccc}
\text{fixed shore}&X&X_A&X_B&X_{AB}\\ \hline
\text{old }960\text{ shore, }|S|=161&160&161&160&161\\
\text{new }9104\text{ shore, }|S|=25&25&24&25&24\\
\text{old }8216\text{ shore, }|S|=321&319&319&320&320\\
\text{new }8217\text{ shore, }|S|=129&129&129&128&128\\
\text{new }8218\text{ shore, }|S|=161&160&160&160&160.
\end{array}
\tag{4.4}
\]

The first two rows give the root-960/root-9104 rank transfer.  For move `B`,
the old fused shore gains one rank, the new root-8217 shore loses one rank,
and the root-8218 shore carries its existing one-unit defect unchanged.  This
is the exact refinement of “gap two splits into two gap-one components.”

### 4.2 Complete exceptional profile current for move B

On the fixed old root-8216 shore, canceling common profiles leaves

```text
removed: {8217,8219}, {24601,24603}
added:   {8217}, 2*{8219}, {8223}, {24603}.
```

The number of cells changes `319 -> 322` and the induced rank changes
`319 -> 320`.

On the fixed new root-8217 shore, the exact current is

```text
removed: {8217}, {8249}, {24601}, {24633}
added:   {8217,8249}.
```

The cell count changes `131 -> 128` and rank `129 -> 128`.  On the fixed
root-8218 shore the entire profile Counter is unchanged.  All three displayed
profile currents are identical before and after move `A`, which is the
profile-level commutation certificate for (4.3).

## 5. Final native atlas and readiness

Every one of the 19 final positive components is a gap-one native basis.  The
330 right cells have pairwise distinct native traces, equal componentwise to
the target shore minus its exposed root.  The three nontrivial replacement
components are

```text
root 8217: 129/128, exposed root 8217;
root 8218: 161/160, exposed root 8218;
root 9104:  25/24,  exposed root 9104.
```

The other 16 components and exposed roots are

```text
1103 3/2; 2420 2/1; 2575 2/1; 2676 2/1; 4213 5/4;
5801 1/0; 7504 5/4; 9524 2/1; 13616 1/0; 13620 1/0;
17683 2/1; 17738 1/0; 18970 3/2; 19568 2/1;
21641 1/0; 29776 1/0.
```

Across all physical compiler cells, none of these 330 selected native child
targets has a second native occurrence.  Hence the all-reserve-preserving
single-root rebase count is zero in every final component.  In particular:

| component | raw root sockets | central-safe after releasing its child | all-330-pin preserving |
|---|---:|---:|---:|
| root 8217 | 74 | 74 | 0 |
| root 8218 | 74 | 73 | 0 |
| root 9104 | 12 | 12 | 0 |

Thus the double compression reduces the canonical DM shore but does not by
itself create the duplicate child needed for the next native shrink.

### 5.1 The old root-8216 shore is not secretly ready

In the final graph, the fixed old root-8216 shore has 321 targets, 322
neighbour cells, and abstract rank 320.  Its native bank contains exactly 319
distinct nonroot targets, misses roots `{8217,8218}`, and has no duplicated
child.

Holding those 319 native pins together with all 330 final-DM native pins
gives 366 distinct target/cell pins after identifying 283 shared cells.
Every cell of the old shore adjacent to either missing root is already one of
these held cells.  There is no unused root socket.  Exhaustive literal checks
therefore give

\[
 \#\text{single-root shrink witnesses for }8217=0,
 \qquad
 \#\text{single-root shrink witnesses for }8218=0,
\]

and no two-root witness.  The abstract rank 320 is obtained through profile
rerouting; it is not an unused-cell native-shrink certificate.

### 5.2 The root-960 duplicate-child witness persists

Move `B` leaves the root-960 transfer physically intact.  The final graph
still has two depth-zero `{960,9152}` rows, at cells `4800` and `6053`, both
with native child `9152`.  Shrinking either selected cell by deleting mask
`8192` realizes root `960` while retaining the other `9152` pin.

Each resulting controller word preserves all 6,435 central windows, all 330
final-DM native pins, and all 160 nonroot native pins on the former root-960
shore.  The two banks share one pin, so after adding the exceptional root
there are 490 distinct target/cell pins on 490 distinct targets.  The word
digests are

```text
cell 4800: 1f4246d4bbf71901651921cfa6268f1541537ca8d286992b404cda6f572958fa
cell 6053: 88f7941518dbe1de09e257de1789b987628f0762c233a91ccca0b307d2e12315.
```

This is a literal common-`Q` certificate for the discharged root-960 rank
unit.  It does not supply a common controller for a full 16,364-edge matching.

## 6. Exact proved boundary

The c0530 square establishes all of the following.

1. The two disjoint-support braids commute as exact 6,435-state paths.
2. Their lower and upper trace Counters add as signed measures at every depth
   through seven, including the observed cancellations at upper depths six
   and seven.
3. Their DM actions are componentwise independent: the two replacements
   (4.2) and (4.3) coexist, producing the exact `349/330` Hall-19 shore.
4. The root-960 common-`Q` duplicate-child witness survives the composition.
5. The final 330-pin native basis has no duplicated child, so roots `8217`,
   `8218`, and `9104` remain physically unready under the native-shrink
   architecture despite many central-safe one-for-one edits.
6. The result retains all upper supports and four lower-q1 holes, but inherits
   c0440's two additional lower-q3 holes.  It is not an all-lower-ledger
   preserving carrier.

The next Hall descent therefore requires a new splitter/router that creates a
duplicate child at one of the three exposed large-component roots, or a
genuinely nonnative common-`Q` rerouting theorem.  The already-running H18
direct scan is outside this audit and was not duplicated.
