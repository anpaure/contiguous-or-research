# Exact audit of the frozen H19 c0440 root-9104 neutral braid

Date: 2026-07-28

Status: **PASS**, with one material ledger qualification.  The frozen braid is
a deck-exact, Johnson, depth-three-resident, Hall-neutral component exchange,
and its root-960 rank transfer has a literal common-`Q` realization.  It does
not preserve the complete lower support ledger: at lower depth three it loses
exactly targets `9104` and `10688`, changing the lower hole count from 11 to
13.  No braid search was run for this audit.

## 1. Frozen inputs and independent checker

The audited transition is

\[
 X_{19}\xrightarrow{\operatorname{FR}(3814,4556,5539)}X'_{19}.
\]

The frozen input hashes are

```text
5c0d8125253440283769a89019400170457adb659ae63d570bf110cac417a2ec
    scratch/k15_segment_braid_hall19_zero6.provisional.json
a51f8631a9b2394405b8304c949bf9606d3b43f897f51ad9474de725df34584a
    scratch/k15_h19_profile_20260728/candidate_0440_root9104.json
```

The base hash is also the hash of the H100 source
`/dev/shm/k15_rotation/h19_scan_20260728/state.json`.  Direct application of
the `FR` block formula to the base middle sequence gives the candidate middle
sequence byte for byte.

The search-free exact checker and its raw result are

```text
scratch/audit_k15_h19_c0440_root9104.py
scratch/k15_h19_profile_20260728/audit_k15_h19_c0440_root9104.json
```

with SHA-256 values

```text
54f95f21081aedc310c39971c0a7a436dd913118c8b562e3e1e42a9aa8ab798f
fd1ee165a73299d161a3ac82c10e1f6b7d783662be7227102ebce92b8fbea74e.
```

The independent generic physical-readiness postprocessor gives

```text
scratch/k15_h19_profile_20260728/candidate_0440_root9104.physical_readiness.json
SHA-256 57407a00117e6ef77adb0a53221016925f6e0dd1a831bdf164c737778b0c716a
```

and independently agrees that the final positive-DM shore is a global native
basis but has no duplicate native child and no all-reserve-preserving root
rebase.

## 2. Exact carrier and shadow ledgers

Both endpoints are permutations of all

\[
 W=\binom{15}{8}=6435
\]

rank-eight middle states.  Every consecutive pair is a Johnson edge, and the
depth-three residence scan has no bad run at either endpoint.  The middle
sequence digests are

```text
base   97429bb3f25ccf921e794c1d20ed361684116823d0a14787634dc22af820e441
child  014c9f5a870f819c0b22045e9e98ddbdfc6adb839f2354d387528e7cdbb6dd38.
```

The complete support-hole ledgers are

| shore | state | q=1 | q=2 | q=3 | q=4 | q=5 | q=6 | q=7 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| lower | base | 4 | 18 | 11 | 1 | 0 | 0 | 0 |
| lower | child | 4 | 18 | 13 | 1 | 0 | 0 | 0 |
| upper | base | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| upper | child | 0 | 0 | 0 | 0 | 0 | 0 | 0 |

The occurrence-multiplicity transitions are also exact.  The following table
gives the half-open comparison as `removed/added`, together with full
multiplicity \(L^1\):

| q | lower removed/added; L1 | upper removed/added; L1 |
|---:|---:|---:|
| 1 | 0/0; 0 | 0/0; 0 |
| 2 | 0/0; 0 | 0/0; 0 |
| 3 | 2/2; 4 | 2/2; 4 |
| 4 | 4/4; 8 | 4/3; 7 |
| 5 | 7/6; 13 | 2/2; 4 |
| 6 | 7/4; 11 | 1/2; 3 |
| 7 | 2/2; 4 | 0/1; 1 |

Thus the complete lower and upper counters are identical at depths one and
two.  At lower depth three the support loss is exactly

\[
                       \{9104,10688\},
\]

with no gained support.  At every other lower depth the support set is
unchanged, although multiplicities change.  Every upper support set remains
complete; upper counters are identical only at depths one and two.

This is why `score.lower_holes=4` is correct but is not a certificate of
all-depth lower-support preservation.

## 3. Exact Hall-neutral DM component exchange

The compiler matching rank and deficiency are unchanged:

