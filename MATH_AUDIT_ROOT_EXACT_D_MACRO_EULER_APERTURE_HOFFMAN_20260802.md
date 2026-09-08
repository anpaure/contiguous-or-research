# Audit of the exact-`d` macro-Euler aperture/Hoffman theorem

**Date:** 2026-08-02  
**Audited theorem:**
`MATH_THEOREM_ROOT_EXACT_D_MACRO_EULER_APERTURE_HOFFMAN_AND_C0_GATE_20260802.md`  
**Theorem SHA:**
`bf0e5515d0f395eb060cd017f93987fb173009595dcf7cd284fcb35427d8f824`  
**Verdict:** `PASS_SCOPE_SAFE`.

## 1. Fixed-state overlap repair

The new transitivity lemma is correct and does not reinstate the previously
rejected pairwise-port argument.

For full overlap, starts satisfy `a_(i+1)=a_i+ell_i` and both starts and
ends are strictly increasing.  If a global source address belongs to two
nonadjacent block images, it belongs to every intervening image and to each
adjacent `d`-overlap.  Once one literal realization of every component has
been fixed, adjacent rail equality therefore identifies all letters at that
address transitively.

The qualifications are load-bearing.

* A state-forgetting port matching can use different realizations of one
  component on its two incident seams; transitivity does not repair that.
* Equality of letters does not prevent two capacity-one interval pins from
  acquiring the same global address.
* Componentwise clipped history is not propagated aggregate history.  The
  complete input-to-output transition, not only a local summary, must be in
  the macro token.

The exclusive-core formula is exact.  Previous blocks end no later than
`a_i+d-1` and later blocks begin no earlier than `a_i+ell_i`.  Thus an
internal core has length `max(ell_i-d,0)`, while the first and last blocks
each have an exclusive core of length `ell_i`.  Pin intervals placed wholly
inside these disjoint cores cannot collide across components.  The count
`q(q+1)/2` is only an address count; the theorem correctly does not infer
target-OR supply from it.

The quotient-address Hall theorem is the exact, less restrictive row.  It
first maps every candidate occurrence to its final global interval address,
deduplicates identified occurrences, and removes protected addresses.  The
deficient Hall formula then gives

\[
 \Delta_{\rm pin}=
   \max_Y\left(|Y|-\left|\bigcup_{t\in Y}\Gamma_t\right|\right)
\]

as the exact number of unmatched tasks.  Thus `Delta_pin=0`, rather than
the private-core condition, is the minimal address criterion on a fixed
order.  Private cores are correctly retained only as a decomposed
sufficient certificate.

## 2. Macro-Euler and aperture audit

With boundary convention

\[
                  \partial(u\to v)={\bf1}_v-{\bf1}_u,
\]

a residual trail from `beta` to `tau` has boundary
`1_tau-1_beta`.  The virtual closing arc `c:tau->beta` has the opposite
boundary.  Hence balance of the selected residual arcs plus `c` has the
correct sign.

Weak connectivity on the nonisolated support plus balance is exactly the
directed Euler-circuit criterion.  Terminal isolation is essential: because
`r_o` is the unique selected entrance to `tau` and `c` its unique exit,
every Euler circuit traverses `r_o,c` consecutively.  Cutting immediately
after `c` therefore starts at `beta` and ends with `r_o` at `tau`.
Prepending the fixed pivot makes it the first component.  Requiring the
last owner of `r_o` to contain `o` is exactly the forward phase of the
audited endpoint-aperture theorem; whole-state reversal gives the opposite
phase.

No source charge is assigned to `c`.  It is only a balancing device and is
removed before the physical word is read.

## 3. Hoffman sign and integrality audit

Let `P={c} union R` and `eta_R=partial P`.  If free tail and head count
vectors are `p,q`, total balance is

\[
                         p-q=\eta_R.
\]

For a state set `X`, at least `ell_A(X)` free tails must lie in `X` and at
most `r_H(X)` free heads can lie there.  Therefore

\[
                    \ell_A(X)-r_H(X)\le\eta_R(X)
\]

has the stated orientation.  Integral polymatroid intersection supplies
aggregate integer counts, and the two role-to-state `b`-matchings choose one
tail and one head per component.  Pairing those two choices is literal only
because every cross-pair belongs to `A_K x H_K`.  The reserved bank already
spans the used state set, so the proof does not silently infer connectivity
from balance.

The converse in Corollary 3.2 is also correctly scoped to a pure rectangle
atlas.  From any connected selector one may reserve its distinct-colour
spanning-tree arcs (and the terminal arc), restrict every remaining
rectangle to the used state set, and apply the necessary cut inequalities.
For a general correlated relation containing a rectangle, the theorem
claims sufficiency only.

## 4. Support-first Rado--erosion audit

