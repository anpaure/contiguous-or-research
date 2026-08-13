# Independent audit: odd-router obstruction is exact only for row-private reset boxes

**Date:** 2026-08-14  
**Audited note:**
`MATH_OBSTRUCTION_D5_THREE_STATE_RESET_NEEDS_AN_ODD_ROUTER_NOT_A_CLOSED_C6_TUBE_20260814.md`  
**Verdict:** **FAIL as currently worded; PASS after four explicit scope and
composition repairs below.**  The row-local parity obstruction and the
displayed `S_4` factorization are correct.  They do not rule out a global
all-C6 realization of the complete even D5 matching permutation.

## 1. What passes unchanged

### 1.1 Row-local parity

In the private three-terminal switchbox architecture, a nontrivial D5 row
has a tail state `a` and old/new head states `b,c`.  Encapsulating that row
while fixing the tail port asks for `(bc)`, an odd permutation.

An alternating incidence `C_(2h)` acts on its `h` strands by an `h`-cycle,
of sign `(-1)^(h-1)`.  Every C6 strand action is therefore a three-cycle and
is even.  Products, inverses, and conjugates remain even.  This proves:

\[
 \boxed{\text{a row-private tail-fixed reset box cannot be composed only
 from C6 routers}.}                                    \tag{1.1}
\]

The known two-stage physical C6 carrier is the sharp immediate example: its
new stage actions are `tau^(-1),tau`, so its complete new action, like its old
action, is identity.

### 1.2 The explicit mixed factorization

On `{a,b,c,d}` put

\[
                 \rho=(a\ b\ c\ d),\qquad
                 \tau=(a\ d\ c).                       \tag{1.2}
\]

With right factors acting first,

\[
                         \rho\tau=(b\ c).                \tag{1.3}
\]

Indeed `a,d` are fixed and `b,c` are exchanged.  The cycle algebra is exact.
Operationally, `(1.3)` applies the C6 action `tau` first and the C8 action
`rho` second.

### 1.3 Frozen carrier replay

The cited H100 replay supports every finite carrier count in Section 3 of
the note:

```text
owners                         33 occurrences / 33 distinct, old=new
immediate-upper colours        30 occurrences / 30 distinct, old=new
immediate-lower tickets        30 occurrences / 26 distinct, old=new
ticket multiplicities          24 x 1, 2 x 3
internal lower/upper residence PASS/PASS in both states
linear lower q2 support losses 6
linear upper q2 support losses 3
terminal-crossing collars      not audited.
```

At the one-stage level, each displayed C6 stage has 12 lower-ticket
occurrences but only 10 values: nine singleton tickets and its exit common
core repeated on all three rows.  Each stage loses three internal lower-q2
targets.  Thus the note's warning that a future C6 half needs ticket
desingularization and q2 repair is supported directly, not merely inferred
from the two-stage total.

## 2. First required repair: “odd-action,” not “available”

The owner/lower containment graph has C6 alternating cycles.  Therefore the
sentence

```text
the smallest incidence geometry available ... is a C8
```

is false literally.  What is true is:

> The containment graph is C4-free; C6 is the first alternating geometry
> but has even port action.  Hence C8 is the smallest available
> **odd-action simple alternating-cycle router**.

The final sentence must likewise say “C8 is the first possible
**odd-action** alternating incidence cycle,” not the first possible
alternating incidence cycle.

## 3. Second required repair: order of the factors

Under the note's explicit right-factor-first convention, `rho tau` means

```text
C6 tau, followed by C8 rho.                              (3.1)
```

The prose currently says “a C8 router followed by a C6 router.”  Reverse
that prose, or provide a new factorization in the desired operational order.
The abstract phrase “mixed C8--C6” is order-neutral and needs no change.

## 4. Third required repair: minimality is architecture-relative

A single C4 would have the desired transposition action, but C4 is forbidden
by the containment geometry.  A single C6 is even; a single C8 is a 4-cycle,
not a transposition.  Thus C6 plus C8 is the smallest serial product of
simple alternating-cycle routers that can realize `(bc)` on four terminals.

This does not prove absolute minimality among tapped, overlapping,
multi-boundary, or nonserial packets.  Replace

```text
the correct smallest topology target
```

by

```text
the smallest serial simple-cycle-router target.          (4.1)
```

The target remains a sufficient constant local packet after this
qualification.

## 5. Fourth and load-bearing repair: local versus global parity

The three-colouring makes `(bc)` the action of the chosen **row-private
encapsulation**.  It does not prove that every D5 architecture must
encapsulate each row independently.

The actual frozen D5 matching permutation is the product of 41 disjoint
circuit cycles on 477 changed rows.  Its sign is

\[
       (-1)^{\sum_Q(|Q|-1)}=(-1)^{477-41}=(-1)^{436}=+1. \tag{5.1}
\]

The exact owner-cycle length histogram is

```text
9:6, 10:6, 11:11, 12:6, 13:4, 14:3, 15:4, 16:1.        (5.2)
```

Exactly 16 circuit permutations are odd, so their product is even.  Since
three-cycles generate every alternating group, parity alone does not exclude
a global network of open C6 routers realizing the whole D5 permutation.
Literal resource geometry may still obstruct such a network, but Theorem
1.1 does not.

Accordingly the following phrases need a `row-private` qualifier:

```text
The D5 reset needs an odd router.
Theorem 1.1 rules out all-C6 topology.
A future construction must introduce an odd router.      (5.3)
```

A proof-safe replacement is:

> A row-private tail-fixed three-state reset box needs an odd router, and
> the smallest serial simple-cycle-router target for such a box is a C6
> followed by a C8 under the displayed convention.  A global open-C6 atlas
> remains algebraically possible because the complete D5 permutation is
> even.

This is a scope repair, not a challenge to the local transposition theorem.

## 6. Exact surviving conclusion

After the four repairs, the note proves the useful dichotomy

\[
\boxed{
\begin{array}{l}
\text{row-private reset: mixed odd/even router required;}\\
\text{global reset atlas: all-C6 parity remains open.}
\end{array}}
\tag{6.1}
\]

The mixed C8--C6 target is still conditional on one state-independent simple
owner/lower/upper bank, internal and terminal q2 residence, and
support-monotone lower/upper currents.  No existing C8 resident tensor cited
in the repository automatically supplies the needed open four-strand
monodromy: the known coatom path tensors close to common endpoints and would
need a new open-router interface.

## 7. H100 binding

The independent replay was extended to verify the individual C6 stages and
the complete D5 permutation parity.  All execution and hashing occurred on
H100.  The verifier consumes the frozen selection SHA-256

```text
94deb656dac1d8955b20d851e92600156d703842d6de169d4b6bea356fa3ec32.
```

Its source/output SHA-256 values are

```text
bbb1fd5236cd9e0e8b67b7b756dfcd55b94281656aef8bdd36435a77a732d44e
5ea04cc7d43220b96c315d754f49151a9cf4a2cd472a0b28b792ce53e20b4d73.
```

No PASS digest is assigned to the audited note until the four wording and
scope repairs are applied.
