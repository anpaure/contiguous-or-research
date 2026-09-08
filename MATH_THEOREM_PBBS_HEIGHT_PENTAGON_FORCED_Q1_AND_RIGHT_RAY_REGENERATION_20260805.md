# High PBBS height pentagons regenerate their complete `q1` palette and all one-sided right rays

**Date:** 2026-08-05  
**Method:** literal PBBS successor formulas and set complements; no search or
computation  
**Status:** unconditional for the explicit height pentagons.  At every
height `h>=4`, the complete old `q1` upper palette is recreated by the five
new pentagon edges, and every upper witness which uses only the endpoint
owner on its incoming side is transported exactly.  At heights `2,3`, the
unique old `q1` occurrence forced into the selected ladder cut is still
recreated.  Thus the complete ladder has at most ten unresolved `q1` target
values, all at the two bottom pentagons.  Two-sided exterior penetration
remains open.

## 1. Setup

Use the notation of
`MATH_THEOREM_PBBS_AH_LADDER_PENTAGON_RETURN_20260805.md`.  Thus

\[
 n=2r+1,
 \qquad Z_i=Z_h^i\quad(i\in\mathbb Z_5),
 \qquad Q_i=[n]\setminus Z_i,
\]

and the matching exchange replaces

\[
                         P_iQ_i\longleftrightarrow P_iQ_{i+1},
 \qquad P_i=[n]\setminus g(Z_i),                       \tag{1.1}
\]

where `g=f^2` is the centered PBBS successor.  The first two exchange
states are

\[
 Z_0=L_h+\{c,a\},
 \qquad
 Z_1=L_h+\{z_1,c\},                                    \tag{1.2}
\]

with

\[
 z_0=0,
 \qquad z_1=1,
 \qquad c=2,
 \qquad a=2h+1.                                        \tag{1.3}
\]

Put

\[
                              p=h+1.                    \tag{1.4}
\]

The literal word for `L_h` shows that `p` belongs to `L_h`.

## 2. Two consecutive PBBS successors delete the same coordinate

The normalized roots at the first two roles are

\[
\begin{aligned}
 D_h^0&=1^h0^{h-1}(10)^{r-h}0,\\
 D_h^1&=1^{h+1}0^{h+1}(10)^{r-h-1}.
\end{aligned}                                           \tag{2.1}
\]

In both rows the first up-step reaching the global maximum is the physical
coordinate `p=h+1`.  Their unmatched root zeros are respectively `z_1`
and `z_0`.  The distinguished-deletion PBBS formula therefore gives

\[
 g(Z_0)=Z_0-\{p\}+\{z_1\},
 \qquad
 g(Z_1)=Z_1-\{p\}+\{z_0\}.                              \tag{2.2}
\]

This is the key special feature of the first height-pentagon arrow: the
exchange changes the root zero, while the PBBS deletion coordinate remains
fixed.

### 2.1 At height at least four all five roles delete the same coordinate

The five normalized roots are

\[
\begin{aligned}
 D_h^0&=1^h0^{h-1}(10)^{r-h}0,\\
 D_h^1&=1^{h+1}0^{h+1}(10)^{r-h-1},\\
 D_h^2&=(10)^{r-h-1}1101^{h-1}0^h,\\
 D_h^3&=1(10)^{r-h-1}0101^{h-1}0^{h-1},\\
 D_h^4&=1^{h-1}0^{h-1}11(10)^{r-h-1}00.
\end{aligned}                                           \tag{2.3}
\]

Their maximum heights are respectively

\[
 h,quad h+1,quad h,quad \max\{2,h-1\},
                    \quad\max\{3,h-1\}.                \tag{2.4}
\]

For `h>=4`, the first visit to the displayed maximum in every row is the
up-step at the same physical coordinate

\[
                              p=h+1.                    \tag{2.5}
\]

For the final row at `h=4`, the later height-three peak can tie the first
one, but it occurs later in the normalized root, so the distinguished
deletion is still `p`.  If

\[
                         r_i=p_+(Z_i),                  \tag{2.6}
\]

then the pentagon arrow and PBBS successor have the simultaneous forms

\[
 Z_{i+1}=Z_i-\{d_i\}+\{r_i\},
 \qquad
 g(Z_i)=Z_i-\{p\}+\{r_i\}.                              \tag{2.7}
\]

Here `d_i` is one of the five active labels, whereas `p` lies in the common
core `L_h`.  In particular all three labels in (2.7) are distinct.

## 3. Exact regeneration of the forced `q1` target

Let

\[
                         V_h=P_1\cup Q_1                \tag{3.1}
\]

be the old `q1` upper target on the outgoing PBBS edge at `Z_1`.  Taking
complements and using (2.2),

\[
 V_h^c=g(Z_1)\cap Z_1=Z_1-\{p\}.                        \tag{3.2}
\]

The new edge at the preceding role is `P_0Q_1`.  Its upper target has
complement

\[
\begin{aligned}
 (P_0\cup Q_1)^c
   &=g(Z_0)\cap Z_1\\
   &=(Z_0-\{p\}+\{z_1\})\cap Z_1\\
   &=(L_h-\{p\})+\{z_1,c\}\\
   &=Z_1-\{p\}.
\end{aligned}                                           \tag{3.3}
\]

Comparison with (3.2) proves the exact identity

\[
                         \boxed{P_0\cup Q_1=P_1\cup Q_1.} \tag{3.4}
\]

The deficit-three core `Z_1-\{p\}` has reverse-gap counts `(0,0,3)`.
By the exact reverse-gap occurrence theorem it has precisely one corrected
old physical occurrence, namely `Z_1--g(Z_1)`.  Thus the apparently most
fragile old `q1` target is genuinely unique before the switch, but (3.4)
shows that it is not a casualty: the pentagon itself creates a replacement
occurrence.

