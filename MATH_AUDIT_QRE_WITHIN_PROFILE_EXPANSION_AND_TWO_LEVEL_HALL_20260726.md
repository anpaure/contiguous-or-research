# Audit of within-profile QRE expansion and the two-level Hall gate

Date: 2026-07-26

Method: pure mathematics only.  No computation, solver, finite search, or
web input is used.

## 0. Verdict

The component-expansion argument in
`MATH_THEOREM_QRE_WITHIN_PROFILE_COMPONENT_EXPANSION_20260726.md` is
correct.  In a safe diffuse ordered target profile, after deleting a
relative fraction at most

\[
                         2q e^{-cd},
\]

every raw subfamily has lower, respectively upper, neighborhood at least

\[
                         K\,|\mathcal A|,
 \qquad                  K=(3/2)^q.                 \tag{0.1}
\]

There is one minor repair in the full-mass argument: half-count safety
should be proved directly under the fixed-cardinality law, rather than by
conditioning a Bernoulli estimate and omitting its \(O(\sqrt m)\) cost.
The direct hypergeometric estimate gives exactly the stated conclusion.

However, (0.1) does **not** combine abstractly with a size-weighted
profile-quotient flow, even if that quotient flow has fixed positive
capacity slack.  Cross-profile competition can defeat raw Hall by a
constant factor while every individual profile arc is \(K\)-expanding.

The exact additional datum needed by the elementary two-level argument is
an *unweighted incoming profile congestion*.  If
\(\alpha_{ij}\) is the fraction of target profile \(i\) assigned to owner
profile \(j\), then the sufficient condition is

\[
 \max_j\sum_i\alpha_{ij}
       \le {K\over1+\delta}.                         \tag{0.2}
\]

The existing quotient theorem controls
\(\sum_i |L_i|\alpha_{ij}\), not (0.2).  The two statements are not
interchangeable.

## 1. Audit of the one-block ledgers

Fix a lower block, write its target half counts as \((a,c)\), put
\(t=a+c\le d\), and evaluate statuses in the required source-rank
matching \(\pi_{t+1}\).  If the target has \(f\) full matching edges,
then

\[
 p=a-f,\qquad s=c-f,\qquad z=d-a-c+f                 \tag{1.1}
\]

are its numbers of \(A\)-single, \(C\)-single, and empty edges.
Lower promotion preserves the exact full-edge set.

On the shore obtained by adding an \(A\)-endpoint, every target has
degree \(z\), while every source has reverse degree \(p+1\).  On the
\(C\)-shore the reverse degree is \(s+1\).  The shores have different
ordered half counts and hence are disjoint.  Edge counting therefore
gives, for every subfamily of one full-edge component,

\[
 |N(\mathcal D)|
 \ge z\left({1\over a-f+1}+{1\over c-f+1}\right)|\mathcal D|.
                                                               \tag{1.2}
\]

For a uniformly chosen target with the fixed half counts,

\[
                         F\sim\operatorname{Hyp}(d,c,a).          \tag{1.3}
\]

Writing \(x=a/d,y=c/d\), the large-\(d\) value of the factor in
(1.2), at \(F/d=xy\), is

\[
                         {1-x\over x}+{1-y\over y}.               \tag{1.4}
\]

On

\[
 1/4\le x,y\le3/4,\qquad x+y\le1,                 \tag{1.5}
\]

this is at least \(2\).  Uniform continuity on the compact region,
together with a hypergeometric tail estimate, therefore gives absolute
\(c,\varepsilon>0\) such that

\[
 |F-ac/d|\le\varepsilon d
 \quad\Longrightarrow\quad R^-(F)\ge3/2,
 \qquad
 \Pr\{|F-ac/d|>\varepsilon d\}\le2e^{-cd}.          \tag{1.6}
\]

All denominators in (1.2) are positive on the stated region.  No
randomness of the matching array is used.

For the upper sign, removal of one endpoint of a full edge preserves the
exact empty-edge set.  The two reverse degrees are again \(a-f+1\) and
\(c-f+1\), and the union factor is

\[
 f\left({1\over a-f+1}+{1\over c-f+1}\right).       \tag{1.7}
\]

At \(F/d=xy\), (1.7) tends to

\[
                         {y\over1-y}+{x\over1-x},                  \tag{1.8}
\]

which is at least \(2\) when \(x+y\ge1\).  This verifies the upper
one-block estimate as written.

## 2. Audit of tensoring and exceptional mass

Fix the exterior target configuration and, in each of the selected
blocks, the preserved full-edge set below or empty-edge set above.  For a
fixed side word, the global graph is a tensor product of biregular local
graphs.  Its left and right degrees are the products of the local
degrees, so edge counting gives the product of the local expansion
ratios for **every** raw subfamily; no product-expansion theorem is being
assumed.

