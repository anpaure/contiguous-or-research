# Adaptive Johnson Bellman value and the equivariant-hiding obstruction

**Date:** 2026-08-06  
**Method:** Johnson resolvent kernels, orbit-quotient filtrations, and an
exact killed-process Bellman compensator; no computation or search  
**Status:** proof-safe reduction.  The pristine resolvent has a bounded
pointwise kernel, but hiding a global or stabilizer permutation does not
decorrelate an adapted vector from the stopped operator.  The absolute
perturbation rows `(JRES)` and `(JSW)` can be replaced by one strictly
weaker, one-sided Bellman-value bound.  Equivariance and the existing static
trace estimate do not prove that bound; a finite regular counterexample
shows why.  The exact remaining analytic statement is the selected-relation
Bellman domination `(JBEL)` below, on the marked separator-prefix class
actually used downstream.

This note continues
`MATH_THEOREM_JOINT_ROOT_PAIR_LYAPUNOV_AND_MARKED_CLUSTER_NORMALIZATION_20260806.md`.
Its notation, in particular `B_T,L_T,R_T`, `mathscr L_i`, and the stopped
positive Dirichlet payment `mathfrak D_i`, is retained.

## 1. The pristine resolvent is pointwise bounded

Fix a central Johnson layer `Omega_q`, put `N=|Omega_q|`, and use counting
measure.  The pristine resolvent from (5.26) is

\[
 R=\sum_{s\ge1}{\widehat\chi_s\over\vartheta_s}\Pi_s.
 \tag{1.1}
\]

It is positive semidefinite and commutes with the full coordinate action.

### Theorem 1.1 (constant diagonal and kernel bound)

Under `(JT)`,

\[
 \boxed{
 R(x,x)={1\over N}\sum_{s\ge1}m_s
       {\widehat\chi_s\over\vartheta_s}=O(1)
 \quad(x\in\Omega_q).}
 \tag{1.2}
\]

Consequently

\[
 \boxed{|R(x,y)|\le C\quad(x,y\in\Omega_q)}
 \tag{1.3}
\]

and, for every signed vector `z`,

\[
             0\le\langle z,Rz\rangle\le C\|z\|_1^2.
 \tag{1.4}
\]

The same statements hold for each fixed unmarked side/union template after
changing the absolute constant.

#### Proof

Transitivity makes the diagonal constant.  The trace is

\[
 \operatorname {tr}R=\sum_{s\ge1}m_s
       {\widehat\chi_s\over\vartheta_s}.
\]

Equation (5.34) is precisely `tr(R)/N=O(1)`, proving (1.2).  A positive
semidefinite kernel has positive semidefinite two-by-two principal minors,
so

\[
 |R(x,y)|^2\le R(x,x)R(y,y)\le C^2.
\]

This proves (1.3), and summing
`|z_x z_y R(x,y)|` proves (1.4).  The fixed-template conclusion is the
last assertion of Lemma 5.5.  \(\square\)

The very large low-sector eigenvalues of `R` therefore do **not** appear as
large entries.  They can be activated only by a coherent adapted sum over
many resources.  This is the exact reason a trace argument works for a
fresh orbit vector but not automatically for an adapted stopped vector.

There is a sharper identity on one Johnson switch.  It gives a concrete
route for a switching proof of `(JBEL)`.

### Theorem 1.2 (exact resolvent resistance of a Johnson switch)

Let `P` be normalized Johnson adjacency, `L=I-P`, and let `B` be any
positive-semidefinite operator commuting with `L` and the coordinate
action, with `B 1=0` (as for the centered covariance in (5.26)).  Put
`R=L^dagger B` on the mean-zero subspace.  If `x` and `y` are
adjacent Johnson states, then

\[
 \boxed{
 \langle e_x-e_y,R(e_x-e_y)\rangle
       ={2\over N}\operatorname {tr}B=2B(x,x).}
 \tag{1.5}
\]

If `d_J(x,y)=ell`, then

\[
 \boxed{
 \langle e_x-e_y,R(e_x-e_y)\rangle
       \le 2\ell^2 B(x,x).}
 \tag{1.6}
\]

More generally, if a mean-zero signed innovation has an oriented
Johnson-edge flow representation

