# Adjacent necklaces: the concentrated radial socket is one allocation cycle

**Date:** 2026-08-05  
**Method:** an explicit one-dimensional chip-transfer orbit; no computation  
**Status:** unconditional.  It resolves the complete local matching state
of the `CD` radial socket: after the two radial endpoints are consumed, the
canonical allocation spine contributes either zero monomers or exactly one
named monomer according to the inner shell mass parity.

## 1. The allocation cycle

Fix `q>=3` and an inner boundary-shell mass `t>=2`.  Put

\[
 C=[0^{q-1},t]                                      \tag{1.1}
\]

and, for `1<=a<t`, put

\[
 V_a=[0^{q-2},a,t-a].                               \tag{1.2}
\]

### Theorem 1.1

The displayed necklace classes are pairwise distinct and the adjacent-chip
graph contains the simple cycle

\[
              C-V_1-V_2-\cdots-V_{t-1}-C.           \tag{1.3}
\]

#### Proof

For `1<=a<t-1`, moving one unit from the last positive coordinate to the
preceding one gives

\[
                         V_a\longrightarrow V_{a+1}.
\]

Moving one unit from the final coordinate of `C` into the preceding zero
gives `V_1`.  At the other end, moving the final singleton of `V_(t-1)`
into its predecessor gives `[0^(q-2),t,0]`, a rotation of `C`.

The class `C` has one positive coordinate.  Every `V_a` has exactly two
adjacent positive coordinates.  Rooting a `V_a` at the unique zero run of
length `q-2` recovers the ordered pair `(a,t-a)`; a rotation cannot exchange
the pair while retaining that root.  Hence the displayed classes are
distinct, and (1.3) is simple.  \(\square\)

For the universal radial square between outer mass `s` and inner mass
`t=s-q`, its two inner endpoints are exactly

\[
                         C,qquad D=V_1.              \tag{1.4}
\]

The opposite endpoint of the allocation spine is

\[
                         E=V_{t-1}.                  \tag{1.5}
\]

## 2. Exact post-splice matching state

### Theorem 2.1 (sharp `CD` socket parity)

After the radial cross edges consume `C` and `D=V_1`, the remaining spine

\[
                         V_2-V_3-\cdots-V_{t-1}      \tag{2.1}
\]

has:

* a perfect matching when `t` is even;
* a matching leaving exactly `E=V_(t-1)` unmatched when `t` is odd.

The matching is the alternating edge set starting with `V_2V_3`.

#### Proof

The path (2.1) has `t-2` vertices.  If `t` is even this number is even and

\[
 V_2V_3,\ V_4V_5,\ldots,\ V_{t-2}V_{t-1}
\]

is perfect.  If `t` is odd, the same pattern ends at `V_(t-2)` and leaves
only `V_(t-1)=E`.  \(\square\)

### Corollary 2.2

The universal radial square does not create an uncontrolled phase-fibre
defect.  Its `AB` edge is protected inside the outer unique-zero phase
fibre by the Clifford-active edge theorem, while its `CD` side has the
deterministic state

\[
 \boxed{
 0\text{ exported monomers if }t\text{ is even};\qquad
 E\text{ if }t\text{ is odd}.}                      \tag{2.2}
\]

Thus the only remaining shell interaction is transport of the explicitly
named parity monomer `E` through the rest of the zero-core matching.  (For
odd `t`, `E` is generally an active rather than an all-quiet allocation.)
No arbitrary mate of `D` has to be carried.

## 3. Scope

Proved:

1. the exact allocation cycle containing both orientations of the
   concentrated radial socket;
2. its post-splice perfect/one-monomer matching; and
3. an explicit identity for the sole possible exported monomer.

Not proved:

1. that the remaining shell core can always absorb or transport `E`;
2. the full radial-flexibility theorem;
3. PBBS physical halo compatibility; or
4. any universal-word upper bound.
