# Audit of the shifted-eight support-three/support-four searches

## 1. Frozen inputs

This audit concerns

```text
scratch/k16_exact229_shifted8_natural_near_20260730.targets
  e8c720ef977b5f561c32d84c7c4a51e710999eab80d88bf814aa1f855b254f06

scratch/threadA_search_k16_shifted8_interacting_support3_20260730.cpp
  cbff65179543a2ce27a40fa52553bb2dd478aaff3d7f179655f5a114b46d9414

scratch/threadA_search_k16_shifted8_interacting_support4_20260730.cpp
  90af4d6a402ffdb33ac78dce2f47beb1c5f815558d299f3b0c5b47be530a4fb7

included geometry implementation
scratch/search_ad_k16_bad2_splitbuffer_pair_20260730.cpp
  65abf0532b0bbfced9041cbc3d22b48a66ffc7044525e412c37890a62c36d655
```

The input has length 12873, flats at 6320, 12869, 12871, no zero envelope,
no arbitrary-upper hole, and precisely one replay failure:

```text
row 3845: 6ba8 -> 69a8, missing 0200.
```

The numerical conclusions reported for the two runs are respectively 25910
and 6054792 tested cycles, with zero exact survivor.  The source-level audit
below verifies those catalogue sizes and identifies their exact theorem
boundary.  A final authenticated theorem should additionally freeze each run
log/output hash.

## 2. Exact protected-profile theorem

Let (E_i) be the maximal envelope at physical cell (i), under the fixed
depth-three schedule, and put

\[
 L=E_{4653},\quad X=E_{4654},\quad Y=E_{4655},\quad
 Z=E_{4656},\quad R=E_{4657},\quad S=E_{4658}.
\]

Direct replay gives

\[
 (X,Y,Z)=({\tt 6221},{\tt 4a21},{\tt 0a29}).             \tag{2.1}
\]

The complete component signatures, not merely their allowed unions, are

\[
 \begin{array}{c|c|c|c}
 \text{cell}&\text{interval}&\text{ordered envelopes}&M\\ \hline
 13964&[4654,4657)&(6221,4a21,0a29)&6809\\
 13966&[4655,4657)&(4a21,0a29)&4809.
 \end{array}                                             \tag{2.2}
\]

Here (M) is the mandatory mask.  For arbitrary simultaneous local edits
with the fixed depth schedule, the mandatory masks obey the exact identities

\[
 M_{13964}=(X\vee Y\vee Z)\wedge\neg(L\wedge R),          \tag{2.3}
\]

and

\[
 M_{13966}=(Y\vee Z)\wedge
 [ (\neg L\wedge\neg X)\vee(\neg X\wedge\neg R)
                    \vee(\neg R\wedge\neg S)].           \tag{2.4}
\]

All complements in (2.3)--(2.4) are clipped to sixteen coordinates.
Therefore the two cells are hard-protected if and only if (2.1) holds and
the right sides of (2.3), (2.4) equal `6809`, `4809` respectively.

The minimal functional target-row closures are

```text
cell 13964: rows 4650..4657,
cell 13966: rows 4650..4658,
joint:      rows 4650..4658,
```

with flat-status additionally checked on edges 4649..4658.  Thus an edit
disjoint from rows 4650 through 4658 automatically preserves both complete
profiles when the flat schedule is fixed.

### Proof of the mandatory formulas

For `[4654,4657)`, a carrier meeting the cell from a row on its left contains
(L), and a carrier meeting it from a row on its right contains (R).
Rows 4653 and 4654 show the converse.  Hence a bit in (X\vee Y\vee Z) is
mandatory exactly when (L) and (R) are not both one, proving (2.3).

For `[4655,4657)`, domination reduces the possible escaping carriers to the
three endpoint pairs ((L,X),(X,R),(R,S)).  A bit of (Y\vee Z) is mandatory
exactly when at least one of these pairs is `00`, which is (2.4).  The displayed
row closures follow by expanding the six envelopes in these formulas.  Each
endpoint is functionally necessary under a suitable simultaneous local edit.

### Consequence for row 4653

If all other protected-collar rows are fixed, replacing row 4653 by a rank-eight
mask (Q) preserves both complete profiles exactly when

