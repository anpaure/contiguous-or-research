# Algebraic calibrated packet orbits: exact constraints, an owner near-transversal, and the cyclic-bundling gate

Date: 2026-07-25

Method: pure mathematics only.  No computation, solver, or web input is
used.

## 0. Verdict

This algebraic route does **not** yet prove the calibrated packet theorem or
the coefficient-one contiguous-OR theorem.  It does, however, settle the
unbundled owner-capacity marginal and the elementary orbit obstructions
exactly.

The proved conclusions are these.

1. A union of whole group orbits having exactly one packet above every top
   is necessarily an equivariant section.  The packet stabilizer must equal
   the top stabilizer, and every target load is governed by an exact
   stabilizer quotient.
2. For the regular cyclic group in every dimension, and for
   \(\operatorname {AGL}(1,2^a)\) when \(2m=2^a\), all but
   \(2^{m+o(m)}\) central masks are strongly aperiodic throughout the
   calibrated band.
3. After deleting that exponentially negligible sector, Hall's theorem on
   the group quotient gives an exact equivariant assignment of \(M\)
   distinct owners to every retained top.  Its lift uses
   \(W-o(W)\) distinct physical owners.  Thus the algebraic owner
   near-transversal exists nonrandomly and integrally.
4. A top-order construction obtained by restricting only
   \(K=\exp(o(H))\) ambient cyclic orders cannot work: it supports only an
   \(o(1)\) fraction of every fixed Gaussian-window row.  In particular,
   finitely, polynomially, or quasipolynomially many affine images of
   ambient templates are ruled out.
5. On the strongly aperiodic quotient, same-rank packet codegrees are not
   enlarged by orbit aggregation.  In fact, at most one group alignment can
   contribute.  This prevents new orbit collisions, but it also shows that
   quotienting does not improve the ambient \(\Theta(1/m)\) nested
   owner--facet correlation.

The exact unproved gate is a **top-intrinsic quotient cyclic-bundling
theorem**.  The Hall owners assigned to one top are arbitrary containment
neighbours.  They need not be consecutive windows of any cyclic order.

## 1. Calibrated notation

Put

\[
 v=2m,\qquad W=\binom{2m}{m},\qquad
 N_h=\binom{2m}{m-h},\qquad \lambda_h=\frac{W}{N_h}.
\tag{1.1}
\]

Let \(H\) be the least positive integer such that

\[
 \lambda_H\ge m+H,
\tag{1.2}
\]

and put

\[
 M=m+H,\qquad N=N_H=\binom{2m}{M}.
\tag{1.3}
\]

The standard calibrated estimates are

\[
 H=(1+o(1))\sqrt{m\log m},\qquad
 MN=W-o(W),\qquad N=O(W/m).
\tag{1.4}
\]

For completeness, the ratio identity

\[
 \frac{\lambda_h}{\lambda_{h-1}}
 =\frac{m+h}{m-h+1}
\tag{1.5}
\]

and Taylor expansion give, uniformly for \(h=o(m^{2/3})\),

\[
 \log\lambda_h
 =\frac{h^2}{m}+O\left(\frac hm+\frac{h^3}{m^2}\right).
\tag{1.6}
\]

Minimality in (1.2), followed by (1.5), gives

\[
 M\le\lambda_H
 <(M-1)\frac{m+H}{m-H+1}
 =M\left(1+O(H/m)\right).
\tag{1.7}
\]

Equations (1.4) follow from (1.6)--(1.7).

A **top** is an \(M\)-set \(U\).  A directed packet over \(U\) is a
directed cyclic order \(C\) of its coordinates, considered modulo cyclic
rotation.  It exposes the \(M\) cyclic \(k\)-intervals at every proper
rank \(1\le k<M\).  Its rank-\(m\) intervals are called its owners.

## 2. The exact orbit ledger

Let a finite group \(G\le\operatorname {Sym}(\Omega)\) act on the ground
coordinates.  A decorated packet

