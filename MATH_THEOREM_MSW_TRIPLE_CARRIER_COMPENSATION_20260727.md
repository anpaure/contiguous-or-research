# MSW triple-carrier compensation: a linear exact cycle supply

Date: 2026-07-27

## 1. Every separated-double-swap catalogue is functional

Let $F$ be an exact wreath factor on $[2m+1]$.  A separated double swap in a
row written locally as

$$
(a,b,X,c,d,Y),\qquad |X|=m-2,\quad |Y|=m-1,
$$

has removed triple

$$
R=\{Y+a,\ X+b+c,\ Y+d\}. \tag{1.1}
$$

This is the length-two path in the odd graph centred at the middle owner
$X+b+c$.  As the swap start runs around one row, its centre runs through all
$2m+1$ middle owners of that row.  Since the rows of $F$ partition the middle
layer, the $W$ removed triples are pairwise distinct.

### Theorem 1 (triple functional graph)

The $W$ separated-double-swap atoms define a partial function

$$
R\longmapsto A
$$

on their triple ports.  Every directed cycle using distinct factor rows is
an exact support-matched wreath trade, and all such cycles can be found in
$O(W)$ incidence operations.

#### Proof

Uniqueness of the source ports follows from the centre argument above.  On a
directed cycle, every removed triple is the added triple of its predecessor,
so the signed owner boundary is zero.  Distinct factor rows make all removed
owners distinct.  The owner-circulation criterion therefore gives an exact
trade.  A partial functional graph is decomposed into its directed cycles in
linear time. QED.

The implementation is `enumerate_all_near_carrier_cycles` in
`scratch/near_wreath_two_trades.py`.  This removes the previous artificial
restriction to inverse 2-cycles.

## 2. Canonical MSW has a linear all-$m$ family of 2-cycles

For a Dyck word $x$, let $\pi(x)$ be the MSW flip permutation.  We use two
consequences of its recursive formula (Lemma 13 of the MSW paper).

1. If a four-step Dyck block is inserted at a marked vertex of a Dyck path,
   its four step positions occur consecutively in $\pi$.  Nesting may reverse
   the local traversal, but does not interleave outside positions.
2. For Dyck concatenation, $\pi(a\circ b)$ processes the positions of $a$
   and then the shifted positions of $b$.

Both statements follow by induction on the canonical decomposition
$x=1\circ u\circ0\circ v$.  An insertion inside $u$ is passed to the
reflected recursive call, an insertion inside $v$ to the direct recursive
call, and an insertion at a component boundary is checked directly.

The two four-step flip words, in zero-based labels, are

$$
\pi(1100)=(3,1,2,0),\qquad
\pi(1010)=(1,0,3,2). \tag{2.1}
$$

In the reflected orientation they are respectively
$(0,2,1,3)$ and $(2,3,0,1)$.  In either orientation the second block is
obtained from the first by

$$
(A,B,C,D)\longmapsto(B,D,A,C). \tag{2.2}
$$

Extend $\pi(x)$ by the extra coordinate $2m$, obtaining a cyclic word $q(x)$
of length $n=2m+1$.  The cyclic order of the corresponding MSW wreath is

$$
r_j=q(x)_{-1-2j\pmod n}. \tag{2.3}
$$

If the changed four-block of $q$ starts at index $s$, choose $p$ by
$-1-2p=s+2$.  Then (2.2)--(2.3) say that the two row orders agree outside
four locations and locally have the form

$$
(a,b,X,c,d,Y),\qquad (b,d,X,a,c,Y). \tag{2.4}
$$

The removed and added triples of the first row are

$$
R_1=\{Y+a,X+b+c,Y+d\},\qquad
A_1=\{Y+b,X+a+d,Y+c\},
$$

whereas those of the second are $R_2=A_1$ and $A_2=R_1$.  Thus the two
separated double swaps at start $p$ form an inverse triple 2-cycle.

### Theorem 2 (explicit MSW triple-cycle supply)

For every $m\ge3$, every smaller Dyck word $z\in D_{2m-4}^0$, and every split
$z=u\circ v$, there is one same-start inverse cycle

$$
u\circ1100\circ v\quad\longleftrightarrow\quad
u\circ1010\circ v. \tag{2.5}
$$

There are $2m-3$ split positions.  The two boundary families are

$$
110\circ z\circ0\longleftrightarrow101\circ z\circ0,
\qquad
1\circ z\circ100\longleftrightarrow1\circ z\circ010. \tag{2.6}
$$

with local-move start displacement $+1$ and $-1$, respectively.  Thus every
one of the $2m-1$ classes is explicitly bijective with $D_{2m-4}^0$.  In
particular canonical MSW contains at least

$$
\boxed{N_m=(2m-1)C_{m-2}
      ={m\over2}C_{m-1}+2C_{m-2}} \tag{2.7}
$$

distinct exact inverse-triple trades.

