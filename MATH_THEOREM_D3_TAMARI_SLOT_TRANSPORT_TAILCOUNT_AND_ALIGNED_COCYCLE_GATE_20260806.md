# Tamari moves the `D_3` slot, but a tail-count invariant blocks the two-slot current loop

**Date:** 2026-08-06  
**Method:** pure mathematics; exact native-current and tensor-word algebra  
**Status:** unconditional no-go for the direct Tamari two-slot closure and
for resource-disjoint parallel cocycles with one fixed rail pair.  It does
not exclude a three-or-more-slot dynamic circuit, fragmented-row absorber,
or exterior current halo.

## 0. Verdict

The port-restored Tamari associator can be relabelled so that its `A--L`
negative slot is any chosen endpoint-sealed companion edge of the suspended
`D_3` pentagon.  It then transports that edge to a genuinely different
native slot while paying zero q1 current itself.

This does **not** close a native-current loop.  With a nonempty tensor tail
of semilength `s`, the old Tamari slot has two q1 claims containing exactly
`s-1` protected tail coordinates.  Every q1 claim of the transported slot
contains exactly `s` protected tail coordinates.  Therefore the two native
slot currents are linearly independent, even if either move is reversed and
even after arbitrary relabelling of the base coordinates.

There is a second exact obstruction.  Every native inverse-pair packet with
fixed `X` bank and fixed four-label active set already uses all six central
owners

\[
                         X+\binom A2.                         \tag{0.1}
\]

Consequently two whole aligned packets cannot coexist resource-disjointly.
Thus a fixed-rail cocycle identity, including the natural `D_3` automorphism
square, is algebraically valid but cannot be implemented by simply packing
its whole native packets in parallel.  The independently audited fused
four-term square still has owner multiplicity three.

The exact next target is a changing-slot transport which also carries one
opposite truncated-tail claim, or a fragmented/exterior halo which absorbs
that claim.

## 1. Fixed-rail native packets saturate the full-`X` owner bank

Let

\[
 \begin{aligned}
 r_0&=(a,b,X,c,d,Y),\\
 r_1&=(b,d,X,a,c,Y),
 \end{aligned}                                                \tag{1.1}
\]

be a native inverse pair at semilength `m`, with `|X|=m-2`, and put

\[
                              A=\{a,b,c,d\}.                    \tag{1.2}
\]

### Lemma 1.1 (six-owner saturation)

Among the cyclic length-`m` intervals of the two rows in (1.1), the
intervals containing all of `X` are exactly

\[
 \begin{array}{c|c}
 r_0&X+ab,\quad X+bc,\quad X+cd,\\
 r_1&X+bd,\quad X+da,\quad X+ac.
 \end{array}                                                \tag{1.3}
\]

Hence every member of `X+binom(A,2)` occurs exactly once.

#### Proof

A cyclic length-`m=|X|+2` interval containing the whole consecutive block
`X` can extend it by only the two positions at its left boundary, one at
each boundary, or the two positions at its right boundary.  Reading those
three possibilities in each row gives (1.3).  The six displayed unordered
pairs are precisely the six two-subsets of `A`.  \(\square\)

### Corollary 1.2 (parallel aligned-cocycle no-go)

Two native old packets with the same ordered `X` bank and the same active
four-set `A` cannot both be partial packets of one simple exact factor:
their central owner ledgers collide on all six targets (0.1).

In particular, no nontrivial endpoint-label cocycle with fixed rails can be
implemented by a resource-disjoint union of its whole native packets.

This does not exclude algebraically cancelling identical rows first and
packing only the residual fragments.  For the natural `H=< (23),(45) >`
four-term `D_3` current square, that stronger fused possibility is ruled out
by
`MATH_THEOREM_D3_CONJUGATE_CURRENT_SQUARE_OWNER_MULTIPLICITY_OBSTRUCTION_20260806.md`:
after all row cancellations, each residual shore still has owner
multiplicity three.

## 2. Exact Tamari slot transport with a tensor tail

Use the negative and port-restored Tamari `A--L` normal forms.  At base
semilength four they are

\[
 \begin{aligned}
  \text{negative: }&X=(7,3),\quad Y=(5,2,1),
       \quad(a,d)=(8,4),\\
  \text{restored: }&X=(2,1),\quad Y=(7,3,\mathord\infty),
       \quad(a,d)=(6,4).
 \end{aligned}                                                \tag{2.1}
\]

Let

\[
                         U=(u_1,\ldots,u_s),\qquad
                         V=(v_1,\ldots,v_s)                    \tag{2.2}
\]

be respectively the deletion and insertion blocks of the common tensor
tail.  The exact tensor word `(D_P,D_S,I_P,I_S,infinity)`, cut at the
displayed native slot, gives

