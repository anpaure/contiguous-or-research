# Z23: isolated line-gadget trap bounds and the exact unweighted high-overlap obstruction

Date: 2026-07-25

Method: pure mathematics only.  No computation, finite search, solver, or
web input is used.

## 0. Verdict

The D-scale line-arrangement example in
`MATH_ATTACK_Z22_BOUNDED_DISPLACEMENT_LINE_ARRANGEMENT_D_SCALE_AUDIT_20260725.md`
is a genuine obstruction to a universal **weighted colouring** theorem.  It
does not produce the corresponding unweighted obstruction in the isolated
catalogue.  The exact conclusions are as follows.

Let (T) be the number of chunk tags, let every raw tag fibre have size
(A), and put

\[
        \mu=pA=m^{11/6-o(1)}
\tag{0.1}
\]

for the pointwise Bernoulli-isolation mean.  Let

\[
        \ell=\lfloor\sqrt{QH}\rfloor,
        \qquad g=\ell+2Q-1=(1+o(1))\ell,
        \qquad T=(1+o(1)){W\over g},
\tag{0.2}
\]

where (Q=m^{1/2+o(1)}), (Q=o(H)), and hence

\[
        {\mu\over Q^2}=m^{5/6-o(1)},
        \qquad
        {\mu\over Q^2\ell}=m^{1/3-o(1)}.
\tag{0.3}
\]

Partition every oriented tag fibre by its complete physical central
skeleton.  If ({\cal B}) is one skeleton bundle, Z22 Lemma 5.1 gives

\[
 { |{\cal B}|\over A}
 \le \xi,
 \qquad
 \xi\le
 {2\over
  \binom{m+H}{m}(m)_{\ell-1}(H)_{\ell-1}}
 =\exp[-(1-o(1))\ell\log m].
\tag{0.4}
\]

The main adaptive estimate proved below is this.  Consider any later
deletion-only residual stage of density (z\ge1/Q), and any residual
probability measure satisfying the atom bound

\[
             x_{U,P}\le {\Lambda\over z\mu}.
\tag{0.5}
\]

The uniform isolated point has \(z=1,\Lambda=2\), and a uniform residual
fibre of size at least \(z\mu/2\) again has \(\Lambda=2\).  A union of line
systems selects some number (R_U) of central skeleton bundles above tag
(U); put ({\cal R}=\sum_U R_U).  Even when this union is chosen after
the entire marking, isolation, and dynamic deletion history is visible,
the number (N_{\rm trap}(\alpha,z)) of tags on which the union carries
mass at least \(\alpha\) satisfies, with probability \(1-o(1)\),

\[
 \boxed{
 N_{\rm trap}(\alpha,z)
 \le N_{\rm exc}
      +{2\Lambda{\cal R}\over \alpha z\mu}
      +o(T/Q). }
\tag{0.6}
\]

Here (N_{\rm exc}=o(T/Q)) is the already allowed pointwise-pruning tag
exception.  The estimate is simultaneous for all post-sample bundle
unions and all (z\ge1/Q).  Consequently

\[
 {\cal R}=o\!\left({\alpha z\mu T\over\Lambda Q}\right)
       \quad\Longrightarrow\quad
 N_{\rm trap}(\alpha,z)=o(T/Q).
\tag{0.7}
\]

For (S) actual (n)-line systems, (n=\lceil\ell/2\rceil), one has
({\cal R}\le nS).  An anchor-disjoint packing has

\[
       S\binom n2\le W,
       \qquad nS=O(T),
\tag{0.8}
\]

and therefore, even at the last density (z=1/Q),

\[
 \boxed{
 N_{\rm trap}(\alpha,1/Q)
 \le O\!\left({\Lambda QT\over\alpha\mu}\right)+o(T/Q)
 =o(T/Q) }
\tag{0.9}
\]

for fixed \(\alpha>0\) and fixed \(\Lambda=O(1)\).  More generally, the
same conclusion holds whenever

\[
                    {\Lambda Q^2\over\alpha\mu}\longrightarrow0.
\tag{0.9a}
\]

Thus a union of all anchor-budget-compatible Z22 line systems cannot trap a
coefficient-scale number of isolated tags.

There are three independent unweighted reinforcements.

* With probability \(1-o(1)\), no common-anchor-frame block-coded line
  gadget of order at least \(C\sqrt{m/\log m}=o(Q)\) survives, even
  when carrier tails and interleaved filler transitions are chosen
  independently.  In particular, the original order-\(\Theta(\ell)\)
  Z22 gadget is absent hereditarily.
* With probability (1-o(1)), after deleting (o(T/Q)) candidate
  occurrences (or simply declaring the at most (o(T/Q)) affected tags
  exceptional), every retained tag--target pair has multiplicity at most
  one.  This destroys the parallel-variant amplification used by the
  adversarial rational weighted example.
* If line gadgets form conflict-separated bins, the tag--bin incidence
  graph satisfies Hall exactly and has a perfect integral transversal.
  No tag is lost.  More generally, if the line-conflict graph has no
  integral transversal, then some one path--target incidence has at least

  \[
       {d\over2eK}
  \tag{0.10}
  \]

  distinct line-neighbours, where (d) is the minimum residual tag
  degree and (K\le(2Q+1)\ell) is the number of protected claims of one
  path.  At (d\ge\mu/(2Q)), this is at least

  \[
       {\mu\over4eQ(2Q+1)\ell}
       =m^{1/3-o(1)}.
  \tag{0.11}
  \]