\[
 Q={\tt 6a29}\vee b,
 \quad
 b\in\{{\tt 8000,1000,0400,0100,0080,0040,0010,0002}\}. \tag{2.5}
\]

Indeed (2.1) forces `Q` to contain `6a29` and excludes bit `0004`; the
mandatory equations then add no further condition because the one extra bit
lies outside both allowed unions.  The incumbent `6b29` is only the
`b=0100` member of this eight-mask fibre.

## 3. What the support-three program actually proves

The program fixes the incoming source at one of the nine positions

```text
437,6263,468,2206,3847,795,4652,3845,681
```

and tests cycles

\[
 3846\leftarrow d\leftarrow c\leftarrow3846              \tag{3.1}
\]

only when one of the three support pairs has distance at most six.

Two listed donors, 3845 and 3847, are adjacent to 3846, so each admits all
(12871) remaining compensators.  For each of the seven remote donors, the
root and donor radius-six collars are disjoint and contain 24 possible
compensators.  Hence

\[
 2(12871)+7(24)=25910.                                    \tag{3.2}
\]

Thus the reported zero-exact result is a valid no-go for exactly this
25910-cycle catalogue.

After this gap was reported, the unrestricted replacement

```text
scratch/threadA_search_k16_shifted8_unrestricted_interacting_support3_20260730.cpp
SHA-256 3ac35a2315c3af0705da8ec038adebbbbd325c1efbe49b2c132e4121381f6982
```

enumerated every ordered pair for which one of the three support distances is
at most six, with no donor restriction and with dynamic flats replayed in
full.  Its catalogue size is

\[
 12(2\cdot12872-12-1)
 +2[(6\cdot3840-21)+(6\cdot9020-21)]
 =308772+154236=463008.
\]

The reported exact count is zero.  Thus the interacting support-three gap is
now closed; the criticisms below describe the superseded `cbff6517...`
source and remain relevant to the analogous support-four pruning.

The superseded `cbff6517...` source was **not** the complete interacting
support-three shell:

1. The root has ten nearby `0200`-bearing source rows.  Besides the two listed
   sources 3845 and 3847, the program omits

   ```text
   3840,3841,3842,3848,3849,3850,3851,3852.
   ```

   Because the source edit itself lies in the root radius-six collar, the
   fixed-neighbour ten-token theorem does not apply to these eight rows.

2. In the current shifted word, `6b29` occurs at row 4653, not row 3846.
   It is omitted from the donor list.  Formula (2.5) shows seven nonincumbent
   physical return values that can replace it while preserving both protected
   profiles.  These are genuine three-cycle candidates, not excluded by the
   one-donor swap audit.

3. Fully separated return cycles (3.1) are outside the program by definition.
   Closing a transposition does not close such a three-cycle because the donor
   may receive a third token rather than `6939`.

The exact fixed-flat support-three quotient is nevertheless small.  Root the
cycle as

\[
3846\leftarrow s\leftarrow t\leftarrow3846.
\]

Every repair must put bit `0200` at row 3846.  Indeed, the `0200` trace on
rows 3842 through 3848 is `1001011`.  If row 3846 remains zero, the carrier
ending at 3845 requires both zero rows 3843 and 3844 to receive one-tokens,
while the carrier ending at 3847 requires both rows 3844 and 3846 to receive
one-tokens.  A three-cycle has too few old one-tokens in either required local
support; the other two possible carriers require at least as many changes.
The complete disjoint cases are therefore:

```text
(i)   s is root-near and has bit 0200; t arbitrary:       128710,
(ii)  s is root-far with bit 0200; t is root-near:         77124,
(iii) s is a root-far seam token; t is root-far:          102872.
```

Their total is 308706.  The unrun fail-closed generator

```text
scratch/threadA_k16_shifted8_protected_support3_quotient_20260730.cpp
```

implements this quotient, exact fixed-flat replay, both complete protected
signatures, unrestricted upper replay, and a full-Hall handoff.

## 4. Complete support-two floor

The old nine-donor audit was also not, by itself, a complete transposition
audit.  A transposition with a remote source is forced into the seam-token
language; a root-near source need only pass the interacting bit condition.
The union consists of 18 sources: eight root-far seam sources and ten
root-near `0200` sources.

The independent lightweight audit

