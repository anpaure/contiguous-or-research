# K16 H/A portal test for the Johnson C4, and the complete-reversal host gate

**Date:** 2026-08-01  
**Lane:** L, exact portal columns / complete-reversal integration  
**Status:** exact finite C4-reversal no-completion theorem on the frozen H1
word; solver-free interaction-order reduction; exact integration of the
resident reset-return theorem.  No new K16 word or all-k bound is claimed.

## 0. Verdict

There are two different projections, and they must not be conflated.

1. A four-cell Johnson-square reversal can cross the literal H/A target cut.
   Thus `e_H+e_A` is **not** a conserved cut for word-entry reversals.
2. The crossing is not a primitive support-four OR interaction.  For every
   induced square reversal, all interval classes meeting three or four edits
   cancel identically.  Only four singleton classes and the two outer-pair
   classes can change.  Hence every newly created target already has a
   witness using at most two of the four edits.
3. The complete occurrence census on the authenticated H1 word contains
   `2,488,607` ordered induced/rainbow square reversals.  Exactly `1,784`
   create `H`; `1,770` do so in a singleton class and `14` only in an outer
   pair class.  Exact compound replay finds no universal word.  The minimum
   final defect is `14` holes, attained by three reversals.
4. The long return rail now closes the all-depth local packet completely by
   `MATH_THEOREM_RESET_RETURN_RAIL_COMPLETE_REVERSAL_GUARDED_CYCLE_20260801.md`.
   It is resident, q1-simple, all-width cyclic-transparent, derivative-row
   transparent, and internally compiler-isomorphic.  In a one-copy host it
   is nevertheless a **closed** alternating exchange.  Its only possible
   H/A portal action comes from exterior cross-windows after opening; a
   context-transparent exterior would make that action zero.

Thus the bare C4 does not furnish a new high-order portal column, while the
resident reset-return cycle solves the local literal packet but still needs
global planting, opening/joining, exterior control, a common residual
compiler, and regeneration.

## 1. Frozen word and sign convention

Let

```text
w = scratch/k16_h2_to_h1_p0.h1.word
SHA-256 ba4bf6d38e1510d06ee64c03c5f13e9a2a4f276882d930d0b5435caf7bcc1e7a
length 12873
H = 0x2c6d
A = 0xa86d.
```

For a rewrite `w -> v`, put

\[
                 \beta_{w,v}(t)=m_w(t)-m_v(t).             \tag{1.1}
\]

The source has

\[
                         (m_w(H),m_w(A))=(0,1),             \tag{1.2}
\]

and its unique `A` witness is `[6438,6440]` in zero-based coordinates.  For
`Q={H,A}`, the positive-cut inequality of the H/A cycle-column theorem is

\[
                         \beta(Q)\le -1.                    \tag{1.3}
\]

The right side is `(m_w(A)-1)-1=-1`: `A` has zero spare capacity and `H` is
the source hole.

## 2. A literal cut crossing exists

At zero-based positions

\[
                   (2408,3752,4487,5390)                   \tag{2.1}
\]

the source values are

\[
 (V_1,V_2,V_3,V_0)
   =(0x0005,0x0404,0x2400,0x2001).                         \tag{2.2}
\]

Replace them by the reverse phase

\[
 (V_0,V_3,V_2,V_1)
   =(0x2001,0x2400,0x0404,0x0005).                         \tag{2.3}
\]

The cyclic order `(V0,V1,V2,V3)` is an induced `J(16,2)` square.  Its lower
and upper edge palettes are respectively

\[
 \{0x0001,0x0004,0x0400,0x2000\},                         \tag{2.4}
\]

\[
 \{0x2005,0x0405,0x2404,0x2401\}.                         \tag{2.5}
\]

Both are simple.  Exact all-mask replay gives

\[
                 (m(H),m(A)):(0,1)\longmapsto(1,1),        \tag{2.6}
\]

so

\[
                         \beta(Q)=-1.                      \tag{2.7}
\]

The reversal saturates (1.3).  Its new `H` witness is the literal collar