Different side words have different ordered source half-count profiles,
and hence disjoint source shores.  Summing over all side words turns the
sum of the products into the product of the sums.  Different preserved
edge sets, or different exterior configurations, also give disjoint
source components.  Thus arbitrary unions of good components retain the
factor \((3/2)^q\).

Under the uniform law on one ordered target profile, the selected blocks
are independent.  A union bound applied to (1.6) gives bad-component mass
at most \(2q e^{-cd}\).  Therefore this mass is \(o(1)\) whenever
\(q e^{-cd}=o(1)\), as required.

For completeness, the global safety estimate can be made without the
minor conditioning ambiguity in the source note.  If \(T\) is uniform
on \(\binom{[2m]}{m-q}\), then for every fixed half-block \(A_j\),

\[
 |T\cap A_j|
 \sim\operatorname{Hyp}(2m,m-q,d).                 \tag{2.1}
\]

Its mean is \(d/2+O(dq/m)\), and the fixed-population Hoeffding bound
gives

\[
 \Pr\{|T\cap A_j|-d/2|>d/4\}\le2e^{-c_0d}.         \tag{2.2}
\]

The same holds for \(C_j\), so a direct union bound gives unsafe mass
\(O((m/d)e^{-c_0d})=o(1)\).  No \(O(\sqrt m)\) conditioning loss occurs.
The Bernoulli-conditioning proof for the number of below-centre blocks
is harmless, because its failure probability is \(e^{-\Omega(m/d)}\),
which remains \(o(1)\) after multiplication by \(O(\sqrt m)\).  Since
\(q=o(m/d)\), diffuse profiles have full asymptotic mass.  Residual
coordinates of total size \(O(d)\) do not change these estimates outside
an \(o(1)\) family of residual fibres.

This completes the audit of the within-profile theorem.

## 3. The exact two-level congestion lemma

Let

\[
 L=\mathop{\dot\bigcup}_{i\in I}L_i,
 \qquad
 R=\mathop{\dot\bigcup}_{j\in J}R_j                 \tag{3.1}
\]

be target and owner partitions.  For every allowed pair \((i,j)\), let
\(G_{ij}\subseteq L_i\times R_j\) be a bipartite graph satisfying

\[
 |N_{ij}(S)|\ge K|S|
 \qquad(S\subseteq L_i).                            \tag{3.2}
\]

Let \(\alpha_{ij}\ge0\) be supported on allowed pairs and satisfy

\[
                         \sum_j\alpha_{ij}=1
 \qquad(i\in I).                                    \tag{3.3}
\]

Put

\[
                         C=\max_j\sum_i\alpha_{ij}.               \tag{3.4}
\]

### Theorem 3.1 (two-level Hall with profile congestion)

For every raw family \(\mathcal A\subseteq L\),

\[
                         |N_G(\mathcal A)|
                         \ge {K\over C}|\mathcal A|.              \tag{3.5}
\]

In particular, (0.2) implies raw \((1+\delta)\)-expansion.

#### Proof

Write \(\mathcal A_i=\mathcal A\cap L_i\).  Since the owner profiles
are disjoint,

\[
 |N_G(\mathcal A)|
 =\sum_j |N_G(\mathcal A)\cap R_j|.                \tag{3.6}
\]

For a fixed \(j\), (3.2) gives

\[
 |N_G(\mathcal A)\cap R_j|
 \ge K\max_{i:\alpha_{ij}>0}|\mathcal A_i|.         \tag{3.7}
\]

Moreover,

\[
 \sum_i\alpha_{ij}|\mathcal A_i|
 \le\left(\sum_i\alpha_{ij}\right)
       \max_{i:\alpha_{ij}>0}|\mathcal A_i|
 \le C\max_{i:\alpha_{ij}>0}|\mathcal A_i|.        \tag{3.8}
\]

Combining (3.7)--(3.8), summing over \(j\), and using (3.3) yields

\[
 |N_G(\mathcal A)|
 \ge {K\over C}\sum_{i,j}\alpha_{ij}|\mathcal A_i|
 ={K\over C}|\mathcal A|.                          \tag{3.9}
\]

This proves the theorem. \(\square\)

The lemma also gives a fractional-flow interpretation.  Expansion
(3.2) lets profile \(i\) send its entire unit demand through arc
\((i,j)\) with uniform right capacity \(1/K\).  Scaling by
\(\alpha_{ij}\) and superposing the arc flows gives owner load at most
\(C/K\).

## 4. Size-weighted quotient slack does not control congestion

A conventional quotient flow has numbers \(f_{ij}\ge0\) satisfying

\[
 \sum_j f_{ij}=|L_i|,
 \qquad
 \sum_i f_{ij}\le(1-\eta)|R_j|.                   \tag{4.1}
\]

The associated row probabilities are

