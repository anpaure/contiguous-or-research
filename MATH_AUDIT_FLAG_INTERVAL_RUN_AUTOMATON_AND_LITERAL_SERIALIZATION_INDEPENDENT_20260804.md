# Independent audit: flag-interval run automata and literal serialization

**Date:** 2026-08-04  
**Method:** independent symbolic proof replay; pure mathematics; no search,
solver, or finite computational census  
**Audited theorem:**
`MATH_THEOREM_FLAG_INTERVAL_RUN_AUTOMATON_AND_LITERAL_SERIALIZATION_20260804.md`  
**Audited theorem SHA-256:**
`34940204b7381eaf11cb8019340059a444abd87a619199e428292b84b1bdcc14`  
**Audited self-audit SHA-256:**
`054438e49dcf7ecc60c31634531f58f473943d998cd43e1c186dd3b0f493da33`  
**Verdict:** **INDEPENDENT-GO at the theorem's stated fixed-factor,
fixed-named-flag, fixed-address scope.**

The equivalence, cyclic reconstruction, right-aligned specialization, and
conditional waste implication are proof-safe.  During the audit one
wording error in the displayed `d=2` counterexample was corrected: at age
`d-1` the increment is forbidden, so the only legal survivor transition is
a reset to zero.  This does not change the counterexample or any theorem.

## 1. Index and convention replay

At the turn

\[
 Q_{i+1}=Q_i-\{\alpha_i\}+\{\beta_i\},
\]

the source letter appended at the new root is indexed `B_(i+1)`.  Thus
`Q_i` is the union of the `d` letters ending at `B_i`, and the crossing
`(d+1)`-window ending at `B_(i+1)` is

\[
 Q_i\cup B_{i+1}=Q_i\cup\{\beta_i\}=Q_i\cup Q_{i+1}=T_{i+1}.
\]

This agrees with every index in (0.1), (0.2), (2.5), and (2.6).  A maximal
positive cyclic run starts at `Q_(i+1)` precisely when its coordinate is
`beta_i`, and ends at `Q_i` precisely when it is `alpha_i`.  Hence its
entry and terminal ages are respectively zero and `d-1`.

The hypothesis that no coordinate occurs at every root is exactly what
lets every positive cyclic run be cut at a genuine entry and departure.
There is no omitted seam condition.  In particular, if the automata accept,
every run has at least `d` vertices.  Therefore an accepted nontrivial
instance automatically has cycle length greater than `d`: when `N<=d`, a
non-ubiquitous run has length at most `N-1<d`.  The cyclic `d`-window
interpretation consequently has no repeated-position pathology.

## 2. Flag addresses are exactly age intervals

Let `x` first enter the strict flag at block `j`.  The equalities

\[
 F^i_{\theta^i_h}=S^i_h
\]

say that `x` is absent at the preceding declared threshold and present at
the current one.  Since `F_t` is the set of coordinates of age at most
`t`, this is exactly

\[
 \theta^i_{j-1}<a_i(x)\le \theta^i_j,
 \qquad \theta^i_0=-1.
\]

Thus (0.5) is necessary.  Conversely, assigning every coordinate in
`S^i_j-S^i_(j-1)` an age in that interval makes membership at every
declared threshold exactly `S^i_h`; there is no missing condition at an
undeclared threshold.  The intervals partition `{0,...,d-1}` because the
addresses are strict and the last address is `d-1`.

Two useful endpoint consequences are also exact.  Age zero lies only in
the first block, so an accepted entering coordinate lies in `S^i_1`.
Age `d-1` lies only in the final block, so an accepted departing coordinate
lies in `Q_i-S^i_(m_i-1)` when the flag has more than one member.

## 3. Run recurrence and its iff direction

For a present coordinate, one step has only two possibilities:

* it occurs in the newly appended letter and resets to age zero; or
* it does not occur there and increments from `a` to `a+1`, which is legal
  only for `a<d-1`.

The complete forward image of a reachable set is therefore

\[
 \{0\}\cup\{a+1:a\in\mathcal R_t,\ a<d-1\}.
\]

Intersecting this image with the next allowed interval gives exactly
(0.7).  Induction proves that `mathcal R_t` is neither an overapproximation
nor an underapproximation: it is the full set of reachable ages at time
`t`.  Entry fixes age zero, and departure fixes age `d-1`; hence terminal
membership (0.8) is necessary and sufficient.  Backtracking any terminal
`d-1` chooses one legal predecessor at each earlier state.