\[
 [4486,4488]:\qquad
 0x0849\vee0x0404\vee0x2029=0x2c6d,                       \tag{2.8}
\]

whose old OR was `0x2c69`.  The `A` witness is disjoint and survives.

This is an integral cut crossing, not a completion: the final word has 34
holes.  Moreover the singleton substitution

```text
position 4487: 0x2400 -> 0x0404
```

already makes the witness (2.8), preserves `A`, and leaves only nine holes.
The other three square edits add 25 holes and repair none.  Consequently the
row is support-minimal only inside the clean square-reversal architecture;
it is not the smallest substitution which crosses `Q`.

The apparent contradiction with state-cycle telescoping is only a type
error.  If `V_i` denoted four **whole word states**, their stateful columns
would telescope.  Here `V_i` are four values placed in four occurrence-
labelled cells.  Intervals see unequal spatial collars, so the physical
column does not factor through the abstract cycle incidence.

## 3. Exact context-kernel formula

Let `p1<p2<p3<p4` be the four edited positions.  For `1<=i<=j<=4`, let
`K_ij(C)` be the number of intervals whose edited-position intersection is
exactly the consecutive block `pi,...,pj` and whose fixed-cell OR, after
removing those edited cells, is `C`.  Let

\[
 R^-_{ij}=\bigvee_{h=i}^{j}V_h^-,\qquad
 R^+_{ij}=\bigvee_{h=i}^{j}V_h^+.                          \tag{3.1}
\]

For the reversal `(V1,V2,V3,V0)->(V0,V3,V2,V1)`, one has

\[
                         R^+_{ij}=R^-_{5-j,,5-i}.          \tag{3.2}
\]

Therefore every target set `Q` has the exact weighted column

\[
 \boxed{
 \beta(Q)=
 \sum_{i\le j}\sum_C K_{ij}(C)
 \left(
  {f1}_{C\vee R^-_{ij}\in Q}
 -{f1}_{C\vee R^-_{5-j,,5-i}\in Q}
 \right).}                                                \tag{3.3}
\]

Thus abstract cycle balance cancels the physical column only when the
relevant mirror context kernels agree, or when a saturation/dominance
hypothesis annihilates both labels.  Neither follows from equality of the
lower/upper edge palettes.

## 4. The high-order interaction is identically zero

Every induced Johnson square has the normal form

\[
\begin{aligned}
 V_1&=M+c,&V_2&=M+d,\\
 V_3&=(M-f)+d+g,&V_0&=(M-f)+c+g,                           \tag{4.1}
\end{aligned}
\]

where `f in M` and `g` lies outside `V1 union V2`.

### Theorem 4.1 (six-class collapse)

For the reversal in (4.1), the edited-value OR is unchanged in the interval
classes

\[
                         23,\quad123,\quad234,\quad1234.    \tag{4.2}
\]

Only

\[
                         1,2,3,4,12,34                     \tag{4.3}
\]

can contribute to (3.3).  In particular, every target absent from the old
word and present after the reversal has a new witness using at most two
edited positions.

#### Proof

Class `23` merely reverses `V2,V3`, so its OR is unchanged.  Any three
vertices of (4.1) contain `M-f` together with all four active coordinates
`f,c,d,g`; hence the ORs of both triple classes agree under reversal.  The
four-vertex OR is tautologically invariant.  Formula (3.3) leaves exactly
(4.3).  Since the source had no witness for a newly created target, at
least one changed interval class supplies its new witness, and every such
class has size one or two. \(\square\)

Equivalently, the third- and fourth-order spatial Möbius interaction of a
square reversal is zero.  This is the conserved quotient requested by the
portal question.  The square is attachment-active in the ordered-diamond
graph, but it creates no new high-order contiguous-OR column.

## 5. Complete literal C4 census

The exact occurrence generator takes every ordered adjacent pair `V1,V2`
present in the word, every `f in V1 intersect V2`, and every fresh
`g outside V1 union V2`, constructs (4.1), and enumerates occurrences

