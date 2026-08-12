# Linear triangular fold braids: exact absorbers and the surviving recursion

## 1. Outcome

Let

\[
 \mathcal T_R=\{P_0=(0,0)\}\cup
 \{E_{s,y}=(s,y):1\le s\le R,\ 0\le y<s\},
 \qquad P_s=E_{s,0}.
\]

The target `(u,r,x)` is the bounding rectangle

\[
                         [u,r]\times[0,x],
 \qquad 0\le u<r\le R,\quad0\le x<r.                 \tag{1.1}
\]

The new `R=6` certificate has length 27.  Since

\[
                         |\mathcal T_6|=22,            \tag{1.2}
\]

it uses only five repetitions.  This disproves the proposed pattern

\[
 \rho(R)\stackrel{?}{=}
 \left\lfloor{(R-1)^2\over4}\right\rfloor,            \tag{1.3}
\]

whose right side is six at `R=6`.  A search with four repetitions remaining
one target short is not a lower bound.

More importantly, the certificate admits a short mathematical explanation.
It is the superposition of:

1. a length-15 strict-interior core on rows at most five;
2. one common ascending peak spine;
3. the new sixth-row arm; and
4. one omitted old cell parked harmlessly inside that new arm.

This note proves the general absorber theorem behind that decomposition and
an exact selective version of the fold lift.  Together they reduce a
linear-overhead all-`R` construction to a sharply stated core recursion.
That last recursion is not yet proved.

## 2. The outer scaffold has free parking capacity

Put

\[
                         A_x=E_{R,x}=(R,x),
                         \qquad1\le x<R.               \tag{2.1}
\]

For `1<=j<R`, let `H_j` be an arbitrary possibly empty word all of whose
cells `(s,y)` satisfy

\[
                         R-1\le s\le R,
                         \qquad0\le y\le j.            \tag{2.2}
\]

Consider the scaffold

\[
 \begin{split}
 \mathcal C_R(H)={}&P_0,P_1,\ldots,P_R,\\
 &A_1,H_1,A_2,H_2,\ldots,A_{R-1},H_{R-1}.
 \end{split}                                           \tag{2.3}
\]

### Lemma 1 (safe parking lemma)

Every target with `x=0` or `r=R` occurs in `C_R(H)`, regardless of the
parking words satisfying (2.2).

#### Proof

For `x=0`, use the peak interval `P_u,...,P_r`.

For a target `[u,R]x[0,x]` with `x>=1`, start at `P_u` and stop at `A_x`.
The peak segment supplies minimum first coordinate `u`, maximum first
coordinate `R`, and minimum height zero.  The cells `A_1,...,A_x` supply
maximum height `x`.

Only `H_j` with `j<x` lies before the stopping point.  Every one of its
cells has height at most `j<x` and first coordinate at least `R-1>=u`.
It therefore changes none of the four extrema.  QED.

In particular, old cells from row `R-1` can be inserted after the new arm
has already reached their height.  They then cost no additional occurrence:
they simultaneously satisfy the spanning requirement and act as clean
fillers for every new-row witness containing them.

## 3. A terminal suffix fan absorbs the entire `u=0` boundary

Let `V` be a word ending in `P_0`.  Say that `V` has a **suffix seed of
height `x` and reach `b_x`** when some suffix of `V` has bounding box

\[
                         [0,b_x]\times[0,x].           \tag{3.1}
\]

### Lemma 2 (suffix-fan absorber)

After appending the peak word

\[
                         P_1,P_2,\ldots,P_R,            \tag{3.2}
\]

a suffix seed `(x,b_x)` represents every target

\[
                         [0,r]\times[0,x]
                         \qquad(r\ge b_x).             \tag{3.3}
\]

#### Proof

Take the seed suffix and extend it through `P_1,...,P_r`.  The appended
cells all have height zero and first coordinates between zero and `r`.
They increase only the maximum first coordinate, from `b_x` to `r`.  QED.

Call the suffix fan **perfect through height `h`** when it has

\[
                         b_x=x+1
                         \qquad(1\le x\le h).          \tag{3.4}
\]

Such a fan absorbs every valid `u=0` target of those heights, because
validity itself says `r>=x+1`.

## 4. Exact core-to-full completion

Let `R>=2`.  A word `V` on rows at most `R-1` is an **`R`-completion core**
when:

1. `V` ends in `P_0`;
2. every target with
   \[
        1\le u<r\le R-1,\qquad1\le x<r             \tag{4.1}
   \]
   occurs in `V`;
3. `V` has a perfect suffix fan through height `R-2`;
4. `V` contains every nonpeak cell of `T_(R-1)` except a hole set `H`
   contained in row `R-1`.

