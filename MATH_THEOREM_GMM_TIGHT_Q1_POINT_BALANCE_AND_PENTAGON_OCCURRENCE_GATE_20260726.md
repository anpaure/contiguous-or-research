# The GMM tight \(q=1\) Hamilton cycle: exact point balance and the pentagon-occurrence gate

Date: 2026-07-26

Method: pure mathematics only.  The GMM tight-enumeration theorem is used
through its exact contraction to a full-owner lower-complete Hamilton
cycle.  No marginal probabilities are multiplied.

## 0. Outcome

Let \(n\in\{2m,2m+1\}\), and write

\[
 \mathcal L=\binom{[n]}{m-1},\qquad
 \mathcal M=\binom{[n]}m,\qquad
 \mathcal U=\binom{[n]}{m+1},
 \tag{0.1}
\]
\[
 W=|\mathcal M|,\qquad N_-=|\mathcal L|,
 \qquad E=W-N_-.
 \tag{0.2}
\]

A tight enumeration of the two levels \(m-1,m\) contracts to a Hamilton
cycle \(C\) of \(J(n,m)\) on all \(W\) middle owners.  Its lower load
\(\ell\) has no holes, so

\[
 \ell(S)=1+h(S),\qquad h(S)\in\mathbb Z_{\ge0},
 \qquad \sum_{S\in\mathcal L}h(S)=E.                 \tag{0.3}
\]

Let \(u(U)\) be the upper-union load of \(C\), and put

\[
 R^+(C)=\sum_{U\in\mathcal U}(u(U)-1)_+,\qquad
 M^+(C)=\#\{U:u(U)=0\}.                              \tag{0.4}
\]

The exact results are as follows.

1. **The owner point margins are already perfect.**  For every
coordinate \(v\),
\[
 \boxed{
 |\{X\in\mathcal M:v\in X\}|=\binom{n-1}{m-1}.}      \tag{0.5}
\]
This is independent of the Hamilton ordering and cannot be improved by
relabeling.

2. The upper point margins are determined exactly by the small lower
excess \(h\):
\[
 \boxed{
 P_{m+1}u
 =2\binom{n-1}{m-1}\mathbf1
  -P_{m-1}(\mathbf1+h).}                             \tag{0.6}
\]

3. On even ground \(n=2m\), put
\[
                         h_v=\sum_{S\ni v}h(S).
\]
Then
\[
 \boxed{
 P_{m+1}(u-\mathbf1)=
       (E-h_v)_{v\in[2m]}.}                          \tag{0.7}
\]
For every possible \(h\), there exists an integral nonnegative upper
excess vector \(g\) of mass \(E\) such that
\[
 P_{m+1}g=(E-h_v)_v.                                 \tag{0.8}
\]
Hence the upper load \(\mathbf1+g\) covers every upper target and has
exactly the point margins forced by \(C\).  The point invariant therefore
creates no obstruction at all at the load-vector level.

4. On odd ground \(n=2m+1\), put
\[
 \eta={E(m-1)\over2m+1}\in\mathbb Z.
\]
Then
\[
 \boxed{
 P_{m+1}(u-\mathbf1)=
       (\eta-h_v)_{v\in[2m+1]}.}                     \tag{0.9}
\]
Exact upper rainbowness requires the repeated-lower family to be
point-regular, \(h_v=\eta\).  Without that regularity, the complete point
discrepancy still satisfies
\[
 \sum_v|\eta-h_v|\le2(m-1)E=O(W),                   \tag{0.10}
\]
so its normalized repeat lower bound is only \(O(W/m)=o(W)\).  Thus point
margins do not obstruct the asymptotic \(q=1\) target on either ground.

5. The GMM word “tight” supplies no hidden local pentagon structure.
Conversely, every Hamilton Johnson cycle with complete lower support
expands to a tight enumeration.  Therefore positive-density occurrence of
the complemented six-coordinate pentagon is an additional prescribed-
forest theorem, not a consequence of tightness.