\[
 p_1\in\operatorname{Pos}(V_1)<p_2\in\operatorname{Pos}(V_2)
 <p_3\in\operatorname{Pos}(V_3)<p_4\in\operatorname{Pos}(V_0). \tag{5.1}
\]

It finds exactly

```text
ordered induced/rainbow occurrence supports   2,488,607
reversals creating H                               1,784
  with a singleton H witness                       1,770
  pair-only H witness                                 14
preserving the unique A witness                    1,784
universal reversals                                    0
minimum final hole count                              14
rows attaining the minimum                             3.
```

One minimum row is

```text
positions  (1,528,556,5534)
old        (0x2068,0x0069,0x0063,0x2062)
new        (0x2062,0x0063,0x0069,0x2068)
```

and its exact final holes are

```text
0x1469 0x146b 0x2463 0x2867 0x2877 0x2c67 0x3463
0x3467 0x3663 0x367b 0x5469 0x5669 0x6879 0x766d.
```

This proves a finite no-completion theorem for literal reversals of four
existing word values in the ordered induced/rainbow C4 architecture.  It is
not an unrestricted four-substitution theorem: arbitrary new square values,
another ordering, a non-square four-edit packet, or a longer rethread lie
outside the census.  The exhaustive radius-three theorem and the older
1,341-support nested-portal theorem remain logically separate.

## 6. Integration of the resident complete-reversal packet

The authoritative return theorem takes `n=d+1`, opens the two-queue reset at
`E=T0,F=T_(2n-1)`, chooses `d` exchange coordinates in its permanent core
while retaining one permanent anchor, and chooses `d` fresh coordinates
outside the reset support.  The return rail `R_d` closes the reset path to a
cycle `Z+`; `Z-` is its complete reversal.

Under

\[
                         r\ge2d+2,\qquad k-r\ge2d+1,        \tag{6.1}
\]

the frozen theorem proves, without further hypotheses:

* `4d+2` distinct rank-`r` roots;
* globally simple lower and upper q1 palettes;
* every nonconstant positive run of length at least `d+1`;
* a nonempty maximal depth-`d` antecedent;
* exact reversal of every derivative-row inventory;
* equality of every cyclic interval-OR deck at every width;
* an isomorphism of every compiler cell wholly internal to the packet; and
* one closed attachment cycle and two closed predecessor parity cycles,
  which become the required one-plus-two paths after opening a common edge.

The independently frozen audit
`MATH_AUDIT_RESET_RETURN_RAIL_COMPLETE_REVERSAL_GUARDED_CYCLE_20260801.md`
sharpens only the coordinate supply to `r>=2d+1,k-r>=2d+1` by proving every
maximal erosion cell nonempty without a permanent anchor.  This note uses
the anchored face (6.1), so it does not depend on that sharpening.

At `k=16,d=3`, the tight choice `r=8` satisfies (6.1).  The independent
calibration in this lane constructs 14 roots with 14 distinct lower q1 and
14 distinct upper q1 colours, minimum run four, one attachment overlay
component and two predecessor components.

The rank-two C4 in Section 2 does **not** satisfy (6.1), has no permanent
depth-three reset core, and cannot be post-hoc lengthened by this theorem.
The resident packet must be planted prospectively in a rank-eight host; it
is not a repair of the four positions (2.1).

## 7. Exact one-copy / DM / portal impact

### Theorem 7.1 (closed packet is DM-neutral)

Before opening, the two complete-reversal phases differ by closed
alternating cycles only: one in the attachment projection and two in the
predecessor projection.  Therefore switching one planted copy preserves
matching cardinality and exposes no augmenting endpoint.  It rethreads one
exchange component but does not by itself discharge a portal deficiency.

This does not contradict the one-plus-two return theorem: those paths appear
only after a common edge is opened, and must then be joined to the ambient
topology.

### Theorem 7.2 (all physical portal charge is a boundary current)

