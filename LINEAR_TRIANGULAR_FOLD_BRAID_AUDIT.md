# Audit of `LINEAR_TRIANGULAR_FOLD_BRAID.md`

## 1. Verdict

The principal finite construction and the two local lifting lemmas are
correct.

* Safe parking is correctly indexed.  Because `H_j` occurs **after**
  `A_j`, a witness stopping at `A_x` contains only `H_j` with `j<x`.
  The stated height bound `y<=j` is therefore sufficient.  It is actually
  one unit more restrictive than necessary.
* The suffix-fan lemma, including `x=1` and `r=b_x`, is correct.
* The four target classes in the core-completion proof are exhaustive and
  the displayed witnesses are valid.  To be a literal partition, the
  second class should say `r=R,x>=1`, since `r=R,x=0` was already assigned
  to the first class.
* The length identity `|W|-|T_R|=kappa(V,H)` is correct provided the parking
  words contain exactly one occurrence of each hole and no other entries.
* Every stated `V5` property and the final `R=6` certificate pass independent
  interval enumeration.
* The selective fold coverage criterion and length formula are correct.
  Complete endpoint blocks create no contamination.

Three qualifications are needed.

1. The selective lift's spanning conclusion requires the lower word `W` to
   span the lower triangle.  The colour condition alone supplies only the
   two-point peak fibres; it cannot supply a missing singleton nonpeak fibre.
2. To turn a selective lift into a completion core, every omitted nonpeak
   fibre must be in the permitted top row.  Arbitrary unused `H_a` fibres are
   not automatically parkable holes.
3. “Equivalently” in Section 7 is best read as a proposed recursive route,
   not as a consequence of Theorems 3 and 4 alone: the suffix fan, terminal
   `P_0`, top-row location of holes, and `O(R)` core ledger still have to be
   maintained simultaneously.

With those corrections, the note gives a rigorous `rho(6)<=5` theorem and a
useful selective-fold framework.

## 2. Safe-parking audit

Recall the physical order

\[
 P_0,P_1,\ldots,P_R,
 A_1,H_1,A_2,H_2,\ldots,A_{R-1},H_{R-1},             \tag{2.1}
\]

where `A_x=(R,x)`.

For a target `(u,R,x)` with `x>=1`, the proposed interval starts at `P_u`
and ends at `A_x`.  Its nonparking entries have extrema

\[
                         [u,R]\times[0,x].            \tag{2.2}
\]

Since `H_j` follows `A_j`, that interval contains `H_j` exactly when
`j<x`.  Under the source hypothesis, every such parked cell has

\[
 R-1\le s\le R,qquad0\le y\le j<x.                 \tag{2.3}
\]

Because `u<=R-1`, its first coordinate lies inside `[u,R]`; its height is
strictly below `x`.  It changes no extremum.  For `x=0`, the selected
interval stays entirely inside the peak spine and sees no parking word.
Lemma 1 is correct.

### Sharpening 1 (the maximal safe height)

The placement after `A_j` permits the weaker condition

\[
                         y\le j+1                    \tag{2.4}
\]

for `j<=R-2`.  Indeed, the first new-row witness that contains `H_j` stops
at `A_(j+1)`, so height `j+1` is already allowed.  The terminal word
`H_(R-1)` is not used by any of these witnesses at all and needs no height
restriction for Lemma 1 beyond being a legal alphabet word.

Thus a row-`R-1` hole `E_(R-1,y)` can safely be parked as early as
`H_(y-1)` when `y>=2`, rather than only in some `H_j` with `j>=y`.
The source's rule is conservative, not erroneous.

## 3. Suffix-fan audit

Let a suffix of `V` have bounding box

\[
                         [0,b_x]\times[0,x],          \tag{3.1}
\]

and recall that `V` ends at `P_0`.  After appending `P_1,...,P_R`, extend
the suffix through `P_r`.  If `r>=b_x`, the appended peaks have first
coordinates in `[0,r]` and height zero, so they change only the maximum
first coordinate, from `b_x` to `r`.  The resulting box is exactly

\[
                         [0,r]\times[0,x].            \tag{3.2}
\]

Equality `r=b_x` is harmless: the maximum simply stays fixed.  For a
perfect fan `b_x=x+1`, every valid target has `r>x`, hence
`r>=x+1=b_x`.  In the completion theorem, `r<=R-1` implies
`x<=R-2`, so a fan through height `R-2` covers every needed boundary case.

