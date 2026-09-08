# Stateful global-portal target extraction: exact thinning and a quadratic collision obstruction

Date: 2026-07-25

## 0. Verdict

This report attacks the target-distinctness gate left by
`GLOBAL_PORTAL_CONSTRUCTION_AFTER_DRAY_20260724.md`,
`MATH_ATTACK_V4_PORTAL_MEMBERSHIP_MTF_FUSION_20260725.md`, and
`ADAPTIVE_MTF_PORTAL_DEPLETION_OBSTRUCTION_20260725.md`.

The chronology and state-compatibility parts can be completed.  Starting
from one exact odd factor, there is already one legal literal adaptive-MTF
word of length

\[
 W+(2H+1)\frac{W}{m+1}=W+o(W),
 \qquad
 W=\binom{2m}{m},\quad H=\lceil A\sqrt m\rceil,
 \tag{0.1}
\]

with a radius-\(H\) saturated flag at every one of its \(W\) middle-state
endpoints.  After one common coordinate relabelling, these flags have

\[
 (2H+1)W-o(W)=\Omega(HW)
 \tag{0.2}
\]

distinct endpoint--product-box cells.  No new reset or bridge is required.

The new structural fact is that **each complementary-geodesic component is
internally target-rainbow at every signed depth**.  Thus all equal-target
collisions in the canonical word occur between different odd-factor
components.  Stateful MTF compatibility creates no collision inside a
component.

Define the cross-component same-rank target-collision energy

\[
 \mathfrak K_H
 =\sum_{\varepsilon\in\{-,+\}}\sum_{q=1}^{H}
   \sum_{S\in\binom{[2m]}{m+\varepsilon q}}
       \binom{\mu_{\varepsilon,q}(S)}2,
 \tag{0.3}
\]

where \(\mu_{\varepsilon,q}(S)\) is the number of state endpoints whose
signed depth-\(q\) canonical target is \(S\).  Put

\[
 p=\left\lceil\frac WH\right\rceil.
 \tag{0.4}
\]

The main exact extraction estimate is

\[
 \boxed{
 M_p\ge
 (2H+1)p
 -\frac{p(p-1)}{W(W-1)}\mathfrak K_H
 -O_A\!\left(\frac W{\sqrt m}\right),}
 \tag{0.5}
\]

where \(M_p\) is the maximum number of literal canonical occurrences on
some \(p\) physical endpoints that can be chosen with pairwise distinct
Boolean targets and pairwise distinct endpoint--box cells.  Every selected
occurrence is a suffix interval in the same word.

Since

\[
 (2H+1)p=2W+o(W),
 \qquad
 \frac{p(p-1)}{W(W-1)}=(1+o(1))H^{-2},
 \tag{0.6}
\]

(0.5) gives the following precise dichotomy.

* If
  \[
  \boxed{\mathfrak K_H\le(1+o(1))H^2W,}
  \tag{QPC\(_A\)}
  \]
  then the audited legal word contains \(p=\Theta(W/H)\) stateful portals
  supporting \(W-o(W)\) pairwise distinct Boolean targets in pairwise
  distinct endpoint--box cells.  Their right-endpoint sharing surplus is
  also \(W-o(W)\), while the word's portal/reset excess is \(o(W)\).

* Conversely, if for some fixed \(\delta>0\), along an infinite subsequence,
  every set of \(p\) state endpoints supports fewer than
  \((1-\delta)W\) such genuine incidences, then necessarily
  \[
  \boxed{
  \mathfrak K_H\ge(1+\delta-o(1))H^2W.}
  \tag{0.7}
  \]

Thus failure of stateful target extraction forces a new, genuinely
quadratic-in-window collision obstruction.  Ordinary rank capacity forces
only \(\Theta_A(HW)\) pair collisions.  The obstruction (0.7) is larger by
a factor \(\Theta(H)\), and, by internal target-rainbowness, every one of
those excess collisions is cross-component.

There is also an exact load-functional form, stronger than (0.5), in
Theorem 4.1 below.  It gives the expected number of distinct targets after
uniformly thinning the \(W\) state endpoints to \(p\) endpoints.  The
quadratic estimate is a transparent sufficient relaxation.

