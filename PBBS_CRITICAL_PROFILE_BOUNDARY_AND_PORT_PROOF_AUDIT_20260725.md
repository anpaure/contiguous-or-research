# Proof audit: critical profile--boundary saturation versus normalized-port crossing

Date: 2026-07-25

Method: proof-level mathematics only. No computation, search, or external input.

## 0. Verdict

This note audits the two claims

1. `MATH_ATTACK_PBBS_CRITICAL_PROFILE_BOUNDARY_JOINT_SATURATION_20260725.md`,
2. `MATH_ATTACK_W_PBBS_NORMALIZED_PORT_CROSSING_OBSTRUCTION_20260725.md`.

The conclusions are different.

* The normalized-port note is proof-level correct within its explicitly
  conditional and architectural scope.  It proves an exact chart, an exact
  trail ledger, and an exact obstruction to chronology-preserving decorated
  port joins.  It does **not** prove any estimate on the number of critical
  PBBS runs or on their crossing support.
* The profile--boundary note correctly identifies the critical coefficient
  scale and correctly constructs an integral assignment to *formal word
  labels*.  Its advertised exact joint capacitated realization is not proved.
  Two separate steps use capacity that has not been supplied.

Consequently the two notes do not combine to prove the critical

\[
 p\asymp q\asymp \sqrt m
\]

little-oh estimate.  The surviving problem is still an actual canonical-PBBS
cross-phase incidence theorem.

## 1. What survives from the critical-profile note

Let

\[
 \Omega_{m;s,p}
\]

be the weak-composition tower set in its equation (1.4).  Subject to the
previously established continuant coefficient formula, the equality

\[
 |\Omega_{m;s,p}|=\mathcal E_{m;s,p}
\]

is exact.  The critical-cell computation at \(z=1/4\) is also consistent:

\[
 4^{-s}\mathscr F^\star_{s,p}(1/4)=\Theta(p^{-4})
\]

when \(p\le b\le 2p\).  The averaging argument therefore gives, along an
infinite sequence of coefficient indices, a critical cell family with

\[
 \sum_{(s,p)\in\mathscr C_m}|\Omega_{m;s,p}|
   =\Omega(4^m/m^2),
 \qquad p,q,s\asymp\sqrt m,
\]

provided one imports the stated moment/two-pole estimates.  Nothing in the
audit below challenges this coefficient calculation.

The count

\[
 |\mathcal W_p|=\binom{2p-2}{p}\asymp 4^p/\sqrt p
\]

is exact, and balancing \(\Omega_{m;s,p}\) over this many word labels gives

\[
 |\beta_{s,p}^{-1}(e)|
 \le C\frac{4^{m-p}\sqrt p}{m^3}+1.
\]

Thus there is a valid **integral formal load table**.  This is already
stronger than multiplication of two marginal estimates.

There is, however, an antecedent scope restriction inherited from the
source profile theorem.  That theorem defines \(\mathcal E_{m;s,p}\) as a
**capacity envelope** and explicitly says that it is only an upper bound for
genuine returns: not every weak-composition tuple counted by the product is
known to be dynamically realizable.  Consequently (1.4) is an exact finite
set whose cardinality equals the envelope coefficient, but calling its
members "literal inverse towers" does not turn them into canonical PBBS
inverse paths.  Any theorem about actual towers additionally needs a
realization map

\[
 \Omega_{m;s,p}\longrightarrow
 \{\hbox{canonical PBBS inverse towers of profile }(s,p)\},
\]

with controlled fibres.  No such map is proved.  This is harmless if the
claim is explicitly only about a formal envelope relaxation, but it rules
out the stronger wording "exact joint realization" from the start.

## 2. First gap: an upper bound is used as lower capacity

The note proves only

\[
 \mathcal B_{m;s,p}(e)
 \le C4^{m-p}\frac{(p+2)^2}{s^6}.                 \tag{2.1}
\]

In a critical cell the right side of (2.1) has order

\[
 U_{m;s,p}:=\Theta_C(4^{m-p}/m^2).
\]

But its equation (3.9) silently replaces the one-sided assertion (2.1) by

