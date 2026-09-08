# First-order intersection expansion for the protected-strip multicover

Date: 2026-07-25

Method: pure mathematics only.

## 0. Outcome

Let \({\cal H}\) be the protected return-free grid-strip catalogue after
the three-antichain pruning.  A support edge has one tag and a protected
target set \(C(P)\) of size

\[
 K=g+2\sum_{q\le Q}c_q^{(g)}\le(2Q+1)g=m^{1+o(1)},    \tag{0.1}
\]

and every retained good tag and target fibre has degree

\[
 D=m^{5/2-o(1)}.                                      \tag{0.2}
\]

The nonlinear width-two moment subtracts its terms at intersection sizes
zero and one.  A finite projective plane is therefore the correct abstract
warning.  It is not, however, a \(D\)-scale obstruction at the actual
parameters.

This note proves the following.

1.  If \({\cal F}\) is a pairwise-intersecting family of distinct
    protected supports, every two members meet in exactly one target, and
    \({\cal F}\) has no common target, then

    \[
      \boxed{|{\cal F}|\le K^2-K+1.}                  \tag{0.3}
    \]

    This is exact: equality is the projective-plane parameter.  Since

    \[
      {K^2\over D}=m^{-1/2+o(1)}=o(1),                \tag{0.4}
    \]

    a pure singleton-intersection line system can force only \(o(D)\)
    mutually conflicting supports.  It cannot produce a constant-factor
    excess over the tag-degree lower bound \(D\).

2.  The actual grid orbit has a stronger one-star expansion.  For a target
    \(v\) and a strip \(E\) not containing \(v\), put

    \[
      \Gamma_v(E)=\{P:v\in C(P),\ C(P)\cap C(E)\ne\varnothing\}.
    \]

    Then

    \[
      \boxed{
      {|\Gamma_v(E)|\over d(v)}
      \le \varepsilon_1\qquad
      \varepsilon_1
       ={8+o(1)\over m}+O\!\left({gK\over m^2}\right)
       =m^{-1/2+o(1)}.}                               \tag{0.5}
    \]

    The first term is the complete adjacent nested-cover contribution;
    the second contains every non-cover target.  Formula (0.5) is one
    joint codegree sum, not a product of target marginals.

3.  The isolated pruning can be chosen to preserve (0.5), with a changed
    absolute constant, simultaneously for all retained strips and all
    good targets.  Thus any pairwise-intersecting retained family with no
    common target has maximum target degree at most

    \[
      O(\varepsilon_1D)=m^{2+o(1)}.                   \tag{0.6}
    \]

