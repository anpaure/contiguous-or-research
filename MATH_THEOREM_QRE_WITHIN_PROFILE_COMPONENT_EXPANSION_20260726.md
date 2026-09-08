# QRE: exact all-subsets expansion inside one diffuse ordered profile

Date: 2026-07-26

Method: pure mathematics only. No computation, solver, or web input is
used.

## 0. Result

Partition the core coordinates into blocks

\[
 B_j=A_j\mathbin{\dot\cup}C_j,qquad |A_j|=|C_j|=d,
\tag{0.1}
\]

and choose an arbitrary rank-dependent bijection

\[
                         \pi_{j,k}:A_j\longrightarrow C_j.
\tag{0.2}
\]

Randomness and independence will not be needed below.  Fix

\[
                         q=A\sqrt m+O(1),            \tag{0.3}
\]

and one safe ordered lower half-count profile

\[
 \tau=((a_j,c_j))_{j\le b},qquad
 {d\over4}\le a_j,c_j\le {3d\over4}.               \tag{0.4}
\]

Call it **lower diffuse** if at least \(q\) blocks satisfy

\[
                         a_j+c_j\le d.              \tag{0.5}
\]

Choose any \(q\) such blocks and call their set \(J\).  In each
\(j\in J\), use the source-rank matching
\(\pi_{j,a_j+c_j+1}\), and add one endpoint of an edge empty in the
target.  Leave every other block unchanged.  This defines a literal
subgraph of the maximal lower compatibility graph.

### Theorem 0.1 (within-profile raw expansion)

There is an absolute \(c>0\) and a family
\(\mathcal E_\tau^-\subseteq\tau\) such that

\[
 { |\mathcal E_\tau^-|\over|\tau|}
 \le 2q e^{-cd},                                    \tag{0.6}
\]

and, for every raw, arbitrarily block-labelled family

\[
                 \mathcal A\subseteq\tau\setminus\mathcal E_\tau^-,
\]

\[
 \boxed{
 |N_{G_q^-}(\mathcal A)|
 \ge \left({3\over2}\right)^q|\mathcal A|.}        \tag{0.7}
\]

The upper analogue holds for every safe ordered upper profile having at
least \(q\) blocks with \(a_j+c_j\ge d\).  In those blocks use
\(\pi_{j,a_j+c_j-1}\) and remove one endpoint of a full edge.  There is
an exceptional family of the same relative size, and

\[
 \boxed{
 |N_{G_q^+}(\mathcal A)|
 \ge \left({3\over2}\right)^q|\mathcal A|}          \tag{0.8}
\]

for every remaining subfamily.

All but \(o(N_q)\) lower and upper targets lie in safe diffuse ordered
profiles when \(d\to\infty\), \(q=o(m/d)\), and
\((m/d)e^{-c_0d}=o(1)\) for a sufficiently small absolute \(c_0\).

Thus no \(\Omega(W)\) raw Hall counter-cut can be supported inside one
retained diffuse ordered profile.  Any counter-cut to `QRE_A` must combine
many ordered profiles and exploit overlap of their middle-source
neighborhoods.  The theorem does not solve that cross-profile capacity
problem, and it says nothing about selected packet axes or chronology.

## 1. One lower block

Fix one selected lower block and abbreviate

\[
                         a=a_j,qquad c=c_j,qquad t=a+c\le d.
\tag{1.1}
\]

Use the matching \(M=\pi_{j,t+1}\).  If a target has \(f\) full
\(M\)-edges, then its status counts are

\[
 p=a-f,qquad s=c-f,qquad z=d-a-c+f,                \tag{1.2}
\]

where \(p,s,z\) are respectively the numbers of \(A\)-single,
\(C\)-single, and empty edges.

Fix the *set* \(F\) of full edges.  Lower promotion never changes \(F\),
so different \(F\)'s give disjoint source components.  Inside the
\(F\)-component there are two disjoint source shores.

