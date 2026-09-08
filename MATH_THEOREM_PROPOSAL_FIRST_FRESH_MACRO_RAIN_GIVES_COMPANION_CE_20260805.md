# Proposal-first fresh-macro rain gives the exact companion cylinder

**Date:** 2026-08-05  
**Method:** fractional-orbit cluster codegrees, independent macro rain, and
monotone alteration; no computation or search  
**Status:** unconditional probability theorem, followed by a sharp coverage
barrier.  A unit-intensity proposal-first selector inherits the desired
companion cylinder under arbitrary deletion, and uniform pre-reserved banks
also act only by deletion.  However an independent unit-intensity rain
leaves a constant fraction of lower resources unproposed.  Raising its
intensity enough to reach the separator scale loses a factor `Theta(log d)`
in the cylinder.  Thus the simple rain is not the missing near-perfect
integral selector.  The theorem precisely reduces that selector to a
spread dependent rounding (or an acceptance-aware nibble); it must not be
cited as an unconditional macro packing.

## 1. The projected marked macro orbit

Put

\[
 t=r-d,
 \qquad M={k\choose t},
 \qquad W={k\choose r}.
\]

Let

\[
 \mathcal S=\{(T,b):T\in{[k]\choose r},\ b\in T\}
\tag{1.1}
\]

be the set of marked level-two owner occurrences.  Thus
`|mathcal S|=Wr`.

For `h in {2,3}`, project a labelled fresh `h`-fold macro from Theorem 3.2
of
`MATH_THEOREM_FRESH_FIFO_BLOCK_CHAIN_KERNEL_AND_PAYLOAD_ATLAS_GATE_20260805.md`
to its `h` marked level-two occurrences

\[
 \Sigma(E)=\{(T_2^c,b_2):1\le c\le h\}\subseteq\mathcal S.
\tag{1.2}
\]

Keep multiplicities: two full labelled macros with the same projection are
still two proposal atoms.  Give the complete `h`-orbit the uniform weight

\[
 \omega_h(E)=\lambda_h{M\over d|\mathcal P_h|},
\tag{1.3}
\]

where

\[
 \lambda_3={\rho d\over d+1}-2,
 \qquad
 \lambda_2=3-{\rho d\over d+1},
 \qquad
 \rho={W\over M}.
\tag{1.4}
\]

For all sufficiently large central parameters these weights are
nonnegative and `lambda_2+lambda_3=1`.  They are the exact fractional
`2/3` factor weights.

For a finite set `A subseteq mathcal S`, define its same-macro weighted
codegree

\[
 \Omega(A)=\sum_{h=2}^3\ \sum_{E\in\mathcal P_h:\ A\subseteq\Sigma(E)}
                         \omega_h(E).
\tag{1.5}
\]

## 2. Exact one-point intensity

### Lemma 2.1

Every marked occurrence `s in mathcal S` has the same weighted degree, and

\[
 \boxed{
 \Omega(\{s\})={1\over r(d+1)}.}
\tag{2.1}
\]

Equivalently, at the integral copy count
`H=W/(d+1)` the value in (2.1) is exactly `H/(Wr)`; using the floor in the
finite scalar ledger changes it by `o(H/(Wr))`.

#### Proof

Coordinate relabelling and the displayed order choices act transitively on
`mathcal S`, so the weighted degree is constant.  The total weight of the
`h`-orbit is `lambda_h M/d`, and every macro contributes `h` marked
level-two occurrences.  Hence the common degree is

\[
 {M\over dWr}(2\lambda_2+3\lambda_3).
\tag{2.2}
\]

Equation (1.4) gives

\[
 2\lambda_2+3\lambda_3={\rho d\over d+1}
                       ={Wd\over M(d+1)}.
\tag{2.3}
\]

Substitution in (2.2) proves (2.1).  \(\square\)

Write

\[
                         \eta_*={1\over r(d+1)}.
\tag{2.4}
\]

## 3. The complete orbit already has the required cluster codegrees

Put `ell=d-2`.  In a marked level-two copy one has

\[
                         T_2=P\mathbin{\dot\cup}X^+,
 \qquad |P|=r-d+2,
 \qquad |X^+|=\ell,
 \qquad b_2\in P.
\tag{3.1}
\]

For two copies of one macro, the private tails are disjoint.  Define

\[
 N_*={k-r-(h_0-2)\ell\choose\ell},
 \qquad h_0=3,
 \qquad
 \kappa_*={2\over N_*}.
\tag{3.2}
\]

In the central regime,

\[
                         \log N_*=\Theta(d\log d),
 \qquad
                         \kappa_*=\exp[-\Theta(d\log d)].
\tag{3.3}
\]

### Lemma 3.1 (weighted cluster codegree)

For every set `A` of `b` distinct marked occurrences, where
`1<=b<=3`,

\[
 \boxed{
                         \Omega(A)
              \le \eta_*\kappa_*^{,b-1}.}
\tag{3.4}
\]

The left side is zero unless the occurrences have one common mark, one
common rank-`r-d+2` kernel, and pairwise disjoint private tails.

