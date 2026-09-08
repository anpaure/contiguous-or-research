# K16 exact-229 Hall-25 component and donor-signature audit

## 1. Result and scope

Let \(T_{229}\) be

```text
scratch/ad_k16_bad2_splitpair_exact_20260730/exact_229.targets
```

(SHA-256
`cae23cfcedbc9d193ebd9191045edd0e5c14f56af5fc96a802b8cefa7cd7e974`).
It is one of the literal middle-exact, zero-envelope, arbitrary-upper-complete
split-pair endpoints in the frozen catalogue.  This note audits only its
generalized depth-three lower compiler incidence graph.  It does not assert
that any two endpoint macros can be spliced.

The exact generalized Hall parameters are

\[
 |L|=26332,qquad |R|=32063,qquad |E|=347875,
 \qquad \nu=26307.
\]

Thus the deficiency is exactly \(25\).  The canonical alternating Hall shore
has

\[
 |Z_L|=212,qquad |N(Z_L)|=187,qquad
 |Z_L|-|N(Z_L)|=25.                       \tag{1.1}
\]

The decisive structural fact is stronger:

> **Hall-component theorem.**  The induced graph on the canonical shore is
> the disjoint union of exactly 25 connected components, and every component
> has matching deficiency exactly one.

There is therefore no surviving deficiency-two packet in \(T_{229}\).

## 2. Forced-provider normal form

The 212 left masks have rank histogram

\[
 1^1,5^6,6^{44},7^{161}.
\]

Their degrees in the full incidence graph split as follows.

| class | count | ranks |
|---|---:|---|
| zero provider | 12 | one rank 1, eleven rank 7 |
| unique provider | 150 | all rank 7 |
| multiple providers | 50 | six rank 5, forty-four rank 6 |

The 150 unique-provider targets use 150 distinct physical cells.  Hence the
187-cell shore consists of those 150 forced cells plus only 37 further cells
for the 50 lower targets.  This gives the exact decomposition

\[
 25=12+(50-37).                            \tag{2.1}
\]

The twelve zero-provider masks are

```text
2665 28e9 291d 29a9 2f28 4879 48e9 4e70
6989 6a29 6c70 8000
```

The 25 components, written `minimal root : left/right`, are

```text
00cd:15/14  014e:34/33  04d8:35/34  05a4:18/17
0665:7/6    091d:4/3    21a9:3/2    2665:1/0
28e9:1/0    291c:3/2    291d:1/0    29a9:1/0
2e28:6/5    2f28:1/0    30e0:44/43  4879:1/0
48e9:1/0    4a29:4/3    4e70:1/0    5340:23/22
6989:1/0    6a29:1/0    6c30:4/3    6c70:1/0
8000:1/0
```

The full left and right lists for every component are frozen in the JSON
audit rather than duplicated here.

## 3. Monotone component-expansion lemma

Let \(M\) be the matching used to construct the canonical alternating shore.
Inside any one of the 25 components, every left vertex is reachable from its
unmatched left root by an \(M\)-alternating path.  Suppose a modification:

1. retains every old incidence;
2. supplies an \(M\)-unmatched right cell \(r\) adjacent to any left member
   of that component; and
3. does not identify \(r\) with a fresh cell assigned to another component.

Append the new edge to the alternating path.  This is an augmenting path, so
the matching increases by one.  Paths in distinct old components are
vertex-disjoint.  Consequently \(s\) such monotone additions in \(s\)
distinct components decrease the deficiency by exactly \(s\).

Both hypotheses are essential.  A cell merely fresh to \(N(Z_L)\) can already
be matched by \(M\) to a target outside \(Z_L\), and deleting one of its old
candidate incidences can move the defect outside \(Z_L\).  Such a cell needs
an independently certified continuation of the alternating path to a free
right endpoint.  All endpoint comparisons below are audited against that
distinction.

### 3.1 Exact component signature

For a proper-prefix cell \(c=[s,s+\ell)\), write its full physical profile as

\[
 \pi(c)=\bigl(M_c;E_s,E_{s+1},\ldots,E_{s+\ell-1}\bigr),
 \qquad A_c=\bigcup_{p=s}^{s+\ell-1}E_p.                 \tag{3.1}
\]