Thus an unweighted positive-density counterexample is not supplied by
the D-scale line construction.  For the intended uniform residual
measure \(\Lambda=2\) and fixed trapped mass \(\alpha>0\), any still
possible generalized line counterexample must simultaneously use at
least \(\Omega(\mu T/Q)\) post-isolation bundle incidences at density
\(1/Q\) to trap a positive fraction of the tags, and must create an
\(m^{1/3-o(1)}\)-fold common-anchor star.  No such actual geodesic
family is constructed here.  Controlling that high-overlap star, or the
equivalent cross-gadget pair energy, is the precise remaining boundary.

The atom condition (0.5) is essential.  An arbitrary post-sample measure
may concentrate mass one on one retained path.  Skeleton dispersion by
itself says nothing about such a reweighting.

## 1. Canonical skeleton partition and collision excess

Fix a tag (U).  The complete central data of a path are:

1. its owner at the first physical phase;
2. its ordered \(\ell-1\) central departures; and
3. its ordered \(\ell-1\) central arrivals.

These data partition the raw oriented fibre into bundles ({\cal B}).
The prefix and suffix buffers remain free inside a bundle.  The estimate
(0.4) applies to every bundle.

Let (N_{U,{\cal B}}) be the number of independently marked paths in
bundle ({\cal B}), before isolation, and define

\[
       C_U=\sum_{\cal B}(N_{U,{\cal B}}-1)_+.
\tag{1.1}
\]

The variable (C_U) is deliberately defined before isolation.  Every
later catalogue in this argument is obtained by deletion, so its bundle
occupancies are bounded by the same (N_{U,{\cal B}}).

### Lemma 1.1 (collision-excess expectation)

For every tag,

\[
          \mathbb E C_U\le {1\over2}\xi\mu^2.
\tag{1.2}
\]

The variables (C_U) are independent as (U) varies.

#### Proof

For every nonnegative integer (a),
((a-1)_+\le\binom a2).  Hence

\[
\begin{aligned}
 \mathbb E C_U
 &\le \sum_{\cal B}\mathbb E\binom{N_{U,{\cal B}}}{2}\\
 &=p^2\sum_{\cal B}\binom{|{\cal B}|}{2}\\
 &\le {p^2\over2}\sum_{\cal B}|{\cal B}|^2\\
 &\le {p^2\over2}
       \left(\max_{\cal B}|{\cal B}|\right)
       \sum_{\cal B}|{\cal B}|\\
 &\le {1\over2}p^2(\xi A)A
  ={1\over2}\xi\mu^2.
\end{aligned}
\tag{1.3}
\]

The raw marking variables belonging to distinct tagged fibres are
independent.  Each (C_U) is a function only of the marks in its own
fibre, proving the last assertion. \(\square\)

### Lemma 1.2 (deterministic adaptive bundle bound)

Let (0\le a_{U,{\cal B}}\le1) be chosen in an arbitrary way after all
marks, all isolation deletions, and all later deletion-only dynamics have
been exposed.  If

\[
          \sum_{\cal B}a_{U,{\cal B}}\le R_U,
\tag{1.4}
\]

then

\[
 \boxed{
 \sum_{\cal B}a_{U,{\cal B}}N_{U,{\cal B}}
       \le R_U+C_U. }
\tag{1.5}
\]

In particular, a union of at most (R_U) bundles contains at most
(R_U+C_U) retained paths above (U).

#### Proof

For every integer (N\ge0),

\[
       aN\le a+a(N-1)_+\le a+(N-1)_+.
\]

Sum this inequality over the bundles and use (1.1) and (1.4).
\(\square\)

The point of Lemma 1.2 is that no union bound over adaptive choices is
needed.  The entire post-sample choice is absorbed by the single random
quantity (C_U).

## 2. The adaptive trapped-tag theorem

Fix (z\ge1/Q).  Above every nonexceptional tag let (x_{U,P}) be a
probability measure on a deletion-only residual fibre and assume (0.5).
For an adaptive bundle profile (a_{U,{\cal B}}), call (U)
((\alpha,z))-trapped when

\[
   \sum_{\cal B}a_{U,{\cal B}}
       \sum_{P\in {\cal B}\ {m retained}}x_{U,P}
       \ge\alpha.
\tag{2.1}
\]

### Theorem 2.1 (uniform adaptive trap bound)

Let ({\cal R}=\sum_U R_U).  Put

\[
 Z_{\alpha,z}
 =\#\left\{U:
 C_U\ge {\alpha z\mu\over2\Lambda}\right\}.
\tag{2.2}
\]

For every realized marking and every adaptive bundle profile,

\[
 N_{\rm trap}(\alpha,z)
 \le N_{\rm exc}
      +{2\Lambda{\cal R}\over\alpha z\mu}
      +Z_{\alpha,z}.
\tag{2.3}
\]

Moreover

\[
 q_{\alpha,z}:=Pr\left(
 C_U\ge {\alpha z\mu\over2\Lambda}\right)
 \le {\Lambda\xi\mu\over\alpha z},
\tag{2.4}
\]

and, for every integer (s\ge1),

\[
 \Pr(Z_{\alpha,z}\ge s)
 \le
 \left({eTq_{\alpha,z}\over s}\right)^s.
\tag{2.5}
\]

For fixed \(\alpha>0\), polynomial \(\Lambda\), and all \(z\ge1/Q\),

\[
             Z_{\alpha,z}=o(T/Q)
\tag{2.6}
\]

