# Phase-flag cycle hypergraphs: exact degrees, antipodal codegrees, and the adaptive-cycle obstruction

Date: 2026-07-26

Method: pure mathematics only. No computation, finite search, solver, or
web input is used.

## 0. Verdict

Fix a full \(h\)-dimensional orientation-cube cell and protect prefixes
through depth \(H<h\).  A phase flag consists of an owner and an ordered
\(H\)-tuple of distinct pair directions.  An oriented isometric
\(C_{2h}\) with direction word \(\pi\pi\) supplies one phase flag at each
of its \(2h\) owners.

The resulting hypergraph can be calculated exactly.

1. It has

   \[
    v=2^h(h)_{\underline H}
   \]

   flag vertices, edge size \(2h\), and constant degree

   \[
    \boxed{d=(h-H)!.}
   \tag{0.1}
   \]

2. A flag and its antipodal copy have identical links.  Their codegree is
   \(d\), so

   \[
    \boxed{\Delta_2=d.}
   \tag{0.2}
   \]

   Thus the uncontracted hypergraph fails the small-codegree hypothesis of
   every ordinary nibble theorem in the strongest possible way.

3. Contracting each antipodal flag pair gives an \(h\)-uniform regular
   hypergraph of the same degree.  For distinct contracted vertices,

   \[
    \boxed{\Delta_2^{\rm nt}\le2(h-H-1)!
       ={2d\over h-H}.}
   \tag{0.3}
   \]

   This removes the local antipodal obstruction, but it does not solve the
   required grouped matching: there are \((h)_{\underline H}\) possible
   flags over every owner class, and an ordinary matching may choose many
   different flags over the same owner.

4. More decisively, choose one antipodally coherent flag independently and
   uniformly at every folded owner.  If \(L=(h)_{\underline H}\), then the
   expected fraction of owners lying in even one compatible cycle is at
   most

   \[
    \boxed{{h!\over L^h}\le {h!\over h^h}
       =\exp(-h+O(\log h)).}
   \tag{0.4}
   \]

   Hence with probability \(1-o(1)\), a \(1-o(1)\) fraction of owners
   cannot lie in any compatible cycle, before disjointness is even asked.
   Independent uncontracted flags are still worse: antipodal equality
   itself occurs with probability \(1/L\).

Consequently a generic ownerwise version of the \(W^{o(1)}\)-frame SCD
literalization cannot be grouped into cycles after its flags have been
independently fixed.  The degree of the universal flag hypergraph is
large, but an independent restriction to one preselected flag over each
owner annihilates essentially all its edges.  This is an asymptotic
obstruction, not a determinant-two artifact.  It does not rule out a
specially cycle-correlated SCD; it proves that such correlation must be
built before, not inferred from, the ownerwise literalization theorem.

The viable order of construction is the reverse:

\[
 \boxed{\text{choose frame-labelled cycle factors first,
 then inherit their flags, then match targets to phase occurrences}.}
\tag{0.5}
\]

When \(h=2^t\), the owner-grouping part is exact rather than asymptotic:
every \(Q_h\) has a vertex factor into isometric \(C_{2h}\)'s.  What
remains is a target-incidence theorem for the flags induced by a correlated
choice of those factors.  The prior SCD/Hoffman theorem does not supply
that correlation.

## 1. Phase flags and the universal cycle hypergraph

Write

\[
 Q_h=\mathbb F_2^h
\]

and let \(e_0,\ldots,e_{h-1}\) be its coordinate directions.  Put

\[
 \Omega_{h,H}
 =\{(a_0,\ldots,a_{H-1}):a_i\in[h]\text{ distinct}\},
 \qquad
 L=|\Omega_{h,H}|=(h)_{\underline H}.
\tag{1.1}
\]

A phase flag is a pair

\[
 F=(x,\alpha)\in\mathbb F_2^h\times\Omega_{h,H}.
\tag{1.2}
\]

In a pair frame, \(\alpha\) determines both Boolean traces of the forward
window from \(x\).  If \(c_x(a)\) is the coordinate currently selected
from split pair \(a\), then at depth \(q\)

\[
 T_q^-(F)
 =X_x\setminus\{c_x(a_0),\ldots,c_x(a_{q-1})\},
\tag{1.3}
\]

and, writing \(\bar c_x(a)\) for the unselected coordinate,

\[
 T_q^+(F)
 =X_x\cup\{\bar c_x(a_0),\ldots,\bar c_x(a_{q-1})\}.
\tag{1.4}
\]

