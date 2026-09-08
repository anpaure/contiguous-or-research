# Capacitated Hall theory for stateful MTF portals

Date: 2026-07-25

## 0. Verdict

This report continues the stateful portal-extraction line after
MATH_ATTACK_V_STATEFUL_PORTAL_EXTRACTION_20260725.md.

There are two logically different incidence systems.

1. A relabelled global symmetric-chain decomposition supplies
   \(\Theta_A(HW)\) target--product-box incidences, with only
   \(O_A(HW/m)=o(W)\) same-chain box collisions.
2. The exact odd-factor adaptive-MTF word supplies literal suffix
   occurrences at \(W\) physical endpoints.  An endpoint has exactly one
   canonical target in every signed rank \(-H,\ldots,H\).

A single coordinate relabelling can make both box-collision ledgers small.
However, a product-box incidence is not an endpoint--target edge.  The
target Hall graph is invariant, up to renaming targets, under coordinate
relabeling.  Thus the global SCD theorem certifies abundant relevant box
incidence, while the separate MTF nested-pair estimate pays cell diversity
after a target matching.  Neither statement can by itself prove target
Hall.

The exact endpoint-capacitated Hall problem is as follows.  Let
\(\mathcal F(v)\) be the \(2H+1\) canonical Boolean targets at MTF endpoint
\(v\).  For a set \(J\) of endpoints and an integer demand \(b\), a
\(b\)-fold target extraction exists precisely when

\[
 \boxed{
 |\mathcal N(X)|\ge b|X|
 \quad\text{for every }X\subseteq J,}
 \tag{0.1}
\]

where

\[
 \mathcal N(X)=\bigcup_{v\in X}\mathcal F(v).
 \tag{0.2}
\]

For the portal scale

\[
 b=H,
 \qquad
 |J|=\left\lceil\frac WH\right\rceil,
 \tag{0.3}
\]

Hall would give at least \(W\) distinct literal targets on
\(\Theta(W/H)\) state-compatible endpoints.

The principal positive theorem is a nontrivial exact Hall regime.

> After one common relabelling which simultaneously preserves the global
> SCD incidence theorem, there are two long canonical complementary-
> geodesic components and
> \[
> 2(m+1)-O_A(H)
> \]
> box-rainbow state endpoints on them whose endpoint--target graph satisfies
> \(H\)-fold Hall on every endpoint subset.

Consequently those two components alone contain a literal matching of size

\[
 \boxed{
 2H(m+1)-O_A(H^2)
 =\Theta_A(m^{3/2})}
 \tag{0.4}
\]

for \(H=\lceil A\sqrt m\rceil\), with pairwise distinct Boolean targets and
pairwise distinct endpoint--box cells.  No reset or new MTF transition is
added.

The proof uses componentwise target-rainbowness.  If \(X\) meets at most
\(r\) long components and \(x_{\max}\) is its largest component section,
then

\[
 \boxed{
 |\mathcal N(X)|
 \ge |X|+2H x_{\max}
 \ge\left(1+\frac{2H}{r}\right)|X|.}
 \tag{0.5}
\]

For \(r=2\), the right side is at least \(H|X|\).  Hence two components
always satisfy the desired Hall inequalities.

The first possible obstruction is therefore genuinely intercomponent.  On
noninitial odd-factor endpoints the middle and upper-depth-one targets are
globally injective.  If

\[
 \ell_a(X)=|X|-|\mathcal N_a(X)|
 \tag{0.6}
\]

is the repetition loss at signed rank \(a\), then the exact \(H\)-Hall cut
inequality is

\[
 \boxed{
 \sum_{a\ne0,+1}\ell_a(X)
 \le(H+1)|X|.}
 \tag{0.7}
\]

A deficient cut violates (0.7).  No one- or two-endpoint cut can be
deficient.  For \(H\ge6\), three endpoints are the first cardinality at
which deficiency is possible under the audited state constraints.  This is
sharp in the local canonical-state category: three legitimate saturated
MTF states can have common targets at every lower depth and every upper
depth at least two, while keeping their middle and upper-depth-one targets
distinct.  Their target union has size

\[
 2H+5
\]

against demand \(3H\), so the Hall deficit is exactly

\[
 \boxed{H-5.}
 \tag{0.8}
\]

These three states extend separately to long complementary geodesics.  The
construction does not prove that such a triple occurs inside one exact odd
factor; it proves that no argument using only canonical-state axioms,
componentwise injectivity, and global depth-one injectivity can rule it out.

For an inclusion-minimal deficient cut of deficit \(\delta\), every
endpoint has at most \(H-\delta\) private targets and therefore at least

\[
 \boxed{H+1+\delta}
 \tag{0.9}
\]

targets shared with other endpoints of the cut.  Thus the exact remaining
global obstruction is a dense cluster across at least three long
components, not an aggregate shortage of box incidences.

The full Gaussian-scale Hall theorem remains unproved.  The exact missing
statement is to find \(J\) of size \(\lceil W/H\rceil\), among the
box-compatible endpoints of one legal word, such that (0.7) holds for
every \(X\subseteq J\).  This report proves Hall on two long components and
exhibits the minimal possible deficient geometry beyond that regime.

No web search, finite search, or computation is used.

---

## 1. The two structures and their common relabelling

Put