simultaneously with probability (1-o(1)).  Equations (0.6)--(0.7)
follow.

#### Proof

By the atom bound, mass at least \(\alpha\) requires at least
\(\alpha z\mu/\Lambda\) distinct retained paths.  Lemma 1.2 therefore
gives, on every trapped nonexceptional tag,

\[
            R_U+C_U\ge {\alpha z\mu\over\Lambda}.
\tag{2.7}
\]

If (C_U<\alpha z\mu/(2\Lambda)), then
(R_U\ge\alpha z\mu/(2\Lambda)).  The number of such tags is at most
(2\Lambda{\cal R}/(\alpha z\mu)).  Add the tags counted by
(Z_{\alpha,z}) and the pre-existing exceptional tags.  This proves
(2.3).

Markov's inequality and Lemma 1.1 give

\[
 q_{\alpha,z}
 \le
 {\frac12\xi\mu^2\over
  \alpha z\mu/(2\Lambda)}
 ={\Lambda\xi\mu\over\alpha z},
\]

which is (2.4).  The indicators in (2.2) are independent.  Thus

\[
 \Pr(Z_{\alpha,z}\ge s)
 \le\binom Ts q_{\alpha,z}^{,s}
 \le\left({eTq_{\alpha,z}\over s}\right)^s,
\]

proving (2.5).

For simultaneous control over (z\ge1/Q), use the smallest threshold,
namely (z=1/Q).  With

\[
             s={T\over Q\log m},
\]

the right side of (2.5) is at most

\[
 \left(
 {e\Lambda\xi\mu Q^2\log m\over\alpha}
 \right)^{T/(Q\log m)}=o(1),
\tag{2.8}
\]

because (0.4) is exponentially small in \(\ell\log m\), while all other
factors in the base are polynomial.  Since
\(T/(Q\log m)=o(T/Q)\), (2.6) follows. \(\square\)

### Corollary 2.2 (exact incidence threshold)

At the original isolated point (z=1), trapping (T/Q) tags with
fixed mass \(\alpha\) requires

\[
        {\cal R}\ge
        (1-o(1)){\alpha\mu T\over2\Lambda Q}.
\tag{2.9}
\]

At the last deletion density (z=1/Q), it requires

\[
        {\cal R}\ge
        (1-o(1)){\alpha\mu T\over2\Lambda Q^2}.
\tag{2.10}
\]

Trapping a fixed positive fraction (eta T) at (z=1/Q) requires

\[
        {\cal R}\ge
        (1-o(1)){\alpha\eta\mu T\over2\Lambda Q}.
\tag{2.11}
\]

These are necessary conditions, not existence assertions.

#### Proof

Rearrange (2.3), use (N_{\rm exc}+Z_{\alpha,z}=o(T/Q)), and substitute
the stated values of \(N_{\rm trap}\) and \(z\). \(\square\)

## 3. Application to unions of actual Z22 line systems

An (n)-line Z22 system specifies one complete central skeleton above
each of its (n) distinct carrier tags.  Therefore a union of (S)
systems has

\[
                 {\cal R}\le nS.
\tag{3.1}
\]

This remains true if systems overlap: repeated selection of the same
bundle can only decrease the number of distinct selected bundles.

If their singleton crossing-anchor sets are pairwise disjoint, Z22
Theorem 2.1 gives

\[
              S\binom n2\le W.
\tag{3.2}
\]

Since (n=(1+o(1))\ell/2), (g=(1+o(1))\ell), and
(T=(1+o(1))W/g), equations (3.1)--(3.2) imply

\[
             {\cal R}\le {2W\over n-1}=O(T).
\tag{3.3}
\]

Substitution in Theorem 2.1 proves (0.9).  Equivalently, at density
(1/Q), the number of line systems needed merely to trap (T/Q) tags
is larger than the whole anchor-disjoint capacity by a factor

\[
             \Omega(\mu/Q^2)=m^{5/6-o(1)}.
\tag{3.4}
\]

At the original density the gap factor is \(\Omega(\mu/Q)\).  These gap
factors are stated for fixed \(\alpha>0\) and \(\Lambda=O(1)\); in
general they are divided by \(\Lambda/\alpha\).

This conclusion is about normalized mass and is unchanged by clearing a
rational denominator.  It is also stronger than bounding one fixed line
system: the selected union may depend arbitrarily on the realized
isolated sample.

## 4. Parallel tag--target variants disappear

The previous section counts exact central bundles.  There is a second
dispersion fact which is specific to the unweighted problem.

For a protected target (v) of rank (r) and a tag (U), let
(a_{U,v}) be the number of raw candidates above (U) claiming (v).
Let \(k_r\le g\) be the number of claims of rank \(r\) on each candidate.
Coordinate symmetry of the fully decorated raw fibre gives, whenever
\(v\subseteq U\) in the appropriate rank convention,

\[
             a_{U,v}={Ak_r\over\binom Mr},
             \qquad M=m+H.
\tag{4.1}
\]

Let (Y_{U,v}) be its marked count.

### Proposition 4.1 (tag--target simplicity after negligible cleanup)

With probability (1-o(1)), the number of marked candidate occurrences
which must be deleted in order to obtain

\[
                   d(U,v)\le1
\tag{4.2}
\]

for every retained tag--target pair is (o(T/Q)).  Equivalently, one may
declare (o(T/Q)) tags exceptional and retain every marked candidate on
all remaining tags.  The property is hereditary under isolation and all
later candidate deletions.

#### Proof

Using ((Y-1)_+\le\binom Y2), (4.1), and summing first over the targets
inside one carrier gives

