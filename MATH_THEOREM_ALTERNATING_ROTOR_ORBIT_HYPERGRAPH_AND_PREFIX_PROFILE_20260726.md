# The odd-\(m\) alternating rotor orbit: exact codegrees, prefix loads, and the remaining design gate

Date: 2026-07-26

## Verdict

For odd \(m\), the alternating component from Theorem 4.6 has a very
rigid product normal form.  Its coordinate orbit gives a
\(2m(m+1)\)-uniform, exactly regular hypergraph on the \(m\)-subsets.
The exact degree and worst pair-codegree are

\[
 D=\frac{m!(m+1)!}{2},
 \qquad
 \frac{\Delta_2}{D}=\frac{3}{m+1}
 \tag{0.1}
\]

for all sufficiently large odd \(m\).  The maximum is attained by
disjoint owner pairs.  At Johnson distance one the sharper exact ratio is

\[
 \frac{D_1}{D}=\frac{8}{m(m+1)}.
 \tag{0.2}
\]

Thus the owner catalogue has excellent pair sparsity, but its rank is
\(\Theta(m^2)\).  The audited general growing-uniformity nibble theorems
do not give a leave \(o(W/m)\): the full-edge constraint sees

\[
 D^{1/(2m(m+1)-1)}
 =\exp\!\left((1+o(1))\frac{\log m}{m}\right)
 =1+o(1).
 \tag{0.3}
\]

There is also a sharp prefix warning.  In a single alternating component,
the lower-prefix profile alternates between rainbow and double-covered
according to parity, while its signed upper--lower divergence is maximal
at every depth:

\[
 \frac12\|R_s-L_s\|_1=m(m+1)
 \qquad(1\le s\le m).
 \tag{0.4}
\]

Consequently the alternating component solves the long-component and
owner-simplicity gates, but it is actually incompatible with the first
lower shadow.  Even a perfect owner matching by these blocks can cover
at most \(W/2\) rank-\((m-1)\) targets, whereas
\(N_1=mW/(m+2)\).  Thus it leaves
\((1/2-o(1))W\) first-shadow holes.  The pure alternating-block route is
therefore closed.  In fact, any viable rotor construction may place only
\(o(W)\) owner occurrences in these components; the bulk must use a
different parity profile.

## 1. Product normal form

Assume

\[
 m=2r+1\ge3,\qquad n=2m+1,\qquad L=m(m+1).
\]

Let \(G=BA\), with position cycles

\[
 C_0=(1,3,5,\ldots,2m-1),\qquad
 C_1=(2,4,6,\ldots,2m,2m+1),
\]

of lengths \(m\) and \(m+1\).  Write
\(\mathcal I_{\ell,a}\) for the family of cyclic intervals of length
\(a\) in an \(\ell\)-cycle.

Let \(\mathcal B\) be the set of middle owners occurring in one
alternating component.  Then, relative to \(C_0\sqcup C_1\),

\[
 \boxed{
 \mathcal B=
 \bigl(\mathcal I_{m,r+1}\times\mathcal I_{m+1,r}\bigr)
 \mathbin{\dot\cup}
 \bigl(\mathcal I_{m,r}\times\mathcal I_{m+1,r+1}\bigr).}
 \tag{1.1}
\]

In particular,

\[
 K:=|\mathcal B|=2m(m+1)=2L.
 \tag{1.2}
\]

### Proof

The two base owners are

\[
 P=\{1,\ldots,m\},\qquad Q=\{2,\ldots,m+1\}.
\]

Their intersection sizes with \(C_0,C_1\) are respectively

\[
 (r+1,r),\qquad (r,r+1).
\]

A power \(G^j\) rotates independently on \(C_0\) and \(C_1\).
Because \(m\) and \(m+1\) are coprime, the Chinese remainder theorem
makes the two rotations independent as \(j\) ranges over
\(\mathbb Z_L\).  The \(G\)-orbit of \(P\) is therefore the first
product in (1.1), and the \(G\)-orbit of \(Q\) is the second.  Their
intersection-size vectors differ, so the products are disjoint.
\(\square\)

## 2. The exact coordinate-orbit hypergraph

Let

\[
 V=\binom{[n]}m,\qquad W=|V|,
\]

and let \(\mathcal H_m\) be the simple orbit hypergraph whose edges are
the distinct images \(g\mathcal B\), \(g\in S_n\).

### Lemma 2.1 (block stabiliser)