Lemma 2 is correct.

## 4. Core-completion audit

Use the following disjoint target partition:

1. `x=0`;
2. `x>=1,r=R`;
3. `x>=1,r<=R-1,u=0`;
4. `x>=1,r<=R-1,u>=1`.

The source's bullets prove these four classes in order; only the word
“partition” needs the explicit `x>=1` qualification in class 2.

### Class 1

The final `P_0` of `V` followed by `P_1,...,P_R` is a contiguous ascending
peak spine.  Its subinterval `P_u,...,P_r` gives `(u,r,0)`.

### Class 2

This is exactly the safe-parking witness of Section 2.

### Class 3

Here `1<=x<r<=R-1`, so `x<=R-2`.  Use the perfect suffix seed and extend
through the appended `P_r`, as in Section 3.

### Class 4

These are precisely the targets required inside the core by condition 2.

Thus the coverage theorem is correct.

For spanning:

* `V` gives `P_0` and every old nonpeak except the holes;
* the appended spine gives `P_1,...,P_R`;
* `A_1,...,A_(R-1)` give every new-row nonpeak; and
* the parking words give the old holes.

No old peak other than `P_0` is required inside `V`.

## 5. Exact length ledger

The number of old nonpeaks is

\[
             N_{R-1}^{\rm np}=\sum_{s=2}^{R-1}(s-1)
                              ={(R-1)(R-2)\over2}.    \tag{5.1}
\]

Write

\[
 |V|=\kappa+N_{R-1}^{\rm np}-|H|+1.                 \tag{5.2}
\]

If the parking words together contain every hole exactly once and contain
no additional entries, then

\[
\begin{aligned}
 |W|
 &=|V|+R+(R-1)+|H|\\
 &=\kappa+{(R-1)(R-2)\over2}+2R\\
 &=\kappa+1+{R(R+1)\over2}\\
 &=\kappa+|\mathcal T_R|.                            \tag{5.3}
\end{aligned}
\]

Equation (4.5) is therefore correct under this exact-parking convention.
The phrase “distribute every hole” should be interpreted as:

> place exactly one occurrence of every member of `H` among the parking
> words, and place nothing else there for the purpose of the length claim.

If extra fillers or repeated holes are included, coverage remains valid but
their number must be added to the right side of (4.5).

## 6. Independent audit of the `V5` and `R=6` claims

The core is

```text
(5,4) (5,3) (4,2) (5,1) (4,0) (3,1) (2,1) (1,0)
(4,3) (4,1) (3,2) (3,0) (2,1) (1,0) (0,0)
```

### 6.1 Length, terminal cell, and spanning inventory

It has length 15 and ends in `P_0`.  The ten nonpeaks of `T_5` are

\[
 E_{2,1};\quad E_{3,1},E_{3,2};\quad
 E_{4,1},E_{4,2},E_{4,3};\quad
 E_{5,1},E_{5,2},E_{5,3},E_{5,4}.                    \tag{6.1}
\]

Every one occurs in `V5` except `E_(5,2)`; `E_(2,1)` occurs twice.  Thus
the asserted hole set is exact.

### 6.2 Strict-positive coverage

Compiling `scratch/test_triangular_patterns.cpp` with C++ and running its
independent interval enumeration gives

```text
V5 positive miss=3
 missing(0,4,1) missing(0,5,1) missing(0,5,2)
V5 strict-positive miss=0
```

The three positive targets missing from `V5` all have `u=0`, so they are
outside core condition 2 and are exactly of the type delegated to the
suffix fan.  Every target with

\[
                         1\le u<r\le5,\quad1\le x<r  \tag{6.2}
\]

is present.

### 6.3 Perfect suffix fan

The suffixes begin at the following physical occurrences:

* the **last** `E_(2,1)` for `x=1`;
* `E_(3,2)` for `x=2`;
* `E_(4,3)` for `x=3`; and
* `E_(5,4)` for `x=4`.

Reading each suffix through the terminal `P_0` gives respectively

\[
 [0,2]\times[0,1],\quad[0,3]\times[0,2],\quad
 [0,4]\times[0,3],\quad[0,5]\times[0,4].             \tag{6.3}
\]