\[
 n=2m,
 \qquad
 W=\binom{2m}{m},
 \qquad
 1\le H<m/2.
 \tag{1.1}
\]

For the Gaussian application,

\[
 H=\lceil A\sqrt m\rceil
 \tag{1.2}
\]

with \(A>0\) fixed.

### 1.1 The global SCD incidence structure

Fix any symmetric-chain decomposition \(\mathcal E\) of
\(2^{[2m]}\).  It has \(W\) chains, one through every middle mask.  Split
\([2m]\) into a fixed number of coordinate blocks, in particular the
audited three equal blocks when \(2m=3s\), and fix an SCD in each block.
Their products partition the cube into product boxes.

For a coordinate permutation \(\sigma\), let

\[
 \operatorname{Col}^{\rm SCD}_H(\sigma)
 \tag{1.3}
\]

be the sum, over all chains \(D\in\sigma\mathcal E\) and product boxes
\(\mathcal B\), of

\[
 \binom{
 |D\cap\mathcal B\cap
 \bigcup_{q=-H}^{H}\binom{[2m]}{m+q}|
 }2.
 \tag{1.4}
\]

The relabelled global SCD incidence theorem gives

\[
 \mathbb E_\sigma
 \operatorname{Col}^{\rm SCD}_H(\sigma)
 =O_A(HW/m).
 \tag{1.5}
\]

After restriction to the audited dominant target family
\(\mathcal T\), the same collision count still dominates all repeated-box
loss.  Since

\[
 |\mathcal T|=\Theta(HW),
 \tag{1.6}
\]

a relabelling satisfying (1.5) leaves \(\Theta(HW)\) distinct
SCD-chain--product-box incidences on \(\mathcal T\).

### 1.2 The literal MTF structure

Cut an exact odd factor into

\[
 B=\frac{W}{m+1}
 \tag{1.7}
\]

vertex-disjoint complementary geodesics.  The audited radius-\(H\)
adaptive-MTF lift gives a literal word \(\mathcal W_H\) of length

\[
 |\mathcal W_H|
 =W+(2H+1)B.
 \tag{1.8}
\]

At every middle-state endpoint \(v\), the last-occurrence state exposes a
saturated flag

\[
 \mathcal F(v)
 =
 \{F_{v,-H},\ldots,F_{v,0},\ldots,F_{v,+H}\},
 \qquad
 |F_{v,a}|=m+a.
 \tag{1.9}
\]

Each \(F_{v,a}\) is a literal suffix union ending at \(v\).

For a relabelling \(\sigma\), define the MTF endpoint--box collision count

\[
 \operatorname{Col}^{\rm MTF}_H(\sigma)
 =
 \sum_v\sum_{\mathcal B}
 \binom{
 |\{a:\sigma F_{v,a}\in\mathcal B\}|
 }2.
 \tag{1.10}
\]

The same nested-pair calculation gives

\[
 \mathbb E_\sigma
 \operatorname{Col}^{\rm MTF}_H(\sigma)
 =O_A(HW/m).
 \tag{1.11}
\]

### Theorem 1.1 -- simultaneous SCD/MTF relabelling

There is one coordinate permutation \(\sigma\) for which

\[
 \boxed{
 \operatorname{Col}^{\rm SCD}_H(\sigma)
 +
 \operatorname{Col}^{\rm MTF}_H(\sigma)
 =O_A(HW/m).}
 \tag{1.12}
\]

Consequently, for \(H=\lceil A\sqrt m\rceil\):

1. the relabelled global SCD retains \(\Theta_A(HW)\) distinct
   chain--box incidences, including \(\Theta(HW)\) incidences on the audited
   target family;
2. the literal MTF word loses only \(O_A(W/\sqrt m)=o(W)\) occurrences when
   one enforces at most one selected target in each endpoint--box cell.

#### Proof

Choose \(\sigma\) uniformly.  Equations (1.5) and (1.11), followed by
linearity of expectation, bound the expectation of the sum in (1.12).
Some \(\sigma\) attains at most that expectation.

For the first consequence, deduplicating \(r\) visits of one chain to one
box loses \(r-1\le\binom r2\).  Restriction to a target family can only
decrease collision pairs.  For the second consequence, the identical
inequality applies to occurrences in one endpoint--box cell. \(\square\)

### Lemma 1.2 -- the no-transfer principle

Let \(G_{\rm MTF}\) be the bipartite graph whose left vertices are MTF state
endpoints and whose right vertices are Boolean targets, with

\[
 vS\in E(G_{\rm MTF})
 \quad\Longleftrightarrow\quad
 S\in\mathcal F(v).
 \tag{1.13}
\]

A coordinate relabelling maps \(G_{\rm MTF}\) isomorphically to itself,
with the target names permuted.  In particular, every endpoint-subset Hall
deficiency is invariant under relabelling.

Membership of \(S\) in the same product box as a global-SCD target, or on
the same global-SCD chain, does not create the edge \(vS\).  Therefore the
global SCD incidence theorem alone implies no target Hall inequality in
\(G_{\rm MTF}\).

#### Proof

A coordinate permutation is a bijection \(S\mapsto\sigma S\), and

\[
 S\in\mathcal F(v)
 \quad\Longleftrightarrow\quad
 \sigma S\in\sigma\mathcal F(v).
 \]