Thus one physical forward arc fixes the lower and upper target chains
simultaneously.  If a compiler assigns the two sides to opposite arcs of
the cycle instead, the same analysis applies after replacing one of the
two words by the corresponding reversed cyclic suffix.  In either
convention, the two words must be parts of one cyclic permutation; they
cannot be selected independently.

For \(x\in\mathbb F_2^h\) and a permutation

\[
 \pi=(\pi_0,\ldots,\pi_{h-1})\in S_h,
\]

put

\[
 x_i=x+\sum_{j=0}^{i-1}e_{\pi_{j\bmod h}}
 \qquad(0\le i<2h).
\tag{1.5}
\]

The vertices \(x_0,\ldots,x_{2h-1}\) form an oriented isometric
\(C_{2h}\), whose transition word is \(\pi\pi\).  Its phase flag at
\(x_i\) is

\[
 \alpha_i(\pi)
 =(\pi_{i\bmod h},\pi_{i+1\bmod h},
       \ldots,\pi_{i+H-1\bmod h}).
\tag{1.6}
\]

Define \(\mathcal H_{h,H}\) to have vertex set

\[
 \mathcal V_{h,H}
 =\mathbb F_2^h\times\Omega_{h,H}
\tag{1.7}
\]

and one edge

\[
 E(x,\pi)
 =\{(x_i,\alpha_i(\pi)):0\le i<2h\}
\tag{1.8}
\]

for each distinct oriented cycle profile.

Reversal is retained as a different oriented profile, because it produces
different forward flags.  Cyclic change of starting phase does not produce
a new edge.

### Lemma 1.1 (edge count and degree)

\[
 |\mathcal E_{h,H}|=2^{h-1}(h-1)!,
 \qquad
 \deg(x,\alpha)=(h-H)!.
\tag{1.9}
\]

#### Proof

There are \(2^h h!\) pairs \((x,\pi)\).  Every oriented cycle profile has
exactly \(2h\) choices of starting phase, so the first formula follows.

Fix \((x,\alpha)\).  An edge through it is obtained uniquely by extending
the ordered word \(\alpha\) to a permutation of all \(h\) directions.
There are \((h-H)!\) extensions.  Conversely each extension gives one
edge through the flag.  This proves the degree formula. \(\square\)

The incidence identity audits both formulas:

\[
 2^h(h)_{\underline H}(h-H)!
 =2h\cdot2^{h-1}(h-1)!.
\tag{1.10}
\]

If a phase flag lives in a larger orientation cube \(Q_s\) and the
active \(h\)-set is not fixed, its degree becomes

\[
 (s-H)_{\underline{h-H}},
\tag{1.11}
\]

because the remaining \(h-H\) ordered directions may be chosen from the
other \(s-H\) split pairs.  The fixed-cell calculation is the relevant
one after the standard partition into \(Q_h\)-fibres.

## 2. Exact pair codegrees

Take flags

\[
 F=(x,\alpha),\qquad G=(y,\beta),
\]

and put

\[
 D=\{j:x_j\ne y_j\},\qquad d=|D|.
\tag{2.1}
\]

For an offset \(r\in\{0,\ldots,2h-1\}\), define a set of permutation
positions

\[
 J_r=
 \begin{cases}
  \{0,\ldots,r-1\},&0\le r\le h,\\
  \{r-h,\ldots,h-1\},&h<r<2h.
 \end{cases}
\tag{2.2}
\]

Then \(|J_r|=\min(r,2h-r)\).  The equality \(y=x_r\) is equivalent to

\[
 D=\{\pi_j:j\in J_r\}.
\tag{2.3}
\]

Write \(k=r\bmod h\), and set

\[
 I_0=\{0,\ldots,H-1\},
 \qquad
 I_k=\{k,\ldots,k+H-1\}\pmod h.
\tag{2.4}
\]

The flags prescribe \(\pi=\alpha\) on \(I_0\) and
\(\pi=\beta\) on \(I_k\).  Let \(\Gamma_r\) be this partial assignment.
Call \(r\) compatible when

1. the two assignments agree on \(I_0\cap I_k\);
2. no direction is assigned to two different positions;
3. \(|J_r|=d\);
4. every assigned position in \(J_r\) receives a direction in \(D\), and
   every assigned position outside \(J_r\) receives a direction outside
   \(D\).

For a compatible \(r\), put

\[
 u_r=|I_0\cup I_k|,
 \qquad
 t_r=|(I_0\cup I_k)\cap J_r|.
\tag{2.5}
\]

### Theorem 2.1 (exact codegree formula)

For distinct flags,

