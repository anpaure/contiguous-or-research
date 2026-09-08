# Exact contiguous-OR frontier after the k=11 solution

Date: 2026-07-27

## 1. Settled results

Let

\[
r=\lceil k/2\rceil,
\qquad
W(k)=\binom kr,
\]

and let `d(k)` be the least integer satisfying

\[
dW(k)+\binom{d+1}{2}
\ge
\sum_{j=1}^{r-1}\binom kj.
\]

Put `B(k)=W(k)+d(k)`.

The monotone-deadline argument proves unconditionally that

\[
\nu(k)\ge B(k)
\]

for every `k`.  Exact universal words now prove

\[
\boxed{\nu(k)=B(k)\quad\text{for every }k\le12.}
\]

The formerly missing case is

\[
\boxed{\nu(11)=465}.
\]

Its two independently verified optimal words, verifier, and reproduction
commands are recorded in `K11_EXACT_465_SEARCH_CERTIFICATE_20260727.md`.

## 2. What the new optimum proves structurally

The `k=11` construction is not an unstructured SAT string.  Its third Boolean
derivative is a translation-equivariant Hamilton cycle through all 462
six-sets.  A 42-step rotor of voltage two generates the whole cycle.  Every
lower and upper sliding shadow is complete at every depth, and every
coordinate residence run has length at least four.

After one safe cut, the nested boundary flag is

\[
155\supset154\supset152.
\]

The first certificate uses a pin-compatible sandwich Hall matching of size
231.  A later, cleaner compiler needs only a coordinatewise run-alternating
core `C` with `DC=DP`, followed by one capacitated surplus-Hall matching.
It gives the tableau

| row | length | rank profile |
|---|---:|---|
| `D^0` | 465 | `1^11,2^57,3^397` |
| `D^1` | 464 | `4^464` |
| `D^2` | 463 | `5^463` |
| `D^3` | 462 | `6^462` |

The cleaner word is `scratch/sigma_calibration_bulk_k11_465.word`, with
SHA-256

```text
bda651d3e40d0920d3e6ed12e6a2091e477695d8ad7f6bd186b831f087cf136a
```

The common pattern across the known rank-exact optima is therefore

\[
\boxed{
\text{perfect upper shadow tower}
+
\text{lower defects contained in one boundary flag}.}
\]

## 3. Exact finite compiler and its asymptotic scope

`MATH_BULK_PCSH_COMPILER_20260727.md` proves the following sharper form for
the literal-base-row normal form used at `k=11`.

Let `P` be the depth-`d` cyclic erosion of a rank-`r` chronology and construct
the canonical run-alternating coordinate core `C subseteq P`.  Then

\[
DC=DP.
\]

Consequently every intermediate word `C subseteq A subseteq P` satisfies

\[
D^tA=D^tP\qquad(t\ge1).
\]

Thus all intermediate derivative pins disappear.  The literal low targets
can be inserted if and only if the following exact capacitated Hall system
holds.  Put `s=r-d`, `R_Q={j:P_j=Q}`, and `mu(Q)=|R_Q|`.  For every family
`A` of targets of ranks strictly below `s`,

\[
|A|\le
\sum_{Q\in\binom{[k]}s}
\min\{\mu(Q)-1,\ |N(A)\cap R_Q|\}.
\]

One position in each `R_Q` is reserved for the literal rank-`s` target.
Translation symmetry and submodular uncrossing reduce any bulk failure to an
orbit-union witness.  At `k=11` there are only 63 nonempty quotient
inequalities; their minimum margin is two.

Hence an exact universal word follows in this normal form when a chronology
has:

1. every middle set exactly once;
2. residence through delay `d` and all required cyclic derivative shadows;
3. the surplus-Hall inequalities above; and
4. an exterior-safe cut that preserves the upper shadows on linearization.

Then it compiles to a universal word of length `W+d`.  Combined with the
lower bound, this proves `nu(k)=B(k)`.

The boundary is genuine.  A complete-shadow, resident, cap-two `k=7` cycle
has cyclic PCSH failure, while 24 of its 28 exterior-safe cuts succeed.
Across 121 bounded samples every cycle had at least 15 successful cuts, but
this is evidence rather than a theorem.

There is an essential scope correction.  This compiler puts every mask of
rank at most `s=r-d` literally in `D^0`.  Already at `k=9` that requests 129
different masks in a word of length 128, and asymptotically it requests
`Theta(sqrt(k) W)` masks in only `(1+o(1))W` positions.  Thus it is a strong
finite/special-regime compiler, not the uniform exact reduction.  The
correct general compiler distributes all lower masks across the first `d`
derivative rows according to the rank-quantile polytope and uses the exact
full interval-label realization criterion.  See
`MATH_BULK_COMPILER_SCOPE_AND_MULTIROW_FRONTIER_20260727.md`.