The support-first alternative is logically sound and strictly avoids an
unproved componentwise source-rail factorization.

* In one rooted phase, the occurrence support of the full owner Hamilton
  path is an incidence matching whose rooted graph is itself a path.
  Protected Rado deficiency zero therefore selects `U` upper-distinct edges
  forming `Q_0`.  Removing those `U` edges from the `W-1` path edges leaves
  exactly `C-1` connectors between the `C=W-U` contiguous components.
* The nonnegative defect `Delta_er` is zero exactly when the three
  arbitrary-window maximal-erosion conditions hold: every pin lies in its
  envelope, every source envelope is nonempty, and every prescribed union
  is covered by its envelopes.  Choosing `A_j=E_j` then realizes all rows
  simultaneously.
* If a component occupies depth indices `[b,b+ell-1]`, restricting the one
  global source word to `[b,b+ell+d-1]` reproduces exactly those depth cells.
  Two consecutive restrictions share the literal positions
  `[b+ell,b+ell+d-1]`.  Hence the exact-`d` ports are consequences of the
  global antecedent, not additional choices.

The owner-history acceptance and endpoint aperture remain explicit inputs.
Neither Rado deficiency zero nor erosion defect zero implies them.  Likewise
the five zero-defect rows in (3A.7) are a sufficient decomposition; their
simultaneous canonical existence is not claimed.

The unsaturated-state rider is also necessary.  If an internal `d`-state
already unions to its rank-`r` owner, both adjacent `(d+1)`-windows have that
same owner, violating one-copy simplicity.  The theorem therefore does not
misuse the known empty/proper-depth hinge rectangles: those menus are
saturated and are allowed only at a boundary or next to the unique
nonowner.  A positive owner-level Hoffman implementation still needs
unsaturated completed rectangles (or a nonrectangular integral selector).

## 5. Correlation obstruction and gammoid scope

The depth-one reversal example is literal.  For disjoint nonempty letters
`U,V`, the two blocks `(U,V)` and `(V,U)` have the same owner `U union V`
and opposite state boundaries.  Their half--half average is balanced, but
neither integral choice is.  Tail and head projections both equal
`{U,V}`.  Completing them to a rectangle introduces the loops `(U,U)` and
`(V,V)`, whose owners are wrong.

An unpaired fixed-sink gammoid rank cannot distinguish the crossed
two-pairing from its complete rectangle: both source subsets link to an
undifferentiated sink bank with the same ranks.  A pairing-resolved
transition relation or a proved rectangle subatlas is therefore genuinely
necessary.  The theorem does not claim that strict gammoids are useless;
they remain valid for internal disjoint-linkage or compiler-route rows.

## 6. Independent finite replay

The independent script

`scratch/audit_root_exact_d_macro_euler_aperture_hoffman_20260802.py`

has SHA

`c8b4a33f591151b047ab4e939d491da077541aab2487d50b4ca749e226d978b8`

and returns

```text
PASS
overlap_cases=5440 shared_addresses=59936 nonadjacent_shared=9856
pin_menus=15 pin_hall_tests=3375
born_port_partitions=1020
saturated_repeat_antecedents=15159
hoffman_systems=2401 hoffman_tests=45619
terminal_euler_cases=1364 terminal_euler_positive=298
correlated_legal=2 cartesian_hull=4
```

The overlap replay exhausts depths `1..4`, two through five blocks, and all
component lengths `1..4`.  The Hoffman replay exhausts all 2,401 two-role
rectangle systems on three states against all 19 zero-sum integral boundary
vectors in `[-2,2]^3`.  The aperture replay independently compares the
balanced-connected criterion with all residual arc orders through five
arcs.  The script also checks the projected-rectangle false loops in the
literal correlation obstruction.  Separately, it exhausts all 3,375
nonempty three-task candidate families on four already-quotiented addresses
and compares Hall with direct injective selection.  Finally, 1,020
partitions of small global source words independently confirm that
restriction to depth-row components reproduces their windows and gives
literal full-`d` overlaps.  It also checks 15,159 small flat antecedents of
the saturated-state premise and always obtains the forced repeated owner.

## 7. Scope verdict

The theorem converts `OPEN-2` and the endpoint portion of `OPEN-3` into an
exact complete-state macro condition and, on the rectangle face, a finite
Hoffman deficit plus protected-skeleton condition.  It does **not** prove
that the canonical Catalan atlas contains the rectangles, that the
owner-preserving reset rethread exists, that private cores contain a
complete target-correct compiler bank, that the terminal casualty family is
empty, or that a compatible infinite regenerative spine exists.

Accordingly the displayed `B+1` conclusion is conditional on the explicitly
marked `HYP-1`--`HYP-6`; it is not a new unconditional upper bound.