The table (5.2) is correct; disambiguating the last `E_(2,1)` removes the
only notational ambiguity.

### 6.4 Parking and final verification

The hole `E_(5,2)` is placed in `H_3`, after `A_3=(6,3)`.  It satisfies the
source's conservative bounds `s=R-1,y=2<=3`.

The resulting word has `15+6+6=27` entries.  An independent generic
bounding-box checker reports

```text
SUMMARY missing=0 alphabet_valid=1 span=1 distinct_cells=22/22
```

Since `|T_6|=22`, its excess is five.  The calculation

\[
 \kappa(V5,H)=15-(10-1+1)=5                         \tag{6.4}
\]

and the rigorous conclusion `rho(6)<=5` are correct.  No computation is
being used as an impossibility certificate.

## 7. Selective-fold coverage audit

Fix a selected lower witness `J`.  Replace each of its lower occurrences by
the chosen block and take the upper interval from the beginning of the first
replacement block through the end of the last.  In particular, both
endpoint blocks are included **completely**.

Every upper preimage of a lower cell `(s,y)` has first coordinate `s+1`, so
the first-coordinate extrema translate exactly by one.

### Positive lower height

Suppose the lower maximum height is `x'>0`.  A lower nonpeak attaining
height `x'` has the unique upper preimage of height `x'+1`.  Every other
lower nonpeak lifts to height at most `x'+1`; every `H` peak preimage has
height one.  Since the desired upper maximum is `x'+1>=2`, no `H` choice
contaminates it.  Condition 1 supplies an `L` preimage of height zero, so
the upper height extrema are exactly `0,x'+1`.

### Zero lower height

Now every lower occurrence in the witness is a peak, and the desired upper
height interval is `[0,1]`.  Condition 1 supplies an `L` and condition 2 an
`H`.  Every selected peak block has height zero, one, or both, so the extrema
are exactly `0,1`.

This also covers lower witnesses meeting `P_0`: its unique preimage `P_1`
is an `L`.  Every zero-height lower target has positive maximum first
coordinate `r'>0`, hence contains at least one nonzero peak at which an `H`
may be chosen.

### Endpoint-block contamination

There is none in Theorem 4.  A double endpoint block contributes only two
preimages of the same lower peak.  They have the same translated first
coordinate and heights zero and one.  For a positive lower target, height
one is below the desired maximum; for a zero-height lower target, it is the
desired maximum.  Because the full endpoint block is selected, reversing
its internal order changes no extremum and does not cross into a block
outside the lower witness.

Theorem 4's coverage criterion is therefore correct.

Each lower occurrence contributes one upper letter, plus one precisely when
it receives a double block.  Hence

\[
                         |\widetilde W|=|W|+d          \tag{7.1}
\]

is also correct.

## 8. Selective-fold spanning correction

The source states that supplying at least one `L_a` and one `H_a` for every
nonzero lower peak label yields a word spanning outside `P_0`.  This needs
one additional premise:

\[
                         W\text{ spans }\mathcal T_{R-1}. \tag{8.1}
\]

The label-colour condition supplies both elements of every two-point peak
fibre.  It says nothing about a lower nonpeak label absent from `W`; such a
label has a unique upper preimage, which would remain absent.  Under (8.1),
all singleton fibres occur, lower `P_0` supplies upper `P_1`, and the stated
`L/H` condition supplies both members of every nonzero-peak fibre.  The
correct conclusion then is exactly

\[
                         \mathcal T_R\setminus\{P_0\}. \tag{8.2}
\]

In the global triangular problem the lower words are normally required to
be spanning, so this is likely intended; it should nevertheless be explicit
in the standalone theorem.

## 9. Scope of the remaining recursion

Theorems 3 and 4 do not by themselves prove the “equivalently” sentence in
Section 7.  A selective lift becomes an `(R+1)`-completion core only after
all of the following additional properties are secured:

1. it contains or is extended by a terminal `P_0`;
2. it has a perfect terminal suffix fan through the required height;
3. every missing nonpeak fibre lies in the top row allowed for the core
   hole set;
4. its total occurrence ledger satisfies `kappa=O(R)`; and
5. the witness-hitting conditions remain valid after whatever ordering is
   used to create properties 1--3.

