# A clean full-port D5 row reset needs odd action; the closed C6 tube is identity

**Date:** 2026-08-14
**Status:** exact obstruction and corrected finite target.  It rules out a
tempting reuse of the known closed two-C6 carrier and identifies an existing
resident C8 as an abstract marked-socket model.  Prescribed D5 terminal
identification and simultaneous embedding remain open.

## 0. Outcome

The frozen D5 union graph is exactly three-colourable.  At every nontrivial
changed row, the tail has one state `a in {0,1,2}` and the old/new heads are
the other two states.  The required local action is therefore the
tail-fixed transposition

\[
                       (bc),\qquad \{a,b,c\}=\{0,1,2\}.
\tag{0.1}
\]

The literal common-core C6 carrier from
`MATH_ATTACK_O_PHYSICAL_COMMON_CORE_C6_CARRIER_PACKET_20260726.md` cannot
implement `(0.1)`.  Its two router stages have opposite three-cycle
monodromies and hence total identity.  More generally, a composition of
C6 three-cycle routers acting on the same complete three-port set lies in
`A_3`; a transposition does not.

Thus a **clean full-port** row-private D5 box, in which the D5 terminals are
the complete invariant port set and every auxiliary port is fixed, needs an
odd full-port action.  A C4 would already induce a transposition, but the
middle-levels incidence graph has no C4.  The smallest available odd-action
alternating incidence geometry is therefore a C8 router.  If all four outer
ports must be fixed literally except for `b,c`, a 4-cycle and a 3-cycle can
have product `(bc)` while fixing a tail `a` and a dummy port `d`; within that
serial full-port model the smallest mixed target is a C8--C6 tube.

Parity does **not** survive a marked first-return quotient.  The even C6
action `(b u c)` induces `(b c)` when only `b,c` are marked.  Hence neither
row-private boxes in general nor C6 marked-socket quotients are excluded.

This is not a global parity obstruction.  The complete frozen D5
permutation is even, so a coordinated atlas of open C6 routers is not ruled
out; what fails here is the proposed closed inverse-C6 tube and, more
generally, a clean full-port all-C6 box with fixed auxiliaries.

## 1. Exact parity obstruction

Suppress the internal vertices of a fixed-bank `h`-strand router and record
the permutation carrying its input ports to its output ports.  An
alternating incidence `C_(2h)` replaces one matching by the other around
the cycle.  With a suitable orientation its port action is an `h`-cycle.
Its sign is

\[
                             (-1)^{h-1}.
\tag{1.1}
\]

Hence a C6 router (`h=3`) has even action, while a C8 router (`h=4`) has odd
action.

### Theorem 1.1 (clean full-port all-C6 boxes cannot realize the reset)

Any clean full-port packet composed only of C6 port routers, with arbitrary
inversions and conjugations, has even monodromy on its complete invariant
port set.  If every auxiliary port is fixed, it cannot realize `(bc)`.

The known physical two-stage C6 carrier has actions `tau` and `tau^{-1}`;
both its old and new outer monodromies are the identity.

#### Proof

Every C6 action is a three-cycle and therefore even.  Products, inverses,
and conjugates of even permutations remain even.  Fixing every auxiliary
port would leave the odd action `(bc)` on the complete port set.  In the
cited packet the two displayed stage actions multiply to
`tau tau^{-1}=1`, giving the final sentence. `square`

Without the clean-ancilla hypothesis the marked quotient of `(b u c)` is
a counterexample to the broader claim.

This is not merely a residence or palette defect: suppressing the complete
known tube recovers the identity boundary assignment, so no choice of
clock labels can turn it into the selected D5 incidence toggle.

## 2. The full-port serial parity-correct topology

Introduce a dummy port `d`.  On `{a,b,c,d}`, let

\[
                       \rho=(a\ b\ c\ d),
\tag{2.1}
\]

and let

\[
                       \tau=(a\ d\ c).
\tag{2.2}
\]

With the convention that the right factor acts first,

\[
                       \rho\tau=(b\ c).
\tag{2.3}
\]

Indeed, applying `tau` and then `rho` sends

\[
 a\mapsto d\mapsto a,\qquad
 d\mapsto c\mapsto d,\qquad
 b\mapsto b\mapsto c,\qquad
 c\mapsto a\mapsto b.
\tag{2.4}
\]

Thus `a,d` are fixed and `b,c` are exchanged.

Thus a C6 router followed by a C8 router has exactly the required abstract
terminal action while fixing `a,d`.

Equations `(2.1)--(2.4)` are only permutation algebra.  A physical packet must use
one common owner/lower/upper bank in its pass and swap states, keep its
terminal collars q2-resident, and preserve q2 support.

## 3. Why the known C6 carrier still cannot serve as the C6 half unchecked

Independent H100 replay of the known closed carrier confirms its literal
owner/upper formulas, but exposes three resource defects relevant to D5.

1. The 33 owners and 30 immediate-upper colours are simple and equal in
   the old/new states.
