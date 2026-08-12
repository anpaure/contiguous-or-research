# The fourth height-pentagon rail leaves only three middle-interval endpoints per height

**Date:** 2026-08-05  
**Method:** literal normalized-root calculus on the auxiliary `E4` shore;
no search or computation  
**Status:** unconditional target-support theorem on the explicit height
ladder.  The `E4` edge of the next height pentagon is the missing reflected
seam for every middle-interval target except three endpoint pairs at each
**non-top** height.  The top forced seam has no next pentagon and retains
its complete middle-interval family until a separate terminal rail is
planted.  Away from that top boundary, the remaining family is linear in
the ladder height, rather than quadratic or cubic.

## 1. Input residual

Keep the notation of
`MATH_THEOREM_PBBS_HEIGHT_SEAM_FAN_CALCULUS_AND_MIDDLE_INTERVAL_RESIDUAL_20260805.md`.
The forced old edge at the mountain state

\[
 A_b=[1,b]\cup T_b,
 \qquad
 T_b=\{2b+1,2b+3,\ldots,2r-1\},                         \tag{1.1}
\]

has the unresolved correct-rank target family

\[
 C_b(u,v)=[v+1,b-u-1]\cup T_b,
 \qquad
 v\ge1,\qquad u\ge0,\qquad u+v\le b-2.                \tag{1.2}
\]

The monotone height seam cannot realize (1.2), because its low part is
always a prefix beginning at coordinate `1`.

The needed reflected shore is already one of the five legal edges in the
**next** height pentagon.

## 2. The `E4` edge at height `b`

In the height-`b` pentagon, let

\[
 Z_4=Z_b^4,
 \qquad
 B_b=Z_b^0=g^{-1}A_b.                                   \tag{2.1}
\]

The fourth new pentagon edge is

\[
             U_{gZ_4}\longrightarrow U_{B_b}.           \tag{2.2}
\]

Using the literal five-survivor formulas and the common distinguished
deletion `b+1` of the height-`b` pentagon, put

\[
 E_b=T_b\cup\{2b+2\}.                                   \tag{2.3}
\]

Then its tail state is

\[
 G_b:=gZ_4=[2,b]\cup E_b,                               \tag{2.4}
\]

whereas

\[
 B_b=[2,b+1]\cup T_b.                                  \tag{2.5}
\]

Thus the central new edge already has the correct reflected left endpoint:
it deletes coordinate `1`, retains the complete tail `T_b`, and carries
only one harmless extra coordinate `2b+2`, which the head removes.

## 3. Stable positive history on the auxiliary rail

### Lemma 3.1 (balanced auxiliary peeling)

For `0<=s<=b-4`,

\[
 g^sG_b
   =[2,b-s]\cup[2b-s+1,2b]\cup E_b.                   \tag{3.2}
\]

Consequently,

\[
 J_b(a):=\bigcap_{s=0}^{a}g^sG_b
       =[2,b-a]\cup E_b
       \qquad(0<=a<=b-4).                               \tag{3.3}
\]

#### Proof

At stage `s`, the unique unmatched root is `2b-s`.  Cutting immediately
after it gives the Dyck word

\[
 1^{s+3}0(10)^{r-b-2}00\,1^{b-s-1}0^{b-1}.             \tag{3.4}
\]

The first displayed part has height `s+3`.  After its closing zero, the
unit tail, and the next two zeros, the baseline is `s`; the final up-run
has length `b-s-1` and therefore reaches the **absolute** height `b-1`.
The PBBS distinguished deletion remains the final-mountain coordinate
`b-s` exactly while

\[
                         b-1>s+3.                        \tag{3.5}
\]

For every transition needed to reach a state `s<=b-4`, inequality (3.5)
holds.  At the state `s=b-4`, the two peaks tie at height `b-1`; the
prefix peak occurs first, so the next transition leaves the peeling rail.
The successor therefore removes `b-s` and inserts the root `2b-s`, giving
(3.2) inductively.  Intersecting the states deletes the high end of the
low interval one coordinate at a time and proves (3.3). \(\square\)

The strict inequality in (3.5) explains the exact three-endpoint cutoff.
At the tie, the earlier height-`s+3` block wins the first-maximum rule, so
the same rail cannot simply be continued by a tie convention.

For `1<=s<=b-4`, the state in (3.2) contains `2`, `2b+1`, and `2b+2`,
while omitting `0,1`.  Its PBBS component has height `b-1`.  The
component-load census lists only

\[
 Z_{b-1}^0,\quad Z_{b-1}^2,\quad Z_{b-2}^1=A_{b-1},
 \quad Z_b^3,\quad Z_b^4                              \tag{3.6}
\]

as possible height-pentagon support states on that component.  The first
omits `2b+2`; the second contains `0`; the third contains `1`; and the last
two omit `2` (with `Z_b^3` also containing `1`).  Hence none equals an
interior state in (3.2).  The positive auxiliary history is therefore
retained literally after all simultaneous pentagon switches.

## 4. The inherited right history is the required reverse mountain ray

For `1<=t<=b-1`, the reverse mountain iterates are

\[
 g^{-t}A_b=[t+1,b+t]\cup T_b.                           \tag{4.1}
\]

Therefore, without the redundant central state `A_b`,

