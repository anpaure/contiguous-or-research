# Native PBBS steps cannot realize the odd bridge, and two bad singleton gaps defeat the initial-envelope strategy

**Date:** 2026-08-06  
**Method:** rooted-Dyck two-step formula, exact terminal hook banks, and
cyclic run order; no computation or search  
**Status:** unconditional scoped no-go.  It proves that a terminal
two-soliton on an untouched PBBS component cannot change the hook step
parity, and that even an abstract odd-bridge generator does not by itself
close mixed singleton/nontrivial-run targets if all singleton payload is
required to live in the native initial envelope.

## 1. Universal parity of a native PBBS factor step

Let a rooted Dyck word be factored at the first maximum and its subsequent
first return as

\[
 D=P\,1\,R\,0\,S,
\tag{1.1}
\]

where `S` is a Dyck word.  The exact rooted PBBS formula is

\[
 \phi^2D=S\,1\,P\,0\,R,
\qquad
 q'=q-(|S|+1)\pmod n.
\tag{1.2}
\]

The sign in `(1.2)` uses the decreasing-root convention of the hook
notes.  Since every Dyck word has even length, write `|S|=2a`.  Then every
native step of the centered factor has the form

\[
 \boxed{q'=q-(2a+1).}
\tag{1.3}
\]

In particular its lifted root displacement is always odd.

### Theorem 1.1 (native odd-bridge no-go)

Suppose a one-edge source interface has an exit label `y` and exports the
next root one coordinate below it:

\[
 q'=y-1.
\tag{1.4}
\]

If the edge is an untouched PBBS factor edge, then necessarily

\[
 \boxed{y=q-2a,\qquad q'=q-(2a+1)}
\tag{1.5}
\]

for some `a>=0`.  Hence no native edge can realize

\[
 y=q-(2z+1),
 \qquad
 q'=q-(2z+2).
\tag{OB}
\]

#### Proof

Equation `(1.3)` and `(1.4)` give

\[
 q-y=(q-q')-1=2a.
\]

The odd span required in `(OB)` is impossible.  \(\square\)

This is independent of the PBBS action partition.  In particular replacing
two unit solitons by one length-two soliton may change the Dyck suffix `S`
and therefore the integer `a`, but `|S|` remains even.  The proposed
terminal near-hook formula

\[
 2z+1\longmapsto2z+2
\]

for the root step is false on every untouched component.  A physical odd
bridge must therefore be a genuinely rethreaded edge, a seam between
components, or another nonnative packet.  Merely moving to the action
sector `(h,2,1^{b-2})` cannot supply it.

## 2. What a native even bridge preloads into the initial envelope

Return to a height-`d+1` hook component.  On a lifted nonwrapping source
interval write

\[
 q_{i+1}=q_i-(2z_i+1),
 \qquad
 y_i=q_i-2z_i=q_{i+1}+1.
\tag{2.1}
\]

The exact terminal bank at phase `i` is

\[
 C_i={q_i-2,q_i-4,\ldots,q_i-2z_i}\subseteq P_i.
\tag{2.2}
\]

For `z_i=0`, this bank is empty.  The one-token update is

\[
 P_{i+1}=P_i-\{y_i\}+\{y_i-1\}.
\tag{2.3}
\]

All modifications before phase `i` occur strictly above `q_i` in the
nonwrapping lift.  Every member of `(2.2)` is at most `q_i-2`.  Therefore

\[
 \boxed{C_i\subseteq P_0.}
\tag{2.4}
\]

Every native hook envelope `P_0` is an independent set in the coordinate
cycle.

### Lemma 2.1 (exact local singleton-parity test)

Consider a native bridge from a run tail `q` to the next active run head
`y=q-2z`, and let `s` be a singleton target strictly between `q` and `y`
which is carried as envelope payload rather than as a mandatory-core root.
Then `s` is compatible with this bridge exactly when

\[
 \boxed{q-s\equiv0\pmod2.}
\tag{2.5}
\]

#### Proof

As payload, `s` is not one of the later roots.  The union identity

\[
 \bigcup_iP_i=P_0\cup\{q_1,\ldots,q_{\ell-1}\}
\]

therefore forces `s in P_0`.

If `q-s` is even, `s` itself is one of the bank coordinates `(2.2)`, so
it imposes no additional local condition.

If `q-s` is odd, `s` is adjacent to the preceding or following coordinate
of the alternating bank `(2.2)`; because `s` is strictly internal, in fact
it is adjacent to both except at a vacuous one-sided endpoint.  Equation
`(2.4)` would then put adjacent coordinates in the independent set `P_0`,
which is impossible.  \(\square\)

Thus the singleton interface is not a capacity question.  A native bridge
has one allowed parity class across its entire skipped gap.

## 3. Exact fixed-route characterization

For a fixed nonwrapping native hook route, let

\[
 M=\bigcup_i\{q_i,y_i\}
\]

be its mandatory-core union and let `I=S\setminus M` be the payload part of
a target `S`.  Put

\[
 R=\{q_0\}\cup I\cup\bigcup_iC_i.
\tag{3.1}
\]

The target is carryable by the strategy "route the cores and keep every
other target coordinate in the initial envelope" if and only if the hook
angle may be chosen with

\[
 \boxed{R\subseteq P_0.}
\tag{3.2}
\]

After translating `q_0` to zero, all hook envelopes are

\[
 P_0=\{0\}\cup J,
 \quad
 J\in\binom{\{3,4,\ldots,n-2\}}b,
 \quad J\text{ nonconsecutive}.
\tag{3.3}
\]

Ignoring for one moment which hook slots were fixed to realize the route,
containment in the ambient family of all hook envelopes has the following
exact static test.  Let

\[
 A=(R-\{0\})\subseteq V:=\{3,\ldots,n-2\}.
\]

It is necessary that `A` be independent, and `A` extends to an ambient
hook envelope precisely when

\[
 |A|+\alpha(V-N[A])\ge b,
\tag{3.4}
\]

where `N[A]` is the closed path-neighbourhood and `alpha` is the sum of
the independence numbers of the remaining path components.  Equivalently,
if those component lengths are `L_1,...,L_t`, then

\[
 \boxed{|A|+\sum_{j=1}^t\left\lceil{L_j\over2}\right\rceil\ge b.}
\tag{3.5}
\]

For a fixed route, `(3.2)` remains the exact criterion, but `P_0` must be
restricted to the weak-composition fibre realizing its prescribed
terminal occupancies.  Thus `(3.5)` is an exact ambient completion test and
a necessary test for the fixed fibre; it is not asserted to override the
slot constraints.  Lemma 2.1 is independent of this final completion issue
and already detects zero-degree targets.

## 4. Singleton cores can occur only at the two path ends

Let `s` be a maximal singleton run of `S`.

### Lemma 4.1 (singleton endpoint lemma)

In any parity-complete source path with interface

\[
 F_i=\{q_i,y_i\},
 \qquad q_{i+1}=y_i-1,
\tag{4.1}
\]

a singleton can occur as a core root only at the initial end, and can
occur as a secondary core only on the final arc.

#### Proof

If `q_i=s` with `i>0`, then `y_{i-1}=s+1`.  The preceding mandatory core
would contain `s+1`, contradicting maximality of the singleton.

If `y_i=s` and `i+1<ell`, then the next mandatory core contains
`q_{i+1}=s-1`, again contradicting maximality.  \(\square\)

Thus choosing the linear cut can absorb singleton cores only in the one
macro-gap containing the two ends of the route.  Singleton defects in two
different gaps cannot both be removed by endpoint choices.

## 5. A rank-eight mixed zero-degree target

For every odd `n>=19`, take

\[
 \boxed{
 S=\{0,-1,-4,-7,-8,-11,-14,-15\}\subseteq\mathbb Z_n.}
\tag{5.1}
\]

Its nontrivial runs are the three maximal dimers

\[
 \{0,-1\},
 \qquad
 \{-7,-8\},
 \qquad
 \{-14,-15\},
\tag{5.2}
\]

and its singleton runs are `{-4}` and `{-11}`.

The first two inter-dimer bridges have even span six:

\[
 -1\longrightarrow-7,
 \qquad
 -8\longrightarrow-14.
\tag{5.3}
\]

Their forced terminal banks are respectively

\[
 \{-3,-5,-7\},
 \qquad
 \{-10,-12,-14\}.
\tag{5.4}
\]

The singleton `-4` has the wrong parity in the first gap and is adjacent
to `-3,-5`.  The singleton `-11` has the wrong parity in the second gap
and is adjacent to `-10,-12`.

Every maximal dimer forces its own entry slide, so a nonwrapping source
path which carries all three dimers must encounter them in their displayed
cyclic order.  It has only one linear cut.  If the first gap is cut, the
second bad singleton remains inside a native bridge.  If the second is
cut, the first remains.  If the third gap is cut, both remain.  By Lemma
4.1, using a bad singleton as a source endpoint merely chooses its own
macro-gap as the cut and cannot eliminate the other bad gap.

Lemma 2.1 therefore gives:

### Theorem 5.1 (mixed singleton two-gap obstruction)

For every eventual parameter with `d>=8`, the target `(5.1)` has no
single-hook source ticket obtained by:

1. traversing all nontrivial runs with native cores, allowing any abstract
   odd-bridge packet where an odd span occurs; and
2. carrying all remaining singleton runs in the native initial envelope.

The obstruction appears before the mass budget and before component Hall.
In `(5.1)` the two decisive bridges are even, so adding the abstract odd
generator `(OB)` does not affect the contradiction.

## 6. Consequence for the low-payload programme

Two proposed shortcuts are now excluded.

1. A terminal two-soliton on an untouched near-hook component cannot be
   the physical odd bridge; native PBBS root steps have invariant odd
   parity.
2. Even a separately supplied odd bridge does not make the strategy
   "nontrivial cores plus singleton payload in `P_0`" universal.  The
   target `(5.1)` has incompatible singleton payload in two different even
   bridge gaps.

The next positive packet must therefore do more than change bridge parity.
It must also have at least one of the following literal features:

* a rethreaded bridge with a selectable support parity or movable parity
  switch inside the skipped gap;
* a singleton-bypass rail which transports wrong-parity singleton payload
  outside the native independent envelope; or
* more than one independently resettable envelope segment, with a global
  packing theorem.

The all-low gate is consequently a combined **parity-and-singleton bypass**
packet, not the native near-hook formula proposed previously.