In particular, omitting `H_a=E_(a+1,1)` for an arbitrary lower label `a`
creates a missing nonpeak in row `a+1`.  It is parkable by Theorem 3 only if
that row is the core's permitted top row.  Missing `L_a=P_(a+1)` is less
serious because the outer completion spine supplies all peaks, but it still
affects the selective witness conditions.

There is a second distinction for top-row holes of height at least two.  In
the selective lift as stated, every lower nonpeak occurrence is replaced by
its unique preimage, so a **spanning** lower word necessarily supplies all
of those singleton fibres.  The only top-row nonpeak that can be omitted by
an `L/H` colour choice is `H_(R-1)=E_(R,1)`.  A hole
`E_(R,y)` with `y>=2` corresponds to the singleton lower label
`E_(R-1,y-1)`; producing such a hole requires that label to be absent from
the lower word, or requires an additional omission operation not present in
Theorem 4.  The `V5` hole `E_(5,2)` is exactly of this singleton-fibre type
when viewed as a fold from dimension four.

Accordingly, the recursion may naturally use lower words that are target-
universal but deliberately nonspanning, with their missing singleton labels
tracked as future top-row holes.  That is compatible with the core program,
but it is a further invariant beyond the selective colour theorem.

The finite certificate exhibits exactly this behaviour.  Delete the final
`P_0` from `V5` and fold its other fourteen entries.  By the exact target
quotient it is universal on `T_4`; its distinct-cell inventory is all of
`T_4` except `E_(4,1)`.  The unique upper preimage of that missing singleton
is `E_(5,2)`, exactly the hole of `V5`.  This is positive evidence for the
nonspanning-core invariant, not a consequence of the colour criterion alone.

Thus selective unfolding is a promising **sufficient construction route**
to the stated linear fold-braid target.  The remaining inductive theorem is
precisely the simultaneous preservation of the suffix fan, top-row-hole
condition, and linear `kappa` ledger.  None of those is supplied merely by
solving the two-colour interval-hitting conditions.

## 10. Safe theorem summary

The defensible result is:

> An `R`-completion core with exact hole parking completes to a universal
> spanning word with no excess beyond its core excess.  The displayed
> `V5` is such a core and proves `rho(6)<=5`.  Separately, the complete-block
> spans of a fixed lower witness system preserve all strict-interior targets
> when they receive the stated `L` and `H` hits; complete endpoint blocks are
> safe, and the added length is the number of double blocks.

The open theorem is:

> Construct selective lifts whose missing nonpeaks are top-row holes and
> whose terminal suffix fans and core excess remain controlled by `O(R)`.

That theorem would establish the desired linear repetition bound.  It has
not yet been proved.

---

## 11. Incremental audit of Section 6.1: the low lift

Section 6.1 was added after the preceding audit.  Its map is

\[
 \lambda_R(P_a)=P_{a+1},\qquad
 \lambda_R(E_{s,y})=E_{s+1,y+1}\quad(y\ge1).          \tag{11.1}
\]

It chooses the height-zero member of every lower peak fibre and the unique
member of every positive-height singleton fibre.

### 11.1 Target coverage

Take an upper target

\[
 1\le u<r\le R,\qquad2\le x<r.                       \tag{11.2}
\]

The folded parameters are

\[
             u'=u-1,\qquad r'=r-1,\qquad x'=x-1.     \tag{11.3}
\]

They satisfy

\[
 0\le u'<r'\le R-1,qquad1\le x'<r'.                \tag{11.4}
\]

Thus the requested lower target is among the positive-height targets
covered by `V`.  A lower witness has a peak, which (11.1) sends to height
zero, and a nonpeak of maximum height `x'`, which it sends to height
`x'+1=x`.  Every first coordinate increases by one, and no lifted height
exceeds `x`.

This checks all edge cases:

* `u=1` simply gives the legal lower boundary `u'=0`;
* `x=2` gives the legal first positive lower height `x'=1`;
* `r=R` gives `r'=R-1`; and
* `x<r` gives `x-1<r-1`, so no top-height boundary is lost.

The first assertion of Lemma 5 is correct.

### 11.2 The first-column backbone

Write the word in indexed pairs:

\[
 X_R=\mathop{\Vert}_{k=R,R-1,\ldots,2}
                    \bigl(E_{k,1},P_{k-1}\bigr).      \tag{11.5}
\]