For every odd \(m\ge3\),

\[
 \operatorname{Stab}_{S_n}(\mathcal B)
 \cong D_m\times D_{m+1},
 \qquad
 |\operatorname{Stab}(\mathcal B)|=4m(m+1)=2K.
 \tag{2.1}
\]

#### Proof

The number of members of \(\mathcal B\) containing a fixed coordinate is

\[
 \begin{cases}
 m(m+1),&x\in C_0,\\
 m^2,&x\in C_1.
 \end{cases}
 \tag{2.2}
\]

Indeed, for \(x\in C_0\), the two terms in (1.1) contribute
\((r+1)(m+1)\) and \(r(m+1)\).  For \(x\in C_1\), they contribute
\(mr\) and \(m(r+1)\).  The values in (2.2) differ, so every block
stabiliser preserves \(C_0\) and \(C_1\) setwise.

After this partition is fixed, the projections of \(\mathcal B\) onto
each part are exactly the indicated cyclic-interval families.  The
automorphism group of a nontrivial cyclic-interval family is the
dihedral group of the underlying cycle.  This also holds in the two
small boundary cases: on three points \(D_3=S_3\), and on four points
the length-two intervals recover the four-cycle.  Thus the restriction
to \(C_0\) lies in \(D_m\), and the restriction to \(C_1\) lies in
\(D_{m+1}\).  Conversely, the two dihedral groups independently preserve
both products in (1.1).  This proves (2.1). \(\square\)

### Corollary 2.2 (edge count and exact degree)

\[
 |E(\mathcal H_m)|=\frac{n!}{4m(m+1)}
 \tag{2.3}
\]

and \(\mathcal H_m\) is regular of degree

\[
 \boxed{D=\frac{m!(m+1)!}{2}.}
 \tag{2.4}
\]

#### Proof

Equation (2.3) is orbit--stabiliser.  Double-counting vertex--edge
incidences and using \(n!/W=m!(m+1)!\) gives

\[
 D=\frac{|E|K}{W}
 =\frac{n!}{4m(m+1)}\frac{2m(m+1)}W
 =\frac{m!(m+1)!}{2}.
\]

\(\square\)

The same calculations can instead be made in the labelled orbit
multihypergraph with one copy for each \(g\in S_n\).  Every degree is
then multiplied by \(4m(m+1)\), so all relative codegrees below are
unchanged.

## 3. Exact pair-codegree formula

For \(0\le d\le m\), put

\[
 b_d=\binom md\binom{m+1}d.
 \tag{3.1}
\]

Every \(m\)-set has exactly \(b_d\) other \(m\)-sets at Johnson distance
\(d\).  Let

\[
 N_d(\mathcal B)
 =|\{(X,Y)\in\mathcal B^2:d_J(X,Y)=d\}|
\]

count ordered block pairs, and define

\[
 c_d=\frac{N_d(\mathcal B)}K.
 \tag{3.2}
\]

Thus \(c_d\) is the average number of block members at distance \(d\)
from a fixed block member.

### Proposition 3.1 (exact orbital formula)

For an ordered ambient pair \(X,Y\) at Johnson distance \(d\), its
common edge degree \(D_d\) is

\[
 \boxed{
 \frac{D_d}{D}
 =\frac{c_d}{\binom md\binom{m+1}d}.}
 \tag{3.3}
\]

#### Proof

The symmetric group is transitive on ordered pairs at Johnson distance
\(d\).  Double-count triples consisting of an orbit edge and an ordered
distance-\(d\) pair inside it:

\[
 |E(\mathcal H_m)|N_d(\mathcal B)
 =Wb_dD_d.
\]

The degree identity \(|E|K=WD\) now gives (3.3). \(\square\)

### Proposition 3.2 (the two exact endpoint counts)

\[
 \boxed{c_1=8,\qquad c_m=3}
\tag{3.4}
\]

for odd \(m\ge5\).  (At the exceptional value \(m=3\),
\(c_1=17/2\), while \(c_m=3\) still holds.)

Consequently

\[
 \frac{D_1}{D}=\frac8{m(m+1)},
 \qquad
 \frac{D_m}{D}=\frac3{m+1}.
 \tag{3.5}
\]

#### Proof

Fix a member \(X=(I,J)\) of either product in (1.1).