What remains unproved is \((\mathrm{QPC}_A)\), or the still weaker exact
load-functional inequality stated in (5.5), for some exact odd factor.
No MWB, labelled synchronization, or deep-support theorem is silently
assumed.  The report therefore does not prove the contiguous-OR width
conjecture.  It proves that, inside the audited odd-factor MTF chronology,
the remaining obstruction is a large cross-component target-collision
energy, not state compatibility or portal reset cost.

No web search, finite search, or computation is used.

---

## 1. Audited legal MTF chronology

Fix

\[
 n=2m,
 \qquad
 W=\binom{2m}{m},
 \qquad
 1\le H<m/2.
 \tag{1.1}
\]

The exact odd factor cuts into

\[
 B=\frac{W}{m+1}
 \tag{1.2}
\]

vertex-disjoint oriented complementary Johnson geodesics.  Each component
has middle vertices

\[
 T_0,T_1,\ldots,T_m
 \tag{1.3}
\]

which can be written using a cyclic order

\[
 w=(a_0,\ldots,a_{m-1},b_0,\ldots,b_{m-1})
 \tag{1.4}
\]

of \([2m]\) as

\[
 T_t=I_w(t,m),
 \qquad 0\le t\le m.
 \tag{1.5}
\]

Here \(I_w(r,\ell)\) denotes the set of the \(\ell\) consecutive symbols
of \(w\) starting at cyclic position \(r\).  The transition from \(T_t\)
to \(T_{t+1}\) removes \(a_t\) and inserts \(b_t\).  No removed coordinate
returns and no inserted coordinate is later removed.

Choose the audited initial upper queue and terminal dummy departures.  The
canonical adaptive-MTF state at \(T_t\) exposes, for \(0\le q\le H\),

\[
 \boxed{
 F_{t,-q}=I_w(t+q,m-q),
 \qquad
 F_{t,+q}=I_w(t-q,m+q).}
 \tag{1.6}
\]

In particular,

\[
 F_{t,0}=T_t,
 \qquad
 |F_{t,\varepsilon q}|=m+\varepsilon q.
 \tag{1.7}
\]

Every member of (1.6) is the union of a literal suffix ending at the
physical word position representing the state \(T_t\).  Consecutive states
are related by one legal MTF update.  Reverse-initializing each of the
\(B\) components and concatenating them produces one nonzero Boolean word
\(\mathcal W_H\) of exact length

\[
 \boxed{
 |\mathcal W_H|
 =W+(2H+1)B.}
 \tag{1.8}
\]

For fixed \(A>0\) and \(H=\lceil A\sqrt m\rceil\),

\[
 (2H+1)B=O_A(W/\sqrt m)=o(W).
 \tag{1.9}
\]

This is the single stateful trajectory used throughout the report.  No
selected endpoint is reinitialized, reordered, or connected to another
selected endpoint.

---

## 2. State compatibility causes no within-component target collision

The following lemma is the first new structural input.

### Lemma 2.1 -- uniqueness of a proper cyclic interval

Let \(w\) be a cyclic order of \(N\) distinct symbols and let
\(1\le \ell<N\).  Then

\[
 r\longmapsto I_w(r,\ell)
 \tag{2.1}
\]

is injective on cyclic starting positions.

#### Proof

The indicator of a nonempty proper cyclic interval has exactly one directed
boundary edge at which it changes from outside to inside.  For
\(I_w(r,\ell)\), that boundary edge is

\[
 (w_{r-1},w_r).
\]

The set therefore determines \(r\) uniquely. \(\square\)

### Theorem 2.2 -- componentwise target-rainbowness

Fix one complementary-geodesic component.  For every signed depth
\(\varepsilon q\), where \(\varepsilon\in\{-,+\}\) and
\(1\le q\le H\), the \(m+1\) targets

\[
 F_{0,\varepsilon q},F_{1,\varepsilon q},\ldots,
 F_{m,\varepsilon q}
 \tag{2.2}
\]

are pairwise distinct.  The full \((2H+1)\)-target flags at two different
state endpoints in the same component have no common target.

