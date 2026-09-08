# Audit: orbit energy, relabeling reachability, and soft-greedy stall

Date: 2026-07-25

Method: pure mathematics only.

## 0. Verdict

Three proposed conclusions have different statuses.

1. The prime-cycle crossover `q=m^(1/4)` and the
   `O_A(Wm^(-1/4))` aggregate orbit floor are correct.  The claim that the
   hypothesis must be changed from physical centered energy to a prescribed
   orbit-energy hypothesis is **false**.  Exact conjugacy-class averaging
   converts physical energy into orbit energy for one common adaptively
   chosen prime cycle.

2. The relabeling reachability cardinality bound is correct after replacing
   the stated set of moves by the subgroup it generates.  Its proposed
   consequence--that a small phase family cannot contain a low-hole
   factor--does not follow.  Cardinality is not an action-capacity lower
   bound, and an exponentially small structured family may contain an
   exceptional design.

3. The displayed greedy stall calculation is a useful first-moment
   diagnostic for a pseudorandom/independent residual trajectory.  It is
   not a theorem about every adaptive sequential construction.  No
   deterministic sequential route can be closed from that calculation
   without a hereditary entropy or supersaturation theorem applying to
   every reachable residual.

Accordingly the fixed-`Z_n` phase route remains unproved, not disproved.
The correct joint gate is still Poisson-scale physical energy plus an exact
structured row lift.

## 1. Physical energy really does imply orbit energy after choosing the cycle

Let `n=2m+1` be prime, let `f` be a centered function on one nontrivial
Johnson rank, and for an `n`-cycle `sigma` put

\[
 \Pi_\sigma={1\over n}\sum_{j=0}^{n-1}P_{\sigma^j}.
\tag{1.1}
\]

On a target necklace `O`, if

\[
                         d_O=\sum_{S\in O}f(S),
\]

then

\[
 \mathcal E_\sigma(f):=\sum_Od_O^2
 =n\|\Pi_\sigma f\|_2^2.
\tag{1.2}
\]

For one prescribed `sigma`, Cauchy gives only

\[
                         \mathcal E_\sigma(f)\le n\|f\|_2^2.
\tag{1.3}
\]

That observation is correct but irrelevant to the prime-cycle theorem,
which chooses `sigma`.  The exact class average is

\[
 \mathbb E_\sigma\Pi_\sigma
 =\Pi_0+{1\over n}\sum_{j\ge2}\Pi_j.
\tag{1.4}
\]

For an exact cyclic load, `f` has no degrees zero or one.  Hence

\[
 \boxed{
 \mathbb E_\sigma\mathcal E_\sigma(f)
 =\|f\|_2^2.}
\tag{1.5}
\]

For a centered load from a near-factor, the degree-one term has coefficient
zero and therefore

\[
 \mathbb E_\sigma\mathcal E_\sigma(f)
 \le\|f\|_2^2.
\tag{1.6}
\]

Thus `||f_q||^2=O_A(W)` at every controlled depth gives one common cycle
with the required weighted orbit energies, by averaging the normalized sum
of the shallow and surplus-weighted functionals.  No orbit-decorrelation
hypothesis must be added separately.

An exactly `Z_n`-invariant seed is indeed maximally correlated for that
same prescribed cycle.  It follows only that the cycle used for smoothing
cannot automatically be identified with a preassigned symmetry of the
seed.  This is the already stated row-lift correlation gate, not a flaw in
the energy theorem.

## 2. The correct reachability bound

Let `S` be a set of allowed coordinate relabelings and put

\[
                         H=\langle S\rangle\le S_n.
\]

Start from a factor with `T` rows.  Under any sequence of legal replacements
using elements of `S`, every row ever appearing belongs to `H dot F`.
Therefore

\[
 |H\cdot F|\le |H|T,
\]

and the number of reachable `T`-row families satisfies

\[
 \boxed{
 |\mathcal R|\le\binom{|H|T}{T}
 \le(e|H|)^T.}
\tag{2.1}
\]

This is a valid catalogue-size upper bound.

Two quantifier corrections are essential.

* Repeated use of one fixed involution has `|H|=2`, but adaptive use of
  coordinate transpositions has `H=S_n`, not a group of size two.
* Repeated phases of one fixed prime cycle have `H=Z_n` and satisfy the
  smaller bound.  This is the scope relevant to the component-phase gate.

## 3. Why catalogue size is not a repair-capacity obstruction

No implication of the form

\[
                         \log|\mathcal R|=o(W)
 \quad\Longrightarrow\quad
 \min_{F'\in\mathcal R}H_1(F')=\Omega(W)
\tag{3.1}
\]

is valid without an additional structural theorem.

The simplest counterexample to the inference is formal but decisive: a
reachable family of size one may itself consist of a perfect design.  More
generally, one binary choice can exchange two globally different factors
whose shadow counts differ by `Theta(W)`.  The number of choice bits does
not upper-bound the magnitude of the objective change.

To turn (2.1) into a no-go, one would need a theorem such as

\[
 \#\{F'\in H\cdot F:\ H_1(F')\le\epsilon W\}=0,
\tag{3.2}
\]

or a probability measure on the structured catalogue under which the good
event has probability smaller than `1/|mathcal R|`, together with a union
bound over a genuinely random external parameter.  Neither statement is
provided by the cardinality calculation.

The assertion that `H_1` is a sum of weakly dependent Bernoulli indicators
with mean `e^(-1)` is true for an iid-like occupancy model.  It is exactly
what an algebraic design is intended to violate.  It cannot be assumed for
the phase factors whose strong correlations are the entire point of the
construction.