\[
 \boxed{
 \operatorname{codeg}(F,G)
 =\sum_{\substack{1\le r<2h\\r\ {\rm compatible}}}
 (d-t_r)!\,
 (h-d-u_r+t_r)!.}
\tag{2.6}
\]

At most two terms are nonzero: \(r=d\) and \(r=2h-d\), with the two
coinciding when \(d=h\).

#### Proof

Once \(r\) is fixed, (2.3) forces the positions in \(J_r\) to receive
exactly the labels in \(D\).  The partial assignment has already filled
\(t_r\) of those positions and \(u_r-t_r\) positions outside \(J_r\).
The unfilled positions inside \(J_r\) may be bijected with the remaining
directions of \(D\) in \((d-t_r)!\) ways.  The outside positions may be
filled by the remaining outside directions in
\((h-d-u_r+t_r)!\) ways.  This gives the summand.

The cardinality condition \(|J_r|=d\) permits only \(r=d\) below \(h\)
and \(r=2h-d\) above \(h\).  A simple cycle contains \(G\)'s owner at a
unique phase, so no cycle is counted twice. \(\square\)

### Corollary 2.2 (the antipodal twin)

Let \(\mathbf1=(1,\ldots,1)\).  Then

\[
 \operatorname{codeg}\bigl((x,\alpha),(x+\mathbf1,\beta)\bigr)
 =
 \begin{cases}
  (h-H)!,&\beta=\alpha,\\
  0,&\beta\ne\alpha.
 \end{cases}
\tag{2.7}
\]

Thus \((x,\alpha)\) and \((x+\mathbf1,\alpha)\) have identical links.

#### Proof

Here \(d=h\), the only offset is \(r=h\), and \(I_k=I_0\).
Compatibility is exactly \(\beta=\alpha\).  Formula (2.6) then gives
\((h-H)!\). \(\square\)

### Corollary 2.3 (all non-antipodal codegrees)

If \(y\notin\{x,x+\mathbf1\}\), then

\[
 \operatorname{codeg}(F,G)\le2(h-H-1)!.
\tag{2.8}
\]

#### Proof

For either possible offset, \(k\ne0\), so the two distinct cyclic
length-\(H\) intervals have union size \(u_r\ge H+1\).  Each summand in
(2.6) is a product \(a!b!\), where

\[
 a+b=h-u_r\le h-H-1.
\]

Since \(a!b!\le(a+b)!\), each term is at most
\((h-H-1)!\), and there are at most two terms. \(\square\)

## 3. Antipodal contraction: useful but insufficient

Identify

\[
 (x,\alpha)\sim(x+\mathbf1,\alpha).
\tag{3.1}
\]

Every edge of \(\mathcal H_{h,H}\) consists of \(h\) such antipodal
pairs.  Its quotient \(\overline{\mathcal H}_{h,H}\) therefore has

\[
 \bar v=2^{h-1}(h)_{\underline H},
 \qquad
 \bar k=h,
 \qquad
 \bar d=(h-H)!.
\tag{3.2}
\]

For distinct quotient vertices, Corollary 2.3 gives

\[
 {\bar\Delta_2\over\bar d}
 \le {2\over h-H}.
\tag{3.3}
\]

Thus, when \(h-H\to\infty\), the contracted universal hypergraph has
vanishing relative pair codegree.  This is the only place where a
nibble-scale heuristic is legitimate.

It is not the matching problem required by the compiler.  Over every
folded owner \([x]=\{x,x+\mathbf1\}\) there are \(L\) vertices
\(([x],\alpha)\).  A matching in \(\overline{\mathcal H}_{h,H}\) does
not prevent two selected edges from using different flag vertices over
the same owner.  Adding the owner classes as conflicts changes the problem
to a grouped or rainbow hypergraph matching.  The small ordinary codegree
in (3.3) says nothing about these size-\(L\) conflict cliques.

There is in fact no need for a local owner-only nibble when \(h=2^t\):
the resolvable isometric-cycle theorem supplies an exact \(C_{2h}\)-factor
of \(Q_h\).  The difficulty is retaining prescribed target flags, not
packing the unlabelled owners.

## 4. Independent flag selection destroys all cycle density

The following calculation is the sharp obstruction to postprocessing the
SCD literalization.

Choose independently for every folded owner \([x]\) a uniform word

\[
 A([x])\in\Omega_{h,H}.
\tag{4.1}
\]

Let \(\mathcal G_A\) contain the oriented cycles whose phase flag at every
folded owner equals its selected word.

### Theorem 4.1 (exponential selected-flag sparsity)