Thus it preserves all neighborhoods and their cardinalities.  A literal
OR witness at endpoint \(v\) exists only for an actual prefix of its
last-occurrence state, equivalently for one of the masks in
\(\mathcal F(v)\).  Product-box or SCD-chain co-membership is not such an
equality. \(\square\)

Theorem 1.1 and Lemma 1.2 give the valid order of operations:

\[
 \text{target Hall first}
 \quad\longrightarrow\quad
 \text{box-cell deduplication at }o(W)\text{ cost}.
 \tag{1.14}
\]

Reversing this implication is unsupported.

---

## 2. Exact endpoint-capacitated Hall

Let \(J\) be any set of state endpoints in one legal MTF word.  Each
endpoint \(v\) has a set \(\mathcal F(v)\) of distinct canonical targets.
For \(X\subseteq J\), write

\[
 \mathcal N(X)=\bigcup_{v\in X}\mathcal F(v).
 \tag{2.1}
\]

Fix an integer demand

\[
 0\le b\le2H+1.
 \tag{2.2}
\]

A \(b\)-fold endpoint--target matching is a set of pairs \((v,S)\) such
that:

* \(S\in\mathcal F(v)\);
* every endpoint occurs in exactly \(b\) pairs;
* every Boolean target occurs in at most one pair.

### Theorem 2.1 -- exact capacitated Hall and deficiency

A \(b\)-fold endpoint--target matching on \(J\) exists if and only if

\[
 \boxed{
 |\mathcal N(X)|\ge b|X|
 \quad\text{for every }X\subseteq J.}
 \tag{2.3}
\]

Define

\[
 \Delta_b(J)
 =
 \max_{X\subseteq J}
 \bigl(b|X|-|\mathcal N(X)|\bigr)_+.
 \tag{2.4}
\]

Then the maximum number of endpoint clones which can be matched is exactly

\[
 \boxed{
 b|J|-\Delta_b(J).}
 \tag{2.5}
\]

#### Proof

Replace every endpoint \(v\) by \(b\) clones with common neighborhood
\(\mathcal F(v)\), and give every target capacity one.  Ordinary Hall gives
(2.3).

For the deficiency formula, max-flow/min-cut says that the number of
unmatched clones in a maximum matching is the largest clone-set Hall
deficit.  If a clone set contains one clone of \(v\), adding any omitted
clone of the same endpoint enlarges the clone set by one without enlarging
its target neighborhood.  Hence a maximizing deficient clone set contains
either all \(b\) clones of an endpoint or none.  The maximum is therefore
(2.4), proving (2.5). \(\square\)

### Remark 2.2 -- why the demand is \(H\)

Take

\[
 p=\left\lceil\frac WH\right\rceil.
 \tag{2.6}
\]

An \(H\)-fold matching on \(p\) endpoints has size

\[
 Hp\ge W.
 \tag{2.7}
\]

After discarding at most \(Hp-W<H\) matched pairs, it gives exactly \(W\)
distinct target occurrences.  The endpoint state offers \(2H+1\) candidate
targets, so demanding only \(H\) retains \(H+1\) units of collision slack
per endpoint.

This balanced Hall requirement is stronger than the previous random-
thinning theorem, which allowed the matched degree to be uneven among the
\(p\) endpoints.

### 2.1 Target Hall versus prescribed-target coverage

Theorem 2.1 concerns extraction: the targets may be chosen from the
canonical occurrence graph.  If instead one prescribes a target family
\(\mathcal A\) from the global SCD and asks to cover every member, the
opposite Hall inequalities are required:

\[
 |Y|
 \le
 \sum_{v\in N(Y)} b_v
 \quad\text{for every }Y\subseteq\mathcal A.
 \tag{2.8}
\]

An unsupported target \(S\in\mathcal A\) is already a singleton deficient
cut.  The global SCD incidence theorem does not rule out such a canonical
support hole.  This is why the present theorem is an extraction theorem,
not a proof of full-band coverage.

---

## 3. Componentwise expansion

Write the complementary-geodesic components of the odd-factor word as

\[
 \mathcal P_1,\ldots,\mathcal P_B.
 \tag{3.1}
\]

The componentwise target-rainbowness theorem says that, for every signed
rank \(a\), the map

\[
 v\in\mathcal P_i
 \longmapsto
 F_{v,a}
 \tag{3.2}
\]

is injective.

Also, the middle targets \(F_{v,0}\) are globally injective because the
components partition the middle layer.

For \(X\) in the endpoint set, put

\[
 x_i=|X\cap\mathcal P_i|,
 \qquad
 x_{\max}=\max_i x_i,
 \qquad
 r(X)=|\{i:x_i>0\}|.
 \tag{3.3}
\]

### Theorem 3.1 -- universal component-section expansion

For every endpoint set \(X\),

\[
 \boxed{
 |\mathcal N(X)|
 \ge |X|+2H x_{\max}.}
 \tag{3.4}
\]

If \(X\) meets at most \(r\) components, then

\[
 \boxed{
 |\mathcal N(X)|
 \ge
 \left(1+\frac{2H}{r}\right)|X|.}
 \tag{3.5}
\]

#### Proof