* Adding the \(A\)-endpoint of an empty edge gives a bipartite graph of
  target degree \(z\) and reverse source degree \(p+1\).  Its normalized
  expansion factor is

  \[
                             R_A^-={z\over p+1}.      \tag{1.3}
  \]

* Adding the \(C\)-endpoint gives target degree \(z\), reverse degree
  \(s+1\), and factor

  \[
                             R_C^-={z\over s+1}.      \tag{1.4}
  \]

The two source shores have different ordered half counts and hence are
disjoint.  Consequently, for every subfamily \(\mathcal D\) of the
\(F\)-component,

\[
 |N_A(\mathcal D)\mathbin{\dot\cup}N_C(\mathcal D)|
 \ge R^-(f)|\mathcal D|,                            \tag{1.5}
\]

where

\[
 \boxed{
 R^-(f)
 =z\left({1\over a-f+1}+{1\over c-f+1}\right).}     \tag{1.6}
\]

Indeed, (1.3) follows simply by counting edges out of \(\mathcal D\):
\(z|\mathcal D|\le(p+1)|N_A(\mathcal D)|\).  The other shore is
identical.

For a uniformly chosen local target with fixed half counts \(a,c\), the
full-edge count relative to every fixed matching has the exact law

\[
                         F\sim\operatorname{Hyp}(d,c,a),qquad
 \mathbb EF={ac\over d}.                            \tag{1.7}
\]

Put \(x=a/d\), \(y=c/d\), and \(u=f/d\).  At the mean \(u=xy\), the
large-\(d\) form of (1.6) is

\[
 (1-x-y+xy)\left({1\over x-xy}+{1\over y-xy}\right)
 ={1-x\over x}+{1-y\over y}.                       \tag{1.8}
\]

On the compact region

\[
 {1\over4}\le x,y\le{3\over4},qquad x+y\le1,      \tag{1.9}
\]

the right side of (1.8) is at least \(2\).  All denominators stay
bounded away from zero.  Uniform continuity therefore supplies absolute
\(\varepsilon,c>0\) such that, for all sufficiently large \(d\),

\[
 |F-ac/d|\le\varepsilon d
 \quad\Longrightarrow\quad R^-(F)\ge {3\over2},     \tag{1.10}
\]

whereas the hypergeometric tail bound gives

\[
 \Pr\{|F-ac/d|>\varepsilon d\}\le2e^{-cd}.          \tag{1.11}
\]

Nothing in (1.7)--(1.11) depends on the identity or randomness of the
matching.

## 2. Tensoring the selected lower blocks

In every block outside \(J\), target and source are identical.  Fixing
that exact exterior configuration separates the graph into disjoint
components.  In each block \(j\in J\), also fix its full-edge set
\(F_j\).  The resulting global component is a tensor product of the
local components from Section 1.

For a side word \(\sigma\in\{A,C\}^J\), keep only the promotion shore
specified by \(\sigma_j\) in every selected block.  This product graph is
biregular, and edge counting gives expansion factor

\[
                         \prod_{j\in J}R^-_{\sigma_j}(F_j).
\tag{2.1}
\]

Distinct side words produce distinct ordered source half-count profiles,
so their source neighborhoods are pairwise disjoint.  Summing (2.1) over
all side words yields, for every subfamily (mathcal D) of the global
component,

\[
 |N(\mathcal D)|
 \ge\prod_{j\in J}\bigl(R_A^-(F_j)+R_C^-(F_j)\bigr)
            |\mathcal D|
 =\prod_{j\in J}R^-(F_j)|\mathcal D|.               \tag{2.2}
\]

Call a component good when every factor in (2.2) is at least \(3/2\).
The uniform measure on one ordered profile is a product of the uniform
local half-count measures.  Thus the \(F_j\)'s are independent and
(1.11), followed by a union bound, gives

\[
 \Pr\{\text{the target lies in a bad component}\}
 \le2q e^{-cd}.                                     \tag{2.3}
\]

Delete precisely the bad components.  Different good components have
disjoint source neighborhoods, because their exterior configurations or
their full-edge sets differ.  Summing (2.2) over an arbitrary family
spread among good components proves (0.6)--(0.7).

