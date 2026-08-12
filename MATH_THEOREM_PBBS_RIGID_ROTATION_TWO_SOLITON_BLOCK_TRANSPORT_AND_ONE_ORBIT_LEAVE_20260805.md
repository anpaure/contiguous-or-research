# The rigid rotation rethread preserves every two-soliton block interior; only one edge orbit can leave a fan defect

**Date:** 2026-08-05  
**Method:** rooted PBBS shape-word decomposition and exact q1-row transport;
no computation or search  
**Status:** unconditional support theorem for `m>=4`.  In the full rigid
rotation rethread, the apparent two-orbit two-soliton leave collapses to the
inverse fan of the single `E_1` spatial orbit.  Every old whole-fan corridor
which avoids an `E_1` edge is reproduced literally inside one final residual
block.

## 1. Old two-soliton shape tours

Put

\[
                         n=2m+1,\qquad p=2m-3.
\]

On the old two-soliton `g=f^2` component, start a rooted shape tour at
`P_2(t)`, the state of shape `A_1` and root `t`.  The q1-row shapes occur in
the order

\[
 A_1,A_2,\ldots,A_{m-1},B_1,B_2,\ldots,B_{m-2}.   \tag{1.1}
\]

The first row is the selected edge

\[
                         E_2(t)\quad\text{with row }R_2(t), \tag{1.2}
\]

and the last row is

\[
                         E_1(t+3)\quad\text{with row }R_1(t+3). \tag{1.3}
\]

After (1.3), its head is

\[
                         Q_1(t+3)=P_2(t+2),        \tag{1.4}
\]

so the next old shape tour starts at phase `t+2`.

Define `W_t` to be the q1-row word obtained from (1.1) by omitting its final
`B_(m-2)` row.  Thus

\[
 W_t=(A_1(t),A_2(t),\ldots,A_{m-1}(t),
                    B_1(t),\ldots,B_{m-3}(t))     \tag{1.5}
\]

has length

\[
                         p-1=2m-4.                 \tag{1.6}
\]

At the level of q1-row words, the old component is therefore

\[
 \cdots W_t,\ R_1(t+3),\ W_{t+2},\ R_1(t+5),\cdots . \tag{1.7}
\]

Here a symbol such as `A_j(t)` denotes the literal row occurrence with the
root inherited from the tour beginning at phase `t`, not merely its shape.

## 2. The final residual word

After the full rotation switch, the new edge

\[
                         N_1(t):P_1(t)\longrightarrow Q_2(t) \tag{2.1}
\]

has the same q1 row `R_2(t)` as the old first edge `E_2(t)`.  From `Q_2(t)`
to `P_1(t+3)`, every edge is the unchanged old path through

\[
                         A_2,\ldots,A_{m-1},B_1,\ldots,B_{m-3}. \tag{2.2}
\]

Thus (2.1) followed by (2.2) has q1 word **literally equal** to `W_t`.
The terminal owner is `P_1(t+3)`, whose new outgoing edge is `N_1(t+3)`.
Consequently the final residual cycles have row words

\[
                         \cdots W_t,W_{t+3},W_{t+6},\cdots . \tag{2.3}
\]

Their phase return is `t->t+3`, giving `gcd(n,3)` residual cycles, as in
the full topology theorem.

## 3. Exact block-interior transport

### Theorem 3.1 (one-orbit leave localization)

Every old correct-rank whole-fan corridor on the two-soliton component which
does not contain an edge `E_1(s)` occurs with the same ordered q1 rows on the
final residual factor.  Hence it has a literal target-equal replacement,
with the same width and rank.

Therefore every potentially lost named lower target on the two-soliton shore
may be charged to the inverse fan of the single spatial orbit

\[
                         \{E_1(s):s\in\mathbb Z_n\}. \tag{3.1}
\]

The same statement holds for the paired complementary upper bank.

#### Proof

The rows `E_1(s)` are exactly the separators displayed in (1.7).  An old
contiguous corridor which contains no separator lies wholly inside one word
`W_t`.  By (2.3), that exact ordered word is a contiguous subword of a final
residual cycle.  Intersecting the rows gives the same lower target; taking
complements gives the paired upper target.

At deadline depth at most `m`, a corridor has at most `m` q1 rows.  Since