Distribute every hole `E_(R-1,y)` exactly once into any parking word `H_j`
with `j>=y`, and put no additional entries into the parking words when using
the exact length ledger below.
Define

\[
 W=V\Vert(P_1,P_2,\ldots,P_R)\Vert
       (A_1,H_1,A_2,H_2,\ldots,A_{R-1},H_{R-1}).       \tag{4.2}
\]

### Theorem 3 (core completion theorem)

The word `W` is universal and contains every cell of `T_R`.

#### Proof

Partition the targets into four classes.

* If `x=0`, the terminal `P_0` of `V` followed by (3.2) is a complete peak
  spine, so the target is present.
* If `r=R`, Lemma 1 applies.
* If `u=0`, `r<=R-1`, and `x>=1`, the perfect suffix seed of height `x`
  followed through `P_r` represents the target by Lemma 2.
* The remaining targets have `u>=1`, `r<=R-1`, and `x>=1`, so they occur
  inside `V` by condition 2.

For spanning, `V` supplies every old nonpeak except `H` and supplies `P_0`.
The peak spine supplies `P_1,...,P_R`, the new arm supplies every `A_x`, and
the parking words supply exactly the holes.  QED.

This completion has no hidden additive loss.  Put

\[
 N_{R-1}^{\rm np}={(R-1)(R-2)\over2},                 \tag{4.3}
\]

the number of nonpeak cells in `T_(R-1)`, and define the core excess

\[
 \kappa(V,H)=|V|-\bigl(N_{R-1}^{\rm np}-|H|+1\bigr).  \tag{4.4}
\]

The subtracted quantity counts the compulsory old nonpeaks present in `V`
and its terminal `P_0`.  Every other occurrence in `V` is genuine overhead.
Direct counting in (4.2) gives

\[
                         |W|-|\mathcal T_R|
                         =\kappa(V,H).                 \tag{4.5}
\]

Thus the outer scaffold and every parked hole are literally free relative
to the spanning baseline.  A family of completion cores with
`kappa(V,H)=O(R)` would prove

\[
                         \rho(R)=O(R).                 \tag{4.6}
\]

## 5. The `R=6` certificate is exactly one core completion

Take

```text
V5 =
(5,4) (5,3) (4,2) (5,1) (4,0) (3,1) (2,1) (1,0)
(4,3) (4,1) (3,2) (3,0) (2,1) (1,0) (0,0).
```

It has length 15 and ends in `P_0`.  It contains every nonpeak cell of
`T_5` except

\[
                              H=\{E_{5,2}\}.           \tag{5.1}
\]

It covers every strict-interior target (4.1) for `R=6`.  This finite claim
has been checked by enumerating all intervals of `V5`; the exact checker is
`scratch/test_triangular_patterns.cpp`.

The following nested suffixes are a perfect suffix fan:

\[
\begin{array}{c|c|c}
x&\text{suffix begins at}&\text{bounding box}\\ \hline
1&E_{2,1}&[0,2]\times[0,1]\\
2&E_{3,2}&[0,3]\times[0,2]\\
3&E_{4,3}&[0,4]\times[0,3]\\
4&E_{5,4}&[0,5]\times[0,4].
\end{array}                                           \tag{5.2}
\]

Append `P_1,...,P_6`, then the sixth-row arm, parking `E_(5,2)` after the
arm has reached height three:

```text
(6,1) (6,2) (6,3) (5,2) (6,4) (6,5).
```

The resulting word is

```text
(5,4) (5,3) (4,2) (5,1) (4,0) (3,1) (2,1) (1,0)
(4,3) (4,1) (3,2) (3,0) (2,1) (1,0) (0,0)
(1,0) (2,0) (3,0) (4,0) (5,0) (6,0)
(6,1) (6,2) (6,3) (5,2) (6,4) (6,5).
```

By Theorem 3 this is a mathematical coverage certificate, not merely a
search output.  Its excess is

\[
 \kappa(V5,H)=15-(10-1+1)=5.                          \tag{5.3}
\]

Hence

\[
                              \boxed{\rho(6)\le5}.     \tag{5.4}
\]

No matching lower bound is claimed.

## 6. Selective fold lifting

The exact fold map is

\[
                         \phi_R(s,y)
                          =(s-1,\max\{y-1,0\}).        \tag{6.1}
\]

A nonzero lower peak `P_a` has two preimages:

\[
 L_a=P_{a+1},\qquad H_a=E_{a+1,1}.                    \tag{6.2}
\]

The full block lift copies both preimages at every occurrence.  That is
sufficient but unnecessary.