6. Fix a six-set \(D\).  Its rank-three fibres
\[
 \mathcal F_K=\{K\cup A:A\in\tbinom D3\},
 \qquad K\in\tbinom{[n]\setminus D}{m-3},             \tag{0.11}
\]
form a disjoint bank of
\[
 F=\binom{n-6}{m-3}
   =\left({1\over64}+o(1)\right)W                    \tag{0.12}
\]
potential pentagons.  If \(I_D(C)\) is the number of cycle edges internal
to these rank-three fibres, then every eligible pentagon consumes fifteen
such edges and
\[
 \boxed{
 g_D(C)\le {I_D(C)\over15}.}                         \tag{0.13}
\]

7. Averaging over all six-sets gives the exact identity
\[
 \boxed{
 \sum_{D\in\tbinom{[n]}6}I_D(C)
 =W\binom{m-1}{2}\binom{n-m-1}{2}.}                  \tag{0.14}
\]
Consequently a uniformly relabelled fixed six-coordinate bank has
\[
 \mathbb E_D g_D(C)
 \le\left({3\over16}+o(1)\right){W\over m^2}.         \tag{0.15}
\]
Thus random relabeling misses the required positive-density supply by a
factor \(\Theta(m^2)\).  A successful choice of \(D\) must be a highly
structured exceptional frame.

8. If one fixed bank contains \(k\) eligible descending pentagons, their
owner and upper-target supports are mutually disjoint, so all \(k\)
switches may be performed simultaneously.  They preserve Hamiltonicity
and the complete lower load, and reduce upper repeat excess by the sum of
their exact local descent scores.  In particular, margin-one descent in
each copy reduces \(R^+\) by at least \(k\).

9. There are two exact statewise obstructions to this route:

   * if upper repeats and holes have Johnson distance at least three, no
     complemented pentagon descends;
   * if no six-set has \(g_D(C)=\Omega(W)\), no fixed-frame pentagon bank
     has positive density.

No \(q=1\) two-sided Hamilton cycle is claimed.  The owner-margin gate is
closed positively; the sole remaining issue in this lane is a structured
Hamilton completion containing a positive-density, defect-aligned
pentagon forest, or a larger-diameter trade atlas.

## 1. Full-owner contraction and the lower excess

Let a tight cyclic enumeration contain every member of
\(\mathcal L\cup\mathcal M\).  Contract every lower vertex between its
two incident middle supersets.  The tightness calculation gives a
Hamilton cycle \(C\) on all \(W\) middle owners.  Exactly \(N_-\) cycle
edges arise from contracted lower vertices and exactly
\[
                         E=W-N_-                     \tag{1.1}
\]
are direct middle-to-middle transitions.

Every lower target occurs on its contracted edge.  The \(E\) direct edges
may repeat lower colours, giving (0.3).  No assertion about which
\(h(S)\)'s are nonzero follows from tightness.

The upper load has total mass
\[
                         \sum_{U\in\mathcal U}u(U)=W.           \tag{1.2}
\]
Therefore
\[
 \boxed{
 M^+(C)=|\mathcal U|-W+R^+(C).}                     \tag{1.3}
\]
For even ground this is
\[
                         M^+(C)=R^+(C)-E,             \tag{1.4}
\]
while for odd ground it is
\[
                         M^+(C)=R^+(C).               \tag{1.5}
\]

Thus the correct goals are \(R^+=E+o(W)\) on even ground and
\(R^+=o(W)\) on odd ground.

## 2. Tight enumeration is equivalent to lower-complete Hamiltonicity

The converse to the GMM contraction is useful for scope control.

### Theorem 2.1 (exact converse)

Let \(C\) be any Hamilton cycle of \(J(n,m)\) for which every member of
\(\mathcal L\) occurs as an edge intersection.  Then \(C\) expands to a
tight enumeration of the two levels \(m-1,m\).

#### Proof

For every \(S\in\mathcal L\), choose one cycle edge \(XY\) with
\(X\cap Y=S\), and insert \(S\) between \(X,Y\) in the cyclic order.
Distinct lower colours choose distinct cycle edges because a Johnson edge
has a unique intersection.

