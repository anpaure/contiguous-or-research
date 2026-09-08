# Zero holonomy is not topology: signed-fragment and split counterexamples

**Date:** 2026-08-02  
**Lane:** A, obstruction audit  
**Audited file:**
`MATH_THEOREM_COPRIME_VOLTAGE_LOCALIZATION_AND_ZERO_HOLONOMY_REPAIR_20260802.md`  
**Verdict:** Theorem 1 and its fixed-`z` seam-displacement calculation are
correct under their explicit hypotheses.  Those hypotheses are essential.
Local packet holonomy zero alone neither preserves voltage nor prevents a
topology split.

## 1. The signed fragment ledger

Let a directed quotient cycle `F` over `Z_n` be cut into retained fragments
`P_1,...,P_t`.  Orient every `P_j` as it appears in `F`, and write

\[
                           p_j=\delta(P_j).              \tag{1.1}
\]

Let `E` be the directed old seam multiset.  Suppose a rethread uses directed
new seams `N` and produces one quotient cycle `F'`.  Let
`epsilon_j in {+1,-1}` record whether `F'` traverses `P_j` in its old or
reverse orientation.  Then the exact identity is

\[
 V(F')-V(F)=
   \sum_{j=1}^t(\epsilon_j-1)p_j
   +\sum_{f\in N}\delta(f)-\sum_{e\in E}\delta(e)
       \pmod n.                                        \tag{1.2}
\]

### Proposition 1.1 (correct zero-displacement criterion)

One-cycle voltage is preserved if all retained fragments are co-oriented,
`epsilon_j=+1`, and the exact directed seam displacement is zero.  If a set
`R` of fragments is reversed, zero seam displacement instead gives

\[
                         V(F')-V(F)
                       =-2\sum_{j\in R}p_j\pmod n.       \tag{1.3}
\]

#### Proof

The input and output ledgers are

\[
 V(F)=\sum_jp_j+\sum_{e\in E}\delta(e),\qquad
 V(F')=\sum_j\epsilon_jp_j+\sum_{f\in N}\delta(f).
\]

Subtract them. \(\square\)

Thus the source theorem is exactly the `epsilon_j=+1` specialization.  Its
phrase “the same oriented fragments” is load-bearing, not cosmetic.

## 2. Minimal voltage counterexample

Take `n=5` and two retained fragments

\[
 P:A\longrightarrow B,\quad \delta(P)=1,
 \qquad
 Q:C\longrightarrow D,\quad \delta(Q)=1.               \tag{2.1}
\]

Let the old seams be

\[
                         B\longrightarrow C,qquad
                         D\longrightarrow A             \tag{2.2}
\]

with voltage zero.  The old quotient cycle is

\[
                     A\,P\,B-C\,Q\,D-A                 \tag{2.3}
\]

and has voltage `2 mod 5`, hence its development is one physical cycle.

Now use zero-voltage seams

\[
                         B\longrightarrow D,qquad
                         C\longrightarrow A.            \tag{2.4}
\]

The output is still one quotient cycle, but it traverses `Q` backwards:

\[
                     A\,P\,B-D\,Q^\dagger\,C-A.         \tag{2.5}
\]

Both old and new seam sums are zero, while

\[
                         V(F')=1-1=0\pmod5.              \tag{2.6}
\]

The physical lift now has `gcd(5,0)=5` components.  This is a two-fragment
counterexample to the weakened assertion

> zero local seam displacement preserves voltage even when retained
> fragment orientations may change.

It does not contradict the source Theorem 1, because that theorem forbids
the reversal in (2.5).

## 3. Minimal topology-split counterexample

Use the same two voltage-one fragments and old cycle (2.3).  Replace the old
seams by two zero-voltage closing seams

\[
                         B\longrightarrow A,qquad
                         D\longrightarrow C.            \tag{3.1}
\]

The fragments keep their orientations, and the total new-minus-old seam
voltage is zero.  Nevertheless the output has two quotient cycles,

\[
                         A\,P\,B-A,qquad
                         C\,Q\,D-C,                     \tag{3.2}
\]

each of voltage one.  Their physical developments are two components.  The
old factor had one physical component.

For a general multi-cycle output `K`, the authoritative ledger is

\[
 V(K)=\sum_{P_j\subset K}\epsilon_{K,j}p_j
       +\sum_{f\in N\cap K}\delta(f),                  \tag{3.3}
\]

and the physical component count is

\[
                           \sum_K\gcd(n,V(K)).           \tag{3.4}
\]

There is no scalar “total factor voltage” which replaces the list in
(3.3).  This is why the one-output-cycle hypothesis in the source theorem
is also load-bearing.

## 4. Audit of the fixed-`z` seam displacement

The fixed-`z` heptagon has old and new projected seams

\[
 e_i=\{x_i,y_i\},\qquad e_i'=\{x_{i+1},y_i\}.           \tag{4.1}
\]

In the step-two retained-path orientation they are traversed as

\[
                   y_i\longrightarrow x_i,qquad
                   y_i\longrightarrow x_{i+1}.         \tag{4.2}
\]

The source note assumes the literal phasewise packet.  In its natural
representatives both types of seams have voltage zero.  More generally,
after arbitrary consistent vertex-gauge changes with endpoint potentials
`g(w)`, their voltage sums are

\[
 \sum_i\bigl(g(x_i)-g(y_i)\bigr),qquad
 \sum_i\bigl(g(x_{i+1})-g(y_i)\bigr).                  \tag{4.3}
\]

They are equal because `i mapsto i+1` permutes the moving endpoints.  Hence

\[
                       \sigma_{\rm seam}=0              \tag{4.4}
\]

is exact and gauge-independent.  Endpoint phase differences alone do not
produce a counterexample.

The common extension label `z` is essential for the cap-multiset identity
and for separating moving from retained owners.  It is not what proves
(4.4); the latter follows from the cyclic endpoint permutation.  Therefore
one should distinguish:

1. **cap holonomy**, closed by the fixed-`z` cap rotor in the phasewise
   packet;
2. **seam displacement**, zero by (4.3); and
3. **factor topology/orientation**, which still requires the step-two
   retained-path predicate.

## 5. Proof-safe correction to the localization statement

Call a local packet a **qualified zero-displacement rethread** in the current
factor if all three conditions hold.

1. Every retained fragment is used with its old orientation, or its signed
   voltage correction is included explicitly in (1.2).
2. The new port matching forms one directed quotient cycle.
3. The exact directed seam displacement in the current endpoint gauge is
   zero.

### Theorem 5.1 (serial localization, corrected scope)

Starting from a one-cycle quotient factor of voltage `v`, any serial sequence
whose every prefix applies a qualified zero-displacement rethread remains one
quotient cycle of voltage `v`.  If `gcd(n,v)=1`, every prefix develops to one
physical cycle.

#### Proof

Apply Proposition 1.1 at each prefix; condition 2 permits the scalar voltage
to be iterated. \(\square\)

This is already the mathematical content of Theorem 1 and Corollary 1.1 in
the audited source.  The needed correction is terminological and downstream:

* “zero-holonomy family” must mean the qualified, current-factor predicate
  above, not merely an abstract phasewise `h=0` packet catalogue;
* after an earlier repair changes the port pairing, the step-two order and
  fragment orientations must be checked again;
* a local fixed-`z` circuit with zero seam displacement is not automatically
  topology-safe on every exposed seven-edge support.

Under this interpretation, the source Theorem 2 is valid.  Its consequence
for abundance remains conditional on proving positive supply of complete
fixed-`z` tickets which satisfy the one-cycle/co-orientation predicate at
every serial prefix.  It does not follow from the raw `Theta(k^7)` central
atlas alone.

## 6. Scope

The counterexamples are abstract exact fragment ledgers; no finite search is
used.  They show the smallest information omitted by an unqualified local
`h=0` label.  They do not refute the literal fixed-`z` step-two construction
when its retained paths are indeed co-oriented and form one output quotient
cycle.

## 7. Provenance

The audited source at the time of this note has SHA-256

```text
d17cb7517fa9a0566e4068aef714811865bf76c2248ae58a83437fbf389bf951
  MATH_THEOREM_COPRIME_VOLTAGE_LOCALIZATION_AND_ZERO_HOLONOMY_REPAIR_20260802.md
```

The signed multi-fragment convention agrees with the exact fragment-voltage
ledger in
`MATH_THEOREM_A_K17_PROTECTED_TWO_C6_FUSION_VOLTAGE_RESIDENCE_AND_DEEP_GATE_20260802.md`.
