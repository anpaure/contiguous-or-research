# The unfinished odd packet is its own exact midpoint reservoir

**Date:** 2026-08-06  
**Method:** signed connector charge, opposite-pair cancellation, and literal
four-coordinate paths  
**Status:** unconditional algebraic and local-path theorem.  The remaining
gap is occurrence-labelled shuttling of the bounded remote packet to the
fixed collar before the double head is installed.

## 1. Connector charge

Use

\[
 A=00,\qquad B=20,\qquad C=22,\qquad
 M=11,\qquad H=02,
\tag{1.1}
\]

and write `C(a)` for `A,B,C` when `a=0,1,2`.  Put

\[
                         \epsilon(a)=a-1.
\tag{1.2}
\]

Thus `A,B,C` have masses `2+2epsilon(a)`, while `M,H` both have mass two.

Let the first connector be `C(a_1)`, and let the fixed two-block collar be

\[
                         C(a)\mid C(b).
\tag{1.3}
\]

After removing these three connectors, noncrossing cancellation of the work
tape leaves a residual extreme bank whose signed charge is

\[
             -q,\qquad
             q=\epsilon(a_1)+\epsilon(a)+\epsilon(b).
\tag{1.4}
\]

The bank has `|q| in {0,1,2,3}` blocks, all of the sign `-sign(q)`.

Define the **unfinished packet** `P` to consist of the first connector and
this residual bank, omitting a neutral first connector `B` from its extreme
subbank.

### Lemma 1.1 (exact packet--collar balance)

The signed extreme charge of `P` is

\[
 \boxed{
        \sum_{X\in P}\epsilon(X)
             =-\epsilon(a)-\epsilon(b).
 }
\tag{1.5}
\]

Consequently the union of the extreme blocks in `P` and in the collar has
equal numbers of `A` and `C`, and hence admits a partition into opposite
`A/C` pairs.

#### Proof

The residual bank has signed charge `-q`.  Adding the first connector gives

\[
 \epsilon(a_1)-q
   =-\epsilon(a)-\epsilon(b),
\]

which is (1.5).  Adding the collar charge gives zero.  A finite word in
`A,C` has total signed charge zero exactly when its two letter counts are
equal, so its letters pair oppositely.  \(\square\)

This identity is valid in all four residual-multiplicity cases; no unique
residual connector is assumed.

## 2. Literal midpoint paths

There are two oriented collar--packet paths ending at the same midpoint:

\[
 \begin{aligned}
 A\mid C:quad
 0022&\to0112\to0121\to0211=H\mid M,\\
 C\mid A:quad
 2200&\to2110\to1210\to1120\to1111\to0211=H\mid M.
 \end{aligned}
\tag{2.1}
\]

Every arrow moves one unit across one adjacent physical edge.  Reversing
the second line takes `H|M` to `C|A`, while reversing the first takes it to
`A|C`.  Hence the source-oriented pair

\[
 A\mid C\longrightarrow H\mid M
                   \longrightarrow C\mid A
\tag{2.2}
\]

and its opposite orientation both pass through the common midpoint and end
at the connectorwise complement.

If both members of an opposite pair lie in the collar, use

\[
                         A\mid C\leadsto H\mid H
\tag{2.3}
\]

from the existing path `0022->0112->0202`, or its reflected orientation;
the audited retirement path takes `H|H` to the complementary ordered pair.

If both members lie in the remote packet, use the existing oriented tags

\[
 A\mid C\leadsto T_A\mid T_C=21\mid01,
 \qquad
 C\mid A\leadsto T_C\mid T_A=01\mid21,
\tag{2.4}
\]

and their audited finalization paths to the complementary pairs.  These
tags retain the source orientation literally.

Finally a neutral collar block has the local fixed-mass path

\[
                         B=20\to11\to02=H,
\tag{2.5}
\]

and a neutral packet block remains `B`.

## 3. Exact bounded setup and teardown at paired endpoints

Choose any opposite-pair partition supplied by Lemma 1.1, deterministically
from the decoded source.  Classify its pairs as collar--collar,
collar--packet, or packet--packet.

### Theorem 3.1 (reservoir-free midpoint normal form)

After bringing the paired blocks next to one another, the literal paths
(2.1)--(2.5) transform

\[
 \bigl(C(a)\mid C(b),\ P\bigr)
          \longrightarrow
 \bigl(H\mid H,\ P_{\rm mid}\bigr)
          \longrightarrow
 \bigl(C^*(a)\mid C^*(b),\ P^*\bigr),
\tag{3.1}
\]

at constant total mass.  Here:

1. every cross-paired packet extreme is `M` in `P_mid`;
2. every internally paired packet extreme is in its oriented `01/21` tag;
3. every neutral packet block is still `B`; and
4. `P^*` is the connectorwise complement of the original packet.

No arbitrary work reservoir, unknown overwritten cell, or scalar prepayment
is used.

#### Proof

Every collar block belongs to exactly one of the following cases.  A neutral
block follows (2.5).  Two oppositely signed collar blocks follow (2.3).  Any
remaining collar extreme is cross-paired with an opposite packet extreme and
follows (2.1).  Hence both collar positions end at `H`.

Every packet extreme is either cross-paired and ends at `M`, or internally
paired and ends at the oriented tags (2.4).  Neutral packet blocks are fixed.
All paths preserve the mass of their paired support, so the complete setup
preserves total mass.

For teardown, use the other branch from the common midpoint in (2.1) on a
cross pair, the complementing retirement branch in (2.3) on an internal
collar pair, and the finalization branch in (2.4) on an internal packet pair.
Every original extreme is thereby replaced by its complement; neutral blocks
remain neutral.  This proves (3.1).  \(\square\)

### Corollary 3.2 (the midpoint retains the source record)

Assume the three-row collar record `R_(a,b)` is held fixed.  Then at the
midpoint checkpoint the original value of every block in the collar and
unfinished packet is recoverable:

* `R_(a,b)` gives the ordered collar and hence the source type opposite each
  cross-paired `M`;
* `01/21` records the orientation of every internal packet pair;
* `B` is fixed; and
* the deterministic opposite-pair rule gives the labelled pairing.

Thus the midpoint operation itself loses no source information.

## 4. Exact remaining occurrence lemma

The theorem assumes that paired remote blocks have been brought adjacent to
the fixed collar or to one another and later returned to their physical
addresses.  Scalar component connectivity does not make those shuttles
occurrence-injective.

The remaining statement is now the following bounded marked-shuttle lemma.

> **Midpoint-packet shuttle lemma.**  With the three-row collar record and
> root phase fixed, realize the deterministic opposite-pair partition by
> marked-corridor shuttles such that every remote block returns to its
> labelled address, all strict local interchange states recover the active
> pair and microstep, and the path families for all source types are
> disjoint.  The setup shuttle ends in the midpoint alphabet of Theorem 3.1;
> the teardown shuttle starts there and ends at the complemented source.

Only at most four packet blocks participate: the first connector and at most
three residual extremes.  The macro checkpoints are already source-decodable
by Corollary 3.2.  What remains is the finite strict-intermediate
visible-cart audit for these marked shuttles before the double head exists.

## 5. Consequence

The arbitrary private-reservoir premise in the previous odd collar proposals
is unnecessary.  The actual unfinished packet supplies exactly the opposite
charge of the fixed collar and is converted reversibly through a
source-decodable midpoint.  An occurrence-labelled proof of the
midpoint-packet shuttle lemma would therefore close both the nine-type collar
and all `0,1,2,3` residual cases without any additional mass bank.