\[
 \mathcal B_{m;s,p}(e)\asymp_C U_{m;s,p},         \tag{2.2}
\]

and then concludes

\[
 |\beta_{s,p}^{-1}(e)|\le \mathcal B_{m;s,p}(e). \tag{2.3}
\]

Neither (2.2) nor (2.3) follows from (2.1).  A proved upper bound on the
number of feasible arrays is not a stock of available arrays.  It may be
strict, and for a prescribed word \(e\) the actual fibre may even be empty.

The step can be repaired only by changing the theorem.  Define the *formal
allowance*

\[
 U(e)=C4^{m-p}(p+2)^2/s^6.
\]

Then the balanced assignment proves

\[
 |\beta^{-1}_{s,p}(e)|\le U(e),
\]

for large critical cells.  This is saturation of a numerical cap
relaxation, not compliance with the actual fixed-word fibre.

To recover the advertised claim one needs a lower-realization lemma, uniform
in a sufficiently large subfamily of words:

\[
 \#\{\hbox{actual boundary arrays with word }e\}
 \ge c4^{m-p}/m^2.                                \tag{2.4}
\]

No such lemma is proved in the note.

## 3. Second gap: the artificial cycle has no fibrewise supply map

For each single table object \(\tau\), Section 5 creates a fresh directed
cycle

\[
 \Gamma_\tau=\mathbb Z_{3g},\qquad g=2s+1,
\]

tags all \(3g\) vertices by the same profile object, and selects three
length-\(g\) intervals.  Pairwise edge-disjointness is tautological in these
fresh cycles.  What is not supplied is an injection of those artificial
parent edges into the real inverse fibres whose capacities the construction
claims to respect.

The sentence "use one clone of the reduced edge for every profile object
lying over it" supplies one clone per \(\tau\).  The artificial cycle uses
\(3g\) parent-edge positions carrying that same \(\tau\), and its three
translated descendant fans are asserted to live over those positions.  A
global estimate

\[
 \sum_\tau 3g=O(\operatorname{Cat}_m)
\]

does not imply that, inside each reduced-edge/profile fibre, \(3g\) distinct
compatible parent clones exist.  Global Catalan mass cannot be redistributed
freely between inverse fibres.

The missing datum is a family of injections

\[
 \iota_{j,e}:
 \{(\tau,t):\partial^j(\tau)=e, t\in\mathbb Z_{3g}\}
 \longrightarrow \partial^{-j}(e),                \tag{3.1}
\]

compatible across \(j\), with the phase-translated fan of \((\tau,t)\)
realized by the image tower.  No construction or Hall inequality proving
(3.1) appears.

Equivalently, one would need a uniform fibrewise lower supply roughly a
factor \(g\asymp\sqrt m\) larger than the loaded constrained objects, not
merely the global equality of orders.  The exact inverse-fibre ledgers give
upper capacities; they do not manufacture these copies.

Therefore Section 5 proves an integral packing in a freely generated
ambient-cycle model.  It does not prove an integral packing in the stated
profile--descendant fibre-capacity relaxation.

## 4. Corrected theorem from the profile construction

What is proved after the two corrections above is the following.

> **Formal joint-load theorem.**  Along infinitely many \(m\), there is an
> integral table of \(\Omega(4^m/m^2)\) exact weak-composition tower objects,
> each carrying a positive word label and the formal triangular interval
> pattern, such that the load on each word label is below the explicit
> numerical upper allowance \(U(e)\).  These objects can be placed in freely
> generated disjoint cycles using Catalan-order total edge mass.

This theorem is a useful compatibility check.  It shows that the *orders of
magnitude* of the known marginal ledgers are mutually compatible.  It does
not show that all known exact local capacities can be jointly saturated.

The genuine PBBS atom in Section 6.1 proves only nonemptiness of one local
geometry at critical scale.  It does not supply either uniform word-fibre
abundance (2.4) or the descendant supply maps (3.1).

## 5. Audit of the normalized-port note

The following claims check exactly.

### 5.1 Sandwich chart

For

\[
 X_t=S\cup\{\gamma_t,\ldots,\gamma_{t+q-1}\},
\]

the nonlazy Johnson property gives separation at least \(q+1\) between
equal token occurrences.  Consequently the displayed word has exact length

