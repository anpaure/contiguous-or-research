# Cyclic-quotient cross-orbit bridge packing and the exact star-factor gate

**Date:** 2026-08-06  
**Method:** literal depth-three normal form, cyclic-orbit counting, greedy
rainbow hypermatching, and modular-sum core colouring  
**Status:** unconditional prospective cross-orbit packing theorem and an
unconditional positive-scale bottom-disjoint star packing.  The residual quotient-chain
extension and the all-depth target-disjoint star factor remain open.

## 0. Outcome

The old direct necklace lift fails because almost every middle set has no
Johnson-adjacent nontrivial rotation.  That obstruction is strictly
within-orbit.  Cross-orbit supply is different.

For depth three, every literal state-compatible bridge has a seven-resource
Boolean normal form.  After removing exponentially few periodic or
within-orbit atoms, those atoms form a quotient hypergraph with

\[
 |\mathcal A|=(1-o(1))\mathsf N_{m-2}D,
 \qquad
 D=(m-2)(m+1)(m+2)(m+3),
\]

where \(\mathsf N_{m-2}=\binom{2m+1}{m-2}/(2m+1)\) is the
normalized quotient scale.  A direct greedy argument gives
a resource-disjoint, owner-rainbow matching of size

\[
 \boxed{|M|\ge (1/13-o(1))\mathsf N_{m-2}.}
\]

Thus a positive fraction of quotient chain fragments can be joined by
literal cross-orbit, age-compatible bridges.  The direct-necklace no-go is
not a global bridge-scarcity theorem.

For general depth, there is a canonical renewal bridge which rotates the
complete age composition.  It is literal and cross-orbit on all but an
exponentially small set.  Its exact invariant is the cyclic orbit of the
age-composition vector; this bounded-state bridge alone cannot mix different
composition necklaces.

Finally, for the new full-piece star packet, modular-sum colouring gives a
family of at least

\[
 \frac1n\binom n{s-1}
\]

maximal common-core packets whose bottom targets are pairwise disjoint.
They serialize at least

\[
 \boxed{\frac{s}{n}\binom ns}
\]

full pieces using the correct (\Theta(\binom ns/n)) number of packets.
This closes the bottom row at the required scale.  It does not close the
higher rows: an exact balanced two-exchange obstruction already appears at
depth two.  The remaining star theorem is a coloured cyclic-interval
matching problem, not an ordinary Johnson matching.

## 1. The literal depth-three cross-orbit atom

Let

\[
 \Omega=\mathbb Z_n,\qquad n=2m+1.
\]

Choose

\[
 S\in\binom\Omega{m-2},\qquad \gamma\in S,
\]

and pairwise distinct labels

\[
 \beta,a,z\in\Omega\setminus S.
\]

Put

\[
 T=S-\{\gamma\}+\{\beta\},\qquad H=S\cup\{\beta\}.
\]

Define two saturated quotient-chain fragments

\[
 \begin{aligned}
 \mathcal C^-&:\quad S\subset S+a\subset S+a+z,\\
 \mathcal C^+&:\quad T\subset H\subset H+a.
 \end{aligned}
 \tag{1.1}
\]

Here and below \(X+x\) means \(X\cup\{x\}\).

### Theorem 1.1 (exact bridge normal form)

The two flags in (1.1) have the literal deletion words

\[
 (z,a),\qquad(a,\gamma),
\]

respectively.  Therefore they form a legal depth-three state-compatible
turn with common rail state \(a\).  Their roots are Johnson adjacent,

\[
 R^-=S+a+z,qquad R^+=S+a+\beta,
\]

and the owner colour is

\[
 O=S+a+z+\beta.
 \tag{1.2}
\]

Conversely, every legal Johnson, state-compatible turn between two full
depth-three flags has this form after naming its common rail state \(a\).

#### Proof

Deleting \(z\) and then \(a\) from \(R^-\) gives the first chain in
(1.1).  Deleting \(a\) and then \(\gamma\) from \(R^+=H+a\) gives

\[
 H-\gamma=S-\gamma+\beta=T.
\]

The second departure \(\gamma\) survives in the old bottom \(S\), exactly
the depth-three age condition.  The two roots differ by the exchange
(z\leftrightarrow\beta), and their union is (1.2).

For the converse, normalize a legal turn by its common state \(a\).  Let
\(S\) be the old bottom, \(z\) the old first departure, \(\gamma\in S\) the
new second departure, and \(\beta\) the entering root label.  The two flags
then reconstruct exactly as (1.1).  \(\square\)