For `(u,r,1)`, start at `E_(r,1)` and stop at `P_u`.  The actual interval is

\[
 E_{r,1},P_{r-1},E_{r-1,1},P_{r-2},\ldots,
 E_{u+1,1},P_u.                                      \tag{11.6}
\]

Its first coordinates lie between `u` and `r` and attain both; its heights
are zero and one and attain both.  This includes the shortest boundary case
`(u,r)=(1,2)`, whose witness is simply `E_(2,1),P_1`.

Hence the second assertion of Lemma 5 is correct.

### 11.3 Exact nonpeak inventory

The lower nonpeaks are precisely

\[
                         E_{s,y},\quad2\le s\le R-1,
                         \quad1\le y<s.               \tag{11.7}
\]

Their low lifts are precisely all upper nonpeaks of height at least two:

\[
 E_{s+1,y+1},\quad3\le s+1\le R,\quad2\le y+1<s+1. \tag{11.8}
\]

This is a bijection.  Separately, `X_R` contains each first-column nonpeak

\[
                         E_{2,1},E_{3,1},\ldots,E_{R,1} \tag{11.9}
\]

exactly once.  The two families are disjoint and exhaust every upper
nonpeak.  Numerically,

\[
 { (R-1)(R-2)\over2}+(R-1)={R(R-1)\over2}.           \tag{11.10}
\]

Thus the inventory statement is correct under its explicit premise that
`V` contains every lower nonpeak.

There is also a useful hole-preserving extension.  If `V` omits a lower
top-row nonpeak `E_(R-1,y)`, its low lift omits exactly

\[
                         E_{R,y+1},                   \tag{11.11}
\]

which is again a top-row nonpeak.  All other singleton fibres and the whole
first column are still supplied.  Therefore low lifting naturally transports
top-row holes upward by increasing their height by one.  The hypothesis and
conclusion in the source are correct; (11.11) is the version relevant to the
nonspanning completion cores.

### 11.4 Scope of the braid consequence

The low lift and `X_R` consist of letters whose **nonpeak types** are all
needed in a spanning core.  The peaks in `X_R`, however, are portal
occurrences inside the core and contribute to `kappa`, because the outer
completion later appends the compulsory peak spine again.  Consequently,
“both pieces consist of compulsory cells” should not be read as saying that
every occurrence in their literal concatenation is free in the core ledger.

Likewise, an interleaving with `O(1)` additional portal occurrences per
level establishes a recurrence of the form

\[
                         \kappa_R\le\kappa_{R-1}+O(1), \tag{11.12}
\]

and hence `kappa_R=O(R)`.  It does not by itself establish the exact
edge-balanced identity `kappa_R=R`.  For that, the incremental ledger must
be controlled exactly (in the evident normalization, one net new overhead
position per level), or compensated by an explicitly proved saving.

Thus Section 6.1 correctly isolates the first-column corridor problem and
would suffice for the desired linear asymptotic construction.  The phrase
“then the edge-balanced cores of Section 8 follow” is too strong if
“edge-balanced” means the exact size and excess in (8.1)--(8.2); only the
linear-order conclusion follows from an unspecified `O(1)` increment.

Literal concatenation `lambda_R(V)||X_R` is valid for the two strict target
classes and for the stated nonpeak inventory.  It is not by itself a
completion core: it ends in `P_1`, not `P_0`, and no perfect terminal suffix
fan follows merely from concatenation.  Those are exactly the additional
braiding requirements stated later in the section.

### 11.5 Nested-shell lemma

Lemma 6 is also correct.  An insertion in `B_x` is invisible to suffixes
starting later at `D_j`, `j<x`, and lies inside the already attained box of
every suffix starting at `D_j`, `j>=x`.  The pair
`E_(x+1,1),P_x` lies in `[0,x+1]x[0,x]`, so all `X_R` pairs have safe
shell-local homes.

One sentence needs a small boundary qualification: the separator
`D_(x-1)` has height `x-1`, which exceeds one only for `x>=3`.  At the
lowest seam `x=2`, `D_1=E_(2,1)` still has height one and does not itself
break an `x=1` corridor.  The general corridor-continuity obstruction for
the higher shells remains valid.