\[
 r+2q+1
\]

and its interval ORs give all unions and intersections internal to the run.
The proof correctly handles labels repeated far apart.

### 5.2 Coarse normalized-port trail ledger

The type count

\[
 T_q=(N-1)_{q-2}
\]

is exact.  Directed trail decomposition and phase-voltage lifting give, for
the chosen deckwise-uniform routing,

\[
 L_q=M_q+N\bar R_q+(q-1)c_q,
 \qquad c_q\le N(D_q+T_q).
\]

The resulting conditional gate

\[
 \sum_q(q-1)D_q=o(B)
\]

is valid under the explicitly assumed global owner-disjointness.  The note
does not claim or prove that canonical PBBS supplies this bound.

### 5.3 Reversal and decorated-port rigidity

For every orientation choice the imbalance satisfies

\[
 d-Jd=\Xi,
 \qquad D(d)\ge\|\Xi\|_1/4.
\]

This calculation is correct.  The free phase action, normalized decorated
input injectivity, and maximal-run FIFO gluing theorem are also valid in the
stated PBBS quotient setting.  A decorated match merely rejoins two pieces
of the same maximal run; it creates no join between distinct proper maximal
runs.

Hence the architectural conclusion is sound: coarse ports can fuse internal
charts but forget crossing chronology, whereas chronology-bearing ports are
rigid.  The existing QCF chart cannot be paid independently at a critical
number of lost seams.

### 5.4 Explicit scope

The note still assumes, rather than proves,

\[
 \sum_q(q-1)D_q=o(B),
 \qquad |\mathcal X|=o(W).
\]

It is therefore an exact conditional compiler/no-go for a particular port
architecture, not a critical PBBS packing theorem and not a lower bound
against arbitrary OR words.

## 6. Why the two notes do not combine

The first note assigns formal endpoint words to profile objects but does not
place those objects in the actual canonical PBBS chronology.  The second
note starts from actual PBBS maximal runs and proves that chronology cannot
be restored by local decorated-port matching.  There is no map carrying the
formal table of the first note into the run multigraph of the second while
preserving fibres, phases, and crossing targets.

In symbols, the missing object is not another marginal estimate but an
actual incidence map

\[
 (\text{inverse tower},\text{phase})
 \longmapsto
 (\text{PBBS owner run},\text{boundary word},\text{descendant fan}),
\]

with simultaneous control of

\[
 \sum_q(q-1)D_q,
 \qquad |\mathcal X|,
\]

or, on the packing side, a strict common-base cross-phase estimate such as

\[
 \sum_i\sum_{e,e'}
 |\mathcal A_i(e)\cap\tau^{-g}\mathcal A_{i+g}(e')|
 =o\!\left(m^{-1/2}\sum_i|\Omega|\right).          \tag{6.1}
\]

Neither audited note proves (6.1), and the exact last-level mountain phase
calculation shows why a one-level argument cannot: in the dominant
unit-curvature sector the permitted anchor set has \(\Theta(\sqrt m)\)
phases and supports critical-density disjoint candidates.

## 7. Final corrected status

The critical lane remains open.

Proved:

1. the critical profile coefficient envelope is of order \(4^m/m^2\);
2. its objects can be balanced over formal positive word labels below the
   explicit numerical allowance;
3. the one-run sandwich compiler and normalized-port ledger are exact;
4. local chronology-bearing decorated ports cannot join distinct maximal
   PBBS runs;
5. additive full-fan descendant-volume ledgers, like the last-level phase
   ledger, remain critical and cannot alone give little-oh.

Not proved:

1. actual fixed-word fibres have enough objects to realize the balanced
   assignment;
2. the artificial residue cycles embed fibrewise into actual inverse towers;
3. canonical PBBS transport gives a strict cross-phase incidence saving;
4. the coarse-port imbalance and lost-crossing support are little-oh.

Thus there is no coefficient-one proof in the two notes.  Their valid common
message is narrower and useful: every successful argument must exploit a
genuine nonlocal canonical-PBBS cross-phase identity, not only profile
coefficients, endpoint strip bounds, descendant volumes, or local port
matching.