#### Proof

The case `b=1` is Lemma 2.1.  Fix one occurrence `s in A` and sample a
macro through `s` with probability proportional to its orbit weight.

To install the first prescribed companion, the macro must choose the
unique compatible common kernel and the prescribed private tail.  Before
the kernel is fixed there are

\[
 {r-1\choose\ell}{k-r\choose\ell}
\tag{3.5}
\]

prospective choices.  In particular, the probability of the prescribed
companion in any one of the at most two companion roles is at most
`2/N_*`.

After one companion is fixed, every further companion has at least `N_*`
fresh tail choices, and there is at most one remaining role.  Thus each
additional prescribed occurrence costs another factor at most `2/N_*`.
All choices of the lower path, invisible orders, terminal labels, and
payload data occur with the same multiplicity on the numerator and
denominator and cancel.  Therefore, in each `h`-orbit,

\[
 {\deg_h(A)\over\deg_h(s)}
                         \le\kappa_*^{b-1}.
\tag{3.6}
\]

Multiply by the weighted one-point degree in that orbit, sum over
`h=2,3`, and use Lemma 2.1.  \(\square\)

This is the crucial distinction between a selected-factor cylinder and a
proposal-orbit cylinder: (3.4) is a direct finite count in the complete
orbit and needs no matching theorem.

## 4. Independent macro rain

Let `mathcal I` be any finite or countable set of proposal rounds.  In
round `i`, independently mark every labelled macro `E` with probability

\[
                         p_i(E)=\tau_i\omega_h(E),
 \qquad E\in\mathcal P_h,
\tag{4.1}
\]

where `0<=p_i(E)<=1` and

\[
                         \sum_{i\in\mathcal I}\tau_i\le1.
\tag{4.2}
\]

It is harmless to omit any proposal before drawing it.  In particular, we
may omit every macro whose marked level-two owner lies in either
pre-reserved bank `B_0,B_1`, every macro meeting an already used owner, and
every macro forbidden by the current suffix or hull state.  Omission only
decreases all sums below.

After all proposals have been exposed, apply an arbitrary, possibly random
and history-dependent **monotone alteration**: retain some proposed macros
and delete all others.  The alteration may enforce lower-vertex
disjointness, owner disjointness at every level, terminal Hall, hull caps,
component connectivity, residence guards, and typed compiler guards.  It
may not create an unproposed macro.

Let `mathcal F` be the retained integral macro family.  For prescribed
distinct occurrences `s_1,...,s_m`, let `Pi_mathcal F` be their partition
by membership in the same retained macro; the event is false if some
occurrence is not retained.

### Theorem 4.1 (proposal-first companion cylinder)

For every partition `pi` of `[m]` into blocks of size at most three,

\[
 \boxed{
 \Pr\bigl(\Pi_{\mathcal F}=\pi\mid B_0,B_1\bigr)
       \le \eta_*^{|\pi|}\kappa_*^{,m-|\pi|}.}
\tag{4.3}
\]

The same conclusion holds if the proposal probabilities are exposed
adaptively, provided that conditional on the past their total remaining
cluster intensities satisfy the analogues of (3.4) with numbers
`eta_i` whose sum is at most `eta_*`.

#### Proof

For each block `A` of `pi`, exact membership in one retained macro implies
that at least one proposal `(i,E)` satisfies

\[
                         \{s_a:a\in A\}\subseteq\Sigma(E).
\tag{4.4}
\]

Different blocks require different retained macros.  Forget exactness,
forget all conflicts, and take a union bound over one distinct proposal
for each block.  Independent proposal indicators give an upper bound which
factorizes over the blocks:

\[
 \prod_{A\in\pi}
 \left(
   \sum_i\sum_{E:\{s_a:a\in A\}\subseteq\Sigma(E)}p_i(E)
 \right).
\tag{4.5}
\]

By (4.1)--(4.2) and Lemma 3.1, the factor for a block of size `|A|` is at
most

\[
                         \eta_*\kappa_*^{|A|-1}.
\tag{4.6}
\]

Multiplying (4.6) over the blocks gives (4.3), since

\[
 \sum_{A\in\pi}(|A|-1)=m-|\pi|.
\tag{4.7}
\]

The actual retained event is a subevent of the proposal event, so the
alteration cannot increase its probability.

For adaptive rounds, expose the rounds chronologically and assign every
block to the round of its retained macro.  The conditional version of
(4.6) applies at every exposure.  Summing over the round assignment of
each block replaces its `eta_i` by `sum_i eta_i<=eta_*`; the same product
then proves (4.3).  \(\square\)

Thus `(CE)` is inherited automatically from a **unit-total-intensity**
proposal-first alteration.  Section 7 explains why this qualifier is
binding for a near-perfect packing.

## 5. Shared marks now give `(C2)`

After `mathcal F` is fixed, choose independently for each retained macro
one common first mark, uniformly from its persistent-kernel aperture of
size

\[
                         a=r-d+1.
\tag{5.1}
\]

All two or three copies in that macro use the same mark, exactly as the
literal duplicate lift requires.

