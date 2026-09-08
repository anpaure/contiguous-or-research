# A q4 seven-by-seven near-C owner atom exists on thirteen labels

**Date:** 2026-08-14
**Status:** exact named-owner theorem with independent H100 replay.  The
construction closes the q4 positive owner-semigroup atom gate.  It does not
claim that seven rails or thirteen labels are minimal in the unrestricted
model, and it does not yet supply typed palettes, residence, or global
factor topology.

## 0. Outcome

Let

\[
                   V=\{0,1,\ldots,12\},\qquad
                   H=\{0,1,2,3,4\}.
\]

There are seven positive and seven negative cyclic q4 rails of periods 10
and 11 whose owner decks are simple on each shore and satisfy

\[
       \sum_{Q\in\mathcal A^+}f(Q)
       =\sum_{Q\in\mathcal A^-}f(Q)+e_H.             \tag{0.1}
\]

The positive shore has 73 distinct owners and the negative shore has 72.
The construction has two layers:

1. five rails per shore leave exactly one four-owner Johnson rectangle;
2. two adjacent-transposition rail pairs telescope through one intermediate
   core and cancel that rectangle.

The second layer is symbolic and explains the witness; it is not a
solver-found opaque correction.

## 1. Rail notation

For a centre `c` and a cyclic word
`sigma=(s_0,...,s_(N-1))` of distinct labels avoiding `c`, put

\[
 R(c;\sigma)=
 \bigl(\{c,s_i,s_{i+1},s_{i+2},s_{i+3}\}\bigr)_{i\in\mathbb Z_N}.
                                                               \tag{1.1}
\]

Every consecutive pair in `(1.1)`, including the wrap pair, differs by
one deletion and one insertion.  Thus every displayed object below is a
closed Johnson cycle.

## 2. The five-rail near atom

Take the positive rails

```text
p10c4_1  centre 4:  7 10 11 3 0 5 8 9 1 2
p10c4_2  centre 4:  2 12 5 11 6 10 8 1 9 0
p11c0    centre 0:  12 11 1 10 6 5 8 9 3 4 2
p11c1    centre 1:  8 5 11 12 6 10 2 0 4 3 9
p11c2    centre 2:  6 0 8 9 1 12 3 7 10 11 5
```

and the negative rails

```text
n10c0    centre 0:  5 8 9 4 2 12 11 1 10 6
n10c1    centre 1:  12 6 10 2 0 4 9 8 5 11
n10c2    centre 2:  4 1 9 8 0 6 5 11 10 7
n11c3    centre 3:  1 9 8 5 0 4 11 10 7 2 12
n11c4    centre 4:  2 0 3 9 1 8 10 6 11 5 12.
```

Each shore is simple.  Define

```text
A = 2,   B = 3,
C1 = {0,4,8,9},
C2 = {1,8,9,12}.
```

Direct expansion of all cyclic four-windows gives the exact current

\[
 \mathcal D^+_5-\mathcal D^-_5
 =e_H-e_{C_1\cup\{A\}}+e_{C_1\cup\{B\}}
       +e_{C_2\cup\{A\}}-e_{C_2\cup\{B\}}.          \tag{2.1}
\]

Thus the only error is the balanced rectangle

\[
 \mathcal R(C_1,C_2)
 =-e_{C_1A}+e_{C_1B}+e_{C_2A}-e_{C_2B}.             \tag{2.2}
\]

## 3. The adjacent-transposition identity

Let `c,A,B` be distinct and let `L=(l_1,l_2,l_3)` and
`R=(r_1,r_2,r_3)` be disjoint triples avoiding them.  In any longer cyclic
word containing the consecutive segment

```text
                 l1 l2 l3 A B r1 r2 r3,
```

swap the adjacent labels `A,B`, leaving every other position fixed.  Every
cyclic four-window containing both or neither of them is unchanged.  The
only changed windows are

```text
L+A -> L+B,             B+R -> A+R.
```

