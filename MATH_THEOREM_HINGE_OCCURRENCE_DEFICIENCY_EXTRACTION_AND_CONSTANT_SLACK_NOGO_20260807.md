# Hinge collisions may be discarded by occurrence deficiency, but constant reservoir slack alone cannot do it

**Date:** 2026-08-07  
**Method:** maximum-matching deficiency, collision energy, and a first-moment
counterexample with an injective base row  
**Status:** unconditional abstract extraction and no-go theorems.  They
formalize exactly how complete all-depth target-disjointness can be weakened
in the merged PBBS rechainization ledger.  Applying the positive theorem to
literal hinges still requires a mode-consistent occurrence graph and a
proof of its Hall deficiency bound.

## 1. The rechainization scale

Use the odd triangular notation

\[
 W={2m+1\choose m},\qquad
 h=(\theta+o(1))W,
 \qquad
 \theta=4\sum_{a\ge1}e^{-4\pi a^2}.                    \tag{1.1}
\]

The single-bulge reservoir has endpoint capacity

\[
                         N=(\rho+o(1))W,qquad
 \rho=e^{-\pi},                                         \tag{1.2}
\]

so \(\rho/\theta>3000\).  Every productive endpoint exports \(d\)
named lower cells in the zero-charge ledger.  Complete target-disjointness
of all exported cells is sufficient, but it is stronger than necessary:
we may discard candidate endpoints whose cells cannot be integrated into
the residual PBBS target matching.

The right abstraction is an occurrence graph.  Let \(E\) be \(N\)
candidate endpoints and let

\[
                         \mathcal S=E\times[d]            \tag{1.3}
\]

be their logical lower slots.  Let \(\mathcal T\) be the named target bank
released by the rechainization, with ranks kept as types.  Join a slot to
every named target that it may legally carry in the same literal phase,
envelope and compiler state.  Call the resulting bipartite graph \(G\).

There is one essential scope condition.

