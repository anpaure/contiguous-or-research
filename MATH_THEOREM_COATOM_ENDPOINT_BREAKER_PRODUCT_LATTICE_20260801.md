# Endpoint-planted adjacent twists generate the full labelled all-depth lattice

Date: 2026-08-01
Status: unconditional integer catalogue theorem.  It closes the complete
all-depth occurrence **span** after all admissible packet-role injections are
allowed.  It is not a fixed-endpoint planting theorem and does not create a
Thread D return-Hall edge.

## 0. Result

Fix `d>=3`, `r>=d+4`, and a `k`-coordinate ground set with `k-r>=4`.
Use the current endpoint-planted schedule

\[
                         E=\{0,2,4,6,8,10\},                 \tag{0.1}
\]

the first `Iab` omission order

\[
                         p,f_1,\ldots,f_d,f_0,               \tag{0.2}
\]

and the common order `f_0,f_1,...,f_d,p` in the other blocks.  Enlarge this
catalogue by allowing the label-attached `Ica` block, in both phases, to
transpose any adjacent internal pair `f_s,f_(s+1)`.  All packet roles may be
injected admissibly into the ground set, and packet reversal supplies both
orientations.

For `2<=q<=d`, let

\[
 M_q=\mathbb Z^{\binom{[k]}{r-q}},\qquad
 \partial_q e_X=\sum_{x\in X}e_x,                           \tag{0.3}
\]

and let `L_d` be the integer span of the complete signed lower-occurrence
actions of this labelled packet catalogue.

### Theorem 0.1 (full product lattice)

\[
 \boxed{
 L_d=\bigoplus_{q=2}^{d}\ker_{\mathbb Z}\partial_q .
 }                                                            \tag{0.4}
\]

The equality is integral: there is no finite index, parity condition, or
remaining cross-depth linear invariant.  In fact, only the adjacent twists
with

\[
                         1\le s\le\lfloor d/2\rfloor          \tag{0.5}
\]

are needed.

The load-bearing qualifier is **labelled catalogue**.  The proof isolates a
depth by subtracting packets whose boundary role `p` or `f_0` is exchanged
with an active role.  Those packets generally have different endpoints and
different owner slots.  Thus (0.4) does not assert that one planted carrier
contains a serially usable realization of the required signed combination.

## 1. The planted baseline and square notation

Write the internal filler order as

\[
                         u_1,\ldots,u_d,                      \tag{1.1}
\]

put `f_0=ell`, `f_(d+1)=p`, and let `K` have size `r-d-4`.  For disjoint
`H,alpha,beta,x,y`, define the integral Johnson square

\[
 Q_H(\alpha,\beta;x,y)
 =[H\alpha x]+[H\beta y]-[H\alpha y]-[H\beta x].              \tag{1.2}
\]

Let

\[
 L=\{e,d\},\qquad I=\{\mathord\infty,c\},\qquad
 P_t=\{u_1,\ldots,u_t\},\qquad
 S_t=\{u_{d-t+1},\ldots,u_d\}.                               \tag{1.3}
\]

At depth `q`, put `t=d+1-q`.  Direct intersection of the planted packet
gives the common-order action

\[
\begin{aligned}
 \Delta_q^0={}&[KLaP_t]+[KLbS_t]-[KLbP_t]-[KLaS_t]\\
              &-[KIaP_t]-[KIbS_t]+[KIbP_t]+[KIaS_t].          \tag{1.4}
\end{aligned}
\]

Thus the corrected endpoint planting changes the four-term unplanted flag
row into an eight-term three-trade.  In particular (1.4) has zero point
degree, and indeed zero pair degree, separately at every depth.

Formula (1.4) is included to prevent a scope error: the endpoint-planted
baseline is not literally the unplanted four-term row.  The theorem below
uses its safe adjacent-order differences.

## 2. Exact triangular adjacent-twist formula

Let `Delta^s` be the packet action after swapping `u_s,u_(s+1)` only in the
label-attached `Ica` block in both phases, and put

\[
                             C_s=\Delta^s-\Delta^0.            \tag{2.1}
\]

Write `x=u_s`, `y=u_(s+1)` and suppose `1<=s<=floor(d/2)`.  Define