\[
 \begin{array}{c|c|c|c}
 &X&Y&(a,d)\\ \hline
 \text{negative}&(7,3,V)&(5,2,1,U)&(8,4)\\
 \text{restored}&(2,1,U)&(7,3,V,\mathord\infty)&(6,4).
 \end{array}                                                \tag{2.3}
\]

Thus the associator really changes the slot: both ordered rails and one
active endpoint change.  At the unguarded row-order level, any native normal
form of the same semilength is a coordinate relabelling of the negative line
in (2.3).  A literal overlap with a chosen sealed `D_3` edge additionally
requires that this relabelling respect the designated protected tail
subblocks and that the Tamari `C,D` helper rows coexist.  Theorem 3.1 is a
no-go even after granting those planting premises.

## 3. The q1 tail-count obstruction

For an inverse-pair slot `(X,Y;a,d)`, the immediate-upper q1 current is the
complement of the length-`m-1` current

\[
          [Y^++d]+[Y^-+a]-[Y^++a]-[Y^-+d],                   \tag{3.1}
\]

where `Y^-` and `Y^+` are respectively the prefix and suffix of `Y` of
length `m-2`.  The `X` rectangle vanishes at this width.

Here `m=s+4`.  For the negative slot in (2.3),

\[
 \begin{aligned}
 Y^-_-&=(5,2,1,u_1,\ldots,u_{s-1}),\\
 Y^+_-&=(2,1,u_1,\ldots,u_s).
 \end{aligned}                                                \tag{3.2}
\]

For the restored slot,

\[
 \begin{aligned}
 Y^-_*&=(7,3,v_1,\ldots,v_s),\\
 Y^+_*&=(3,v_1,\ldots,v_s,\mathord\infty).
 \end{aligned}                                                \tag{3.3}
\]

### Theorem 3.1 (Tamari two-slot q1 independence)

Assume `s>=1`, and treat `U union V` as the protected tail-coordinate bank.
Let `C^-` and `C^*` be the native q1 currents at the negative and restored
slots in (2.3).  Then

\[
                           \lambda C^-+\mu C^*=0               \tag{3.4}
\]

over `Q` or `Z` implies

\[
                           \lambda=\mu=0.                      \tag{3.5}
\]

The conclusion remains true after arbitrary permutation of the base
coordinates, after swapping or reversing the two protected tail blocks,
and after replacing either current by its negative.

#### Proof

Grade every target in (3.1) by the number of coordinates it contains from
the protected tail bank `U union V`.

In `C^-`, the two terms based on `Y^-_-` have tail grade `s-1`; explicitly
their grade-`s-1` projection is

\[
              [Y^-_-+8]-[Y^-_-+4],                           \tag{3.6}
\]

which is nonzero because `8!=4`.  The other two terms of `C^-` have grade
`s`.

Every term of `C^*` has tail grade `s`, by (3.3).  Therefore projecting
(3.4) to grade `s-1` forces `lambda=0`.  The four terms of `C^*` are
distinct, so `C^*` is nonzero and then `mu=0`.

Base relabelling cannot change tail grade.  Swapping or reversing `U,V`
also preserves their union and hence the grade.  Changing a sign does not
change support.  \(\square\)

### Corollary 3.2 (zero-q1 transport is not a zero-q1 native loop)

Even though the Tamari associator itself has zero q1 current, the circuit
consisting of a native move at its old slot and a signed native move at its
transported slot cannot have zero q1 current when the tensor tail is
nonempty.

Thus “zero-current host transport + two native slots” is insufficient; the
two native currents must still be audited, and in this case they cannot
cancel.

## 4. Relation to the corrected `D_3` phase skeleton

The endpoint theorem
`MATH_THEOREM_D3_PENTAGON_SEALED_COMPANION_MATCHINGS_AND_ENDPOINT_CYCLE_GATE_20260806.md`
gives the connected phase union

\[
                         \{12,54\}^-\cup\{14,32\}^+            \tag{4.1}
\]

with every displayed edge endpoint-sealed.  The current obstruction is now
strictly above that endpoint layer:

1. the four fixed persistent currents are linearly independent at all
   widths;
2. the automorphism current square cancels algebraically but fails physical
   owner capacity after row fusion;
3. whole fixed-rail packet packing is impossible by Lemma 1.1; and
4. the Tamari transported pair is already independent at q1 by Theorem 3.1.

Therefore the shortest currently viable constructions are:

* a third transported slot carrying the opposite grade-`s-1` claim;
* a fragmented-row realization which evades six-owner saturation;
* or an exterior halo whose physical claim bank contains that truncated
  tail ray.

Any positive dynamic circuit must explicitly cross one of these three
boundaries; connected companion supply and endpoint sealing alone do not.