#### Proof

For fixed \(\varepsilon q\), formula (1.6) expresses the targets as cyclic
intervals of fixed length \(m+\varepsilon q\).  Because \(H<m/2\),

\[
 1\le m-H\le m+\varepsilon q\le m+H<2m.
\]

Their starting positions are \(t+q\) on the lower side and \(t-q\) on the
upper side.  As \(t\) ranges from \(0\) through \(m\), these are distinct
modulo \(2m\).  Lemma 2.1 proves injectivity.

Targets at different signed depths have different cardinalities, except
only for the identical signed depth itself.  The middle masks \(T_t\) are
also distinct along a geodesic.  Hence two flags in the same component
share no target. \(\square\)

### Corollary 2.3 -- every canonical target collision is cross-component

For a signed depth \(\varepsilon q\), define

\[
 \mu_{\varepsilon,q}(S)
 =\#\{(P,t):F^P_{t,\varepsilon q}=S\},
 \tag{2.3}
\]

where \(P\) ranges over the \(B\) complementary-geodesic components.
Then

\[
 0\le\mu_{\varepsilon,q}(S)\le B,
 \tag{2.4}
\]

and

\[
 \sum_S\binom{\mu_{\varepsilon,q}(S)}2
 \tag{2.5}
\]

counts pairs of occurrences on two different components.  Consequently
the total energy \(\mathfrak K_H\) in (0.3) is exactly the number of
equal-target, equal-signed-depth pairs belonging to different components.

#### Proof

Theorem 2.2 permits at most one occurrence of a fixed target in each
component.  The assertions follow by counting pairs. \(\square\)

This proves a strict state/support separation.  The legal MTF evolution
along a component is target-rainbow.  Only the global geometry of how the
exact factor's different cyclic intervals overlap can obstruct extraction.

---

## 3. Product-box cells cost only \(o(W)\)

Assume now that \(2m=3s\), with the coordinate set split into three
\(s\)-blocks and with one fixed symmetric-chain decomposition in each
block.  Their products partition the Boolean cube into product boxes.

For a coordinate permutation \(\sigma\), a state endpoint \(v\), and a
product box \(\mathcal B\), let

\[
 n_{v,\mathcal B}(\sigma)
 =\#\{a\in[-H,H]:\sigma F_{v,a}\in\mathcal B\}.
 \tag{3.1}
\]

Define the endpoint--box pair-collision count

\[
 \mathfrak C_{\Box}(\sigma)
 =\sum_v\sum_{\mathcal B}
   \binom{n_{v,\mathcal B}(\sigma)}2.
 \tag{3.2}
\]

### Lemma 3.1 -- one common relabelling has negligible cell collision

For some coordinate permutation \(\sigma\),

\[
 \boxed{
 \mathfrak C_{\Box}(\sigma)
 \le W\varepsilon_{m,H},}
 \tag{3.3}
\]

where

\[
 \varepsilon_{m,H}
 =\sum_{d=1}^{2H}(2H+1-d)
   \frac{\binom{d+2}{2}}{\binom{m-H}{d}}.
 \tag{3.4}
\]

For fixed \(A\) and \(H=\lceil A\sqrt m\rceil\),

\[
 \varepsilon_{m,H}=O_A(H/m)=O_A(m^{-1/2}),
 \tag{3.5}
\]

so

\[
 \mathfrak C_{\Box}(\sigma)=O_A(W/\sqrt m)=o(W).
 \tag{3.6}
\]

#### Proof

Fix a nested pair \(S\subset T\) in one flag, with rank gap \(d\).  Under
a uniform coordinate permutation, conditional on the upper mask, the lower
mask is a uniform \(d\)-deletion.  In one three-chain product box, a
\(d\)-step predecessor is specified by the three nonnegative factor-chain
drops whose sum is \(d\).  There are at most \(\binom{d+2}{2}\) choices.
The upper mask has at least \(m-H\) elements.  Therefore

\[
 \Pr(\sigma S,\sigma T\text{ lie in one box})
 \le
 \frac{\binom{d+2}{2}}{\binom{m-H}{d}}.
 \tag{3.7}
\]