The bottom targets \(S,T\), the two rank-\((m-1)\) targets \(S+a,H\), the
two roots \(R^-,R^+\), and the owner \(O\) are the seven named resources of
the atom.

## 2. Exact atom and resource degrees

Let

\[
 \begin{aligned}
 D_0&=(m-2)(m+3)(m+2)(m+1),\\
 D_1&=(m-1)(m-2)(m+2)(m+1),\\
 D_2&=m(m-1)(m-2)(m+1).
 \end{aligned}
 \tag{2.1}
\]

### Lemma 2.1 (exact labelled degrees)

The number of labelled atoms is

\[
 \binom n{m-2}D_0.
 \tag{2.2}
\]

A fixed resource occurs in at most the following numbers of atoms:

\[
\begin{array}{c|c}
\text{resource rank}&\text{total degree over both roles}\\ \hline
m-2&2D_0\\
m-1&2D_1\\
m&2D_2\\
m+1&D_2.
\end{array}
\tag{2.3}
\]

#### Proof

After fixing \(S\), choose \(\gamma\in S\), then choose the ordered,
distinct triple \((\beta,a,z)\) outside \(S\).  This gives (2.2).

For a fixed old rank-\((m-1)\) resource \(P=S+a\), choose \(a\in P\),
\(\gamma\in P-a\), and the ordered pair \((\beta,z)\) outside \(P\).
This gives \(D_1\) atoms in that role.  The new rank-\((m-1)\) role is
symmetric.  For a fixed old root, choose the ordered pair \((a,z)\) in the
root, then \(\gamma\) in the remaining bottom and \(\beta\) outside the
root; this gives \(D_2\).  The new-root role has the same count.  For a
fixed owner, choose the ordered triple \((\beta,a,z)\) inside it and then
\(\gamma\) in the remaining bottom, again giving \(D_2\).  \(\square\)

Notice that

\[
 D_1\le D_0,\qquad D_2\le D_0.
 \tag{2.4}
\]

At \(n=17,m=8\),

\[
 N_6=728,qquad D_0=5940,qquad N_6D_0=4,324,320.
 \tag{2.5}
\]

The last number is exactly the turn-option census in the compact
depth-three quotient master.  Thus (1.1) parametrizes that complete host,
not a strict subcatalogue.

## 3. Quotienting and removing the true within-orbit exceptions

Call an atom **simple aperiodic** if all seven resources are aperiodic and
the two resources in each repeated rank lie in different rotation orbits.

For a rank-\(r\) set \(X\), the condition

\[
 |X\triangle(X+t)|=2
\]

for some nonzero rotation \(t\) has at most

\[
 n^3 2^{n/2}
\]

solutions over all ranks, up to an immaterial polynomial refinement.  The
number of periodic subsets is at most (n2^{n/2}).  These are the exact
exceptional forms from the direct-necklace audit.

Each failure of simplicity in (1.1) either touches a periodic resource or
makes one of

\[
 S,T;\qquad S+a,H;\qquad R^-,R^+
\]

a Johnson-adjacent rotation pair.  By Lemma 2.1, the number of discarded
labelled atoms is therefore

\[
 O(n^3 2^{n/2}D_0)
   =o\!\left(\binom n{m-2}D_0\right).
 \tag{3.1}
\]

Every remaining atom has a free orbit of size \(n\), and every one of its
seven resource incidences also quotients without folding.

## 4. A positive-density owner-rainbow cross-orbit packing

Form a seven-uniform hypergraph \(\mathcal H\).  Its vertices are the
rotation orbits of resources at ranks \(m-2,m-1,m,m+1\), and every simple
aperiodic atom orbit is one hyperedge containing its seven resources.

### Theorem 4.1 (cross-orbit rainbow hypermatching)

The hypergraph \(\mathcal H\) has a matching of size

\[
 \boxed{
 |M|\ge
 \frac{(1-o(1))\mathsf N_{m-2}D_0}
      {4D_0+4D_1+5D_2}
 \ge (1/13-o(1))\mathsf N_{m-2}.}
 \tag{4.1}
\]

Every selected bridge joins two different bottom-chain orbits, uses two
different rank-\((m-1)\) target orbits and two different root orbits, and
has a different owner orbit from every other selected bridge.

#### Proof

By (3.1), \(\mathcal H\) has

