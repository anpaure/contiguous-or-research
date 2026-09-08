# Audit of chronological-upset Hall and adaptive orbit repairs

**Date:** 2026-08-02  
**Audited theorem:**  
`MATH_THEOREM_CHRONOLOGICAL_UPSET_HALL_COMPRESSION_AND_ADAPTIVE_ORBIT_REPAIRS_20260802.md`

**Verdict:** PASS for the upset compression, exposed-root equivalence,
finite Hall obstructions, and K11/K46/K121 static repairs. The all-\(k\)
adaptive Hall statement and every literal serialization consequence remain
unproved exactly as marked.

## 1. Compression and uncrossing

For

\[
 x\preceq_\tau y
 \iff x=y\ \text{or}\ (x\subsetneq y,\ \tau(x)\le\tau(y)),
\]

every right neighbor of \(y\) is also a neighbor of \(x\). Replacing a
selected \(x\) by an omitted \(y\) therefore preserves source cardinality,
cannot enlarge the neighborhood, and strictly raises rank sum. This proves
termination at a chronological upset and certifies that checking only
upsets is an if-and-only-if Hall reduction.

For \(\delta(F)=|F|-|N(F)|\),

\[
 N(A\cup B)=N(A)\cup N(B),\qquad
 N(A\cap B)\subseteq N(A)\cap N(B)
\]

gives supermodularity. Two maximum-deficiency sets therefore have
maximum-deficiency union and intersection. Unioning all symmetry
translates of an upset maximizer produces an invariant upset maximizer.
No integrality or averaging assumption is hidden in this step.

If \(U\) is an upset, every target neighbor lies in \(U\). Hence its target
neighborhood is \(U-R_\tau(U)\), and Hall cancels exactly to

\[
                         |R_\tau(U)|\le|\Gamma_r(U)|.
\]

This verifies the exposed-root formulation and the weak-time inequality in
the upset order.

## 2. Terminal and exchange laws

Applying Hall to the complete top target rank together with
\(F\subseteq{[k]\choose r-2}\) gives

\[
 |F|\le W-{k\choose r-1}+|\Gamma_\tau(F)|.
\]

For odd \(k\), the first two terms cancel. This independently proves the
top-forcing shadow law used in every terminal counterexample.

For a fixed boundary source family, moving top orbit \(p\) later and
\(q\) earlier changes the shadow by

\[
 |p|\,1_{F\cap\operatorname {Pred}(p)\ne\varnothing}
 -
 |q|\,1_{F\cap\operatorname {Pred}(q)\ne\varnothing}.
\]

It is nonnegative for every \(F\) exactly under predecessor-menu
containment and weight dominance. A singleton in the menu difference, or
a common predecessor when the weight inequality is reversed, proves
necessity. The theorem correctly scopes this to one terminal face; it does
not claim a globally safe exchange.

The horizontal-cover identity also replays directly:

\[
 q|F|\le q_+|F|+q|N_{\mathcal B}(F)|.
\]

The covering-design sufficient bound follows because one selected
\((a+1)\)-set contains at most \(a+1\) members of \(F\).

## 3. Fixed-core numerical replay

The exact script

    scratch/audit_fixed_core_nextfit_order_20260802.py

checks the following independent facts.

* K11 ascending binary-mask loads are \(461,457,105\). The principal
  two-core star has mass \(36\) and later top shadow \(34\), giving
  max-flow \(1021/1023\).
* Every decreasing-core tie order has a terminal uncovered singleton and
  deficit at least five. Deliberate one-orbit underfill with a three-edge
  cover has loads \(446,436,141\) and flow \(1023/1023\).
* The compact analytic setwise-core flow independently saturates all
  \(561\) sources below the top rank.
* K41's full staircase has source mass \(827279041974\), target mass
  \(551490893730\), owner mass \(269128937220\), and exact deficit
  \(6659211024\). The dense max-flow cut is exactly the displayed
  staircase.
* K121's ascending-mask staircase has exact deficit
  \(26797240071313150869734178805578123\).

The script implements both the dense product-comparability network and a
sparse Hasse-DAG network. On three K11 audit orders their flow values agree
exactly. In the sparse construction, each source time has its own upward
product DAG; a path reaches exactly the later compatible target types and
owners. Standard path decomposition proves equivalence to the dense type
flow.

For the K121 fresh collar, the eight audited loads sum to
\(\Lambda=2^{120}-1\), every load is at most \(W\), and the sparse network
returns flow \(\Lambda\). The adjacent normalized-Hall cross-product
deficit in the theorem is positive, so global skipping is genuinely
strictly stronger than adjacent uniform coupling.

## 4. Balanced setwise-core replay

The independent script

    scratch/audit_balanced_setwise_core_serpentine_flow_20260802.py

reconstructs the weighted two-dimensional product network. It verifies:

* the unconditional capacity bound
  \(\lceil\Lambda/W\rceil+4\le d+5\);
* the K9 terminal serpent deficit \(4\);
* the K19 monotone deficit \(1125\);
* the separated-top K46 interior deficit \(64633068796\); and
* the adaptive five-orbit K46 menu with full flow
  \(\Lambda=31067656725031\) in four blocks.

The K46 cut has a nonempty later-target neighborhood, so it independently
confirms that terminal aperture is not sufficient.

## 5. Fail-closed boundary

The audit certifies finite static chain factors and exact Hall reductions
only. It proves no adaptive chronology at all \(k\), no bounded carried
sidecar, no literal overlap/Euler host, no endpoint aperture on a common
physical table, no address/history or residence closure, and no
\(\nu(k)\le B(k)+O(1)\) theorem.