#### Boundary calculation

For the left boundary family, put $z^*=\overline{\operatorname{rev}}(z)$
and $A=2m-\pi(z^*)$ componentwise, in one-based labels.  The recursive
formula gives

$$
\pi(110z0)=(2m,A,2,3,1),
$$

$$
\pi(101z0)=(2,1,2m,A,3). \tag{2.8}
$$

After adjoining the sentinel $2m+1$ and cyclically shifting the second word
by two places, the common block $(2m,A)$ aligns and the remaining four entries
again obey (2.2).  A two-place shift in $q$ is a one-place shift in the row
order by (2.3), giving start displacement $+1$.  Reflection gives the right
boundary family and displacement $-1$.  The same-start cases follow directly
from (2.1)--(2.4).  Distinctness is immediate: the differing position and
deletion of the displayed four-step block recover the split and $z$.

Thus the proved cycle supply is asymptotically

$$
N_m\sim {W\over16},\qquad 2N_m\sim {W\over8}. \tag{2.9}
$$

The functional decomposition has also been audited through $m=10$.  In those
instances every pure triple cycle belongs to the family above and has length
two.  The theorem proves the displayed family for all $m$; the stronger
classification saying that there are **no additional** pure triple cycles is
still only finite-verified.

The independent finite verifier is
`scratch/audit_msw_triple_cycle_formula.py`; its complete output is
`scratch/msw_triple_cycle_formula_m3_m10_report.json`.

## 3. An explicit near-perfect row-disjoint packet

The linear supply in Theorem 2 can be organized without solving a matching
problem.  Partition the $2m$ step positions into the aligned blocks

$$
[0,3],[4,7],\ldots .
$$

For a Dyck word $x$, locate its first aligned block equal to $1100$ or
$1010$ and toggle that block.  If no such block exists, leave $x$ unmatched.

### Theorem 3 (aligned-block matching)

The first-block rule is an involution on its matched Dyck words, and every
matched pair is one of the same-start inverse-triple trades of Theorem 2.
It therefore gives a row-disjoint exact trade packet.  If $U_m$ is its number
of unmatched rows, then

$$
U_m\le 14^{\lfloor m/2\rfloor}
       2^{2m-4\lfloor m/2\rfloor},
$$

and hence

$$
{U_m\over C_m}
=O\!\left(m^{3/2}(7/8)^{\lfloor m/2\rfloor}\right)=o(1). \tag{3.1}
$$

Thus the packet covers $(1-o(1))C_m$ MSW rows by mutually row-disjoint
exact inverse-triple trades.

The same statement holds for each of the four translated block partitions
with starts congruent to $s\pmod4$, $s\in\{0,1,2,3\}$.  If that partition
contains $b_s$ full blocks, its elementary unmatched bound is
$14^{b_s}2^{2m-4b_s}$, which has the same exponentially vanishing ratio.

#### Proof

Both $1100$ and $1010$ are balanced four-step Dyck excursions.  Replacing
one by the other preserves the height before and after the block and never
goes below the block's starting height, so it preserves the Dyck property.
All earlier aligned blocks are unchanged and the selected block remains
eligible.  The first-block rule is therefore an involution.  Deleting the
selected balanced block leaves a Dyck word of semilength $m-2$, so Theorem 2
identifies the pair with a same-start inverse-triple trade.

An unmatched word avoids two of the sixteen binary patterns in each of
$\lfloor m/2\rfloor$ disjoint four-bit blocks.  Ignoring the Dyck and weight
conditions gives the stated upper bound.  Dividing by
$C_m\asymp4^m/m^{3/2}$ proves (3.1). QED.

The literal generator is `scratch/msw_dyck_trade_matching.py`.  It does not
use the favorable orientation of individual trades and does not perform a
search.

The exact aggregate quadratic effect, including every cross-trade term, was
evaluated for all four translated partitions.  The best translated packet is:

| $m$ | offset | trades | matched rows / $C_m$ | individual favorable / bad | aggregate weighted CPCR change |
|---:|---:|---:|---:|---:|---:|
| 3 | 1 | 1 | $2/5$ | $0/0$ | $0$ |
| 4 | 2 | 2 | $4/14$ | $2/0$ | $-10/3$ |
| 5 | 3 | 5 | $10/42$ | $5/0$ | $-53/4$ |
| 6 | 2 | 24 | $48/132$ | $24/0$ | $-6695/66$ |
| 7 | 2 | 100 | $200/429$ | $91/9$ | $-888085/1708$ |
| 8 | 2 | 320 | $640/1430$ | $320/0$ | $-68666999/18690$ |
| 9 | 2 | 1284 | $2568/4862$ | $1213/71$ | $-7451856887/412965$ |
| 10 | 2 | 4344 | $8688/16796$ | $4344/0$ | $-121804742015251/1316117730$ |