\[
\begin{aligned}
 \mathbb E\sum_{U,v}(Y_{U,v}-1)_+
 &\le {T\mu^2\over2}
       \sum_{|r-m|\le Q}{k_r^2\over\binom Mr}.
\end{aligned}
\tag{4.3}
\]

Indeed, at rank \(r\), there are \(\binom Mr\) possible \(v\)'s above a
fixed carrier, and

\[
 \binom Mr {1\over2}
 \left({\mu k_r\over\binom Mr}\right)^2
 ={\mu^2k_r^2\over2\binom Mr}.
\]

Uniformly for (|r-m|\le Q=o(H)),

\[
 \binom Mr=\binom M{M-r}
 \ge\exp[\Omega(H\log(m/H))].
\tag{4.4}
\]

The numerator in (4.3) apart from (T) is polynomial in (m).
Consequently (4.3) is (o(T/Q)), in fact exponentially smaller than
(T/Q).  Markov's inequality gives the assertion with probability
(1-o(1)).  Deleting, for every pair ((U,v)), all but one of the
marked occurrences costs at most the sum in (4.3).  Alternatively, the
number of tags on which any deletion is required is bounded by the same
sum.  Isolation and later dynamics only delete candidates, so (4.2) is
hereditary. \(\square\)

All priority decorations are included on both sides of (4.1), so they
cancel in the ratio.  Proposition 4.1 concerns the genuine sampled
support before any artificial denominator-cleared parallel copying.
The adversarial Z22 weighted point put many line variants over each tag
through the same prescribed crossing data.  Proposition 4.1 shows that
this parallel-anchor mechanism is absent from the isolated support,
apart from the already coefficient-safe exceptional tags.

## 5. The exact Hall theorem for separated line bins

The weighted-colouring obstruction asks for many colours.  The
unweighted target asks only for one candidate per tag.  In the separated
case the distinction is exact.

Let the residual candidates be partitioned into bins.  A line bin
contains at most (b) candidates, on distinct tags, and any two
line-conflicting candidates belong to the same bin.  Candidates in
distinct bins have no line conflict.  A candidate outside the displayed
line systems may be regarded as a private singleton bin only under this
same separation hypothesis: it must have no relevant line conflict with
another bin or another private candidate.  Otherwise it belongs to the
cross-gadget sector of Sections 6--7.

### Theorem 5.1 (separated-bin Hall integrality)

Suppose a residual fractional measure saturates every tag and

\[
              \sum_{P\in G}x_P\le1
\tag{5.1}
\]

for every bin (G).  Then there is an integral choice of one candidate
from every tag with no line conflict.

In particular, (5.1) holds under (0.5) whenever

\[
                    b\Lambda\le z\mu.
\tag{5.2}
\]

At every relevant isolated or dynamic density, (5.2) holds for
\(b\le n=O(\ell)\), because \(\mu/(Q\ell)\to\infty\).

#### Proof

Form a bipartite graph whose left vertices are tags and whose right
vertices are bins; a candidate (P\in G) above (U) gives the edge
(UG).  Put weight (x_P) on that edge.  Tag saturation says every left
vertex has weighted degree one, while (5.1) says every right vertex has
weighted degree at most one.  For every tag set \(S\),

\[
\begin{aligned}
 |S|
 &=\sum_{U\in S}\sum_G x_{UG}\\
 &=\sum_{G\in N(S)}\sum_{U\in S}x_{UG}\\
 &\le |N(S)|.
\end{aligned}
\tag{5.2a}
\]

Thus Hall's condition holds, and Hall's theorem gives an integral
matching saturating every tag.  Its selected candidate edges use
distinct bins, hence create no line conflict.

Finally, a bin has at most (b) atoms, each at most
\(\Lambda/(z\mu)\), proving (5.2) sufficient. \(\square\)

For uniform fibres there is also a direct Hall count.  If every tag has
at least (d) candidates and every bin contains at most (b), then for
every tag set (S),

\[
           d|S|\le b|N(S)|.
\tag{5.3}
\]

Thus (d\ge b) implies Hall.  In particular, even at (z=1/Q),

\[
             d\ge {\mu\over2Q}\gg n.
\tag{5.4}
\]

The fillers in the Z22 adversarial rational construction are private
bins.  Hence that construction has a perfect unweighted matching even
though its cleared line copies violate the proposed weighted colouring
bound by a factor (n/2).

## 6. A local-lemma certificate for every remaining deficiency

Separated bins do not cover superposed gadgets which share candidates or
have cross-gadget conflicts.  Nevertheless Proposition 4.1 permits an
exact necessary condition for any unweighted obstruction.

Let \(\Gamma\) be the graph on residual candidates in which two candidates
on distinct tags are adjacent when the line-gadget union declares a
forbidden common target.  Assume every candidate claims at most (K)
such targets.  Define the common-anchor multiplicity

\[
 \rho=\max_{P,v\in P}
 \#\{P': P'\sim_\Gamma P
          \hbox{ with the edge witnessed by }v\}.
\tag{6.1}
\]

After Proposition 4.1, the neighbours counted in (6.1) lie on distinct
tags.  Multiple witnesses for one neighbour may be assigned arbitrarily
to one of their common targets.

### Lemma 6.1 (elementary symmetric local lemma)

Let events have probability at most (p), and suppose every event is
independent of all but at most (D) other events.  If

\[
                       ep(D+1)\le1,
\tag{6.2}
\]

