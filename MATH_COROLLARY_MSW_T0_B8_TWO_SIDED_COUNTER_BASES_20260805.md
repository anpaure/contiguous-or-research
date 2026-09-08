# The `T0` and `B8` relays are the two minimal raw-disjoint chamber states

**Date:** 2026-08-05  
**Method:** direct chamber-interval calculation; no computation or search  
**Status:** unconditional identification of the two frozen relay targets in
the MSW one-counter grammar.  It closes the finite **orientation** state of
the raw-disjoint chamber problem.  It does not prove the physical renewal
carry, handle the two endpoint-flaw decorations, or show that arbitrary
renewal contexts can be planted simultaneously.

## 1. The two frozen targets

The two exact closed relays currently available are

```text
T0 = 110011001111,
B8 = 11101101.
```

The first is repaired by the frozen two-hex relay, and the second by the
frozen four-hex relay.  Both relays preserve every previously represented
upper-`q2` target and tensor over arbitrary Dyck suffixes.

For a productive chamber `C`, use the notation of the chamber theorem:

\[
 I_C=[A_C,A_C+a_C],
 \qquad
 J_C=[B_C,B_C+b_C].                                \tag{1.1}
\]

A raw-disjoint chamber is **under** when `max I_C < min J_C` and **over**
when `max J_C < min I_C`.

## 2. Exact chamber of `T0`

Reading `T0` from height zero, its barriers are the two down-steps
`D_2` in positions three and seven.  The only productive chamber is the
terminal chamber after the second barrier.  It contains

```text
D1 U0 U1 U2 U3.
```

There are two `U0` steps before this chamber, one `U0` step inside it, no
`U3` step after it, and one `U3` step inside it.  Hence

\[
 A=2,\quad a=1,\quad B=0,\quad b=1,                \tag{2.1}
\]

and therefore

\[
             I=[2,3],\qquad J=[0,1].               \tag{2.2}
\]

Thus `T0` is the minimal frozen **over** relay state, with signed chamber
offset

\[
                         A-B=2.                     \tag{2.3}
\]

## 3. Exact chamber of `B8`

For `B8`, the unique barrier is the `D_3` in position four.  The initial
chamber contains

```text
U0 U1 U2
```

and is the only productive chamber.  It has one `U0` internally, no `U0`
before it, two `U3` steps after it, and no `U3` internally.  Consequently

\[
 A=0,\quad a=1,\quad B=2,\quad b=0,                \tag{3.1}
\]

so

\[
             I=[0,1],\qquad J=[2,2].               \tag{3.2}
\]

Thus `B8` is the minimal frozen **under** relay state, with

\[
                         A-B=-2.                    \tag{3.3}
\]

## 4. Two-sided base corollary

### Corollary 4.1

The exact relay library contains one closed, topology-improving base packet
on each side of the one-counter cut:

\[
 \boxed{
   \text{over base }(+2):T0,
   \qquad
   \text{under base }(-2):B8.}                     \tag{4.1}
\]

Their lifted topology effects are respectively

\[
       5\text{ cycles}\longrightarrow1,
       \qquad
       6\text{ cycles}\longrightarrow1.           \tag{4.2}
\]

Hence a recursive chamber repair no longer needs a new terminal packet for
the two possible raw-disjoint orientations.  It needs a two-sided renewal
transport theorem carrying these packets through the low and high renewal
blocks while preserving literal phase, old-target multiplicity and socket
compatibility.

#### Proof

Equations (2.2) and (3.2) put the targets on opposite sides of the unique
cut in the chamber theorem.  The two cited relay theorems give exact closure
and (4.2).  The chamber grammar has only the under and over orientations
once the intervals are disjoint, so no third raw-disjoint orientation
exists.  \(\square\)

### Corollary 4.2 (no component-count congruence obstruction)

At the scalar component level, the two relay types have decrements four
and five.  Since

\[
                         \gcd(4,5)=1,                \tag{4.3}
\]

every integer at least twelve is a nonnegative combination of these two
decrements.  Consequently every initial component count `C>=13` admits the
formal arithmetic

\[
                         C-1=4u+5v                  \tag{4.4}
\]

for some `u,v>=0`.  Thus the combined two-sided MSW relay library has no
fixed-arity residue obstruction to a one-component carrier.

This is only component arithmetic.  Equation (4.4) does not choose
`u+v` physically compatible relay occurrences or prove that their component
hyperedges form a merge forest.

#### Proof

The Frobenius number of `4,5` is `4*5-4-5=11`; hence every integer at least
twelve has the form `4u+5v`.  Apply this to `C-1`.  \(\square\)

## 5. Exact remaining finite control state

The raw interval test is not the whole canonical inverse test.  A target
can also be missing when every interval intersection consists only of the
at most two endpoint exceptions:

* one possible flaw-zero, type-`(1,3)` label;
* one possible flaw-terminal, type-`(0,2)` label.

Therefore the relay control state after (4.1) is finite but not yet fully
closed.  The raw-disjoint states are `under` and `over`.  At the unique cut
there can additionally be a touching state whose surviving labels are
drawn from

\[
  \{(1,3),(0,2)\},                                   \tag{5.1}
\]

with at most one label of each type.  This is a finite decoration of the
counter, but it is not asserted to be a Cartesian product: some formal
flag combinations may be unrealizable.

The two raw-disjoint states now have explicit base relays.  The touching
endpoint states still require either:

1. a proof that the same two relays transport through the endpoint flags;
   or
2. at most two additional decorated base relays and a flag-preserving
   renewal carry.

This is the precise finite part left after the unbounded integer counter is
separated from its decorations.

## 6. Scope

This note does not infer a physical carry merely from the incidence-cycle
transport identity.  The latter still needs a compatible factor phase (or
another literal realization), and packets for different nonsuffix contexts
need a simultaneous support theorem.  No statement about PBBS component
necklaces, higher upper widths, residence, or the common cap is made.

## 7. Dependencies

1. `MATH_THEOREM_CANONICAL_MSW_Q2_CHAMBER_LANGUAGE_AND_RENEWAL_GRAMMAR_20260805.md`;
2. `MATH_THEOREM_MSW_TWO_HEX_T0V_HOLE_RELAY_AND_DYCK_TENSOR_20260805.md`;
3. `MATH_THEOREM_MSW_FOUR_HEX_B8V_CLOSED_RELAY_TOPOLOGY_AND_SOCKET_20260805.md`;
4. `MATH_THEOREM_INCIDENCE_CIRCULATION_CONTEXT_TRANSPORT_AND_MSW_1100_CARRY_GATE_20260805.md`.