For \(m\ge5\), at distance one there are four targets of the same type:
shift \(I\)
one step in either direction while fixing \(J\), or shift \(J\) one
step in either direction while fixing \(I\).  There are also four
targets of the opposite type: delete either endpoint from the larger
interval and add either adjacent endpoint to the smaller interval.
These eight targets are distinct, proving \(c_1=8\).

For a first-type owner, a disjoint target must have the opposite type.
Its interval on the odd cycle \(C_0\) is forced to be the complement of
the larger interval, and there are exactly two choices on \(C_1\).
Thus a first-type owner has two disjoint block partners.

A second-type owner also has two opposite-type disjoint partners.  In
addition it has two same-type disjoint partners: on \(C_1\) the
length-\((r+1)\) interval is forced to its complementary interval,
while on \(C_0\) there are two length-\(r\) intervals disjoint from the
given length-\(r\) interval.  Thus a second-type owner has four
disjoint block partners.  The two types have equal size \(L\), so their
average is

\[
 c_m=\frac{2+4}{2}=3.
\]

For \(m=3\), direct inspection of the two small interval families gives
\(c_1=17/2\); this finite exception has no asymptotic role. \(\square\)

### Lemma 3.3 (uniform all-distance bound)

For \(1\le d\le m\),

\[
 c_d\le18\bigl(\min\{d,m-d\}+1\bigr).
 \tag{3.6}
\]

#### Proof

Fix \(X\) and one of the two possible target types.  Write
\(X_i=X\cap C_i\), \(Y_i=Y\cap C_i\).  The two intersection sizes
\(|X_i\cap Y_i|\) sum to \(m-d\), while the two deletion counts
\(|X_i\setminus Y_i|\) sum to \(d\).  Hence there are at most

\[
 \min\{d,m-d\}+1
\]

admissible splits between \(C_0\) and \(C_1\).

For a fixed cyclic interval \(I\), fixed target length differing from
\(|I|\) by at most one, and fixed intersection size, there are at most
three target intervals.  Partial overlaps give at most two choices;
containment gives at most two; and the only larger disjoint family
occurs for two length-\(r\) intervals in the \(2r+2\)-cycle, where
there are three.  Thus each split gives at most \(3^2=9\) target
pairs.  There are two target types.  This proves (3.6). \(\square\)

### Corollary 3.4 (worst pair-codegree)

For all sufficiently large odd \(m\),

\[
 \boxed{
 \max_{X\ne Y}
 \frac{D(X,Y)}D
 =\frac3{m+1},}
 \tag{3.7}
\]

attained precisely at the antipodal Johnson class \(d=m\).  In
particular,

\[
 \Delta_2=\frac32(m!)^2.
 \tag{3.8}
\]

#### Proof

At \(d=1\), (3.5) is \(8/[m(m+1)]<3/(m+1)\).
For \(2\le d\le m-1\), combine (3.3) and (3.6).  The binomial product
in the denominator grows at least quadratically beyond either endpoint,
whereas the numerator is linear in the nearer endpoint distance.  More
explicitly, if \(2\le d\le m/2\), then

\[
 \binom md\binom{m+1}d
 \ge \binom m2\binom{m+1}2,
\]

while the numerator in (3.6) is \(O(m)\).  If \(m/2<d\le m-1\), put
\(k=m-d\).  Then

\[
 \binom md\binom{m+1}d
 =\binom mk\binom{m+1}{k+1}
 \ge m\binom{m+1}2,
\]

and again the numerator is \(O(m)\).  Consequently, uniformly in the
whole range,

\[
 \frac{18(\min\{d,m-d\}+1)}
 {\binom md\binom{m+1}d}
 =o(1/m).
\]

The value \(3/(m+1)\) at \(d=m\) is exact by (3.5), proving (3.7).
Finally, substitute (2.4):

\[
 D\frac3{m+1}
 =\frac{m!(m+1)!}{2}\frac3{m+1}
 =\frac32(m!)^2.
\]

\(\square\)

## 4. Why the generic nibble does not give the required leave

A matching in \(\mathcal H_m\) covering all but \(o(W/m)\) vertices
would pack alternating components with the component count required by
the rotor compiler.  The exact pair bound (3.7) is encouraging, but it
does not put the problem inside any audited black-box matching theorem.

Indeed,

\[
 K=2m(m+1)=(2+o(1))m^2
\tag{4.1}
\]

and Stirling's formula gives

\[
 \log D=(2+o(1))m\log m.
\tag{4.2}
\]

Therefore

