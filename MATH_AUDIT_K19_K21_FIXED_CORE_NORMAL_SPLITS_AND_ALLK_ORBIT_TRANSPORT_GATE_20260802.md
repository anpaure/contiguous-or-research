# Independent audit of the K19/K21 fixed-core splits and all-\(k\) gate

**Date:** 2026-08-02  
**Audited theorem:**  
MATH_THEOREM_K19_K21_FIXED_CORE_NORMAL_SPLITS_AND_ALLK_ORBIT_TRANSPORT_GATE_20260802.md

**Verdict:** PASS for both finite static factors and for the stated
all-\(k\) reductions. The logarithmic-core global Hall flow and literal
serialization remain unproved exactly as marked.

## 1. Orbit lifting

For source type \((s,i)\) and target type \((t,j)\), direct counting gives

\[
\begin{aligned}
 q_{s,i}d^+
 &={h\choose i}{n-h\choose s-i}
   {h-i\choose j-i}
   {n-h-s+i\choose t-j-s+i},\\
 q_{t,j}d^-
 &={h\choose j}{n-h\choose t-j}
   {j\choose i}{t-j\choose s-i}.
\end{aligned}
\]

Both expressions count the same pairs \(S\subset T\), so every compatible
orbit graph is biregular. If type flow \(F_{uv}\) has rows
\(|u||Q|\) and columns \(|v||P|\), spreading \(F_{uv}\) equally over the
literal orbit incidences gives individual marginals \(1/|P|\) and
\(1/|Q|\). Conversely, group-averaging any uniform coupling gives such a
type flow. The quotient/literal equivalence is exact.

## 2. K19 fixed-triple replay

For \(|H|=3\),

\[
 |Y|={16\choose4}=1\,820,\qquad
 |X|={19\choose7}-|Y|=48\,568,
\]

and the three block sizes are

\[
                         92\,363,\quad77\,402,\quad92\,378.
\]

The exact script

    scratch/audit_k19_fixed_triple_normal_split_20260802.py

checks:

* all source and target orbit inventories;
* every supported type arc and the literal left/right degree identity;
* all rows and columns of the closed 28-arc and 8-arc transport
  certificates;
* independent integer max-flow recomputations for all three links,
  including rank9 to rank10 owners.

Its output is

    PASS K19 fixed-triple normalized split
    W=92378 X=48568 Y=1820
    block_sizes=92363,77402,92378 owner_size=92378
    AB_nonzero_type_arcs=28
    BC_nonzero_type_arcs=8
    independent_type_maxflows=AB,BC,CD

The first coupling is correctly used only for LYM: since
\(92\,363>77\,402\), it is not an injection. Dilworth supplies the integral
chain partition after the width proof. Here Dilworth is applied to the
explicit auxiliary poset \(\mathsf Q(P_0,P_1,P_2)\): each block is declared
an antichain, and exactly the cross-block containment relations (including
\(P_0\to P_2\)) are retained. The audited couplings use only
\(P_0\to P_1\) and \(P_1\to P_2\) relations of this poset. Consequently a
Dilworth chain has at most one element from each of the three blocks and
is a genuine Boolean inclusion chain. This repairs the otherwise invalid
inference from "three compressed levels" when \(P_0\) itself contains
several ordinary ranks.

## 3. K21 single-orbit replay

For \(|H|=8\) and \(Y=\mathcal O_{8,4}\),

\[
 |Y|={8\choose4}{13\choose4}=50\,050,
\]

inside the required interval \([49\,213,58\,786]\). The block sizes are

\[
                         351\,879,\quad343\,980,\quad352\,716.
\]

The exact script

    scratch/audit_k21_single_orbit_normal_split_20260802.py

checks both transports twice:

1. by an independent integer Dinic computation; and
2. by every weighted interval-Hall cut.

For \(A\to B\), after division by \(39\), the minimum slacks by target
interval length are

\[
\begin{split}
&(108473,\ 4750697,\ 54282865,\ 228843545,\ 449490965,\\
&\hspace{12mm}561723932,\ 251016788,\ 87408692,\
31370107,\ 0).
\end{split}
\]

For \(B\to C\), after division by \(14196\), they are

\[
 (1567,\ 41503,\ 327635,\ 521752,\ 285516,\
   141988,\ 24772,\ 10835,\ 0).
\]