At the middle rank, global injectivity gives exactly \(|X|\) targets.  At
each of the other \(2H\) signed ranks, componentwise injectivity on a
component containing \(x_{\max}\) endpoints gives at least
\(x_{\max}\) distinct targets.  Different signed ranks contain targets of
different cardinalities, so their supports are disjoint.  Summing proves
(3.4).

If \(X\) meets at most \(r\) components, then

\[
 x_{\max}\ge |X|/r.
\]

Substitute into (3.4). \(\square\)

### Corollary 3.2 -- exact Hall on two long components

Let \(J\) be any endpoint subset contained in the union of at most two
complementary-geodesic components.  Then

\[
 |\mathcal N(X)|\ge H|X|
 \quad\text{for every }X\subseteq J.
 \tag{3.6}
\]

Consequently \(J\) admits an \(H\)-fold endpoint--target matching.

#### Proof

With \(r=2\), (3.5) gives

\[
 |\mathcal N(X)|\ge(H+1)|X|\ge H|X|.
\]

Apply Theorem 2.1. \(\square\)

This Hall theorem is insensitive to how heavily the two components collide
with one another at individual signed ranks.  At one rank their two rows
may coincide completely; the unused \(H+1\) state slots per endpoint absorb
all such two-component collisions.

### 3.1 The depth-one anchor improvement

At every noninitial endpoint of a cut exact odd factor, the upper
depth-one target is the union of one internal Johnson edge.  These internal
upper edge unions partition rank \(m+1\).  Therefore both

\[
 v\mapsto F_{v,0}
 \quad\text{and}\quad
 v\mapsto F_{v,+1}
 \tag{3.7}
\]

are globally injective on the noninitial endpoints.

If \(X\) contains only noninitial endpoints, then

\[
 \boxed{
 |\mathcal N(X)|
 \ge
 2|X|+(2H-1)x_{\max}.}
 \tag{3.8}
\]

In particular, if \(X\) meets at most \(r\) components,

\[
 |\mathcal N(X)|
 \ge
 \left(2+\frac{2H-1}{r}\right)|X|.
 \tag{3.9}
\]

The proof is the same as Theorem 3.1, separating the two globally injective
anchor ranks and using componentwise injectivity at the remaining
\(2H-1\) ranks.

Thus \(H\)-fold Hall is automatic whenever

\[
 2+\frac{2H-1}{r}\ge H.
 \tag{3.10}
\]

For \(H\ge6\), this universal criterion permits \(r=2\) but not \(r=3\).
The threshold is sharp under the local state axioms, as Section 6 shows.

---

## 4. A common-relabelling Hall construction

Use the simultaneous relabelling \(\sigma\) from Theorem 1.1.  For a
component \(\mathcal P_i\), let

\[
 C_i
 =
 \sum_{v\in\mathcal P_i}\sum_{\mathcal B}
 \binom{
 |\{a:\sigma F_{v,a}\in\mathcal B\}|
 }2.
 \tag{4.1}
\]

Then

\[
 \sum_{i=1}^{B} C_i
 =
 \operatorname{Col}^{\rm MTF}_H(\sigma)
 =O_A(HW/m).
 \tag{4.2}
\]

Since \(B=W/(m+1)\), the average component collision is

\[
 \frac1B\sum_i C_i
 =O_A(H).
 \tag{4.3}
\]

At least \(B/2\) components therefore satisfy

\[
 C_i=O_A(H).
 \tag{4.4}
\]

Choose two such components, \(\mathcal P_i,\mathcal P_j\).  In each, delete
every endpoint whose full canonical flag visits one product box more than
once.  Each deleted endpoint contributes at least one to \(C_i\) or
\(C_j\), so the surviving set \(J\) satisfies

\[
 |J|
 \ge2(m+1)-O_A(H).
 \tag{4.5}
\]

Every surviving endpoint is box-rainbow: its \(2H+1\) candidate targets
belong to \(2H+1\) distinct endpoint--box cells.

### Theorem 4.1 -- two-component distinct-target/cell Hall theorem

For the common relabelling in Theorem 1.1, there exist two long canonical
components and a set \(J\) of state endpoints satisfying (4.5) for which
there is an \(H\)-fold matching

\[
 \mathcal M\subseteq
 \{(v,S):v\in J,\ S\in\sigma\mathcal F(v)\}
 \tag{4.6}
\]

such that:

1. every \(v\in J\) occurs in exactly \(H\) matched pairs;
2. all matched Boolean targets \(S\) are distinct;
3. all endpoint--box cells
   \((v,\mathcal B(S))\) are distinct;
4. every \(S\) is represented by a literal suffix ending at \(v\) in the
   same word \(\sigma\mathcal W_H\); and
5. the matching size is
   \[
   \boxed{
   |\mathcal M|
   =H|J|
   \ge2H(m+1)-O_A(H^2).}
   \tag{4.7}
   \]

For \(H=\lceil A\sqrt m\rceil\), this is

\[
 |\mathcal M|=\Theta_A(m^{3/2}).
 \tag{4.8}
\]

#### Proof

Coordinate relabelling preserves the endpoint--target graph.  The set
\(J\) lies on two components, so Corollary 3.2 and Theorem 2.1 give an
\(H\)-fold target matching.

At a surviving endpoint the entire canonical flag is box-rainbow.
Therefore the \(H\) targets assigned to that endpoint lie in distinct
product boxes.  Cells at different endpoints are distinct by their endpoint
coordinate.  Hence the matching also has pairwise distinct cells.

