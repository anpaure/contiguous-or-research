# Owner-rooted mixed-SCD orbits and the dynamic empty-rectangle gate

Date: 2026-07-26

Method: pure mathematics only.  No computation, search, solver,
probabilistic black box, or web input is used.

## 0. Result

The BTK decomposition and every \(O(\log\log m)\)-sized catalogue of its
coordinate conjugates remain excluded by the record-tail countercuts.
This note replaces that catalogue by a genuinely mixed, endpoint-rooted
SCD orbit.

Start with an explicit noncanonical SCD \({\mathscr D}\) obtained by
tensoring the cyclic \(B_4\) seed

\[
 14\longrightarrow12\longrightarrow23\longrightarrow34
 \longrightarrow14
                                                               \tag{0.1}
\]

over four-blocks and symmetrically decomposing the resulting products of
chains.  Use the complete labelled coordinate orbit

\[
 {\mathfrak E}
  =\{\pi{\mathscr D},\pi{\mathscr D}^{\,c}:\pi\in{\mathfrak S}_m\}.
                                                               \tag{0.2}
\]

Here the complemented colour is included only to make the ensemble
closed under raw complementation.  The conclusion below does not depend
on special properties of the seed: the complete-orbit law holds for the
orbit of every SCD.  The ensemble uses independently rooted occurrences
from the entire orbit, rather than one coordinate-ordered BTK colour.

Fix ranks

\[
 r,\quad m-r,\qquad h=m-2r,\qquad k=m-r=r+h.                    \tag{0.3}
\]

At a prescribed upper endpoint \(T\in\binom{[m]}k\), the labelled
occurrences in (0.2) realize every active alphabet

\[
                         U\in\binom Th                           \tag{0.4}
\]

with exactly the same multiplicity.  They also realize every ordering of
each \(U\) with the same multiplicity.  The bottom-end statement is
identical with \(U\subseteq[m]\setminus B\).

Consequently, at a high endpoint of a two-half product path, the exact
conservative safe-option fraction against incoming queue supports of
sizes \(f,g\) is

\[
 p_{f,g}
   ={\binom{k-f}{h}\binom{k-g}{h}\over\binom kh^2}.              \tag{0.5}
\]

More strongly, the bipartite graph between all such history supports and
all active-alphabet pairs is biregular.  Therefore every empty rectangle
\({\cal F}\times{\cal U}\) satisfies

\[
 { |{\cal F}|\over
       \binom kf\binom kg}
 +{ |{\cal U}|\over
       \binom kh^2}
 \le1.                                                          \tag{0.6}
\]

This is an exact dynamic empty-rectangle theorem.  It holds for every
subset of histories, including histories selected adaptively by a
coherent route; no independence or first moment is used.

The same statement remains true after the literal Johnson seam is put
back.  Once the rank profile, queue-region counts, seam orientation, and
base-chain types are fixed, every nonempty physical state-to-coloured-path
transition block is biregular and therefore has normalized Hall with zero
deficiency.

At

\[
 H=\sqrt m\,\omega,\qquad \omega=\log\log m,\qquad
 h=C\sqrt m,                                                    \tag{0.7}
\]

and \(f+g\le2H+O(1)\),

\[
                         p_{f,g}\ge e^{-O_C(\omega)}
                                  =(\log m)^{-O_C(1)}.           \tag{0.8}
\]

Thus the BTK six-label phenomenon disappears completely in the full
mixed option stack.

There is one load-bearing qualification.  The options in (0.2) are
independently coloured chain occurrences.  Selecting a different colour
at each endpoint need not produce one SCD: the selected chains may
overlap at intermediate ranks.  The exact remaining gate is an integral
chain-grouping problem.  The empty-rectangle theorem solves the dynamic
history-versus-active-alphabet Hall system before grouping, but does not
prove that its matched options form one owner-disjoint SCD or one
product-path partition.