then the probability that none of the events occurs is positive.

#### Proof

Put (x=1/(D+1)).  Since

\[
       x(1-x)^D
       ={1\over D+1}\left({D\over D+1}\right)^D
       \ge {1\over e(D+1)},
\]

(6.2) gives \(p\le x(1-x)^D\).  We include the usual induction.  For
every \(i\) and every set \(S\) not containing \(i\), claim

\[
 \Pr\!\left(A_i\mid\bigcap_{j\in S}\overline{A_j}\right)\le x.
\tag{6.2a}
\]

The assertion is immediate for \(S=\varnothing\).  Split a nonempty
\(S\) as \(S_1\cup S_2\), where \(S_1\) consists of neighbours of
\(A_i\) in the dependency graph.  There are at most \(D\) of them, and
\(A_i\) is independent of the sigma-algebra generated by the events in
\(S_2\).  Ordering \(S_1=\{j_1,\ldots,j_s\}\), the induction hypothesis
gives

\[
\begin{aligned}
 \Pr\!\left(A_i\mid\bigcap_{j\in S}\overline{A_j}\right)
 &\le
 {p\over
  \Pr(\bigcap_{j\in S_1}\overline{A_j}\mid
      \bigcap_{j\in S_2}\overline{A_j})}\\
 &=
 {p\over
  \prod_{h=1}^s
  \Pr(\overline{A_{j_h}}\mid
      \bigcap_{j\in S_2}\overline{A_j}
      \cap\bigcap_{a<h}\overline{A_{j_a}})}\\
 &\le {p\over(1-x)^s}
 \le {p\over(1-x)^D}
 \le x.
\end{aligned}
\tag{6.2b}
\]

This proves (6.2a).  Finally, order all events and multiply their
successive conditional nonoccurrence probabilities.  Each is at least
\(1-x>0\), so the joint avoidance probability is positive.  The case
\(D=0\) is immediate from independence. \(\square\)

### Theorem 6.2 (high common-anchor multiplicity is necessary in the stated conflict graph)

Let every residual tag fibre have at least (d) candidates.  If

\[
                       2eK\rho\le d,
\tag{6.3}
\]

then \(\Gamma\) has an independent transversal containing one candidate
from every tag.  Consequently, failure of an integral transversal
implies

\[
 \boxed{\rho>{d\over2eK}.}
\tag{6.4}
\]

#### Proof

Trim every fibre arbitrarily to size exactly (d), and choose one
candidate independently and uniformly from every tag.  For each edge
\(PQ\) of \(\Gamma\), let \(A_{PQ}\) be the event that both endpoints are
chosen.  Then

\[
                        \Pr(A_{PQ})={1\over d^2}.
\tag{6.5}
\]

Every candidate has degree at most (K\rho), by assigning each neighbour
to one of at most (K) witnessing targets.  Therefore at most
(dK\rho) edge events involve any fixed tag.  The event (A_{PQ})
depends only on the two endpoint-tag choices, so it is independent of
all but at most

\[
                       D\le2dK\rho-1
\tag{6.6}
\]

other edge events.  Equations (6.3), (6.5), and (6.6) give

\[
 ep(D+1)
 \le {e\over d^2}(2dK\rho)\le1.
\]

Lemma 6.1 supplies a choice with no conflict edge. \(\square\)

At a dynamic stage with (d\ge z\mu/2), (z\ge1/Q), and
(K\le(2Q+1)\ell), Theorem 6.2 says that any deficiency forces

\[
 \rho>
 {z\mu\over4eK}
 \ge
 {\mu\over4eQ(2Q+1)\ell}
 =m^{1/3-o(1)}.
\tag{6.7}
\]

This is a quotient-edge packing obstruction, not a marginal start
bound: one literal path and one literal target must support the displayed
number of distinct conflicting tagged paths.  A superposition of loose
line gadgets in which every used crossing anchor has multiplicity
\(o(\mu/(Q^2\ell))\) therefore has a full unweighted transversal for
the conflicts represented in \(\Gamma\).  This is a full target
transversal only when \(\Gamma\) contains every relevant cross-tag
forbidden pair.

## 7. Bounded-overlap superpositions

There is a complementary quantitative statement when conflict pairs are
assigned to gadgets.  Assign every line-generated conflict edge to one
genuine gadget containing its two endpoints.  Suppose:

* every assigned gadget has at most (b) candidates on distinct tags;
* every candidate belongs to at most (r) assigned gadgets; and
* the total fractional pair energy of unassigned conflicts is

  \[
       E_{\rm out}
       :=\sum_{\substack{PQ\ {\rm unassigned}\\
                         {\rm cross\mbox{-}tag\ conflict}}}x_Px_Q.
  \tag{7.0}
  \]

Under (0.5), the mass (a_G=\sum_{P\in G}x_P) of one gadget satisfies

\[
           a_G\le {\Lambda b\over z\mu},
       \qquad
           \sum_Ga_G\le rT.
\tag{7.1}
\]

Independent one-per-tag sampling therefore gives

\[
\begin{aligned}
 \mathbb E[\hbox{assigned conflict edges}]
 &\le {1\over2}\sum_Ga_G^2\\
 &\le {\Lambda brT\over2z\mu}.
\end{aligned}
\tag{7.2}
\]

Delete one endpoint tag from every realized conflict edge.  Some outcome
leaves an integral line-conflict-free selection missing at most

\[
             {\Lambda brT\over2z\mu}+E_{\rm out}
\tag{7.3}
\]