Every inserted transition \(X,S,Y\) consists of two cube edges and costs
two bit flips.  Every unexpanded Johnson edge is a direct equal-rank
transition and also costs two bit flips.  Hence the total Hamming distance
of the resulting cyclic enumeration is \(2W\).

The enumeration has \(W+N_-\) vertices, and the difference of the two
bipartition sizes is \(W-N_-=E\).  Therefore its tight lower bound is
\[
                         W+N_-+E=2W.                 \tag{2.1}
\]
Equality holds, so the enumeration is tight. \(\square\)

Thus “GMM tight Hamilton cycle” means precisely “full-owner Hamilton
cycle with complete lower support” at the level relevant here.  No
pentagon occurrence, point regularity of the lower excess, or opposite-
colour dispersion is encoded in the adjective tight.

## 3. Exact owner and upper point margins

Let \(P_k\) denote point-versus-\(k\)-set incidence.  For every Johnson
edge \(XY\),
\[
 \mathbf1_{X\cap Y}+\mathbf1_{X\cup Y}
 =\mathbf1_X+\mathbf1_Y                              \tag{3.1}
\]
as coordinate incidence vectors.  Summing (3.1) over a Hamilton cycle
gives
\[
 P_{m-1}\ell+P_{m+1}u
 =2P_m\mathbf1_{\mathcal M}.                         \tag{3.2}
\]

Since all middle owners occur,
\[
 P_m\mathbf1_{\mathcal M}
 =\binom{n-1}{m-1}\mathbf1.                          \tag{3.3}
\]
Equations (3.2)--(3.3) prove (0.5)--(0.6).

### 3.1 Even ground

Take \(n=2m\).  Elementary binomial identities give
\[
\begin{aligned}
 2\binom{2m-1}{m-1}
 -\binom{2m-1}{m-2}
 -\binom{2m-1}{m}
 &=E.
\end{aligned}                                                   \tag{3.4}
\]
Substitute \(\ell=\mathbf1+h\) into (3.2) to obtain (0.7).

For every \(v\),
\[
                         0\le E-h_v\le E,             \tag{3.5}
\]
and
\[
 \sum_v(E-h_v)
 =2mE-(m-1)E=(m+1)E.                                \tag{3.6}
\]

### Theorem 3.1 (exact point-compatible full upper cover)

There is a multiset of \(E\) upper targets whose coordinate degree
sequence is \((E-h_v)_v\).  Equivalently, (0.8) has a nonnegative integral
solution \(g\).

#### Proof

Create \(E\) labelled right vertices, each required to have degree
\(m+1\), and \(2m\) coordinate vertices on the left, with required degrees
\[
                         q_v=E-h_v.
\]
We seek a simple bipartite graph with these degrees; the neighborhood of
one right vertex will be one upper target.

The degree sums agree by (3.6), and \(0\le q_v\le E\).  The Gale--Ryser
inequalities are immediate.  For the \(k\) largest left degrees,
\[
 \sum_{i=1}^kq_i\le
 \begin{cases}
 kE,&k\le m+1,\\
 (m+1)E,&k\ge m+1,
 \end{cases}                                                   \tag{3.7}
\]
which equals
\[
                         \sum_{j=1}^E\min\{k,m+1\}.
\]
Hence the required bipartite graph exists.  Its right neighborhoods give
the asserted multiset. \(\square\)

The right neighborhoods need not be distinct, and they need not be the
actual upper colours of a Hamilton cycle.  The theorem closes exactly the
point-margin obstruction and no more.

### 3.2 Odd ground

Take \(n=2m+1\).  Put
\[
 \eta=
 2\binom{2m}{m-1}
 -\binom{2m}{m-2}
 -\binom{2m}{m}
 ={E(m-1)\over2m+1}.                                \tag{3.8}
\]
The first expression proves integrality.  Equation (3.2) gives (0.9).
Moreover
\[
 \sum_vh_v=(m-1)E,\qquad
 (2m+1)\eta=(m-1)E.                                 \tag{3.9}
\]
Therefore
\[
 \sum_v|\eta-h_v|
 \le\sum_v(\eta+h_v)=2(m-1)E,                        \tag{3.10}
\]
proving (0.10).