## 1. A concrete noncanonical base SCD

On a four-set use the six-chain SCD

\[
\begin{array}{ccl}
 \varnothing&\subset&1\subset14\subset124\subset1234,\\
 2&\subset&12\subset123,\\
 3&\subset&23\subset234,\\
 4&\subset&34\subset134,\\
 &&13,\\
 &&24.
\end{array}                                                     \tag{1.1}
\]

Its central nontrivial diamonds contain the directed cycle (0.1), so it
is not a fixed-priority ordered-star SCD.

Partition \(4\lfloor m/4\rfloor\) coordinates into four-blocks, put
(1.1) in every block, and use any SCD on the at most three remaining
coordinates.  The Cartesian products of the resulting local chains
partition \(B_m\) into products of chains.  A product of chains admits a
symmetric-chain decomposition, inductively from the usual two-chain grid
decomposition.  Decomposing every product cell gives a full SCD
\({\mathscr D}\) of \(B_m\).

The later counting theorem uses only that \({\mathscr D}\) is an SCD.
Thus no unproved global promotion property of this tensor construction is
being assumed.

For a chain \(C\in{\mathscr D}\) whose minimum rank is at most \(r\), let

\[
 B_r(C)\subset T_r(C),\qquad
 |B_r(C)|=r,\quad |T_r(C)|=m-r,                                 \tag{1.2}
\]

be its unique rank-\(r\) and rank-\((m-r)\) members.  Its central active
alphabet and ordered word are

\[
 A_r(C)=T_r(C)\setminus B_r(C),\qquad
 {\bf a}_r(C)=(a_1,\ldots,a_h),                                 \tag{1.3}
\]

where the chain adds \(a_1,\ldots,a_h\) between the two displayed ranks.

There are exactly

\[
                         \binom mr                               \tag{1.4}
\]

such central segments: every rank-\(r\) set belongs to one chain, and
that symmetric chain reaches rank \(m-r\).

## 2. The complete active-alphabet design

Keep the conjugating permutation as a label, even when two permutations
happen to give the same unlabelled SCD.

### Theorem 2.1 (exact stabilizer-orbit law)

Fix \(T\in\binom{[m]}{m-r}\), \(U\in\binom Th\), and an ordering
\({\bf u}\) of \(U\).  The number of pairs

\[
 (\pi,C),\qquad \pi\in{\mathfrak S}_m,\quad
 C\in{\mathscr D},\quad \min(C)\le r,                             \tag{2.1}
\]

such that

\[
 \pi T_r(C)=T,\qquad
 \pi A_r(C)=U,\qquad
 \pi{\bf a}_r(C)={\bf u}                                        \tag{2.2}
\]

is exactly

\[
                         \binom mr(r!)^2.                        \tag{2.3}
\]

After forgetting the order, every \(U\in\binom Th\) has multiplicity

\[
                         \binom mr\,h!(r!)^2.                    \tag{2.4}
\]

The same statements hold when the chain minimum is prescribed to equal
any \(a\le r\), with \(\binom mr\) in (2.3)--(2.4) replaced by

\[
                         b_a=\binom ma-\binom m{a-1}.            \tag{2.5}
\]

#### Proof

Fix one central segment \(C\).  The ground set is partitioned into

\[
 A_r(C),\qquad B_r(C),\qquad [m]\setminus T_r(C)                 \tag{2.6}
\]

of sizes \(h,r,r\).  For a prescribed ordered word \({\bf u}\), there
is one bijection from the ordered alphabet \({\bf a}_r(C)\) to
\({\bf u}\), and there are independently \(r!\) bijections on each of
the other two parts.  Hence precisely \((r!)^2\) permutations satisfy
(2.2) for this segment.  Sum over the \(\binom mr\) segments in (1.4).