One flag has \(2H+1-d\) pairs at rank gap \(d\).  Sum (3.7) over its pairs
and then over the \(W\) endpoints.  This proves the expectation bound
corresponding to (3.3), so some \(\sigma\) attains it.

For \(H=O_A(\sqrt m)\), the \(d=1\) term is

\[
 \frac{6H}{m-H}=O_A(H/m).
\]

The \(d=2\) term is \(O_A(H/m^2)\), and the ratio of consecutive terms is
bounded away from one for \(3\le d\le2H\), once \(m\) is sufficiently
large depending on \(A\).  This gives (3.5). \(\square\)

### Corollary 3.2 -- the full trajectory has \(\Omega(HW)\) genuine cells

For the relabelling in Lemma 3.1, the number of distinct endpoint--box
cells occupied by the \((2H+1)W\) canonical occurrences is at least

\[
 (2H+1)W-\mathfrak C_{\Box}(\sigma)
 =(2H+1)W-o(W).
 \tag{3.8}
\]

#### Proof

At a cell of multiplicity \(r\), deduplicating loses \(r-1\), and

\[
 (r-1)_+\le\binom r2.
\]

Sum over the cells and apply (3.6). \(\square\)

A coordinate permutation is a bijection on Boolean masks.  It does not
change any target equality or any load \(\mu_{\varepsilon,q}(S)\).
Therefore the relabelling in Lemma 3.1 leaves \(\mathfrak K_H\) invariant.

---

## 4. Exact random-thinning theorem

This section is independent of the special cyclic-interval formulas.  It
applies to any single legal trajectory with one target occurrence in each
of \(R\) different ranks at every one of \(N\) marked endpoints.  We state
it in the parameters needed here:

\[
 N=W,
 \qquad
 R=2H+1.
 \tag{4.1}
\]

Let \(\mathcal A=[-H,H]\) index the signed ranks.  For \(a\in\mathcal A\)
and a rank-\((m+a)\) target \(S\), put

\[
 \mu_a(S)=\#\{v:F_{v,a}=S\}.
 \tag{4.2}
\]

Thus \(\sum_S\mu_a(S)=W\) for every \(a\), and \(\mu_0(S)=1\) for every
middle target.

For \(1\le p\le W\), define the exact thinned-support functional

\[
 \boxed{
 \Phi_p
 =\sum_{a=-H}^{H}\sum_S
 \left(
 1-\frac{\binom{W-\mu_a(S)}p}{\binom Wp}
 \right),}
 \tag{4.3}
\]

where \(\binom{x}{p}=0\) when \(x<p\).

### Theorem 4.1 -- exact target support under endpoint thinning

There is a set \(J\) of exactly \(p\) state endpoints for which the
canonical occurrences ending in \(J\) contain at least \(\Phi_p\) distinct
Boolean targets.  Moreover, with

\[
 \alpha_p=\frac{p(p-1)}{W(W-1)}
 \tag{4.4}
\]

and

\[
 \mathfrak K_H
 =\sum_{a=-H}^{H}\sum_S\binom{\mu_a(S)}2,
 \tag{4.5}
\]

where the middle term is zero, one has

\[
 \boxed{
 \Phi_p\ge(2H+1)p-\alpha_p\mathfrak K_H.}
 \tag{4.6}
\]

#### Proof

Choose \(J\) uniformly among the \(p\)-subsets of the \(W\) endpoints.
A fixed target of load \(\mu\) is absent precisely when all selected
endpoints lie among the \(W-\mu\) endpoints not carrying it.  Its presence
probability is

\[
 1-\frac{\binom{W-\mu}p}{\binom Wp}.
\]

Targets in different signed ranks are different because their
cardinalities are different.  Summing the displayed probability proves
that the expected number of distinct targets is exactly \(\Phi_p\).  Some
choice of \(J\) attains at least the expectation.

For the quadratic relaxation, let \(X_{a,S}\) be the number of selected
occurrences of target \(S\) at signed rank \(a\).  The number of repeated
occurrences lost when that target is deduplicated is

\[
 (X_{a,S}-1)_+\le\binom{X_{a,S}}2.
 \tag{4.7}
\]