\[
 P=(U,C,(J_k)_k)
\]

consists of a top, a directed cyclic order, and optional sets \(J_k\) of
claimed cyclic starts.  Write \(G_U,G_P,G_S\) for the setwise stabilizers
of a top, a decorated packet, and a target set.

All loads below use one fixed incidence convention.  Proper-rank interval
occurrences are counted by their claimed starts.  At rank \(M\), the \(M\)
identical intervals are collapsed to the single top tag; if instead one
keeps multiplicity, that multiplicity must be included in
\(a_{\cal O}(P)\).

### Theorem 2.1 (top multiplicity and target load)

The full packet orbit \(GP\) contributes exactly

\[
 \boxed{\frac{|G_U|}{|G_P|}}
\tag{2.1}
\]

packet columns above each top in \(GU\).

Fix a target orbit \({\cal O}=GS\), and let \(a_{\cal O}(P)\) be the
number of claimed targets of \(P\) which lie in \({\cal O}\).  Every
target in \({\cal O}\) receives the same load, namely

\[
 \boxed{
 \mu_{\cal O}(P)
 =a_{\cal O}(P)\frac{|G_S|}{|G_P|}.}
\tag{2.2}
\]

In particular,

\[
 |G_P|\mid a_{\cal O}(P)|G_S|.
\tag{2.3}
\]

#### Proof

The packet orbit and top orbit have respective sizes

\[
 |GP|=\frac{|G|}{|G_P|},\qquad
 |GU|=\frac{|G|}{|G_U|}.
\]

Equivariance makes the number of columns over each top constant, and their
ratio is (2.1).

There are \(|G|a_{\cal O}(P)/|G_P|\) target occurrences from
\({\cal O}\) in the full packet orbit.  Equivariance distributes them
uniformly over the \(|G|/|G_S|\) members of \({\cal O}\), proving
(2.2).  Since this is an actual integer load, (2.3) follows. \(\square\)

### Corollary 2.2 (unit top load forces an equivariant section)

Suppose a nonnegative integral union of whole packet orbits has top load
exactly one.  Above every top orbit it chooses exactly one packet orbit,
and that orbit satisfies

\[
 \boxed{G_P=G_U.}
\tag{2.4}
\]

#### Proof

Every selected packet orbit above \(GU\) contributes the positive integer
\(|G_U|/|G_P|\).  A sum of such integers can equal one only when there is
one term and it equals one. \(\square\)

Thus orbit averaging is not an integrality mechanism: rational orbit
weights, after clearing denominators, give several packets per top rather
than one literal packet.

### Proposition 2.3 (stabilizer criterion for a directed cyclic order)

Let \(G_U^U\) be the permutation group induced by \(G_U\) on \(U\), after
quotienting by the pointwise kernel.  A \(G_U\)-fixed directed cyclic order
of \(U\) exists if and only if \(G_U^U\) is cyclic and semiregular on
\(U\).

If its order is \(d\), every invariant phase subset has size divisible by
\(d\).  Conversely, when the phase subset itself is free to be chosen, one
of every prescribed size divisible by \(d\) exists.

#### Proof

The automorphism group of a directed \(M\)-cycle is its rotation group
\(C_M\).  Every subgroup is cyclic, and every nonidentity rotation is
fixed-point-free.  This proves necessity.

Conversely, let \(h\) generate a semiregular cyclic action of order
\(d\).  Choose one representative from each of its \(M/d\) point orbits.
List the representatives, then their images under \(h\), and continue
through \(h^{d-1}\).  In the resulting cyclic order, \(h\) is rotation by
\(M/d\) positions.  Its phase orbits all have size \(d\), proving the last
assertion. \(\square\)

For the affine actions used below, a transformation fixing two ground
points is the identity, so the pointwise kernel on a top is trivial.

## 3. Strong masks are exponentially generic

For two sets of the same size define Johnson distance by

\[
 d_J(S,T)=\frac12|S\triangle T|.
\tag{3.1}
\]