4.  There is no literal Helly theorem: three actual return-free strips can
    intersect pairwise in three different owners and have empty total
    protected intersection.  Thus `pairwise intersecting implies a common
    target' is false.  The valid conclusion is the quantitative one
    (0.3)--(0.6).

5.  For mixed intersections, let \(B\) be the maximum number of members of
    an intersecting family which meet one member in at least two protected
    targets.  Then the exact reduction is

    \[
      \boxed{
      |{\cal F}|\le(B+1)
      \max\{K^2-K+1,K+B\}.}                           \tag{0.7}
    \]

    Hence the genuinely remaining edge-colouring obstruction is not the
    invisible projective-plane sector.  It is the size-two-or-more overlap
    graph.  The existing exponential census proves a subpolynomial
    normalized moment, but not the much stronger

    \[
      B=o(D/K^2)=m^{1/2-o(1)}                         \tag{0.8}
    \]

    which would make (0.7) an \(o(D)\) bound.  Near-\(D\) edge colouring is
    therefore still open, but the first-order-only counterexample has been
    ruled out at the required scale.

## 1. The actual support hypergraph

For one return-free geodesic grid write

\[
 G_{i,j}=C\cup\{a_{i+1},\ldots,a_g\}
             \cup\{b_1,\ldots,b_j\}.                 \tag{1.1}
\]

At phase \(t\), the protected target column consists of

\[
 G_{t,t},\qquad G_{t+q,t},\qquad G_{t-q,t},           \tag{1.2}
\]

for the claimed depths \(q\).  The calibrated priorities give exactly
(0.1).  We treat two labelled copies with the same protected support as
different multicover edges but as one support in the incidence statements
below.  Copies of one support meet in \(K\) targets and hence belong to the
higher-overlap sector, not the singleton sector.

The pruning removes pairs which share a three-element antichain.  It does
not remove a singleton intersection.  The issue is consequently whether a
large family can behave like the lines of a projective plane.

## 2. Exact singleton-intersection theorem

The following elementary theorem is the precise projective-plane bound
needed here.

### Theorem 2.1 (linear intersecting family)

Let \({\cal F}\) be a family of sets of size at most \(K\).  Suppose

\[
 |E\cap F|=1\qquad(E,F\in{\cal F},\ E\ne F)           \tag{2.1}
\]

and \(\bigcap_{E\in{\cal F}}E=\varnothing\).  Then

\[
 \boxed{|{\cal F}|\le K^2-K+1.}                      \tag{2.2}
\]

#### Proof

Fix \(E_0\in{\cal F}\).  For \(v\in E_0\), let

\[
 d_{\cal F}(v)=|\{E\in{\cal F}:v\in E\}|.           \tag{2.3}
\]

Since \(v\) is not common to the family, choose \(F_v\in{\cal F}\) with
\(v\notin F_v\).  Every member of the \(v\)-star meets \(F_v\).  These
intersection points are distinct: if two different members contained both
\(v\) and the same point of \(F_v\), their mutual intersection would have
size at least two.  Hence

\[
 d_{\cal F}(v)\le |F_v|\le K.                         \tag{2.4}
\]

Every member other than \(E_0\) meets \(E_0\) in one unique point, so

\[
 |{\cal F}|-1
 =\sum_{v\in E_0}(d_{\cal F}(v)-1)
 \le |E_0|(K-1)
 \le K(K-1).                                         \tag{2.5}
\]

This is (2.2). \(\square\)

For a projective plane of order \(q\), one has \(K=q+1\) and
\(|{\cal F}|=q^2+q+1=K^2-K+1\), so the theorem is sharp without using
additional strip geometry.

### Corollary 2.2 (projective planes are below the colour scale)

Every pairwise-intersecting, singleton-only, non-star subfamily of the
protected-strip support catalogue has size

\[
 K^2-K+1=m^{2+o(1)}=o(D).                             \tag{2.6}
\]

Thus even if the actual strip catalogue contained a full projective plane
at the largest rank allowed by one strip, that component would require
only \(o(D)\) colours.  Taking disjoint unions of such components does not
increase their chromatic requirement.  Repeating individual lines moves
the repetitions into the visible higher-overlap sector.

This does not prove a near-\(D\) colouring.  It proves that a counterexample
whose obstruction is carried only by single common targets cannot supply a
constant-factor gap.

The statement also has the exact weighted form needed by the fractional
edge-colouring dual.  If \(y_E\ge0\) is supported on such an intersecting
family, a matching contains at most one supported edge, and therefore

\[
 {\sum_{E\in{\cal F}}y_E\over
   \max_M\sum_{E\in M}y_E}
 ={\sum_Ey_E\over\max_Ey_E}
 \le |{\cal F}|le K^2-K+1=o(D).                     \tag{2.7}
\]

Parallel copies of one support are not covered by (2.7): two such copies
share all \(K\) targets, so their obstruction is recorded by the nonlinear
overlap term.  Tag coincidences are likewise ordinary tag stars of size at
most \(D\), not singleton target line systems.

## 3. Exact one-star expansion in the grid orbit

We use two orbit facts already established for the return-free catalogue.

* If \(v\subset w\) or \(w\subset v\) and their ranks differ by one, the
  exact forced adjacent-slot relative codegree is at most

  \[
    {2+o(1)\over m}.                                  \tag{3.1}
  \]

* For every other pair of distinct protected targets, the stabilizer-orbit
  bound, summed over all time offsets of a \(g\)-phase chunk, is

  \[
    {d(v,w)\over d(v)}\le {C g\over m^2}.             \tag{3.2}
  \]

For (3.2), the smallest non-cover orbit has size \(\Theta(m^2)\): it is
either a same-rank Johnson-neighbour orbit, a nested rank gap of at least
two, or a nonnested adjacent-rank orbit.  There are at most \(g\) normalized
time offsets after division by the one-target degree.

The next lemma is where the actual phase order improves the naive sum over
all \(K\) targets.

### Lemma 3.1 (at most four cover neighbours in one strip)

Fix a Boolean target \(v\).  A protected return-free strip contains at
most four targets which are Boolean covers or cocovers of \(v\).

#### Proof

Only the two ranks \(|v|-1\) and \(|v|+1\) are relevant.  At each fixed
rank, the targets of a geodesic strip, in phase order, form a subpath of an
isometric Johnson path.  All \((|v|-1)\)-subsets of \(v\) form a clique in
that Johnson graph.  An isometric path meets a clique in at most two
consecutive vertices: three such vertices would put its first and third
vertices at path distance two but Johnson distance one.  The same argument
applies to the \((|v|+1)\)-supersets of \(v\).  Thus there are at most two
on each side. \(\square\)

### Theorem 3.2 (one-strip hitting expansion)

For every protected target \(v\) and every protected strip \(E\) with
\(v\notin C(E)\),

\[
 \boxed{
 {|\Gamma_v(E)|\over d(v)}
 \le {8+o(1)\over m}+{C gK\over m^2}.}               \tag{3.3}
\]

#### Proof

Every \(P\in\Gamma_v(E)\) contains \(v\) and at least one
\(w\in C(E)\).  The union bound is therefore the joint-codegree inequality

\[
 |\Gamma_v(E)|
 \le\sum_{w\in C(E)}d(v,w).                           \tag{3.4}
\]

By Lemma 3.1, at most four summands are adjacent nested-cover pairs.  Their
total, using (3.1), is at most \((8+o(1))d(v)/m\).  Every other summand is
bounded by (3.2), and there are at most \(K\) of them.  Divide by \(d(v)\)
to obtain (3.3). \(\square\)

At the protected-strip scales,

\[
 {gK\over m^2}=m^{-1/2+o(1)},                         \tag{3.5}
\]

which proves (0.5).  The estimate remains meaningful precisely because
the first-order cover pairs were counted jointly and because their number
inside one external strip is four, not \(K\).

### Corollary 3.3 (non-star degree bound)

Let \({\cal F}\) be pairwise intersecting and have no common protected
target.  Then, in the full symmetric orbit,

\[
 \boxed{
 \max_v d_{\cal F}(v)\le\varepsilon_1d(v),}           \tag{3.6}
\]

with \(\varepsilon_1\) as in (0.5).

#### Proof

For each \(v\), choose \(E_v\in{\cal F}\) not containing \(v\).  Every
member of \({\cal F}\) which contains \(v\) must intersect \(E_v\), and
hence belongs to \(\Gamma_v(E_v)\).  Apply Theorem 3.2. \(\square\)

## 4. Preservation by isolated pruning

The expansion can be included in the same isolated-pruning experiment
which produces the balanced protected multicover.

Let the unpruned tag degree be \(A\), let paths be marked with probability
\(p\), and put

\[
 \mu=pA=m^{5/2-o(1)}.                                 \tag{4.1}
\]

For each pair \((v,E)\) with \(v\notin C(E)\), let \(Y_{v,E}\) be the
number of marked paths in \(\Gamma_v(E)\).  Theorem 3.2 and the calibration
\(d(v)\le A\) give

\[
 \mathbb EY_{v,E}le\mu\varepsilon_1.                \tag{4.2}
\]

Here

\[
 \mu\varepsilon_1=m^{2-o(1)}\gg m.                  \tag{4.3}
\]

The total number of target--candidate pairs \((v,E)\) is
\(\exp(O(m))\): there are at most \(4^m\) Boolean targets, the carrier
count is \(\exp(O(m))\), and the logarithm of one geodesic orbit degree is
\(o(m)\).  Chernoff and a union bound therefore give, simultaneously,

\[
 Y_{v,E}\le2\mu\varepsilon_1                         \tag{4.4}
\]

for every \((v,E)\), with probability \(1-o(1)\).

Isolation only deletes marked paths, so (4.4) remains true in the retained
catalogue.  Intersect this event with the balanced-pruning event and keep
only the good target fibres, whose retained degrees are at least \(\mu/4\).
There is an outcome satisfying both.  In that outcome,

\[
 \boxed{
 { |\Gamma'_v(E)|\over d'(v)}
 \le8\varepsilon_1}                                  \tag{4.5}
\]

for every retained candidate \(E\) and every good target \(v\notin C(E)\).
The exceptional tag and target fibres have the same \(o(W)\) physical
ledger as in the original balanced pruning.

Consequently every pairwise-intersecting retained family with no common
good target satisfies

\[
 \max_v d_{\cal F}(v)\le8\varepsilon_1d'(v)
 =m^{2+o(1)},                                         \tag{4.6}
\]

which is (0.6).  A family using an exceptional target is charged to the
existing \(o(W)\) exceptional-target ledger.

## 5. Mixed intersections: the exact remaining reduction

The preceding theorems settle only the invisible singleton sector.  Here
is an exact way to separate it from the already visible nonlinear sector.

For a pairwise-intersecting family \({\cal F}\), form a graph \(J\) on its
members by joining \(E,F\) when

\[
 |E\cap F|\ge2.                                       \tag{5.1}
\]

Let \(B=\Delta(J)\).

### Theorem 5.1 (linear/nonlinear decomposition)

If \({\cal F}\) has no common target, then

\[
 \boxed{
 |{\cal F}|\le(B+1)max\{K^2-K+1,K+B\}.}             \tag{5.2}
\]

#### Proof

Greedily colour \(J\) with \(B+1\) colours.  One colour class \({\cal C}\)
has pairwise intersections exactly one.

If \({\cal C}\) has no common target, Theorem 2.1 gives
\(|{\cal C}|\le K^2-K+1\).

Otherwise, all members of \({\cal C}\) contain one target \(v\).  Since
their pairwise intersections have size one, the petals
\(C\setminus\{v\}\), \(C\in{\cal C}\), are pairwise disjoint.  The full
family has no common target, so choose \(F\in{\cal F}\) with \(v\notin F\).
At most \(B\) members of \({\cal C}\) are nonlinear neighbours of \(F\).
Every remaining member must meet \(F\) in a point of its private petal;
the points are distinct, so there are at most \(|F|\le K\) such members.
Thus

\[
 |{\cal C}|\le K+B.                                   \tag{5.3}
\]

Every one of the at most \(B+1\) colour classes obeys one of these two
bounds.  Summing proves (5.2). \(\square\)

The nonlinear exponential moment at \(w=2\) majorizes \(B\), because

\[
 2^s-1-s\ge1\qquad(s\ge2).                            \tag{5.4}
\]

But the proved census only bounds its normalized row sum by \(m^{o(1)}\).
It does not imply (0.8).  Formula (5.2) identifies the exact quantitative
gap: to make every no-common-target clique \(o(D)\) by this reduction it is
enough that

\[
 (B+1)(K^2+B)=o(D),                                   \tag{5.5}
\]

whose restrictive term here is \(B=o(D/K^2)\).

## 6. A literal non-Helly triangle

For clarity, the protected strips do not satisfy an exact Helly property.
Let \(R\) have size \(m-2\), and choose four points \(1,2,3,4\notin R\).
Put

\[
 A=R\cup\{1,2\},\qquad
 B=R\cup\{3,4\},\qquad
 C=R\cup\{1,3\}.                                    \tag{6.1}
\]

Use the following geodesic cores:

\[
 \begin{array}{lll}
 P_{AB}:&A\longrightarrow R\cup\{2,4\}
               \longrightarrow B,&
        (1\mapsto4,\ 2\mapsto3),\\[1mm]
 P_{AC}:&A\longrightarrow C,&(2\mapsto3),\\[1mm]
 P_{CB}:&C\longrightarrow B.&(1\mapsto4)
 \end{array}                                         \tag{6.2}
\]

The forced lower/upper cover pairs in (6.2) are respectively

\[
 \begin{array}{c|c}
 P_{AB}&R\cup\{2\},\ R\cup\{1,2,4\},\
          R\cup\{4\},\ R\cup\{2,3,4\}\cr
 P_{AC}&R\cup\{1\},\ R\cup\{1,2,3\}\cr
 P_{CB}&R\cup\{3\},\ R\cup\{1,3,4\}.
 \end{array}                                         \tag{6.3}
\]

They are all distinct.  Extend the three cores to buffered return-free
chunks using disjoint private departure and arrival pools.  This is
possible because \(g=o(m)\).  The private pools can be chosen so that no
additional protected flags coincide.  The resulting strips satisfy

\[
 C(P_{AB})\cap C(P_{AC})=\{A\},\qquad
 C(P_{AB})\cap C(P_{CB})=\{B\},\qquad
 C(P_{AC})\cap C(P_{CB})=\{C\}.                      \tag{6.4}
\]

Thus they are pairwise intersecting and have empty total intersection.
This example rules out an absolute common-target theorem, but it has only
three members.  Theorem 2.1 shows that every first-order-only amplification
has at most \(K^2-K+1=o(D)\) members.

## 7. Edge-colouring implication

The edge-colouring lower bound \(D\) comes from tag and target stars.  A
projective-plane component would be dangerous only if it supplied
\(\Theta(D)\) pairwise conflicting supports with no common star.  Equations
(0.3)--(0.4) rule that out, and (0.5) shows directly that no strip outside
a target star can hit more than an \(m^{-1/2+o(1)}\) fraction of that star.

What remains is not a first-order line-system question.  It is to prove a
strong matching/expansion estimate for the graph of pairs sharing at least
two targets, or to exploit the chronological skew-Ferrers structure more
sharply than the maximum-degree reduction (5.2).  Until that is done, the
width-two exponential census plus the present first-order theorem still
does not imply a near-\(D\) edge colouring.