For sampling without replacement,

\[
 \mathbb E\binom{X_{a,S}}2
 =\frac{\binom p2}{\binom W2}
   \binom{\mu_a(S)}2
 =\alpha_p\binom{\mu_a(S)}2.
 \tag{4.8}
\]

There are exactly \((2H+1)p\) occurrences at the selected endpoints.
Taking expectations in (4.7), summing, and using (4.8) proves (4.6).
\(\square\)

The exact quantity \(\Phi_p\) is preferable when a few targets have large
loads: it charges such a target by its probability of being hit, rather
than by all \(\binom\mu2\) collision pairs.  The energy inequality (4.6)
is intentionally a simpler sufficient criterion.

### Theorem 4.2 -- stateful incidence extraction

Assume the product-box setup of Section 3 and use the common relabelling
\(\sigma\) from Lemma 3.1.  There is a set \(J\) of exactly \(p\) physical
state endpoints and a family of literal suffix witnesses ending in \(J\)
with pairwise distinct target masks and pairwise distinct endpoint--box
cells, of cardinality at least

\[
 \boxed{
 M_p\ge\Phi_p-\mathfrak C_{\Box}(\sigma).}
 \tag{4.9}
\]

Consequently,

\[
 \boxed{
 M_p\ge
 (2H+1)p-\alpha_p\mathfrak K_H
 -\mathfrak C_{\Box}(\sigma).}
 \tag{4.10}
\]

#### Proof

Choose \(J\) as in Theorem 4.1 and first retain one occurrence of every
distinct target represented on \(J\).  This leaves at least \(\Phi_p\)
occurrences with distinct targets.

An occurrence has one endpoint--box cell

\[
 (v,\mathcal B(F_{v,a})).
\]

Within every repeated cell retain only one occurrence.  If a cell initially
has multiplicity \(r\), this loses at most

\[
 (r-1)_+\le\binom r2.
\]

Restriction to \(J\), followed by target deduplication, cannot increase
the full collision sum \(\mathfrak C_{\Box}(\sigma)\).  Thus the second
deduplication loses at most \(\mathfrak C_{\Box}(\sigma)\) occurrences.
The survivors have distinct targets and distinct cells.

Every survivor was already a canonical flag occurrence in
\(\sigma\mathcal W_H\).  Hence its target is represented by a literal
suffix interval in the original legal MTF chronology; the selection adds
no letters and changes no state.  Equation (4.10) follows from (4.6).
\(\square\)

Theorem 4.2 is an occurrence-to-MTF fusion theorem specialized to
high-degree endpoint thinning.  Unlike selecting the largest endpoint
degrees after a global matching, it guarantees from the outset that only
\(p=\Theta(W/H)\) physical endpoints are used.

---

## 5. Gaussian-scale extraction and the new collision alternative

Fix \(A>0\) and put

\[
 H=\lceil A\sqrt m\rceil,
 \qquad
 p=\left\lceil\frac WH\right\rceil.
 \tag{5.1}
\]

Since \(W\) is exponential in \(m\), while \(H=O_A(\sqrt m)\),

\[
 (2H+1)p=2W+o(W)
 \tag{5.2}
\]

and

\[
 \alpha_p
 =\frac{p(p-1)}{W(W-1)}
 =(1+o(1))H^{-2}.
 \tag{5.3}
\]

Combining (3.6), (4.10), (5.2), and (5.3) gives

\[
 \boxed{
 M_p
 \ge
 2W-\frac{\mathfrak K_H}{H^2}-o(W).}
 \tag{5.4}
\]

The exact, and potentially weaker, sufficient condition is

\[
 \boxed{\Phi_p\ge W-o(W).}
 \tag{5.5}
\]

The following is the principal theorem of the report.

### Theorem 5.1 -- stateful portal-extraction dichotomy

For the audited odd-factor adaptive-MTF word, one common coordinate
relabelling has the following properties.

1. The word is legal, literal, and has length
   \[
   W+O_A(W/\sqrt m)=W+o(W).
   \tag{5.6}
   \]

2. It carries \((2H+1)W-o(W)=\Omega(HW)\) distinct endpoint--box cells.