tags.  At (z=1/Q), this is (o(T/Q)) provided

\[
          \Lambda brQ^2=o(\mu),
          \qquad E_{\rm out}=o(T/Q).
\tag{7.4}
\]

For (b\asymp\ell), (7.4) permits

\[
              r=o\!\left({\mu\over\Lambda\ell Q^2}\right)
                =m^{1/3-o(1)}.
\tag{7.5}
\]

This agrees at exponent scale with the common-anchor threshold in (6.7).
It is an internal check that both arguments identify
\(m^{1/3-o(1)}\) as the first uncontrolled scale.  No deterministic
identification of the gadget-membership parameter \(r\) with the
common-anchor parameter \(\rho\) is claimed.

## 8. Strict canonical Z22 gadgets are absent at large order

This section is an independent reinforcement and has deliberately narrow
scope.  It concerns the strict block-coded images of Z22 Lemmas 1.1--1.2:
one common four-coordinate block system, common padding blocks, and one
common carrier reservoir (R).  It does **not** cover arbitrary
displacement-zero geodesics with independently chosen carrier tails.

Put

\[
             B=\binom{m+H}{m}.
\tag{8.1}
\]

For one fixed strict block-coded (r)-line image, each of its (r)
distinct tags must contain a marked path with one prescribed first
physical owner.  That subfibre has raw relative size at most (2/B),
including reversal.  Since markings on distinct tagged fibres are
independent,

\[
 \Pr(\hbox{the fixed image survives})
       \le\left({2\mu\over B}\right)^r.
\tag{8.2}
\]

The number of strict images of order (r\le\ell) is at most

\[
 \exp\{O(m\log m)+O((g+r)\log m)+O(r^2\log r)\}.
\tag{8.3}
\]

Indeed, one global labelled coordinate ordering encodes all sign blocks,
padding blocks, common reservoirs, and the (r) jointly forced carriers;
the tag copy/phase labels contribute (m^{O(r)}); and even allowing all
labelled simple-pseudoline crossing orders contributes at most
(((r-1)!)^r\), absorbed by the last term.

Since

\[
       \log B=(1+o(1))H\log(m/H),
       \qquad
       {\ell\log\ell\over\log B}=o(1),
\tag{8.4}
\]

the union of (8.2) over (8.3) tends to zero uniformly for

\[
 r\ge r_0:=
 \left\lceil {C m\log m\over\log B}\right\rceil
\tag{8.5}
\]

once (C) is a sufficiently large absolute constant.  In the calibrated
regime

\[
        {m\log m\over QH\log(m/H)}\longrightarrow0,
\tag{8.6}
\]

so (r_0=o(Q)).  Thus, with probability (1-o(1)), no strict canonical
Z22 gadget of order (r\ge r_0) survives.  In particular the original
(n=(1+o(1))\ell/2) gadget is absent, and this remains true under every
later deletion-only dynamics.

For a tag-disjoint, line-pure union of the surviving strict gadgets, with
component orders \(r_j<r_0\), assume in addition that different displayed
gadgets have no protected cross-intersections (equivalently, take the
\(r_j\)'s to be the components of the full displayed tag--target conflict
graph).  Quarantining every singleton crossing anchor then costs at
most

\[
        \sum_j\binom{r_j}{2}
        \le {r_0\over2}\sum_jr_j
        \le {r_0T\over2}=o(W),
\tag{8.7}
\]

because \(r_0=o(g)\) and \(gT=(1+o(1))W\).  The selected-path incidence
on those exceptional targets is at most

\[
             \sum_j r_j(r_j-1)\le r_0T=o(W).
\tag{8.8}
\]

Hence such a line-pure union causes zero tag loss after an allowed
\(o(W)\) target quarantine.  Tag-disjointness by itself does not control
new protected intersections between different gadgets; those belong to
the cross-gadget term isolated in Sections 6--7.

The common-reservoir qualification is essential to the particular count
(8.3).  Treating arbitrary independent carrier tails as if they were
jointly forced would incorrectly omit exponentially many tag choices.
The next theorem handles those tails by summing them exactly rather than
discarding them.

### Theorem 8.1 (tail-uniform absence for consecutive common-frame gadgets)

Consider a common-frame Z22 block datum of order \(r\), but now allow
each line path to choose its carrier tail independently.  Assume that on
each path the

\[
                  d=2(r-1)
\tag{8.9}
\]

line-crossing swaps form one consecutive directed monotone segment.
All other prefix and suffix data may vary.  Let \(K_{\rm cp}=m^{O(1)}\)
be the number of labelled carrier copies/phases.  Then, for a sufficiently
large absolute constant \(C\), with probability \(1-o(1)\) no such
marked gadget exists for

\[
             C\sqrt{m/\log m}\le r\le (g+2)/2.
\tag{8.10}
\]

The assertion remains true after isolation and every deletion-only
dynamic stage.

#### Proof

Fix one global directed \(d\)-step monotone segment \({\cal S}\).  Its
owner union has size \(m+d\), so the number of size-\((m+H)\) carriers
containing it is exactly

\[
                 C_d=\binom{m-d}{H-d}.
\tag{8.11}
\]

For one containing carrier and one fixed physical offset, coordinate
transitivity gives relative simple-support mass

\[
             {2\over B(m)_d(H)_d},
             \qquad B=\binom{m+H}{m},
\tag{8.12}
\]

where the harmless factor two allows reversal.  Summing over every
carrier tail, every one of at most \(g\) offsets, and all labelled
copies/phases, the expected number \(Z_{\cal S}\) of marked realizations
satisfies