\[
 (1-o(1))\mathsf N_{m-2}D_0
\]

edges.  A bottom-resource orbit has degree at most (2D_0), a
rank-\((m-1)\) resource at most \(2D_1\), a root at most \(2D_2\), and an
owner at most \(D_2\).

Greedily select one hyperedge and delete every intersecting hyperedge.  One
selection deletes at most

\[
 2(2D_0)+2(2D_1)+2(2D_2)+D_2
 =4D_0+4D_1+5D_2
\]

edges.  Iteration proves the first inequality in (4.1), and (2.4) proves
the second.  The hypergraph matching condition is exactly the displayed
resource-disjointness.  \(\square\)

### Corollary 4.2 (positive-fraction serialization)

The selected atoms form pairwise resource-disjoint two-chain serializations
and reduce the number of prospective chain components by

\[
 (1/13-o(1))\mathsf N_{m-2}.
\]

Since

\[
 \frac{\mathsf N_{m-2}}{\mathsf N_m}
 =\frac{m(m-1)}{(m+2)(m+3)}=1-o(1),
\]

this is also a 
\((1/13-o(1))\)-fraction of the middle-root quotient chains.

Thus cross-orbit literal bridges exist at positive density even though
within-orbit bridges occur on only an exponentially small fraction of
necklaces.

This corollary is prospective.  To obtain the exact necklace-SCD selector,
the four partial containment matchings supplied by the selected two-chain
fragments must extend over the residual rank-\((m-2,m-1,m)\) quotient
graphs.  Theorem 4.1 does not assert that residual Hall property.

### Corollary 4.3 (explicit (k=17) lower bound)

At (n=17,m=8), the complete quotient bridge host contains a
seven-resource matching of at least (77) cross-orbit atoms.

#### Proof

Every nontrivial subset orbit is free because (17) is prime.  For one
nonzero rotation step, a rank-(r) set is Johnson adjacent to its translate
only when it is one cyclic interval in that step order.  Hence at each rank
there are at most

\[
 17\cdot16
\]

bad named sets, or at most (16) bad necklace orbits.

For (m=8),

\[
 D_0=5940,qquad D_1=3780,qquad D_2=3024.
\]

The three possible internal folds therefore remove at most

\[
 16(D_0+D_1+D_2)=203,904
\]

of the (4,324,320) quotient atoms.  At least (4,120,416) simple atoms
remain.  One greedy selection deletes at most

\[
 4D_0+4D_1+5D_2=54,000
\]

atoms, so the matching has size at least

\[
 \left\lceil\frac{4,120,416}{54,000}\right\rceil=77.
\]

\(\square\)

## 5. The general-depth bounded-state renewal bridge

Let a full depth-\(d\) age flag at a rank-\(m\) root be the ordered
partition

\[
 Q=C_0\mathbin{\dot\cup}\cdots\mathbin{\dot\cup}C_{d-1}.
\]

Choose

\[
 \alpha\in C_{d-1},\qquad \beta\notin Q,
\]

and define

\[
 \begin{aligned}
 Q'&=Q-\alpha+\beta,\\
 C'_0&=(C_{d-1}-\alpha)+\beta,\\
 C'_{i+1}&=C_i\qquad(0\le i<d-1).
 \end{aligned}
 \tag{5.1}
\]

### Theorem 5.1 (renewal bridge and its exact invariant)

Equation (5.1) is a literal age-compatible Johnson transition with owner

\[
 Q\cup\{\beta\}.
\]

If (c_i=|C_i|), its age-composition action is

\[
 (c_0,c_1,\ldots,c_{d-1})
 \longmapsto
 (c_{d-1},c_0,\ldots,c_{d-2}).
 \tag{5.2}
\]

Consequently the cyclic orbit of the composition vector is invariant under
all renewal bridges, and every renewal-only directed cycle has length
divisible by the period of that composition.  Apart from exponentially few
roots, (5.1) is cross-orbit.

#### Proof