Only the full interval is tight. The independent total flows are exactly

\[
\begin{aligned}
 |A||B|&=121\,039\,338\,420,\\
 |B||C|&=121\,327\,249\,680.
\end{aligned}
\]

The script reports PASS, including the owner link. This proves K21 static
depth three after applying Dilworth to
\(\mathsf Q(A,B,C)\), not to the induced Boolean subposet: the auxiliary
layers are antichains, all cross-layer relations are containments, and the
audited couplings lie on its adjacent relations. Direct evaluation shows
the odd depth-three range is exactly
\(k=11,13,15,17,19,21\); the first four have separated whole-rank
compressions. Thus the claimed phase closure is sound.

The principal-star negative statement also replays. At K21 the shift
window is \([49\,213,58\,786]\), while the eight principal-star sizes are

\[
 77\,520,\ 27\,132,\ 8\,568,\ 2\,380,\ 560,\ 105,\ 14,\ 1.
\]

None lies in the window.

## 4. Rank quotient and normalized-coupling separation

Cyclically distributing the increasing stream of rank tokens among \(W\)
columns gives exactly \(\lfloor\Lambda/W\rfloor\) or
\(\lceil\Lambda/W\rceil\) tokens per column and never repeats a rank in one
column. This proves the rank-quotient path theorem.

It does not prove normalized row coupling. At K6, the two right-aligned
rows have rank laws

\[
 \delta_1,\qquad {5\over20}\delta_1+{15\over20}\delta_2.
\]

The first is not stochastically below the second, since its probability of
rank at least two is zero on the source requirement but a strict nested
coupling from rank one would require target rank at least two with
probability one. Equivalently, the target provides only \(15/20\). This
checks the theorem's distinction between ordinary path injection and
uniform normalized coupling.

## 5. Fixed-core capacity reduction

Every pointwise-core orbit has size at most

\[
 M_h={k-h\choose\lfloor(k-h)/2\rfloor}.
\]

Next-fit closes a block only after its load exceeds \(W-M_h\). Therefore
at least \(d+2\) blocks would imply

\[
 \Lambda>(d+1)(W-M_h).
\]

Under \((d+1)M_h\le W-\binom{d+1}{2}\), this contradicts
\(\Lambda\le dW+\binom{d+1}{2}\). The asymptotic estimate

\[
 M_h/W=(1+o(1))2^{-h}\sqrt{k/(k-h)}
\]

with \(h=\lceil\log_2(8(d+1))\rceil\) verifies the polynomial
\(O(k^{3/2})\)-type reduction for all sufficiently large \(k\). Singleton
orbits handle the finite exceptions.

## 6. Global orbit Hall

The bipartite fixed-chronology formulation is exact. A matching saturating
every target-left-copy gives a directed graph with target outdegree one,
right indegree at most one, and strictly increasing time on target arcs.
It is therefore a disjoint path family ending at distinct owners.

For pointwise-core orbits \((A,j)\), an allowed target-type arc is exactly

\[
 \tau(A,j)<\tau(B,\ell),\qquad A\subseteq B,\qquad j\le\ell.
\]

Averaging a matching proves necessity of the type flow. Conversely,
biregular lifting gives a fractional literal matching from any feasible
type flow, and bipartite integrality gives an integral matching. Hence the
global product-order flow is an if-and-only-if static criterion and is
strictly weaker than adjacent normalized couplings.

## 7. Fail-closed boundary

The audit proves no all-\(k\) flow feasibility. The exact surviving static
statement is:

> **UNPROVED.** Some adaptive choice of within-rank orbit order, underfill,
> or refinement with only \(d+O(1)\) blocks has a saturating global
> product-order type flow.

The capacity chronology does not canonically specify its within-rank tie
order. Subsequent exact Hall cuts refute several fixed choices, including
ascending binary-mask order; this does not refute the adaptive existential
clause.

An all-\(k\) depth-\(d+C\) factor would imply a minimum Boolean-lattice
chain decomposition with maximum below the average by at most the stated
additive \(2C+3\) allowance. No such theorem is inferred from the finite
cases.

Literal overlap/Euler balance, endpoint aperture, global address/history,
residence, upper/common-cap/compiler closure, and regenerative linkage are
all outside this audit.
