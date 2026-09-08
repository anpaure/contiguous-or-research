# Audit of the three attached exploratory texts: implications for flagged reserve

Date: 2026-07-25

Method: pure mathematics only.

## 0. Verdict

The three pasted texts are exploratory derivations, not complete proofs.
They recover several correct themes already present in the audited ledger:

1. the ordered-partition / move-to-front state formulation;
2. the cyclic-window reduction for a central band;
3. the `Theta(W sqrt(m))` Poisson miss barrier;
4. the distinction between the exact middle wreath factor and its
   unresolved multirank shadows;
5. the possibility that holes at different ranks could share one repair
   chain.

They do not contain a new construction proving coefficient one.  The only
point needing a precise flagged-reserve correction is item 5.

## 1. Cross-rank repair is a width problem, not a maximum-row problem

Let `H` be a family of missing masks in the controlled band, ordered by
inclusion.  If one chain

\[
 S_0\subset S_1\subset\cdots\subset S_a
\]

is supplied as one legal vertical reserve column, then its masks can share
one initialization and one trajectory.  Thus cross-rank sharing is real.
However, it is not automatic that all holes can be arranged into only

\[
 \max_r |H\cap\tbinom{[n]}r|
\]

chains.  By Dilworth, the exact minimum number of abstract inclusion
chains is

\[
 \boxed{\operatorname {width}(H).}
\]

Always

\[
 \operatorname {width}(H)
 \ge \max_r |H\cap\tbinom{[n]}r|,
\]

and the inequality may be strict: holes on different ranks can be
pairwise incomparable.  Therefore the attachment's phrase "perfect
chaining makes the repair cost the worst single row" is a conditional
ideal, not a theorem.

For the literal one-column compiler already proved in the workspace,

\[
 \boxed{
 \operatorname {RCov}_Q(H)
 \le (2Q+2)\operatorname {width}(H).}
\]

With tagged reserve columns, the correct necessary and sufficient Hall
condition is the tagged chain-Hall inequality

\[
 |A|\le |\Gamma^+_H(A)|
       +\sum_{U\in\Gamma_{\mathcal R}(A)}b_U
 \qquad(A\subseteq H).
\]

So the useful idea from the attachments reduces exactly to the existing
chain-Hall / low-width reserve gate.

## 2. Why sparse random wreaths plus chain repair is not yet a proof

If a random wreath family leaves hole family `H`, its row counts alone do
not control `width(H)`.  In particular, a common-core or distance-code
hole family can have moderate load in every row while remaining almost
entirely incomparable across rows.  Hence an estimate of the form

\[
 \max_q M_q=o(W)
\]

does not imply an `o(W)` repair word unless one also proves a cross-rank
comparability or tagged chain-Hall theorem.

At the middle rank there is additionally no sharing gain: it is an
antichain, so `M_0` missing middle masks alone require at least `M_0`
right endpoints.  Thus any proposed low-density main word must retain the
middle endpoint ledger explicitly.

## 3. Translation and arithmetic-progression orbits

The observations about arithmetic-progression cyclic orders are useful as
examples of maximally correlated wreaths, but taking translation orbits
does not improve the normalized coverage load.  At every rank it merely
divides both the number of slots and the number of targets by the orbit
size.  Stabilizers and the congruence of the required number of wreaths
also prevent a naive fully translation-equivariant exact factor in small
dimensions.

The correct symmetry statement is instead the edge-transitive orbit
lemma proved in
`EDGE_TRANSITIVE_AUGMENTED_TEMPLATE_ORBIT_REDUCTION_20260725.md`: for one
fixed coordinate-template orbit, every weighted residual matching cut is
equivalent to its single unweighted full-orbit matching number.  Symmetry
removes the weighted quantifier but does not prove that matching number is
near the fractional capacity.

## 4. Ucycles and permutation states

A permutation move-to-front trajectory exposes a maximal chain at each
endpoint, and its middle prefixes may be viewed as a distinct-symbol
window process.  This is a useful model.  A universal cycle for the middle
sets alone, however, does not automatically cover the upper ranks: the
longer recency prefixes depend on return gaps, and the required lower and
upper flags must remain synchronized.  The attachments do not establish
the needed return-gap or multirank coverage theorem.

## 5. Exact status

The attachments add no proved coefficient-one step.  Their strongest
surviving suggestion is already isolated as one of two equivalent gates:

* prove low inclusion width / tagged chain Hall for the residual holes; or
* prove a near-perfect matching in one augmented edge-transitive geodesic
  template orbit.

Both remain open.  Random occupancy, translation averaging, and rowwise
hole counts alone do not imply either gate.