If order is forgotten, the alphabet may be mapped to \(U\) in \(h!\)
ways, giving (2.4).  Finally, the number of chains of minimum rank exactly
\(a\) is (2.5), and every such chain has one segment (1.2).  The same
count proves the last assertion. \(\square\)

Thus the full orbit is an exact complete design, not merely a random
source with correct first moments.  In particular, independently chosen
colours at adjacent endpoints have active-alphabet intersection with the
hypergeometric law.  When \(h=\Theta(\sqrt m)\), two such alphabets have
expected intersection

\[
                         {h^2\over k}=\Theta(1),                 \tag{2.7}
\]

so their symmetric difference is \(2h-O_{\rm av}(1)\).  This violates
the bounded-edit mechanism used by both BTK countercuts.

### Corollary 2.2 (bottom-rooted law and complement)

Fix \(B\in\binom{[m]}r\).  Among the labelled orbit occurrences rooted at
\(B_r(C)=B\), every active \(h\)-set

\[
                         U\subseteq[m]\setminus B                \tag{2.8}
\]

and every order on it has the same multiplicity.  Raw complementation
interchanges this bottom-rooted fibre with the corresponding top-rooted
fibre in the complemented colour \({\mathscr D}^{\,c}\).

#### Proof

Use the ordered partition
\[
 B_r(C),\quad A_r(C),\quad[m]\setminus T_r(C)
\]
in the proof of Theorem 2.1.  Complementation reverses the chain and
swaps its bottom and top. \(\square\)

## 3. Product paths and the exact conservative safe graph

Take disjoint coordinate halves \(A,B\), each of size \(m\), and
independent colours from \({\mathfrak E}\) in the two halves.  At a high
rank-\(m\) product endpoint write

\[
 X=S\mathbin{\dot\cup}T,\qquad
 |S|=m-r=k,\quad |T|=r.                                          \tag{3.1}
\]

Traversing the central product segment toward its low endpoint removes
an ordered active alphabet

\[
                         U_A\in\binom Sh                          \tag{3.2}
\]

and inserts an ordered active alphabet

\[
                         U_B\in\binom{B\setminus T}h.            \tag{3.3}
\]

The product level condition that at least one child chain has minimum
exactly \(r\) changes only the common multiplicity: Theorem 2.1 is
uniform for every prescribed pair of child minimum types.  Hence the
pair \((U_A,U_B)\) is uniform on

\[
 {\cal U}_h(S,T)
 =\binom Sh\times\binom{B\setminus T}h                            \tag{3.4}
\]

in the labelled option catalogue.

Let a valid signed two-queue state have recent insertion and removal
supports \({\cal I},{\cal R}\).  Validity of the history itself implies

\[
                         {\cal I}\subseteq X,\qquad
                         {\cal R}\subseteq X^c.                  \tag{3.5}
\]

Put

\[
 I={\cal I}\cap S,\quad |I|=f,\qquad
 R={\cal R}\cap(B\setminus T),\quad |R|=g.                       \tag{3.6}
\]

Avoiding the full incoming supports,

\[
                         U_A\cap I=\varnothing,\qquad
                         U_B\cap R=\varnothing,                  \tag{3.7}
\]

is sufficient for every edge of the product segment to pass the signed
two-queue test.  It is conservative because some old queue entries may
expire before the corresponding direction is read.

Define

\[
 \begin{split}
 {\cal H}_{f,g}(S,T)
   &=\binom Sf\times\binom{B\setminus T}g,\\
 {\cal U}_{h}(S,T)
   &=\binom Sh\times\binom{B\setminus T}h.
 \end{split}                                                     \tag{3.8}
\]

Join \((I,R)\) to \((U_A,U_B)\) precisely under (3.7).

### Theorem 3.1 (dynamic Kneser empty rectangles)

The graph in (3.8) is biregular.  For every
\({\cal F}\subseteq{\cal H}_{f,g}(S,T)\),