All its edges are pre-existing canonical suffix witnesses, so no state or
word position is changed.  Equation (4.7) follows from (4.5).  Since
\(H=\Theta_A(\sqrt m)\) and \(H^2=O_A(m)\), the leading term has order
\(m^{3/2}\) and the error has order \(m\), proving (4.8). \(\square\)

### Scope of Theorem 4.1

The theorem is a genuine integral MTF construction and a nontrivial Hall
regime.  It does not have the global size \(W\): two components contain
only \(2(m+1)\) state endpoints.  Its role is to prove that neither
within-component MTF compatibility nor collisions between one pair of
long components can cause the Gaussian portal Hall failure.

The common relabelling simultaneously leaves the global SCD with
\(\Theta(HW)\) useful box incidences.  The matched targets in Theorem 4.1
are not asserted to lie in every prescribed part of the audited target
family.  Such an assertion would require the prescribed-target Hall
conditions (2.8), which remain unproved.

---

## 5. Exact Hall loss and the global missing condition

Restrict now to noninitial odd-factor endpoints so that the two anchor maps
in (3.7) are globally injective.  Let

\[
 \mathcal A_*
 =
 \{-H,\ldots,-1,+2,\ldots,+H\}.
 \tag{5.1}
\]

Thus

\[
 |\mathcal A_*|=2H-1.
 \tag{5.2}
\]

For \(X\) in the endpoint set and \(a\in\mathcal A_*\), define

\[
 \mathcal N_a(X)=\{F_{v,a}:v\in X\},
 \tag{5.3}
\]

and the signed-rank repetition loss

\[
 \ell_a(X)
 =
 |X|-|\mathcal N_a(X)|
 =
 \sum_S(\mu_{a,X}(S)-1)_+.
 \tag{5.4}
\]

Here \(\mu_{a,X}(S)\) is the number of endpoints of \(X\) carrying target
\(S\) at signed rank \(a\).

Because the two anchor ranks have zero loss and different ranks are
disjoint,

\[
 |\mathcal N(X)|
 =(2H+1)|X|-\sum_{a\in\mathcal A_*}\ell_a(X).
 \tag{5.5}
\]

### Theorem 5.1 -- exact \(H\)-Hall cut criterion

For a set \(J\) of noninitial endpoints, an \(H\)-fold target matching
exists if and only if, for every \(X\subseteq J\),

\[
 \boxed{
 \sum_{a\in\mathcal A_*}\ell_a(X)
 \le(H+1)|X|.}
 \tag{5.6}
\]

The exact Hall deficiency is

\[
 \boxed{
 \Delta_H(J)
 =
 \max_{X\subseteq J}
 \left(
 \sum_{a\in\mathcal A_*}\ell_a(X)
 -(H+1)|X|
 \right)_+.}
 \tag{5.7}
\]

#### Proof

Substitute (5.5) into the Hall inequality
\(|\mathcal N(X)|\ge H|X|\) and into the deficiency formula (2.4).
\(\square\)

Equation (5.6) is the exact stateful target-Hall condition.  It is an
all-subset density bound, not merely a global support estimate.

For

\[
 p=\left\lceil\frac WH\right\rceil,
 \tag{5.8}
\]

the sharp missing global theorem is:

> Find \(p\) noninitial, box-compatible endpoints in the one legal odd-
> factor MTF word such that (5.6) holds for every endpoint subset.

This would give \(Hp\ge W\) distinct literal targets on the desired
\(\Theta(W/H)\) physical portals.  The simultaneous relabelling theorem
would then make the endpoint--box loss negligible.

### 5.1 Relation to quadratic collision energy

For every \(X\) and signed rank \(a\),

\[
 \ell_a(X)
 \le
 \sum_S\binom{\mu_{a,X}(S)}2.
 \tag{5.9}
\]

Hence the sufficient local energy condition

\[
 \sum_{a\in\mathcal A_*}\sum_S
 \binom{\mu_{a,X}(S)}2
 \le(H+1)|X|
 \quad\text{for every }X\subseteq J
 \tag{5.10}
\]

implies Hall.

The global quadratic bound

\[
 \mathfrak K_H\le(1+o(1))H^2W
 \tag{5.11}
\]

from the previous stateful extraction report does not imply (5.10):
collision energy may concentrate on a small endpoint subset.  Conversely,
(5.6) controls repetition loss rather than all collision pairs, so high
multiplicity in a few permitted fibers may violate (5.10) without violating
Hall.  The two criteria serve different purposes:

* (5.11) is sufficient for an uneven random-thinned extraction on some
  \(p\) endpoints;
* (5.6) is necessary and sufficient for exactly \(H\) distinct targets per
  selected endpoint.

---

## 6. The minimal deficient cut

The exact cut formula permits a sharp local analysis.

### Lemma 6.1 -- no one- or two-endpoint deficiency

Let \(J\) consist of noninitial odd-factor endpoints.  If
\(|X|\le2\), then

\[
 |\mathcal N(X)|\ge H|X|.
 \tag{6.1}
\]

Thus every \(H\)-Hall deficient cut has at least three endpoints and meets
at least three complementary-geodesic components.

#### Proof

A singleton flag has \(2H+1\ge H\) targets.