3. If either (5.5) holds or, sufficiently, if
   \[
   \mathfrak K_H\le(1+o(1))H^2W,
   \tag{5.7}
   \]
   then some
   \[
   p=\left\lceil W/H\right\rceil=\Theta(W/H)=o(W)
   \tag{5.8}
   \]
   physical endpoints support \(W-o(W)\) literal occurrences with pairwise
   distinct Boolean targets and pairwise distinct endpoint--box cells.

4. If \(d_v\) is the number of retained cells at selected endpoint \(v\),
   then their right-sharing surplus satisfies
   \[
   \sum_{v\in J}(d_v-1)_+
   \ge M_p-p
   =W-o(W).
   \tag{5.9}
   \]

5. Conversely, suppose that for a fixed \(\delta>0\), along an infinite
   sequence of \(m\), no \(p\)-endpoint set supports
   \((1-\delta)W\) distinct-target, distinct-cell canonical occurrences.
   Then along that sequence
   \[
   \boxed{
   \mathfrak K_H\ge(1+\delta-o(1))H^2W.}
   \tag{5.10}
   \]
   Every collision counted in (5.10) is between two different exact-factor
   components.

#### Proof

Items 1 and 2 are (1.8)--(1.9) and Corollary 3.2.  Under (5.5), Theorem
4.2 and (3.6) give \(M_p\ge W-o(W)\).  Under (5.7), the same conclusion
follows from (5.4).  This proves item 3.

The matched cells at an endpoint lie in distinct boxes.  If \(d_v>0\),
one may charge one cell as the baseline and the other \(d_v-1\) cells as
right-sharing surplus.  There are at most \(p=o(W)\) baselines, proving
(5.9).

For item 5, rearrange (4.10).  If \(M_p<(1-\delta)W\), then

\[
 \alpha_p\mathfrak K_H
 >(2H+1)p-\mathfrak C_{\Box}-(1-\delta)W
 =(1+\delta-o(1))W.
 \tag{5.11}
\]

Use (5.3) to obtain (5.10).  Corollary 2.3 makes all these collisions
cross-component. \(\square\)

### Remark 5.2 -- what “portal excess” means here

The selected portals are not independently initialized flag blocks.  They
are marked state positions on the already constructed word
\(\mathcal W_H\).  Hence selecting them adds zero letters.  The entire word
has reset/initialization excess

\[
 (2H+1)B=O_A(W/\sqrt m)=o(W).
 \tag{5.12}
\]

This is the relevant portal excess in the coefficient-one construction.
The number of marked physical endpoints is itself
\(p=O(W/\sqrt m)=o(W)\).

---

## 6. Rank capacity does not explain the obstruction

Let

\[
 N_q=\binom{2m}{m+q}=\binom{2m}{m-q}.
 \tag{6.1}
\]

At either signed depth \(q\), the \(W\) occurrences are distributed among
at most \(N_q\) targets.  Put

\[
 c_q=\left\lfloor\frac W{N_q}\right\rfloor,
 \qquad
 r_q=W-c_qN_q.
 \tag{6.2}
\]

### Lemma 6.1 -- exact rank-capacity collision floor

For either sign and every \(1\le q\le H\),

\[
 \boxed{
 \sum_S\binom{\mu_{\varepsilon,q}(S)}2
 \ge
 N_q\binom{c_q}2+r_qc_q.}
 \tag{6.3}
\]

Equality in this purely numerical problem occurs precisely when every load
is \(c_q\) or \(c_q+1\), with exactly \(r_q\) loads equal to \(c_q+1\).

#### Proof

If two loads satisfy \(x\ge y+2\), moving one occurrence from the first
to the second changes the pair sum by

\[
 \binom{x-1}2+\binom{y+1}2-\binom x2-\binom y2
 =y-x+1<0.
\]

Thus a minimizing load vector differs by at most one between occupied
bins.  Filling all \(N_q\) bins as evenly as possible gives (6.3).
\(\square\)

For \(q=t\sqrt m+O(1)\), uniformly for bounded \(t\),