\[
 {|\Gamma({\cal F})|\over|{\cal U}_h(S,T)|}
       \ge { |{\cal F}|\over|{\cal H}_{f,g}(S,T)|}.              \tag{3.9}
\]

Equivalently, if
\({\cal F}\subseteq{\cal H}_{f,g}(S,T)\) and
\({\cal V}\subseteq{\cal U}_{h}(S,T)\) have no legal pair between
them, then

\[
 { |{\cal F}|\over\binom kf\binom kg}
 +{ |{\cal V}|\over\binom kh^2}\le1.                            \tag{3.10}
\]

These assertions hold for an arbitrary set \({\cal F}\) of queue
supports.  In particular \({\cal F}\) may be the set of histories
actually reached by an adaptive coherent route.

#### Proof

Every history vertex has degree

\[
                         d_L=\binom{k-f}h\binom{k-g}h,            \tag{3.11}
\]

and every option vertex has degree

\[
                         d_R=\binom{k-h}f\binom{k-h}g.            \tag{3.12}
\]

Thus the graph is biregular.  Count the edges leaving
\({\cal F}\):

\[
 d_L|{\cal F}|
 \le d_R|\Gamma({\cal F})|.                                    \tag{3.13}
\]

The total edge identity

\[
 d_L|{\cal H}_{f,g}|=d_R|{\cal U}_h|                            \tag{3.14}
\]

turns (3.13) into (3.9).  If \({\cal F}\times{\cal V}\) is empty, then
\({\cal V}\subseteq{\cal U}_h\setminus\Gamma({\cal F})\);
(3.9) gives (3.10). \(\square\)

The theorem is stronger than a positive-degree statement: after uniform
cloning of the two shores it gives Hall with zero deficiency.  It also
contains both signs.  Complementation merely interchanges the two
disjointness coordinates and the two orbit colours.

### Theorem 3.2 (typed physical transition blocks)

Retain the literal cross-half Johnson seam.  Fix all of the following
finite type data:

1. the level and high/low orientation of the current endpoint;
2. the numbers of insertion-queue and removal-queue labels in each of
   the four half/owner regions;
3. one of the two cross-half seam orientations;
4. the two child minimum ranks; and
5. the two particular base chains of \({\mathscr D}\) whose labelled
   coordinate orbits supply the next product segment.

Let \({\cal L}_\tau\) be all physical signed queue-support states of this
type and
let \({\cal R}_\upsilon\) be all labelled mixed-orbit product segments of
the prescribed right type.  Join a left state to a right occurrence when
there is a literal seam of the prescribed orientation and the seam plus
the entire segment obeys the conservative full-queue avoidance test.

Every nonempty such bipartite graph is biregular.  Consequently

\[
 {|\Gamma({\cal F})|\over|{\cal R}_\upsilon|}
 \ge {|{\cal F}|\over|{\cal L}_\tau|}                         \tag{3.15}
\]

for every \({\cal F}\subseteq{\cal L}_\tau\), and every empty rectangle
\({\cal F}\times{\cal V}\) satisfies

\[
 {|{\cal F}|\over|{\cal L}_\tau|}
 +{|{\cal V}|\over|{\cal R}_\upsilon|}\le1.                    \tag{3.16}
\]

#### Proof

The group
\[
                         G={\mathfrak S}_A\times{\mathfrak S}_B
\]
acts transitively on the left states: the displayed type data specify
all cardinalities of the relevant disjoint regions, and a permutation
may map the labels in each region arbitrarily.  Fixing the two base-chain
identities, Theorem 2.1 shows that \(G\) also acts transitively on the
right labelled occurrences.  The seam relation and full-queue
disjointness are invariant under \(G\).

An invariant bipartite graph on two transitive \(G\)-sets has constant
left degree and constant right degree.  It is therefore biregular.
The edge-count proof (3.13)--(3.14) gives (3.15)--(3.16). \(\square\)