\[
                         \alpha_{ij}={f_{ij}\over|L_i|}.          \tag{4.2}
\]

Equation (4.1) controls

\[
                         \sum_i |L_i|\alpha_{ij},                 \tag{4.3}
\]

whereas Theorem 3.1 needs a bound on
\(\sum_i\alpha_{ij}\).  There is no abstract implication between them.

### Proposition 4.1 (sharp cross-profile counterexample, even with full
arc visibility)

For every integer \(k\ge2\), every fixed \(0<\eta<1\), and every
sufficiently large \(n\), there is a two-level graph such that:

1. every used profile arc is \(k\)-expanding on every raw subset;
2. every full target profile sees **every** owner in its adjacent owner
   profile;
3. the quotient flow has owner slack \(\eta\); but
4. the raw graph has a Hall cut of ratio \(1/2\).

#### Proof

Take \(p=2k\) target profiles.  Split each as

\[
                         L_i=A_i\mathbin{\dot\cup}B_i,
 \qquad                  |A_i|=|B_i|=n.                         \tag{4.4}
\]

Take one owner profile \(R_1\) of size

\[
                         |R_1|=\left\lceil{2pn\over1-\eta}\right\rceil,
                                                                    \tag{4.5}
\]

and split it as \(R_1=C\mathbin{\dot\cup}D\), where \(|C|=kn\).
For every \(i\), put all edges from \(A_i\) to \(C\) and all edges from
\(B_i\) to \(D\), with no other edges on that arc.  Since

\[
 |D|=|R_1|-kn\ge kn,                                             \tag{4.6}
\]

every subfamily contained in just one of \(A_i,B_i\) expands by at least
\(k\).  If a subfamily meets both, its neighborhood is all of \(R_1\),
whose size is at least \(2kn\).  Thus, for every \(S\subseteq L_i\),

\[
                         |N_{i1}(S)|\ge k|S|.                    \tag{4.7}
\]

Moreover,

\[
                         N_{i1}(L_i)=C\cup D=R_1,                \tag{4.8}
\]

so uniform whole-arc visibility holds with \(\zeta=0\).

Send \(f_{i1}=|L_i|=2n\) in the quotient.  Then

\[
 \sum_i f_{i1}=2pn\le(1-\eta)|R_1|,               \tag{4.9}
\]

so the quotient has at least the required slack.  But

\[
 N_G\left(\mathop{\dot\bigcup}_{i=1}^pA_i\right)=C,
 \qquad |C|=kn={1\over2}\left|\mathop{\dot\bigcup}_{i=1}^pA_i\right|.
                                                                    \tag{4.10}
\]

Thus raw Hall fails by a factor two, even though every full arc sees the
entire owner profile.  The failure is the alignment of one good internal
component \(A_i\to C\) across all target profiles. \(\square\)

Taking \(k\ge K=(3/2)^q\) shows that arbitrarily large within-arc
expansion does not repair the logical gap.

The preceding example is abstract, but the same phenomenon occurs in an
actual legal rank-twisted atlas.

### Proposition 4.2 (literal rank-independent component cut)

Assume for simplicity that the macroblocks contain all \(2m\)
coordinates.  Fix one bijection \(\pi_j:A_j\to C_j\) in every block and
use it at **every** local rank:

\[
                         \pi_{j,k}=\pi_j\qquad(0\le k\le2d).       \tag{4.11}
\]

For every fixed \(A>0\) and
\(q=A\sqrt m+O(1)\), the resulting maximal lower graph has a target
family of \(\Omega_A(N_q)\) vertices whose neighborhood has size at most

\[
                         e^{-A^2/3}|\mathcal A|                  \tag{4.12}
\]

for all sufficiently large \(m\).  Hence deleting \(o(N_q)\) targets
cannot repair raw Hall in this deterministic atlas.  The complementary
family gives the identical conclusion on the upper sign.

#### Proof

The fixed block matchings combine into one perfect matching of the
\(2m\) coordinates.  For a target or source, let \(F\) denote its exact
set of full matching edges.  Every lower compatible extension promotes
empty edges to singleton edges and therefore preserves \(F\).

Fix an exact set \(F\) of \(f\) matching edges.  Let \(\mathcal A_F\)
be all rank-\(m-q\) targets having full-edge set exactly \(F\), and let
\(\mathcal X_F\) be the corresponding middle sources.  Direct status
counting gives

\[
\begin{aligned}
 |\mathcal A_F|
   &=\binom{m-f}{f+q}2^{m-q-2f},\\
 |\mathcal X_F|
   &=\binom{m-f}{f}2^{m-2f}.                         \tag{4.13}
\end{aligned}
\]

Every source in \(\mathcal X_F\) has \(m-2f\) singleton edges and is
adjacent to a member of \(\mathcal A_F\) by deleting any \(q\) of them.
Conversely, preservation of \(F\) excludes every other source.  Thus