\[
 \frac{N_q}{W}
 =\prod_{j=1}^q\frac{m-j+1}{m+j}
 =e^{-t^2+o(1)}.
 \tag{6.4}
\]

Consequently \(c_q=O_A(1)\) for \(q\le A\sqrt m+O(1)\).  Summing the
right side of (6.3) over both signs and \(1\le q\le H\) gives a forced
capacity floor of order

\[
 \Theta_A(HW).
 \tag{6.5}
\]

Indeed, it is \(O_A(HW)\) because every \(c_q\) is bounded, and it is
\(\Omega_A(HW)\) because a positive fraction of the depths satisfy
\(q\ge(A/2)\sqrt m\), where \(N_q/W\) is bounded below one by a fixed
amount depending on \(A\).

At Gaussian depth,

\[
 HW=o(H^2W).
 \tag{6.6}
\]

Thus the collision lower bound forced by failure in (5.10) is not the
ordinary fact that off-middle ranks contain fewer than \(W\) masks.  It
requires an extra factor \(H\) of collision concentration beyond the
balanced rank-capacity floor.

For example, at \(q=1\),

\[
 N_1=\frac{m}{m+1}W,
 \qquad
 c_1=1,
 \qquad
 r_1=W-N_1=\frac{W}{m+1}=B,
 \tag{6.7}
\]

so rank capacity forces exactly \(B\) pairs in an optimally balanced load
ledger.  This is negligible compared with the \(H^2W\) obstruction scale.

---

## 7. Why fresh state repair cannot bypass the collision alternative

One might try to discard collision-heavy odd-factor components and rebuild
\(p=\Theta(W/H)\) high-degree portals as independently initialized
canonical flag pieces.  The exact residual-depletion theorem rules out this
escape at \(o(W)\) excess.

For a residual-consuming canonical component, every bridge to a fresh
canonical initial state has length at least

\[
 2H+1.
 \tag{7.1}
\]

For \(K\) independently fresh residual-consuming components, their exact
portal excess is at least

\[
 2H+1+2H(K-1)=2HK+1.
 \tag{7.2}
\]

Taking \(K=p=\lceil W/H\rceil\) gives

\[
 2Hp+1=2W+o(W),
 \tag{7.3}
\]

which is linear, not \(o(W)\).  Hence the collision alternative must be
resolved inside long compatible components, by a residual-preserving
architecture, or by using incidental bridge witnesses.  Independently
fresh canonical portal blocks cannot preserve the coefficient-one budget.

The word in Theorem 5.1 avoids (7.2) because its middle updates and its
portal arms are the same positions.  Its only component charge is the
audited \((2H+1)B=o(W)\) initialization term in (5.12).

---

## 8. Exact remaining lemma and implication scope

The new target-extraction gate can be stated in two nested forms.

### Exact load-functional gate

For some exact odd factor, with the canonical signed interval loads from
(1.6), prove

\[
 \boxed{
 \sum_{a=-H}^{H}\sum_S
 \left(
 1-\frac{\binom{W-\mu_a(S)}p}{\binom Wp}
 \right)
 \ge W-o(W),
 \qquad
 p=\left\lceil W/H\right\rceil.}
 \tag{8.1}
\]

This is exactly sufficient for stateful extraction by Theorem 4.2.

### Quadratic sufficient gate

It is sufficient to prove

\[
 \boxed{
 \sum_{\varepsilon\in\{-,+\}}\sum_{q=1}^{H}\sum_S
 \binom{\mu_{\varepsilon,q}(S)}2
 \le(1+o(1))H^2W.}
 \tag{8.2}
\]

This permits an average collision energy of order \(HW\) per signed rank,
whereas a balanced ledger has only \(O_A(W)\) per signed rank.  It is much
weaker than asking for near-injectivity at every Gaussian rank.  No
implication from MWB to (8.2), or from (8.2) to MWB, is asserted here without
an additional load-cap argument.

If (8.1) or (8.2) is proved for every fixed \(A\), Theorem 5.1 produces,
inside one exact factor and one literal word, the desired
\(W-o(W)\) distinct central targets on \(\Theta(W/H)\) state-compatible
portals with \(o(W)\) word excess.  This is an integral construction; it
does not diagonalize labelled occurrences across different factors.