Place one phase as a linear block and replace it by its reversal.  Intervals
wholly inside the block have a value-preserving reversal bijection.  An
interval meeting both exterior sides sees the same total block OR.  Hence
the only possibly nonzero physical transport comes from intervals crossing
exactly one block boundary.  It is determined by the difference between the
forward prefix-OR and suffix-OR profiles, convolved with the corresponding
exterior suffix/prefix profiles.

Consequently:

1. if the two boundaries are saturated, or a phase-common socket preserves
   the same-side prefix/suffix profiles, then the complete physical column is
   zero and no H/A positive cut is crossed;
2. any H/A gain must use a deliberately nonzero exterior boundary current;
   the bare escape in Section 2 is exactly such an asymmetric collar effect;
   and
3. internal all-width transparency cannot certify those exterior currents.

Thus the complete-reversal packet can be used in either of two honest ways:

* as a neutral resident router, with a separate portal/provider column; or
* as part of a coupled exterior actuator whose exact cross-window column is
  replayed and whose collateral witnesses are protected.

There is no third inference from cyclic deck equality alone.

## 8. Compiler and remaining gates

The authoritative theorem closes internal compiler transport: reverse every
cell wholly inside the component.  What remains is specifically the
**common residual** compiler after the packet is opened and joined.  Cells
crossing the cut and assignments elsewhere must have one common Hall
matching (or one common contracted minor) in both phases.

The exact open rows are therefore:

1. root-palette/global host planting of the extra `2d` return roots;
2. opening and joining the closed component without losing unique targets;
3. protected exterior cross-window currents;
4. one common residual compiler after contraction; and
5. same-parity regeneration of the protected component.

Residence, internal upper transport, derivative-row equality, and internal
compiler transport are **not** open for this packet.

## 9. Audits and scope

The lane audit

```text
scratch/audit_l_k16_ha_open_c4_resident_return_20260801.py
  SHA-256 03b3efd3d298465dddbea4043f3da3b52fc5d0920300711a6570b32a4c3bca58
scratch/l_k16_ha_open_c4_resident_return_20260801.audit.json
  SHA-256 d10cc3cf48b63f8d7a7108023858409d6f4a6050820ad834dd3c3c2e8fb947ed
  payload 26da54d38fae013f6b3d67bcf8af870b63e945adbf9b26cf8bc2950b75cb84cc
```

uses a compact suffix-OR DP for all 65,536 multiplicities, checks the literal
cut crossing, and independently calibrates the complete-reversal packet at
`(k,r,d)=(16,8,3)`.  A second audit

```text
scratch/audit_l_k16_ha_open_c4_escape_independent_20260801.py
  SHA-256 e11ea14898d7a6d19a8192bc698d2b740e6047cf62bfefc4f8600690e87fb839
scratch/l_k16_ha_open_c4_escape_independent_20260801.audit.json
  SHA-256 995abeaa70789a4bf3db61f4819cf8876dd5d067cb0e2f2ad773fc78de283ca3
  payload 6ba59178ee4d9190af161cba4b0804b7036f9cc32819e4ed8b521d36fd28f527
```

recomputes the literal escape by direct left/right interval enumeration.
The exhaustive occurrence-census artifacts are listed after their frozen
hashes below:

```text
scratch/audit_l_k16_induced_c4_nested_reversal_20260801.py
  SHA-256 86c7f36654a1e0a81c58b39562928b6fe485a04548744db6ce7a53bbed90cdc6
scratch/l_k16_induced_c4_nested_reversal_20260801.audit.json
  SHA-256 2fd30e9e7a15c14ff93bcd046e599904c0fa807f064cf0bbc08d11058cb6b24f
  payload 7463ddb9785686f76edb37be1d159296bcd53515bfab2ad2ed8550ce08a3b02c
scratch/l_k16_induced_c4_nested_reversal_best14_20260801.tsv
  SHA-256 eb033b944edbff07a33ba8194c030fdda56c74d76d3661681aa0ba93488e6bb0
```

No statement here changes the proved exact value `nu(16)=12873`, constructs
an alternative optimum, or proves an additive all-k bound.