If \(u=\mathbf1_{\mathcal U}\), then (0.9) forces
\[
                         h_v=\eta\quad(v\in[n]).      \tag{3.11}
\]
This is the exact regular repeated-lower design required for a perfectly
upper-rainbow full Hamilton cycle.  Since \(E=O(W/m)\), failure of
(3.11) cannot yield a linear missing-shadow lower bound through point
margins alone.

## 4. The disjoint six-coordinate carrier bank

Fix \(D\in\binom{[n]}6\).  For every
\[
                         K\in\binom{[n]\setminus D}{m-3},       \tag{4.1}
\]
the fibre \(\mathcal F_K\) in (0.11) consists of twenty middle owners and
is a literal copy of \(J(6,3)\).

Different \(K\)'s give disjoint owner fibres.  Their lower targets
\[
                         K\cup A,\qquad A\in\binom D2,          \tag{4.2}
\]
and upper targets
\[
                         K\cup B,\qquad B\in\binom D4          \tag{4.3}
\]
are also disjoint across \(K\), because intersection with
\([n]\setminus D\) recovers \(K\).

The number of fibres is \(F\) in (0.12).  Indeed,
\[
 {20F\over W}
 =\Pr_{X\in\binom{[n]}m}(|X\cap D|=3)
 \longrightarrow {20\over64},                       \tag{4.4}
\]
which proves \(F/W\to1/64\).

Inside one fibre, the old complemented-pentagon table consists of five
disjoint length-three paths and uses fifteen internal Johnson edges.  It
is **eligible** when those five paths occur as ported subpaths of \(C\).
The new table has the same row endpoints, the same twenty owner degrees,
and the same fifteen lower colours; replacing old by new therefore
preserves the Hamilton cycle and its complete lower load.

Let \(g_D(C)\) count eligible fibres.  Since distinct fibres have disjoint
edge sets and each eligible fibre uses fifteen internal edges, (0.13)
follows.

## 5. Exact internal-edge double count

For a cycle edge \(e=XY\), put
\[
 S=X\cap Y,\qquad U=X\cup Y,\qquad U\setminus S=\{a,b\}.        \tag{5.1}
\]
A six-set \(D\) makes \(e\) internal to a rank-three fibre precisely when

* \(a,b\in D\);
* two further elements of \(D\) are chosen from \(S\);
* the last two elements are chosen from \([n]\setminus U\).

Hence every cycle edge is counted for exactly
\[
                         \binom{m-1}{2}\binom{n-m-1}{2}        \tag{5.2}
\]
six-sets.  Summing over the \(W\) Hamilton edges proves (0.14).

Dividing by \(\binom n6\) and then by fifteen gives
\[
\begin{aligned}
 \mathbb E_D g_D(C)
 &\le {W\over15}
 { \binom{m-1}{2}\binom{n-m-1}{2}\over\binom n6}\\
 &=\left({3\over16}+o(1)\right){W\over m^2},
\end{aligned}                                                   \tag{5.3}
\]
for both \(n=2m\) and \(n=2m+1\).  This proves (0.15).

In particular, for every fixed \(\varepsilon>0\), Markov's inequality
gives
\[
 \Pr_D(g_D(C)\ge\varepsilon W)
 \le\left({3\over16\varepsilon}+o(1)\right)m^{-2}.    \tag{5.4}
\]
Thus a random coordinate relabeling of one fixed six-block almost surely
does not expose a positive-density pentagon bank.

This does not exclude a specially chosen exceptional six-set, nor a bank
whose copies use many different six-sets.  It proves that neither uniform
relabeling nor the scalar tight-enumeration count supplies the desired
density.

## 6. Contracted-edge toll

The tight enumeration marks exactly \(N_-\) Hamilton edges as contractions
through distinct lower vertices and exactly \(E\) edges as direct
middle-to-middle transitions.

### Proposition 6.1 (dense banks must be almost wholly contracted)

Let \(\mathcal P\) be an edge-disjoint family of eligible pentagons.
At most \(E\) members of \(\mathcal P\) contain a direct edge.
Consequently, if \(|\mathcal P|=\Omega(W)\), then all but \(o(W)\) of its
members consist entirely of fifteen contracted edges.