\[
 N(\mathcal A_F)=\mathcal X_F,
 \qquad
 r_f:={|\mathcal X_F|\over|\mathcal A_F|}
 =2^q{\binom{m-f}f\over\binom{m-f}{f+q}}
 =\prod_{i=1}^q{2(f+i)\over m-2f-i+1}.             \tag{4.14}
\]

The last product is increasing in \(f\).  Put

\[
                         f_0=\left\lfloor{m-2q\over4}+{q\over16}
                               \right\rfloor.                    \tag{4.15}
\]

Uniformly for \(f=f_0+O(1)\), Taylor expansion of (4.14) gives

\[
\begin{aligned}
 \log r_f
 &=\sum_{i=1}^q
   \log{m/2-q+q/8+2i+O(1)
             \over m/2+q-q/8-i+1+O(1)}\\
 &=-{q^2\over2m}+o(1)
  =-{A^2\over2}+o(1).                              \tag{4.16}
\end{aligned}
\]

Indeed, before division by the common scale \(m/2\), the sum of the
numerator-minus-denominator displacements is
\(-q^2/4+O(q)\); the quadratic Taylor remainder is
\(O(q^3/m^2)=o(1)\).  Monotonicity therefore implies

\[
                         r_f\le e^{-A^2/3}                         \tag{4.17}
\]

for every integer \(f\le f_0\), once \(m\) is large.

It remains to show that these components contain positive target mass.
For a uniform rank-\(m-q\) target, let \(\mathbf F\) be its number of
full matching edges.  Then

\[
 \mu:=\mathbb E\mathbf F
 ={(m-q)(m-q-1)\over2(2m-1)}
 ={m-2q\over4}+O_A(1),                              \tag{4.18}
\]

and \(\operatorname{Var}\mathbf F=O(m)\).  The latter follows, for
example, from the Poincare inequality on the fixed-size slice: exchanging
one selected and one unselected coordinate changes \(\mathbf F\) by at
most one.  Since

\[
                         f_0-\mu={q\over16}+O_A(1),                \tag{4.19}
\]

Cantelli's inequality gives an \(A\)-dependent constant \(c_A>0\) such
that

\[
                         \Pr\{\mathbf F\le f_0\}\ge c_A.         \tag{4.20}
\]

Let \(\mathcal A\) be the union of \(\mathcal A_F\) over all exact
full-edge sets with \(|F|\le f_0\).  Distinct \(F\)'s have disjoint
source components, so (4.17)--(4.20) give

\[
 |\mathcal A|\ge c_A N_q,
 \qquad
 |N(\mathcal A)|
 =\sum_{|F|\le f_0}|\mathcal X_F|
 \le e^{-A^2/3}|\mathcal A|.                       \tag{4.21}
\]

This proves the proposition. \(\square\)

Complementation preserves the fixed matching, interchanges lower full
edges with upper empty edges, and reverses every compatible inclusion.
It therefore proves the asserted upper analogue without a second count.

Proposition 4.2 does not address the independent-rank random atlas in
`QRE_A`; independence was introduced precisely to break this common
full-edge invariant.  It does show inside the literal model that the
deterministic profile flow, uniform whole-arc visibility, and the
within-profile theorem cannot imply raw Hall by themselves.

## 5. Consequence for QRE

The within-profile theorem eliminates cuts contained in a single safe
diffuse ordered profile.  The profile quotient eliminates cuts whose
dual potentials are constant on the chosen quotient cells.  The two
facts together still do not eliminate a raw family assembled from many
ordered profiles whose neighborhoods align in the same portions of the
owner profiles.

For the direct two-level route, the minimum remaining statement is now
precise.  One must construct profile-routing probabilities supported on
the literal one-hit arcs such that, after the exceptional profiles and
components are removed,

\[
 \sum_\kappa\alpha_{\tau\kappa}=1
 \quad\text{for every retained target profile }\tau,
 \qquad
 \max_\kappa\sum_\tau\alpha_{\tau\kappa}
       \le{(3/2)^q\over1+\delta_A}.                 \tag{5.1}
\]

Then Theorem 3.1 proves raw `QRE_A` immediately.  The existing
size-weighted Gaussian profile flow does not prove the second inequality
in (5.1).  Conversely, Proposition 4.1 shows that some condition of this
cross-profile type cannot be omitted from an abstract gluing theorem.

This is a raw maximal-graph statement only.  It makes no selected-axis,
packet-chronology, or coefficient-one claim.  In the diverse-order
compiler, whole-packet conditional expectations eliminate only the
rounding gap **after** one has constructed packet-option distributions
with small nonlinear hole or collision cost.  They do not convert a
maximal-graph raw flow into such distributions, and they do not create
the missing cross-profile dispersion in (5.1).
