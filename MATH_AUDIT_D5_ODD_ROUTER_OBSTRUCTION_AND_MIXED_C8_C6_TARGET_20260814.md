# Independent audit: odd-router obstruction for clean full-port reset boxes

**Date:** 2026-08-14
**Audited note:**
`MATH_OBSTRUCTION_D5_THREE_STATE_RESET_NEEDS_AN_ODD_ROUTER_NOT_A_CLOSED_C6_TUBE_20260814.md`
**Verdict:** **PASS.**  The current audited bytes contain all scope and
composition repairs recorded below.  The clean full-port parity obstruction
and displayed `S_4` factorization are correct.  They do not rule out a
marked-socket C6 quotient or a global all-C6 realization of the complete
even D5 matching permutation.

## 1. What passes unchanged

### 1.1 Clean full-port parity

In the clean full-port private switchbox architecture, a nontrivial D5 row
has a tail state `a` and old/new head states `b,c`.  Encapsulating that row
while fixing the tail port asks for `(bc)`, an odd permutation.

An alternating incidence `C_(2h)` acts on its `h` strands by an `h`-cycle,
of sign `(-1)^(h-1)`.  Every C6 strand action is therefore a three-cycle and
is even.  Products, inverses, and conjugates remain even.  This proves:

\[
 \boxed{\text{a clean full-port tail-fixed reset box cannot be composed
 only from C6 routers}.}                               \tag{1.1}
\]

The qualifier is essential: the even three-cycle `(b u c)` has marked
first-return quotient `(b c)` on `{b,c}`.  The known two-stage physical C6
carrier is nevertheless ruled out sharply: its
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

## 2. First applied repair: “odd-action,” not “available”

The owner/lower containment graph has C6 alternating cycles.  The corrected
source therefore uses the proof-safe statement:

> The containment graph is C4-free; C6 is the first alternating geometry
> but has even port action.  Hence C8 is the smallest available
> **odd-action simple alternating-cycle router**.

It likewise calls C8 the first possible **odd-action** alternating incidence
cycle, not the first possible alternating incidence cycle.

## 3. Second applied repair: order of the factors

Under the note's explicit right-factor-first convention, `rho tau` means

```text
C6 tau, followed by C8 rho.                              (3.1)
```

The corrected prose states exactly this operational order.  The abstract
phrase “mixed C8--C6” remains order-neutral.

## 4. Third applied repair: minimality is architecture-relative

A single C4 would have the desired transposition action, but C4 is forbidden
by the containment geometry.  A single C6 is even; a single C8 is a 4-cycle,
not a transposition.  Thus C6 plus C8 is the smallest serial product of
simple alternating-cycle routers that can realize `(bc)` on four terminals.

This does not prove absolute minimality among tapped, overlapping,
multi-boundary, or nonserial packets.  The source now confines the claim to
the serial full-port model, so the target remains a sufficient constant
local packet without an absolute-minimality overclaim.

## 5. Fourth applied and load-bearing repair: local versus global parity

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

The current source uses the proof-safe replacement:

> A clean full-port tail-fixed reset box needs odd full-port action, and the
> smallest serial simple-cycle-router target for such a box is a C6 followed
> by a C8 under the displayed convention.  Marked-socket C6 quotients and a
> global open-C6 atlas remain algebraically possible.

This is the necessary scope distinction, not a challenge to the local
transposition theorem.

## 6. Exact surviving conclusion

After the repairs, the note proves the useful dichotomy

\[
\boxed{
\begin{array}{l}
\text{clean full-port reset: mixed odd/even router required;}\\
\text{marked quotient or global atlas: all-C6 parity remains open.}
\end{array}}
\tag{6.1}
\]

The mixed C8--C6 full-port target is still conditional on one
state-independent simple owner/lower/upper bank, internal and terminal q2
residence, and support-monotone lower/upper currents.  Separately, the
existing complementary-square C8 and four heptagonal backups do supply a
closed marked-socket quotient with the internal rows proved; prescribed D5
terminal grafts remain outside that theorem.

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

The audited source SHA-256 is

```text
d8e1e8c36b577d2b8fbdb375e90bb4c789b3bc217de50081d1885a35fc0264cc.
```

It was rebound only after the full-port, factor-order,
architecture-relative minimality, marked-quotient, and global-parity scope
repairs were applied.
