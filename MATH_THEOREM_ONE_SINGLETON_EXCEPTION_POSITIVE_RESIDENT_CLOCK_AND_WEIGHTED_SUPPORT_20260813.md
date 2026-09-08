# One singleton exception closes a joint clock rethread with positive residence

**Date:** 2026-08-13  
**Status:** unconditional abstract block theorem and exact finite support
reduction.  The `T_2` neighbour test is unconditional.  The finite weighted
support inclusion for that actuator is a separate calculation and is not
asserted here.

## 1. Joint endpoint blocks

Let `F^-` and `F^+` be oriented simple Johnson two-factors on the same
occurrence bank `V`, with rank-`rho` base owner `V_v` at occurrence `v`.
Write `s^-(v),s^+(v)` for the two successors.  Fix one exceptional
occurrence `a`.

Assume a disjoint ground decomposition

\[
                         X\mathbin{\dot\cup}Y\mathbin{\dot\cup}C,
                                                               \tag{1.0}
\]

with every base owner `V_v subseteq X` and every auxiliary payload below
contained in `Y`.  All auxiliary payloads have one common rank.  Thus
adjoining the fixed core and an auxiliary payload cannot mask a coordinate
exchanged by a base Johnson edge, and every displayed owner has one common
rank.

For every normal occurrence `v!=a`, let

\[
 \Gamma_h(v)=(C+V_v+Q_{v,0}(h),\ldots,
               C+V_v+Q_{v,L-1}(h)),\qquad L=2h+2,       \tag{1.1}
\]

where all `Q_(v,j)(h)` have the same rank and consecutive displayed owners
are Johnson adjacent.  Put

\[
                  L_v=Q_{v,0}(h),\qquad R_v=Q_{v,L-1}(h). \tag{1.2}
\]

Replace `a` by the singleton

\[
                         \Gamma_h(a)=(C+V_a+S),             \tag{1.3}
\]

and set `L_a=R_a=S`.  Assume the endpoint equations

\[
                         \boxed{R_v=L_{s^-(v)}=L_{s^+(v)}}  \tag{1.4}
\]

hold for every `v`.  Thus every old and new block join uses the same
auxiliary payload, and the only change at a join is the base Johnson
exchange.

Assume also the following literal separation conditions.

1. All displayed owners are distinct in each state.
2. All internal and joining lower/upper tickets are distinct in each state,
   except for repetitions explicitly allowed by the intended palette
   ledger.
3. Inside a normal block every positive run of an auxiliary coordinate is
   either of length at least `h`, or meets an endpoint.  If it meets the
   initial endpoint its initial run has length at least `h`; if it meets the
   terminal endpoint its terminal run has length at least `h`.

Condition 2 may be replaced by a direct exact ticket ledger.  It is stated
as simplicity only to separate the residence argument from a particular
palette completion.

## 2. The singleton residence condition

For a state `epsilon in {-,+}`, let

\[
 p^\epsilon(a)=(s^\epsilon)^{-1}(a),\qquad
 q^\epsilon(a)=s^\epsilon(a).                         \tag{2.1}
\]

Require

\[
 \boxed{
 x\in V_a\Longrightarrow
 x\in V_{p^\epsilon(a)}\cup V_{q^\epsilon(a)}
 \quad(\epsilon=-,+).}                               \tag{2.2}
\]

Thus no base coordinate present at the singleton is absent from both
adjacent normal blocks in either state.

### Theorem 2.1 (one-singleton positive-resident clock)

Under `(1.1)--(2.2)`, block substitution gives two simple Johnson
two-factors with the same base successor actions.  Every nonconstant
coordinate has every positive run of length at least `h`.  The exceptional
block costs one owner while every normal block costs `2h+2` owners.

#### Proof

Internal legality is assumed in (1.1).  At a join `v->w`, equation (1.4)
makes the auxiliary payload identical, so the join is exactly the base
Johnson exchange `V_v->V_w`.  Distinctness and the palette assertion are
the stated separation hypotheses.

A base coordinate is constant through every normal block.  Any positive
run avoiding `a` therefore contains a whole normal block and has length at
least `L`.  If a positive run contains the singleton `a`, condition (2.2)
says that it continues into at least one adjacent normal block.  It again
has length at least `L+1`.

Consider an auxiliary coordinate.  A run internal to a normal block has
length at least `h` by condition 3.  A run crossing an ordinary join is
the union of a terminal and an initial endpoint run and cannot shorten.
If it crosses the singleton, its coordinate lies in `S=R_p=L_a=R_a=L_q`.
It therefore contains the terminal run of the predecessor, the singleton,
and the initial run of the successor, of total length at least `2h+1`.
Core coordinates are constant.  This proves positive `h`-residence.
\(\square\)

