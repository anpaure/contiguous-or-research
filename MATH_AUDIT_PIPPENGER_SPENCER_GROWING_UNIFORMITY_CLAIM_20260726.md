# Audit of the claimed growing-uniformity Pippenger--Spencer application

Date: 2026-07-26

## 0. Verdict

The proposed black-box application is **not valid**.

1. The Pippenger--Spencer and Pippenger matching theorems have fixed
   uniformity.  Their thresholds depend on both the uniformity and the
   requested uncovered fraction.  They do not contain absolute exponents
   (c,c'>0) giving

   \[
   \varepsilon\lesssim
   \left(\frac{\Delta _2}{D}\right)^c+
   \left(\frac{\log N}{D}\right)^{c'}.
   \tag{0.1}
   \]

2. The displayed (N/\sqrt m) leave is obtained by formally inserting
   (K=2m) into Grable's **linear-hypergraph** estimate.  The tight packet
   hypergraph is not linear: its maximum codegree is

   \[
   \Delta _2=(2+o(1))D/m^2\gg1.
   \tag{0.2}
   \]

3. Vu's quantitative theorem for a non-linear (K)-uniform hypergraph
   with codegree at most (C) gives, for fixed (K), a leave of order

   \[
   O_K\!\left(
      N(D/C)^{-1/(K-1)}\log^{c_K}D
   \right).
   \tag{0.3}
   \]

   Here (K=2m) and (D/C=\Theta(m^2)), so even with every hidden
   constant suppressed,

   \[
   (D/C)^{-1/(K-1)}
   =\exp\!\left[-\frac{2\log m+O(1)}{2m-1}\right]
   =1-o(1).
   \tag{0.4}
   \]

   Thus (0.3) is quantitatively vacuous in the required diagonal regime;
   it does not yield (N/\sqrt m).

4. A single isolated bite with marking probability (\gamma/(KD)) is
   valid uniformly in growing (K) and covers a (\Theta(1/K)) fraction.
   Iterating it for (\Theta(K\log m)) bites requires a new
   trajectory-specific regeneration or absorption theorem.  Time-zero
   regularity and pair codegrees do not supply that theorem.

Consequently the favorable time-zero geometry remains useful, but the
near-perfect protected-deck matching remains open.

## 1. What the primary theorems actually say

The official abstract of Pippenger--Spencer explicitly assumes that every
edge has size (k) for **some fixed (k)**.  Its asymptotic statement is
therefore not uniform in a sequence (k=k(N)\to\infty):

* N. Pippenger and J. Spencer,
  [*Asymptotic Behavior of the Chromatic Index for Hypergraphs*](https://scholarship.claremont.edu/hmc_fac_pub/1041/),
  JCTA 51 (1989), 24--42.

The quantitative formulation quoted in Alon--Kim--Spencer is:

> For every fixed (K) and every fixed (\epsilon>0), there are
> (\delta(K,\epsilon)>0) and (D_0(K,\epsilon)) such that a nearly
> (D)-regular (K)-uniform hypergraph with maximum codegree at most
> (\delta D) has a matching leaving at most (\epsilon N) vertices.

See page 1 of N. Alon, J.-H. Kim, and J. Spencer,
[*Nearly perfect matchings in regular simple hypergraphs*](https://math.nyu.edu/~spencer/papers/alonkimjs.pdf),
Israel J. Math. 100 (1997), 171--187.  The paper explicitly says that the
proof does not give a good dependence of (\delta,D_0) on
(K,\epsilon).

To use this result here one would have to verify, for

\[
K=2m,\qquad \epsilon=o(m^{-1/2}),
\tag{1.1}
\]

both

\[
m^{-2}\le\delta(2m,\epsilon)
\quad\text{and}\quad
D\ge D_0(2m,\epsilon).
\tag{1.2}
\]

Neither inequality follows from the theorem.  The assertion
"(m^{-2}=o(1)), hence Pippenger--Spencer applies" reverses these
quantifiers.

## 2. Uniformity enters the classical proof in more than the round count

The proof in Alon--Kim--Spencer makes the fixed-(K) dependence visible.

* Theorem 2.1 begins with "Let (K\ge3) be fixed."
* Their random bite marks each edge with probability (1/D), so the
  covered proportion per bite is (e^{-K}+o(1)), not an absolute
  constant.
* Their "limited effect" bound is (K(K+1)), written as (O(1)) only
  because (K) is fixed.
* The independence approximation for the (K-1) other vertices of an
  edge uses inclusion--exclusion with (3^{K-1}) terms, again written as
  (O(1)) only for fixed (K).
* The concentration and local-lemma dependency bounds suppress further
  (K)-dependent constants, and every (O(\cdot)) constant in the main
  theorem is declared to depend on (K).

Replacing (1/D) by (\gamma/(KD)) is a sensible new slow-bite design,
but it is not a verbatim invocation of the classical proof.  Its residual
concentration and regeneration estimates have to be proved with all
(K)-dependence retained.

There is also a clean calibration showing why uniformity cannot disappear
from a general theorem.  Let \(q\) be a prime power and take the line
hypergraph of the projective plane of order \(q\).  It is

\[
K=q+1\text{-uniform},\qquad D=q+1\text{-regular},\qquad
\Delta _2=1,
\]

but every two edges meet, so its matching number is one.  Take the disjoint
union of \(t_q=\lceil e^q\rceil\) copies.  The resulting sequence has

\[
K=\Theta(\log N),\qquad \Delta_2/D=1/(q+1)=o(1),
\]

while every matching covers only a \(1/q+o(1)\) fraction of the vertices.
This example does not satisfy \(D\gg\log N\), so it does not refute a
stronger theorem containing a degree-versus-size hypothesis.  It does
rigorously refute the claim that small relative pair codegree alone is
uniform in \(K\), or that \(K\) enters only through the number of rounds.

The 2025 Gould--Kelly theorem does not remove this issue.  Its main
matching theorem assumes the hierarchy

\[
1/D\ll1/A\ll\gamma\ll1/K\le1,
\tag{2.1}
\]

which likewise fixes (K) before sending (D\to\infty); see
S. Gould and T. Kelly,
[*Advancing the Rödl Nibble*](https://arxiv.org/abs/2511.11375),
Theorem 1.4.

## 3. Where the claimed (N/\sqrt m) formula comes from

For a **simple/linear**, (K)-uniform, (D)-regular hypergraph, Grable's
estimate is quoted by Alon--Kim--Spencer as

\[
O_K\!\left(
N(D/\log N)^{-1/(2K-1+\eta)}
\right),
\tag{3.1}
\]

for fixed (K,\eta) and sufficiently large (D) depending on them.
For the tight packet parameters

\[
K=2m,\qquad
\log D=2m\log m-2m+O(\log m),
\tag{3.2}
\]

a purely formal substitution in (3.1) gives

\[
\exp\!\left[-\frac{\log(D/\log N)}{2K+O(1)}\right]
=m^{-1/2+o(1)}.
\tag{3.3}
\]

This is the source of the proposed leave.  But (3.1) requires pair
codegree at most one.  Our pair codegree is \(D/m^2\), not one.

For comparison, the Alon--Kim--Spencer simple-hypergraph bound

\[
O_K(ND^{-1/(K-1)})
\tag{3.4}
\]

would formally give (N/m^{1+o(1)}), but it is inapplicable for the same
reason and has an uncontrolled (K)-dependent constant.

Vu's theorem is the relevant classical replacement when the codegree is
(C>1).  An exact statement is reproduced as Theorem 1.3 in
D. Y. Kang, D. Kühn, A. Methuku, and D. Osthus,
[*New bounds on the size of nearly perfect matchings in almost regular
hypergraphs*](https://arxiv.org/abs/2010.04183), from the original theorem
of V. Vu,
[*New bounds on nearly perfect matchings in hypergraphs: higher codegrees
do help*](https://doi.org/10.1002/1098-2418(200008)17:1%3C29::AID-RSA4%3E3.0.CO;2-W).
It is (0.3), with (D_0,c), and the implicit constant depending on (K).
Substitution of (C/D=\Theta(m^{-2})) gives (0.4), not (3.3).

Thus no classical quantitative theorem cited in the proposal produces a
vanishing leave from the audited pair-codegree alone.

## 4. The actual packet codegree arithmetic

Let

\[
r=m-q_0<m,\qquad q_0=a\sqrt m+O(1),
\tag{4.1}
\]

and let the vertices be the (r)-sets of ([2m]).  A cyclic packet has
(K=2m) such interval vertices, and every target has degree

\[
D=\frac{r!(2m-r)!}{2}.
\tag{4.2}
\]

For a fixed interval in a packet there are two Johnson-distance-one
intervals.  Orbit double counting therefore gives

\[
\frac{\operatorname{codeg}(S,T)}D
=\frac{2}{r(2m-r)}
=\frac{2+o(1)}{m^2}
\tag{4.3}
\]

for adjacent (r)-sets.  The other distance strata are smaller; at the
disjoint endpoint the ratio is exponentially small because (r<m).
Hence

\[
\boxed{\Delta_2/D=(2+o(1))/m^2.}
\tag{4.4}
\]

The suggested (\Theta(1/m)) antipodal pair is imported from a different
middle-wreath catalogue.  At the exact middle rank, complementary pairs
have relative codegree one, but the protected formulation contracts each
complementary pair into one atom.  At the lower annular rank (r<m), a
disjoint pair is not complementary and is not extremal.

The known variable-rank Grable sufficient condition is stronger than
mere \(\Delta_2/D=o(1)\): in the present notation it requires

\[
\Delta_2=o\!\left(\frac{D}{K\log N}\right).
\tag{4.5}
\]

The packet catalogue is exactly constant-critical for this condition.
Indeed, using \(K=2m\), (4.4), and
\(\log N=2m\log2+O(\log m)\),

\[
\boxed{
\frac{K\Delta_2\log N}{D}
=8\log2+o(1),}
\tag{4.6}
\]

not \(o(1)\).  Thus even the classical result specifically designed to
retain growing-rank dependence does not cover this packet hypergraph.  See
D. A. Grable,
[*More-than-nearly-perfect packings and partial designs*](https://doi.org/10.1007/s004930050053),
Combinatorica 19 (1999), 221--239.

For the two-packet protected component, the independently audited bounds
are

\[
\Delta_2/D=O(m^{-3/2})
\tag{4.7}
\]

over the full protected support, and at the tight rank the sharper

\[
\Delta_2/D\le(5+o(1))/m^2.
\tag{4.8}
\]

These are favorable time-zero estimates, but the preceding theorem audit
shows that they are not themselves an integral matching theorem.

## 5. The common-core configuration hypergraph is not in this regime

For the synchronized common-core tight-path configuration hypergraph, the
target part of an edge has size

\[
K_{\rm cc}=(\sqrt\pi+o(1))m^{3/2},
\tag{5.1}
\]

not (2m).  Its audited maximum relative codegree satisfies

\[
\Delta_2/D\le4/m,
\tag{5.2}
\]

and every edge has normalized vertical-spine pair mass
(\Omega(\sqrt m)).  In particular,

\[
K_{\rm cc}\Delta_2/D=\Theta(\sqrt m),
\tag{5.3}
\]

so even the favorable (K\Delta_2/D=o(1)) pilot condition fails.

There is an additional applicability issue: the roots have degree (D),
whereas signed target orbits have degrees

\[
D\,b_q/\Lambda_q,
\tag{5.4}
\]

which are not uniformly (1+o(1)) times one common scale near the active
boundary.  The exact fractional matching handles these orbit imbalances,
but ordinary Pippenger--Spencer regularity does not.

Thus the (K=2m) packet audit cannot be used as a black box for the
common-core configuration hypergraph.

## 6. The exact growing-(K) conclusion that is justified

The following one-bite lemma is uniform in (K).

### Lemma 6.1 (one isolated slow bite)

Let (\mathcal H) be a (K)-uniform (D)-regular hypergraph.  Mark every
edge independently with probability

\[
p=\frac{\gamma}{KD},\qquad0<\gamma\le1,
\tag{6.1}
\]

and retain a marked edge iff it meets no other marked edge.  The retained
edges form a matching, and some outcome covers at least

\[
\frac{\gamma e^{-\gamma}+o(1)}K\,|V(\mathcal H)|
\tag{6.2}
\]

vertices as (KD\to\infty).

#### Proof

An edge meets at most (K(D-1)) other edges.  Conditional on being marked,
it is isolated with probability at least

\[
(1-p)^{K(D-1)}=e^{-\gamma+o(1)}.
\]

For a fixed vertex, the events that two different incident edges are
retained are disjoint.  Summing the retention probabilities of its (D)
incident edges gives coverage probability at least
((\gamma e^{-\gamma}+o(1))/K).  Sum over vertices and choose an outcome
at least as good as the expectation. \(\square\)

For the tight packet (K=2m), Lemma 6.1 supplies one matching bite
covering (\Theta(N/m)) targets.  Reaching density (m^{-1/2}) requires

\[
\Theta(K\log m)=\Theta(m\log m)
\tag{6.3}
\]

successive bites whose residual degrees continue to regenerate.
Lemma 6.1 supplies no such regeneration.

Moreover, the protected component catalogue has an explicit
point-balanced residual of density (1-\Theta(m^{-1/2})) containing no
edge.  This does not disprove the existence of a good random trajectory,
but it proves that regeneration cannot be required for every dense
balanced residual.  A positive proof must control its chosen trajectory
or add an absorber/global resolution.

## 7. What remains open

There is one further exact bookkeeping point about the proposed
correlated leave.  Suppose one synchronized family selects (s) cyclic
packets and hence contributes

\[
                         M=ns=N_{q_0}-L
\tag{7.1}
\]

occurrences at every deeper rank.  If (R_q) is its repeat count and

\[
 \widetilde E_q=R_q-(M-N_q)_+\ge0
\tag{7.2}
\]

is repeat excess above the forced floor, then the hole count is exactly

\[
                  H_q=(N_q-M)_+ + \widetilde E_q.
\tag{7.3}
\]

Thus sharing the packet family really can remove the scalar
(\sqrt m)-loss.  For (q_0=a\sqrt m),

\[
 {N_{q_0+d}\over N_{q_0}}
 =1-{2ad\over\sqrt m}+O_a(d^2/m),
\tag{7.4}
\]

so if (L=O(N_{q_0}/\sqrt m)), the deficiency term in (7.3) survives
for only (O_a(1)) ranks and

\[
                  \sum_{q\ge q_0}(N_q-M)_+
                  =O_a(N_{q_0}/\sqrt m)=o(W).
\tag{7.5}
\]

What equality of the selected packet family does **not** control is the
second term.  A positive correlated-leave theorem must prove

\[
                         \sum_q\widetilde E_q=o(W),
\tag{7.6}
\]

or an equivalent compiler/repair statement.  Entrance-rank matching by
itself gives no information about these deeper-rank repeats.

The exact usable conclusions are therefore:

* the maximum pair codegree at the original tight rank really is
  (\Theta(D/m^2)), not (\Theta(D/m));
* a uniform growing-(K) first bite is available and quantitatively
  efficient;
* none of Pippenger--Spencer, Grable, Alon--Kim--Spencer, Vu, or the 2025
  Gould--Kelly theorem supplies the required diagonal iteration;
* even a hypothetical (N/\sqrt m) leave separately at each Gaussian
  rank would aggregate to (\Theta(W)).  Correlated leaves could avoid
  this arithmetic, but correlation is an additional theorem, not a
  consequence of the classical nibble.

So the live gate is precisely a **trajectory-specific correlated
growing-uniformity nibble or absorber**, not the applicability of a
classical fixed-uniformity theorem.