For \(D\ge0\), call \(S\) **\(D\)-strong** if

\[
 d_J(S,gS)>D\qquad(1\ne g\in G).
\tag{3.2}
\]

We use either of the following groups.

* \(G=C_v\), acting regularly by translation on \(\mathbb Z_v\).  This
  is available for every \(v=2m\).
* If \(v=2^a\), \(G=\operatorname {AGL}(1,v)\), acting on
  \(\mathbb F_v\).  Here \(|G|=v(v-1)\).

### Lemma 3.1 (cycle-transition bound)

If a permutation \(g\) of \(v\) points has \(c(g)\) cycles, then

\[
 \#\{S:d_J(S,gS)\le D\}
 \le 2^{c(g)}\sum_{j=0}^{2D}\binom vj.
\tag{3.3}
\]

#### Proof

Write the membership indicator of \(S\) around every permutation cycle of
\(g\).  The number of cycle edges across which this bit changes is exactly
\(|S\triangle gS|\), hence at most \(2D\).  Choose those transition edges,
then choose one initial bit on every cycle.  These choices determine the
whole indicator word.  Allowing inconsistent transition choices only
increases the count, giving (3.3). \(\square\)

### Lemma 3.2 (half-cycle property)

Every nonidentity element of either group above has at most
\((v+1)/2\) permutation cycles.

#### Proof

A nonzero translation of \(\mathbb Z_v\) has
\(\gcd(v,t)\le v/2\) cycles.

For \(\operatorname {AGL}(1,2^a)\), a nonzero translation is a product of
\(v/2\) transpositions.  A map \(x\mapsto ax+b\) with \(a\ne1\) has one
fixed point and is conjugate to multiplication by \(a\) on the remaining
points.  Since \(v-1\) is odd, the multiplicative order of \(a\ne1\) is
at least three.  It therefore has at most
\(1+(v-1)/3<(v+1)/2\) cycles. \(\square\)

### Corollary 3.3 (exceptional-set estimate)

Uniformly for \(D=O(H)\), at every calibrated rank
\(|k-m|\le H\),

\[
 \boxed{
 \#\{S\in\tbinom{[v]}k:S\text{ is not }D\text{-strong}\}
 \le 2^{v/2+o(v)}=2^{m+o(m)}.}
\tag{3.4}
\]

The same estimate holds for nonfree \(M\)-tops.

#### Proof

By Lemmas 3.1--3.2 and \(|G|\le v^2\), the left side is at most

\[
 v^2 2^{(v+1)/2}\sum_{j\le2D}\binom vj.
\tag{3.5}
\]

Since \(D=O(\sqrt{m\log m})=o(v/\log v)\), the binomial sum is
\(2^{o(v)}\).  This proves (3.4).  A nonfree top satisfies \(gU=U\) for
some \(g\ne1\), which is the case \(D=0\) of the same argument. \(\square\)

Every calibrated row has size \(2^{v-o(v)}\), so (3.4) is exponentially
negligible.  Summing it over \(O(H)\) ranks does not change its exponential
order.

## 4. An exact equivariant owner near-transversal

Set

\[
 a=\binom MH,\qquad b=\binom mH.
\tag{4.1}
\]

Every top contains \(a\) owners, every owner is contained in \(b\) tops,
and double counting gives

\[
 Na=Wb,\qquad \frac ab=\lambda_H\ge M.
\tag{4.2}
\]

### Theorem 4.1 (group-equivariant owner Hall theorem)

For either group in Section 3, there is a \(G\)-equivariant containment
assignment with the following properties.

* All but \(2^{-m+o(m)}N\) physical tops receive exactly \(M\) owners.
* No physical owner is assigned twice.
* Every assignment is literal containment \(X\subset U\).
* The total number of assigned owners is \(W-o(W)\).

#### Proof

Call an owner an **anchor** when it is \(10H\)-strong.  By Corollary 3.3
the number \(B\) of nonanchors satisfies

\[
 B=2^{m+o(m)}.
\tag{4.3}
\]