With no marked restrictions, a path from zero to `d-1` needs at least
`d-1` transitions and exists on every run of at least `d` vertices.  This
confirms the claimed recovery of the minimum-run criterion, including the
`d=1` case.

## 4. Reconstruction and cyclic closure

Choose one accepting path independently on each positive run of each
coordinate.  These variables are genuinely disjoint.  At root `i`, their
ages partition `Q_i` into `C^i_0,...,C^i_(d-1)`.  Define

\[
 B_{i+1}=\{\beta_i\}\cup
 \{x\in Q_i\cap Q_{i+1}:a_{i+1}(x)=0\}.
\]

The two parts are disjoint because `beta_i` is not in `Q_i`, and the letter
is nonempty.  Every survivor with positive next age has unique previous
age one lower.  Every survivor with next age zero is in `B_(i+1)`.  The
departing coordinate has age `d-1`, while the entering coordinate is the
new age-zero element.  Consequently shifting the age partition and
appending `B_(i+1)` gives exactly the declared next partition.

This local statement also verifies the periodic seam.  The age paths were
chosen on maximal *cyclic* runs, so the last transition of the indexed
cycle returns to the initially declared partition.  Equivalently, tracing
an element of age `t` backwards reaches its most recent age-zero occurrence
in `B_(i-t)`, with no newer occurrence; a coordinate absent from `Q_i`
cannot occur in any of those last `d` letters, because legal departure is
possible only from age `d-1`.  Hence the cyclic word formed by the `B_i`
has last-`d` union exactly `Q_i` at every root.

No cross-coordinate compatibility remains: source letters are arbitrary
subsets, so simultaneous resets have no capacity restriction, and the
newborn `beta_i` guarantees nonemptiness.  This validates the theorem's
claim that no product automaton or extra age holonomy is required after
the factor, flags, and addresses are fixed.

## 5. Right-aligned specialization

For `theta_j=d-m+j-1` and `c=d-m`, the first block has interval

\[
 [-1+1,\theta_1]=[0,c],
\]

whereas for `j>=2`,

\[
 [\theta_{j-1}+1,\theta_j]=\{c+j-1\}.
\]

Thus (0.10) is exact.  A nonminimal block at the next root can only inherit
from the immediately preceding forced age; it cannot reset because its
allowed age is positive.  The bottom block remains flexible only inside
`[0,c]` and is still constrained by the same run recurrence.  The
corollary does not overstate that flexibility.

## 6. Counterexample and the corrected wording

At depth two, the flags

\[
 \{1\}\subset\{1,2,4\},\qquad
 \{3\}\subset\{1,3,4\}
\]

force coordinate `4` to age one on both sides of the turn.  Since one is
already the terminal allowed age, a surviving `4` must reset to zero; it
cannot increment to two.  Hence it cannot have required next age one.
The departure and birth endpoint tests nevertheless pass.  This proves
the advertised strict separation between endpoint apertures and the full
run automaton.  The theorem and self-audit now use this exact wording.

## 7. Conditional waste transfer

Theorem 4.1 explicitly assumes that the cyclic spelling is opened and
collared while retaining at least `Lambda-C` pairwise target-distinct
marked occurrences.  It does not infer this preservation from run
acceptance.  Under the separately stated residence, halo, `W>2d`, and
`r>=2d` hypotheses, the mandatory-collar theorem gives `R_A=0`.

The short-cell multiset has cardinality `Lambda+sigma`.  With no rank-`r`
leakage, its support is the union of the right-endpoint short chains, and
the exact collision identity gives

\[
 D_A=(\Lambda+\sigma)-
       \left|\bigcup_j\mathcal K_j\right|.
\]

Every retained marked occurrence is a member of that union, and target
disjointness makes these `Lambda-C` distinct support values.  Therefore

\[
 D_A\le(\Lambda+\sigma)-(\Lambda-C)=\sigma+C.
\]

This implication is exact.  The zero-local-plateau theorem supplies the
chain interpretation, although the same numerical equality also follows
directly from the lower-deck waste identity once `R_A=0`.

## 8. Scope boundary

The audited theorem proves only the fixed-data serialization equivalence
and the explicitly conditional waste transfer.  It does not prove:

* an atomic-to-named flag lift;
* a joint choice of factor, flags, and addresses accepted by all run
  automata;
* connectedness or component fusion;
* arbitrary-width upper completeness;
* a safe opening retaining `Lambda-O(1)` distinct marks; or
* `nu(k)<=B(k)+O(1)`.

Subject to those stated exclusions, the theorem is independently
proof-safe.