Theorem 3.2 is the physical dynamic empty-rectangle bound at the
mixed-option level.  The conservative avoidance rule forgets ages and
uses only queue supports, so it is enough to retain the region counts.
There are only polynomially many such count types through
\(H=m^{1/2+o(1)}\).

## 4. The calibrated survival probability

For one fixed history support, Theorem 3.1 gives the exact safe fraction

\[
 p_{f,g}
 ={d_L\over|{\cal U}_h|}
 ={\binom{k-f}h\binom{k-g}h\over\binom kh^2}.                   \tag{4.1}
\]

### Lemma 4.1 (Gaussian-scale queue cost)

If \(f+g+h=o(k)\), then

\[
 \log p_{f,g}
  =-{h(f+g)\over k}
   +O\left({h(f+g)(h+f+g)\over k^2}\right).                     \tag{4.2}
\]

Consequently, for

\[
 H=\sqrt m\,\omega,\qquad h=C\sqrt m,\qquad
 f+g\le2H+O(1),                                                 \tag{4.3}
\]

one has

\[
                         p_{f,g}\ge\exp(-O_C(\omega)).           \tag{4.4}
\]

For \(\omega=\log\log m\), this is
\((\log m)^{-O_C(1)}\).

#### Proof

Apply
\[
 \log{\binom{k-s}h\over\binom kh}
 =\sum_{i=0}^{h-1}\log\left(1-{s\over k-i}\right)
\]
with \(s=f,g\), and expand \(\log(1-x)\).  Since
\(k=(m+h)/2\), substitution of (4.3) gives (4.4). \(\square\)

Using the same length core as in the two-queue theorem,

\[
 {\sqrt m\over\omega}
 \le h\le
 \sqrt{m(\log\omega+3\log\log\omega)},                          \tag{4.5}
\]

deletes only \(o(W/H)\) product components.  Uniformly on this core,

\[
             p_{f,g}\ge
       \exp\bigl(-O(\omega\sqrt{\log\omega})\bigr)=m^{-o(1)}.    \tag{4.6}
\]

Thus the full mixed orbit has no statewise \(O(H)\)-label entropy cut.

## 5. A route-level Hall corollary and its hypothesis

The exact normalized inequality can be used when a coherent route
produces a controlled multiset of queue states.

Fix one fibre (3.8).  Give the history type \(\xi\) an integral demand
\(d_\xi\).  Give every option type the same integer capacity \(c\), and
assume that both total demand and total option capacity equal

\[
                         n=c|{\cal U}_h|.                       \tag{5.0}
\]

This is the natural labelled-orbit multiplicity scale.  Suppose

\[
                  d_\xi\le(1+\varepsilon)
                     {n\over|{\cal H}_{f,g}|}
                  \qquad\text{for every }\xi.                   \tag{5.1}
\]

### Corollary 5.1 (flat-history entrance matching)

The history demands admit a matching to conservative-safe mixed-SCD
options leaving at most

\[
                         \varepsilon n                          \tag{5.2}
\]

unmatched slots.

#### Proof

For a set \({\cal F}\) of history types, (5.1) bounds its demand by
\[
 (1+\varepsilon)n{|{\cal F}|\over|{\cal H}_{f,g}|}.
\]
Theorem 3.1 gives option capacity at least
\[
 n{|\Gamma({\cal F})|\over|{\cal U}_h|}
 \ge n{|{\cal F}|\over|{\cal H}_{f,g}|}.
\]
Thus every Hall cut has deficiency at most
\(\varepsilon n\).
The deficient Hall theorem proves (5.2). \(\square\)

This is the precise sense in which the histories may be generated
coherently rather than adversarially: the construction need only keep
their multiplicities flat inside the endpoint/minimum-rank/queue-size
fibres.  It need not prove that BTK survives arbitrary histories.

For \(K\) route shelves, Corollary 5.1 and Theorem 3.2 supply the
active-alphabet and typed-endpoint projections of the two-queue Hall
input whenever the accumulated flatness errors satisfy