Call a top clean if it contains at least one anchor.  Every nonclean top
contributes all of its \(a\) owner incidences to the \(Bb\) incidences of
nonanchors.  Therefore

\[
 \#\{\text{nonclean tops}\}
 \le \frac{Bb}{a}
 =\frac{B}{\lambda_H}
 =2^{-m+o(m)}N.
\tag{4.4}
\]

Every clean top is automatically free.  Indeed, if \(A\subset U\) is an
anchor and \(gU=U\), then \(A,gA\subset U\), so
\(d_J(A,gA)\le H\), forcing \(g=1\).

More is true.  If \(X\subset U\) is any owner, then

\[
 d_J(X,gX)
 \ge d_J(A,gA)-d_J(A,X)-d_J(gA,gX)>8H
\tag{4.5}
\]

for every \(g\ne1\), because two owners in one \(M\)-top have distance at
most \(H\).  Thus every owner of a clean top is strongly free.

In fact every band mask inside a clean top is strongly free.  If
\(S\subset U\), \(m-H\le |S|\le M\), extend or restrict \(S\) to an owner
\(X\subset U\).  The symmetric-difference triangle inequality and (4.5)
give

\[
 d_J(S,gS)
 \ge d_J(X,gX)-\bigl||S|-m\bigr|>7H.
\tag{4.5a}
\]

Here \(d_J(S,gS)=|S\triangle gS|/2\), while the two comparison terms
between sets of unequal sizes together contribute exactly
\(\bigl||S|-m\bigr|\).

Form the quotient bipartite graph whose left vertices are the retained
free top orbits and whose right vertices are the owner orbits occurring in
those tops, with an edge for containment.

This quotient graph is simple.  Indeed, if
\(X,gX\subset U\), then

\[
 d_J(X,gX)\le |U|-m=H,
\tag{4.6}
\]

so strength forces \(g=1\).  Thus distinct strong owners inside one top
belong to distinct owner orbits.  Similarly, if \(U\) and \(gU\) both
contain a fixed strong owner \(X\), then \(U\) contains both \(X\) and
\(g^{-1}X\); (4.6) again forces \(g=1\).  Thus distinct tops containing a
strong owner belong to distinct top orbits.  The same argument rules out
multiple quotient incidence edges.

Consequently every left quotient vertex has its full degree \(a\), while
every right quotient vertex has degree at most \(b\).  For every
left family \({\cal A}\), edge counting gives

\[
 |N({\cal A})|
 \ge \frac ab|{\cal A}|
 =\lambda_H|{\cal A}|
 \ge M|{\cal A}|.
\tag{4.7}
\]

Clone each left vertex \(M\) times.  Inequality (4.7) is precisely the
Hall condition for the cloned graph, so there is an integral matching
which assigns \(M\) distinct owner orbits to every retained top orbit,
with no owner orbit reused.

Every chosen quotient edge is a free orbit of physical containment
incidences.  Its lift pairs each top in the top orbit with exactly one
owner in the owner orbit.  Lifting the matching therefore gives the first
three assertions.

Finally, (1.4) and (4.4) give

\[
 M(N-o(N))
 =W-o(W),
\tag{4.8}
\]

as required. \(\square\)

### Why Theorem 4.1 is not yet a packet theorem

The \(M\) owners of one cyclic packet form a cycle in the Johnson graph
\(J(M,m)\): consecutive windows have Johnson distance one.  There is also
an exact coordinate-degree constraint: across all \(M\) cyclic
\(m\)-windows, every coordinate of \(U\) occurs exactly \(m\) times.

Hall's theorem in Section 4 imposes neither constraint.  An arbitrary
set of \(M\) assigned owners can have no Johnson-adjacent pair at all.  Thus
"cyclicize the Hall assignment" is a genuinely new global theorem, not a
formal ordering step.

## 5. A sharp no-go for low-complexity ambient atlases

