# Logarithmic-degree residual matching and independent-boundary corridor pressure

Date: 2026-07-31  
Lane: K, Catalan residual matching  
Status: explicit sharp-scale obstruction and exact deterministic completion
theorem; no unconditional Boolean residual theorem

## 0. Verdict

At survival

\[
 p=m^{-1/3},\qquad
 n=Np,\qquad
 K=\operatorname{Cat}_m=N/m,
\tag{0.1}
\]

the expected ordered-diamond residual scales are

\[
 D=\Theta(m)=\Theta(\log n),\qquad
 \Delta_2=\Theta(m^{1/3}),\qquad
 \frac K n=\Theta(m^{-2/3}).
\tag{0.2}
\]

These four numerical facts do not imply an outer-perfect matching.  There
are explicit four-partite hypergraphs with exactly these scales, every
degree \(\Theta(D)\), and a Hall obstruction of order
\(\Theta(nm^{-2/3})=\Theta(K)\).  A second, exactly regular affine example
has pair-codegree at most two and a parity obstruction despite a uniform
fractional perfect matching.

The positive result is necessarily correlation-sensitive.  Suppose an
absorber-aware partial matching leaves \(h\) vertices on each outer shore.
Pair those endpoints in a bipartite endpoint graph.  For every chosen pair,
take a family of fully matching-aligned independent-boundary absorbers.  If
the endpoint graph satisfies Hall and the absorber lists satisfy either

\[
 \sum_{j<i}\eta_{j,i}<1
\tag{0.3}
\]

in an ordering, or the probability-pressure inequality

\[
                         e\chi(2h-3)\le1,
\tag{0.4}
\]

then one can choose mutually resource-disjoint absorbers and toggle them
simultaneously.  This gives an outer-perfect four-partite matching.

The independent-boundary construction has support length \(O(m)\), but its
two states differ in at most three deleted and five introduced physical
middle resources.  For a bank of generic length-\(\Theta(m)\) corridors,
the unavoidable scalar bottleneck is outer support; the conservative
worst-case count is

\[
                         h(m+1)\le n.
\tag{0.5}
\]

Thus generic long corridors require a core matching with

\[
 h=O(n/m)=O(Nm^{-4/3})=O(Km^{-1/3}),
\tag{0.6}
\]

not merely \(h=O(K)\).  To absorb a Catalan-size leave, the average corridor
length must instead be \(O(m^{2/3})\), or shorter/direct ears must be used.

Outer saturation is still not the forest target.  The completed directed
lift may contain cycles.  An exact contraction-forest criterion for a
palette-neutral replacement is given in Section 7.

There is now one important structured exception to the negative verdict.
The balanced-subcube reserve complement has an explicit full-support
fractional state, obtained from the two signed three-edge path families of
`MATH_THEOREM_CATALAN_BALANCED_SUBCUBE_RESERVE_AND_EXACT_COLLAR_DEFECT_20260731.md`.
Section 8 proves a quantitative relative-interior form.  This discharges
the fractional space-barrier gate for that deterministic recursive
complement, but not for an arbitrary logarithmic-degree thinning.
For the two-coordinate specialization, the stronger dual-rank theorem now
makes even the synchronized common deletion basis automatic for every
child forest at \(n\ge4\).  The remaining central recursion row there is
only physical side-forest realization.

## 1. Ordered residuals

Let

\[
 \mathcal H\subseteq
 A\times B\times C\times D
\]

be a four-partite four-uniform hypergraph.  The outer shores are \(A,B\);
the middle tail/head shores are \(C,D\).  An **outer-perfect matching** is a
hypergraph matching saturating every vertex of \(A\cup B\).  When

\[
 |A|=|B|=n,\qquad |C|=|D|=n+K,
\tag{1.1}
\]

it uses exactly \(n\) atoms and leaves exactly \(K\) vertices unused in
each middle role.

For the Boolean ordered-diamond system, an atom is
\((L,U,T,H)\), where \(L=T\cap H\), \(U=T\cup H\), and \(T,H\) are
ordered.  The abstract obstruction below is not claimed to embed in that
geometric subhypergraph.  It proves that the advertised degree, codegree,
part-size, and surplus data are logically insufficient.

## 2. A sharp-scale space obstruction

Choose integers \(r,q\to\infty\), and choose a prime

\[
                         6r<s<12r.
\]

Such a prime exists by Bertrand's theorem.  All arithmetic in the base
construction is in \(\mathbb Z_s\).

### 2.1 Base AP components

A **regular AP component** has all four parts equal to \(\mathbb Z_s\).
For

\[
 x\in\mathbb Z_s,\qquad 0\le t<r,
\]

include

\[
                         (x,x+t,x+2t,x+3t).
\tag{2.1}
\]

Every vertex has degree \(r\), and every pair of vertices from different
parts lies in at most one edge.