For two endpoints, the middle and upper-depth-one targets are distinct,
giving four anchor targets.  At each of the remaining \(2H-1\) signed
ranks there is at least one target.  Hence

\[
 |\mathcal N(X)|
 \ge4+(2H-1)=2H+3>2H.
 \tag{6.2}
\]

Alternatively, the assertion that a deficient set meets at least three
components follows from Corollary 3.2. \(\square\)

For a three-endpoint set, the same argument gives the universal lower bound

\[
 |\mathcal N(X)|\ge6+(2H-1)=2H+5.
 \tag{6.3}
\]

This can be smaller than the demand \(3H\) exactly when \(H\ge6\).

### Theorem 6.2 -- a sharp three-state Hall cut

Assume

\[
 H\ge6,
 \qquad
 m\ge2H+1.
 \tag{6.4}
\]

There exist three saturated canonical radius-\(H\) MTF states, with
distinct middle targets and distinct upper-depth-one targets, such that
their endpoint--target graph has

\[
 |\mathcal N(X)|=2H+5.
 \tag{6.5}
\]

For endpoint demand \(H\), this three-endpoint cut has exact deficit

\[
 \boxed{
 3H-(2H+5)=H-5.}
 \tag{6.6}
\]

Each state separately extends to a long complementary-geodesic canonical
MTF component.

#### Construction

Choose a set \(C\) of size

\[
 |C|=m-H.
 \tag{6.7}
\]

Choose distinct elements

\[
 d_2,\ldots,d_H,\quad
 x_1,x_2,x_3,\quad
 y_3,\ldots,y_H
 \tag{6.8}
\]

outside \(C\).  The total number of used coordinates is

\[
 (m-H)+(H-1)+3+(H-2)=m+H\le2m.
 \tag{6.9}
\]

For \(1\le q\le H\), define the common lower chain

\[
 L_q
 =
 C\cup\{d_{q+1},d_{q+2},\ldots,d_H\},
 \tag{6.10}
\]

where the added set is empty at \(q=H\).  Then

\[
 |L_q|=m-q.
 \tag{6.11}
\]

Define three middle targets

\[
 T_i=L_1\cup\{x_i\},
 \qquad i=1,2,3.
 \tag{6.12}
\]

Take the three distinct upper-depth-one targets

\[
 \begin{aligned}
 U_{1,1}&=L_1\cup\{x_1,x_2\},\\
 U_{2,1}&=L_1\cup\{x_2,x_3\},\\
 U_{3,1}&=L_1\cup\{x_3,x_1\}.
 \end{aligned}
 \tag{6.13}
\]

Their common rank-\((m+2)\) extension is

\[
 U_2=L_1\cup\{x_1,x_2,x_3\}.
 \tag{6.14}
\]

For \(3\le q\le H\), put

\[
 U_q
 =
 U_2\cup\{y_3,\ldots,y_q\}.
 \tag{6.15}
\]

For each \(i\), the chain

\[
 L_H\subset L_{H-1}\subset\cdots\subset L_1
 \subset T_i\subset U_{i,1}\subset U_2\subset\cdots\subset U_H
 \tag{6.16}
\]

is saturated from rank \(m-H\) through rank \(m+H\).

#### Proof of the claims

The three flags share all \(H\) lower targets \(L_q\).  They have three
distinct middle targets and three distinct upper-depth-one targets.  They
share the \(H-1\) upper targets \(U_2,\ldots,U_H\).  Hence their union has

\[
 H+3+3+(H-1)=2H+5
\]

targets, proving (6.5)--(6.6).

Every consecutive difference in (6.16) is a singleton.  Moreover the first
block \(L_H=C\) and the complement of \(U_H\) both have size \(m-H\).
Therefore the successive differences in (6.16), followed by
\([2m]\setminus U_H\), form an ordered partition with the canonical block
sizes

\[
 (m-H),\underbrace{1,\ldots,1}_{2H\text{ times}},(m-H).
 \tag{6.17}
\]

Thus (6.16) is the prefix flag of a legitimate canonical MTF state.

It can be placed at an internal, noninitial position of a complementary
geodesic.  Let

\[
 D_i=T_i\setminus C
\]

be the \(H\) desired future departures, and let

\[
 P_i=U_H\setminus T_i
\]

be the \(H\) desired recent past departures.  Since
\(|C|=m-H\ge H\), choose an \(H\)-set \(Q_i\subseteq C\).  Start the
geodesic at

\[
 A_i=(T_i\setminus Q_i)\cup P_i.
\]

During its first \(H\) steps, remove the elements of \(P_i\) in the reverse
order required by the upper flag and insert the elements of \(Q_i\).
The state after those \(H\) steps is \(T_i\), and its first \(H\) upper
singletons are precisely the prescribed recent departures.  Next remove
the elements of \(D_i\) in the order prescribed by the lower flag.  Because
\(Q_i\subseteq C\) and \(D_i\cap C=\varnothing\), no inserted coordinate is
later removed.  Order all remaining departures and arrivals arbitrarily.
This completes a complementary geodesic and realizes (6.16) at a
noninitial endpoint. \(\square\)

### Scope of Theorem 6.2

The three components constructed in Theorem 6.2 are independently legal
long canonical components.  The theorem does not assert that they are
simultaneously middle-disjoint or extendible to one exact odd factor.
Accordingly:

* it is a sharp counterexample to any proposed proof of three-component
  Hall using only the local canonical-state axioms and the two global
  anchor injections;
* it is not proof that the actual odd-factor endpoint graph contains a
  deficient triple.

Any proof that the exact odd factor avoids (6.16) must use additional
cross-component geometry.

### 6.1 Boundary endpoints

If initial endpoints are retained, the upper-depth-one boundary targets
need not be globally injective.  With only the globally unique middle rank,
the universal three-endpoint lower bound becomes

\[
 3+2H,
 \tag{6.18}
\]

and an abstract deficient triple is possible already for \(H\ge4\), with
maximum deficit \(H-3\).  Since only \(B=W/(m+1)=o(W)\) endpoints are
initial, the Gaussian portal problem may discard them.  The sharper
noninitial formulation is therefore the relevant one.

---

## 7. Structure of an inclusion-minimal deficient cut

Let \(J\) be any endpoint family with uniform demand \(b\), and let
\(X\subseteq J\) be inclusion-minimal with positive Hall deficit

\[
 \delta
 =
 b|X|-|\mathcal N(X)|
 \ge1.
 \tag{7.1}
\]

For \(v\in X\), define the number of targets private to \(v\) within the
cut:

\[
 p_X(v)
 =
 |\mathcal F(v)\setminus\mathcal N(X\setminus\{v\})|.
 \tag{7.2}
\]

### Theorem 7.1 -- private-target bound in a minimal cut

For every \(v\in X\),

\[
 \boxed{
 p_X(v)\le b-\delta.}
 \tag{7.3}
\]

If every endpoint has \(R\) candidate targets, then every endpoint of the
minimal cut shares at least

\[
 \boxed{
 R-b+\delta}
 \tag{7.4}
\]

of its targets with another endpoint of \(X\).

For the canonical portal parameters

\[
 R=2H+1,
 \qquad
 b=H,
 \tag{7.5}
\]

every endpoint in a minimal deficient cut shares at least

\[
 \boxed{H+1+\delta}
 \tag{7.6}
\]

targets with the rest of the cut.

#### Proof

By inclusion minimality, \(X\setminus\{v\}\) is not deficient, so

\[
 |\mathcal N(X\setminus\{v\})|
 \ge b(|X|-1).
 \tag{7.7}
\]

The full neighborhood is the disjoint union of that neighborhood and the
targets private to \(v\):

\[
 |\mathcal N(X)|
 =
 |\mathcal N(X\setminus\{v\})|+p_X(v).
 \tag{7.8}
\]

Together with

\[
 |\mathcal N(X)|=b|X|-\delta,
\]

this gives

\[
 b|X|-\delta
 \ge b(|X|-1)+p_X(v),
\]

which is (7.3).  Subtract from \(R\) to obtain (7.4)--(7.6).
\(\square\)

On noninitial odd-factor endpoints, the middle and upper-depth-one targets
are globally private.  Hence

\[
 p_X(v)\ge2,
 \tag{7.9}
\]

and Theorem 7.1 also gives

\[
 \delta\le H-2.
 \tag{7.10}
\]

The sharp abstract triple of Theorem 6.2 has

\[
 \delta=H-5
\]

and exactly two private targets per endpoint inside the triple: its middle
target and its upper-depth-one target.  It is consistent with (7.3), which
only requires \(p_X(v)\le5\) in this case.

The decisive content of (7.6) is qualitative: a minimal obstruction cannot
be caused by a few isolated repeated masks.  Every endpoint in it must
participate in shared fibers at more than half of the available signed
ranks.

---

## 8. Product-box cells after target Hall

For a selected endpoint set \(J\), the exact joint problem may be written as
a three-level flow:

\[
 \text{endpoint }v
 \longrightarrow
 \text{cell }(v,\mathcal B)
 \longrightarrow
 \text{target }S.
 \tag{8.1}
\]

The source-to-endpoint capacity is \(H\), every endpoint-to-cell capacity is
one, and every target has capacity one.  An edge from
\((v,\mathcal B)\) to \(S\) exists only when

\[
 S\in\mathcal F(v)\cap\mathcal B.
 \tag{8.2}
\]

This flow enforces both state capacity and one incidence per endpoint--box
cell.

If every selected endpoint is box-rainbow, its \(2H+1\) target neighbors
use distinct cells and the cell layer may be contracted.  The joint flow is
then exactly the Hall graph of Section 2.  This is the situation in Theorem
4.1.

For arbitrary selected endpoints, let

\[
 \lambda_v
 =
 (2H+1)
 -
 |\{\mathcal B:\mathcal F(v)\cap\mathcal B\ne\varnothing\}|.
 \tag{8.3}
\]

Then

\[
 \sum_v\lambda_v
 \le
 \operatorname{Col}^{\rm MTF}_H(\sigma)
 =O_A(HW/m)=o(W).
 \tag{8.4}
\]

Thus box-cell contraction costs only \(o(W)\) globally.  It still cannot
repair a target Hall deficiency: deleting or splitting endpoint capacity
never creates a missing target edge.  This formally locates the global SCD
incidence theorem on the cell side of the flow.

---

## 9. What is proved and what remains open

### Proved