\[
\begin{aligned}
 H_s^+&=K\cup\{\mathord\infty,c\}
              \cup\{u_{s+2},\ldots,u_d\},\\
 H_s^-&=K\cup\{\mathord\infty,c\}
              \cup\{u_1,\ldots,u_{s-1}\},\\
 H_{s,t}^{\rm tail}&=K\cup\{\mathord\infty\}
              \cup\{u_{s-t},\ldots,u_{s-1}\}.               \tag{2.2}
\end{aligned}
\]

Empty displayed filler ranges are omitted.

### Lemma 2.1 (unit triangular correction)

For `2<=q<=d`, the nonzero components of `C_s` are exactly

\[
\begin{array}{c|c}
q& (C_s)_q\\ \hline
s+1&Q_{H_s^+}(a,p;x,y),\\[1mm]
d+1-s&Q_{H_s^-}(a,f_0;x,y),\\[1mm]
q>d+1-s&Q_{H_{s,d+1-q}^{\rm tail}}(a,c;x,y).
\end{array}                                                    \tag{2.3}
\]

If `2s=d`, the first two entries occur in the same central row and are
added.  All rows strictly before `s+1`, and all rows strictly between
`s+1` and `d+1-s`, vanish.

#### Proof

Only an intersection window containing exactly one of the two transposed
coatoms can change.  A window wholly inside the `Ica` block occurs with the
same order change in both ECO phases and cancels from (2.1).  The remaining
windows cross one of the two exterior screens of that block.

For the first crossing, the common filler intersection is
`{u_(s+2),...,u_d}` and the exterior alternatives are `a,p`; it first
appears at width `s+2`, hence at depth `s+1`.  Its four signed values are
exactly `Q_(H_s^+)(a,p;x,y)`.  The opposite crossing first sees the common
prefix `{u_1,...,u_(s-1)}` at reflected depth `d+1-s`; its alternatives are
`a,f_0`, giving the second row of (2.3).

After that reflected crossing, put `t=d+1-q<s`.  The window retains exactly
the `t` omissions immediately preceding the swapped pair.  The active
alternatives are `a,c`, so its four values are
`Q_(H_(s,t)^tail)(a,c;x,y)`.  Before either crossing the two coatoms are
both present or both absent from the window intersection, so there is no
change.  This exhausts the crossing windows and proves (2.3).  Every term
has coefficient one. \(\square\)

For adjacent positions in the second half the analogous local
classification is a sum of Johnson squares as well.  Hence every safe
adjacent twist is point balanced.  Lemma 2.1 is the triangular half needed
for generation.

## 3. Boundary commutators isolate one depth integrally

Let `sigma_p` be the global role relabelling which exchanges `p` with the
active role `b`, fixing all other roles.  Role `b` does not occur anywhere
in (2.3), while `p` occurs only in its first row.  Consequently

\[
 C_s-\sigma_p C_s
 =\mathbf e_{s+1}\otimes Q_{H_s^+}(b,p;x,y),                  \tag{3.1}
\]

where `e_q` denotes support only in depth `q`.

Likewise, if `sigma_0` exchanges `f_0` with `b`, then

\[
 C_s-\sigma_0 C_s
 =\mathbf e_{d+1-s}\otimes Q_{H_s^-}(b,f_0;x,y).              \tag{3.2}
\]

These are primitive four-term squares, not twice a square.  This is why no
index two survives despite the value `2` seen when an antisymmetric
reflection functional is evaluated on a breaker.

Each `C_s` lies in `L_d` because it is the difference of a twisted and an
untwisted reversible packet.  Its relabelled copy also lies in `L_d`.
Therefore (3.1)--(3.2) are honest integer combinations of catalogue
columns.

The role `b` is reused as the alternate aperture label.  No new fifth
exterior coordinate is required.  This preserves the sharp packet
co-rank assumption `k-r>=4`.

For odd `d`, equations (3.1)--(3.2) cover the depth pairs

\[
 (2,d),(3,d-1),\ldots.
\]

For even `d`, they cover the same pairs and (3.1) with `s=d/2` covers the
central depth.  Thus a primitive pure-depth Johnson square is available at
every `2<=q<=d`.

## 4. Every labelled square is realized

It remains to check that the square in (3.1) or (3.2) may receive arbitrary
labels.

At the shallow depth `q=s+1`, the desired square core has size

\[
 |H|=r-q-2=r-s-3
     =|K|+2+(d-s-1).                                         \tag{4.1}
\]

Partition an arbitrary such `H` into `K`, the roles `infinity,c`, and the
tail roles `u_(s+2),...,u_d`.  Assign the four external square labels to
`b,p,x,y`.  The remaining roles outside `H` are