#### Proof

Charge a pentagon containing a direct edge to one such edge.  Edge
disjointness makes the charge injective, and there are exactly \(E\)
direct edges.  Since \(E=O(W/m)=o(W)\), the conclusion follows.
\(\square\)

Thus a positive-density supply requires the original two-level tight
enumeration to contain a positive-density family of complete local
alternating sub-enumerations
\[
 \text{middle--lower--middle--lower--middle--lower--middle}
\]
on all five pentagon rows.  GMM tightness supplies only the total numbers
of contracted and direct transitions, not this fifteen-edge correlation.

## 7. Simultaneous descent in one bank

For an eligible fibre \(K\), let \(\Delta_K^+\) be the six-term upper
difference of the complemented pentagon.  The exact repeat change is
\[
 \Delta_K R^+
 =\#\{\text{positive targets already occupied}\}
  -\#\{\text{negative targets currently repeated}\}.          \tag{7.1}
\]

Call the fibre descending with margin \(\gamma_K\) when
\[
                         \Delta_KR^+\le-\gamma_K<0.            \tag{7.2}
\]

### Theorem 7.1 (fixed-bank simultaneous improvement)

Let \(\mathcal K\) be any family of eligible fibres for one fixed \(D\).
All their switches may be performed simultaneously, and
\[
 R^+(C_{\rm new})
 =R^+(C)+\sum_{K\in\mathcal K}\Delta_KR^+.            \tag{7.3}
\]
In particular, if every selected fibre has \(\gamma_K\ge1\), then
\[
                         R^+(C_{\rm new})
 \le R^+(C)-|\mathcal K|.                            \tag{7.4}
\]

#### Proof

Distinct fibres have disjoint owner sets, ports, cycle edges, lower
targets, and upper targets.  Each local replacement has the same five
contracted port pairs, so contracting every replaced path to its endpoints
leaves the same global cycle.  Hence the replacements preserve one
Hamilton cycle.  Disjoint upper supports make the nonlinear repeat changes
add exactly, proving (7.3). \(\square\)

This is a genuine positive theorem: a positive-density descending bank
would remove a positive-density upper defect in one integral move while
retaining all owners and every lower target.  What remains unproved is the
hypothesis that the GMM tight cycle can be selected with such a bank.

## 8. Exact remaining alternatives

Let
\[
 \mathcal R=\{U:u(U)\ge2\},\qquad
 \mathcal H=\{U:u(U)=0\}.                            \tag{8.1}
\]
Every complemented pentagon has upper support of Johnson diameter at most
two.  Therefore
\[
                         d_J(\mathcal R,\mathcal H)\ge3         \tag{8.2}
\]
is a statewise obstruction to strict pentagon descent, even if eligible
copies are abundant.

If (8.2) fails, local algebraic descent directions exist, but physical
eligibility still requires the complete five-path negative table.  The
remaining positive theorem can now be stated sharply:

> **Pentagon-rich tight enumeration.**  Choose a lower-complete tight
> Hamilton cycle for which some structured family of six-coordinate
> fibres contains \(\Omega(M^+(C))\) mutually compatible eligible
> pentagons, with total descent score
> \(-M^+(C)+o(W)\).

Alternatively one must use a larger-diameter trade.  The fixed-owner point
invariant does not block either route: Sections 3.1--3.2 show that its
entire possible cost is \(o(W)\), and on even ground it vanishes exactly
at the upper load-vector level.

The exact conclusion is therefore:

* full ownership closes the owner point-margin problem without any
relabeling;
* the six-coordinate pentagon has enough abstract carrier capacity
(\(W/64+o(W)\) disjoint fibres);
* a random relabeling exposes only \(O(W/m^2)\) eligible copies in
expectation;
* tight enumeration forces neither eligibility nor defect alignment.

A \(q=1\) two-sided Hamilton cycle up to \(o(W)\) defects remains
equivalent, in this lane, to the pentagon-rich tight-enumeration theorem
above.