\[
 \nu(G)=\nu(G')=16364,
 \qquad \operatorname{def}(G)=\operatorname{def}(G')=19.
\]

The positive DM shore contracts from

\[
                         516/497\quad\hbox{to}\quad380/361.
\]

There are 18 positive components at both endpoints.  Seventeen components
retain exactly the same target shore, type, induced matching rank, and full
physical restricted-profile multiset.  The only component-root change is

\[
              (161/160)_{960}\quad\longrightarrow\quad(25/24)_{9104}.
\tag{3.1}
\]

The two target shores in (3.1) are not nested: their intersection is the
single target `13264`.  Hence “compression” here means an exact replacement
of a 161/160 positive component by a 25/24 positive component, reducing both
DM shores by 136 while preserving gap one.  It is not a 25-target subset cut
out of the old component.

On the fixed old 161-target shore, the induced rank changes

\[
                         160\longrightarrow161;
\tag{3.2}
\]

on the fixed new 25-target shore, it changes

\[
                          25\longrightarrow24.
\tag{3.3}
\]

Equations (3.2) and (3.3), together with exact invariance of the other 17
component profiles, give a direct physical-profile proof of Hall neutrality.

### 3.1 Complete old-shore profile current

After cancelling identical physical profiles with multiplicity, the old
root-960 shore loses

```text
{960,3008,9152,11200}
{960,9152,9168}
{961,3009,9153,11201}
{3008,3024,11200,11216}
{5056,7104,13248,15296}
{9154,9170}
```

and gains

```text
{960,9152}
{3008,3009,11200,11201}
{3008,11200}
{3024,11216}
{7104,15296}
{9168}
{9170}.
```

Every displayed multiplicity is one.  The decisive rank-one feature is the
new copy of the two-target star

\[
                             \{960,9152\}.
\tag{3.4}
\]

The base has one such physical row, at depth/start `0/6053`.  The child has
two, at depth/start `0/4800` and `0/6053`.  At either cell the controller
value and envelope are `9152`, the mandatory core is `576`, and the native
trace is `9152`.

### 3.2 Complete new-shore profile current

On the fixed 25-target root-9104 shore, the child loses the singleton rows

```text
{9104}, {11152}, {11153}
```

and gains

```text
{9104,11152}, {9105,11153}.
```

This changes 25 available cells of rank 25 into 24 cells of rank 24 and is
the exact source of the new gap-one component.

## 4. Literal common-`Q` realization of the root-960 transfer

The child neighbourhood of the former root-960 target shore contains 161
cells.  Their native traces consist of every one of the 160 nonroot targets,
with `9152` occurring twice, and omit only root `960`.  Thus (3.4) is not only
an abstract matching edge: it is the duplicate-child configuration needed
for a literal shrink.

Choose either star cell and retain the other as the native pin for `9152`.
At the chosen depth-zero cell replace

\[
                 9152\longmapsto960,
                 \qquad9152\setminus960=8192.
\]

The exact checker verifies, for either choice, all 6,435 central windows,
all 361 native pins of the final positive-DM shore, all 160 nonroot native
pins of the former root-960 shore, and the exceptional root-960 pin.  The two
native banks share one identical pin, cell `13326` for target `13264`; after
identifying it, each word realizes 521 distinct target/cell pins on 521
distinct targets.

The two choices and word digests are

| root cell | companion `9152` cell | changed position | word SHA-256 |
|---:|---:|---:|---|
| 4800 | 6053 | 4800 | `d4a366e3037bb702f02b369af41acf3da160935a9a9421c1fa94722b0780855c` |
| 6053 | 4800 | 6053 | `746bf0bd9048dac284793196585e734e55b90f8e1354c630402a4547b919d590` |

This proves a literal common-`Q` realization of the rank unit moved off the
old component.  Its scope is the 521-pin union just stated, not a common word
for a full 16,364-edge global matching.

## 5. Final native basis and the new physical obstruction

Every final positive component is a native forest.  Its right cells have
pairwise distinct native traces equal to its target shore minus the exposed
roots.  The exact atlas is

| structural root | type | exposed native roots |
|---:|---:|---|
| 1103 | 3/2 | 1103 |
| 2420 | 2/1 | 2420 |
| 2575 | 2/1 | 2575 |
| 2676 | 2/1 | 2676 |
| 4213 | 5/4 | 4213 |
| 5801 | 1/0 | 5801 |
| 7504 | 5/4 | 7504 |
| 8216 | 321/319 | 8217, 8218 |
| 9104 | 25/24 | 9104 |
| 9524 | 2/1 | 9524 |
| 13616 | 1/0 | 13616 |
| 13620 | 1/0 | 13620 |
| 17683 | 2/1 | 17683 |
| 17738 | 1/0 | 17738 |
| 18970 | 3/2 | 18970 |
| 19568 | 2/1 | 19568 |
| 21641 | 1/0 | 21641 |
| 29776 | 1/0 | 29776 |

Across all physical compiler cells, none of the 361 native child targets in
this final reserve has a second native occurrence.  Consequently every raw
root socket occupies the unique selected pin of its child.  There is no
literal single-root shrink that simultaneously preserves all 361 selected
native pins, in any component.

For the new root-9104 component there are 12 raw child/root sockets.  All 12
are central-window-safe and preserve every other final native pin if their
own child pin is released.  Seven are unit-coordinate sockets, with deleted
coordinates `1,2,3,6,12,13,15`.  But none has a second occurrence of its
child, so the exact all-reserve-preserving rebase count is zero.  This is the
precise physical distinction between the discharged root-960 star and the
new abstract root-9104 deficiency.

The no-duplicate conclusion is scoped to the canonical final native basis
and literal downward shrinks of its native children.  It does not rule out an
arbitrary nonnative common controller or a later braid that creates a second
child occurrence.

## 6. The root-8216 two-root component: partial and full readiness

The persistent component with structural intersection `8216` has type

\[
                           321/319
\]

and exposed roots `{8217,8218}`.  Its raw socket census is:

* 74 child/root sockets for `8217`;
* 74 child/root sockets for `8218`;
* 148 total.

If the occupied child pin is released, 74/74 `8217` sockets and 73/74 `8218`
sockets admit a literal central-safe shrink preserving every other final
native pin.  The sole failure is

```text
root 8218, child 9247, cell 16486, depth/start 2/3611,
deleted mask 1029.
```

For simultaneous two-root shrink, 5,355 ordered cell pairs preserve every
central window and every native pin except the two socket children.  Their
certificate digest is

```text
0f8c0c9832f4a0d7c52838cb1a8690da278f1b4cfca8760c658be218adf5c692.
```

One explicit pair is

```text
8217: child 8219 at cell/start 2654, delete mask 2;
8218: child 8222 at cell/start 6323, delete mask 4;
word SHA-256 9c82a3d9e418660dcb32b41c59ac909c311949fa82f6a6f2cd9db5c0e0cf05e3.
```

Thus chronology and central-window compatibility are abundant.  The exact
native-pin verdict is nevertheless:

\[
 \begin{array}{c|c}
 \text{test}&\text{result}\\ \hline
 \text{one exposed root while preserving all 361 native pins}&0\\
 \text{both exposed roots while preserving all 361 native pins}&0.
 \end{array}
\]

There is no duplicate native child anywhere in the reserve, so neither a
partial nor a full discharge is physically ready under the native-shrink
architecture.  The obstruction is pin conservation, not a scarcity of
central-safe two-root controller edits.

## 7. Proved boundary and next exact target

The frozen c0440 braid proves all of the following.

1. It is an exact `FR(3814,4556,5539)` carrier move preserving the middle
   deck, Johnson chronology, and depth-three residence.
2. It keeps Hall deficiency 19 and transports one DM gap unit from the
   root-960 161/160 component to the root-9104 25/24 component.
3. The transfer is explained by exact opposite local ranks `160 -> 161` and
   `25 -> 24`; all other positive components retain their complete restricted
   profile counters.
4. The new `{960,9152}` copy is a literal duplicate-child star and yields two
   common-`Q` 521-pin shrink witnesses.
5. The final 380/361 positive shore is a native forest atlas with 19 exposed
   roots, but has no duplicated native child.  Root `9104` is therefore not
   immediately shrink-ready, and the two-root `8216` component is neither
   partially nor fully shrink-ready while all 361 native pins are reserved.
6. The braid preserves every upper support and the exact depth-one and
   depth-two counters on both sides, but it is not an all-lower-shadow move:
   its lower depth-three hole count is 13, not 11.

Accordingly, the next router/splitter must do more than compress the raw DM
shore.  It must create a second native occurrence at a root-9104 or
root-8216 socket (or supply a genuinely nonnative common-`Q` replacement)
without sacrificing the reserved child pin.  The present audit neither
launches nor assumes such a search.