Here \(M_c\) is the mandatory mask and the \(E_p\) are the ordered maximal
envelope letters.  If \(L_j\) is the left shore of component \(j\), define

\[
 \Sigma(c)=\left\{j:\exists X\in L_j,
   M_c\subseteq X\subseteq A_c,
   \quad X\cap E_p\ne\varnothing\text{ for all }p\in[s,s+\ell)
             \right\}.                                  \tag{3.2}
\]

Then \(j\in\Sigma(c)\) if and only if \(c\) is a literal candidate cell for
some target in component \(j\).  Thus (3.2), not merely the pair
\((A_c,M_c)\), is the exact cell signature.  A proposed profile change
\(\pi(c)\to\pi'(c)\) adds precisely the components in
\(\Sigma'(c)\setminus\Sigma(c)\).  When the changed right cells are
\(M\)-free, retain all old incidences, and admit distinct component
representatives, the alternating paths of the component theorem turn this
signature SDR into literal disjoint augmentations.

## 4. Relation to the detached-cycle Hall-34 carrier

For the former `pass_1` carrier, the canonical shore was \(249/215\), with
33 connected components and total deficiency 34.  Passing to \(T_{229}\)
removes the old components rooted at

```text
4268 4331 4339 4378 5439 5670 581c
583c 5c30 5c70 6a38 6a70 6b21
```

whose total deficiency was 14; the `4331` component was the unique
deficiency-two component.  It introduces the five deficiency-one roots

```text
091d 291c 291d 2e28 2f28.
```

Thus the exact accounting is

\[
 34-14+5=25.                               \tag{4.1}
\]

### 4.1 The old sixteen-cell donor bank

Relative to `pass_1`, the upper-complete `pass_0` macro supplied 16 fresh
right cells to the old 249-left shore.  In \(T_{229}\):

* nine signatures survive literally, at cells

```text
2357 2359 2360 2364 16157 17968 17969 18880 18881;
```

  every one of their intended targets has left the deficient shore;
* five further nonsurviving signatures have also become obsolete because
  their targets `5c70,5c30,6a70,6a38,6b21` left the shore;
* precisely two nonsurviving signatures still target deficient components.

Those last two are the cleanest current local objectives:

| cell | interval | exact-229 ordered envelopes | pass-0 ordered envelopes | `(allowed,mandatory)` old -> new |
|---:|---|---|---|---|
| 13964 | `[4654,4657)` | `6021,4821,0829` | `6221,4a21,0a29` | `(6829,6809)` -> `(6a29,6809)` |
| 13966 | `[4655,4657)` | `4821,0829` | `4a21,0a29` | `(4829,4809)` -> `(4a29,4809)` |

The envelope sequences are ordered by increasing physical position; they are
not unordered multisets.  Replaying the full candidate predicate (allowed
set, mandatory set, and a nonempty hit in every displayed envelope letter)
gives

```text
cell13964: {6809,6829} -> {6809,6829,6a09,6a29},
cell13966: {4809,4829} -> {4809,4829,4a09,4a29}.
```

Thus the changes are genuinely incidence-monotone, not merely
allowed/mandatory-compatible.  Both physical cells are free in the frozen exact-229 maximum
matching.  The two disjoint augmenting paths are explicitly

```text
6a29 -- cell13964,
5a29 -- cell18077 --[matched] 4a29 -- cell13966.
```

Here `6a29` and `5a29` are the unmatched left vertices of their respective
components, and cell 18077 is matched to `4a29`.  Thus an exact and
arbitrary-upper-safe local macro realizing both signatures while retaining
the rest of \(T_{229}\) would prove a deficiency drop

\[
 25\longrightarrow23.                    \tag{4.2}
\]

This local macro is **not proved** here.  The old pass-0 implementation
coupled these cells to a larger target permutation.

### 4.2 The natural shifted eight-cycle fails by one carrier bit

The most direct occurrence-cycle transplant was tested exactly.  On

```text
positions: 3846 2328 3933 3522 2063 817 238 4653
values:    6b29 6939 293d 297c 293e 693a 69aa 69a9
```

cyclically assign each position the next displayed value.  This installs
`6b29` at 4653 and realizes both desired ordered envelope profiles in the
table above.  It retains capacity 32063, has no zero envelope, and has zero
arbitrary-upper holes.  Nevertheless it is not middle-exact.  At row 3845,

```text
target              6ba8
ordered envelopes   6888 6828 6920 6120
their OR             69a8
missing              0200
```

Equivalently, the bit-9 carrier of row 3845 is empty.  The former last
envelope was `6320`; the shifted cycle leaves `6120`.  Therefore the natural
eight-cycle is rigorously closed.  A successful extension needs a
compensating rethread that restores `0200` at this seam without undoing the
late cell profiles.

There is also a complete fixed-neighbour seam atlas.  Hold every target row
except row 3846 fixed, retain the frozen depth schedule, and ask which
rank-eight mask can occupy row 3846 while every affected middle replay
equation remains exact.  Exactly ten masks work:

```text
2b39 2ba9 2bb1 2bb8 6b29 6b31 6b38 6ba1 6ba8 6bb0.
```

All contain the missing bit `0200`; `6b29` is the incumbent.  For each of the
nine nontrivial donors, insert it between `6b29` and the former shifted-eight
tail and close the resulting nine-token occurrence cycle.  Exact full replay
rejects all nine at the donor's source collar.  Two retain arbitrary-upper
completeness, four create one upper hole, two create two, and one creates
four, but none is middle-exact.  Thus a single inserted seam-compatible donor
cannot repair the natural cycle.  This is a scoped nine-cycle no-go: a
different circulation, a block braid, or changes to multiple seam-neighbour
rows remain open.

The former transfer cell 18449, which moves service to `5670`, also survives
literally; `5670` is now outside the deficient shore.  That transfer is not
globally incidence-monotone.

## 5. Exact+upper endpoint signature matrix

There are eight distinct target words among the eleven frozen split-pair
outputs with zero arbitrary-upper holes.  Replaying generalized Hall and then
restricting each graph to the fixed \(T_{229}\) shore gives:

| endpoint | full deficiency | deficiency on fixed 212-left shore | fixed components repaired |
|---|---:|---:|---|
| 151 | 26 | 22 | `091d,2e28,2f28` |
| 155 | 26 | 21 | `091d,2e28,2f28,4a29,6a29` |
| 162 | 26 | 22 | `091d,2e28,2f28` |
| 178 | 28 | 19 | `091d,291c,291d,2e28,2f28,4879` |
| **229** | **25** | **25** | none |
| 231 | 27 | 26 | none; `05a4` worsens to deficiency two |
| 233 | 26 | 18 | `0665,091d,291c,291d,2e28,2f28,4879` |
| 282 | 27 | 20 | `091d,291c,291d,2e28,2f28` |

Thus endpoint 233 supplies the largest local contraction, seven components,
but its full deficiency is 26.  Endpoint 155 is the only frozen macro in
this family that locally repairs both surviving old donor targets `4a29` and
`6a29`, but its full deficiency is also 26.

For every non-229 endpoint, every right cell fresh to the fixed 212-left shore
loses at least one old global candidate incidence.  Hence none of these rows
is a monotone Hall descent, despite their local contractions.  They provide a
finite cross-pair atom library, not a solved compiler.  A useful compound
switch must combine the provider losses of one endpoint with gains from
another, or isolate the two monotone late signatures in (4.2).

## 6. Corrected local influence and a three-component collar target

The two-block materialization is

```text
source packet A: [2186,2217), forward
source packet B: [1266,1295), reversed
destination body: [3786,3846)=A|rev(B)
changed joins: 1266,2157,3786,3817,3846
```

A cell profile is not determined merely by whether the cell interval crosses
a changed join.  Its exact target-row dependency window can have length up to
12.  Recomputing these closures exposes exactly two old shore cells:

| component | cell | interval | profile | dependency rows |
|---|---:|---|---|---|
| `30e0` | 11423 | `[3807,3810)` | `A=31e2, M=30e0` | `[3801,3813)` |
| `00cd` | 11561 | `[3853,3856)` | `A=12cd, M=00cc` | `[3847,3859)` |

The other 23 component profiles are guaranteed unchanged by an edit supported
on the declared packet/join rows, provided the three-flat depth schedule is
unchanged.  This is the corrected influence statement; interval overlap alone
would incorrectly expose only the first component.

The authenticated contextual 19-row collar has three distinct local role
cells for `8000`, `2665`, and `0665`.  In the frozen \(T_{229}\) matching,
there are 536 starts at which all three corresponding right-cell IDs are
unmatched.  Five lie near the active packet, and the three starts

```text
r=3772: cells 11337,11359,11361
r=3773: cells 11340,11362,11364
r=3822: cells 11487,11509,11511
```

avoid both protected dependency windows.  Starts 3837 and 3857 meet the
dependency closure of cell 11561 and therefore need an explicit reconstruction
of that matching edge.

If a source-compensated embedding at any clean start retains every old
matching edge and supplies the three collar incidences, the disjoint
augmenting paths are

```text
8000 -> Q_free,
2665 -> P_free,
1665 -> cell8696 ->[matched] 0665 -> S_free.
```

Hence that retained-matching embedding would prove

\[
             26307\longrightarrow26310,
             \qquad 25\longrightarrow\text{at most }22.             \tag{6.1}
\]

No such global embedding is claimed here.  Local collar replay and
matching-freeness do not by themselves preserve source occurrences, arbitrary
upper coverage, or the remaining matching edges.

## 7. Reproducibility and exact boundary

The independent light audit is

```text
scratch/audit_k16_exact229_hall_component_signatures_20260730.py
```

and emits

```text
scratch/ad_k16_bad2_splitpair_exact_20260730/
  exact_229.hall_components.k.audit.json
```

It independently reconstructs every maximal envelope, mandatory bit, proper
prefix cell, candidate incidence, maximum matching, canonical shore, and
connected component.  It also replays all eight distinct exact+upper endpoint
words and binds every input by SHA-256.

The corrected full-shore and clean-workspace audits are

```text
scratch/audit_k16_exact229_hall_shore_20260730.py
scratch/ad_k16_bad2_splitpair_exact_20260730/
  exact_229.hall_shore.k.audit.json

scratch/audit_k16_exact229_mfree_collar_workspace_20260730.py
scratch/ad_k16_bad2_splitpair_exact_20260730/
  exact_229.mfree_collar_workspace.audit.json
```

The frozen hashes are

```text
audit_k16_exact229_hall_component_signatures_20260730.py
  71e4de130bded5f7fa22a7a9f89d4a0bbb83f8b31b7ecb35b07253a3d8f06f0b
exact_229.hall_components.k.audit.json
  f3532a10f89422bbadc4fb981b490dd9d13a77cfdfa0604b66e63fd9d31ad25d
  payload 52a716554828240f8d3d6737ca5502b518cb7c2aefe175c3ebc1ac874c7c28ff
audit_k16_exact229_hall_shore_20260730.py
  9ff85e75088226696ad2fbb1853fbe84070b832e80ad5fb86da5a77c4fc08aeb
exact_229.hall_shore.k.audit.json
  bb346b39e0321ad45361442e7c6c1dc41bcff0866a0c87104a3e96a3065fe010
  payload b37da09ef947db9692683fae21aa6a7a7236dda05f51972d2d7c88214a1bee8f
audit_k16_exact229_mfree_collar_workspace_20260730.py
  3b44766dd713495caecb251730b3bb2953194c96f6ff131abffbd5c41b5d13e8
exact_229.mfree_collar_workspace.audit.json
  502a9aef3865f9248496a0232095a2a96ef407442326546481280966eb1cb884
  payload e648da92f5d17f8c535867f7bba1ba35067c606c7d78ba9d70969a6fadfd2c6c
audit_k16_exact229_paired_halo_seam_donor_atlas_20260730.py
  88fb75ffb462b59c7cc63567d3f533541e7ce59d5c432a0647513f486b36961d
exact_229.paired_halo_seam_donor.audit.json
  87128dc4dbde011d5d20b928d020a27d596a52162da063a4f83ef0d41c23f152
  payload cb2c3a18826f400e66df3d1c18431eaa15c38bf834d931cba146924b11c96116
```

What remains is sharply local but genuinely nontrivial: construct an
exact-middle and arbitrary-upper-safe cross-pair that retains old global
candidate incidences while importing fresh cells into distinct Hall-25
components.  No convergence or Hall pass is claimed.