\[
 \mathbb E|\mathcal E(\mathcal G_A)|
 ={2^{h-1}(h-1)!\over L^h}.
\tag{4.2}
\]

If \(Z_A\) is the number of folded owners lying in at least one compatible
cycle, then

\[
 {\mathbb E Z_A\over2^{h-1}}
 \le {h!\over L^h}
 \le {h!\over h^h}
 =\exp(-h+O(\log h)).
\tag{4.3}
\]

Consequently \(Z_A=o(2^{h-1})\) with probability \(1-o(1)\).

#### Proof

A cycle has \(h\) distinct folded phase owners and prescribes one word at
each.  Its compatibility probability is exactly \(L^{-h}\).  Multiply by
the edge count in Lemma 1.1 to obtain (4.2).

Every compatible edge contains \(h\) folded owners, so

\[
 Z_A\le h|\mathcal E(\mathcal G_A)|.
\]

Taking expectations gives the first inequality in (4.3).  Since
\(L=(h)_{\underline H}\ge h\), the second follows.  Stirling's formula
gives the last equality.  Markov's inequality, for example at the square
root of the right side of (4.3), proves the probability statement.
\(\square\)

In particular, an absorber allowed to alter only \(o(2^h)\) owner flags
cannot repair an independent selection: with high probability
\((1-o(1))2^h\) owners are outside every compatible cycle.  The repair
must rewrite a positive-density set of flags, which is a redesign rather
than absorption.

If flags are instead selected independently at all \(2^h\) uncontracted
owners, a necessary condition for either member of an antipodal pair to
belong to a selected-profile cycle is

\[
 A(x+\mathbf1)=A(x),
\tag{4.4}
\]

which has probability \(1/L\).  Conditional independence across the other
phase owners only decreases the cycle density further.

The same obstruction persists if every owner receives an independently
random menu of at most \(R\) flags: a fixed cycle is accepted with
probability at most \((R/L)^h\), so the right side of (4.3) is multiplied
by at most \(R^h\).  Stirling's formula shows that this first moment still
tends to zero whenever

\[
 {hR\over eL}\le1-\varepsilon
\]

for a fixed \(\varepsilon>0\).  Thus a random menu must have size at least
about \(eL/h\) merely to escape this obstruction.  An adversarially
correlated menu can of course encode a cycle factor in advance; that is
precisely the cycle-first redesign below.

## 5. Why the preceding \(W^{o(1)}\)-frame theorem does not group

The SCD literalization theorem made two ownerwise choices:

1. a coherent lower chain and a coherent upper chain through each middle
   owner;
2. one of \(W^{o(1)}\) frames that literalizes those chains.

It imposed no relation between flags of different owners.  A physical
cycle imposes the exact covariance identities

\[
 \alpha_{x+\mathbf1}=\alpha_x,
\tag{5.1}
\]

\[
 \alpha_{x_i}
 =(\pi_i,\pi_{i+1},\ldots,\pi_{i+H-1})
 \qquad(0\le i<h).
\tag{5.2}
\]

It also requires the same frame at all \(2h\) phases.  None of
(5.1)--(5.2), nor frame monochromaticity, is a consequence of ownerwise
literalization.

Under the standard single-forward-window convention, the earlier theorem
is even more visibly unsynchronized: it deliberately found disjoint
direction families for its lower and upper chains, while (1.3)--(1.4)
use the same direction word.  Under the alternative opposite-arc
convention, disjointness is allowed only when the two prescribed words
occupy the appropriate prefix and reversed-suffix positions of one cyclic
permutation.  The earlier construction did not impose that relation
either.

Thus its exact Hoffman flows are valid residual path flows, but they are
not phase profiles of complete cycles.  This is not a rounding loss that
an edge-coloring or ordinary hypergraph nibble can repair.

## 6. The cycle-first adaptive redesign

There is a clean exact redesign for owner grouping.

### Theorem 6.1 (cycle-first flag factor)

Let \(h=2^t\ge2\) and \(H<h\).  There is a vertex partition
\(\mathcal F\) of \(Q_h\) into isometric \(C_{2h}\)'s.  Orient every
component and give every owner its induced phase flag (1.6).  Then

1. every owner receives exactly one flag;
2. all antipodal and shift identities (5.1)--(5.2) hold;
3. the selected flag vertices are partitioned by hyperedges of
   \(\mathcal H_{h,H}\).

The same statement holds in \(Q_s\), \(s\ge h\), after fixing an
\(h\)-set of directions, partitioning by the other \(s-h\) spectator
coordinates, and factoring every \(Q_h\)-fibre.