A **\(P\)-doubled AP component**, where \(P\) is one of the four parts, has

\[
 P=\{0,1\}\times\mathbb Z_s
\]

and each other part equal to \(\mathbb Z_s\).  For

\[
 j\in\{0,1\},\quad 0\le t<r,\quad u=jr+t,\quad
 x\in\mathbb Z_s,
\]

include the AP edge

\[
                         (x,x+u,x+2u,x+3u),
\tag{2.2}
\]

tagging the coordinate in part \(P\) by \(j\).

### Lemma 2.1 (base degrees and codegrees)

In a \(P\)-doubled component, every doubled-part vertex has degree \(r\),
every other vertex has degree \(2r\), and every pair-codegree is at most
one.

#### Proof

Fixing a coordinate value and \(j,t\) determines \(x\), giving the degree
counts.  Given values in two positions, their difference determines
\((\ell-k)u\), where \(1\le\ell-k\le3\).  Since \(s>6r\) is prime and
\(0\le u<2r\), this determines \(u\), then \(j,t,x\), uniquely.  A tag can
only reduce the number of possibilities.  \(\square\)

### 2.2 Additive clone blow-up

Replace every base vertex \(v\) by clones

\[
                         (v,z),\qquad z\in\mathbb Z_q.
\]

Replace every base edge by all \(q^3\) clone edges satisfying

\[
                         z_A+z_B+z_C+z_D=0
                         \pmod q.
\tag{2.3}
\]

### Lemma 2.2 (blown-up parameters)

Every cloned degree is \(rq^2\) or \(2rq^2\), and the maximum pair-codegree
is \(q\).

#### Proof

After fixing one clone coordinate, choose two of the remaining clone
coordinates freely and solve for the last, giving \(q^2\) lifts of every
incident base edge.  After fixing two clone coordinates, choose one freely
and solve for the last, giving \(q\) lifts.  Lemma 2.1 says that at most one
base edge contains a given cross-part pair.  Some compatible pair attains
the value \(q\).  \(\square\)

### 2.3 Global part sizes

Take the disjoint union of:

* one \(A\)-doubled component;
* one \(B\)-doubled component;
* two \(C\)-doubled components;
* two \(D\)-doubled components; and
* \(R\) regular AP components.

After clone blow-up, the part sizes are

\[
 |A|=|B|=(R+7)sq,\qquad
 |C|=|D|=(R+8)sq.
\tag{2.4}
\]

The middle surplus and its relative size are

\[
 K_0=sq,\qquad
 \frac{K_0}{|A|}=\frac1{R+7}.
\tag{2.5}
\]

The \(A\)-doubled component contains \(2sq\) vertices of \(A\) and only
\(sq\) vertices of \(B\).  Since there are no cross-component edges, every
matching misses at least \(sq\) vertices of that \(A\)-block.  The
\(B\)-doubled component gives the dual deficit.

### Theorem 2.3 (sharp logarithmic-degree obstruction)

There is an infinite family with

\[
\begin{aligned}
 |A|=|B|&=n,\\
 |C|=|D|&=n+\Theta(nm^{-2/3}),\\
 \deg(v)&=\Theta(m),\\
 \Delta_2&=\Theta(m^{1/3}),
\end{aligned}
\tag{2.6}
\]

but no outer-perfect matching.  Every matching leaves at least
\(\Theta(nm^{-2/3})\) vertices on each outer shore.

#### Proof

Take

\[
 r,q=\Theta(m^{1/3}),\qquad R=\Theta(m^{2/3}).
\]

Then Lemma 2.2 gives degree \(\Theta(rq^2)=\Theta(m)\) and
\(\Delta_2=q=\Theta(m^{1/3})\).  Equations (2.4)--(2.5) give the required
surplus ratio.  The doubled-component Hall cuts give outer deficiency at
least \(sq=n/(R+7)=\Theta(nm^{-2/3})\).

One base union has outer size \(n_0=(R+7)sq=\Theta(m^{4/3})\).  Take

\[
 L=\left\lfloor\frac{Nm^{-1/3}}{n_0}\right\rfloor
\]

disjoint copies.  Then \(L\to\infty\) and
\(n=Ln_0=(1+o(1))Nm^{-1/3}\).  This changes neither local parameters nor
ratios, while \(\log n=\Theta(m)\).  \(\square\)

The obstruction is scale-sharp for the proposed Catalan reserve:

\[
 nm^{-2/3}
 =Nm^{-1/3}m^{-2/3}
 =N/m
 =K.
\tag{2.7}
\]

Thus every viable deterministic hypothesis must exclude Hall concentration
down to the Catalan scale.