Fix one witnessing interval `J_S` in a lower word `W` for every lower target
`S`.  At every occurrence of a nonzero peak, choose one of the blocks

\[
                         [L_a],\qquad[H_a],
                         \qquad[L_a,H_a]               \tag{6.3}
\]

(the two-letter block may be reversed).  Replace `P_0` by `P_1`, and replace
every lower nonpeak by its unique preimage.

### Theorem 4 (selective fold criterion)

The resulting lifted word covers every positive-interior target in
`T_R` provided:

1. every selected lower witness contains a peak occurrence whose block
   includes a height-zero (`L`) preimage; the unique preimage of `P_0`
   counts as `L`;
2. every selected lower witness of height zero additionally contains a peak
   occurrence whose block includes an `H` preimage.

Its length is

\[
                         |W|+d,                        \tag{6.4}
\]

where `d` is the number of two-letter choices in (6.3).

If the lower word spans its lower alphabet and, for every lower label `P_a`
with `a>=1`, at least one occurrence supplies `L_a` and at least one supplies
`H_a`, then the lift contains the whole fibre over every lower cell and is
spanning outside `P_0`.

#### Proof

Span the replacement blocks belonging to `J_S`.  First-coordinate extrema
increase by one.  An `L` preimage supplies height zero.

If the lower target has positive maximum height, a cell attaining that
height is a nonpeak and its unique preimage increases the maximum height by
one.  If the lower maximum is zero, all its cells are peaks; an `H` preimage
supplies height one.  The two stated hitting conditions therefore give
exactly the required height extrema in both cases.  No replacement cell can
exceed them.  Formula (6.4) is immediate, and the spanning assertion follows
from the fold fibres.  QED.

This turns the vague phrase “choose peak preimages globally” into a finite
two-colour interval-hitting problem.  The expensive full block lift sets
`d` equal to every nonzero-peak occurrence.  A linear braid needs a witness
system and an `L/H` assignment with only `O(R)` double choices, followed by
the free scaffold completion of Theorem 3.

### 6.1 The fold difficulty is concentrated in one first-column backbone

There is an even simpler exact decomposition if height-one targets are
handled separately.  Define the **low lift**

\[
 \lambda_R(P_a)=P_{a+1},\qquad
 \lambda_R(E_{s,y})=E_{s+1,y+1}\quad(y\ge1).           \tag{6.5}
\]

It selects only the height-zero preimage of every lower peak.

### Lemma 5 (low-lift decomposition)

If a lower word `V` covers every positive-height target in `T_(R-1)`, then
`lambda_R(V)` covers every target

\[
            1\le u<r\le R,\qquad2\le x<r.             \tag{6.6}
\]

The word

\[
 X_R=E_{R,1},P_{R-1},E_{R-1,1},P_{R-2},\ldots,
                         E_{2,1},P_1                  \tag{6.7}
\]

covers every target

\[
            1\le u<r\le R,\qquad x=1.                \tag{6.8}
\]

If `V` contains every lower nonpeak, then the two words together contain
every upper nonpeak: the low lift supplies exactly the cells of height at
least two, and `X_R` supplies exactly the first column.

#### Proof

For (6.6), fold the target to
`[u-1,r-1]x[0,x-1]`.  Its lower height is positive.  A lower witness has a
peak, which the low lift sends to height zero, and a nonpeak of maximum
height `x-1`, which is sent to height `x`.  All first coordinates increase
by one.

For (6.8), start at `E_(r,1)` in (6.7) and stop at `P_u`.  The intervening
first coordinates descend from `r` to `u`, and their heights are zero or
one.  QED.

Thus the recursive obstacle is not an amorphous full fibre expansion.  It is
the following concrete braid:

> Interleave the compulsory first-column backbone `X_R` through the low
> lift of a lower positive word, without destroying its old lifted
> witnesses, and arrange the result as a perfect terminal suffix fan.

Both pieces consist of compulsory cells.  If this interleaving can be done
with only `O(1)` new portal occurrences per level—or directly with `O(R)`
total portal occurrences—then the edge-balanced cores of Section 8 follow.
Literal concatenation is valid but loses `Theta(R)` occurrences per level,
which is exactly the cost that the braid must eliminate.

### 6.2 Nested-shell parking preserves the suffix fan

The suffix constraint itself is not the obstruction.  Suppose a perfect fan
is written in diagonal-normalized form

\[
 D_hB_hD_{h-1}B_{h-1}\cdots D_1B_1P_0,
 \qquad D_x=E_{x+1,x},                                \tag{6.9}
\]

where the suffix beginning at `D_x` has box
`[0,x+1]x[0,x]`.

### Lemma 6 (nested-shell parking)