Theorem 1.1 of
`MATH_THEOREM_SHARED_MARK_MACRO_COMPANION_SPREAD_CYLINDER_20260805.md`,
applied with (4.3), gives through every order `m<=C d`

\[
 \Pr(\text{prescribed two-mark occurrences})
 \le
 \left({\eta_*\over a}\right)^m
 \sum_{c=0}^{m-1}
       \left({m^2a\kappa_*\over\eta_*}\right)^c.
\tag{5.2}
\]

Here

\[
 {m^2a\kappa_*\over\eta_*}
 =\exp[-\Theta(d\log d)]=o(1),
\tag{5.3}
\]

and

\[
 {\eta_*\over a}
 ={1\over r(d+1)(r-d+1)}
 \le(1+O(d/r)){H\over W(r)_2}.
\tag{5.4}
\]

Consequently the retained marked level-two states satisfy the
bank-conditioned two-mark cylinder `(C2)` with multiplicative error
`1+o(1)`.

## 6. Exact-cleanup interface

The theorem permits arbitrary deletion but not arbitrary addition.  This
gives a sharp rule for the separator-funded cleanup.

### Corollary 6.1 (quarantine the cleanup)

Suppose a proposal-first nibble leaves at most `C H/d` copy tasks and an
exact deterministic completion installs them using macros not drawn from
the rain.  Exclude those tasks from the bottom Haxell instance and charge
them to the pre-existing separator sidecar.  Then all remaining
`H-O(H/d)` tasks retain (4.3) and `(C2)` exactly.

Conversely, inserting an unrestricted deterministic cleanup macro into the
marked population can violate `(CE)` at order two by assigning one fixed
companion to one fixed root.  Thus cleanup quarantine, or drawing cleanup
macros from the same bounded-intensity rain, is logically necessary.

#### Proof

The positive assertion is immediate from Theorem 4.1 because restricting
the marked task set is another monotone deletion.  For the negative
assertion, choose a legal root occurrence and one legal companion in its
fresh orbit, and include that pair deterministically.  Its same-macro
probability is one, whereas `(CE)` asks for at most
`eta_* kappa_*=o(1)`.  \(\square\)

## 7. The unit-intensity coverage barrier

The restriction (4.2) cannot simply be removed.  The exact fractional
factor gives total incident proposal weight one at every lower resource.
Let `v` be such a resource and let `p_E` be the independent proposal
probabilities of the macros through it.  In the complete orbit

\[
                         \max_{E\ni v}p_E=o(1),
 \qquad
                         \sum_{E\ni v}p_E\le1.
\tag{7.1}
\]

Consequently

\[
 \Pr(v\text{ receives no proposal})
   =\prod_{E\ni v}(1-p_E)
   =\exp\!\left(-\sum_{E\ni v}p_E-o(1)\right)
   \ge e^{-1-o(1)}.
\tag{7.2}
\]

No deletion-only alteration can cover an unproposed resource.  Hence a
unit-intensity independent rain leaves a constant expected fraction of the
lower layer, whereas the separator permits only `O(1/d)`.

To make the right side of (7.2) `O(1/d)`, an independent rain needs total
incident intensity at least

\[
                         \log d-O(1).
\tag{7.3}
\]

But the proof of Theorem 4.1 then gives one-point parameter at least
`(log d-O(1))eta_*`, not the required `(1+o(1))eta_*`.  Monotone deletion
alone cannot recover the lost factor in an upper-bound argument.

This is an exact obstruction to the most tempting completion of the
proposal-first idea.  One of the following genuinely stronger inputs is
necessary:

1. a dependent rounding which proposes at least one macro at almost every
   lower resource while retaining the cluster sums (3.4);
2. an acceptance-aware random-greedy proof which recovers the survival
   factor discarded by the monotone union bound; or
3. a regenerative nibble theorem whose **accepted**, rather than proposed,
   cluster intensities sum to at most `eta_*`.

The complete-orbit count (3.4) is the exact local input for each of these
routes, but it is not the global rounding theorem.

## 8. What is closed and what remains

The following conditional row is now closed:

> **Companion spread under unit-budget integral alteration.**  The complete fractional
> `2/3` macro orbit has the exact cluster intensity
> `eta_* kappa_*^(b-1)`.  Independent proposal rain followed by any
> deletion-only integral alteration inherits `(CE)`, even after the bottom
> banks have been pre-reserved.  Shared `b_1` marks then give `(C2)`.

What remains is a correlated rounding statement, not a new local
companion count:

> retain all but `O(H/d)` copy tasks with total **accepted** cluster
> intensity at most `eta_* kappa_*^(b-1)`, while satisfying the lower-block
> cover, every owner SDR, hull energy, and regeneration/topology
> requirements.

The existing spectral fresh-path theorem proves an `O(M/d)` lower leave,
and the level-stratified reduction converts internal owners into ordinary
SDRs, but neither result supplies the spread dependent rounding demanded by
Section 7.  The present theorem supplies its exact local cluster ledger and
rules out the naive independent-rain shortcut.