This obstruction is complementary to the previously proved hidden-middle
space barrier in
`MATH_THEOREM_CATALAN_LOG_RESIDUAL_OUTER_HALL_AND_SPACE_BARRIER_20260731.md`.
That example preserves a perfectly matchable outer projection and obstructs
one middle capacity row.  The present deterministic example instead
calibrates an explicit outer Hall loss of the full Catalan order under the
advertised degree, codegree, and surplus scales; its outer projection is
deliberately disconnected.

## 3. A regular parity obstruction

Let \(g\) be even and let every part be \(\mathbb Z_g\).  For every
\(\ell,u\in\mathbb Z_g\), include

\[
             (\ell,u,\ell+u,\ell+2u).
\tag{3.1}
\]

Every vertex has degree \(g\).  Every pair-codegree is at most two: all
cross-part pairs determine \(\ell,u\) uniquely except \((\ell,h)\), for
which \(2u=h-\ell\) has at most two solutions.

### Proposition 3.1 (fractional feasibility is not integrality)

The uniform weight \(1/g\) on every edge is a fractional perfect matching,
but the hypergraph has no perfect matching.

#### Proof

Uniformity gives load one at every vertex.  Suppose a perfect matching
exists.  Its \(\ell\)-, \(u\)-, and \(t=\ell+u\)-coordinates are each a
permutation of \(\mathbb Z_g\).  Summing modulo \(g\),

\[
 \sum t=\sum\ell+\sum u=2\sum_{x\in\mathbb Z_g}x=0,
\]

whereas

\[
 \sum_{x\in\mathbb Z_g}x=g/2\ne0\pmod g.
\]

This contradiction proves the claim.  \(\square\)

Thus even exact regularity, constant codegree, and a uniform fractional
perfect matching do not remove the integral correlation gate.

### Boolean-native outer cut

Fix one coordinate \(z\) and retain only Boolean diamonds with
\(z\notin U\setminus L\).  The outer projection splits according to whether
\(z\) belongs to both outer endpoints.  In the \(z\)-absent component,

\[
 |\mathcal L_0|=\binom{2m-1}{m-1},\qquad
 |\mathcal U_0|=\binom{2m-1}{m+1}
 =\frac{m-1}{m+1}|\mathcal L_0|.
\tag{3.2}
\]

Hence outer Hall fails.  The oriented degrees are nevertheless

\[
\begin{array}{c|cc}
&z\text{-absent}&z\text{-present}\\ \hline
\mathcal L&m(m-1)&m(m+1)\\
\mathcal U&m(m+1)&m(m-1).
\end{array}
\tag{3.3}
\]

This is an exact Boolean obstruction to replacing outer expansion by
asymptotically equal degrees.  No claim is made that a deterministic
\(p=m^{-1/3}\) thinning of this example preserves every local statistic.

## 4. Matching-aligned independent-boundary absorbers

Let \(M\) be a four-partite matching.  An absorber
\(\mathcal A=(P^-,P^+)\) for an endpoint pair \((a,b)\in A\times B\) is
**\(M\)-ready** when:

1. \(P^-\subseteq M\);
2. \(a,b\) are uncovered by \(M\);
3. \((M\setminus P^-)\cup P^+\) is a four-partite matching;
4. its outer coverage is the outer coverage of \(M\), together with
   precisely \(a,b\); and
5. no atom of \(M\setminus P^-\) uses any resource in the full two-state
   support of the absorber.

Two ready absorbers are **independent** when their complete outer supports
(endpoints included) and their complete two-state middle-resource supports
are pairwise disjoint.

### Lemma 4.1 (simultaneous toggling)

For any independent family \(\mathscr A\) of ready absorbers,

\[
 M'=
 \left(M\setminus\bigcup_{\mathcal A\in\mathscr A}P^-_{\mathcal A}\right)
 \cup
 \bigcup_{\mathcal A\in\mathscr A}P^+_{\mathcal A}
\tag{4.1}
\]

is a four-partite matching and adds exactly the advertised endpoint pairs.