\[
 \frac{\log D}{K}
 =(1+o(1))\frac{\log m}{m},
\qquad
 D^{1/(K-1)}=1+o(1).
\tag{4.3}
\]

The fixed-uniformity Pippenger--Frankl--Rödl theorem does not apply
uniformly when \(K\to\infty\), and its qualitative \(o(W)\) conclusion
would not by itself imply the stronger \(o(W/m)\) leave.

More sharply, the higher-codegree nibble audited in
MATH_AUDIT_PORT_HYPERGRAPH_GENERAL_NIBBLE_STALLING_20260726.md uses a
parameter bounded by

\[
 \min_{4\le j\le K}(D/D_j)^{1/(j-1)}.
\]

Because a simple \(K\)-graph has \(D_K=1\), its \(j=K\) constraint is
at most \(D^{1/(K-1)}=1+o(1)\).  Its resulting leave estimate is not
even \(o(W)\), and hence cannot yield \(o(W/m)\).  Better pair
codegrees do not remove this full-edge bottleneck within that theorem.

This is a black-box limitation, not a nonexistence result.  The product
structure (1.1) is much stronger than arbitrary high-uniformity
sparsity, and a specialised factorisation theorem could exploit it.

## 5. Exact lower-prefix profile of one component

For \(1\le s\le m\), the two base lower-prefix position sets are

\[
 P_s=\{1,\ldots,s\},\qquad Q_s=\{2,\ldots,s+1\}.
\tag{5.1}
\]

The \(2L\) lower-prefix occurrences in the alternating component are the
\(G\)-orbits of \(P_s\) and \(Q_s\).

### Proposition 5.1 (parity profile)

At \(s=1\), every label in the \(m\)-element class \(C_0\) has load
\(m+1\), and every label in the \((m+1)\)-element class \(C_1\) has
load \(m\).

For \(2\le s\le m\):

* if \(s\) is odd, the component has load \(1\) on \(2L\) distinct
  \(s\)-sets and load \(0\) elsewhere;
* if \(s\) is even, the component has load \(2\) on \(L\) distinct
  \(s\)-sets and load \(0\) elsewhere.

Equivalently, at lower depth \(s=m-q\), since \(m\) is odd, the
component is rainbow when \(q\) is even and exactly doubled when \(q\)
is odd.

#### Proof

For \(s=2u+1\), the intersection-size vectors of \(P_s,Q_s\) with
\((C_0,C_1)\) are

\[
 (u+1,u),\qquad(u,u+1).
\]

Their \(G\)-orbits are disjoint.  For \(s\ge2\), both nonempty
interval factors have trivial rotational stabiliser, so each orbit has
length \(L\).

For \(s=2u\), both vectors are \((u,u)\).  On \(C_0\), \(Q_s\) is a
one-step translate of \(P_s\), while on \(C_1\) it is unchanged.
The Chinese remainder theorem therefore gives \(Q_s=G^jP_s\) for some
\(j\), so the two length-\(L\) orbits coincide and every target in the
orbit has load two.

For \(s=1\), the \(P_1\)-orbit is \(C_0\), traversed \(L/m=m+1\)
times, and the \(Q_1\)-orbit is \(C_1\), traversed
\(L/(m+1)=m\) times. \(\square\)

### Corollary 5.2 (statewise first-shadow no-go)

Let \(\mathcal P\) be any collection of pairwise owner-disjoint
coordinate relabels of alternating components.  Then its rank-\((m-1)\)
lower-prefix hole count satisfies

\[
 \boxed{
 M_1^-(\mathcal P)
 \ge
 \frac{m-2}{2(m+2)}\,W
 =
 \left(\frac12-o(1)\right)W.}
 \tag{5.2}
\]

This remains true even if the owner packing is perfect up to divisibility.

#### Proof

Each component owns \(K=2L\) distinct middle sets, so owner-disjointness
forces

\[
 |\mathcal P|\le\frac{W}{2L}.
\]

At depth \(q=1\), one has \(s=m-1\), which is even.  Proposition 5.1
shows that each component's \(2L\) occurrences have support of size
only \(L\).  Therefore the union of all rank-\((m-1)\) supports has
size at most

\[
 |\mathcal P|L\le\frac W2.
\]

There are

\[
 N_1=\binom n{m-1}=\frac{m}{m+2}W
\]

rank-\((m-1)\) targets.  Subtracting \(W/2\) gives (5.2).
\(\square\)

