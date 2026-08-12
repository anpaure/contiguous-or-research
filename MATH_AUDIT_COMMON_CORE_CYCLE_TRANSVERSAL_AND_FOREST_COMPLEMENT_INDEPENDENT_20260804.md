# Independent audit: common-core cycle transversal and forest complement

**Date:** 2026-08-04  
**Audited file:**
`MATH_THEOREM_COMMON_CORE_CYCLE_TRANSVERSAL_AND_FOREST_COMPLEMENT_20260804.md`  
**Audited SHA256:**
`4530f1c8f204c3ad98dab1934a3ee506d6b2a480fae04e516cf5ab7c2432cea3`  
**Verdict:** **GO with one scope-wording correction and one useful exact
extension corollary supplied below.**  The graphic-nullity identity,
rank-constrained factor equivalence, and zero/constant-cost fusion
implications are correct.  The final promotion-atlas paragraph must not
identify a coordinate-containment core with an ordered de Bruijn history
core.

No search, solver, or finite computational enumeration is used.

## 1. Graphic-nullity identity

Let `F` be a spanning two-factor.  Restrict `F-S` to one cycle component
`C` of `F`.

* If `E(C) cap S=emptyset`, the restriction remains the whole cycle and has
  graphic nullity one.
* If `E(C) cap S` is nonempty, deletion of those edges leaves a disjoint
  union of paths and isolated vertices and has nullity zero.

The restrictions belonging to distinct factor cycles are vertex-disjoint,
so nullity adds.  Therefore

\[
 c_S(F)=\beta(F-S).
\]

The equivalence between “every cycle meets `S`,” “`F-S` is a forest,” and
“nullity zero” follows immediately.

The convention that isolated vertices count in `kappa` is correct and
necessary: an isolated vertex contributes `0-1+1=0` to nullity.

## 2. Forest-extension and rank forms

If `eta=0`, take

\[
                         R=F-S,\qquad T=F\cap S.
\]

Then `R` is a forest, `T subset S`, and `R union T=F`.  Conversely, any
factor of this form has forest complement.  Corollary 1.2 is exact.

For a finite loopless graph, graphic independence is equivalent to

\[
                         |E_R(U)|\le|U|-1
 \qquad(\varnothing\ne U\subseteq V),
\]

where `E_R(U)` denotes the edges of `R` induced by `U`.  Thus (1.5) is the
standard rank-constrained factor formulation.  It would be helpful for the
source to define `E(U)` explicitly as induced edges, but the mathematics is
unambiguous.

## 3. Exact fixed-edge extension corollary

On the Middle-Levels fixed-edge guarded face, the forest formulation admits
the following exact Ore--Ryser specialization.

Let `D` be the forced degree-at-most-two bank, let `Z` be a fixed forbidden
bank disjoint from `D`, and let `S` be the candidate common-core occurrence
bank.  Then a factor containing `D`, avoiding `Z`, and meeting `S` in every
component exists if and only if there is a forest

\[
 R\subseteq E\setminus(S\cup Z),
 \qquad D\setminus S\subseteq R,
\tag{3.1}
\]

such that, with

\[
                         Y_R
 =Z\cup\bigl(E\setminus(R\cup S)\bigr),
\tag{3.2}
\]

the exact guarded extension deficiency satisfies

\[
                         \delta_\star(D,Y_R)=0.
\tag{3.3}
\]

### Proof

For a witnessing factor put `R=F-S`.  The nullity theorem makes it a
forest, it contains `D-S`, and `F` avoids `Y_R`, proving (3.3).

Conversely, a factor supplied by (3.3) contains `D` and uses outside-`S`
edges only from `R`.  Hence `F-S subset R` is a forest, so every factor
cycle meets `S`.

Condition `D-S subset R` ensures `D subset R union S`; together with
`D cap Z=emptyset`, this makes `D` disjoint from `Y_R`, as required by the
extension theorem. \(\square\)

This is an addition rather than a correction to the source.  It gives the
requested exact factor-extension oracle.  It applies only after nonfactor
guards have been compiled into fixed protected/forbidden edges or a larger
occurrence-state expansion.

## 4. Zero-cost completed-hinge implication

When every factor component meets `S`, choose one occurrence-labelled
`S`-hinge from each.  Joint all-pairs completion means every cyclic
permutation of the selected heads is simultaneously legal and preserves
the complete shared ledger.  The component successor permutation is that
head permutation, so choosing one cycle fuses all components without adding
a position.

The source correctly states that all-pairs completion may be weakened to a
selected compatibility digraph containing a directed Hamilton cycle.

The “jointly” qualifier is load-bearing: individually legal head
replacements may share a capacity-one resource and fail simultaneously.

## 5. Constant-cost overlap implication

If every selected exit ends and every selected entry begins with one common
length-`d-K` history, bare history distance is at most `K`.  The source also
assumes a declared guard-preserving connector of that charge and a
product-separable atlas.  With at most `C` factor components, a linear order
uses at most `C-1` connectors, giving

\[
                         A+(C-1)K.
\]

This implication is correct.  Neither the common literal substring nor
component count alone proves the guard/product hypotheses.

## 6. Quantifier obstruction

Attaching independent formal history tags to factor components leaves all
incidence, owner, and immediate-palette data unchanged.  If compatibility
requires tag equality, a distinguished tag bank misses every differently
tagged component.  This correctly proves that those projected data do not
imply `eta=0`.

It is a logical nonimplication, not a claim that no literal Boolean lift can
correlate the tags.  The source uses it only in that scoped sense.

## 7. Required wording correction on the promotion input

The final paragraph says that the promotion atlas has “local ordered common
blocks longer than the OR depth.”  This must not be read as a proved common
history block.

In the promotion theorem, `Q_U` is a coordinate-containment core.  The
retained phases are precisely those whose central `2H`-word lies in
`U-Q_U`, outside that core.  The tail words, orders, and cores also vary by
top.  What is proved is:

* local core-safe paths whose available word length exceeds `d`; and
* masks on each such path containing one coordinate core.

What is not proved is one ordered length-`d-K` suffix/prefix shared by ports
in different factor components.  Thus the safe replacement wording is:

> The promotion atlas has ample local path length and coordinate-core
> aperture; raw length is not the obstruction.  It does not supply one
> common de Bruijn history or place that state in every factor component.

With this interpretation/correction, the source's final conclusion is
fully valid.

## 8. Final verdict

The exact common-core supply gate is

\[
                         \eta_{\mathcal F}(S)=0,
\]

equivalently `F-S` forest for some guarded factor.  A jointly completed
all-pairs hinge class then gives zero-cost fusion, while a common guarded
`K`-router plus bounded components gives constant-cost fusion.

The existing Pascal/promotion inputs do not produce such an occurrence bank
`S`; that remains the construction theorem.