\[
                         m<p=2m-3                  \tag{3.2}
\]

for `m>=4`, it contains at most one `E_1` separator.  Thus all possible
loss is indeed covered by the disjoint one-edge inverse-fan universes in
(3.1).  `square`

This is a support transport.  The final occurrence address generally differs,
so an address-sensitive compiler or cap route still needs a declared
transport/reassignment.

### Corollary 3.2 (sharpened polynomial leave)

On each of the lower and paired-upper shores, the unresolved named fan leave
has size at most

\[
                         \boxed{n\binom{m+1}{2}=O(m^3)}. \tag{3.3}
\]

This halves the earlier `2n binom(m+1,2)` cut-union bound and, more
importantly, identifies one explicit orbit on which every remaining repair
may be concentrated.

#### Proof

One punctured selected edge has at most `binom(m+1,2)` two-sided fan
corridors.  Apply Theorem 3.1 to the `n` edges in (3.1).  `square`

The actual number of missing target **values** may be smaller because
different corridors can coincide or acquire alternatives elsewhere.

## 4. Explicit inverse-fan coordinates at the surviving gate

Let the central separator be `E_1(s)`, whose q1 row is

\[
                         H_{s,0}=\rho^sK^B_{m-2}=R_1(s). \tag{4.1}
\]

The right rows after it begin the next `A` tour:

\[
                         H_{s,v}=\rho^{s-v}K^A_v,
 \qquad 1\le v\le m-1.                            \tag{4.2}
\]

The first `m-3` left rows run backwards through the `B` chain:

\[
                         H_{s,-u}=\rho^{s+u}K^B_{m-2-u},
 \qquad 1\le u\le m-3.                           \tag{4.3}
\]

The next two are

\[
 H_{s,-(m-2)}=\rho^{s-m-1}K^A_{m-1},
 \qquad
 H_{s,-(m-1)}=\rho^{s-m}K^A_{m-2}.               \tag{4.4}
\]

Thus the complete remaining local target universe is explicitly

\[
 T_s(u,v)=\bigcap_{h=-u}^{v}H_{s,h},
 \qquad u,v\ge0,\quad u+v\le m-1.                \tag{4.5}
\]

Equations (4.1)--(4.5) reduce the residual support problem to one translated
triangular family.  No generic three-edge packet atlas is needed to describe
the leave.

#### Verification of the root indices

For a tour beginning at `A_1` root `t=s-3`, the `B_j` root is

\[
                         t+m-j+1.                 \tag{4.6}
\]

Putting `j=m-2-u` gives `s+u`, proving (4.3).  The predecessor of `B_1`
is `A_(m-1)`; the exceptional `A_(m-1)->B_1` root shift is `-3`, giving
the first exponent in (4.4).  One more backward `A` step gives the second.
The head of `E_1(s)` is `P_2(s-1)`, the `A_1` root `s-1`; subsequent `A`
roots decrease by one, proving (4.2).

## 5. Consequences and remaining gate

Combined with the braid interval theorem, the full rigid rotation rethread
now has the following support ledger:

| old bank | final replacement |
|---|---|
| complete single-soliton fan | braid parity subbank, all depths |
| two-soliton corridors avoiding `E_1` | identical residual block `W_t` |
| corridors using `E_1` | open triangular family (4.5) |

The sole fan-support problem is therefore:

> install target-equal alternatives for the translated family (4.5), or
> prove that its values already occur in the braid/residual background.

This does not repair the generalized source-payload obstruction, the
arbitrary exterior upper bank beyond paired complements, zero-gap residence,
typed common cap, or terminal linear opening.  It does replace a diffuse
`3n`-edge fan audit by one exact `n`-edge orbit.

## 6. Dependencies

The topology and phase paths come from

`MATH_THEOREM_PBBS_RIGID_C6_SERIAL_ROTATION_ORBIT_TOPOLOGY_NOGO_20260805.md`.

The single-soliton replacement is

`MATH_THEOREM_PBBS_RIGID_ROTATION_BRAID_ALL_DEPTH_INTERVAL_FAN_TRANSPORT_20260805.md`.

The inverse-fan triangle bound is

`MATH_THEOREM_PBBS_SELECTED_EDGE_INVERSE_FAN_AND_C6_PUNCTURE_GATE_20260805.md`.
