# Corrected coherent-birail implication: the invariant is terminal `chi+lambda`, not the token matrix

Date: 2026-08-01  
Status: exact conditional implication and scope audit.  No unconditional
`B(k)+O(1)` theorem is claimed.

## 0. Short verdict

The coherent-birail `C4/C6` calculation proves an abstract Markov-basis
statement.  It does not by itself prove a physical orbit, a bounded compiler
defect, or a bounded additive length.

The shortest correct implication is

\[
 \boxed{
 \nu(k)\le B(k)+u(T_0)+
   \min_{T\in\operatorname{Comp}_\Gamma(T_0)}
       \bigl(\chi(T)+\lambda_d(T)\bigr).}             \tag{0.1}
\]

Here `Gamma` is a genuinely closed graph of physically safe serial moves,
`u` is the upper-target defect (constant on `Gamma`), `chi` is the number of
uncontracted extra source positions/essential split boundaries, and
`lambda_d` is the exact terminal lower-compiler deletion number.

Thus a closed component containing a state with

\[
                         \chi(T)+\lambda_d(T)\le C     \tag{0.2}
\]

gives `nu(k)<=B(k)+C` when the starting carrier is upper-complete.  Neither
the abstract matrix theorem nor scalar slack proves (0.2).

## 1. Exact theorem

Fix `k,d` and let `C` be a class of physical chronologies.  Each `T in C`
has:

* a base carrier of length `B(k)`;
* `chi(T)>=0` uncontracted added source positions;
* a complete literal upper-coverage defect `u(T)`;
* an occurrence-labelled coherent-birail state `phi(T)`; and
* an exact terminal deletion number `lambda_d(T)`.

Let `Gamma` join `T` to `T'` only when the displayed physical replacement
has been checked in the **current** chronology and satisfies all of the
following.

1. It preserves the middle-owner permutation and simple physical topology.
2. It preserves depth-`d` residence and the complete required boundary
   envelope state.
3. It preserves the complete interval-union language, including exterior
   crossing witnesses, not merely the local internal deck or q1 palettes.
4. Its result remains in `C` and its uncontracted length charge is exactly
   recorded by `chi(T')`.
5. It implements the claimed occurrence-labelled `C4` or `C6` circuit on
   `phi`.

### Theorem 1.1 (corrected serial CBC bound)

Under these definitions, (0.1) holds.

#### Proof

Along a walk in `Gamma`, conditions 1--3 preserve physical carrier legality
and the full upper coverage set, so `u(T)=u(T_0)`.  Condition 4 makes the
terminal physical length exactly `B(k)+chi(T)`.  Solve the lower compiler
only once, at the terminal state.  By definition, deleting and appending
`lambda_d(T)` lower targets suffices.  Hence

\[
             \nu(k)\le B(k)+\chi(T)+u(T_0)+\lambda_d(T).
\]

Minimize over the reachable component.  \(\square\)

For the equal-length mixed-coatom replacements, `chi` stays zero.  For
split-letter lifts, a constant cost **per step** is not enough: unless old
splits contract or recycle, `chi` may grow with the number of dimensions or
serial moves.  This is the exact hidden reset assumption in an unqualified
serial-safe claim.

## 2. What the abstract `C4/C6` theorem really supplies

On the authenticated three-label whole-chain support, supported quadrics and
cubics connect every fixed-margin fibre.  In the smallest face the support
is `C6`, there are two states, no square exists, and the indispensable move
is cubic.  Therefore, if every applicable supported circuit has a physical
lift from every chronology over its source state, and every lift remains in
`C`, then the projection of a physical component contains the entire
abstract fibre.

The two italicized universal quantifiers are the closed-atlas hypothesis.
A prospective menu, or a packet legal in only the initial chronology, does
not establish them.  Nor does a depthwise Markov basis establish diagonal
all-depth closure: one literal packet acts at every depth simultaneously.

Hamilton-connectedness of a full interchange graph is not needed for
(0.1).  Ordinary connectivity of the authenticated `C4/C6` fibre suffices.

## 3. `lambda_d` is not a known token-state invariant

The compiler graph depends on physical cell addresses, exterior unions,
erosion envelopes, the common cap, and competition between target
occurrences.  The coherent-birail matrix records none of these completely.
Consequently

\[
                        \lambda_d(T)=\lambda(\phi(T))           \tag{3.1}
\]

is an additional quotient theorem, not a consequence of the Markov basis.
Indeed the same local provider switch can increase, preserve or decrease
maximum matching rank depending on unchanged exterior incidence edges.

There are only two honest ways to use the abstract fibre in (0.1).

* Prove (3.1), then minimize `lambda` on the finite abstract fibre.
* Avoid (3.1) by producing one **literal terminal certificate**: an actual
  source/cap and a full target-to-cell matching at one reachable chronology.

The second route is weaker and is the correct interpretation of the
split-letter terminal theorem.  The serial moves are allowed to change
`lambda`; only its terminal value matters.

## 4. Why `B+1` scalar slack is not the missing proof

At length `B+1`, the scalar short-window count gains `W+d+1` cells, much
more than the `O(d^2)` footprint of a bounded packet.  This rules out a
scalar-capacity obstruction.  It does not imply Hall feasibility, common-cap
compatibility, exterior witness preservation, or a legal pivot host.

In the notation of (0.1), `B+1` merely permits `chi=1`.  Exact completion
still requires `lambda_d=0` (or a literal split-terminal matching that proves
the same fact).  Positive scalar slack can coexist with zero-candidate lower
targets and arbitrary Hall deficiency.  Thus `B+1` is a plausible sharpened
target, not an implication of CBC.

## 5. One concrete next lemma

The quaternary-octagon source audit now gives exact native endpoint-ray
partitions of sizes eight and nine for the two phase-exclusive source decks.
This suggests the following sharply testable replacement for a vague
"closed atlas" assumption.

### Nine-ray regenerative exterior-ear lemma

For every sufficiently large `k`, construct a class `C` and a phase-common
bank of at most nine actual source anchors such that:

1. every authenticated coherent-birail `C4/C6` circuit has a physical lift
   using those anchors, from every state where the circuit is applicable;
2. after each lift, old anchor splits contract and the same bank is
   regenerated, so `chi<=9` throughout rather than increasing per move;
3. the lift preserves the full exterior interval language, residence,
   owners, topology and one legal common cap; and
4. if `U` is the terminal compiler-source set and `M_T` is the strict
   gammoid of certified open ears from its ray entrances to unused physical
   cells, then for one reachable terminal state

   \[
       r_{M_T}(P_X)\ge |X|-C_0\qquad\text{for every }X\subseteq U, \tag{5.1}
   \]

   for an absolute constant `C_0`.

Rado's theorem turns (5.1) into `lambda_d(T)<=C_0`.  Equations (0.1) and
`chi<=9` then give

\[
                         \nu(k)\le B(k)+C_0+9.          \tag{5.2}
\]

This lemma states exactly the two presently separate obligations: closed
serial host regeneration and integral terminal augmentation.  The new
`8/9` ray theorem supplies the constant-size source geometry, but not the
ambient legality or all-cut gammoid rank (5.1).

## 6. Scope

Proved here: the implication (0.1), the exact role of `chi`, and the logical
alternatives for handling `lambda_d`.

Not proved here: a closed physical circuit atlas, a bounded reset bank, the
quotient identity (3.1), the all-cut rank bound (5.1), or `B(k)+O(1)`.

