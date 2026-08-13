# The second shadow is exactly the double-turn Middle Levels gate

**Date:** 2026-08-13  
**Status:** unconditional component-level equivalence and strongest unconditional
path-forest input; existence of the common chronology remains open

## 1. Parameters

Put

\[
 \Omega=[2r-1],\qquad m=r-1,
\]

and let

\[
 \mathcal L={\Omega\choose r-1},\qquad
 \mathcal M={\Omega\choose r},\qquad
 \mathcal U={\Omega\choose r+1}.
\]

The two middle shores have equal size

\[
 W=|\mathcal L|=|\mathcal M|={2r-1\choose r},       \tag{1.1}
\]

while

\[
 U=|\mathcal U|={2r-1\choose r+1},\qquad
 W-U={2W\over r+1}=\operatorname {Cat}_r.           \tag{1.2}
\]

## 2. Minimum odd cycles and Middle Levels components

Let

\[
 C=(L_0,M_0,L_1,M_1,\ldots,L_{2r-2},M_{2r-2},L_0) \tag{2.1}
\]

be one component of a Hamilton cycle of `ML(2r-1)` after an arbitrary
decomposition into minimum components, or simply one alternating cycle of
length `2(2r-1)`.

Suppose the lower sets `L_i` are all the `(r-1)`-windows in a cyclic
coordinate order

\[
 \sigma=(x_0,\ldots,x_{2r-2}).                      \tag{2.2}
\]

Then the unique alternating middle sets between consecutive lower windows
are

\[
 L_i\cup L_{i+1}=I_i^r(\sigma),                    \tag{2.3}
\]

after shifting the starts.  Hence (2.1) is exactly the ordinary Middle
Levels lift of one wreath.  Conversely, every minimum alternating cycle in
`ML(2r-1)` suppresses to a minimum odd cycle in `KG(2r-1,r-1)`, and every
minimum odd cycle is a wreath.  Thus:

> A partition of both middle shores into alternating cycles of length
> `2(2r-1)` is the same object as an exact wreath factor on either shore.

## 3. Second-shadow coverage and upper turns

Suppress the lower shore of any alternating Middle Levels cycle.  The
resulting rank-`r` Johnson edge

\[
 M_{i-1}M_i                                             \tag{3.1}
\]

has intersection `L_i`, so its lower colours are automatically exact
when the full Middle Levels cycle is Hamiltonian.

For the wreath normal form (2.2)--(2.3), its upper colour is

\[
 M_{i-1}\cup M_i=I_{i-1}^{r+1}(\sigma).              \tag{3.2}
\]

Taking complements in `Omega` gives

\[
 \Omega\setminus I_{i-1}^{r+1}(\sigma)
     =I_{i+r}^{r-2}(\sigma).                         \tag{3.3}
\]

The right side is precisely a length-`r-2=m-1` second-shadow window in
the same wreath order.

### Theorem 3.1 (exact equivalence)

For an exact wreath factor `mathcal F`, the following are equivalent.

1. Every rank-`r-2` second-shadow target occurs in a wreath order of
   `mathcal F`.
2. In the corresponding partition of `ML(2r-1)` into minimum alternating
   cycles, the rank-`r` upper turns cover every member of `mathcal U`.

Moreover, if the minimum components can be fused by degree-preserving
switches which preserve upper-turn coverage, the fused Middle Levels
Hamilton cycle is **double-turn**: intersection-exact and
union-surjective on its suppressed rank-`r` Johnson cycle.

#### Proof

Complementation is a bijection

\[
 {\Omega\choose r-2}\longleftrightarrow
 {\Omega\choose r+1}.
\]

Equations (3.2)--(3.3) identify occurrence in the second-shadow row with
occurrence of the complementary upper-turn colour, component by component
and start by start.  Middle Levels Hamiltonicity makes the lower turns
exact automatically.  This proves every assertion. `square`

Thus the all-`r` second-shadow problem is the local/component form of the
double-turn gate.  Global fusion is a further topology condition and must
not be inferred from the component theorem alone.

## 4. What is unconditional

There are three separate unconditional inputs.

1. The Middle Levels theorem supplies an intersection-exact Hamilton cycle
   on `mathcal M` after suppressing `mathcal L`.
2. A tight enumeration of levels `r,r+1` supplies a generally different
   union-surjective Hamilton cycle on `mathcal M`.
3. Deleting the `Cat_r` direct steps of that upper tight enumeration gives
   a spanning `Cat_r`-component linear forest on `mathcal M` whose union
   colours are bijective onto `mathcal U`.

These facts are audited in
`MATH_AUDIT_GMM_TIGHT_ENUMERATION_DOUBLE_TURN_FUSION_AND_BALANCED_CUT_20260805.md`.
The literature does not identify the two Hamilton orders in items 1 and 2.

There is also an unconditional lower-side forest stronger than a generic
matching projection.  Apply the two-level saturating-cycle theorem to
levels `r-2,r-1`.  Suppression gives a Johnson cycle on `U` distinct
members of `mathcal L` whose lower-turn colours cover every
rank-`r-2` set exactly once.  Open one edge through an unused lower owner,
as in
`MATH_THEOREM_SECOND_SHADOW_CANONICAL_NO_AND_RAINBOW_TWO_SDR_REDUCTION_20260813.md`.
The result is one rainbow path plus `Cat_r-1` isolates on `mathcal L`.

Hence all target, degree-two, and forest constraints already have exact
solutions.  The only missing operation is to choose a common chronology
and perform the balanced endpoint completion without destroying the
opposite turn row.

## 5. Exact remaining theorem

The positive gate separates into two exact equivalences and one implication.

1. There is an exact wreath factor on rank `r-1` whose second shadow covers
   every rank-`r-2` target.
2. There is a partition of `ML(2r-1)` into minimum alternating cycles whose
   rank-`r` upper turns cover every rank-`r+1` target.
3. There is an upper-turn-surjective Middle Levels Hamilton cycle.
4. There is a Hamilton cycle of `J(2r-1,r)` whose intersections are
   bijective onto `mathcal L` and whose unions are surjective onto
   `mathcal U`.

Items 1 and 2 are equivalent by Theorem 3.1.  Items 3 and 4 are equivalent
by suppressing or reinserting the lower shore.  If a witness for item 2
can be fused, preserving upper-turn coverage, then it yields item 3.

The reverse implication from item 3 to item 2 is not formal: a double-turn
Hamilton cycle need not admit cuts into length-`2(2r-1)` wreath returns.
Likewise, item 2 alone does not supply the fusion.  Thus the two honest
all-`r` targets are:

1. construct the shadow-surjective minimum-component factor; and
2. prove an upper-turn-preserving fusion theorem if a single Euler carrier
   is required.

Equivalently, one may attack the stronger one-shot target:

> Construct a double-turn Middle Levels Hamilton cycle whose chronology
> admits the required protected rail interpretation.

The canonical MSW factor is not a witness: its missing second shadow is at
least `(1/32-o(1))W` by the audited marked-gap theorem.  A different
fourteen-wreath factor is a witness at `r=5`.  Therefore the obstruction is
specific to the canonical recursion, not universal.

## 6. Conclusion

The strongest proof-safe formulation is

\[
 \boxed{
 \text{second-shadow-surjective wreath factor}
 \;=\;
 \text{upper-turn-surjective minimum-component chronology}.}
\]

Saturating cycles solve either turn row separately and even solve the
corresponding rainbow linear forests exactly.  The unresolved theorem is
their common chronological fusion.