\[
 z=\sum_{e=(u,v)}theta_e(e_u-e_v),
 \tag{1.7}
\]

then

\[
 \boxed{
 \langle z,Rz\rangle
 \le2B(x,x)\left(\sum_e|theta_e|\right)^2.}
 \tag{1.8}
\]

If the flow uses at most `m` edges, the right side can be replaced by
`2B(x,x)m sum_e theta_e^2`.

#### Proof

The coordinate action is transitive on directed Johnson edges, so the left
side of (1.5) is constant over `x~y`.  Average first over uniform `x` and
then over a uniform neighbour `y`.  The average is

\[
 {2\over N}\operatorname {tr}(R(I-P))
 ={2\over N}\operatorname {tr}(RL)
 ={2\over N}\operatorname {tr}B.
\]

Transitivity also gives `B(x,x)=tr(B)/N`.  This proves (1.5).  Join states
at distance `ell` by a Johnson geodesic and apply the triangle inequality
to the Hilbert vectors `R^(1/2)e_x`; squaring gives (1.6).  Apply the same
triangle inequality to (1.7), use (1.5), and then Cauchy--Schwarz for the
last assertion.  \(\square\)

Thus the resolvent penalty `1/vartheta_s` disappears completely on an
explicit adjacent-switch flow: `RL=B` pays it exactly.  A host-specific
proof of `(JBEL)` may therefore replace an operator comparison by the
following literal task:

> represent every centered adaptive collision innovation, after the
> already priced first-two-hit terms are removed, as a Johnson-switch flow
> whose expected `l1` flow energy is charged by `(ROc)`/`(FE3)` and the
> selected-relation future potential.

This switching-flow assertion is not proved here.  Equations (1.5)--(1.8)
show exactly which quantity it must bound, without a slow-sector loss.

The coherent-edge loss in (1.8) also disappears after the **correct**
uniform coordinate switching.  This is the exact switching identity needed
by a first-differing-label exposure.

### Theorem 1.3 (uniform transposition cancels the resolvent)

Let `tau` be a uniformly random transposition of two distinct coordinates
of `[k]`, acting on `Omega_q`.  Put

\[
                 alpha_q={2q(k-q)\over k(k-1)}.
 \tag{1.9}
\]

For every mean-zero vector `z`,

\[
 \boxed{
 \mathbb E_tau
 \langle (I-tau)z,R(I-tau)z\rangle
       =2alpha_q\langle z,Bz\rangle.}
 \tag{1.10}
\]

#### Proof

Let `Q=E_tau tau`.  A random coordinate transposition changes a fixed
`q`-set with probability `alpha_q`; conditioned on changing it, the result
is a uniform Johnson neighbour.  Hence

\[
                         I-Q=alpha_q(I-P)=alpha_qL.
 \tag{1.11}
\]

Every transposition is a self-adjoint involution and `R` commutes with it.
Therefore

\[
\begin{aligned}
 \mathbb E_tau\langle(I-tau)z,R(I-tau)z\rangle
 &=2\langle z,R(I-Q)z\rangle\\
 &=2alpha_q\langle z,RLz\rangle
 =2alpha_q\langle z,Bz\rangle.
\end{aligned}
\]

This proves (1.10).  \(\square\)

For a complete atomic-doublet orbit, replacing one exposed insertion,
deletion, or header label by a fresh label is literally such a coordinate
transposition.  On every resource word, `I-tau` pairs each affected state
`S` with the adjacent state `tau S`; states containing both or neither
label cancel.  Thus the pristine first-differing-label martingale has
exactly the right resolvent trace, with no `Theta(d)` sector loss.

The adaptive residue is now especially narrow.  At a stopped state the
available candidate labels are not a complete uniform transposition orbit.
One must prove that the missing/bias part of the first-differing-label
average is charged by the first prior edge which broke the switch.  Such a
broken switch consists of the current candidate, its switched mate, and a
prior selected edge meeting exactly one of them; after a second break it is
the `(FE3)` first-two-hit geometry.  This statement is the literal
host-specific switching form of `(JBEL)`; (1.10) proves its unbroken part
exactly.

The required boundary has an exact pathwise partition.

### Theorem 1.4 (earliest-blocker boundary decomposition)