Let \(\Sigma\) be a family of \(K\) directed cyclic orders of the entire
\(v=2m\) point set.  Suppose that every assigned top order is obtained by
deleting the coordinates outside the top from some \(\sigma\in\Sigma\).
The choice of \(\sigma\) may depend arbitrarily on the top.

### Theorem 5.1 (ambient-atlas support bound)

Let \({\cal S}_r\) be the rank-\(r\) targets which occur as intervals in at
least one such top packet, and put \(d=M-r\).  If \(1\le d\le v-r\), then

\[
 \boxed{|{\cal S}_r|\le Kv\binom{v-d}{r}.}
\tag{5.1}
\]

#### Proof

Suppose \(S\) is an interval of the restriction \(\sigma|_U\).  Write

\[
 U=S\mathbin{\dot\cup}E,\qquad |E|=d.
\]

The complement \(E\) is also an interval in the restricted cyclic order.
Hence all points of \(E\) lie in one ambient \(\sigma\)-arc between two
consecutive points of \(S\).  That arc contains no point of \(S\) and has
at least \(d\) ambient positions.  Therefore \(S\) avoids some consecutive
ambient \(d\)-block.

For fixed \(\sigma\), there are \(v\) such blocks and at most
\(\binom{v-d}{r}\) rank-\(r\) sets avoiding each block.  Union over the
blocks and over \(\Sigma\) proves (5.1). \(\square\)

### Corollary 5.2 (calibrated exponential loss)

Write \(r=m+s\), so \(d=H-s\).  Uniformly for
\(|s|\le H=o(m)\) and \(1\le d\le2H\),

\[
 \log\frac{\binom{2m-d}{m+s}}{\binom{2m}{m+s}}
 \le-d\log2+O(H^2/m).
\tag{5.2}
\]

Consequently, if \(\log K=o(H)\), the atlas supports only an \(o(1)\)
fraction of

1. both rows \(r=m\pm q\), uniformly for every fixed
   \(0\le q\le A\sqrt m\);
2. every lower row \(r=m-q\), \(0\le q\le H\); and
3. every upper row \(r=m+q\), \(0\le q\le H/2\).

#### Proof

The exact ratio is

\[
 \frac{\binom{2m-d}{m+s}}{\binom{2m}{m+s}}
 =\prod_{j=0}^{d-1}\frac{m-s-j}{2m-j}.
\tag{5.3}
\]

Taylor expansion of each logarithm, uniformly in the displayed range,
gives

\[
 -d\log2-\frac{ds}{m}-\frac{d(d-1)}{4m}
 +O\left(\frac{d(|s|+d)^2}{m^2}\right),
\tag{5.4}
\]

which implies (5.2).

For \(|s|\le A\sqrt m\), one has
\(d=(1+o(1))H\).  For the lower band \(s=-q\), one has
\(d=H+q\ge H\).  For the upper half-band \(s=q\le H/2\), one has
\(d=H-q\ge H/2\).  Since

\[
 H^2/m=O(\log m)=o(H),\qquad \log(Kv)=o(H),
\]

(5.1)--(5.2) give an exponentially vanishing fraction in all three cases.
\(\square\)

There is deliberately no upper-band claim when \(H/2<q\le H\): at the
top itself, \(q=H\), one has \(d=0\).

If an ambient template family has \(K_0\) seeds and a group of order
\(\gamma\) supplies all their images, then \(K\le K_0\gamma\).  Thus
Theorem 5.1 rules out every such architecture with
\(\log(K_0\gamma)=o(H)\), including polynomial-size affine orbits of
subexponentially many ambient seeds.  A viable orbit construction must be
top-intrinsic, rather than a small ambient atlas.

## 6. Quotienting controls, but does not improve, interval collisions

Let \({\mathscr P}\) be a \(G\)-invariant family of packet columns.  On
free, internally orbit-rainbow packets, define quotient degree and
codegree by counting packet orbits.

### Proposition 6.1 (exact quotient codegree identity)