### Theorem 3.1 (forced-`q1` regeneration)

For every `r>=4` and `2<=h<r`, the height-`h` pentagon recreates the unique
old `q1` upper target forced into the fixed gap-potential section at
`Z_h^1`.  Consequently the `H-2` forced selected cuts from the height
ladder contribute no `q1` holes.

The last sentence concerns target values.  The new occurrences occupy
different physical roles, as they must.

### Theorem 3.2 (complete high-pentagon `q1` regeneration)

For every `h>=4` and every `i in Z_5`, the old `q1` target at role `i+1`
is recreated by the new edge at role `i`:

\[
                    \boxed{P_i\cup Q_{i+1}=P_{i+1}\cup Q_{i+1}.}
                                                               \tag{3.5}
\]

Consequently the height-`h` pentagon preserves its complete `q1` upper
palette as a multiset.

#### Proof

By (2.7),

\[
\begin{aligned}
 (P_i\cup Q_{i+1})^c
   &=g(Z_i)\cap Z_{i+1}\\
   &=(Z_i-\{p\}+\{r_i\})
       \cap(Z_i-\{d_i\}+\{r_i\})\\
   &=Z_{i+1}-\{p\}.
\end{aligned}                                           \tag{3.6}
\]

The same common distinguished deletion at role `i+1` gives

\[
 (P_{i+1}\cup Q_{i+1})^c
    =g(Z_{i+1})\cap Z_{i+1}=Z_{i+1}-\{p\}.              \tag{3.7}
\]

Equations (3.6)--(3.7) prove (3.5).  Cyclically varying `i` accounts for
all five old and all five new edges. \(\square\)

### Corollary 3.3 (bounded ladder `q1` leave)

After simultaneously switching the height pentagons
`h=2,...,H-1`, every `q1` upper value associated with a pentagon of height
at least four survives on a new edge.  Therefore the complete ladder has
at most ten unresolved `q1` values: at most five from height two and at
most five from height three.  The forced selected value at role one
survives at those two heights as well, so ten is only a proof-safe crude
bound.

## 4. The whole one-sided outgoing ray transports

Delete the five old pentagon edges and write `B_i(v)` for the union of the
first `v` owners of the unchanged outgoing arc beginning at `Q_i`, with
`Q_i` included.  In particular,

\[
                              Q_i\subseteq B_i(v).        \tag{4.1}
\]

For every admissible `v`, (3.4) and (4.1) give

\[
\begin{aligned}
 P_1\cup B_1(v)
   &=(P_1\cup Q_1)\cup B_1(v)\\
   &=(P_0\cup Q_1)\cup B_1(v)\\
   &=P_0\cup B_1(v).
\end{aligned}                                           \tag{4.2}
\]

The left side is the old crossing target using only the final incoming
owner `P_1`; the right side is a new crossing target at role zero.  Hence:

### Theorem 4.1 (right-ray regeneration)

The complete one-sided outgoing upper ray based at the forced cut is
transported value-for-value:

\[
                    \boxed{P_1\cup B_1(v)=P_0\cup B_1(v)}
                    \qquad\text{for every }v.            \tag{4.3}
\]

In the exterior-current tensor, every negative term at role `1` with
minimal incoming penetration is dominated by the corresponding positive
term at role `0`.

### Theorem 4.2 (all five high-pentagon right rays)

For `h>=4`, every role satisfies

\[
 \boxed{
 P_{i+1}\cup B_{i+1}(v)=P_i\cup B_{i+1}(v)
 }
 \qquad(i\in\mathbb Z_5)                                \tag{4.4}
\]

for every admissible outgoing penetration `v`.  Hence every negative
one-cut current term with minimal incoming penetration is support-dominated
inside the same pentagon.

#### Proof

The outgoing prefix `B_(i+1)(v)` contains `Q_(i+1)`.  Apply (3.5) exactly
as in (4.2). \(\square\)

## 5. Exact frontier

Equations (4.3)--(4.4) do **not** identify a longer incoming suffix
`A_(i+1)(u)` with `A_i(u)`.  Therefore they do not settle targets whose old
witness penetrates nontrivially on both sides of a switched edge.  The
remaining PBBS upper problem has consequently narrowed from preserving the
forced unique edges and one-sided rays to one of the following:

1. prove a factor-relative alternate-corridor theorem for the genuinely
   two-sided exterior tensor; or
2. telescope those two-sided currents between adjacent heights/roles; or
3. exhibit a target family for which every corridor is two-sided and every
   such corridor is cut.

The theorem rules out two increasingly strong intrinsic-casualty
arguments: unique old `q1` multiplicity at the forced ladder cuts does not
force even one upper hole, and all but two bottom pentagons preserve the
entire `q1` palette plus all one-sided right rays.  Any growing casualty
must therefore use genuinely two-sided corridors (or an independent typed
cap/residence obstruction), not merely many changed edges.

## 6. Dependencies

Used:

* `MATH_THEOREM_PBBS_AH_LADDER_PENTAGON_RETURN_20260805.md`;
* `MATH_THEOREM_PBBS_PENTAGON_THREE_SCREEN_COMMON_HISTORY_AND_UPPER_CURRENT_GATE_20260805.md`;
* `MATH_THEOREM_PBBS_REVERSE_GAP_SECTION_DUALITY_AND_DISJOINTNESS_OBSTRUCTION_20260805.md`;
* `MATH_THEOREM_PBBS_OUTGOING_MAX_HEIGHT_OCCURRENCE_CRITERION_20260805.md`.

Not used: computation, search, random choice, or an unproved PBBS
equidistribution assertion.
