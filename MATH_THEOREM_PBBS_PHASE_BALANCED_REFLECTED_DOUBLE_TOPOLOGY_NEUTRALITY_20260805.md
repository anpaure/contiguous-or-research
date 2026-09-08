# A phase-balanced reflected resident double is all-width transparent but topology-neutral

**Date:** 2026-08-05  
**Method:** occurrence-labelled cut-path permutation calculus; no search or
computation  
**Status:** unconditional abstract gluing theorem and unconditional
application to the reflected resident double.  A literal PBBS use still
requires the stated typed cross-context gluing to exist on disjoint physical
occurrences.  The theorem proves that, even if it exists, this double is not
a component-fusion actuator.

## 0. Outcome

Let

\[
 A=H_2,\qquad B=H_3
\]

be the small-cycle and fused resident states.  The resident reversal
identities are

\[
 H_1=\operatorname{rev}(A),\qquad
 H_0=\operatorname{rev}(B).                         \tag{0.1}
\]

The smallest phase-balanced reflected double is

\[
 \boxed{
 H_0^-\sqcup H_2^+
       \longrightarrow
 H_1^-\sqcup H_3^+.}                               \tag{0.2}
\]

Its two local upper currents cancel.  This cancellation can be upgraded
from an untyped signed-current identity to an exact occurrence identity if
the complete boundary contexts of the two copies are cross-identified by
reflection.  However, under precisely that identification, the terminal
cut-path successor permutation is the reflected inverse of the initial
permutation.  Therefore:

1. every component word at the terminal state is the reversal of one
   initial component word;
2. every cyclic interval-OR occurrence, at every width, transports exactly;
3. the complete cycle type, and hence the component count, is unchanged.

In particular, with the two copies left separate, (0.2) has component
ledger

\[
                  1+q\longrightarrow q+1.          \tag{0.3}
\]

If a complete typed cross-gluing first joins the doubled path bank into one
cycle, the ledger is instead

\[
                         1\longrightarrow1.         \tag{0.4}
\]

More generally it is always `c -> c`.  Thus the reflected double is a
possible all-width-safe **phase converter**, but not a fusion ear.

## 1. The cut-path anti-conjugacy lemma

Cut a finite directed occurrence system at all named packet boundaries.
Let `P` be the set of resulting directed path occurrences.  A complete
gluing is a permutation

\[
                         s:P\longrightarrow P,      \tag{1.1}
\]

where `s(X)` is the path which follows `X`.  The directed components are
exactly the cycles of `s`.

Let

\[
                         \rho:P\longrightarrow P    \tag{1.2}
\]

be an involution pairing the two physical copies.  It is a **typed
reflection** if the source/owner occurrence word on `rho(X)` is the reverse
of the word on `X`, with the same set value at every reflected occurrence.
All complete left and right contexts, not only the changed screen, are part
of the path word.

Define the reflected gluing

\[
                         s^\dagger=\rho s^{-1}\rho. \tag{1.3}
\]

### Theorem 1.1 (anti-conjugacy)

The cycles of `s^dagger` are in value-preserving bijection with the cycles
of `s`; corresponding component words are reversals.  Consequently:

\[
                  \#\operatorname{cyc}(s^\dagger)
                    =\#\operatorname{cyc}(s),       \tag{1.4}
\]

and, for every width `w`, the occurrence-labelled cyclic interval-OR
multisets agree exactly.

The same statement holds for interval intersections, derivative cells,
coordinate run lengths, and every compiler edge whose extra type data are
transported by `rho`.

#### Proof

Let

\[
             X_0\to X_1\to\cdots\to X_{t-1}\to X_0 \tag{1.5}
\]

be one cycle of `s`.  From (1.3),

\[
 \rho X_0\to \rho X_{t-1}\to\cdots\to\rho X_1\to\rho X_0
                                                               \tag{1.6}
\]