Let \(X,Y\) be free target representatives.  Assume every packet orbit
incident to \([X]\) contains a unique representative packet containing
\(X\), and that such a packet contains at most one member of \([Y]\).
All degrees and codegrees below are taken in the same retained
\(G\)-invariant packet family.  Then

\[
 \boxed{
 \operatorname {codeg}_G([X],[Y])
 =\sum_{g\in G}\operatorname {codeg}(X,gY).}
\tag{6.1}
\]

#### Proof

Choose the unique representative containing \(X\) from every quotient
packet orbit counted on the left.  Its unique target from \([Y]\) is
\(gY\) for one \(g\).  This gives a bijection with the disjoint union of
the packet sets counted on the right. \(\square\)

### Proposition 6.2 (one-alignment theorem in the calibrated band)

Suppose \(m-H\le k<M\) and \(m>3H\).  If \(Y\) is \(4H\)-strong, then for
fixed \(X\in\binom{[v]}k\) at most one \(g\in G\) can satisfy

\[
 \operatorname {codeg}(X,gY)>0.
\tag{6.2}
\]

Consequently, in the strong sector quotient codegrees are no larger than
ambient codegrees.

#### Proof

Two rank-\(k\) intervals in one \(M\)-packet are subsets of the same top,
so their Johnson distance is at most

\[
 \min(k,M-k)=M-k\le2H.
\tag{6.3}
\]

If both \(g\) and \(h\) satisfy (6.2), then

\[
 d_J(gY,hY)
 \le d_J(gY,X)+d_J(X,hY)\le4H.
\]

After applying \(g^{-1}\), strength of \(Y\) forces \(g=h\). \(\square\)

For middle owners, \(2H\)-strength is enough for uniqueness of the group
alignment.  A \(10H\)-strong owner \(X\) makes every top containing it
clean, so every packet containing \(X\) remains in the anchor-clean core.
Its quotient degree can therefore be normalized by the full ambient degree

\[
 D_0=\binom mH m!H!=\frac{(m!)^2}{(m-H)!}.
\tag{6.4}
\]

If owners \(X,Y\) have Johnson distance \(1\le j<H\), direct block
counting gives

\[
 \frac{\operatorname {codeg}(X,Y)}{D_0}
 =\frac{2}{\binom mj^2}\le\frac2{m^2}.
\tag{6.5}
\]

Indeed, choose the remaining \(H-j\) top points and arrange the four
blocks \(X\setminus Y,X\cap Y,Y\setminus X,U\setminus(X\cup Y)\) in
either admissible cyclic orientation.  This gives

\[
 \operatorname {codeg}(X,Y)
 =\binom{m-j}{H-j}
   2(m-j)!(j!)^2(H-j)!,
\]

which simplifies to (6.5).  Propositions 6.1--6.2 show that, after choosing
co-occurring representatives, the same exact ratio holds on the
anchor-clean quotient when \(X\) is \(10H\)-strong and \(Y\) is
\(2H\)-strong.  Without the anchor condition, the retained quotient degree
may be smaller than \(D_0\), so no full-degree normalization is asserted.

For different target ranks, the same orbit-rainbow argument gives at most
one group alignment once the relevant target orbit is sufficiently
separated.  This proves collision safety, but no new numerical cross-rank
bound is claimed here.  In particular, quotienting cannot remove the known
adjacent owner--facet correlation.  Under unrestricted interval incidence,
an owner window contains exactly two cyclic \((m-1)\)-windows among its
\(m\) facets, giving \(2/m\).  Under the audited same-phase convention,
one of those orientations is selected, giving \(1/m\).  Both remain
\(\Theta(1/m)\) after quotienting; affine symmetry supplies no vanishing
factor beyond the ambient one.

## 7. The surviving top-intrinsic affine candidate

Use the audited common-priority calibrated decoration of top packets.  It
has the following two properties needed here.

1. The number \(R_m\) of claimed owner/flag vertices in one decorated
   packet satisfies
   \[
   R_m=O(m^{3/2}).
   \tag{7.1}
   \]