\[
                  a,e,d,f_0,u_1,\ldots,u_{s-1},               \tag{4.2}
\]

exactly `s+3` further labels.  Together with the four square labels this
requires `s+7` labels outside `H`, while

\[
                 k-|H|=k-r+s+3\ge s+7.                       \tag{4.3}
\]

At the deep depth `q=d+1-s`, partition `H` into `K`, `infinity,c`, and
`u_1,...,u_(s-1)`, assign the square labels to `b,f_0,x,y`, and use the
remaining outside labels for

\[
                  a,e,d,p,u_{s+2},\ldots,u_d.                 \tag{4.4}
\]

The same count reduces exactly to `k-r>=4`.  Hence every abstract Johnson
square in every required layer occurs with either orientation.

The uniform-degree lattice theorem states integrally that, for
`2<=m<=k-2`,

\[
 \ker\left(
   \mathbb Z^{\binom{[k]}m}\longrightarrow\mathbb Z^k,
   e_X\longmapsto\sum_{x\in X}e_x
 \right)                                                       \tag{4.5}
\]

is generated by the Johnson squares (1.2).  Applying this theorem
independently to (3.1)--(3.2) at every depth proves

\[
 \bigoplus_{q=2}^d\ker\partial_q\subseteq L_d.                \tag{4.6}
\]

Conversely, (1.4), Lemma 2.1, and the analogous square decomposition for
the unused adjacent twists show that every packet action has zero point
degree at every depth.  Thus `L_d` is contained in the right side of
(4.6), proving Theorem 0.1 over the integers. \(\square\)

## 5. Exact physical and compiler scope

The pure-depth square (3.1) is a four-packet aperture commutator:

\[
 (\Delta^s(p)-\Delta^0(p))
 -(\Delta^s(b)-\Delta^0(b)),                                  \tag{5.1}
\]

where the second pair exchanges the packet roles `p,b`.  Formula (3.2) has
the same form with `f_0,b`.  The four columns are individually U1--U4 safe,
but they do not share one endpoint-planted owner slot.

Consequently:

* The full-coupled-span item formerly open in the Thread D catalogue is now
  closed algebraically.
* The breaker correction is not a new physical compiler cell.  It is a
  signed occurrence action assembled from different labelled packet slots.
* It does not add an edge to the fixed-basis Thread D return graph.  A return
  edge requires one freed address-labelled cell to satisfy the opposite
  target and every trace/common-cap guard; (5.1) supplies no such cell.
* The breaker and both commutators have zero `q=1` action, so the closed q1
  hinge is unchanged.
* The canonical local return deficiency therefore remains `2(d-1)` until
  exterior trace-guarded return cells or a genuine shared-owner resolver are
  constructed.

In particular, for one fixed endpoint/filler flag, `p,f_0,b` are not
available for the relabellings used in (3.1)--(3.2).  Theorem 0.1 must not be
quoted as fixed-slot serial reachability.  The remaining gates are physical
regenerative planting, owner-token compatibility, nonnegative intermediate
decks, and the nonlinear common-cap/return-Hall compiler constraints.

## 6. Audit

The replay

```text
scratch/audit_coatom_endpoint_breaker_product_lattice_20260801.py
scratch/coatom_endpoint_breaker_product_lattice_20260801.audit.json
```

checks the literal formula (2.3) and both primitive commutators for
`3<=d<=14`.  It also forms actual minimal-corank labelled packet-orbit
columns and obtains exact full product ranks over `GF(2)`:

```text
d=3:  770 / 770
d=4: 2175 / 2175
d=5: 5382 / 5382
```

It reports

```text
PASS_COATOM_ENDPOINT_BREAKER_PRODUCT_LATTICE
```

with canonical payload SHA-256

```text
34d67c5726976a840c6b049adc915c544fcf6e2d664f4c8954195ab3681c3d22
```

Dependencies:

* `MATH_THEOREM_COATOM_FLAG_SIGNATURE_AND_PLUCKER_LATTICE_20260801.md`;
* `MATH_THEOREM_COATOM_SINGLE_BLOCK_ORDER_REFLECTION_BREAKER_20260801.md`;
* `MATH_THEOREM_COATOM_ENDPOINT_PLANTING_FIXED_SLOT_HALL_CORRECTION_20260801.md`; and
* `MATH_THEOREM_THREAD_D_COATOM_U5_NATIVE_COLUMNS_AND_RETURN_HALL_20260801.md`.
