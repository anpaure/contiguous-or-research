# Annealed quarantine--Haxell composition

**Date:** 2026-08-06  
**Method:** add the two terminal loss variables before selecting an outcome;
no conditioning on cleanup  
**Status:** unconditional abstract composition theorem.  Applied to the
current bottom architecture, it removes the need for a separator-prefix
weighted cleanup law.  The unweighted selected-relation estimate is still
an input.

## 1. The quantifier issue

The selected-relation quarantine theorem produces a random surviving macro
matching `M_good` with two properties:

1. prescribed marked blocks in surviving macros satisfy a hereditary
   killed-event cylinder under the **raw** law; and
2. the expected number of quarantined macros is small.

It is unsafe to condition this law on the event that the quarantine is
small.  A rare separator cylinder can be disjoint from that event.  Such a
conditioning step is unnecessary when the only later randomized use of the
cylinder is to prove an expected exceptional-task bound, followed by a
deterministic Haxell completion.

## 2. Abstract annealed composition

Let `B` denote all banks reserved before the macro selector is run.  On one
finite probability space, let

* `M_good` be the quarantined surviving macro matching;
* `Q>=0` be its total cleanup charge, measured in final lower-resource
  units;
* `Y>=0` be the additional lower-resource charge of all bottom tasks
  discarded by the option-degree/resource-load cleanup; and
* `L_0>=0` be any deterministic preliminary separator charge.

Assume the following.

### (A1) Raw hereditary cylinder

Conditionally on `B`, every allowed stopped separator exposure and every
compatible collection of still-unexposed marked blocks in `M_good` obeys
the fixed-factor cylinder required by the bottom option-tail theorem.

This is a statement about the raw quarantined law.  It is not conditioned
on `Q`.

### (A2) Annealed cleanup

For an absolute `C_Q`,

\[
                  \mathbb E Q\le C_Q {M\over d}.
\tag{2.1}
\]

### (A3) Annealed bottom loss

Applying the option-degree and size-biased resource-load argument under
the cylinder in (A1) gives

\[
                  \mathbb E Y=o(M/d).
\tag{2.2}
\]

For every realized environment, after the tasks counted by `Y` are
discarded, the deterministic independent-transversal theorem completes all
remaining bottom tasks.

### Theorem 2.1 (annealed terminal selection)

Under (A1)--(A3), there is one deterministic realization of the banks,
raw macro clock, quarantine, and bottom choices for which the bottom is
completed and

\[
 \boxed{
             L_0+Q+Y
             \le L_0+C_Q{M\over d}+o(M/d).}
\tag{2.3}
\]

In particular, no lower bound on

\[
       \Pr(Q\le C M/d\mid F)
\]

is required for separator-prefix events `F`.

#### Proof

The killed-event proof of (A1) is valid under the raw law, including after
every stopped separator exposure.  Therefore every factorial-moment and
Laplace calculation used to prove (A3) may be performed under that same
law.  At no point is the law conditioned on a terminal cleanup event.

By linearity of expectation,

\[
 \mathbb E(L_0+Q+Y)
 \le L_0+C_Q{M\over d}+o(M/d).
\tag{2.4}
\]

The probability space is finite.  Hence some realization has total charge
at most the right side of (2.4).  For that realization, the pointwise last
clause of (A3) supplies the deterministic Haxell independent transversal.
All retained macros are genuine members of `M_good`, so all pointwise
resource-disjointness, tile, and queue invariants survive.  This proves
(2.3).  \(\square\)

The same proof works if `Q` and `Y` are first expressed in different
units: multiply each by its deterministic maximum number of lower-resource
casualties before adding them.

### Corollary 2.2 (add a terminal success event)

Let `J` be any terminal event on which a later deterministic component
joiner is available.  If

\[
                         \Pr(J)\ge\eta>0
\tag{2.5}
\]

for an absolute `eta`, then one may additionally require `J` in Theorem
2.1, at the price of the fixed factor `eta^-1`:

\[
 \boxed{
     J\text{ holds},\qquad
     L_0+Q+Y
       \le L_0+\eta^{-1}
          \bigl(C_QM/d+o(M/d)\bigr).}
\tag{2.6}

No independence between `J`, cleanup, or the marked cylinder is required.

#### Proof

Put `Z=Q+Y`.  Since `Z>=0`,

\[
 \mathbb E[Z\mid J]
 ={\mathbb E[Z1_J]\over\Pr(J)}
 \le {\mathbb EZ\over\eta}.
\]

Some outcome in `J` has `Z` at most this conditional mean.  On that
outcome apply both deterministic terminal completions.  \(\square\)

Thus a later component theorem need not preserve a cleaned random law
either.  A pointwise joiner is strongest, but an unconditioned constant
success probability under the same raw experiment is also sufficient.

## 3. Verification against the current bottom ingredients

The hypotheses align exactly with the existing theorems.

1. `MATH_THEOREM_SELECTED_RELATION_QUARANTINE_FOR_REGENERATIVE_CYLINDERS_20260806.md`
   proves (A1), once all marked block types through order `O(d)` are
   included in the quarantine tests.  Its proof is already stopped and
   hereditary.
2. If `B_0+B_1` is the number of individually bad selected macros plus bad
   selected relations, that theorem gives a cleanup of at most
   `B_0+2B_1` macros.  Since one macro has `O(d)` lower resources, the raw
   estimate

   \[
               \mathbb E(B_0+B_1)=O(M/d^2)
   \tag{3.1}
   \]

   implies (A2).
3. `MATH_THEOREM_PRE_RESERVED_KY_OPTION_TAIL_AND_TWO_MARK_CYLINDER_GATE_20260805.md`
   derives exponentially small expected low-option and size-biased
   high-load losses from precisely a fixed-factor cylinder, conditionally
   on the pre-reserved banks.  Integrating over the banks proves (A3).
4. `MATH_THEOREM_SEPARATOR_AMPLIFIED_BOTTOM_INDEPENDENT_TRANSVERSAL_20260805.md`
   is pointwise after its exceptional tasks are removed, supplying the
   deterministic last clause of (A3).

Thus the required stochastic estimate on the bottom branch is only (3.1).
The stronger cylinder-weighted Bellman target `(JCYL)` is sufficient but
not necessary for this terminal use.

## 4. Correct replacement target

The bottom dynamic problem is now:

> **Raw selected-relation estimate.**  Under the unconditioned adaptive
> balanced-doublet clock (with the pre-reserved banks included in the
> initial sigma-field), prove
>
> \[
>            \mathbb E(B_0+B_1)=O(M/d^2).
> \tag{4.1}
> \]

The exact uniform coordinate-switch identity, earliest-blocker
decomposition, and one-birth lemma reduce (4.1) to the unweighted
first-kill coefficient comparison.  The one-resource contribution is the
rooted-overlap ledger `(ROc)` and the correlated multiple-entry
contribution has the `(FE3)` first-two-hit form.

No comparison with `h_i^F=Pr(F|F_i)` is needed in (4.1).  Consequently the
possible mismatch between future-fugacity weights and arbitrary
separator-cylinder Doob weights is no longer a bottom obstruction.

## 5. Scope

This theorem does not prove (4.1).  It also does not prove the PBBS deep
payload bridge, odd midpoint-packet shuttle, or terminal component joining.
It proves a quantifier reduction only:

\[
 \boxed{
 \text{raw hereditary cylinder}
 +\text{ expected quarantine}
 +\text{ expected Haxell loss}
 \Longrightarrow
 \text{one deterministic small-loss completion}.}
\]

The reduction is valid because Haxell completion is deterministic after
the exceptional-task set is exposed.  It must not be reused before a later
stage that genuinely needs the cleaned output itself as a conditioned
random law.