2. If all but \(E\) physical top packets are selected with disjoint claimed
   targets, then their contribution to the aggregate calibrated defect is
   \(O(ER_m)\), in addition to the already audited scalar rounding term.

Let \(\gamma=|G|\).  Retain precisely the anchor-clean top orbits from
Section 4 and all decorated packet orbits above them.  Every such top is
free, and (4.5a) says that every one of its calibrated-band masks is
\(>7H\)-separated.  Thus every retained packet orbit is a simple quotient
hyperedge: one top-orbit vertex and one vertex for every claimed
target-orbit label.  No order-by-order deletion is needed.  The omitted
physical tops number only \(2^{-m+o(m)}N\).

### Candidate 7.1 (top-intrinsic quotient packet matching; unproved)

For \(G=C_{2m}\) in every dimension, or
\(G=\operatorname {AGL}(1,2^a)\) on the power-of-two subsequence, the good
quotient augmented packet hypergraph has a matching containing an edge
above all but

\[
 \boxed{
 e_m=o\left(\frac{W}{\gamma m^{3/2}}\right)}
\tag{7.3}
\]

retained top-orbit vertices.

### Proposition 7.2 (Candidate 7.1 implies the calibrated packet lemma)

Assume Candidate 7.1.  Lift every chosen quotient edge to its full
\(G\)-orbit.  Then every covered physical top receives exactly one literal
cyclic packet, every claimed target has physical load at most one, and the
aggregate additional defect is \(o(W)\).

#### Proof

All retained tops and packets are free, so Corollary 2.2 gives one lifted
packet per covered top.  Strongness makes each quotient edge internally
simple, and matching disjointness makes different edges use disjoint target
orbits.  Their lifts therefore use every physical claimed target at most
once.

The unmatched quotient tops account for at most

\[
 \gamma e_m R_m=o(W)
\tag{7.4}
\]

additional missing claims.  The exponentially few exceptional tops and
target masks account for \(2^{m+o(m)}=o(W)\) more; explicitly, their top
contribution is at most

\[
 2^{-m+o(m)}N R_m=2^{m+o(m)}.
\]

The calibrated
decoration then gives the desired aggregate packet defect. \(\square\)

Candidate 7.1 is top-intrinsic and is not covered by the ambient-atlas
no-go: its seed order is allowed to depend on the top orbit, and
exponentially many inequivalent ambient extensions may occur.

## 8. Precise proved/conditional boundary and adversarial audit

The strongest unconditional positive result is Theorem 4.1.  It closes
all scalar owner capacity, group-orbit divisibility, and integrality issues
with a deterministic exact lift.

It does **not** close cyclic coherence.  The smallest remaining assertion
is Candidate 7.1, or already its middle-only specialization:

> Choose one top-intrinsic cyclic packet orbit above almost every free top
> orbit so that the resulting owner-orbit sets are pairwise disjoint, with
> a leave small enough for (7.3); then impose the common nested shallow
> claims without increasing that leave.

The following possible overclaims have been excluded explicitly.

* Theorem 4.1 is an unbundled inclusion matching, not a packet factor.
* Theorem 5.1 applies only to a common ambient atlas of size
  \(\exp(o(H))\).  It says nothing against exponentially many
  top-dependent orders.
* Strongness removes duplicate group alignments, but Proposition 6.1 shows
  that the quotient retains, rather than improves, the hard vertical
  correlation.
* Exceptional stabilizer orbits can be discarded at exponentially small
  cost.  They cannot be filled equivariantly unless the exact conditions
  (2.4) and Proposition 2.3 hold.
* No fractional orbit mixture is used anywhere in the proved owner
  assignment.

Thus the algebraic lane has a sharp conclusion: free affine/cyclic orbits
are fully compatible with exact unbundled ownership and do not create
shallow same-rank orbit collisions, but low-complexity ambient orbit
atlases are impossible.  What remains is a positive top-intrinsic
cyclic-bundling theorem, not another divisibility calculation.