\[
\begin{aligned}
 \lambda_d:=\mathbb EZ_{\cal S}
 &\le
  2gK_{\rm cp}\mu\,
  {C_d\over B(m)_d(H)_d}\\
 &=2gK_{\rm cp}\mu\,
   {(m-d)!^2\over(m-H)!(m+H)!}\\
 &\le {2gK_{\rm cp}\mu\over(m)_d^2}.
\end{aligned}
\tag{8.13}
\]

Uniform priority decorations multiply the constrained and unconstrained
support counts by the same factor; they are already included in
\(\mu=pA\) and do not alter (8.12)--(8.13).

For the identity, use

\[
 B(m)_d(H)_d
 ={(m+H)!\over(m-d)!(H-d)!}.
\]

For the last inequality, divide the middle factorial ratio by
\((m)_d^{-2}\); the remaining factor is

\[
 {m!^2\over(m-H)!(m+H)!}
 =\prod_{j=0}^{H-1}{m-j\over m+j+1}<1.
\tag{8.14}
\]

A common-frame block pattern of order \(r\) can be specified in at most

\[
 N_r\le
 2^{2m}(2m)^{c_1(g+r)}
 ((r-1)!)^r2^{c_2r^2}
\tag{8.15}
\]

ways for absolute constants \(c_1,c_2\).  The first two factors choose
the constant-number reservoirs and the \(O(g+r)\) labelled active
coordinates; the factorial factor chooses every crossing-order table;
and the last factor absorbs orientations and local interpolation
conventions.  Hence

\[
             \log N_r
             =O(m+g\log m+r^2\log r).
\tag{8.16}
\]

For one fixed pattern, sum over all tuples of independently chosen
carrier tails and copies.  Every realized tuple uses \(r\) distinct
tagged candidate vertices, so its marking probability is the product of
the \(r\) Bernoulli probabilities.  The expected number of marked
tuples is therefore at most

\[
                         \lambda_d^r.
\tag{8.17}
\]

No independence assertion about the aggregate variables
\(Z_{\cal S}\) is needed; (8.17) is simply the expanded first moment
over tuples.

Uniformly in (8.10), \(d=o(m)\), and therefore

\[
 \log(m)_d=d\log m+O(d^2/m).
\tag{8.18}
\]

Since \(gK_{\rm cp}\mu=m^{O(1)}\), equations (8.9), (8.13), and (8.18)
give

\[
                  \log\lambda_d
                  \le-(4-o(1))r\log m.
\tag{8.19}
\]

Also \(\log r\le(1/2+o(1))\log m\).  Combining
(8.16)--(8.19),

\[
 \log(N_r\lambda_d^r)
 \le
 O(m+g\log m)
 -(7/2-o(1))r^2\log m.
\tag{8.20}
\]

Because \(g\log m=o(m)\), a sufficiently large \(C\) makes the right
side at most \(-\Omega(r^2\log m)\) throughout (8.10).  Summing over at
most \(g\) values of \(r\) proves the assertion.  Isolation and all later
stages only delete marked candidates. \(\square\)

In the calibrated regime,

\[
       \sqrt{m/\log m}=o(Q)=o(g).
\tag{8.21}
\]

Thus Theorem 8.1 rules out the original
\(n=(1+o(1))\ell/2\) line gadget even with arbitrary independent carrier
tails.  For a line-pure, tag-disjoint packing of the remaining components,
with no protected cross-intersections between components, the internal
anchor and selected-path incidence ledgers are

\[
       O\!\left(T\sqrt{m/\log m}\right)=o(W),
\tag{8.22}
\]

so they cause zero additional tag loss after scalar quarantine.

The consecutive hypothesis can be removed while retaining a common
outside-block anchor frame.

### Corollary 8.2 (interleaved crossings in a common anchor frame)

Retain the common sign-block and outside-block anchor frame, but permit
the \(d=2(r-1)\) crossing transitions on each path to occupy arbitrary
slots among its at most \(g\) transitions, with path-specific filler
transitions in the other slots.  Then the conclusion of Theorem 8.1
still holds.

#### Proof

For a fixed role, choose an anchor phase and the ordered \(d\) slots of
the prescribed line transitions.  There are at most \(g^{d+1}\) choices.
All prefix, suffix, and interleaved filler coordinates are then free
completion data and are already summed inside the raw fibre.  The same
transition-list calculation as (8.13) gives

\[
       \lambda_d^{\rm int}
       \le {2K_{\rm cp}\mu g^{d+1}\over(m)_d^2}.
\tag{8.23}
\]

Here carrier and reservoir extensions must not be counted again: they
were summed in deriving (8.23).  The remaining common-frame patterns
number at most

\[
 2^{2m}(2m)^{4r}((r-1)!)^r2^{O(r^2)}
 =\exp\{O(m+r\log m+r^2\log r)\}.
\tag{8.24}
\]

Since \(g=m^{1/2+o(1)}\), \(d=2(r-1)\), and (8.18) holds,

\[
             \log\lambda_d^{\rm int}
             \le-(3-o(1))r\log m.
\tag{8.25}
\]

After taking \(r\) roles, the negative term is
\(-(3-o(1))r^2\log m\), while the crossing-order term in (8.24) is at
most \((1/2+o(1))r^2\log m\).  The same
\(r\ge C\sqrt{m/\log m}\) first-moment sum therefore tends to zero.
\(\square\)