#### Proof

The resolvable isometric \(C_{2h}\)-decomposition of \(Q_h\) supplies one
spanning \(2\)-factor whose components have direction word \(\pi\pi\).
Definition (1.6) supplies the flags, and each vertex lies in one component.
For \(Q_s\), the spectator fibres are disjoint copies of \(Q_h\).
\(\square\)

This theorem shows that the grouped flag hypergraph has a perfect
transversal when flags are chosen after the cycles.  It also explains why
degree/codegree alone was the wrong test: the exact factor is easy
unconstrained, whereas almost every independent transversal of the owner
classes contains essentially no edges.

## 7. Exact criterion for adapting a prescribed flag field

The first direction of a flag defines a successor candidate

\[
 S_\alpha(x)=x+e_{\alpha_x(0)}.
\tag{7.1}
\]

### Proposition 7.1 (cycle covariance criterion)

A full flag field \((\alpha_x:x\in Q_h)\) is a union of oriented
isometric \(C_{2h}\) phase profiles if and only if the following hold.

1. \(S_\alpha\) is a permutation of \(Q_h\).
2. Every orbit of \(S_\alpha\) has length \(2h\).
3. Along every orbit, the first \(h\) transition directions are distinct
   and the next \(h\) repeat them in the same order.
4. For every \(x\) and \(0\le j<H\),

   \[
    \alpha_x(j)=\alpha_{S_\alpha^j(x)}(0).
   \tag{7.2}
   \]

#### Proof

Necessity follows immediately from (1.5)--(1.6).  Conversely, conditions
1--3 make every successor orbit an isometric \(C_{2h}\): every arc of
length at most \(h\) uses distinct directions.  Condition 4 identifies
each prescribed flag, entry by entry, with the phase window of that
cycle. \(\square\)

Already condition 1 is a global collision constraint on the prescribed
depth-one directions.  Conditions 3--4 impose all higher-depth coupling.
This is the sharp deterministic obstruction faced by an SCD-first
construction: its depth-one target ownership must induce an almost
permutational successor field, and its deeper ownership must be the shift
extension of that same field.  Independent depthwise Hall matchings do
not approach this criterion.

## 8. The surviving constant-one gate

The owner grouping problem itself is solved by Theorem 6.1 once frames and
cube fibres are selected cycle-first.  The unresolved task is to retain
target coverage while making that correlated choice.

The correct cycle-first system has variables for frame-labelled cycle
factors and uses their actual phase incidences

\[
 a_{C,q}^\pm(T)
\]

in the target rows.  One must prove that a correlated selection satisfies

\[
 \sum_C a_{C,q}^\pm(T)\ge1
\]

outside \(o(W)\) total target exceptions, or equivalently assign targets
to selected phase occurrences so that the residual layered networks obey
all Hoffman cuts.  The frame selection, cycle selection, and target
ownership can no longer be performed in three independent rounds.

The sharp conclusion is:

\[
 \boxed{
 \begin{array}{c}
 \text{universal flag-cycle hypergraph: high degree after contraction;}\\
 \text{independently selected owner flags: exponentially sparse edges;}\\
 \text{cycle-first adaptive flags: exact owner factor, target Hall open.}
 \end{array}}
\tag{8.1}
\]

Thus whole-cycle grouping does not follow from a post hoc near-perfect
matching argument applied to ownerwise \(W^{o(1)}\)-literalized SCD flags;
the independent model is exponentially obstructed.  The next positive
theorem must be a cycle-first target-incidence theorem, not a stronger
owner-flag nibble.

### Subsequent ternary-carry audit

MATH_OBSTRUCTION_TERNARY_CARRY_MACROCELL_SHADOW_RUN_20260726.md applies
this cycle-first viewpoint to the phase-dense ternary-carry factor.  Its
canonical first-\(t\)-eligible-block quotient has a further labelled
obstruction: every covered depth-\(q\) target must contain one or two
local admissibility runs of total length \(q\).  The maximal local
deficient alphabet has size \(40\), versus \(24\) eligible states, so a
uniform target satisfies the necessary run condition with probability at
most

\[
 \operatorname{poly}(m)\exp(O(q^2/m))(5/8)^q.
\]

Thus one fixed carry atlas misses a positive fraction of Gaussian-depth
targets, and no shore, phase, frame, or whole-component choice inside
that atlas repairs it.  At least
\(\exp((\log(8/5)-o(1))q)\) genuinely transverse atlases are necessary;
an additional component-overlap Hall theorem would still be required.