If the extraction conclusion is false by a fixed positive fraction, then
Theorem 5.1 already proves the necessary incompatibility (5.10): one exact
factor must carry \(\Omega(H^2W)\) cross-component equal-target pairs.
That is the sharp new obstruction furnished by this report.

Neither alternative alone covers the entire Gaussian target band.  The
extracted \(W-o(W)\) targets are a portal core for amortizing the local
product-box gaps.  A final width proof would still have to show that the
corresponding core absorbs the required holes of one exact factor or build
the remaining literal witnesses directly.

---

## 9. Independent internal audit

The decisive points were rechecked independently of the heuristic route.

1. **Cyclic-interval formula.**  The audited boundary queue and dummy
   choices give (1.6) at all \(0\le t\le m\), not only away from component
   boundaries.  The interval lengths lie strictly between \(0\) and
   \(2m\), so Lemma 2.1 applies.

2. **Within-component injectivity.**  For fixed signed depth, the \(m+1\)
   starting positions are distinct modulo \(2m\).  Different signed depths
   have different target ranks.  Hence Corollary 2.3 contains no hidden
   exception at the initial or terminal states.

3. **Sampling constant.**  For a uniform \(p\)-subset, a fixed pair of
   endpoints is selected with probability
   \[
   \binom p2/\binom W2=p(p-1)/(W(W-1)).
   \]
   There is no missing factor of two in (4.8) or (4.10).

4. **Distinct-target loss.**  The inequality
   \((r-1)_+\le\binom r2\) is used only as a one-sided loss bound.  Large
   loads make it loose, which is why (4.3) is retained as the exact stronger
   functional.

5. **Target ranks.**  Equality between targets of different signed depths
   is impossible because their cardinalities differ.  Pair collisions need
   therefore be summed only within a signed depth.

6. **Cell matching.**  Target deduplication followed by endpoint--box-cell
   deduplication leaves a genuine matching in the target-versus-cell
   occurrence graph.  Restricting endpoints or deleting targets cannot
   increase the full cell pair-collision count.

7. **Relabelling compatibility.**  One common coordinate permutation
   preserves every MTF update, every suffix union, and every target
   multiplicity.  It can therefore reduce box collisions without changing
   \(\mathfrak K_H\).

8. **Asymptotic threshold.**  With \(p=\lceil W/H\rceil\), the raw selected
   occurrence count is \(2W+o(W)\), not \(W+o(W)\).  Thus a collision loss
   as large as \(W+o(W)\) is allowable, producing precisely the threshold
   \(H^2W\) in (5.7).  This constant is correct.

9. **Portal surplus.**  Pairwise distinct cells give one baseline cell per
   used endpoint.  Subtracting at most \(p=o(W)\) baselines from
   \(W-o(W)\) matched cells proves (5.9).

10. **Unproved statement.**  Neither (8.1) nor (8.2) is proved.  All
    unconditional claims are the legal word, its \(o(W)\) excess, its
    \(\Omega(HW)\) endpoint--box cells, componentwise target-rainbowness,
    the exact thinning theorem, the collision implication (5.10), and the
    rank-capacity comparison.  The constant-one width conjecture is not
    claimed.

## 10. Final theorem-level conclusion

Inside the audited exact odd-factor chronology, the portal target problem
has the following rigorous form:

\[
 \boxed{
 \begin{gathered}
 \text{one legal literal word of length }W+o(W),\\
 \Omega(HW)\text{ distinct endpoint--box cells},\\
 \text{no within-component target collisions},\\
 \mathfrak K_H\le(1+o(1))H^2W
 \Longrightarrow
 W-o(W)\text{ distinct targets on }\Theta(W/H)\text{ portals};\\
 \text{failure by a fraction }\delta
 \Longrightarrow
 \mathfrak K_H\ge(1+\delta-o(1))H^2W.
 \end{gathered}}
 \tag{10.1}
\]

The remaining geometry is therefore a cross-component collision problem
at scale \(H^2W\).  Stateful compatibility and reset chronology are already
paid within \(o(W)\).