The uniform replacement is now proved as a reduction in
`MATH_DEPTH_D_SANDWICH_MULTIROW_COMPILER_20260727.md`.  A sparse core `C`
can be chosen with

\[
D^dC=D^dP.
\]

Therefore every `C subseteq A subseteq P` preserves the middle row and the
entire upper tower while leaving all `d` lower rows free.  On `k=11` the
resulting multirow compiler has only 3,784 variables and 11,913 clauses,
solves in 0.004 seconds, and yields a third exact 465-word.  The remaining
uniform question is lower-band coverage inside this depth-`d` sandwich, not
preservation of the rotor.

## 4. The global construction target

For odd prime `k=2m+1`, translation reduces the middle layer to the Catalan
number `C_m` of necklace orbits.  The supported general target is a
**universal-shadow Catalan rotor**:

- one quotient Hamilton cycle through all middle necklaces;
- nonzero voltage, so its lift is one full middle cycle;
- deadline residence;
- every lower and upper sliding-shadow orbit covered; and
- an exterior-safe cut satisfying PCSH.

This is stated precisely in
`MATH_UNIVERSAL_SHADOW_CATALAN_ROTOR_TARGET_20260727.md`.

The local selector in the `k=11` solution is intentionally generic: it has no
nontrivial affine symmetry, no natural polynomial rule of degree at most
three, and no short linear recurrence.  The reusable structure is global,
not pointwise.

## 5. Next finite test: k=13

Here

\[
W=\binom{13}{7}=1716,
\qquad d=3,
\qquad B(13)=1719.
\]

The quotient has 132 lower orbits and 21 choices per orbit.

Verified progress:

1. a cap-two connected quotient cycle covering both q2 sides exists;
2. its voltage is 11, so the lift is one 1716-cycle;
3. every upper shadow through the top is complete;
4. a local-neighbourhood repair gives a connected h2-resident cycle while
   preserving both q2 sides.

For the first h2-clean certificate, the exact remaining quotient defects are:

- 34 delay-three residence orbits;
- five missing lower-q3 orbits;
- one missing upper-q3 orbit; and
- one missing lower-q4 orbit.

All q1/q2 resources and all deeper layers are complete.  Thus the next case
has not been solved, but it has reached a small, explicit global residual.

A later affine-seed break improves this frontier.  Exact affine symmetry is
incapable of producing one Hamilton cycle, but freeing 60 of its 132
translation choices gives a connected q1 cycle of voltage six in 0.62
seconds.  A 90-free staged solve then gives both q2 sides and h2 residence,
with the sharper residual

- 27 delay-three residence orbits;
- five missing lower-q3 orbits; and
- no missing upper-q3 orbit.

The exact recent-insertion and recent-deletion automata now encode both q3
sides without enumerating four-edge paths.  The corrected full joint formula
has 211,755 variables and 1,923,877 clauses with unary-MTZ connectivity; an
oriented-lazy version has 194,463 variables and 1,181,772 clauses, leaving
connectedness to exact subtour cuts.  Bounded portfolios are live.  Their
timeouts, if any, remain timing evidence only.

Bounded h3-centred searches did not close that residual.  A 90-free-choice
neighbourhood became UNSAT only within that fixed neighbourhood; 120-free
runs returned UNKNOWN; and a five-round 110-free LNS portfolio ended with
312--442 physical h3 violations or a zero-voltage cycle.  None of these is a
global SAT or UNSAT conclusion.

The corrected oriented-lazy portfolio has now passed the connectivity gate.
An independently audited certificate gives one quotient 132-cycle of voltage
eight, hence one physical 1,716-cycle, with every lower and upper shadow
complete through all remaining ranks.  It initially had 19 quotient
depth-three residence defects.  Exact LNS descent reduced this successively
to 16 and then 14 quotient defects while preserving the one-cycle and all
shadow conditions.  Thus the live `k=13` gate is no longer connectivity or
coverage: it is the explicit descent from 14 residence defects to zero,
followed by the depth-three compiler.

## 5a. New certified `k=14` upper bound

The linear depth-two compiler now accepts nonlocal changes to the 3,432-set
middle path.  Compiler-in-the-loop 2-opt descent reduced the missing masks of
an equality-length 3,434-entry prefix from 260 to 251, while preserving exact
second derivative, every middle set, and complete coverage through rank
eight.  Compiler-safe block transpositions reduce the prefix residual to 249
masks, and iterative exact delete-one/edit-one suffix repairs give a
rigorously verified 3,668-entry universal word.  Hence

