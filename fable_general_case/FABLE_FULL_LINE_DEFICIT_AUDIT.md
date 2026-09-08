# Adversarial audit of FABLE_FULL_LINE_DEFICIT_RESOLUTION.md

## Verdict

**PASS with two flagged dependencies (A1, A2) and one unproved lemma
(Lemma M, flagged by the resolution itself).** The joint charge Theorem 5.1,
Corollary 5.2, Lemma 6.1, Theorem 7.1, and the reduction Theorem 9.1 are
correct modulo the flags below. Neither Outcome A nor Outcome B is claimed;
the deliverable is the minimal-lemma branch, and its reduction is complete.

## Item-by-item

### Lemma 3.1 (budget identity) — PASS, flag A1

Correct given **A1: at the bottom threshold every non-plateau internal word
position lies in exactly one predecessor gap.** This is the vertex-gap
convention of Theorem 2.1(2.3) of `MULTISCALE_DIRECTION_COUPLING_NEXT.md`
applied at `c -> 1+`, where the active set is all selected plateaux. A1 is
audited there for internal positions; the terminal gap of a linear word is
handled separately, as the resolution does. Endpoint conventions cost
`O(m) = O(a) = o(a^2)`. No gap double-count is possible since gaps are
disjoint in the vertex convention. PASS.

### Lemma 4.1 (transfer identity) — PASS, flag A2

**A2: the middle word visits every point of `H_a` exactly once (Hamilton
path under the audited encoding).** This is the standing universality
convention of the whole program (the middle order enumerates the middle
layer). Given A2, the injection uncovered-point -> gap-position is
immediate: plateau vertices lie on their own selected lines, which are in
`L_a`. The reverse counting defines `gamma_des` as exactly the gap mass at
uncovered points, so the displayed equation is a definition plus an
injection, not two injections; the stated identity `D_a/a^2 = gamma_des`
is exact by A2. The inequality `gamma_des <= delta` then follows from
Lemma 3.1 with the terminal gap discarded (it only weakens the bound in
the safe direction... checked: terminal-gap positions at uncovered points
would enlarge `gamma_des`; but total gap mass including terminal is still
`delta + o(1)` by Lemma 3.1, so the bound stands). PASS.

### Theorem 5.1 (joint charge) — PASS

The wedge chain of `SMALL_DEFICIT_WEDGE_SEAL.md` Sections 2-3 and 5 is
reused verbatim with the single substitution `D_a/a^2 <= gamma_des + o(1)`
(justified by Lemma 4.1) and the single substitution of the gap charge
`3 int z drho <= 3 gamma_int` (justified by Lemma 3.1, since the audited
gap inequality charges only seam gap marks, which are internal). The
affine optimization in `f` is unchanged; substituting
`eps_d = sqrt(6 gamma_des)` and adding `3 gamma_int - not 3 delta` gives
the stated bound. Verified the crossing algebra: branches
`3f - 3 + 2eps_d + 3gamma_int - and 6 - f + eps_d - 2delta + 3gamma_int`
meet at `f_0 = (9 - 2delta - eps_d)/4`, value
`15/4 + (5/4)eps_d - (3/2)delta + 3gamma_int`; with `gamma_int <= delta`
this is `<= 15/4 + (5/4)eps_d + (3/2)delta`. Both displayed forms match.
The moment bound `int_rho (p-1) = 3 - delta - f` uses the FULL deficit
`delta` (not `gamma_int`), which is correct: edge mass is `3 - delta`
regardless of where gaps sit. PASS.

### Corollary 5.2 — PASS

`(5/4)sqrt(6 g) < 1/4 - (3/2)delta` squares to `g < (1-6delta)^2/150`,
requiring `delta < 1/6`. Diagonal check `g = delta`:
`150 delta < (1-6delta)^2` i.e. `36 delta^2 - 162 delta + 1 > 0`, smaller
root `(162 - sqrt(162^2 - 144))/72 = (81 - sqrt(6561-36))/36
= (81 - sqrt(6525))/36`. And `delta_0 = (sqrt29 - 5)^2/24
= (54 - 10 sqrt29)/24 = (27 - 5 sqrt29)/12 = (81 - 15 sqrt29)/36
= (81 - sqrt(225*29))/36 = (81 - sqrt(6525))/36`. Exact match. PASS.

