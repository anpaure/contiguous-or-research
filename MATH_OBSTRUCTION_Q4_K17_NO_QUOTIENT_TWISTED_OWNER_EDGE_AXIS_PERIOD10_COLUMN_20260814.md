# No q4 k17 quotient-twisted period-ten column has an owner edge-axis reflection

**Date:** 2026-08-14
**Status:** exact finite theorem for quotient-simple period-ten q4 columns
whose induced reflection action on owner starts is a dihedral edge axis.
The translating lift is allowed to depend on the owner row.  Nondihedral
quotient-self actions are not classified.

## 0. Result

Put the ground on `Z_17`.  A q4 period-ten column consists of a five-core
`C`, a cyclic order `s_0,...,s_9` of ten distinct labels outside `C`, and
the ten rank-nine owners

```text
O_i = C union {s_i,s_(i+1),s_(i+2),s_(i+3)}.       (0.1)
```

Assume their translation necklaces are distinct.  Reflection acts on an
owner necklace by `[O] -> [-O]`.  A quotient-twisted self column need only
satisfy

```text
-O_i + t_i = O_pi(i)                               (0.2)
```

for row-dependent translations `t_i`; no common affine lift is imposed.

There is no such column with the owner edge-axis action

```text
                         pi(i)=1-i mod 10.          (0.3)
```

Equivalently, no quotient-simple q4 period-ten column has a reflection
with zero fixed owner starts and the two owner-cycle edges `(0,1)` and
`(5,6)` fixed.  Consequently the proposed quotient-twisted class with
signature

```text
                 0 fixed owner bracelets,
                 2 fixed immediate-lower bracelets                (0.4)
```

cannot arise from an owner edge axis: the owner condition already fails
before lower tickets are inspected.

The complete normalized census is

```text
canonical five-core necklaces                         364
reflected adjacent boundary words                  188160
disjoint pairs of boundary words                  2115072
owner-necklace-nonsimple pairs                      173440
quotient-simple pairs                              1941632
full owner edge-axis columns                             0.       (0.5)
```

For the three owner pairs not forced by the boundary words, the exact
truth-pattern histogram on the `1,941,632` quotient-simple candidates is

```text
000: 1940480,
001:     384,
010:     384,
100:     384,                                         (0.6)
```

and every other pattern, including `111`, has count zero.

## 1. Exact normalization

Translation acts freely on five-subsets of `Z_17`: invariance under a
nonzero translation would force a nonempty proper subset to be a union of
orbits of the prime-order translation.  Hence every five-core has a unique
canonical translate, and there are

```text
                         binom(17,5)/17 = 364        (1.1)
```

canonical core necklaces.

Every dihedral reflection of the ten owner starts has form
`i -> a-i`.  The edge-axis cases are exactly odd `a`.  Rotating the cyclic
order by `k` changes `a` to `a-2k`; for odd `a`, one can choose `k` so the
new parameter is `1`.  Thus `(0.3)` loses no edge-axis column.

Under `(0.3)`, the five owner pairs are

```text
(0,1), (2,9), (3,8), (4,7), (5,6).                 (1.2)
```

The first and last pairs involve adjacent starts.  Define the two boundary
words

```text
u=(s0,s1,s2,s3,s4),
v=(s5,s6,s7,s8,s9).                                (1.3)
```

Then `(0.2)` for `(0,1)` is exactly

```text
[ -(C union {s0,s1,s2,s3}) ]
   = [ C union {s1,s2,s3,s4} ],                    (1.4)
```

and the same boundary equation for `v` is exactly the `(5,6)` relation.
The support labels are distinct precisely when `u` and `v` are internally
simple and have disjoint label sets.  Thus every normalized edge-axis
column occurs in the finite boundary-pair enumeration, and every retained
boundary pair is a literal q4 period-ten column candidate.

## 2. Exhaustive owner obstruction

For each of the `364` canonical cores, enumerate all ordered simple
five-label words outside the core and retain exactly those satisfying
`(1.4)`.  This gives `188160` words.  Pair every two retained words over
the same core and retain disjoint supports, giving `2115072` candidates.

Computing the ten owner necklaces in `(0.1)` removes `173440` candidates
with repeated owner rows.  The two boundary equations already certify the
first and last pairs in `(1.2)`.  The independent replay tests the remaining
relations in the order

```text
[ -O2 ]=[O9], [ -O3 ]=[O8], [ -O4 ]=[O7].          (2.1)
```

Their histogram is `(0.6)`.  In particular no candidate satisfies all
three, proving `(0.3)` is impossible.

The test uses canonical translation representatives for every owner
equality.  Therefore the translations in `(0.2)` are completely free and
may vary with `i`; the obstruction is genuinely quotient-twisted and is
not the earlier common-lift obstruction.

## 3. Consequence for the reflection bracelet master

The frozen globally lifted vertex-axis family supplies self columns with
two fixed owner bracelets and zero fixed immediate-lower bracelets.  The
strong half-turn family supplies zero and zero.  The natural hoped-for
complement was an edge-axis quotient-twisted family with zero fixed owners
and two fixed lower bracelets.  Theorem `(0.3)` rules out that entire
owner-action class.

This does not prove the full quotient-self lower obstruction.  A
quotient-self column may induce a nondihedral involution on its ten owner
necklaces because row-dependent translations need not preserve the
physical owner-cycle adjacency.  Such a column could in principle have a
useful fixed-row signature.  The remaining escape is therefore exactly:

```text
a nondihedral quotient-self column with at least one fixed lower bracelet,
or a construction that breaks reflection / transports lower tickets later.
```

## 4. Scope

Proved here:

* complete translation and cyclic normalization of dihedral owner
  edge-axis columns;
* complete boundary-word and disjoint-pair enumeration;
* quotient simplicity and all five owner reflection relations; and
* the empty target catalogue even with row-dependent translating lifts.

Not proved here:

* classification of nondihedral induced owner involutions;
* feasibility of the 750-row owner bracelet master; or
* any joint owner/lower exact cover.

All enumeration, replay, compilation, and hashing are performed on H100.