Let `G_1,...,G_i` be the already selected resource-disjoint doublets and
let

\[
 A_i=\{E:E\cap G_j=\varnothing\text{ for }1\le j\le i\}
 \tag{1.12}
\]

be the current available candidate set.  For a coordinate transposition
`tau`, orient its boundary by

\[
 \partial_tau^+A_i=\{E\in A_i:tau E\notin A_i\}.
 \tag{1.13}
\]

Then

\[
 \boxed{
 \partial_tau^+A_i=
 \mathbin{\dot\bigcup}_{j=1}^i
 \left\{E:
 \begin{array}{l}
 E\cap G_l=\varnothing\quad(1\le l\le i),\\
 tau E\cap G_l=\varnothing\quad(1\le l<j),\\
 tau E\cap G_j\ne\varnothing
 \end{array}\right\}.}
 \tag{1.14}
\]

For every term in the `j`-th class,

\[
 (tau E\cap G_j)\subseteq(tau E-E)\cap G_j.
 \tag{1.15}
\]

Every **non-slot** resource `x in tau E-E` has the form `x=tau y`, where
`y in E-tau E` and `x,y` are adjacent in their Johnson layer.  In one
atomic doublet there are at most `N_h=O(d)` such changed non-slot resource
occurrences.  A boundary whose first blocker meets only a changed slot is
kept in the separate slot-error ledger; it is not represented as a Johnson
edge.

#### Proof

If `E` belongs to the oriented boundary, `tau E` meets at least one selected
edge.  Let `j` be its first such edge.  This gives a unique class on the
right of (1.14); conversely every member of a displayed class is available
while its switch is not.  The union is therefore disjoint and exact.
Because `E` is disjoint from `G_j`, any member of `tau E cap G_j` is absent
from `E`, proving (1.15).  A coordinate transposition fixes a subset
containing both exchanged labels or neither and replaces exactly one label
when the subset contains just one.  The changed pair is consequently one
Johnson edge on every non-slot shore.  Finally an atomic `h`-doublet has
exactly `N_h` non-slot resource occurrences, so no more can change.  Slots
transform in their own coordinate-copy shore and are covered only by the
set-theoretic partition (1.14).  \(\square\)

Equation (1.14) is a coarea formula for the stopped candidate orbit.  It
has two useful consequences.

* The internal transposition edges of `A_i` retain the exact cancellation
  (1.10).
* Every missing transposition edge has a unique first selected blocker and,
  outside the separately priced slot face, a first changed Johnson
  resource.  If the blocker meets two changed resources,
  or a second earlier relation is needed to distinguish two boundary
  terms, the datum is precisely a first-two-hit triple.

Thus no maximum over missing labels is necessary.  The remaining estimate
is an **average earliest-blocker boundary energy**.  With the coefficients
of the actual future relation potential inserted, its diagonal
one-resource part is the rooted-overlap injection `(ROc)`; its two-resource
and two-blocker parts have the `(FE3)` incidence pattern.  Identifying the
coefficients is not automatic: one still has to prove that the
future-fugacity weights (or their cylinder-weighted versions) dominate the
true earliest-blocker law at scale `M/d^4`.  This coefficient comparison,
not the combinatorial boundary partition, is the unresolved part.

The coordinate-switch aperture of one blocker is already at the correct
scale.

### Lemma 1.5 (one-blocker switch aperture)

Let `E,G` be resource-disjoint atomic doublets and let `tau` be a uniform
coordinate transposition.  For the event that `tau E` meets `G` on a
non-slot resource, one has

\[
 \boxed{
 \Pr_tau(tau E\cap G\ne\varnothing)
 \le {R_E R_G\over {k\choose2}}
 =O(d^2/k^2)=O(d^{-2}).}
 \tag{1.16}
\]

Only non-slot resource occurrences are counted in `R_E,R_G`; replacing
them by `N_h=O(d)` only weakens the bound.  Changed-slot collisions retain
the already proved slot estimate and are excluded from (1.16).

#### Proof