```text
scratch/audit_threadA_k16_shifted8_complete_support2_20260730.cpp
scratch/threadA_k16_shifted8_complete_support2_20260730.audit.tsv
```

replays all 18.  None is middle-exact.  Their bad-row counts, in source order,
are

```text
4,7,2,1,4,11,11,10,2,3,4,7,11,11,13,3,1,2.
```

This proves, for the first time with the interacting exceptions included:

> Any occurrence-permutation repair of the shifted-eight word that preserves
> the two protected profiles has support at least three.

No upper or Hall conclusion is needed because all 18 candidates already fail
middle replay.

## 5. What the support-four program actually proves

Fix one of the same nine incoming donors and the rooted order

\[
 3846\leftarrow d\leftarrow x\leftarrow y\leftarrow3846. \tag{5.1}
\]

For each of the seven remote donors, the program includes every ordered pair
having an endpoint in the 24-position root/donor collar, together with every
ordered distance-at-most-six pair outside that collar.  There are

\[
 24(2\cdot12871-24-1)+2(6\cdot12847-3\cdot21)
 =617208+154038=771246                              \tag{5.2}
\]

pairs per donor.

For the adjacent donors 3845 and 3847, the active collar has 12 positions.
The program reports respectively two and one fixed-schedule-compatible remote
(x) values.  Thus their catalogue sizes are

\[
 12(2\cdot12871-12-1)+2(12858)=334464,
\]

and

\[
 12(2\cdot12871-12-1)+1(12858)=321606.                    \tag{5.3}
\]

Equations (5.2)--(5.3) give exactly

\[
 7(771246)+334464+321606=6054792.                          \tag{5.4}
\]

For the fixed flat schedule and the fixed nine incoming donors, the pair
generation is complete: either a remaining position enters the root/donor
collar, the two remaining positions interact with each other, or—only for an
already adjacent donor—the isolated root/donor partial replay is a necessary
condition.  The reported zero-exact result is therefore a valid no-go for
this precisely scoped catalogue.

It is not a complete support-four theorem:

1. It omits the same eight root-near incoming sources and the `6b29@4653`
   protected fibre from (2.5).

2. Support four need not contain row 3846.  For example, the carrier at cell
   3845 can in principle be made by changing rows 3843 and 3844 and importing
   two external `0200` tokens.  The source hard-wires row 3846 into every
   cycle and never represents this architecture.

3. The `partial_root_donor_ok` pruning uses the original depth schedule.
   It is necessary only when the flat set is fixed.  If (x,y) destroy and
   recreate a flat elsewhere, the depth offsets between the new and old flat
   positions change nonlocally.  A partial fixed-depth failure at the root is
   then not a necessary failure of the final dynamic schedule.  Consequently
   the claim that the quotient is complete while allowing dynamic flats is
   false.  Dynamic-flat exact candidates among the enumerated pairs are valid,
   but omitted pairs are not excluded.

4. The function `profile4` compares only the ordered envelopes
   `(6221,4a21,0a29)`.  It never checks mandatory masks `6809,4809`.
   Equations (2.3)--(2.4) show that ordered-envelope equality alone is not the
   full component signature.  This does not change a zero-exact count, but it
   invalidates the advertised hard-profile predicate for any future survivor.

## 6. Audited boundary

The strongest unconditional conclusions are:

1. the complete protected support-two shell is impossible;
2. the old support-three run closes its 25910-cycle frozen-nine catalogue,
   and the corrected `3ac35a...` run closes the full 463008-cycle interacting
   support-three catalogue;
3. the reported support-four run closes its exact 6054792-cycle fixed-nine,
   fixed-schedule interacting catalogue, but not arbitrary incoming sources,
   root-free four-cycles, or the dynamic-flat completion;
4. complete profile preservation is governed by (2.1), (2.3), and (2.4), not
   by the three ordered envelopes alone;
5. for support four with a second edited row in the root collar, the exact
   two-variable service relation compresses all local rank-eight assignments
   to 1195 value pairs and 1082 two-exterior-source occurrence pairs; see
   `MATH_THEOREM_K16_SHIFTED8_ROOT_COLLAR_PAIR_RELATION_20260730.md`.

No claim about support at least four, no dynamic-flat support-four no-go, and
no Hall descent follows from the two existing searches.