Arbitrary extra cells from `[0,x+1]x[0,x]` may be inserted into `B_x`
without destroying any of the chosen suffix boxes.

#### Proof

A suffix beginning at `D_j` with `j<x` starts after `B_x`, so it does not
see the insertion.  A suffix with `j>=x` contains it, but its target box
`[0,j+1]x[0,j]` contains `[0,x+1]x[0,x]`.  The four extrema already supplied
by the original suffix therefore do not change.  QED.

In particular, the first-column pair

\[
                         E_{x+1,1},P_x                \tag{6.10}
\]

fits safely in shell `B_x`.  Hence all letters of `X_R` have natural
zero-contamination homes in the nested fan.  The unsolved issue is purely
one of **corridor continuity**: consecutive shells are separated by the
diagonal cell `D_(x-1)`, whose height exceeds one and therefore breaks an
`x=1` witness.  The required braid must reconnect those shell-local pieces
with `O(R)` total portal occurrences while retaining the lifted witnesses.
This is more precise than asking for an arbitrary superposition.

## 7. Exact remaining recursion

Theorems 3 and 4 isolate the all-`R` target.

> **Linear fold-braid target.**  Construct, for every `R`, an
> `(R+1)`-completion core `V_R` with a top-row hole set `H_R`, a perfect
> terminal suffix fan, and
> \[
>                          \kappa(V_R,H_R)=O(R).        \tag{7.1}
> \]
> One sufficient recursive route is to selectively unfold a target-universal
> lower core so that the strict-interior witnesses satisfy the two-colour
> hitting criterion while deliberately omitted singleton fibres form
> parkable top-row holes.

This is strictly narrower than the earlier arbitrary portal search:

* strict-interior coverage is inherited through the exact fold;
* all `u=0` targets are absorbed by one nested suffix fan;
* all `r=R` and `x=0` targets are absorbed by one physical scaffold;
* top-row holes have zero excess cost by safe parking.

The data

\[
        \rho(3)\le1,\quad\rho(4)\le2,
        \quad\rho(5)\le4,\quad\rho(6)\le5            \tag{7.2}
\]

is compatible with linear growth.  It does not determine a formula.  In
particular, the heuristic near-misses with `R-2` repetitions are not
impossibility certificates, and neither `rho(R)=R-1` nor `rho(R)=R-2` should
be stated as established or even strongly supported without further cases.

The next mathematical lemma must track four coupled invariants: strict
target coverage, a perfect suffix fan, a top-row-only hole set, and the
linear core ledger.  Peak-fibre colouring alone cannot create a hole of
height at least two from a spanning lower word, because such cells have
singleton fold fibres.  Those holes require a deliberately nonspanning but
target-universal lower core.  An induction preserving all four invariants
would turn the exact fold from a reduction into the desired linear-overhead
recursion.

## 8. A sharper edge-balanced core conjecture

The three known completion cores have an unexpectedly exact size.  For
`S=3,4,5`, there is an `(S+1)`-completion core `V_S` with one top-row hole
and

\[
                         |V_S|={S(S+1)\over2}
                              =|E(K_{S+1})|,            \tag{8.1}
\]

so that

\[
                         \kappa(V_S,H_S)=S.            \tag{8.2}
\]

Besides `V_5` in Section 5, examples are

```text
V3 =
(3,2) (3,0) (2,1) (1,0) (2,1) (0,0)
H3 = {(3,1)}

V4 =
(4,3) (4,2) (4,0) (3,1) (2,1) (1,0)
(3,2) (3,0) (2,1) (0,0)
H4 = {(4,1)}
```

Direct interval enumeration verifies the core conditions.  They can also be
checked by the same nested-suffix argument used for `V_5`.

In all three cases:

* exactly one top-row nonpeak is omitted;
* one low arm `E_(2,1)` is repeated;
* the other excess positions are nonzero peak portals;
* the word ends in `P_0` and contains the nested diagonal suffix fan.

This motivates the precise conjecture

> **Edge-balanced core conjecture.**  For every `S>=3`, there is an
> `(S+1)`-completion core with one top-row hole and core excess exactly `S`.

By Theorem 3 it would imply the explicit linear bound

\[
                              \rho(R)\le R-1
                              \qquad(R\ge4).            \tag{8.3}
\]

The complete-graph edge count in (8.1), the fold fibres, and the nested
diagonal suffixes strongly suggest that the right induction should be an
edge-word braid rather than a literal block lift.  At present only
`S=3,4,5` is certified, so (8.3) remains conjectural.  The known `R=4`
length-13 word is one better than (8.3), showing that the conjectural family
need not be exactly optimal.