> **Simultaneous mode consistency.**  Whenever a matching saturates all
> \(d\) slots in each endpoint of a family \(E'\subseteq E\), those
> incidences can be realized simultaneously by legal endpoint modes (one
> bridge permutation, occurrence state and pin state per endpoint), with
> every shared ring and compiler resource respected.

For fixed literal occurrence values this is automatic because the lists
are singletons.  For bridge menus it is a separate product-closure theorem;
independent row menus must not be silently substituted for it.

## 2. Exact deficiency extraction

Define the Hall deficiency of the occurrence graph by

\[
 \delta(G)=|\mathcal S|-\nu(G)
 =\max_{X\subseteq\mathcal S}\bigl(|X|-|N_G(X)|\bigr),  \tag{2.1}
\]

where \(\nu(G)\) is the maximum matching size.  The equality is the usual
deficiency form of Hall's theorem.

### Theorem 2.1 (endpoint extraction from one global matching)

Assume mode consistency.  The graph \(G\) contains a target-disjoint bank
of at least

\[
                         \boxed{N-\delta(G)}             \tag{2.2}
\]

complete endpoints.

Consequently, the theta demand is met whenever

\[
                         \boxed{\delta(G)\le N-h.}       \tag{2.3}
\]

#### Proof

Take a maximum matching.  It leaves exactly \(\delta(G)\) slots
unmatched.  Every incomplete endpoint contains at least one unmatched
slot, so at most \(\delta(G)\) endpoints are incomplete.  Keep the other
endpoints and discard every matching edge incident with an incomplete one.
All slots of each retained endpoint remain matched to distinct named
targets, and mode consistency makes each retained block literal.  This
proves (2.2), and (2.3) implies \(N-\delta(G)\ge h\). \(\square\)

The allowed deficiency in (2.3) is enormous:

\[
                         N-h=(\rho-\theta+o(1))W.        \tag{2.4}
\]

Thus the all-depth occurrence matching need not be perfect.  It may lose
almost one slot in each discarded candidate endpoint and still leave the
required theta bank.

### Corollary 2.2 (atomic-ring version)

Suppose endpoints occur in rings of \(L\) endpoints and a ring must be
kept or discarded as a whole.  If there are \(R=N/L\) rings, then a
maximum matching leaves at least \(R-\delta(G)\) completely matched rings.
Hence \(h\) endpoints in complete rings are guaranteed by

\[
                         \delta(G)\le {N-h\over L}.       \tag{2.5}
\]

#### Proof

Every incomplete ring contains at least one unmatched slot.  Therefore at
most \(\delta(G)\) rings are incomplete. \(\square\)

For a length-\(3d\) hinge ring, \(L=3d\).  This shows why permission to
use productive endpoints individually, filling the other ring positions
from the residual chart, is mathematically valuable: ring-atomic
extraction makes the same matching deficiency cost a factor \(3d\) more.

### Corollary 2.3 (capacity-faithful PBBS linkage form)

Let \(\Gamma\) be a directed occurrence network whose sources are the
slots \(\mathcal S\) and whose sinks are distinct released target tickets.
The network may include retained PBBS cells and alternating recourse arcs.
Let

\[
 r_\Gamma(\mathcal S)
 =\max\{\text{number of pairwise vertex-disjoint source--sink paths}\}
 =|\mathcal S|-\delta_\Gamma.                            \tag{2.6}
\]

If every completely linked endpoint has a consistent literal mode, then
at least \(N-\delta_\Gamma\) endpoints can be retained.  In particular,
\(\delta_\Gamma\le N-h\) suffices for the theta bank.

#### Proof

Choose a maximum disjoint linkage.  It leaves exactly \(\delta_\Gamma\)
sources unlinked.  Hence at most \(\delta_\Gamma\) endpoint blocks contain
an unlinked source.  Keep the other blocks and their paths. \(\square\)

This is the proof-safe way to incorporate the residual PBBS factor.  A raw
edge saying that a target is set-theoretically compatible with a cell is
not enough: shared alternating interiors and common-cap capacities must be
represented inside \(\Gamma\).  Equivalently, one may use the strict
gammoid rank function \(r_\Gamma(X)\) and its all-cut deficiency

\[
                         \max_{X\subseteq\mathcal S}
                         (|X|-r_\Gamma(X)).              \tag{2.7}
\]

Separate row matchings do not establish (2.6).

## 3. A second-moment sufficient condition for fixed profiles

There is a simpler sufficient theorem when every endpoint already has one
fixed complete target profile.  Let \(C_e\subseteq\mathcal T\) be that
profile and make the conflict graph \(K\) on \(E\), joining \(e,f\) when

\[
                         C_e\cap C_f\ne\varnothing.       \tag{3.1}
\]

For a target \(T\), put

\[
                         m_T=|\{e:T\in C_e\}|,
 \qquad
 \mathcal E_2=\sum_T{m_T\choose2}.                       \tag{3.2}
\]

### Theorem 3.1 (collision-energy extraction)

There is a completely target-disjoint endpoint family of size at least

\[
                         \boxed{{N^2\over N+2\mathcal E_2}.} \tag{3.3}
\]

In particular, a theta-sized family exists if

\[
 \boxed{
 \mathcal E_2\le {1\over2}
 \left({N^2\over h}-N\right).}                           \tag{3.4}
\]

At the scales (1.1)--(1.2), the right side is

\[
 {1\over2}
 \left({\rho^2\over\theta}-\rho+o(1)\right)W.           \tag{3.5}
\]

#### Proof

Every edge of the conflict graph is counted at least once in
\(\mathcal E_2\), so \(e(K)\le\mathcal E_2\).  The standard greedy/Turán
bound gives

\[
 \alpha(K)\ge {N^2\over N+2e(K)}
              \ge {N^2\over N+2\mathcal E_2}.
\]

An independent set in \(K\) has disjoint profiles.  Rearranging the
condition that (3.3) be at least \(h\) gives (3.4). \(\square\)

This theorem permits many collisions, provided their total pair energy is
only \(O(W)\).  It is often much easier to audit than complete
target-disjointness.  It is not, however, a consequence of the base-row
cardinality margin.

## 4. Constant-factor reservoir slack does not control all-depth collisions

We now give a sharp abstract no-go.  It already has a perfectly injective
base row and unbiased higher rows.

### Theorem 4.1 (independent-row no-go)

Fix constants \(0<\theta<\rho<1\).  Let

\[
                         N=\lfloor\rho W\rfloor,
 \qquad                  h=\lceil\theta W\rceil.         \tag{4.1}
\]

For every sufficiently large number of rows \(p\), and all sufficiently
large \(W\), there is a probability distribution on systems of \(N\)
endpoint profiles such that

1. the base-row targets are always all distinct;
2. every later endpoint-row target has an exactly uniform one-point
   marginal on a fresh \(W\)-element layer; and
3. with positive probability the sampled system has no \(h\) profiles
   target-disjoint in all \(p\) rows.

In particular, a deterministic bad realization exists.

Thus even a reservoir ratio \(\rho/\theta>3000\), an injective base row,
and perfectly uniform one-point higher marginals do not force a
theta-sized all-depth packing when the rows have no correlation.  The
claim concerns uniform marginals of the sampling law, not exact empirical
balance in the resulting deterministic bad realization.

#### Proof

Give the \(N\) profiles distinct base targets.  In each of the remaining
\(p-1\) rows, independently assign every endpoint a uniformly random
target from a fresh \(W\)-element layer.

Fix an \(h\)-subset of endpoints.  In one random row, the probability
that its targets are all distinct is

\[
 { (W)_h\over W^h}
 =\prod_{i=0}^{h-1}\left(1-{i\over W}\right)
 \le\exp\left(-{h(h-1)\over2W}\right).                  \tag{4.2}
\]

The rows are independent.  Hence the expected number \(Z\) of
all-row-disjoint \(h\)-subsets satisfies

\[
 \begin{aligned}
 \mathbb EZ
 &\le {N\choose h}
 \exp\left(-{(p-1)h(h-1)\over2W}\right)\\
 &\le
 \exp\left(
 N\log{eN\over h}
 -{(p-1)h(h-1)\over2W}
 \right).                                                \tag{4.3}
 \end{aligned}
\]

The positive term is

\[
 (\rho\log(e\rho/\theta)+o(1))W,
\]

whereas the negative term is

\[
 -\left({(p-1)\theta^2\over2}+o(1)\right)W.
\]

Choose

\[
                         p-1>{2\rho\log(e\rho/\theta)\over\theta^2}.
\tag{4.4}
\]

Then \(\mathbb EZ<1\) for large \(W\), so some realization has \(Z=0\).
Every endpoint marginal in every random row is uniform in the sampling
law by construction.
\(\square\)

For the hinge problem \(p=d\to\infty\), so (4.4) eventually applies.
The theorem does not model the highly correlated nested hinge rows; that
is precisely its point.  A proof which uses only the constant reservoir
ratio and separate uniform row marginals cannot distinguish the true hinge
from this counterexample and therefore cannot succeed.

## 5. The singleton top row is an exact support obstruction

The terminal bridge menu supplies an especially transparent instance.
Let \(\tau:E\to\mathcal T_{\rm top}\) be the forced top map.  If only
that row is considered, the largest injective subfamily has size exactly

\[
                         \boxed{|\tau(E)|}.              \tag{5.1}
\]

Equivalently, its slot-target graph has deficiency

\[
                         \boxed{N-|\tau(E)|}.            \tag{5.2}
\]

Therefore the top row alone permits theta extraction if and only if

\[
                         |\tau(E)|\ge h.                 \tag{5.3}
\]

The two-ring obstruction in
`MATH_THEOREM_SHARED_H_TOP_MAP_OBSTRUCTION_AFTER_TWO_ROW_PACKING_20260807.md`
shows that complete base and first-successor rows do not imply even local
top injectivity.  More generally, base-star disjointness does not bound a
top fibre by an absolute constant: inside a fixed rank-\((s+d)\) target
\(T\), fix \(b\in T\), and choose a Johnson-distance-at-least-two code of
rank-\((s-1)\) centres

\[
                         P_i\subset T-\{b\}.
\]

Put \(A_i=P_i+b\), \(H_i=T-A_i\), and use the same
\((3d-1)\)-set of private labels outside \(T\), together with \(b\), in
every ring.  If two complete base targets were equal, say
\(P_i+f=P_j+g\), then \(P_i,P_j\) would be distinct rank-\((s-1)\)
subsets of one rank-\(s\) set and hence have Johnson distance at most one,
a contradiction.  Nevertheless every distinguished age-one endpoint has
top value

\[
                         A_i\cup H_i=T.
\]

A greedy code in \({T-b\choose s-1}\) has size at least

\[
 { {s+d-1\choose s-1}\over1+(s-1)d},                    \tag{5.4}
\]

which is unbounded.  Thus base-star disjointness gives no absolute bound
on a top fibre.  A global support theorem must use distribution across
different top targets, not merely the local base packing.

## 6. Exact revised target

Complete all-depth target-disjointness of the whole reservoir is stronger
than necessary.  The positive replacement is the occurrence-deficiency
bound

\[
                         \boxed{\delta(G)\le N-h,}       \tag{6.1}
\]

together with mode consistency and residual-PBBS compatibility.  For
fixed profiles, the checkable collision-energy condition (3.4) is a
sufficient substitute.

But neither (6.1) nor (3.4) follows from:

* the \(3000\)-fold base-row capacity;
* separate rank counts;
* uniform one-target marginals; or
* complete disjointness in any fixed number of bottom rows.

Theorem 4.1 rules out precisely that shortcut, while the forced top map
gives the first literal Hall cut.  The remaining mathematical theorem can
therefore be weakened from

> pack the entire hinge reservoir target-disjointly

to

> build one mode-consistent hinge/PBBS occurrence graph whose Hall
> deficiency is at most \((\rho-\theta+o(1))W\), and whose terminal top
> support has size at least \((\theta+o(1))W\).

This is genuinely weaker, but it still requires an all-depth correlated
expansion theorem; constant-factor reservoir slack alone cannot replace
it.