\[
                         \sum_{j=1}^{K-1}\varepsilon_jn_j
                                  =o(W/H).                       \tag{5.3}
\]

Producing (5.1) by an owner-disjoint route is a separate scheduling
problem; it is not a consequence of the orbit count.  Nor do these
projected Hall statements enforce that two selected coloured path
occurrences have disjoint physical interiors.

## 6. Why this is not yet one randomized SCD

There are three different quantifier orders.

1. For a fixed history and a uniform labelled orbit occurrence,
   Theorem 2.1 gives (4.1).
2. For every family of histories, while all independently coloured
   occurrences remain available, Theorem 3.1 gives (3.10).
3. Choose one global colour \(\pi{\mathscr D}\), reveal it, and then allow
   the history to depend on it.

Only the first two are proved.  The third does not follow.  Indeed, if
the base were BTK, the exact six-coordinate and record-tail cuts would
apply to every chosen colour after it is revealed, despite the complete
orbit satisfying Theorems 2.1 and 3.1 before colour grouping.

The obstruction to choosing colours independently is exact.  Let
\({\cal C}_{\rm orb}\) be the multiset of all symmetric chains occurring
in all labelled colours of (0.2).  Introduce variables

\[
                         x_C\in\{0,1\},
                     \qquad C\in{\cal C}_{\rm orb}.              \tag{6.1}
\]

A mixed selection is one SCD precisely when

\[
                  \sum_{C\ni Z}x_C=1
                  \qquad\text{for every }Z\subseteq[m].         \tag{6.2}
\]

Route safety adds restrictions requiring the selected central segment
at each used endpoint to lie in the appropriate neighborhood of
Theorem 3.1.  The normalized Kneser proof controls these endpoint
restrictions but does not control the intermediate-rank equations (6.2).

The unfiltered system has the exact symmetric fractional solution

\[
                         x_C={1\over2\,m!}                       \tag{6.3}
\]

when chains are counted with their two base colours: each of the
\(2\,m!\)
full SCD colours covers every Boolean set once.  After history-dependent
filtering, (6.3) is no longer automatically feasible, and no total
unimodularity or integer-decomposition theorem is known for (6.2).

Thus the first unresolved interface is not endpoint entropy.  It is:

> **Coherent orbit-chain grouping.**  Select owner-disjoint chain
> occurrences from the complete mixed orbit so that (6.2) holds up to
> the allowed \(o(W/H)\) component leave, the induced queue histories
> obey the flatness condition (5.1), and the selected endpoint options
> remain in the conservative-safe Kneser graph.

This is strictly smaller than arbitrary-history robustness for one BTK
colour and strictly stronger than the fractional orbit average.

## 7. Audited conclusion

Proved:

* an explicit noncanonical base SCD and a complement-closed full orbit;
* exact uniformity of endpoint active alphabets and direction orders,
  separately for every child minimum-rank type;
* an exact two-queue product safe fraction;
* the normalized dynamic empty-rectangle inequalities (3.10) and
  (3.16), valid for every adaptively generated history family in an
  ungrouped orbit fibre and including the literal typed seam;
* polynomial survival at
  \(H=\sqrt m\log\log m\); and
* a deficient-Hall route theorem under the explicit history-flatness
  hypothesis (5.1).

Not proved:

* that one random global SCD is robust after its history is allowed to
  depend on it;
* that independently coloured safe chain occurrences can be grouped into
  one SCD;
* that the resulting product paths are owner-disjoint; or
* coefficient one.

No statewise invariant making every SCD vulnerable has been found.  The
BTK cuts use bounded-edit record tails and do not survive the full mixed
orbit: its active alphabets form the complete \(h\)-subset design.
The positive route is therefore viable at the dynamic endpoint-Hall
level, but its exact remaining task is the integral grouping system
(6.2), not another entropy calculation.