Thus the coordinate-orbit owner matching problem, even if solved
perfectly, cannot supply the lower-prefix theorem.  The obstruction is
not probabilistic overlap between different blocks: it is the
deterministic factor-two collision inside every block.

### Corollary 5.3 (alternating blocks cannot have positive density in a hybrid)

Suppose an owner-transversal circulation uses \(A_{\rm alt}\) of its
\(W\) middle-owner occurrences inside disjoint alternating components,
and uses arbitrary other component types on the remaining owners.  Then

\[
 \boxed{
 M_1^-\ge
 \left(
 \frac{A_{\rm alt}}2-\frac{2W}{m+2}
 \right)_+.}
 \tag{5.3}
\]

In particular, \(M_1^-=o(W)\) forces \(A_{\rm alt}=o(W)\).

#### Proof

The alternating occurrences have rank-\((m-1)\) support at most
\(A_{\rm alt}/2\).  The remaining \(W-A_{\rm alt}\) occurrences can
support at most one new target each, regardless of their component
geometry.  Thus total support is at most

\[
 \frac{A_{\rm alt}}2+W-A_{\rm alt}
 =W-\frac{A_{\rm alt}}2.
\]

Subtract this from \(N_1=W-2W/(m+2)\), and take the positive part.
\(\square\)

## 6. Exact divergence profile

Only the states \(G^j\pi\) use an \(A\)-transition.  For rank \(s\), the
base positive and negative endpoints in the divergence identity are

\[
 U_s=\{n-s+1,\ldots,n\},
\qquad
 V_s=\{1,n-s+1,\ldots,n-1\}.
\tag{6.1}
\]

The sets \(U_s,V_s\) have different intersection sizes with
\((C_0,C_1)\), because \(1\in C_0\) and \(n\in C_1\).  Their
\(G\)-orbits are therefore disjoint.

### Proposition 6.1 (maximal component divergence)

For every \(1\le s\le m\),

\[
 \boxed{
 \frac12\|R_s-L_s\|_1=L=m(m+1).}
\tag{6.2}
\]

#### Proof

The component has exactly \(L\) selected \(A\)-arcs.  In the divergence
identity, their positive endpoints form the \(G\)-orbit multiset of
\(U_s\), with total mass \(L\), and their negative endpoints form the
orbit multiset of \(V_s\), also with total mass \(L\).  The two supports
are disjoint by their different \((C_0,C_1)\)-intersection vectors.
Thus the signed vector has \(\ell^1\)-norm \(2L\). \(\square\)

At rank one this gives a useful necessary balancing condition.  Let
\(Z\) be the \(m\)-label class occupying the positions \(C_0\).  One
component contributes

\[
 R_1-L_1
 =
 m\sum_{x\notin Z}\mathbf e_x
 -(m+1)\sum_{x\in Z}\mathbf e_x.
\tag{6.3}
\]

For \(t\) selected coordinate relabels, let \(d_x\) be the number of
their \(m\)-sets \(Z\) containing \(x\).  The coefficient at \(x\) is

\[
 mt-nd_x.
\tag{6.4}
\]

Hence exact rank-one cancellation is equivalent to

\[
 d_x=\frac{mt}{n}\qquad\text{for every }x.
\tag{6.5}
\]

Since \(\gcd(m,n)=1\), this forces

\[
 n\mid t.
\tag{6.6}
\]

Thus even the first divergence coordinate requires the chosen
components' \(C_0\)-classes to form an exact regular design.  Higher
ranks impose nested analogues of the same requirement.

## 7. Final status

The odd-\(m\) alternating component gives, unconditionally:

1. \(K=2m(m+1)\) distinct middle owners;
2. a simple coordinate-orbit hypergraph of exact degree
   \(m!(m+1)!/2\);
3. worst relative pair-codegree \(3/(m+1)\), with the much smaller
   adjacent ratio \(8/[m(m+1)]\);
4. component length \(\Theta(m^2)\), exactly at the desired low-cycle
   scale.

It cannot give:

1. a black-box matching leave \(o(W/m)\);
2. lower-prefix near-rainbowness: Corollary 5.2 forces
   \((1/2-o(1))W\) holes already at depth one;
3. signed-divergence cancellation.

The pure alternating-block architecture is therefore closed for the
band problem.  Corollary 5.3 says more: the component cannot even be a
positive-density part of a successful hybrid.  It can serve only as a
vanishing reserve module unless another operation changes its internal
prefix profile.  Any hybrid must also balance the maximal divergences
quantified in Section 6.