1. One coordinate relabelling simultaneously preserves
   \(\Theta(HW)\) useful global-SCD box incidence and makes the canonical
   MTF endpoint--box collision count \(O_A(HW/m)=o(W)\).
2. Target Hall deficiencies are invariant under this relabelling; same-box
   or same-SCD-chain membership cannot replace literal target equality.
3. The exact endpoint-capacitated Hall/min-cut formula is (2.3)--(2.5).
4. Every endpoint family contained in two long complementary-geodesic
   components satisfies \(H\)-fold Hall.
5. After the common relabelling, two such components contain
   \(2(m+1)-O_A(H)\) box-rainbow endpoints and an integral literal matching
   of size \(2H(m+1)-O_A(H^2)\).
6. On noninitial endpoints, the exact global Hall condition is the
   all-subset collision-loss inequality (5.6).
7. Every deficient cut spans at least three components.  For \(H\ge6\), a
   three-endpoint cut is the first one allowed by the audited local state
   constraints.
8. The explicit canonical-state pattern in Theorem 6.2 attains the sharp
   three-endpoint deficit \(H-5\).
9. Every endpoint of an inclusion-minimal deficit-\(\delta\) cut must share
   at least \(H+1+\delta\) of its \(2H+1\) targets within the cut.

### Unproved

No set of \(\lceil W/H\rceil\) endpoints satisfying (5.6) is constructed.
The three-state deficient pattern is not proved to occur inside an exact
odd factor, and it is not proved avoidable there.  The relabelled global SCD
incidence theorem supplies cell capacity but no endpoint--target expansion.

The precise surviving theorem is therefore:

> Find \(\lceil W/H\rceil\) noninitial endpoints of one exact-factor
> adaptive-MTF word for which every subset \(X\) satisfies
> \[
> \sum_{a\ne0,+1}
> \bigl(|X|-|\mathcal N_a(X)|\bigr)
> \le(H+1)|X|.
> \]

Equivalently, prove that the endpoint target-collision hypergraphs have no
subfamily whose aggregate repetition density exceeds \(H+1\) per endpoint.
Any counterexample has a minimal cut satisfying Theorem 7.1 and spanning at
least three long components.

This is strictly a theorem about literal targets inside one legal word.  It
does not invoke labelled common-owner synchronization, mix exact factors,
or infer target support from product-box incidence.

---

## 10. Internal audit

1. **Hall orientation.**  The extraction problem saturates endpoint clones,
   so its cuts are endpoint subsets as in (2.3).  Covering a prescribed SCD
   family has the opposite target-subset cuts (2.8); the two problems are
   not conflated.
2. **Clone deficiency.**  Once one clone of an endpoint is present in a
   deficient clone set, adding every other clone adds no neighbor and cannot
   decrease deficiency.  Hence (2.5) maximizes over whole endpoints.
3. **Two-component constant.**  The middle rank contributes \(|X|\), and
   each of \(2H\) other ranks contributes at least \(x_{\max}\).  For two
   components this is at least \((H+1)|X|\), leaving one full unit of Hall
   slack per endpoint beyond demand \(H\).
4. **Common relabelling.**  The SCD and MTF box-collision estimates are both
   first-moment inequalities for the same uniform permutation.  Adding
   their expectations justifies one simultaneous choice.
5. **Good-component count.**  Dividing
   \(O_A(HW/m)\) by \(B=W/(m+1)\) gives \(O_A(H)\), not
   \(O_A(H/m)\).  Deleting \(O_A(H)\) bad endpoints from a length-\(m+1\)
   component leaves \(m+1-O_A(H)\).
6. **Three-cut threshold.**  With two anchor ranks and \(2H-1\) remaining
   ranks, three endpoints have union at least
   \(6+(2H-1)=2H+5\).  This is below \(3H\) exactly for \(H\ge6\), and the
   constructed deficit is \(H-5\).
7. **Canonical realization.**  The triple construction uses exactly
   \(m+H\) coordinates before the final residual, leaving a block of size
   \(m-H\).  Each displayed chain is therefore the prefix chain of a valid
   canonical ordered partition.
8. **Exact-factor caveat.**  Separate extension of the three states to long
   complementary geodesics does not prove simultaneous middle-disjointness
   or membership in one exact factor.  The report states only the local
   sharpness that is proved.
9. **Box versus target.**  Product-box relabelling changes cell conflicts
   but preserves target equalities.  Every implication in the report follows
   the direction target matching \(\rightarrow\) cell matching, never the
   reverse.

## 11. Final conclusion

The stateful endpoint--target problem now has an exact Hall description and
a first sharp regime:

\[
 \boxed{
 \begin{gathered}
 \text{two long canonical components}
 \Longrightarrow
 H\text{-fold Hall},\\
 \text{common relabelling}
 \Longrightarrow
 2H(m+1)-O_A(H^2)
 \text{ distinct target--cell matches},\\
 \text{global failure}
 \Longrightarrow
 \text{a minimal cut on at least three components with}\\
 \sum_{a\ne0,+1}\ell_a(X)>(H+1)|X|
 \text{ and at least }H+2\text{ shared targets per endpoint}.
 \end{gathered}}
 \tag{11.1}
\]

The relabelled global SCD theorem supplies abundant box capacity, but the
remaining Gaussian obstruction is exactly the existence of a dense
cross-component target-collision cut.
