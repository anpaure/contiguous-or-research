# The MSW chamber counter and the PBBS adjacent-necklace graph are different fibres

**Date:** 2026-08-05  
**Method:** exact comparison of the two parametrizations and parity counting;
no computation  
**Status:** unconditional scope and quantifier audit.

## 0. Verdict

The vertices of the adjacent-transfer necklace graph `G_(q,b)` are **not**
the missing-context cylinders in the canonical MSW upper-`q2` language, and
an edge of `G_(q,b)` is **not** the one-unit annulus carry proved for an MSW
incidence circulation.

The two constructions share a broad renewal intuition, but live in
different fibres:

* `G_(q,b)` parametrizes PBBS hook **component tori** of one fixed action
  `(h,1^b)`, with `q=2h-1`;
* the MSW chamber grammar parametrizes rank-`(r+2)` **q2 target words** and
  their ordinal inverse obstruction under `Gamma`.

A near-perfect matching in every `G_(q,b)` leaves at most one topology
socket **per hook-action fibre**, not one socket globally.  For fixed
semilength `m`, the hook fibres satisfy `h+b=m`, so there are `Theta(m)`
possible fibres.  Parity alone forces an unbounded number of sockets along
an infinite subsequence: when `m=2^t`, at least `t-1` hook fibres have odd
order.

These sockets are not q2 palette holes.  Every matched PBBS double ear is
q2-neutral, and an unmatched torus remains a represented factor component.
The proved named-hook spine is the separate cross-fibre mechanism intended
to consolidate the per-fibre topology sockets into one or two rails.  No
near-perfect necklace matching, by itself, repairs any canonical MSW q2
hole.

## 1. The two vertex sets

For a hook action `(h,1^b)`, put `q=2h-1`.  Its action-angle tori are

\[
 \mathcal N_{q,b}
 =\{(x_0,\ldots,x_{q-1})\in\mathbb Z_{\ge0}^q:
                          \sum_i x_i=b\}/C_q.                    \tag{1.1}
\]

The entries `x_i` count vacancy renewals in the `q` cyclic slots of one
fixed hook skeleton.  The graph `G_(q,b)` joins

\[
                         x\longmapsto x-e_j+e_{j+1}.              \tag{1.2}

\]

Under the separator encoding, this is one cyclically adjacent binary swap
`10 <-> 01`.

By contrast, a canonical MSW q2 target is a binary path `T` of length `2r`
ending at height four.  After cutting at the `D_2,D_3` barriers, every
productive chamber has ordinal intervals

\[
                         I_C=[A_C,A_C+a_C],\qquad
                         J_C=[B_C,B_C+b_C].                       \tag{1.3}

\]

The target is covered precisely when some common label in `I_C intersect
J_C` yields an internal Chung--Feller predecessor.  A missing-context
cylinder is a suffix class

\[
                         P\mathcal D                             \tag{1.4}

\]

of endpoint-height-four target words under a Dyck suffix, not a cyclic
weak-composition orbit.

There is no canonical map from (1.1) to (1.4):

1. one vertex of (1.1) is a factor component, whereas one element of
   (1.4) is a target colour;
2. a target may have many productive chambers, while a hook torus has one
   fixed cyclic vacancy vector;
3. (1.1) quotients the slot order cyclically, while the MSW inverse test
   uses distinguished left-prefix and right-suffix ordinal counters;
4. the parameters `(q,b)` record hook action and chip mass, not the signed
   chamber gap `A_C-B_C`.

One may fix extra rooted skeleton and chamber data and then express the MSW
counter as an affine function of selected vacancy counts.  Such a
projection is many-to-one and depends on the named chamber; it is not an
identification of the two vertex sets.

## 2. The edge operations are also different

An edge of `G_(q,b)` moves one vacancy chip between adjacent cyclic slots.
Its literal PBBS realization is one clean leaf-plucking C6; two aligned
physical copies form the q1/q2-neutral double ear that absorbs the two
child tori into a promoted parent.

The MSW annulus theorem starts instead with a complete signed incidence
circulation `Z` and a disjoint Johnson context move

\[
                         S\longmapsto S-a+b.                      \tag{2.1}

\]

It transports **every incidence of `Z`**.  The difference

\[
                         Z_{S-a+b}-Z_S                            \tag{2.2}

\]

is a sum of one transport hexagon per signed incidence.  For the frozen
two-hex `T_0` relay, `|supp Z|=12`, so one context move uses twelve
transport hexagons and the two Johnson moves of the `1100` carry use
twenty-four.

Moreover, the canonical context moves

```text
                         1100 -> 1001 -> 0011
```

are not adjacent binary swaps.  Thus even the literal generators differ.
The common phrase “move one renewal unit” does not turn a necklace edge
into an annulus carry.

## 3. What a near-perfect necklace matching leaves

For fixed semilength `m`, the hook profiles are

\[
                         (h,1^b),\qquad h+b=m.                    \tag{3.1}

\]

Suppose each `G_(2h-1,b)` has a matching of deficiency at most one.  Since
the fibres in (3.1) are disjoint, the direct union of these matchings has
deficiency

\[
             \sum_{h+b=m}\operatorname {def}
                         G_{2h-1,b},                              \tag{3.2}

\]

not the maximum of the summands.  Nothing in the per-fibre theorem bounds
(3.2) by a constant.

The parity formula for odd `q` is

\[
 |\mathcal N_{q,b}|\equiv {q+b-1\choose b}\pmod2,
 \qquad
 |\mathcal N_{q,b}|\text{ odd}
       \iff b\mathbin{\&}(q-1)=0.                                \tag{3.3}

\]

Take `m=2^t` and

\[
                         b=2^s-1,qquad1\le s\le t-1.             \tag{3.4}

\]

Then `h=m-b` and

\[
 q-1=2(h-1)
    =2\bigl((2^t-1)-b\bigr).                                    \tag{3.5}

\]

In the lowest `t` bits, `(2^t-1)-b` is the bitwise complement of `b`.
For (3.4), `b` has ones exactly in positions `0,...,s-1`, while the shifted
complement in (3.5) has ones only in positions at least `s+1`.  Hence

\[
                         b\mathbin{\&}(q-1)=0.                    \tag{3.6}

\]

All `t-1` fibres in (3.4) have odd order and every matching leaves at least
one vertex in each.  Therefore the direct per-fibre residual is at least

\[
                         t-1=\log_2m-1,                           \tag{3.7}

\]

which is unbounded.

This is a topology count, not a q2-defect count.  The clean C6 and aligned
double-ear identities preserve the q2 multiset exactly.  An unmatched
vertex in (3.2) is an unabsorbed factor cycle, not a missing target.

## 4. The correct cross-fibre implication

The hook reduction intentionally names the at-most-one unmatched torus in
each fibre.  Leaf promotion sends level `b` to level `b-1`, and the named
one-or-two-rail spine links these named roots across the profiles (3.1).
Conditional on the already stated literal halo-separation premises, that
cross-fibre spine converts the unbounded sum (3.2) into a bounded number of
global rails without creating q2 holes.

Thus the exact implication is

```text
near-perfect matching in every G_(q,b)
  + marked-port halo separation
  + named cross-fibre spine
      => bounded hook topology defect with q2 preserved.
```

It is **not**

```text
near-perfect matching in every G_(q,b)
      => O(1) canonical MSW q2 holes.
```

The MSW chamber repair and the PBBS hook matching remain complementary but
logically separate branches.  A future unified construction may use the
same global factor, but it still needs an explicit occurrence-level map
between their sockets; no such map is currently proved.