### Lemma 6.1 (level tension) — PASS

First-moment minimization under Lebesgue domination is standard
(bathtub principle); the pair bound: pushing mass to `[1-A_d,1]` and
`[1-A_e,1]` minimizes `intint 1_{t+u<=1}`, and on those intervals the
constraint `t+u<=1` cuts the corner triangle of leg `(A_d+A_e-1)_+`,
area `((A_d+A_e-1)_+)^2/2`. Monotone rearrangement justifies minimality.
The budget line restates (4.5) of `ABSORBED_FLOW_COAREA.md`. PASS.
Remark 6.2 correctly concedes this does not empty the sliver.

### Theorem 7.1 (bottom optimality) — PASS with scope note

Monotonicity of `delta(c)`: deletion only removes edge mass — correct.
Monotonicity of `gamma_des(c)`: deleted plateaux remove lines from `L_a(c)`
and convert their positions to gap positions — both moves enlarge the
desert — correct by contraction Theorem 2.1. The value shift `3c - 3 +
2e(c) >= 0` at fixed sub-four test — correct. SCOPE: this proves only that
*this particular* joint charge is bottom-optimal; it does not exclude
lifetime-weighted use of *other* quantities (the resolution says exactly
this). PASS.

### Section 8 (dual near-extremizer X) — PASS as dual object only

X is a scalar ledger; the audit confirms each claimed tightness/slack row
in the ledger file (L1-L9). X is NOT a marked process and NOT a word;
Outcome B is correctly not claimed. The `z`-placement respecting
`p + s - 1 <= 2` while achieving equality in both C-bounds is consistent
at `f_0` since `A = 2f_0 - 3 + eps` and `C = A + 2(3 - delta - f_0)
= 4f_0 - 6 + 2eps` — the two branches meet at `f_0` by construction. PASS.

### Lemma M and Theorem 9.1 — reduction PASS; Lemma M UNPROVED

The concavity optimization: maximize `(5/4)sqrt(6g) - mu g`; derivative
zero at `sqrt(6g*) = 15/(8 mu) times... ` recheck: d/dg
[(5/4)sqrt(6g)] = (5/8)sqrt(6/g); set `= mu`, so `sqrt(g*) =
(5/8)sqrt(6)/mu`, giving `(5/4)sqrt(6 g*) - mu g* = (5/4)(6)(5/(8mu))
- mu (150/(64 mu^2))... = 75/(16mu) - 75/(32 mu) = 75/(32 mu)`. Matches.
Threshold: `75/(32 mu) < 1/4 - (3/2)delta` iff `mu > 75/(8(1-6delta))`.
Matches. Numerical row: at `delta_1 = 1/24`, bound is `75/(8 * 3/4)
= 12.5` — the resolution's first sentence of item 4 ("mu = 12 suffices")
is WRONG and its own correction ("take mu >= 12.5") is right. MINOR ERRATUM,
non-load-bearing. Theorem 9.1 as stated (hypothesis
`mu >= 75/(8(1-6delta_1))`) is correct. Lemma M itself: **UNPROVED**,
clearly labelled, with the X-witness showing it cannot follow from the six
audited families alone. This satisfies the prompt's minimality and
sharpness requirements.

## Unproved dependencies (complete list)

1. **Lemma M** — the sole missing lemma; explicitly flagged.
2. **A1** (gap partition at bottom threshold) — audited elsewhere
   (`MULTISCALE_DIRECTION_COUPLING_NEXT.md` Thm 2.1); LOW RISK.
3. **A2** (Hamilton-path universality encoding) — program-wide standing
   convention; LOW RISK.
4. Erratum: "mu = 12 suffices for delta_1 = 1/24" should read
   "mu >= 12.5"; the surrounding formula is correct.

## Boundary of the result

Nothing here treats `delta >= 1/6`, cross-threshold weighting of new
quantities, or the marked-process Items 1-4 of
`MULTISCALE_DIRECTION_COUPLING_NEXT.md` Section 7 beyond the bottom
threshold. The closed region is exactly `gamma_des < (1-6delta)^2/150`,
`delta < 1/6`, plus the previously known `delta < delta_0`.