Every used edge is literal: in block \(j\), the source has rank \(t+1\),
the matching is exactly \(\pi_{j,t+1}\), and deleting the added singleton
endpoint recovers the target.  Exactly one coordinate is added in every
one of \(q\) blocks, so every source has middle rank.

## 3. The upper sign

Fix an upper block with \(t=a+c\ge d\), and use the source-rank matching
\(M=\pi_{j,t-1}\).  If an upper target has \(f\) full, \(p=a-f\)
\(A\)-single, \(s=c-f\) \(C\)-single, and \(z\) empty edges, then removing
one endpoint from a full edge leaves \(z\) unchanged.  Hence components
are indexed by the exact empty-edge set.

Removing the \(C\)-endpoint leaves an \(A\)-single edge; the resulting
shore has target degree \(f\), reverse degree \(p+1\), and factor
\(f/(p+1)\).  Removing the \(A\)-endpoint gives factor \(f/(s+1)\).
The two source half-count profiles are disjoint, so the local union has

\[
 \boxed{
 R^+(f)=f\left({1\over a-f+1}+{1\over c-f+1}\right).}          \tag{3.1}
\]

Again \(F\sim\operatorname{Hyp}(d,c,a)\).  At \(F/d=xy\), the scaled
version of (3.1) is

\[
 {y\over1-y}+{x\over1-x}.                          \tag{3.2}
\]

On the safe compact region \(x+y\ge1\), (3.2) is at least \(2\).
The same continuity and hypergeometric-tail argument shows that

\[
                         R^+(F)\ge {3\over2}         \tag{3.3}
\]

outside a family of relative mass at most \(2e^{-cd}\).  Tensoring any
\(q\) above-center blocks proves (0.8), exactly as in Section 2.

## 4. Diffuse profiles have full asymptotic mass

It remains to justify that the availability of (q) selected blocks is
not an additional macroscopic quarantine.

Under an independent Bernoulli law of density
\(p=(m-q)/(2m)<1/2\), the block ranks are independent
\(\operatorname{Bin}(2d,p)\) variables and

\[
                         \Pr\{|T\cap B_j|\le d\}\ge c_1       \tag{4.1}
\]

for an absolute \(c_1>0\).  A Chernoff bound therefore shows that fewer
than \(c_1b/2\) below-center blocks has probability \(e^{-\Omega(b)}\).
Conditioning on total rank \(m-q\) costs only the reciprocal of a central
binomial probability, \(O(\sqrt m)\).  Since

\[
                         q=o(b),                    \tag{4.2}
\]

the lower profile is diffuse with probability \(1-o(1)\).

For upper targets use density \(p=(m+q)/(2m)>1/2\) and the event
\(|U\cap B_j|\ge d\).  The same proof applies.  Half-count safety fails
with probability at most

\[
                         O((m/d)e^{-c_0d})=o(1).     \tag{4.3}
\]

Residual coordinates merely fix one additional fibre and change the
conditioning rank by \(O(d)\); the same estimates are uniform in all but
an \(o(N_q)\) collection of residual fibres.

## 5. Exact boundary

Proved:

1. after deleting \(o(1)\) of any diffuse safe ordered profile, **every**
   raw subfamily inside that profile has expansion at least
   \((3/2)^q\) in the maximal graph;
2. this holds for arbitrary rank-matching arrays, not only independent
   random ones;
3. both signs are covered by literal source-rank matchings; and
4. nondiffuse or unsafe profiles contain only \(o(N_q)\) targets.

Not proved:

1. simultaneous capacity across different ordered target profiles;
2. `QRE_A` for a raw family mixing profiles;
3. a source-normalized two-step flow with owner load at most one;
4. selected-axis survival or packet chronology.

The raw-cut gate has therefore narrowed: within-profile block labels are
not an obstruction.  The only remaining maximal-graph obstruction is
cross-profile competition for the same middle owners.