\[
                         \boxed{3434\le\nu(14)\le3668}.
\]

The word, its SHA-256, and an exhaustive independent verifier are recorded in
`K14_UPPER_3668_CERTIFICATE_20260727.md`.

## 6. Two exact gates—not sixteen vague ones

The 16-lane ledger remains useful for provenance, but the mathematical core
has condensed to two statements:

1. **Rotor/gluing gate:** construct a deadline-resident central chronology
   with the required upper shadows (or a path with one controlled boundary
   defect).
2. **Multirow realization gate:** inject the entire lower ideal into all
   `d` short OR--Pascal rows, with the exact coordinatewise interval-label
   realization condition.  Rank counts reduce to the known quantile
   polytope; physical overlap is the open part.

The boundary surplus-Hall theorem is the exact form of gate 2 for `k=11`
and remains a useful terminal module, but it does not cover the asymptotic
multirow regime.  Proving the two gates above uniformly would yield the
exact formula and therefore the asymptotic constant-one theorem immediately.

There is now one rigorous local asymptotic theorem and one equally rigorous
warning.  The six-partite q1/q2 transition catalogue has exact relative
codegree `O(1/r)`, so a standard fixed-uniformity nibble gives
`(1-o(1))W` mutually resource-disjoint local decorated transitions.  But a
statewise pointer defect `Gamma` vanishes exactly when their declared outer
states are the actual predecessor/successor centres.  Random local matchings
at `k=11` have large `Gamma`; the exact rotor has `Gamma=0`.  Thus local
packing is solved, while global chronological gluing is not.  See
`scratch/fast_sigma_transition_design_theorem.md`.

The first coherent-absorption experiment is positive.  Starting from the
canonical complement-invariant PBBS factor at `k=11`, a literal three-orbit
alternating circuit removes its sole q1 cap-three orbit while preserving the
2-factor and both q2 coverages.  A 17-orbit circuit then gives one quotient
42-cycle of voltage two, a physical 462-cycle, cap-two q1, complete shadows
at every audited depth, and zero depth-three residence defects.  Both the
selected-pin and depth-`d` multirow compilers turn this independently
constructed rotor into exact 465-words.  Thus `Gamma=0` is reachable by
cycle-space trades; no statewise gluing obstruction survives at `k=11`.
See `scratch/pbbs_orbit_trade_report.md`.

The same PBBS census at `k=15` is the strongest larger finite seed currently
known.  It starts with all lower and upper shadows at every depth, 73
components, five q1 load-three translation orbits, and 90 depth-three
residence defects.  Exact zero-boundary arity-three and arity-four trades now
reduce it to 17 physical components and 45 forward residence defects while
retaining zero shadow holes at every depth.  An independent audit certifies
the intermediate 18-component state, and the 17-component state is the
current trade frontier.  The remaining factor defects occur on only two
physical cycles; cutting a minimum of 23 edges hits all of them.  Together
with one cut in every other component this produces a 38-segment exact
splicing problem, now being attacked directly instead of insisting on a
one-cycle 2-factor first.
Two of the load-three orbits have size five and are forced by full
`Z_15`-equivariance, so cap two must not be imposed as a false requirement.
The static lower gate is independently solved: three containment matchings
pack all 16,383 lower masks into 6,435 rank-eight anchored chains of depth at
most three, with exactly the scalar slack 2,928.  See
`MATH_STATIC_CHAIN_ANCHOR_GATE_20260727.md`.

There is also a precise limitation on using an odd solution to obtain the
next even one.  A shared-tail lift has the optimal length when the two depths
agree, but it requires a dual erosion: both coordinate runs and coordinate
gaps in the central chronology must have length at least `d+1`, followed by
an exact marked seam-cover condition.  The known `k=11` rotors have minimum
gap one, and exhaustive relabel/reversal seam searches do not recover the
`k=12` word.  Thus `15 -> 16`, `17 -> 18`, and `19 -> 20` remain valid
conditional architectures, not automatic corollaries.  See
`MATH_ODD_EVEN_SHARED_TAIL_LIFT_20260727.md`.

## 7. Honest status

The general identity `nu(k)=B(k)` remains open.  The new work proves a finite
case, an exact compiler theorem, a symmetry-reduced Hall lemma, and a sharply
finite next instance.  It does not justify extrapolating the `k=11` SAT model
to all dimensions without a global construction argument.