is one cycle of `s^dagger`.  This operation is invertible and therefore
bijection (1.4) follows.  Each path word is reversed by `rho`, and the path
order in (1.6) is also reversed, so the complete concatenated component
word is the reversal of (1.5).  Reflection maps every cyclic interval of
width `w` to one cyclic interval of the same width and same OR value.  The
remaining assertions are the identical occurrence-reflection argument.
`square`

### Corollary 1.2 (cross-coupling does not change the conclusion)

Theorem 1.1 allows arbitrary cross-coupling between the two copies.  It is
not necessary that `s` preserve either copy.  Once the phase-balanced flip
uses the reflected gluing `s^dagger`, the complete cycle type is fixed.

Thus cross-coupling may change the common component count of the two
phases, but it cannot make their component counts different.

## 2. Application to the resident clean `C6`

For the resident `q`-port converter, let `A=H_2` and `B=H_3`.  The state
`A` consists of `q` direct-plus-return cycles and `B` is their fused cycle.
Equation (0.1) gives the reflected states.

Use two occurrence-disjoint, typed-identical copies, denoted `-` and `+`.
Pair an occurrence of the `+` copy with the corresponding reflected
occurrence of the `-` copy.  This gives the typed reflection `rho` of
Section 1.

### Theorem 2.1 (exact reflected-double identity)

Suppose the complete contexts in (0.2) are cross-identified so that every
terminal continuation is the `rho`-reflection of the corresponding initial
continuation.  If `s_0` is the initial cut-path successor permutation, then
the terminal permutation is

\[
                         s_1=\rho s_0^{-1}\rho.     \tag{2.1}
\]

Hence the compound move has exact all-width cyclic occurrence transport
and

\[
                         c(s_1)=c(s_0).             \tag{2.2}
\]

#### Proof

On the `+` copy, (0.2) replaces `A` by `B`.  Reflection sends this to the
replacement `rev(B) -> rev(A)` on the `-` copy, which is exactly
`H_0 -> H_1`.  Because a reflected directed continuation is read in the
opposite order, the successor relation is the inverse relation conjugated
by `rho`, giving (2.1).  Theorem 1.1 now applies. `square`

This is the occurrence-level strengthening of cancellation of the two
signed local currents.  The complete-context hypothesis is load-bearing.
Pairing only the three saturated set values, while leaving their exterior
occurrences independent, does not imply (2.1).

### Corollary 2.2 (the independent ledger)

With no cross-gluing between the copies,

\[
 c(H_0^-\sqcup H_2^+)=1+q
   =q+1=c(H_1^-\sqcup H_3^+).                     \tag{2.3}
\]

For the PBBS clean C6, `q=3`, so the ledger is `4 -> 4`.

### Corollary 2.3 (the fully crossed abstract ledger)

At the cut-path level, suppose the `2q` paths are denoted
`X_i^+,X_i^-`, and the initial complete cross-gluing is

\[
 s_0(X_i^+)=X_i^-,\qquad
 s_0(X_i^-)=X_{i+1}^+                              \tag{2.4}
\]

with indices modulo `q`.  Then `s_0` is one `2q`-cycle.  Its reflected
terminal `s_1` is also one `2q`-cycle.  Thus a literal realization of all
the typed seams in (2.4) would give the ledger `1 -> 1`, not a fusion.

#### Proof

Squaring (2.4) advances `i` by one on either sheet, so all `2q` paths lie
in one cycle.  Theorem 1.1 gives the terminal assertion. `square`

Corollary 2.3 is only a topology calculation.  It does not assert that the
PBBS host supplies the required typed physical cross seams; that is a
separate planting question.

## 3. Why arbitrary-exterior cancellation forces this neutral form

The first resident boundary casualty has penetration `(d+2,1)`.  Its
untyped value survives at the opposite penetration `(1,d+2)`, but at a
different named boundary.  A private exterior label distinguishes those
two occurrences.

For two copies, the only local occurrence with the opposite signed role
and the required penetration is the reflected boundary occurrence in the
other copy.  Therefore cancellation valid for every independently chosen
exterior value must transport the **complete** context occurrence across
the two copies; matching only the internal target value is insufficient.