No zero-gap assertion is made.  This is intentional: the flat maximal
antecedent needs positive residence only.

## 3. An `h`-independent weighted support signature

The unequal block lengths require a weighted rather than ordinary base-arc
signature.  Give the singleton type weight `1` and every normal block type
weight `L=2h+2`.

Assume the normal auxiliary words are obtained from finitely many symbolic
templates.  A template records enough data that two blocks of the same type
have, for every `h`, identical auxiliary union on every interval with the
same numerical endpoint offsets.  The variable-tag clock, for example,
may use the ordered input/output tag pair as its normal type.  Give `a` the
distinguished type `star`.

For a based cyclic base arc

\[
                         I=(v_1,\ldots,v_s),                    \tag{3.1}
\]

put

\[
 \Theta(I)=\left(
   \bigcup_{j=1}^sV_{v_j},
   n(I),
   (\kappa(v_1),\ldots,\kappa(v_s))
 \right),                                                   \tag{3.2}
\]

where `n(I)` is the number of normal occurrences and the type word retains
the exact position of `star` when `a` occurs.  Equivalently, (3.2) records
the base value, the number of length-`L` blocks, the ordered auxiliary type
word, and whether the singleton is absent, initial, terminal, or internal.
Retaining the full type word is the fail-closed convention.

Let `Omega^-` and `Omega^+` be the supports of (3.2) over all standard
based cyclic arcs that can be projections of the lifted intervals under
consideration.

### Theorem 3.1 (weighted symbolic support transfer)

If

\[
                         \boxed{\Omega^-\subseteq\Omega^+,}    \tag{3.3}
\]

then, for every `h>=2` and every physical lifted width `w`, every old
interval value of width `w` has a new interval of the same width and value.

#### Proof

Project an old lifted interval to its base arc `I` and retain its numerical
offsets in the first and last blocks.  Condition (3.3) supplies a new arc
`I'` with the same base union and identical ordered type word.  Use the same
endpoint offsets.

The full internal-block contribution to physical width is `nL` plus the
same singleton contribution, while the two clipped endpoint contributions
are identical because the endpoint block types and offsets agree.  Hence
the physical widths coincide for every `h`.  Template equality gives the
same literal auxiliary union, and the first coordinate of (3.2) gives the
same base union.  Adjoining the common core proves equality of the lifted
values.  \(\square\)

The theorem is deliberately conservative.  A complete internal normal
block may make the clock union full and permit a coarser signature, but no
such shielding is needed for (3.3).

## 4. Exact `T_2` residence specialization

In the complete `ML(13)` upper-owner chronology of the frozen two-hex
relay, take

\[
                         a=1010110011010.                      \tag{4.1}
\]

Its old and new neighbours are

\[
\begin{array}{c|cc}
 &p(a)&q(a)\\ \hline
-&d=1010011011010&b=1011100011010\\
+&c=1011110001010&e=1000111011010.
\end{array}                                                  \tag{4.2}
\]

The one-set of `a` is

\[
                         V_a=\{0,2,4,5,8,9,11\}.              \tag{4.3}
\]

Relative to `a`, the four neighbours delete respectively

\[
                         4,\quad5,\quad8,\quad2,               \tag{4.4}
\]

and insert `6,3,3,6`.  Hence each coordinate of `V_a` occurs in at least
one adjacent normal block in each of the old and new states.  Condition
(2.2) holds literally.

### Corollary 4.1

Any endpoint-payload realization of `(1.1)--(1.4)` for this relay which
satisfies the local palette and auxiliary boundary-run hypotheses is
positive `h`-resident after replacing `a` by a singleton.  Its complete
all-width question is exactly the finite weighted inclusion `(3.3)`.

The finite `T_2` census currently finds support casualties for the first
natural singleton clock; therefore this corollary does not claim (3.3).
It isolates the support/backup row from residence, graph legality, and the
two exceptional literal q2 fibres.

## 5. Scope

Proved here:

* graph legality under the joint endpoint equations;
* a sharp local condition eliminating the only singleton positive-run
  defect;
* positive residence of every base, auxiliary, and core coordinate;
* an exact `h`-independent weighted support criterion; and
* the literal `T_2` neighbour verification.

Not proved here:

* weighted support inclusion for the frozen `T_2` packet;
* exact global owner/lower-palette extension of a selected block bank;
* tensorized collision-free planting over every suffix `V`; or
* the final exterior source and typed-cap interfaces.
