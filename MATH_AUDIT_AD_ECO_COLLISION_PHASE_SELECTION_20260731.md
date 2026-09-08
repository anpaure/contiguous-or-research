# Audit of the ECO collision-path phase-selection theorem

Date: 2026-07-31
Audited file:
MATH_THEOREM_AD_ECO_COLLISION_PHASE_SELECTION_20260731.md

## Verdict

PASS, with the scope stated in the theorem. The result is an exact abstract
selection theorem for a repaired, fixed-rotation witness atlas. It is not a
proof that the canonical ECO atlas has the necessary witness
multiplicities, an owner-aligned decoration, or a component-faithful
physical realization.

## 1. Exact probability check

For one required tree edge \(e\), a nontrivial collision path contributes:

* probability zero of failure if it has witnesses on both parities;
* one forced bad bit, of probability \(1/2\), if it has witnesses on exactly
  one parity;
* no constraint if it has no witness.

An isolated witness makes the edge automatic. Thus, after automatic edges
are removed, absence of \(e\) is exactly one cylinder fixing the
\(\tau(e)\) independent path bits in \(J_e\). Hence

\[
                         \Pr(B_e)=2^{-\tau(e)}.
\]

Raw atom multiplicity within one parity class does not change this
probability. The exact CNF (2.1), the union sum (3.1), and the biased product
(3.4) follow.

## 2. Uniform threshold and sharpness check

For \(q\) required tree edges and \(\tau(e)\ge r\),

\[
                       \sum_e2^{-\tau(e)}\le q2^{-r}.
\]

The strict inequality \(q<2^r\) is therefore sufficient. Its integer form
is

\[
                  r\ge\lceil\log_2(q+1)\rceil.
\]

The sharpness construction is internally exact. For every
\(\omega\in\{0,1\}^r\), edge \(e_\omega\) receives on path \(i\) one
witness of parity \(1-\omega_i\). Therefore

\[
 e_\omega\text{ absent}
 \iff \sigma_i=\omega_i\text{ for all }i
 \iff \sigma=\omega.
\]

The \(2^r\) bad cylinders are the \(2^r\) singleton phase assignments and
partition the phase cube. Each witness atom is used for only one strict
binary target edge. At \(r=1\), the obstruction is exactly the contradictory
CNF \((\sigma)\wedge(\neg\sigma)\). Thus no better uniform theorem can be
deduced from phase multiplicity alone.

## 3. Local-lemma check

Bad event \(B_e\) is measurable with respect to exactly the bits in \(J_e\).
The graph

\[
                         e\sim f\iff J_e\cap J_f\ne\varnothing
\]

is therefore a valid ordinary dependency graph. The asymmetric condition

\[
  \Pr(B_e)\le x_e\prod_{f\in\Gamma(e)}(1-x_f)
\]

is the standard asymmetric local lemma. The symmetric specialization

\[
                  {\rm e}\,2^{-r}(\Delta+1)\le1
\]

is correct. Also,

\[
 |\Gamma(e)|\le\sum_{i\in J_e}(\lambda_i-1)
\]

is a valid upper bound: a neighbour sharing several phase bits is merely
overcounted. The note intentionally does not claim that failure of an LLL
condition proves infeasibility.

## 4. Connectivity and physical-scope check

Covering a fixed spanning tree certainly makes the selected binary shadow
connected. Conversely, the optional cut formulation is correct because a
finite graph is connected iff every nontrivial cut is crossed.

Neither conclusion implies literal ECO execution. In particular:

1. one ternary atom can shadow three graph edges but has component rank only
   two;
2. a connected two-section may contain a Berge cycle;
3. disjoint physical cuts on one old component may reconnect in a
   nonfaithful interleaving; and
4. owner injectivity is weaker than membership in one residual
   leaf-forest matching.

The common-cube/subsetwise-faithfulness alternatives in Section 6 are
therefore necessary scope guards. They correctly leave residual owner Hall
and private/laminar occurrence routing downstream.

## 5. Repaired-versus-raw ECO scope

The canonical collision-path identity may be used after a repair only if
the repair preserves all six port occurrences and both forced-owner
collision systems; otherwise the collision forest must be recomputed. The
raw \(m=5\) ECO counterexample is not contradicted: its common missing
period-three palettes prevent an upper transversal before phase selection
can close owner alignment. The proved order is only

\[
 \text{repair}\to\text{collision-free phase}
 \to\text{owner Hall}\to\text{private routing}.
\]

No all-\(n\) lower bound on \(\tau(e)\), no compatible ECO hypertree, and no
physical compiler statement is asserted.