### Theorem 3.1 (topological no-go for the simple phase-balanced double)

Within the following scope:

1. two typed-identical resident/common-history copies;
2. no alternative witness outside the two copies;
3. arbitrary privately labelled boundary contexts; and
4. cancellation obtained by a bijection of complete context occurrences,

every all-width-transparent phase-balanced flip is a reflected
anti-conjugacy on the named cut paths.  In particular it preserves the
component count and cannot merge a positive number of factor components.

#### Proof

Give every named boundary context its own private label.  Any preserved
extended interval containing that label must use the transported copy of
that same context.  The boundary-typed resident calculation forces the
lost `(d+2,1)` occurrence to pair with its reflected `(1,d+2)` occurrence.
Applying this at every named boundary fixes the complete reflected context
bijection `rho`.  Directed reflection reverses successor order, so the
terminal gluing is (1.3).  Equation (1.4) proves the no-go. `square`

The conclusion is specific to cancellation **inside this doubled macro**.
A larger compound packet may evade it by creating a new alternative
witness, by changing the exterior bank, or by using a non-bijective
protected occurrence reservoir.

## 4. The outer-interface consequence

For a closed doubled macro, Theorem 2.1 is a genuine full cyclic-deck
identity.  For an open macro, reflection exchanges its two ends.

### Corollary 4.1 (pointwise-fixed exterior obstruction)

If the left and right exterior occurrences carry distinct private labels
and must remain fixed pointwise, the reflected double alone is not an
arbitrary-exterior-transparent open replacement.  It becomes transparent
only if:

1. the two exterior contexts are themselves exchanged/transported by
   `rho`;
2. the interface is an unordered paired interface on which that exchange
   is accepted; or
3. independent alternative witnesses cover the crossing targets.

#### Proof

Reflection maps a left-crossing interval to a right-crossing interval.
A private left label cannot occur in the latter if the two exterior
contexts are held pointwise fixed.  This is the private-context necessity
argument at the outermost boundary. `square`

Thus cross-identifying the internal packet boundaries does not, by itself,
produce the orientation-preserving fixed outer interface requested by a
local replacement against an arbitrary frozen word.

## 5. What the double is still good for

The result is negative only as a fusion theorem.  If topology has already
been solved and the induction state accepts a reflected paired interface,
the double supplies a strong zero-charge phase conversion:

* complete cyclic OR deck at every width;
* complete strict-lower occurrence transport from the common-history
  source;
* residence and source length unchanged;
* compiler transport whenever its additional typed state is `rho`-functorial.

It can therefore synchronize relative phase without paying an upper
sidecar.  It cannot reduce the number of components or any other
reflection-invariant defect.

## 6. Scope and dependencies

The resident identities and the first boundary casualty are from:

* `MATH_THEOREM_PBBS_RESIDENT_C6_HYBRID_SOURCE_LOWER_TRANSPORT_AND_UPPER_MONOTONICITY_20260805.md`;
* `MATH_THEOREM_PBBS_CLEAN_C6_COMMON_HISTORY_ALL_LOWER_DEPTH_LIFT_AND_SHARP_UPPER_BOUNDARY_20260805.md`;
* `MATH_THEOREM_PBBS_RESIDENT_C6_BOUNDARY_TYPED_EXTERIOR_OBSTRUCTION_20260805.md`.

Proved here:

1. the exact reflected anti-conjugacy for arbitrary cross-couplings;
2. all-width occurrence transparency under complete context pairing;
3. equality of the complete component cycle type;
4. the `q+1 -> q+1` independent ledger and abstract `1 -> 1` fully crossed
   ledger; and
5. failure against pointwise-fixed arbitrary exteriors.

Not proved:

1. existence of the typed physical cross seams in a PBBS owner factor;
2. a phase-balanced double which changes component count;
3. a larger packet with an exterior alternative-witness reservoir;
4. zero-gap residence or typed maximal common-cap regeneration; or
5. any `B(k)+O(1)` or exact all-`k` upper bound.