If a non-slot `x in tau E cap G`, then `x=tau y` for some resource `y in E`.  Since
`E cap G` is empty, `x ne y`; hence `x,y` lie in the same Boolean rank and
are Johnson-adjacent.  Their symmetric difference is the unique coordinate
pair transposed by `tau`.  Charge `tau` to one such ordered resource pair
`(y,x)`.  There are at most `R_E R_G` pairs, while there are `{k choose2}`
uniform transpositions.  Use `R_E,R_G=O(d)` and `k=Theta(d^2)`.  \(\square\)

This is stronger than the raw residual pair scale needed for a single
broken switch.  It does not by itself sum over all prior blockers; that sum
must retain the earliest-blocker/future-survival weight in (1.14).  A
second collision under the same transposition also cannot be treated as
the square of (1.16), because the two resource pairs determine the same
coordinate transposition.  That correlated case is exactly why the
existing `(FE3)` enumeration, rather than an independence assertion, is
still required.

The monotonicity of the available host removes another apparent time loss.

### Lemma 1.6 (a switch boundary is born only once)

For an unordered switch pair `{E,tau E}`, put

\[
 b_i(E,tau)=
 |{\bf1}_{\{E\in A_i\}}-{\bf1}_{\{tau E\in A_i\}}|.
 \tag{1.17}
\]

Then, pathwise,

\[
 \boxed{
 \sum_i[b_{i+1}(E,tau)-b_i(E,tau)]_+\le1.}
 \tag{1.18}
\]

Consequently the positive variation of the unweighted transposition
boundary, summed over all switch pairs, is at most the complete pristine
switching volume.

#### Proof

Availability is monotone.  The two membership bits can only follow

\[
 (1,1)\longrightarrow(1,0)\text{ or }(0,1)
       \longrightarrow(0,0),
\]

with either arrow possibly omitted.  Thus `b_i` follows a subsequence of
`0,1,0` and has at most one positive jump.  Sum over switch pairs for the
last assertion.  \(\square\)

This is the precise advantage of the signed Bellman/Doob formulation over
absolute `(JRES)`: it charges creation of a stopped switch boundary, not
its occupancy at every later time.  For the real compensated weights one
still must control the weight carried at the unique birth time.  The
future-overlap fugacity is designed to prepay exactly such a first-kill
weight.  Proving that its predictable first-kill coefficient dominates the
cylinder-weighted switch-birth coefficient, with multiple blockers sent to
`(FE3)`, is now the sole coefficient row.

## 2. A hidden permutation does not remove the adaptive correlation

Let a group `G` act on the resource layer.  A stopped state `S` determines
a vector `f_S` and a stopped operator `A_S`.  Covariance means

\[
 f_{gS}=g f_S,
 \qquad A_{gS}=gA_Sg^{-1}.
 \tag{2.1}
\]

Let `R` commute with `G`, as the pristine Johnson resolvent does.

### Proposition 2.1 (orbit-hiding invariance)

For every `g in G`,

\[
 \boxed{
 \langle f_{gS},R(A_{gS}-A_0)f_{gS}\rangle
 =\langle f_S,R(A_S-A_0)f_S\rangle,}
 \tag{2.2}
\]

whenever the displayed real form is symmetrized if necessary.  The same is
true for `\langle f_S,(B_S-B_0)f_S\rangle` and for the corresponding
carre-du-champ.

Hence sampling a hidden uniform global permutation, or a hidden uniform
element of the stabilizer of an exposed prefix, does not average the JRES
perturbation toward zero.

#### Proof

Substitute (2.1), use `g^{-1}Rg=R` and
`g^{-1}A_0g=A_0`, and cancel `g^{-1}g`.  The argument is unchanged for a
subgroup stabilizer.  \(\square\)

The orbit-quotient filtration can still avoid unnecessary label unions,
but it cannot by itself prove the adaptive resolvent estimate.  The
adapted vector and the stopped operator rotate together.

## 3. Equivariance plus regular degrees is insufficient

The failure above is not merely formal.  There is a finite regular model
with exactly the same logical obstruction.

### Proposition 3.1 (equivariant stopped-kernel counterexample)

Let `Omega` have even size `N`, and let `A` be a uniformly random
`N/2`-subset.  On the mean-zero subspace put

\[
 f_A={\bf1}_A-{\bf1}_{A^c}.
 \tag{3.1}
\]