\[
 \bigcap_{t=1}^{v}g^{-t}A_b
      =[v+1,b+1]\cup T_b
      \qquad(1<=v<=b-1).                                \tag{4.2}
\]

The head in (2.2) is exactly the first state `g^(-1)A_b=B_b`, and its
unchanged outgoing PBBS arc supplies all later states in (4.2).

For `b>=4`, none of the states `g^(-t)A_b`, `2<=t<=b-1`, belongs to another
height-pentagon support slot.  Indeed they contain `2b+1`, omit `0`, and
omit `2`; the component-height census leaves only `Z_b^0=B_b` with the
first two properties, and that state contains `2`.  Thus the displayed
right histories are literal paths after the simultaneous switch.

## 5. Exact repair up to the last three endpoint pairs

### Theorem 5.1 (`E4` reflected-rail repair)

Let

\[
 v\ge1,\qquad u\ge0,\qquad u+v\le b-2,                \tag{5.1}
\]

and suppose

\[
                         u+1\le b-4.                    \tag{5.2}
\]

Assume also that the height-`b` pentagon belongs to the switched ladder;
equivalently, if the forced seams end at mountain `A_H`, require `b<=H-1`.

Then the old target `C_b(u,v)` has a target-equal, equal-width occurrence
on the final switched factor:

\[
 U_{g^{u+1}G_b},\ldots,U_{G_b},U_{B_b},
 U_{g^{-2}A_b},\ldots,U_{g^{-v}A_b}.                    \tag{5.3}
\]

#### Proof

The path (5.3) contains `u+v+2` owners, exactly as did the old interval
for `C_b(u,v)`.  By (3.3) and (4.2), the complement of its upper union is

\[
\begin{aligned}
 J_b(u+1)\cap\bigcap_{t=1}^{v}g^{-t}A_b
   &=([2,b-u-1]\cup E_b)
       \cap([v+1,b+1]\cup T_b)\\
   &=[v+1,b-u-1]\cup T_b\\
   &=C_b(u,v).
\end{aligned}                                           \tag{5.4}
\]

The tail-to-head step in (5.3) is the literal new `E4` edge (2.2); the
positive and negative interiors are retained by Lemma 3.1 and the support
observation after (4.2). \(\square\)

### Corollary 5.2 (three-pair residual)

At every non-top height `b<=H-1`, after combining the monotone height seams
with the `E4` auxiliary rail, the only unrepaired middle-interval pairs are

\[
 \boxed{
 (u,v)\in\{(b-4,1),(b-4,2),(b-3,1)\}.}                  \tag{5.5}
\]

#### Proof

Theorem 5.1 repairs `u<=b-5`.  In the residual (1.2), the remaining
integer pairs satisfy `u>=b-4`, `v>=1`, and `u+v<=b-2`.  Listing those
solutions gives exactly (5.5). \(\square\)

The bottom heights not covered by the stable inequality contribute only a
fixed finite family.  Across the **non-top** heights, the formerly
quadratic middle-interval leave has therefore fallen to at most
`3H+O(1)` named targets before using alternate old occurrences.  The top
family

\[
 \mathcal R_H=
 \{[v+1,H-u-1]\cup T_H:v\ge1, u\ge0, u+v\le H-2\}    \tag{5.6}
\]

is not covered by this count: adding one more full pentagon merely moves
the same boundary to the new top.

The three values themselves are

\[
 X_b^{23}=\{2,3\}\cup T_b,
 \qquad
 X_b^3=\{3\}\cup T_b,
 \qquad
 X_b^2=\{2\}\cup T_b.                                  \tag{5.7}
\]

Since

\[
                         T_{b+1}=T_b-\{2b+1\},           \tag{5.8}
\]

each fixed superscript in (5.7) is one strict nested chain as `b` grows.
Thus the residual is not `Theta(H)` unrelated defects: it is three
one-dimensional endpoint rays with a constant three-type interface.  The
two singleton rays are incomparable at each fixed height, so a repair by
nested suffix intersections needs at least two root states, but not one
independent gadget per height.

## 6. Exact frontier

The reflected rail is real, not a heuristic: it is one of the five edges
already paid for by the legal pentagon return, and it retains the literal
old reverse history needed by the target.

The three pairs (5.5) begin exactly where the auxiliary normalized root
changes which peak is globally first.  Therefore the next proof must
do one of the following:

1. identify the post-balance continuation with another auxiliary role
   (`E1`, `E2`, or `E3`);
2. splice to a second height seam at the balance point, as in the rigid
   `E1` residual-block theorem; or
3. prove that targets in (5.5) have unaffected alternate PBBS occurrences.

A tie-rule adjustment cannot extend Theorem 5.1: at equality the competing
peak occurs earlier in the normalized word and is forced by the PBBS
first-maximum definition.

## 7. Dependencies

Used:

* `MATH_THEOREM_PBBS_HEIGHT_SEAM_FAN_CALCULUS_AND_MIDDLE_INTERVAL_RESIDUAL_20260805.md`;
* `MATH_THEOREM_PBBS_AH_LADDER_PENTAGON_RETURN_20260805.md`;
* `MATH_THEOREM_PBBS_AH_PENTAGON_COMPONENT_LOAD_AND_REGENERATION_20260805.md`.

No multiplicity or generic shield theorem is used.