Consequently a deterministic translated packet is improving for every
audited $4\le m\le10$ and neutral at $m=3$.  At odd $m=7,9$ the best packet
deliberately includes some individually bad trades; the full simultaneous
change is nevertheless negative after positive cross-interaction is charged.
For even $m=4,6,8,10$, every trade in the best offset-two packet is itself
favorable.  These sign statements are **finite evidence**, not part of
Theorem 3.  Proving an eventual negative aggregate sign, or an explicit
parity-dependent phase rule with a provable sign, is now a sharply specified
compensation problem.

The complete audit is generated by
`scratch/audit_msw_dyck_trade_matching.py --all-offsets` and stored in
`scratch/msw_dyck_trade_matching_offsets_m3_m10_report.json`.  The offset-zero
baseline remains in `scratch/msw_dyck_trade_matching_m3_m10_report.json`.

## 4. Most MSW cycles have favorable quadratic orientation

For a trade with depth-load change $\delta_q$, the exact identity is

$$
\Delta\operatorname{CPCR}_q
=\langle\mu_q,\delta_q\rangle+{1\over2}\|\delta_q\|_2^2. \tag{4.1}
$$

`scratch/local_trade_shadow_evaluator.py` caches the base loads and evaluates
(4.1) from the changed rows only.  It agrees exactly with the full terminal
factor evaluator in the regression suite.

The canonical audit is:

| $m$ | cycles | favorable | greedy disjoint cycles | rows covered | relative CPCR drop |
|---:|---:|---:|---:|---:|---:|
| 4 | 14 | 8 | 4 | .571 | .314 |
| 5 | 45 | 35 | 19 | .905 | .162 |
| 6 | 154 | 138 | 59 | .894 | .158 |
| 7 | 546 | 502 | 198 | .923 | .137 |
| 8 | 1980 | 1842 | 665 | .930 | .119 |
| 9 | 7293 | 6863 | 2307 | .949 | .107 |
| 10 | 27170 | 25762 | 8081 | .962 | .0958 |

Here cycles are sorted by individual weighted CPCR change and greedily
packed subject to disjoint factor rows.  The displayed drop is recomputed
for the **simultaneous** literal trade, so it includes all cross-trade noise;
it is not the sum of individual gains.  From $m=6$ onward the observed drop
is approximately $0.96/m$ of the starting weighted CPCR.

The complete exact fractions and per-depth signs are in
`scratch/msw_triple_compensation_m3_m10_report.json`, generated by
`scratch/audit_msw_triple_compensation.py`.

## 5. Exact descent and the remaining compensation gate

`scratch/greedy_triple_cycle_descent.py` applies row-disjoint packs as single
exact trades.  If cross-noise erases the maximal pack, it scans
strongest-first prefixes; a favorable singleton guarantees a strict descent.
Every intermediate object is therefore an exact wreath factor.
For a canonical generated MSW seed, the option
`--initial-aligned-block-packet` evaluates the four translated packets,
selects the best literal aggregate change (or a prescribed
`--aligned-block-offset`), and applies it exactly when that change is
negative; the replay certificate records this as round zero.

At $m=8$, pure triple descent eventually reaches a state with no favorable
triple cycle.  That state is not a mixed-atlas minimum: it has two favorable
adjacent cycles, three favorable one-junction paths, and ten favorable
multi-junction port cycles.  The best mixed move has compensation margin

$$
{1,104,907\over3115}>0.
$$

`scratch/greedy_structural_compensation_descent.py` then continues exact
descent over the full theorem-driven atlas.  It can pack a strongest-first
row-disjoint family and recomputes the full aggregate cross-noise before
applying it; if the full pack loses its gain, a prefix scan recovers a
favorable exact subpack.  At the audited $m=8$ state, 41 of 45 favorable
structural trades are row-disjoint and their simultaneous change remains

$$
-{1,446,409\over9345}<0.
$$

This is the first finite example
in which the hierarchy

$$
\text{triple cycles}\to\text{carrier paths}\to\text{multi-junction cycles}
$$

is needed at a nontrivial scale rather than only at $m=4,5$.

This does **not** prove MWB.  The missing theorem is a persistent version of
the observed drift: whenever the weighted defect is $\Omega(W)$, a
row-compatible structural family must have aggregate coherent gain exceeding
its full cross-noise by a quantitatively useful amount.  The present result
proves that the required supply exists and is favorably oriented at the MSW
seed through $m=10$; it does not prove that this remains true along an
arbitrary descent trajectory.

The fixed-slot strengthening is developed separately in
`MATH_THEOREM_MSW_FIXED_SLOT_COMPENSATION_CUBE_20260727.md`.  It replaces the
row-disjoint packet by an exact commuting Boolean cube, identifies an explicit
parity-core vertex which decreases every audited depth simultaneously, and
reduces the first all-$m$ sign to a four-class Catalan histogram at slot two.