Let `L_A` be the direct sum of the normalized complete-graph Laplacians on
`A` and `A^c`.  Every vertex has the same current degree, but

\[
                         L_Af_A=0.
 \tag{3.2}
\]

Put

\[
 B_A={f_Af_A^*\over\|f_A\|_2^2}.
 \tag{3.3}
\]

The joint law `(f_A,L_A,B_A)` is `Sym(Omega)`-equivariant.  Nevertheless,

\[
 \langle f_A,B_Af_A\rangle=N,
 \tag{3.4}
\]

while

\[
 \mathbb E B_A={1\over N-1}\Pi_{\bf1^\perp}.
 \tag{3.5}
\]

Thus the pristine trace sees only the scalar `1/(N-1)`, whereas the
adapted vector lies in a zero mode of the current regular operator and pays
a factor `Theta(N)` more.

#### Proof

The two complete blocks are regular and (3.2) is immediate because `f_A`
is constant on each block.  Equation (3.4) follows from
`B_A f_A=f_A` and `||f_A||_2^2=N`.  The average in (3.5) commutes with the
full symmetric group and vanishes on constants.  It is therefore scalar on
the mean-zero representation.  Its trace is one, giving the scalar
`1/(N-1)`.  \(\square\)

This counterexample does not claim that the displayed two-block state is
reachable in the balanced-doublet host.  It proves the exact logical
boundary: neither equivariance, good one-root loads, nor the pristine trace
can exclude an adapted slow stopped mode.  A host-specific selected-relation
argument is indispensable.

## 4. Exact killed-process Bellman compensator

The absolute-value sum in `(JRES)`, and the sum of positive compensator
increments in `(JSW)`, are stronger than the stopped theorem needs.  There
is an exact one-sided formulation.

Let `S_i` be the full stopped state of the raw doublet process, including
the density index and all occurrence labels.  Let `T` be the terminal
stopping time.  After the already proved `(ROc)`, `(FE3)`, owner-ledger, and
slot charges are removed, let

\[
 D(S_i)=\mathfrak D_i\ge0
 \tag{4.1}
\]

be the remaining Johnson FIFO payment in (5.25), including the finitely
many anchored marked versions.

For a stopped state `s` at level `i`, define its actual future value

\[
 \boxed{
 V(s)=\mathbb E_s\sum_{j=i}^{T-1}D(S_j).}
 \tag{4.2}
\]

### Theorem 4.1 (Bellman equality)

Along the actual process,

\[
 \boxed{
 D(S_i)=V(S_i)-
       \mathbb E[V(S_{i+1})\mid\mathcal F_i].}
 \tag{4.3}
\]

In particular

\[
 \boxed{
 \mathbb E\sum_{i<T}D(S_i)=V(S_0).}
 \tag{4.4}
\]

Thus the unconditioned Johnson transfer is equivalent to the single
initial estimate

\[
                         V(S_0)=O(M/d^4).
 \tag{JVAL}
\]

For a class `P` of allowed separator prefixes, the hereditary transfer is
equivalent to the corresponding uniform continuation estimate

\[
 \boxed{
 V(s)\le C\,\mathscr L(s)+I(s)
 \quad(s\in\mathcal P),}
 \tag{JBEL}
\]

where `I(s)` is the already priced future static injection from `(ROc)`,
`(FE3)`, slots, and marked entry patterns.  Any version of `(JBEL)` whose
initial value plus expected injected increments is `O(M/d^4)` implies
`(JSEC)`.

#### Proof

Split the sum in (4.2) into its first term and its tail and use the Markov
property of the full stopped state.  This gives (4.3).  Sum and telescope
to get (4.4).  The equivalence with `(JVAL)` is immediate because `D` is
nonnegative.  Applying the same identity after every `s in P`, followed by
the occupation estimate for `mathscr L` and the stated injection ledger,
gives the hereditary assertion.  \(\square\)

`(JBEL)` is strictly weaker than `(JRES)` and `(JSW)`.  It permits arbitrary
cancellation among signed current-versus-pristine perturbations before
their total future effect is evaluated.  It never takes a supremum over a
Johnson sector and never sums absolute perturbations at every step.

There is an equivalent supersolution form which is more constructive.

### Corollary 4.2 (one-sided selected-relation supersolution)