2. The derived immediate-lower ticket multiset is old/new equal but is not
   simple: only 26 distinct values occur among 30 tickets, with
   multiplicity profile `24 times 1, 2 times 3`.
3. Its internal linear q2 currents lose six lower/intersection targets and
   three upper/union targets.  Internal residence passes away from the
   terminals, but terminal-crossing collars were not audited.

Therefore even the C6 half of a future mixed tube needs ticket
desingularization and explicit q2 backups.  Fixed equality of the raw
owner/upper multisets is not the full D5 resource interface.

## 4. A previously proved C8 already closes the abstract internal gate

The complementary-square actuator in
`MATH_THEOREM_COMMON_MATE_C8_COMPLEMENTARY_SQUARE_RESIDENT_ALLWIDTH_HOST_20260813.md`
is stronger than the bare permutation factorization above.  It consists of
four closed, resource-simple protected cycles.  In its pass state the
first-return permutation on the alternating marked sockets `R_0,R_2` is
the identity; after its C8 switch it is `(R_0 R_2)`.  Both states use the
same owner, immediate-lower, and immediate-upper banks, are two-sided
resident, and have zero owner-union current at every width.

Adjoining an untouched spectator wire labelled by the tail state `a` turns
this into the abstract action

\[
                         1_a\times(b\ c).             \tag{4.1}
\]

Together with the four heptagonal backups in
`MATH_REDUCTION_D5_ROW_RESET_TO_PRESCRIBED_TERMINAL_RESIDENT_C8_QUOTIENT_20260814.md`,
the internal permutation, simplicity, residence, and both lower/upper q2
support rows of the row-private D5 reset interface have a certified model.
What is not automatic is identifying the two private marked sockets and the
spectator with the prescribed D5 owner occurrences while preserving their
external collars.  Nor has a collision-free simultaneous embedding of all
212 prescribed reset rows been proved.  Since 212 is constant, any such
embedding would still have `O(m)` protected incidences and `O(1)` exposure,
inside the quantitative range of the protected coinstantiation theorem.

Thus the sharp row-private gate is now

\[
\boxed{
\begin{array}{l}
\text{embed prescribed D5 tail/head occurrence triples into pairwise}\\
\text{resource-compatible copies of the resident all-width C8}\\
\text{alternating-socket quotient, including every external q2 collar.}
\end{array}}
\tag{4.2}
\]

This is a terminal-identification/coinstantiation problem, not a missing
abstract odd switchbox.

## 5. Full-port serial alternative

The clean full-port serial route reduces to the following constant packet:

\[
\boxed{
\begin{array}{l}
\text{construct a mixed C8--C6 four-port tube realizing `(bc)` and}\\
\text{fixing tail `a` and dummy `d`, with one state-independent simple}\\
\text{owner/lower/upper bank, q2-safe internal and terminal collars, and}\\
\text{support-monotone lower/upper q2 currents.}
\end{array}}
\tag{5.1}
\]

Coordinate relabeling would then supply the three tail-state types in the
frozen D5 three-colouring, and occurrence-distinct tickets must handle the
external multiplicity-four roles.  Suppressing a valid tube would recover
the exact D5 toggle, hence retain the independently verified `372 -> 1`
component action.

The old two-history and arbitrary successor-tag clocks are already ruled
out by the frozen quotient obstruction.  Theorem 1.1 additionally rules out
an all-C6 clean full-port serial box.  Such a box must introduce an odd
router, with C8 the first possible odd-action alternating incidence cycle.
A row-private C6 marked-socket quotient is algebraically viable but has no
proved resident/resource-safe model; a globally coordinated open-C6 atlas
is another separate viable architecture.

## 6. Global open-C6 alternative

The frozen D5 circuit histogram is

```text
9:6, 10:6, 11:11, 12:6, 13:4, 14:3, 15:4, 16:1.
```

There are 25 odd-length cycles and 16 even-length cycles on 477 row
elements.  Decomposing each odd-length cycle internally into 3-cycles and
pairing the even-length cycles gives an algebraically minimal total of

\[
                  \frac{477-25}{2}=226               \tag{6.1}
\]

open C6 routers.  This avoids rowwise odd boxes, but it requires a globally
coordinated resource, chronology, and collar schedule; the closed inverse
C6 carrier does not provide one.

For completeness, if a permutation has `o` odd-length cycles, then one
3-cycle changes the number of odd cycles by at most two.  Hence at least
`(N-o)/2` 3-cycles are required.  An odd cycle of length `r` has the usual
`(r-1)/2`-term 3-cycle factorization, while two even cycles of lengths
`r,s` have a joint `(r+s)/2`-term factorization.  Pairing the sixteen even
cycles attains the lower bound in `(6.1)`.

## 7. Reproducibility

The independent H100 replay of the known C6 carrier has source SHA-256

`bbb1fd5236cd9e0e8b67b7b756dfcd55b94281656aef8bdd36435a77a732d44e`

and output SHA-256

`5ea04cc7d43220b96c315d754f49151a9cf4a2cd472a0b28b792ce53e20b4d73`.

The permutation-parity proof is symbolic and does not depend on the finite
replay.