## 12. Incremental audit of the finite edge-balanced cores

For an `(S+1)`-completion core, the old triangle is `T_S`, so

\[
 N_S^{\rm np}={S(S-1)\over2}.                         \tag{12.1}
\]

With one top-row hole, the compulsory core baseline is

\[
                         N_S^{\rm np}-1+1
                         ={S(S-1)\over2}.             \tag{12.2}
\]

Therefore a word of length `S(S+1)/2` has

\[
                         \kappa={S(S+1)\over2}
                                  -{S(S-1)\over2}=S.  \tag{12.3}
\]

The size/excess equivalence in Section 8 is algebraically correct.

### 12.1 The `S=3` core

```text
V3 = (3,2) (3,0) (2,1) (1,0) (2,1) (0,0)
H3 = {(3,1)}
```

* It has length `6=3*4/2` and ends in `P_0`.
* The nonpeaks of `T_3` are `E_(2,1),E_(3,1),E_(3,2)`.
  It contains all except the top-row hole `E_(3,1)` and repeats
  `E_(2,1)`.
* Its suffix beginning at the last `E_(2,1)` has box
  `[0,2]x[0,1]`; its full suffix beginning at `E_(3,2)` has box
  `[0,3]x[0,2]`.  Hence it has the required perfect fan through height two.
* Independent enumeration reports `V3 strict-positive miss=0`.

Thus it is a valid `4`-completion core and `kappa=3`.

### 12.2 The `S=4` core

```text
V4 =
(4,3) (4,2) (4,0) (3,1) (2,1) (1,0)
(3,2) (3,0) (2,1) (0,0)
H4 = {(4,1)}
```

* It has length `10=4*5/2` and ends in `P_0`.
* It contains every nonpeak of `T_4` except the top-row hole
  `E_(4,1)`; `E_(2,1)` occurs twice.
* The suffixes beginning at the last `E_(2,1)`, at `E_(3,2)`, and at
  `E_(4,3)` have boxes `[0,2]x[0,1]`, `[0,3]x[0,2]`, and
  `[0,4]x[0,3]` respectively.
* Independent enumeration reports `V4 strict-positive miss=0`.

Thus it is a valid `5`-completion core and `kappa=4`.

### 12.3 The `S=5` core

The `V5` inventory, strict-positive coverage, suffix fan, and hole
`H5={E_(5,2)}` were independently certified in Section 6 of this audit.
It has length `15=5*6/2` and `kappa=5`.

Across all three examples, the source's qualitative inventory is correct:

* there is exactly one omitted top-row nonpeak;
* `E_(2,1)` is the unique repeated low arm type;
* after subtracting the present distinct nonpeaks and terminal `P_0`, every
  other overhead occurrence is a nonzero peak; and
* the words end in `P_0` with the displayed nested diagonal suffix fans.

## 13. Conjectural implication

Assume the edge-balanced core conjecture for every `S>=3`.  Apply the
already audited core-completion theorem with

\[
                         R=S+1.                       \tag{13.1}
\]

It produces a universal spanning word on `T_(S+1)` whose excess equals the
core excess `S`.  Relabeling `S+1` as `R` gives

\[
                         \rho(R)\le R-1\qquad(R\ge4). \tag{13.2}
\]

The implication is exact and correctly indexed.  It remains conditional
because cores are certified only for `S=3,4,5`.

Finally, `|T_4|=11`, so the known length-13 word has excess two, one below
the conjectural family bound `R-1=3`.  The source's observation that the
edge-balanced family need not be pointwise optimal is correct.

## 14. Incremental safe summary

The new proved material may safely be stated as follows:

> Low lifting carries every lower positive-height witness to an upper
> witness of height at least two.  The explicit alternating backbone `X_R`
> covers every strict height-one target, and together their nonpeak
> inventories are exact.  Top-row singleton holes shift to top-row holes.
> The displayed `V3,V4,V5` words are genuine completion cores with
> `kappa=3,4,5`.

The conjectural step is:

> Braid the low lift and first-column backbone while preserving the nested
> suffix fan, top-row hole, strict witnesses, and the **exact** one-unit
> growth of core excess.

An `O(1)` overhead theorem would already prove `rho(R)=O(R)`; the sharper
bound `rho(R)<=R-1` requires the exact edge-balanced ledger.