If the physical lift of \(M\) is a forest, every inserted \(P^+\) state is
itself a physical forest, and every inserted physical edge is isolated
from the retained lift and from the other inserted supports, then the lift
of \(M'\) is also a forest.  The explicit independent-boundary state has
pairwise-distinct physical endpoints, so it satisfies the internal-forest
condition.

#### Proof

Readiness makes each individual replacement legal.  Independence makes
all deletions and additions commute and prevents cross-absorber resource
collisions.  The endpoint pairs are disjoint, so their cover gains add.

Under the stronger forest hypothesis, deleting the off states leaves a
forest, and the inserted physical edges form disjoint forest pieces
attached to no retained middle vertex.  Their union is a forest.
\(\square\)

The condition \(P^-\subseteq M\) is essential.  Survival of all corridor
resources does not by itself make the gadget augmenting.  The residual
construction must either preinstall an off-state bank or output an almost
matching whose alternating structure contains the required off states.

## 5. Exact deterministic corridor-pressure theorem

Suppose \(M\) leaves defect sets

\[
                         D_A\subseteq A,\qquad
                         D_B\subseteq B,\qquad
                         |D_A|=|D_B|=h.
\tag{5.1}
\]

Let \(P_M\) be a bipartite endpoint graph on \(D_A,D_B\).  An edge means
that the endpoint pair has at least one \(M\)-ready independent-boundary
absorber.  Assume \(P_M\) has a perfect matching

\[
                         J=\{e_1,\ldots,e_h\}.
\tag{5.2}
\]

For each demand \(e_i\), let \(\mathcal S_i\) be a nonempty family of
\(M\)-ready absorbers.  The support of a candidate includes both its off and
on states and all outer and middle resources.

### Theorem 5.1 (pointwise collision pressure)

Suppose the demands are ordered so that, for all \(j<i\) and every
\(\mathcal A\in\mathcal S_j\),

\[
 \left|
 \{\mathcal B\in\mathcal S_i:
      \operatorname{supp}\mathcal A
      \cap\operatorname{supp}\mathcal B\ne\varnothing\}
 \right|
 \le\eta_{j,i}|\mathcal S_i|,
\tag{5.3}
\]

and

\[
                         \sum_{j<i}\eta_{j,i}<1
 \qquad(1\le i\le h).
\tag{5.4}
\]

Then \(\mathcal H\) has an outer-perfect matching.

#### Proof

Choose a candidate for each demand in order.  Previously selected
candidates forbid at most

\[
 |\mathcal S_i|\sum_{j<i}\eta_{j,i}<|\mathcal S_i|
\]

candidates in the next list, so one remains.  The final candidates have
pairwise disjoint full supports.  Lemma 4.1 toggles them simultaneously and
covers \(D_A\cup D_B\).  \(\square\)

For \(h\ge2\), in the symmetric case it is enough that every selected
candidate conflicts with less than a \(1/(h-1)\) fraction of every other
list.  The case \(h=1\) needs only a nonempty list.

### Theorem 5.2 (probabilistic collision pressure)

Give every \(\mathcal S_i\) a probability measure \(\mu_i\).  If \(h=1\),
a candidate exists by nonemptiness.  Suppose henceforth that \(h\ge2\) and
for all \(i<j\),

\[
 \Pr_{\mathcal A\sim\mu_i,\mathcal B\sim\mu_j}
 [\operatorname{supp}\mathcal A
  \cap\operatorname{supp}\mathcal B\ne\varnothing]
 \le\chi,
\tag{5.5}
\]

and

\[
                         e\chi(2h-3)\le1.
\tag{5.6}
\]

Then \(\mathcal H\) has an outer-perfect matching.

#### Proof

Choose the \(h\) candidates independently.  For every pair \(i<j\), let
\(E_{ij}\) be the collision event.  It has probability at most \(\chi\)
and is independent of every event whose index pair is disjoint from
\(\{i,j\}\).  Its dependency degree is at most \(2h-4\).  The symmetric
local lemma, in the form \(ep(d+1)\le1\), gives a choice with no collision.
Apply Lemma 4.1.  \(\square\)

These are deterministic pseudorandom hypotheses on complete physical
corridor lists.  They do not follow from vertex degrees or pair-codegrees
of the residual atom hypergraph.

### Corollary 5.3 (checkable list--resource pressure)

Suppose \(h\ge2\) and every candidate support has at most \(b\) resources.
Write

\[
 \mathcal U_i
 =\bigcup_{\mathcal A\in\mathcal S_i}
          \operatorname{supp}\mathcal A
\tag{5.7}
\]

and, for \(i\ne j\), define the directional **cross-list pressure**

\[
 \lambda_{j\leftarrow i}
 =\max_{x\in\mathcal U_i}
   \mu_j\{\mathcal B:x\in\operatorname{supp}\mathcal B\}.
\tag{5.8}
\]

Then the pair-collision probability in (5.5) is at most

\[
 \min\{b\lambda_{j\leftarrow i},
       b\lambda_{i\leftarrow j}\}.
\tag{5.9}
\]

Consequently, if \(\lambda_{j\leftarrow i}\le\lambda\) for every distinct
\(i,j\), the sufficient
condition

\[
                         eb\lambda(2h-3)\le1
\tag{5.10}
\]

implies an outer-perfect matching.  For uniform lists this is the fully
deterministic incidence condition

\[
 \max_{i\ne j}\max_{x\in\mathcal U_i}
 \frac{|\{\mathcal B\in\mathcal S_j:
                    x\in\operatorname{supp}\mathcal B\}|}
      {|\mathcal S_j|}
 \le \frac1{eb(2h-3)}.
\tag{5.11}
\]

#### Proof

Condition on a candidate from list \(i\).  Every one of its at most \(b\)
resources lies in \(\mathcal U_i\), so a union bound gives collision
probability at most \(b\lambda_{j\leftarrow i}\).  Reversing \(i,j\) gives
the other bound in (5.9).  Averaging and Theorem 5.2 prove the result.
\(\square\)

At the target scales \(b=\Theta(m)\) and \(h=\Theta(n/m)\), (5.10)
requires cross-list pressure \(\lambda=O(1/n)\).  Equivalently, for uniform
lists of size \(L\), if a resource occurs in at most \(\Lambda\) candidates
of any other list, the sufficient quantitative requirement is

\[
                         L\ge eb(2h-3)\Lambda=\Theta(n\Lambda).
\tag{5.12}
\]

This is the exact dispersion target for a Boolean corridor atlas; raw
schedule count without cross-list dispersion is irrelevant.

### Endpoint Hall

Exact Hall in \(P_M\) is the weakest endpoint condition.  A simple
sufficient degree test is

\[
 \delta(P_M|D_A)\ge\Delta(P_M|D_B)>0,
\tag{5.13}
\]

because for \(X\subseteq D_A\),

\[
 \delta_A|X|
 \le e(X,N(X))
 \le\Delta_B|N(X)|.
\]

In particular, every positive regular balanced endpoint graph has a
perfect matching.

## 6. Quantitative independent-boundary capacity

For the explicit independent-boundary absorber at outer distance at least
three, write \(R=d+1\le m\).  Its off and on states have

\[
                         |P^-|=R,\qquad |P^+|=R+1.
\tag{6.1}
\]

The proof exhibits a guaranteed common physical-middle core of size
\(2d-1=2R-3\).  Since the off and on states use \(2R\) and \(2R+2\)
physical middle vertices, respectively,

\[
 |V(P^-)\setminus V(P^+)|\le3,\qquad
 |V(P^+)\setminus V(P^-)|\le5.
\tag{6.2}
\]

These are worst-case bounds; extra cross-state coincidences can make them
strict.  The overlay of the two physical matchings is a union of alternating
paths and even cycles.  Bipartition each overlay component and orient every
edge from one class to the other.  This is the required **role-coherent
orientation**: a resource common to the two states has the same middle role
in both.  Under this orientation, each role has at most five newly introduced
resources.  Thus the role count below applies when the absorber bank and its
off states are oriented at installation time in this way.  For an already
oriented matching, same-role agreement on the state intersection is an
additional hypothesis.

### Corollary 6.1 (universal reserve count bounds)

The following are conservative worst-case scalar budgets under which raw
resource counts do not obstruct preinstalling \(h\) pairwise independent
distance-at-least-three absorbers; they do not themselves prove that a
packing exists:

\[
                         h(m+1)\le n
\tag{6.3}
\]

on each outer shore and

\[
                         5h\le K+h
\tag{6.4}
\]

on each middle role after a partial matching with \(h\) outer defects.

At \(p=m^{-1/3}\), (6.3) gives

\[
 h\le\frac{n}{m+1}
   =(1+o(1))Nm^{-4/3}
   =\Theta(n/\log n)
   =\Theta(Km^{-1/3}).
\tag{6.5}
\]

This automatically implies (6.4) for all large \(m\).  Hence within this
worst-case length-\(\Theta(m)\) bookkeeping, outer corridor support is the
tighter scalar budget.

More generally, if absorber \(i\) has \(R_i=|P_i^-|\), exact disjointness
requires

\[
                         \sum_{i=1}^h(R_i+1)\le n
\tag{6.6}
\]

on each outer shore.  Thus, writing

\[
 \overline S=\frac1h\sum_{i=1}^h(R_i+1)
\]

for the average full outer-support size, one needs

\[
                         h\overline S\le n.
\tag{6.7}
\]

Absorbing a Catalan-size leave \(h=\Theta(K)\) therefore requires

\[
                         \overline S=O(n/K)=O(m^{2/3}).
\tag{6.8}
\]

Generic distance-\(\Theta(m)\) corridors cannot do this.

### Far endpoint pairing

For fixed \(L\), the number of upper endpoints at distance below three is

\[
 D_{<3}
 =\sum_{s=0}^{2}
   \binom{m-1}{s}\binom{m+1}{s+2}
 =\Theta(m^6).
\tag{6.9}
\]

If \(h\ge2D_{<3}\), the allowed distance-at-least-three graph on any two
balanced defect sets has minimum degree at least \(h/2\), and hence a
perfect matching.

#### Proof

Every endpoint forbids at most \(D_{<3}\) partners.  For Hall, a set of at
most \(h/2\) vertices has at least \(h/2\) neighbours.  If
\(|X|>h/2\) but \(|N(X)|<|X|\), a vertex outside \(N(X)\) has degree at
most \(h-|X|<h/2\), contradicting the minimum degree.  \(\square\)

Thus the distance-only outer pairing is automatic at any exponential leave
scale.  Ordered boundary-role survival, off-state alignment, and packing the
complete \(M\)-aligned corridors remain separate gates.

## 7. Cycle elimination is a separate row

Let an outer-perfect ordered matching use \(n\) directed physical edges on
a common middle ground of \(n+K\) vertices.  Tail and head injectivity give
indegree and outdegree at most one.  Its components are directed paths,
directed cycles, and isolated vertices.

The common-ground hypothesis is substantive.  It holds after recombination
on the full Boolean middle layer, or for a coupled residual using the same
physical label set in both roles.  It is not automatic for two independently
thinned copies of the tail and head shores.

### Lemma 7.1 (path-component identity)

The number of path components, counting isolated vertices, is exactly
\(K\), independent of the number of directed cycle components.

#### Proof

If there are \(p\) path components and any number of cycles, then

\[
 |V|-|E|=p.
\]

Here \(|V|=n+K\) and \(|E|=n\).  \(\square\)

Therefore middle surplus does not forbid cycles.

Let \(F\) be the physical lift on the full common middle ground, isolated
vertices included.  Let \(A\) be an outer-palette set of selected edges
containing every cycle edge to be replaced, and let

\[
                         F_0=F-A
\]

be a forest.  Let \(B\) be an unselected replacement with exactly the same
lower and upper colour multisets as \(A\).

### Theorem 7.2 (exact contraction-forest test)

The replacement

\[
                         F'=F_0\cup B
\]

is a linear forest if and only if:

1. every physical vertex has degree at most two in \(F'\); and
2. after contracting every component of \(F_0\), the multigraph induced by
   \(B\) is loopless and acyclic, with parallel edges counted as a
   two-cycle.

#### Proof

The degree condition is necessary.  A loop after contraction is a new edge
whose endpoints lie in one tree of \(F_0\), and therefore creates a cycle.
A cycle, including a parallel two-cycle, in the contracted multigraph
expands through the unique paths in the corresponding trees to a cycle in
\(F'\).

Conversely, any cycle in \(F'\) contracts to a loop or cycle in the
multigraph induced by \(B\), since \(F_0\) is a forest.  Thus condition 2
is equivalent to acyclicity once condition 1 is imposed.  \(\square\)

Theorem 7.2 is an exact undirected audit for a supplied palette-neutral
cycle packet.  If every Boolean diamond is available in both physical
orientations, each resulting path can then be oriented consistently, giving
tail/head injectivity.  If orientations are fixed in advance, directed-role
feasibility is an additional check.  The theorem does not prove that such a
packet exists in every residual.

## 8. Deterministic balanced-reserve fractional rebase

Write

\[
 N_j=\binom{2j}{j-1},\qquad M_j=\binom{2j}{j},\qquad
 K_j=M_j-N_j=\operatorname{Cat}_j.
\tag{8.1}
\]

Fix a balanced \(a\)-set on \(2a\) collar coordinates and let
\(r=m-a\).  Let \(\mathcal R\) be the induced parameter-\(r\) child reserve,
and let \(\mathcal H^\circ\) consist of all ambient ordered diamonds using
no lower, upper, tail, or head resource of \(\mathcal R\).  Its part sizes
are

\[
 |A^\circ|=|B^\circ|=N^\circ:=N_m-N_r,\qquad
 |C^\circ|=|D^\circ|=M_m-M_r=N^\circ+K^\circ,
\tag{8.2}
\]

where

\[
                         K^\circ=K_m-K_r.
\tag{8.3}
\]

### Theorem 8.1 (balanced-reserve relative interior)

Assume \(a\ge3\) and \(r=m-a\ge2\).  There is an explicit weighting
\(x^\circ\) of \(\mathcal H^\circ\) such that every complement lower and
upper resource has load one and every complement middle resource in either
role has load at most \(1-\sigma_{m,a}\), where

\[
 \sigma_{m,a}
 =\min\left\{
   \frac{r-1}{r(m+1)},
   \frac1m-\frac2{a(m+1)},
   \frac1{m+1}-\frac2{am(m+1)}
 \right\}>0.
\tag{8.4}
\]

Moreover every atom \(e\in\mathcal H^\circ\) has

\[
 x_e^\circ\ge
 \frac{\varepsilon_{m,a}}{m(m+1)},
\tag{8.5}
\]

where

\[
 \varepsilon_{m,a}
 =\min\left\{
  1-\frac{m}{a(a-1)r},
  1-\frac1{\binom a2\binom{r+1}2}
 \right\}>0.
\tag{8.6}
\]

For

\[
                         a=(1/6+o(1))\log_2m,
\]

these margins are

\[
 \varepsilon_{m,a}=1-O(a^{-2}),
 \qquad
 \sigma_{m,a}=(1-o(1))/m.
\tag{8.7}
\]

#### Proof

Start with weight \(w_0=1/[m(m+1)]\) on every reserve-avoiding atom and
apply the two signed path families (5.1) and (5.3) of the balanced-subcube
theorem.  Its Theorem 5.1 proves exact outer loads and middle loads at most
one.

It remains to retain the quantitative margins.  A negative atom of family
(5.1) lies in exactly \(r\) paths.  Its loss per orientation is

\[
 \frac{r\alpha_1}{2}
 =w_0\frac{m}{a(a-1)r}.
\tag{8.8}
\]

A negative atom of family (5.3) lies in one path and loses

\[
 \frac{\alpha_2}{2}
 =\frac{w_0}{\binom a2\binom{r+1}2}.
\tag{8.9}
\]

The two negative trace types are disjoint, and positive corrections can
only raise an atom weight.  Equations (8.5)--(8.6) follow.  Positivity is
strict already at \((a,r)=(3,1)\), hence throughout the stated range.

For middle resources, type \((1,0)\) has final slack

\[
 \frac2{m+1}-\frac{r+1}{(m+1)r}
 =\frac{r-1}{r(m+1)}.
\tag{8.10}
\]

Type \((1,1)\) has slack

\[
                         \frac1m-\frac2{a(m+1)}.
\tag{8.11}
\]

The positive family-(5.3) types \((2,1)\) and \((1,2)\) retain at least

\[
                         \frac1{m+1}-\frac2{am(m+1)};
\tag{8.12}
\]

the family-(5.1) correction on type \((2,1)\) is negative and only helps.
Every other type retains at least the uncorrected slack \(1/(m+1)\) or
receives only a negative correction.  This proves (8.4).  The asymptotics
in (8.7) are immediate from \(r=m-a\).  \(\square\)

### Proposition 8.2 (literal bounded-port augmentor flow)

Every signed three-edge path used in Theorem 8.1 is a reserve-avoiding
literal \(1\to2\) outer augmentor: its negative diamond is an off state,
its two positive diamonds form a four-resource matching, the internal
outer vertices are retained, and precisely its two path endpoints are
added.  Averaging over physical orientation choices expresses the
fractional correction as a rational superposition of such constant-size
augmentors.

#### Proof

In either displayed path \(L_0,U_0,L_1,U_1\), the off state is
\(\{L_1U_0\}\) and the on state is
\(\{L_0U_0,L_1U_1\}\).  The trace formulas show that every resource avoids
the child reserve.  Within the on state the four physical middle resources
are distinct: in family (5.1) they are separated by the missing/extra
collar labels and by \(X\ne Y\); in family (5.3) the two positive diamonds
have respective trace types \((2,1)\) and \((1,2)\).  Thus every choice of
orientations for the off diamond and the two on diamonds gives valid states.
Give each of the eight orientation triples coefficient \(\alpha/8\).  Each
of the two orientations of each signed diamond then has marginal
coefficient \(\alpha/2\), exactly the correction in Theorem 8.1.  The outer
coverage identity is literal.  \(\square\)

This proposition proves statewise legality, not automatic \(M\)-readiness.
In family (5.1) the two states share a physical middle label; installation
in an ordered matching must keep its role aligned (or reserve both role
copies) and isolate the complete two-state support.  Different ears must
still be selected resource-disjointly.

### Corollary 8.3 (what the deterministic state discharges)

The weighting \(x^\circ\) is a full-support relative-interior point of the
outer-perfect fractional polytope of \(\mathcal H^\circ\).  Its projection

\[
                         y_{LU}=\sum_{T,H}x^\circ_{LUTH}
\]

is doubly stochastic, so the complement lower--upper projection satisfies
Hall and has an integral perfect matching.  Combining \(x^\circ\) with the
child uniform fractional matching gives an outer-perfect fractional state
of the full parameter-\(m\) system with no atom crossing the child boundary.

This proves fractional four-resource capacity and excludes every Farkas
space barrier on the separated deterministic face.  It does not prove an
integral four-resource matching: the rational augmentor superposition need
not have a disjoint integral realization, its negative atoms need not lie
in one common matching, and clearing denominators need not remove lattice
torsion.

If an integral outer-perfect complement matching exists, it uses
\(N^\circ\) atoms and leaves exactly \(K^\circ\) middle resources in each
role.  Together with a child matching its total leave is

\[
                         K^\circ+K_r=K_m.
\tag{8.13}
\]

### Theorem 8.4 (two-coordinate synchronized incidence is automatic)

Let \(F\) be any parameter-\(n\) Catalan linear matching with \(n\ge4\),
with every physical path oriented consistently.  In the exact two-
coordinate recursion of Theorem 6.1 in the balanced-subcube note, there is
a single child-atom bank

\[
                         Q\subseteq F,\qquad
 |Q|=\operatorname{Cat}_{n+1},
\tag{8.14}
\]

whose tail complement is a basis of the upper two-step transversal matroid
and whose head complement is a basis of the lower one.  Hence both diagonal
containment matchings exist simultaneously.

Moreover there is a probability distribution on such common banks with
exact marginal

\[
 \Pr(q\in Q)
 =\frac{\operatorname{Cat}_{n+1}}{\binom{2n}{n-1}}
 \qquad(q\in F).
\tag{8.15}
\]

Thus some common bank pays at most this uniform-density fraction of every
nonnegative additive edge-risk cost.  The only remaining two-coordinate
gate is to choose its diagonal representatives so that the two punctured
side graphs and their seam attachments form one linear forest.

#### Proof

Put

\[
 X=\binom{[2n]}n,\quad N=|F|=\binom{2n}{n-1},\quad
 C=\operatorname{Cat}_{n+1}.
\]

The dual-rank theorem in
`MATH_THEOREM_CATALAN_TWO_COORDINATE_COMMON_BASIS_AUTOMATIC_20260731.md`
states that either dual two-step transversal matroid \(T^*\) satisfies

\[
                         r_{T^*}(A)\ge(C/N)|A|
 \qquad(|A|\le N).
\tag{8.16}
\]

Pull the upper dual back through the injective tail map of \(F\), and the
lower dual back through its injective head map.  For every \(S\subseteq F\),
their rank sum on \(S,F-S\) is at least

\[
                         (C/N)|S|+(C/N)(N-|S|)=C.
\]

Edmonds' matroid-intersection theorem gives a common \(C\)-basis \(Q\).
Taking complements converts the two dual bases into the required primal
saturating matchings.

The constant vector \(x_q=C/N\) lies in both pullback base polytopes by
(8.16).  Integrality of the two-matroid intersection polytope decomposes it
into common bases, proving (8.15) and the additive-cost conclusion.
\(\square\)

### Scope relative to the logarithmic residual

The complement \(\mathcal H^\circ\) has \(\Theta(N_m)\) outer vertices and
dense degree.  Theorem 8.1 therefore does **not** prove robust capacity for
an arbitrary degree-\(\Theta(m)\), \(p=m^{-1/3}\) thinning.  It replaces
that route by a deterministic recursive reserve plus an explicitly
fractional-complete complement.  Recovering the sparse route would still
require a capacity-preserving thinning theorem.

## 9. Exact remaining integral theorem

For an arbitrary sparse residual, the following deterministic statement
would close the outer matching problem:

> **Absorber-aware logarithmic residual theorem.**  The Boolean residual at
> \(p=m^{-1/3}\) contains a partial matching \(M\) which either preinstalls,
> or already contains, off states for a corridor bank; its balanced leave
> satisfies \(h=O(n/m)\); its far endpoint graph satisfies Hall; and its
> complete \(M\)-ready corridor lists satisfy (5.4) or (5.6).

Theorems 5.1--5.2 would then give an outer-perfect matching.  A
palette-neutral replacement passing Theorem 7.2 would give the required
linear forest.

The construction must couple the core matching to the off-state bank.
A generic almost-perfect matching followed by an independent absorber
search does not meet the quantifiers.  The explicit obstruction of Section
2 shows that degree, codegree, and middle surplus alone can leave a
Catalan-size Hall defect, which is larger than the universal long-corridor
capacity by a factor \(m^{1/3}\).

For the deterministic balanced-reserve route, the fractional clause is no
longer a hypothesis.  The exact remaining theorem is instead:

> **Integral balanced-collar theorem.**  Round \(x^\circ\) to a partial
> matching \(M\) with balanced leave and with the off states of a
> reserve-avoiding augmentor bank already contained in \(M\).  The endpoint
> graph must satisfy Hall, and the complete ready lists must satisfy (5.4)
> or (5.6).  After toggling, the physical lift must pass Lemma 4.1 or the
> contraction test of Theorem 7.2.

In the two-coordinate specialization at \(n\ge4\), Theorem 8.4 removes both
the separate endpoint-Hall checks and the synchronized common-deletion-
basis condition.  Only the physical punctured-side degree, anchor, and
contracted-forest rows remain.  This simplification does not apply to an
arbitrary sparse residual leave.

The special collar ears of Proposition 8.2 have constant support and should
be used before the length-\(\Theta(m)\) independent-boundary corridors.  If
rounding leaves

\[
 h=O(\Delta_{\rm collar}),
 \qquad
 \Delta_{\rm collar}
 =\Theta\!\left(K_m\frac{\log m}{m^{1/3}}\right),
\tag{9.1}
\]

then even the conservative long-corridor count checks are automatic:

\[
 h(m+1)=o(N^\circ),
 \qquad
 5h=o(K^\circ).
\tag{9.2}
\]

What remains is integral correlation: off-state alignment, lattice
generation, disjoint selection, and topology.  No such rounding is proved
here.