The common outside-block anchor frame remains essential.  Without it,
independent path-specific filler cores can have \(\exp(O(rm))\) pattern
entropy, which the displayed first moment does not absorb.  No absence
claim is made for that broader class.

### Proposition 8.3 (one simultaneous isolated outcome)

The high-probability events in Theorem 2.1, Proposition 4.1, and
Theorem 8.1--Corollary 8.2 may be imposed simultaneously on the
pointwise-balanced isolated outcome.

#### Proof

Their intersection has probability \(1-o(1)\).  Every pruning ledger
used to select the balanced outcome is nonnegative.  Conditioning such
a ledger on an event of probability \(1-o(1)\) multiplies its expectation
by at most \(1+o(1)\).  Hence the usual averaging selection may be made
inside the intersection while preserving every \(o(W)\) and
\(o(T/Q)\) estimate.  All later statements then refer to this single
outcome, not to separately chosen samples. \(\square\)

## 9. Dynamic-measure boundary and sharpness

The deterministic part of Theorem 2.1 survives arbitrary adaptation
provided only that:

1. the residual catalogue is obtained by deleting initially marked
   candidates; and
2. the current measure obeys (0.5).

No predictability assumption is needed: the bundle union and the weights
may be chosen after the sample is known.  If a profile is instead fixed
before fresh Bernoulli marks at a new stage, the usual conditional
Chernoff estimate gives additional control.  For (0\le f_{U,P}\le1),

\[
 r_U={1\over A}\sum_Pf_{U,P},
 \qquad
 Y_U=\sum_Pf_{U,P}{\bf1}_{\{P\ {m marked}\}},
\]

one has

\[
 \mathbb E e^{\lambda Y_U}
 \le\exp\{\mu r_U(e^\lambda-1)\},
\tag{9.1}
\]

and consequently, for \(\beta>r_U\),

\[
 \Pr(Y_U\ge\beta\mu)
 \le
 \exp\{-\mu[\beta\log(\beta/r_U)-\beta+r_U]\}
 \le\left({er_U\over\beta}\right)^{\beta\mu}.
\tag{9.2}
\]

The conditional version iterates for predictable fresh-mark stages.

For arbitrary post-sample reweighting without (0.5), no analogue of
(0.6) is true.  A measure can put mass one on a single occupied bundle.
Even with uniform weights, selecting \(\Theta(\alpha z\mu)\) occupied
bundles on one tag captures mass \(\alpha\).  Thus the bundle-incidence
threshold in (0.7) is sharp in order for general adaptive bundle unions:

\[
         \Theta(\alpha z\mu T/Q)
\tag{9.3}
\]

bundle incidences can trap (T/Q) prescribed tags.  Statement (9.3) is
a sharpness example for arbitrary skeleton unions; it is **not** an
actual line-gadget counterexample, because no compatible crossing
partners are supplied.

## 10. Literal coefficient ledger and audited boundary

Every candidate discussed above is already a literal buffered monotone
geodesic and, for the Z22 systems, extends to the ordinary
displacement-zero cyclic schedule.  The proofs only delete candidates,
choose one existing candidate, or declare whole tags/targets exceptional.
No fractional splice is interpreted as a path.

If (o(T/Q)) tags are discarded, their protected-claim cost is

\[
       K\,o(T/Q)
       =o\!\left({(2Q+1)\ell T\over Q}\right)
       =o(W),
\tag{10.1}
\]

and their physical-owner cost is smaller.  Thus the conclusions
compose at coefficient-one scale.

The decisive steps were independently audited along three routes:

* Lemmas 1.1--1.2 give a post-sample adaptive bound without counting the
  possible unions.
* Proposition 4.1 and Theorem 6.2 do not use skeleton rarity; they use
  tag--target simplicity and an independent-transversal argument.
* The carrier-tail factorial identity (8.13) and both the consecutive
  and interleaved first-moment counts were checked independently; their
  common-frame scope is explicit.

The final classification is:

* **Proved:** every anchor-budget-compatible union of actual Z22 line
  systems has only \(o(T/Q)\) fixed-\(\alpha\) mass-trapped tags in the
  isolated point and in every deletion residual down to density \(1/Q\)
  satisfying \(\Lambda Q^2/(\alpha\mu)=o(1)\).  This normalized-mass
  statement is not, by itself, an independent-transversal theorem.
* **Proved:** after (o(T/Q)) cleanup there are no parallel candidates
  from one tag through one target.
* **Proved:** conflict-separated line bins have a perfect unweighted
  transversal; bounded-overlap superpositions lose only (7.3) tags.
* **Proved:** any unweighted deficiency in a conflict graph containing
  all pairs under consideration forces the \(m^{1/3-o(1)}\)
  common-anchor star (6.7).
* **Proved:** every common-anchor-frame block-coded Z22 gadget of order
  at least \(C\sqrt{m/\log m}=o(Q)\) is absent with high probability,
  even with independent carrier tails and interleaved filler
  transitions.  The original order-\(\Theta(\ell)\) gadget is included.
* **Unsupported and not claimed:** a bound excluding arbitrary
  path-specific-core, highly overlapping geodesic line systems with no
  common outside-block anchor frame and with common-anchor multiplicity
  at or above (6.7).
* **Not constructed:** an actual unweighted Hall-deficient geodesic
  family on a positive density of tags.

Accordingly, the D-scale line arrangement closes as a weighted-only
obstruction.  The sole surviving unweighted version is a quantitatively
different object: a high-multiplicity common-anchor/cross-gadget packing,
not a union of separated loose line arrangements.