Consequently, if `before` has `A B` and `after` has `B A`, then

\[
 f(R(c;\mathrm{after}))-f(R(c;\mathrm{before}))
 =-e_{(cL)A}+e_{(cL)B}+e_{(cR)A}-e_{(cR)B}.         \tag{3.1}
\]

This is an exact occurrence identity, not merely a point projection.

## 4. Two swaps telescope the rectangle

Put

\[
                    C_*=\{5,6,7,8\}.
\]

Use centre `8` and take the two positive `before` words

```text
pX1:  10 11 0 4 9 2 3 5 6 7
pX2:  10 11 5 6 7 2 3 1 9 12
```

and the two negative `after` words

```text
nX1:  10 11 0 4 9 3 2 5 6 7
nX2:  10 11 5 6 7 3 2 1 9 12.
```

For the first pair, `(3.1)` has endpoint cores `C1,C_*`; for the second it
has endpoint cores `C_*,C2`.  Because the positive shore uses `before` and
the negative shore uses `after`, their combined current is

\[
                 -\mathcal R(C_1,C_*)
                 -\mathcal R(C_*,C_2)
                 =-\mathcal R(C_1,C_2).             \tag{4.1}
\]

The two intermediate `C_*` terms cancel literally.  Adding `(4.1)` to
`(2.1)` proves `(0.1)`.

### Theorem 4.1 (exact owner equality and simplicity)

The fourteen displayed rails satisfy all of the following.

1. Every rail is a simple Johnson cycle of its stated period.
2. The seven positive decks are mutually disjoint, with 73 owners.
3. The seven negative decks are mutually disjoint, with 72 owners.
4. The negative owner set is contained in the positive owner set.
5. The set difference is exactly the single owner `H`.

The centre/toggle point-degree difference is consequently the indicator of
`H`; direct replay gives `(1,1,1,1,1,0,...,0)` on the thirteen labels.

## 5. Common-core lift

Let `C_0` be any set disjoint from `V`.  Replacing every reduced owner `Q`
by `C_0 union Q` preserves Johnson adjacency, cyclic orders, shore
simplicity, and every occurrence equality.  Hence

\[
 \sum_{Q\in\mathcal A^+}e_{C_0\cup Q}
 =\sum_{Q\in\mathcal A^-}e_{C_0\cup Q}+e_{C_0\cup H}.          \tag{5.1}
\]

Thus the certificate is a literal distance-one near-core one-owner atom at
every admissible ambient rank.

## 6. Independent H100 replay

The verifier imports no search code.  It rebuilds every cyclic owner deck,
checks all wrap edges and within-shore simplicity, expands the five-rail and
two-swap currents separately, verifies the telescoping identity, and checks
the complete named-owner and point-degree differences.

```text
scratch/verify_q4_v13_seven_by_seven_atom_20260814.py
SHA-256 a5f1d9d1224457ce48ebd38e6489123185f894d5d5f310ef1951e3f6d0d5c69a

H100 output
scratch/verify_q4_v13_seven_by_seven_atom_20260814.h100.out
SHA-256 400865dad6b0a2fef8da2b887f1ce2c62d015497126ffa8b40b48c242ec00bd2
```

Exact output:

```text
PASS q=4 ground=13 rails=7x7 positive_owners=73 negative_owners=72 shore_simple=yes difference=01234 rectangle_telescoped=yes
```

All computation and hashing were run via SSH on H100.  The local Mac was
used only for editing and Git.

## 7. Scope and next gate

The theorem closes the q4 named-owner semigroup atom gate.  It does not yet
prove equality or simplicity of immediate lower/upper colours, wider
windows, residence, or a connected factor topology.  As in the q3 theorem,
the next algebraic step is to place the atom as a positive common reserve
for the insertion/star one-owner macro, with a complete collision audit.

The five-rail minimum remains open: the best certified five-rail object in
this proof has precisely the rectangle `(2.2)`.  That optimization question
is no longer a prerequisite for q4 positivity.