It suffices to construct a nonnegative function `Phi` on the allowed
stopped states and a nonnegative priced injection `J` such that

\[
 \boxed{
 D(s)+\mathbb E_s\Phi(S_{i+1})
       \le\Phi(s)+J(s),}
 \tag{4.5}
\]

and

\[
 \Phi(S_0)+\mathbb E\sum_{i<T}J(S_i)=O(M/d^4).
 \tag{4.6}
\]

For heredity, the same rows are required after every prefix in `P`.

This is the exact place to use a future-weighted selected-relation
potential.  Unlike `(JRES)`, only the **net one-sided Bellman defect** of
that potential must be bounded.

## 5. The cleanup interface has two proof-safe options

The downstream atomic-tile theorem asks for an unordered marked cylinder
through a sequence of doublet-closed separator exposures.  Its rare marked
carrier event is part of the same unordered packing law as cleanup.  A
constant unconditional cleanup probability does not imply a positive
intersection with that rare event: abstractly, one may have
`C=A^c` with `P(C)` close to one and `P(A cap C)=0`.

The later independent orientation coins are different.  They are unexposed
after the unordered packing, so cleanup is independent of that final
orientation layer.  Global coordinate hiding does not similarly separate
the unordered marked-carrier event: both it and cleanup are invariant under
the hidden relabelling.

There are two distinct proof-safe interfaces.

1. If one first conditions the unordered packing law on a small-cleanup
   event, then one needs `(JBEL)`, or the cylinder-weighted variant, on the
   following much smaller class:

> the doublet-closed prefixes generated by the prescribed atomic
> separator/tile cylinder, with only the still-unexposed occurrences left
> as tests.

   This is the proof-safe hereditary scope for a **conditioned** output
   law.

2. The selected-relation quarantine theorem gives another interface.  Run
   the raw process, delete every analytically bad selected block/relation,
   and retain the resulting random law without conditioning on the number
   deleted.  Its killed-event proof gives the hereditary cylinder
   directly, because an occurrence surviving quarantine certifies every
   tested row along its history.  In that interface `(JVAL)` at `S_0` is
   enough to give expected `O(M/d)` lower leave.  No prefix-uniform cleanup
   estimate is needed, provided the next theorem accepts a random
   quarantined law with expected leave and combines its terminal success in
   one joint expectation argument.

Thus a theorem only at `S_0` is not automatically sufficient for an
arbitrarily **conditioned** packing law, but it can be sufficient for the
raw monotone-quarantine architecture.  The exact downstream interface must
be fixed before imposing the stronger prefix row.

## 6. Exact remaining analytic row

The strongest closed facts are now:

1. the false scalar bound is replaced by the pristine resolvent;
2. its complete-orbit kernel has bounded diagonal and bounded entries;
3. the unmarked and finite anchored pristine noise traces have the required
   scale;
4. absolute current-versus-pristine control is unnecessary;
5. global or stabilizer label hiding does not control the adapted form.

The Atomic portal-tile packing lemma is presently stated with a deterministic
`O(M/d)` leave and a hereditary cylinder after every separator exposure.
Without a downstream redesign, it therefore uses the conditioned interface.
Its sole local analytic residue is:

\[
 \boxed{
 \text{Construct a cylinder-prefix-weighted selected-relation
 supersolution satisfying the JCYL rows.}}
 \tag{6.1}
\]

Equivalently, prove the true-`h` weighted form of `(JBEL)` for every allowed
separator-prefix event.  A future redesign which consumes the raw
quarantine law and expected leave could reduce this to `(JVAL)`, but that
redesign is not part of the current implication.
The supersolution may use the actual
current vector and may be state-dependent.  It need not compare current and
pristine operators in absolute value.  A current-operator Lyapunov or a
backward killed observability Gramian is acceptable precisely when its
noise trace and its change under one selected doublet satisfy (4.6).

The regular two-block example shows why one further host-specific input is
necessary.  A sufficient such input would be either:

* a one-sided switching inequality for the future-weighted selected
  relations; or
* an actual-vector conductance/observability estimate ruling out a stopped
  slow mode on every marked separator prefix.

No scalar near-isotropy statement is revived, and no all-direction sector
norm is required.