Consequently the `m/log m` comparison between catalogue entropy and a
generic large-deviation exponent is a heuristic barrier to random search,
not an impossibility theorem for an explicit phase identity.

### 3.1 A cyclic-variant exact-factor countermodel

The failure of the cardinality inference persists in a model having the
same packetwise exactness and fixed-cycle reachability structure as the
proposed argument.

Let `T` and `n` be positive integers.  Partition an abstract middle
universe into `T` disjoint packets

\[
                         \Omega=P_1\sqcup\cdots\sqcup P_T,
 \qquad |P_i|=n.
\]

For every `i` and `a in Z_n`, create a row `C_(i,a)` whose middle support is
exactly `P_i`.  Let the cyclic group act by

\[
                         gC_{i,a}=C_{i,a+1}.
\tag{3.3}
\]

Every family

\[
                         F_{\mathbf a}
 =\{C_{i,a_i}:1\le i\le T\}
\tag{3.4}
\]

is an exact middle factor: its row supports partition `Omega`.  The owner
overlay between a state and its cyclic translate has one independent
component over each packet, so componentwise switches reach every vector
`mathbf a in Z_n^T`.  Thus

\[
                         |\mathcal R|=n^T.
\tag{3.5}
\]

Attach to packet `i` a set `Q_i` of `n` critical shadow targets.  Declare
the row `C_(i,0)` to cover all members of `Q_i` once.  For every `a ne 0`,
let `C_(i,a)` cover a set `R_(i,a)` of `n` distinct filler targets, disjoint
from `Q_i`.  The filler targets may be regarded as already covered by a
fixed background family, so the defect objective counts the uncovered
critical targets.  Take the `Q_i` disjoint over `i`.  Thus every row still
has `n` distinct shadow occurrences; no duplicate within a row is being
used in the counterexample.

The initial state `F_(1,...,1)` misses all `nT` desired targets, while the
reachable state `F_(0,...,0)` misses none.  Nevertheless, on the wreath
scale `T=W/n`,

\[
 \log|\mathcal R|=T\log n={W\log n\over n}=o(W).
\tag{3.6}
\]

Thus even a bad initial factor, a single fixed cyclic relabeling group,
packetwise exactness at every state, and a reachable catalogue saturating
the bound `exp(O(W log n/n))` do not make the entropy inference valid.
The example is abstract rather than a Boolean-wreath realization; that is
enough to disprove any formal deduction using only the stated catalogue
size and exact packet ownership.

The reachability estimate becomes a genuine no-go only after adding at
least one theorem of the following kind.

1. **Statewise exclusion:** every factor in the structured row orbit
   `H dot F` has defect at least `cW`.
2. **Metric stability:** every reachable factor lies within row distance
   `r` of the seed and the defect can fall by at most `Lr`, with
   `Lr=o(W)`.
3. **External-randomness union bound:** conditional on a random external
   parameter, every fixed catalogue state is good with probability at
   most `exp(-cW)`, uniformly over the catalogue, so that (2.1) may be
   union-bounded.
4. **Hereditary continuation bound:** every reachable residual, not merely
   an iid residual, has too few legal continuations to reach a good state.

None of these statements follows from (2.1).

## 4. The stabilizer tension has restricted scope

Large coordinate groups do have large orbits on generic middle sets, and
this can make a decomposition into many **group-invariant** support blocks
impossible.  But a legal adaptive switch requires invariance only under the
particular move used on its current support, not invariance under the full
generated group `H`.  Different stages may use different subgroups and
different component refinements.

Thus orbit-size calculations for Young subgroups correctly rule out some
specific invariant-block architectures.  They do not combine with (2.1)
to rule out every relabeling construction.

## 5. Scope of the soft-greedy stall calculation

The proposed exponent has the form

\[
 \log(\text{catalogue size})
 -\log(\text{survival penalty under a random residual}).
\tag{5.1}
\]

It is a first-moment estimate for a residual whose consumed resources look
independent with density `1-z`, with entropy corrections for tolerated
repetitions.  Under that model it correctly reproduces familiar scales:

* one nearly hard protected depth stalls around `z=m^(-1/2)`;
* finitely many independent protected depths worsen the exponent;
* a growing band makes a pseudorandom residual catalogue disappear very
  early.

It does not prove that every sequential algorithm follows this residual
law.  A deterministic construction may deliberately preserve a highly
structured, exponentially small reservoir of admissible rows.  To obtain a
universal sequential no-go one needs a hereditary theorem saying that **for
every** admissible residual with the prescribed density, the number of
legal continuation rows obeys the same upper bound.  No such theorem is
currently available, and the displayed first moment does not establish it.

The rigorous conclusion is therefore:

\[
 \boxed{
 \text{iid-like or standard random-greedy trajectories are at the critical
 leave scale already at depth one; arbitrary structured sequential
 constructions are not ruled out}.}
\]

## 6. Correct disposition

The following items should be retained:

1. the `m^(1/4)` prime-cycle crossover;
2. the exact reachability bound (2.1), with `H=<S>`;
3. the random/pseudorandom greedy stall as a diagnostic;
4. the warning that the smoothing cycle and a block-rich algebraic symmetry
   must be correlated nontrivially.

The following proposed closures should not be recorded as theorems:

1. physical energy must be replaced by prescribed orbit energy;
2. `e^(o(W))` reachable factors cannot contain an exceptional design;
3. every relabeling repair is impossible;
4. every sequential soft-shadow construction is impossible.

The exact live positive target remains the conjunction of Poisson-scale
physical energy and a structured row lift for one selected prime cycle.