The departure \(\alpha\) lies in the oldest class.  For every
(0\le i<d-1), the new class (C'_{i+1}) is exactly the surviving old
class \(C_i\).  The remaining old-oldest coordinates are refreshed together
with the newborn \(\beta\), giving \(C'_0\).  These are precisely the
literal age-transition equations.  Taking cardinalities gives (5.2).

Every step rotates the composition vector, proving the invariant and cycle
period statement.  The roots \(Q,Q'\) are Johnson adjacent; if they lie in
one rotation orbit then \(Q\) is one of the exceptional adjacent-rotation
sets counted in Section 3.  \(\square\)

Theorem 5.1 is a genuine bounded-state bridge for arbitrary \(d\).  It also
identifies why it is not a complete general-\(d\) serializer: a static SCD
selector may use many age-composition necklaces, while renewal bridges
cannot move between them.  A second bridge which changes composition, or a
selector concentrated in one composition orbit, is necessary.

## 6. The maximal star host has an exact fractional factor

Now use the full-piece star normal form.  Fix a bottom rank \(s\), put

\[
 v=n-s+1,
\]

and assume \(d<v\).  Let a maximal star packet be specified by

* a core (Q\in\binom{[n]}{s-1}); and
* an oriented cyclic order \(\pi\) of the \(v\) labels outside \(Q\).

The packet contains the \(v\) targets

\[
 Q\cup I
\]

at every depth \(j=1,\ldots,d\), where \(I\) runs through the cyclic
\(j\)-intervals of \(\pi\).

There are

\[
 |\mathcal P|=\binom n{s-1}(v-1)!
 \tag{6.1}
\]

oriented packets.  A fixed rank-\((s+j-1)\) target lies in exactly

\[
 E_j=\binom{s+j-1}{j}\,j!\,(v-j)!
 \tag{6.2}
\]

packets: choose its core \(Q\), then contract its \(j\) private labels to
one cyclic block and order that block internally.

Double counting gives the exact identity

\[
 |\mathcal P|v=\binom n{s+j-1}E_j
 \qquad(1\le j\le d).
 \tag{6.3}
\]

When the whole rank band lies in the lower half, the layer sizes in (6.3)
increase with \(j\), so \(E_1\) is maximal.  Uniform packet weight
\(1/E_1\) is therefore a fractional matching of size

\[
 \frac{|\mathcal P|}{E_1}
 =\frac1v\binom ns
 =\frac1s\binom n{s-1}.
 \tag{6.4}
\]

The first expression is also the bottom-layer capacity bound, so (6.4) is
fractionally optimal.  The star-factor obstruction is integral, not scalar.

## 7. An integral bottom-disjoint star packing at the correct scale

Identify the ground set with \(\mathbb Z_n\) and colour a core by

\[
 \kappa(Q)=\sum_{x\in Q}x\pmod n.
 \tag{7.1}
\]

### Theorem 7.1 (modular-sum bottom packing)

Some colour class \(\mathcal Q_c\) has size at least

\[
 |\mathcal Q_c|\ge\frac1n\binom n{s-1}.
 \tag{7.2}
\]

The complete bottom stars

\[
 \{Q+x:x\notin Q\},\qquad Q\in\mathcal Q_c,
\]

are pairwise disjoint.  Hence arbitrary maximal cyclic orders on these
cores give (\Theta(\binom ns/n)) star packets which serialize at least

\[
 |\mathcal Q_c|v
 \ge \frac{s}{n}\binom ns
 \tag{7.3}
\]

different full pieces with no bottom-target collision.

#### Proof

If two distinct \((s-1)\)-cores are Johnson adjacent, then

\[
 Q'=Q-x+y
\]

for distinct residues \(x,y\), so

\[
 \kappa(Q')-\kappa(Q)=y-x\not\equiv0\pmod n.
\]

Thus every colour class is independent in \(J(n,s-1)\).  Two complete
bottom stars intersect exactly when their cores are Johnson adjacent, so
the stars are disjoint.  Pigeonhole gives (7.2), and

\[
 \binom n{s-1}(n-s+1)=s\binom ns
\]

gives (7.3).  \(\square\)

For near-central \(s\), (7.3) is a positive constant fraction of the
rank-\(s\) layer.  In particular its packet count is already on the
\(W/n\) scale required by the theta-reset ledger.  No endpoint-count
obstruction remains on the bottom row.

The modular-sum construction is a named construction.  It need not be
rotation-invariant: translating a core by \(t\) changes its colour by
\((s-1)t\pmod n\).  This is harmless for a single PBBS chronology, but a
fully equivariant star factor would require a separate independent-set
theorem in the quotient Johnson graph.

## 8. Exact higher-depth collision law

The modular-sum packing does not automatically extend above the bottom row.

Let packets \((Q,\pi)\) and \((Q',\pi')\) share a target at depth \(j\):

\[
 Q\cup I=Q'\cup I',
 \tag{8.1}
\]

where \(I,I'\) are cyclic \(j\)-intervals in the respective complements.
Put

\[
 A=Q\setminus Q',\qquad B=Q'\setminus Q,
 \qquad h=|A|=|B|.
\]

### Lemma 8.1 (balanced exchange collision criterion)

Equation (8.1) holds if and only if

\[
 h\le j,qquad
 I=B\mathbin{\dot\cup}C,qquad
 I'=A\mathbin{\dot\cup}C
 \tag{8.2}
\]

for one \((j-h)\)-set \(C\) disjoint from \(Q\cup Q'\), with both displayed
sets occurring as cyclic intervals in their packet orders.

If \(\kappa(Q)=\kappa(Q')\), then additionally

\[
 \sum_{a\in A}a\equiv\sum_{b\in B}b\pmod n,
 \tag{8.3}
\]

and (h\ne1).

#### Proof

Taking the parts of (8.1) outside (Q\cap Q') forces every element of
\(B\) into \(I\), every element of \(A\) into \(I'\), and leaves the same
common extra set \(C\) on both sides.  This is exactly (8.2), and the
converse is immediate.  Equality of the modular core colours gives (8.3).
For \(h=1\), (8.3) equates two distinct residues, impossible.  \(\square\)

At depth two, every collision inside one modular colour class is therefore
exactly a balanced two-exchange

\[
 Q'=Q-A+B,qquad |A|=|B|=2,qquad \sum A=\sum B,
 \tag{8.4}
\]

for which \(B\) is an edge of the complement cycle of \(Q\) and \(A\) is an
edge of the complement cycle of \(Q'\).

This obstruction is real.  For example, whenever the four residues are
available,

\[
 A=\{0,3\},\qquad B=\{1,2\}
\]

have equal sum.  If the two packet cycles use \(B\) and \(A\) as adjacent
pairs, respectively, the two packets share the depth-two target

\[
 Q\cup B=Q'\cup A.
\]

Thus the implication

\[
 \text{bottom-disjoint common-core stars}
 \Longrightarrow
 \text{all-depth target-disjoint stars}
\]

is false.

## 9. Exact remaining theorems

Two correlation rows remain.

### 9.1 Quotient-SCD bridge extension

Choose a positive-density hypermatching from Theorem 4.1 so that its two
partial containment matchings extend over the unused rank
\((m-2,m-1,m)\) quotient resources.  Then choose the remaining state edges
and voltage so the resulting factor has few components.  The cross-orbit
atoms already carry distinct owner colours; the missing statement is
residual Hall/serialization, not local bridge supply.

### 9.2 Target-disjoint cyclic-star factor

Choose (\Theta(W/n)) cores and one complement cycle on each so that none
of the balanced-exchange coincidences (8.2) occurs at any depth
(2\le j\le d), while retaining the PBBS owner-envelope and Euler tickets.
Theorem 7.1 solves its bottom projection, and (6.4) solves its fractional
capacity.  Lemma 8.1 is the exact integral conflict system.

The ordinary cyclic-quotient Johnson matching is therefore only the first
row.  The missing star factor is a simultaneous Hamilton-cycle selection in
the complement fibres avoiding the balanced-exchange conflict graph.

## 10. Audit and scope

The internal consistency checks are:

1. At \(m=8\), (2.2) gives \(728\cdot5940=4,324,320\), exactly the
   independently frozen compact quotient turn census.
2. The seven resource degrees in (2.3) reproduce the same tail/head
   symmetry as the exact depth-three state law.
3. The direct-necklace obstruction is used only to discard orbit-folded
   atoms; no within-orbit edge is asserted.
4. Equation (6.3) independently checks the packet and target degree counts
   at every depth.
5. The modular-sum construction is exact for every \(n\), not only prime
   \(n\).

Proved here:

* a complete depth-three bridge-atom normal form;
* a positive-density root/target/owner-disjoint cross-orbit packing;
* a literal general-depth renewal bridge and its exact composition
  invariant;
* exact fractional maximal-star capacity;
* an integral bottom-disjoint maximal-star family at the correct (W/n)
  packet scale; and
* the exact higher-depth balanced-exchange collision criterion.

Not proved here:

* extension of the positive-density bridge bank to the exact quotient SCD
  selector;
* a connected or nonzero-voltage quotient factor;
* avoidance of all higher-depth star collisions;
* PBBS owner-envelope compatibility; or
* \(\nu(k)\le B(k)+O(1)\).
