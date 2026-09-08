# Dense hook angles have a unique promoted port: a two-C6 jump no-go

**Date:** 2026-08-05  
**Method:** exact marked-double-zero inverse; no search  
**Status:** unconditional.  It rules out a uniform same-parent two-C6 lift
of an arbitrary-transposition necklace Gray code.  It does not rule out
long adjacent routing or higher q2-neutral circuits.

## 1. Exact promoted ports

For a base hook angle `y` of length

\[
                         q=2h-1
\]

and mass `b-1`, the leaf-plucking parent is

\[
                         z=\iota_j(y),
\tag{1.1}

obtained by inserting two consecutive zero entries at the selected cyclic
cut.  The exact marked-port inverse says that the unmarked leaf-plucking
ports of `z` are precisely its cyclic adjacent pairs of zero entries:
delete one such pair to recover the base angle and its cut.

### Lemma 1.1 (unique-port criterion)

If every entry of `y` is positive, then `z=iota_j(y)` has exactly one
promoted port, namely the inserted zero pair.

#### Proof

The two inserted entries are adjacent and zero.  Each of their two outer
neighbors is an entry of `y` and is positive; every other adjacent pair
lies entirely in `y` and contains two positive entries.  Thus there is
exactly one cyclic `00` pair.  The marked-port inverse completes the
claim.  `square`

## 2. A dense source has no two-port excursion

Let `x` be a hook angle of mass `b` satisfying

\[
                         x_i\ge2
                \qquad(0\le i<q).
\tag{2.1}

Every leaf-plucking C6 containing `x` as one of its two repeated-hook
shores first removes one chip at some occupied slot:

\[
                         y=x-e_i.
\tag{2.2}

By (2.1), `y` is still strictly positive.  Lemma 1.1 therefore says that
the promoted parent of this C6 has no second marked port.  A second C6 on
the same promoted parent either reuses the identical port/component triple
or is impossible.

Moreover `x` itself has no adjacent zero-entry pair, so it cannot serve as
a promoted parent for a downward/upward two-port excursion either.

### Theorem 2.1 (dense two-C6 no-go)

For every dense hook angle (2.1), a two-C6 compound made only from the
leaf-plucking family cannot realize a nonlocal hook-angle jump through one
common promoted parent.  If the second C6 instead continues from the
first sibling through a different parent, the compound is merely two
adjacent chip moves and has cyclic earthmover reach at most two.

Dense angles exist whenever

\[
                         b\ge2q=4h-2;
\tag{2.3}

for example take `x_i=2` and distribute any remaining chips arbitrarily.
Hence the obstruction occurs in infinitely many hook sectors.

## 3. Consequence for arbitrary-transposition Gray codes

An arbitrary bit/chip transposition can have unbounded cyclic transport
distance.  The one-C6 adjacency-uniqueness theorem already rules out a
direct lift.  Theorem 2.1 shows that adding a second leaf-plucking C6 and
asking it to use another port of the same promoted parent is not a uniform
repair: dense angles have no such port.

Therefore an arbitrary-transposition Gray cycle cannot be converted
edge-for-edge into bounded two-C6 leaf-plucking ears over all hook angles.
A successful use of that Gray cycle would require a new higher circuit,
or a compound whose length grows with the transported distance.  The
existing adjacent-chip connectedness theorem remains the exact universal
one-C6 reachability statement.

