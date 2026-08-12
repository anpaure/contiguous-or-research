# The terminal rigid braid has exact run lengths `m+1,m-1` and gap lengths `m,m+2`

**Date:** 2026-08-05  
**Method:** direct membership word on the `P_0/P_2` braid; no computation or
search  
**Status:** unconditional for `m>=4`.  The braid component created by the
full rigid rotation orbit is cyclically bi-resident through every deadline
`d<=m-2`, and therefore admits the standard depth-`d` cyclic source
factorization on that component.

## 1. Braid owner sequence

Let `n=2m+1`.  Index the `2n` owners on the braid by

\[
 O_h=
 \begin{cases}
  P_0(-h),&h\text{ even},\\
  P_2(-h),&h\text{ odd},
 \end{cases}
 \qquad h\in\mathbb Z_{2n}.                       \tag{1.1}
\]

This is the directed sequence

\[
 P_0(0),P_2(-1),P_0(-2),P_2(-3),\ldots           \tag{1.2}
\]

coming from the two-edge phase map `t->t-2`.

The two base shapes are

\[
 P_0=\{1,2,\ldots,m\},
 \qquad
 P_2=\{1,2,\ldots,m-1,m+1\}.                    \tag{1.3}
\]

## 2. Exact coordinate membership word

Fix a coordinate `z`.  At time `h`, put

\[
                         r_h=z+h\pmod n.           \tag{2.1}
\]

Then `r_(h+1)=r_h+1`, and

\[
 z\in O_h
 \iff
 \begin{cases}
 r_h\in\{1,\ldots,m\},&h\text{ even},\\
 r_h\in\{1,\ldots,m-1,m+1\},&h\text{ odd}.
 \end{cases}                                      \tag{2.2}
\]

During `2n` steps, every residue occurs once with each parity.  On one pass
through the residues, `r=m` occurs at even parity and `r=m+1` at odd parity;
both are present.  On the other pass their parities are reversed; both are
absent.  All residues `1,...,m-1` are always present, and all residues
`m+2,...,2m,0` are always absent.

### Theorem 2.1 (exact biresidence)

For every coordinate, the cyclic positive-run lengths on the braid are

\[
                         \boxed{m+1,\ m-1},        \tag{2.3}
\]

and the intervening zero-gap lengths are

\[
                         \boxed{m,\ m+2}.          \tag{2.4}
\]

The two runs and two gaps alternate around the `2n`-cycle.

#### Proof

On the first parity pass, residues `1,...,m+1` are present and the remaining
`m` residues are absent.  On the opposite-parity pass, precisely
`1,...,m-1` are present, followed by the two exceptional absent residues
`m,m+1` and the same `m` always-absent residues.  This gives (2.3)--(2.4).
Translation in `z` only rotates the word.  `square`

### Corollary 2.2 (deadline residence)

For every

\[
                         1\le d\le m-2,            \tag{2.5}
\]

every positive run and every zero gap has length at least `d+1`.

In particular the braid owner chronology satisfies the coordinatewise
depth-`d` factorization criterion and admits a cyclic antecedent `A` with

\[
                         D^dA=(O_h)_h.             \tag{2.6}
\]

It also satisfies the corresponding zero-gap residence condition.

## 3. Scope

This theorem closes residence and source factorization on the braid
component only.  It does not prove residence on the `gcd(n,3)` residual
two-soliton components, compatibility of the component antecedents at a
linear join, occurrence-cap compiler routing, arbitrary exterior upper
protection, or a constant-charge opening.

It combines with the braid all-depth support theorem, but it does not repair
the generalized full-rail payload equation: the latter asks for one
simultaneous common-history decoration of every moving `C6`, a strictly
stronger object than existence of an antecedent for the terminal braid.

## 4. Dependency

The braid order (1.1) is the first component in

`MATH_THEOREM_PBBS_RIGID_C6_SERIAL_ROTATION_ORBIT_TOPOLOGY_NOGO_20260805.md`.
