# Diverse-order Johnson exchanges and the nested harmonic gate

Date: 2026-07-26

Method: pure mathematics only.  No computation, solver, common-order
syndrome assumption, probabilistic packing, or web input is used.

## 0. Result

This note constructs the missing support-profile trade at the abstract
and packet levels, determines its minimum derivative size, and gives an
exact criterion for simultaneous all-depth span.

### Local Johnson exchange

Swapping two adjacent directions \(a,b\) in a cyclic order changes
exactly two depth-\(q\) supports.  Its derivative is

\[
 \rho_q(L,R;a,b)
   =e_{L+b}+e_{R+a}-e_{L+a}-e_{R+b},                 \tag{0.1}
\]

where \(L,R\) are the \((q-1)\)-sets immediately before and after the
swapped pair.  It preserves every direction degree.

The minimum nonzero integral support derivative with zero total and zero
direction degree has \(\ell^1\)-norm \(4\), attained by (0.1).  Because
literal faces occur in antipodal pairs, its minimum literal lift changes
eight faces per sign.  Lower and upper lifts are the same under the
empty/full identification.

For \(r\ge3q-1\), the exchanges (0.1), over all cyclic contexts,
generate the complete integral kernel of the point-versus-\(q\)-set
incidence matrix.  Thus the *ideal support lattice* has index one.

### Certified owner trade

If \(F\) is a compiler factor on a physical \(Q_r\) packet and
\(\tau\in\mathfrak S_r\) is a coordinate permutation, then

\[
                              F\longleftrightarrow\tau F            \tag{0.2}
\]

is an exact owner-preserving trade on the same \(2^r\) owners.  Its
depth-\(q\) derivative is an integral sum of Johnson exchanges, preserves
direction degree and antipodal pairing, and is legal with arbitrary
diverse packet orders.

The smallest abstract derivative has eight literal faces per sign; the
smallest certified direction-changing cross-parent primitive is one
\(Q_{R+1}\) slab, of mass \(2^{R+1}\).  It cannot itself be a Johnson
exchange because its direction marginal is nonzero.  Zero-direction
multi-support trades first occur as a two-slab labelled parallel-edge
digon, when two owner-disjoint copies are available, or as a four-slab
rectangle in the simple compatibility graph.  Their owner masses are
\(2^{R+2}\) and \(2^{R+3}\), respectively.

### Simultaneous nesting

Support span at separate depths is insufficient.  In the direct sum over
\(q\le H\), the \(j\)-th Johnson harmonic representation occurs with
multiplicity \(H-j+1\).  The conjugate trades span all separate-depth
kernels simultaneously if and only if the diverse template library has
full multiplicity rank in every harmonic level \(2\le j\le H\).

Failure at one level gives a stable cross-depth linear invariant
annihilating every coordinate-conjugate packet trade and every bundle of
such trades, regardless of size.  This is the exact remaining audit for
the certified compiler library.

### Residues and compound holonomy

A slab move changes the signed depth-\(q\) direction histogram by

\[
                         2qg_R(e_e-e_i).
\]

Hence the coordinate residues, component sums,
\(z_q^\epsilon-qz_1^\epsilon\), and \(z_q^+-z_q^-\) are exact
invariants.  More sharply, a compound move closes at depth one if and
only if it closes at every depth and both signs.

The decorated circulation module is generated integrally by labelled
parallel-edge digons and lifts of a simple-graph cycle basis.  Therefore
the smallest possible nonflat holonomy uses two slabs; if every digon is
flat, the actual local macroblock graph at \(d\ge5\) forces any nonflat
holonomy to appear already on a four-slab rectangle.  Vanishing
curvature on these generators is a complete
no-go: every compound slab circuit then has zero literal derivative.
For energy descent, every circuit through four slabs is exactly a digon,
a carrier rectangle, or a sum of two digons; the last topology must be
audited separately because energy is quadratic rather than linear.

## 1. Support profiles of a packet factor

Let \(F\) be a factor of \(Q_r\) into isometric \(C_{2r}\)'s.  For
\(q<r\), let

\[
 c_q^F(J)
  ={1\over2}|\{\text{depth-\(q\) starts whose direction support is }J\}|
                                                              \tag{1.1}
\]

for \(J\in\binom{[r]}q\).  The division by two quotients the forced
antipodal face pairing.  Hence \(c_q^F(J)\in\mathbb Z_{\ge0}\).

Let

\[
 M_{1,q}:\mathbb Z^{\binom{[r]}q}\longrightarrow\mathbb Z^r,\qquad
 e_J\longmapsto\mathbf1_J.                           \tag{1.2}
\]

Depth-\(q\) direction regularity gives

\[
 M_{1,q}c_q^F={qg_r\over2}\mathbf1,\qquad
                         g_r={2^r\over r}.            \tag{1.3}
\]

For a coordinate permutation \(\tau\),

\[
          \delta_q(\tau;F)=c_q^{\tau F}-c_q^F
                          =\tau c_q^F-c_q^F           \tag{1.4}
\]

satisfies

\[
                         M_{1,q}\delta_q(\tau;F)=0.   \tag{1.5}
\]

It also has total zero, already implied by (1.5).

## 2. Adjacent order swap

Take a cyclic direction order and suppose \(a,b\) occupy adjacent
positions.  Let \(L\) be the \(q-1\) directions immediately preceding
\(a\), and \(R\) the \(q-1\) directions immediately following \(b\).
Assume \(2q<r\), as holds uniformly for \(q\le H=o(r)\).

All length-\(q\) windows containing both or neither of \(a,b\) retain
the same support after the swap.  Exactly two windows contain one but not
the other.  Before the swap their supports are

\[
                              L+a,\qquad R+b,         \tag{2.1}
\]

and afterwards they are

\[
                              L+b,\qquad R+a.         \tag{2.2}
\]

Thus the new-minus-old derivative is exactly (0.1).

The four sets in (0.1) have equal total mass and equal point incidence:

\[
 \mathbf1_{L+b}+\mathbf1_{R+a}
      =\mathbf1_{L+a}+\mathbf1_{R+b}.                \tag{2.3}
\]

Hence the trade preserves the fixed direction-degree vector.

## 3. Minimum derivative size

### Lemma 3.1 (minimum support trade)

For \(2\le q\le r-2\), every nonzero
\(z\in\ker_{\mathbb Z}M_{1,q}\) has

\[
                              \|z\|_1\ge4.            \tag{3.1}
\]

Equality is attained by (0.1).

#### Proof

Since every column of \(M_{1,q}\) has sum \(q\),
\(M_{1,q}z=0\) implies \(\mathbf1^Tz=0\).  A nonzero vector of
\(\ell^1\)-norm two would be \(e_J-e_K\).  Its point incidence vanishes
only if \(\mathbf1_J=\mathbf1_K\), hence \(J=K\), a contradiction.
Norm three is impossible because a zero-total integer vector has even
\(\ell^1\)-norm.  Formula (2.3) shows that (0.1) has norm four and lies
in the kernel. \(\square\)

Each support occurrence represents an antipodal pair of literal faces.
Therefore the literal lower derivative of (0.1) has norm eight.  The
upper derivative has norm eight and is identified term by term with the
lower derivative.

## 4. Integral generation of the support lattice

### Theorem 4.1 (Johnson-square generation)

For \(2\le q<r/3\), the adjacent-context exchanges (0.1) generate

\[
                         \ker_{\mathbb Z}M_{1,q}.     \tag{4.1}
\]

#### Proof

The integral kernel of the incidence map on uniform \(q\)-sets is
generated by symmetric exchanges

\[
 e_A+e_B-e_{A-a+b}-e_{B-b+a},                       \tag{4.2}
\]

where \(a\in A\setminus B\), \(b\in B\setminus A\).  One proof views
the positive and negative parts as two bipartite incidence graphs with
the same degrees and transforms one to the other by \(2\times2\)
switches.

Write

\[
 L=A-a,\qquad R=B-b.
\]

Then (4.2), up to sign, is \(\rho_q(L,R;a,b)\).  If \(L\cap R\ne
\varnothing\), choose a fresh \((q-1)\)-set \(C\) disjoint from
\(L\cup R\cup\{a,b\}\).  This is possible when \(r\ge3q-1\).  The
telescoping identity

\[
 \rho_q(L,R;a,b)
   =\rho_q(L,C;a,b)+\rho_q(C,R;a,b)                  \tag{4.3}
\]

reduces to exchanges with disjoint left and right contexts.

When \(L,R,\{a,b\}\) are disjoint, place the elements of \(L\), then
\(a,b\), then the elements of \(R\) consecutively in a cyclic order,
with arbitrary unused directions filling the remaining positions.
The adjacent swap calculation in Section 2 realizes the required
exchange.  Hence all generators (4.2) lie in the lattice generated by
(0.1). \(\square\)

Thus there is no further integral support invariant at one fixed depth:
total mass and direction degree are complete.

## 5. Owner-preserving packet realization

### Theorem 5.1 (coordinate-conjugate compiler trade)

Let \(F\) be any certified compiler factor on one physical \(Q_r\)
packet, and let \(\tau\) be any permutation of its physical directions.
Then \(F\) and \(\tau F\) are spanning degree-two factors of the same
owner set.  Replacing one by the other is an exact owner trade with no
seam or collar.

At every \(q<r\), its support derivative lies in
\(\ker_{\mathbb Z}M_{1,q}\), preserves antipodal literal-face pairing,
and has identical lower and upper derivatives under empty/full
identification.

#### Proof

A coordinate permutation is an automorphism of \(Q_r\), so it maps a
spanning factor to a spanning factor on the same vertex set.  Both shores
therefore use every owner exactly once in degree two.  Equations
(1.4)--(1.5) give the support assertion.  Coordinate automorphisms
commute with antipodal complementation, and the lower/upper face identity
holds start by start. \(\square\)

If \(c_q^F\) is not invariant under the full symmetric group, some
transposition has nonzero derivative.  If it is invariant, it is constant
on \(\binom{[r]}q\), so the packet is already perfectly balanced at the
support-profile level for that depth.

By Theorem 4.1, the derivative of (0.2) decomposes integrally into the
minimal exchanges (0.1).  This decomposition is a lattice ledger; it
does not split one physical packet trade into owner-disjoint constant-size
trades.

## 5A. Cross-parent slab circulations

We now incorporate the exact primitive from
`MATH_THEOREM_RANK_TWISTED_CROSS_PARENT_QR_PLUS_ONE_SLAB_TRADE_20260726.md`.
Write \(s=2^R\), \(g_R=2^R/R\).  A primitive cross-parent slab replaces
an old active direction \(i\) by a cross-parent direction \(e\) on one
\(Q_{R+1}\) owner slab.  Denote its signed literal derivative at colour
\(c=(\pm,q)\) by

\[
                         \Delta_c(i\to e).            \tag{5A.1}
\]

The audited primitive gives

\[
\begin{aligned}
 \sum_T\Delta_c(i\to e)(T)&=0,\\
 \|\Delta_c(i\to e)\|_1&\le4s,\\
 \operatorname{dir}_q\Delta_c(i\to e)
                 &=2qg_R(e_e-e_i).                  \tag{5A.2}
\end{aligned}
\]

It is an exact two-packet-versus-two-packet owner trade, crosses two
rank-twisted parent status coordinates, and accepts independent diverse
compiler labels on all four packets.

Let \(G_{\rm cp}\) be the compatibility graph whose left vertices are
old rank-frame directions \(i\), whose right vertices are admissible
nonmatching cross-parent directions \(e\), and whose edges are available
Hamming-two slab types.  The target derivative depends not only on the
underlying edge but also on the compiler label and on the physical slab
copy.  We therefore replace \(G_{\rm cp}\) by its decorated multigraph
\(\widetilde G_{\rm cp}\).  A decorated edge

\[
                         \widetilde a=(i,e;\lambda,\omega)          \tag{5A.3}
\]

records the diverse compiler label \(\lambda\) and owner-slab tag
\(\omega\); the boundary forgets both decorations.  Take an integer
signed decorated-edge vector

\[
                         z\in\mathbb Z^{E(\widetilde G_{\rm cp})}.  \tag{5A.4}
\]

Fix a finite carrier ground set \(\Omega\) containing every old and
cross-parent direction label under consideration, and put
\(n=|\Omega|\).  Every packet support profile is extended by zero to
\(\binom{\Omega}{q}\); write \(M_{1,q}^{\Omega}\) for its point-incidence
map.  This enlargement is essential: one slab uses \(R\) directions,
but its old and new shores together use \(R+1\).

Orient every graph edge from its old direction to its cross direction.
The aggregate direction derivative is

\[
             \operatorname{dir}_q\Delta_c(z)
                    =2qg_R\,\widetilde\partial z,    \tag{5A.5}
\]

where \(\widetilde\partial\) is the vertex-edge boundary map after
forgetting the decorations.

### Theorem 5A.1 (owner-preserving multi-support circulation)

If \(z\in\ker_{\mathbb Z}\widetilde\partial\) has an embedding in
which its slab copies are owner-disjoint, then the disjoint union of its
oriented cross-parent slab trades is an exact owner-preserving trade
whose direction derivative is zero for both signs and every
\(q\le H\).  It preserves antipodal face pairing and the common
lower/upper empty/full identification.

Its literal derivative is

\[
                         \Delta_c(z)
                    =\sum_{\widetilde a\in E(\widetilde G_{\rm cp})}
                       z_{\widetilde a}\Delta_c(\widetilde a),     \tag{5A.6}
\]

and need not vanish when the slab edges use diverse compiler labels.

#### Proof

Each primitive is owner-preserving on its own slab, and the slabs are
owner-disjoint, so their disjoint union is owner-preserving.  Equation
(5A.5) and \(\widetilde\partial z=0\) give zero direction degree simultaneously
at all depths.  The antipodal and sign identities hold term by term and
therefore survive summation.  Formula (5A.6) is additivity of literal
target ledgers. \(\square\)

If every occurrence of a carrier direction uses one common compiler
template with one consistent relabeling, a graph cycle can telescope to
zero at the support-profile level.  Independent diverse-order labels
prevent that forced telescope.  They are therefore essential, not a
cosmetic enlargement.

### Minimal circulation size

The graph \(G_{\rm cp}\) is bipartite by definition.  Its nonzero simple
circulations are generated by even cycles.  If four compatible directions
form a rectangle

\[
                   i-e-j-f-i,                       \tag{5A.7}
\]

the alternating four-edge vector gives the exact trade

\[
 \Delta_c(i\to e)+\Delta_c(j\to f)
 -\Delta_c(i\to f)-\Delta_c(j\to e).                \tag{5A.8}
\]

It uses four \(Q_{R+1}\) slabs, hence

\[
                         4\cdot2^{R+1}=2^{R+3}       \tag{5A.9}
\]

owners, has zero interface leave, and satisfies

\[
                         \|\Delta_c\|_1\le16s         \tag{5A.10}
\]

for every sign and depth.  A four-cycle is the minimum nonzero simple
circulation in a simple bipartite graph.

If two owner-disjoint copies of the same compatibility edge are
available, one may orient them oppositely and use different compiler
labels.  This labelled digon has two slabs, owner mass \(2^{R+2}\), and
\(\ell^1\)-bound \(8s\).  Its unlabelled carrier circulation is trivial;
all nonzero support motion comes from the difference of its compiler
templates.  Thus:

* minimum simple cross-parent circulation: four slabs;
* minimum labelled repeated-edge circulation: two slabs;
* minimum ideal support derivative: four supports, or eight literal
  antipodal faces per sign.

These are different notions of minimality.

### Corollary 5A.2 (physical carrier graph reduction)

For every depth \(q\), define the decorated cycle-image map

\[
 \Phi_q:\ker_{\mathbb Z}\widetilde\partial
        \longrightarrow\ker_{\mathbb Z}M_{1,q}^{\Omega}           \tag{5A.11}
\]

by taking the antipodal support profile of (5A.6).  The formal
cross-parent multi-support lattice is \(\operatorname{im}\Phi_q\).
Its elements having owner-disjoint embeddings are literal legal trades;
proving that enough such embeddings exist is a separate packing
question.

Theorem 4.1 says the desired codomain is generated by Johnson squares.
Thus cross-parent slabs span the full fixed-depth support lattice exactly
when their labelled cycle derivatives realize those square generators.
The parent Hamming-two geometry supplies the owner-preserving
circulations; it does not by itself prove surjectivity of \(\Phi_q\).

## 6. Literal orientation lattice

Let \(\mathcal Y_J\) be the antipodal orientation classes

\[
 \mathcal Y_J
   =\mathbb F_2^{[r]\setminus J}/(y\sim\bar y).       \tag{6.1}
\]

An antipodal literal face-pair vector is

\[
 x=(x_{J,[y]})_{J,[y]}
 \in\bigoplus_{J\in\binom{[r]}q}\mathbb Z^{\mathcal Y_J}.          \tag{6.2}
\]

Let \(p\) forget orientation:

\[
                         (px)_J=\sum_{[y]}x_{J,[y]}. \tag{6.3}
\]

The complete abstract degree-preserving face lattice is

\[
 \mathcal K_q^{\rm face}
   =\{x:M_{1,q}px=0\}.                               \tag{6.4}
\]

It has an index-one generator description:

1. lift every support square (0.1) to arbitrary orientation classes;
2. for fixed \(J\), use orientation transfers

\[
                         e_{J,[y]}-e_{J,[y']}.        \tag{6.5}
\]

Indeed, apply Theorem 4.1 to \(px\), subtract lifted support squares,
and then the remaining vector has zero sum separately in every
\(\mathcal Y_J\), where it is generated by (6.5).

Thus the *abstract literal antipodal lattice* also has index one.  What
is not proved is that the physical packet-conjugation derivatives realize
the individual generators (6.5) and the independently oriented lifts of
(0.1).

## 7. Rational span of a diverse template library

At one fixed depth, the rational permutation module on \(q\)-sets has
the multiplicity-free decomposition

\[
 \mathbb Q^{\binom{[r]}q}
   \cong\bigoplus_{j=0}^q S^{(r-j,j)}.               \tag{7.1}
\]

The constant and point-incidence space is the sum of the \(j=0,1\)
terms.  Therefore

\[
 \ker_{\mathbb Q}M_{1,q}
   \cong\bigoplus_{j=2}^q S^{(r-j,j)}.               \tag{7.2}
\]

Let \(F_1,\ldots,F_s\) be diverse compiler templates, and let
\(\mathcal T_q\) be the rational span of all conjugate differences

\[
 \sigma c_q^{F_\alpha}-c_q^{F_\alpha},
 \qquad \sigma\in\mathfrak S_r.                     \tag{7.3}
\]

### Theorem 7.1 (fixed-depth harmonic criterion)

\(\mathcal T_q=\ker_{\mathbb Q}M_{1,q}\) if and only if, for every
\(2\le j\le q\), at least one template \(c_q^{F_\alpha}\) has nonzero
projection to \(S^{(r-j,j)}\).

#### Proof

Each Specht summand in (7.1) is irreducible and occurs once.  The orbit
of a nonzero vector in an irreducible summand spans that summand.  A
missing projection is annihilated by every conjugate difference, while
one nonzero projection supplies the whole summand. \(\square\)

If the criterion holds, the integral lattice generated by the conjugate
trades has finite index in the ideal support lattice.  Theorem 7.1 alone
does not bound that Smith index; real span must not be confused with an
\(o(W)\) repair theorem.

## 8. Simultaneous nesting and the stable harmonic invariant

Now put

\[
 \mathcal K_{\le H}
   =\bigoplus_{q=2}^H\ker_{\mathbb Q}M_{1,q}.         \tag{8.1}
\]

For fixed \(j\), the irreducible module \(S^{(r-j,j)}\) occurs once at
each depth \(q=j,j+1,\ldots,H\).  Hence its isotypic component is

\[
 S^{(r-j,j)}\otimes\mathbb Q^{H-j+1}.                \tag{8.2}
\]

Project every full template profile

\[
                         C^{F_\alpha}
                  =(c_2^{F_\alpha},\ldots,c_H^{F_\alpha})          \tag{8.3}
\]

to (8.2).  Let \(U_j\subseteq\mathbb Q^{H-j+1}\) be the smallest
multiplicity subspace for which all these projections lie in

\[
                         S^{(r-j,j)}\otimes U_j.      \tag{8.4}
\]

### Theorem 8.1 (common-depth span criterion)

The rational span of all coordinate-conjugate trades from the diverse
template library equals \(\mathcal K_{\le H}\) if and only if

\[
                         U_j=\mathbb Q^{H-j+1}
                  \qquad(2\le j\le H).               \tag{8.5}
\]

If (8.5) fails, every nonzero functional in

\[
                         U_j^\perp                   \tag{8.6}
\]

combined with a \(j\)-th harmonic functional gives a nonzero stable
linear invariant annihilating every legal coordinate-conjugate trade and
every Minkowski sum of such trades.

#### Proof

An invariant submodule of the isotypic component (8.2) has the form
\(S^{(r-j,j)}\otimes U\), because the Specht module is absolutely
irreducible.  The module generated by all template projections is
therefore exactly the space in (8.4).  It fills (8.2) precisely under
(8.5).  The annihilator when \(U_j\) is proper is
\((S^{(r-j,j)})^*\otimes U_j^\perp\), proving the invariant claim.
\(\square\)

This criterion incorporates simultaneous nesting.  Separate success of
Theorem 7.1 at every \(q\) does not imply (8.5), because the same
template trade supplies all depths at once.

## 8A. The exact cross-parent cycle-image gate

The slab primitive makes the preceding harmonic obstruction physical,
but it changes the domain.  Individual slab edges are not admissible
Johnson trades: only decorated circulations are.  Put

\[
 \Phi_{\le H}=\bigoplus_{q=2}^H\Phi_q,
 \qquad
 \Lambda^{\rm cp}_{\le H}
   =\operatorname{im}\Phi_{\le H}
   \subseteq\bigoplus_{q=2}^H\ker_{\mathbb Z}M_{1,q}^{\Omega}.     \tag{8A.1}
\]

The same decorated circulation is used in every coordinate of
\(\Phi_{\le H}\).  Thus (8A.1), rather than the separate images
\(\operatorname{im}\Phi_q\), is the correct nested lattice.

Let \({\cal C}_{\rm cp}\) be the family of all labelled digons and even
cycles allowed by the cross-parent atlas, with all available compiler
coordinate conjugates.  For \(C\in{\cal C}_{\rm cp}\), write

\[
                         D(C)=\Phi_{\le H}(C).                       \tag{8A.2}
\]

### Theorem 8A.1 (cross-parent harmonic criterion)

For each \(j\ge2\), project the rational span of the actual vectors
\(D(C)\) to the \(j\)-th isotypic component

\[
 S^{(n-j,j)}\otimes\mathbb Q^{H-j+1}.                              \tag{8A.3}
\]

The cross-parent cycles span the complete all-depth rational support
kernel if and only if their projection equals (8A.3) for every
\(2\le j\le H\).

If the compiler conjugates make the family symmetric under
\(\mathfrak S_{\Omega}\), there is a uniquely determined smallest multiplicity
space \(U_j^{\rm cp}\) such that the projection lies in

\[
 S^{(n-j,j)}\otimes U_j^{\rm cp},                                  \tag{8A.4}
\]

and the condition becomes

\[
                         U_j^{\rm cp}=\mathbb Q^{H-j+1}
                         \quad(2\le j\le H).                        \tag{8A.5}
\]

If (8A.5) fails, any vector in
\((U_j^{\rm cp})^\perp\) tensored with a \(j\)-harmonic functional is
a stable invariant annihilating every cross-parent slab circulation,
regardless of the number of slabs or their owner placement.

#### Proof

Every legal primitive combination has zero direction marginal exactly
when its decorated edge vector is a circulation, by (5A.5).  Therefore
the legal support span is precisely the span of the vectors (8A.2), not
the span of individual edge derivatives.  Decompose this span into the
isotypic summands (8A.3).  It equals the whole kernel exactly when every
projected summand is full.  Under symmetric conjugation, Schur's lemma
puts each invariant subspace in the form (8A.4), and fullness is exactly
(8A.5).  The stated annihilator is the dual of the missing multiplicity
space. \(\square\)

This yields an exact integral formulation as well.  If
\(n\ge3H-1\), Theorem 4.1 on the ground set \(\Omega\) shows that
\(\Lambda^{\rm cp}_{\le H}\) equals the ideal all-depth support lattice
if and only if, for every \(q\le H\), every Johnson square placed in
depth \(q\) and zero in all other depths has an integral preimage under
\(\Phi_{\le H}\).  Full rational rank proves only finite Smith index.
A nonzero element of the Smith cokernel is a persistent congruence
obstruction which no number of slab circulations can remove.

There is a second, literal gate.  Let

\[
 \widehat\Phi_{\le H}:\ker_{\mathbb Z}\widetilde\partial
       \longrightarrow\bigoplus_{q=2}^H{\cal K}^{\rm face}_{q,\Omega}
                                                                        \tag{8A.6}
\]

retain the physical target identities and orientations.  Its support
projection is \(\Phi_{\le H}\).  Hence literal completeness requires
both

\[
 p\,\operatorname{im}\widehat\Phi_{\le H}
       =\bigoplus_{q=2}^H\ker_{\mathbb Z}M_{1,q}^{\Omega}          \tag{8A.7}
\]

and generation of the vertical orientation-transfer lattice
\(\ker p\) by elements of
\(\operatorname{im}\widehat\Phi_{\le H}\cap\ker p\).  Support
surjectivity alone does not imply the latter.

### Proposition 8A.2 (minimality within the slab calculus)

A single cross-parent slab cannot have zero direction derivative at any
positive depth.  In the decorated multigraph, a two-slab zero-direction
combination exists only as two parallel copies of the same underlying
edge with opposite signs.  If parallel copies are forbidden, three
slabs are impossible and four slabs are necessary; equality is attained
exactly by a compatible rectangle.

#### Proof

The first assertion follows from
\(2qg_R(e_e-e_i)\ne0\).  A two-edge circulation has the same two
endpoints with opposite orientations, so it is a parallel-edge digon.
After parallel edges are removed, every nonzero circulation in a simple
bipartite graph contains an even cycle of length at least four.  A
four-edge circulation has minimal support precisely when those edges
form a rectangle. \(\square\)

The proposition proves the minimum *carrier circulation* size.  It does
not say that a labelled digon or rectangle has the minimum Johnson
derivative: its compiler labels may move many supports, and derivatives
on physically disjoint exterior tags need not cancel target by target.

## 8B. Residue invariants and the minimal holonomy circuit

This section incorporates the exact slab-residue ledger from
`MATH_THEOREM_HAMMING2_SLAB_COLLISION_DERIVATIVE_AND_LOCAL_MINIMUM_GATE_20260726.md`
and the equivalent direction calculation in the slab-energy audit.

Let \(z_q^\epsilon\in\mathbb Z^\Omega\) be the direction-support
histogram at signed depth \((\epsilon,q)\).  Put

\[
                         \alpha_q=2qg_R.                            \tag{8B.1}
\]

For every signed decorated slab vector \(x\), the audited marginal is

\[
 \boxed{\Delta z_q^\epsilon=\alpha_q\widetilde\partial x.}         \tag{8B.2}
\]

### Theorem 8B.1 (complete projected residue ledger)

Every sequence of Hamming-two slab exchanges preserves:

1. each coordinate of \(z_q^\epsilon\) modulo \(\alpha_q\);
2. the sum of \(z_q^\epsilon\) on every connected component of
   \(G_{\rm cp}\);
3. \(z_q^\epsilon-qz_1^\epsilon\); and
4. \(z_q^+-z_q^-\).

Moreover, for a compound exchange \(x\), the following are equivalent:

\[
 \Delta z_1^+=0;
 \qquad \widetilde\partial x=0;
 \qquad
 \Delta z_q^\epsilon=0\quad\hbox{for every }q,\epsilon.            \tag{8B.3}
\]

Thus a decorated carrier circulation respects all four invariants in
the stronger sense of preserving every direction histogram exactly.

#### Proof

The first two assertions follow directly from (8B.2), since a graph
boundary has coordinate entries in \(\mathbb Z\) and has sum zero on
each component.  Since \(\alpha_q=q\alpha_1\),

\[
 \Delta(z_q^\epsilon-qz_1^\epsilon)
 =\alpha_q\widetilde\partial x
  -q\alpha_1\widetilde\partial x=0.
\]

The marginal (8B.2) is the same for both signs, proving the fourth
invariant.  Finally \(\alpha_1>0\), so depth-one closure is equivalent
to \(\widetilde\partial x=0\), which by (8B.2) is equivalent to closure
at every signed depth. \(\square\)

The theorem is important conceptually: the residues constrain which
histogram coset is reachable, but impose no further condition on a
closed compound correction.  Inside one coset, the remaining object is
the literal holonomy of the decorated cycle.

For a decorated oriented edge \(\widetilde a\), let

\[
 {\bf D}(\widetilde a)
   =\bigl(\Delta_{(\epsilon,q)}(\widetilde a)
      \bigr)_{\epsilon,q\le H}                                   \tag{8B.4}
\]

be its complete literal derivative.  For two decorations
\(\lambda,\mu\) of the same underlying edge \(a\), define the vertical
digon curvature

\[
 {\bf H}_{a;\lambda,\mu}
      ={\bf D}(a,\lambda)-{\bf D}(a,\mu).                          \tag{8B.5}
\]

For an oriented simple cycle \(C\), define its curvature by the signed
edge sum

\[
                         {\bf H}_C
                   =\sum_{a\in C}\operatorname{sgn}_C(a)
                                      {\bf D}(a,\lambda_a).         \tag{8B.6}
\]

### Theorem 8B.2 (integral holonomy generators)

The complete decorated circulation module is generated integrally by:

1. the parallel-edge digons (8B.5); and
2. lifts of an integral cycle basis of the simple graph \(G_{\rm cp}\).

Consequently its literal holonomy lattice is generated by (8B.5) and
(8B.6).  If the simple cycle lattice of \(G_{\rm cp}\) is generated by
rectangles, then labelled digons and four-slab rectangles generate the
entire compound slab lattice.

#### Proof

Choose one reference decoration on each underlying edge.  Given a
decorated circulation \(x\), sum its coefficients over the decorations
of each edge.  The resulting vector \(\bar x\) is an integral
circulation of the simple graph, so it is an integral sum of cycle-basis
vectors.  Lift those cycles using the reference decorations and subtract
them from \(x\).  The remainder has coefficient sum zero separately
over the decorations of every underlying edge.  It is therefore an
integral sum of differences between a decoration and the reference
decoration, namely parallel-edge digons.  Applying the homomorphism
\({\bf D}\) proves the holonomy statement. \(\square\)

### Corollary 8B.3 (sharp minimum and flatness obstruction)

The minimum number of slabs in a nonzero invariant-respecting holonomy
is:

* two, if some labelled parallel-edge digon has
  \({\bf H}_{a;\lambda,\mu}\ne0\);
* otherwise the length of the shortest simple cycle with nonzero
  curvature; in particular four if some compatible rectangle has
  nonzero curvature.

If every labelled digon and every member of a simple-cycle basis has
zero curvature, then every compound circulation has zero literal
derivative.  Equivalently, the edge derivative is a flat abelian
connection: after fixing one vertex in each component, there are vertex
potentials \({\bf P}_v\) with

\[
                         {\bf D}(u\to v)
                              ={\bf P}_v-{\bf P}_u.                 \tag{8B.7}
\]

In that case no compound slab circuit, of any size, can correct a
literal target discrepancy.

#### Proof

The minimum statement combines Proposition 8A.2 with Theorem 8B.2.
If every generator has zero image, the entire circulation module has
zero image.  Conversely, vanishing on all cycles makes the path sum of
\({\bf D}\) independent of the path from a fixed root, defining the
potentials in (8B.7). \(\square\)

The actual local compatibility graph admits a stronger rectangle
reduction.  Relabel one rank-\(k\) macroblock so that

\[
                         M_k=\{a_tc_t:t\in[d]\}.                    \tag{8B.8}
\]

Its old-direction vertices are \(t\in[d]\), its nonmatching cross-half
vertices are ordered pairs \((p,q)\) with \(p\ne q\), representing
\(e_{p,q}=\{a_p,c_q\}\), and compatibility is

\[
                         t\sim(p,q)
                         \quad\Longleftrightarrow\quad
                         t\notin\{p,q\}.                           \tag{8B.9}
\]

### Theorem 8B.4 (local rectangle span)

For \(d\ge5\), the graph in (8B.9) is connected, has degrees

\[
             \deg(t)=(d-1)(d-2),\qquad
             \deg(p,q)=d-2,                                      \tag{8B.10}
\]

and its integral cycle lattice is generated by its four-cycles.
Therefore:

1. if every labelled digon is flat but some local compound circuit has
   nonzero literal holonomy, some four-slab rectangle already has
   nonzero holonomy; and
2. if every labelled digon and every compatible rectangle is flat, then
   every local compound circuit is flat.

#### Proof

The degree formulas follow from (8B.9).  Any two left vertices have a
common right neighbour: choose two distinct indices outside them.  Every
right vertex has a left neighbour, proving connectedness.

Let \(w_{t,r}\in\mathbb Q\) be an edge weighting which annihilates every
oriented rectangle.  If \(t,u\) are left vertices and \(r,s\) are right
vertices adjacent to both, the rectangle relation gives

\[
                         w_{t,r}-w_{u,r}
                           =w_{t,s}-w_{u,s}.                        \tag{8B.11}
\]

Call this common difference \(A_{t,u}\).  For any three left vertices
\(t,u,v\), there is a right vertex avoiding all three because at least
two indices remain when \(d\ge5\).  Evaluating at that common neighbour
gives

\[
                         A_{t,u}+A_{u,v}=A_{t,v}.                   \tag{8B.12}
\]

Hence \(A_{t,u}=A_t-A_u\) for suitable vertex potentials \(A_t\).
Equation (8B.11) then shows that

\[
                         w_{t,r}=A_t+B_r                            \tag{8B.13}
\]

on every edge, for suitable right-vertex potentials \(B_r\).  Thus the
orthogonal complement of the rectangle span is exactly the cut space.
Taking orthogonal complements proves that rectangles span the rational
cycle space.

To upgrade this integrally, choose once and for all, for every unordered
left pair \(\{t,u\}\), a right vertex \(r_{t,u}\) adjacent to both.
In an oriented bipartite cycle, a rectangle replaces each two-edge path

\[
                         t-r-u
\]

by the reference path \(t-r_{t,u}-u\).  The resulting left-vertex
polygon is an integral sum of the fan triangles
\((t_1,t_j,t_{j+1})\).  For one such triangle \((a,b,c)\), choose a
right vertex \(r\) adjacent to all three; this is possible because two
indices remain outside \(\{a,b,c\}\).  Three rectangles replace its
three reference paths by

\[
                         a-r-b,\qquad b-r-c,\qquad c-r-a.
\]

These six oriented edges cancel in pairs.  Hence every lifted triangle,
and therefore every integral cycle, is an integral sum of rectangles.
The decorated statement follows after adding the parallel-label digons
from Theorem 8B.2. \(\square\)

Consequently, writing \(\Lambda^{\rm cp,loc}_{\le H}\) for the
restriction of (8A.1) to this local atlas,

\[
 \Lambda^{\rm cp,loc}_{\le H}
  =\left\langle
       \text{labelled-digon profiles, rectangle profiles}
    \right\rangle_{\mathbb Z}.                                   \tag{8B.14}
\]

The harmonic multiplicity ranks \(U_j^{\rm cp}\) therefore need only
these two template classes.  Longer carrier cycles can aid
owner-disjoint packing, but cannot add even an integral carrier-image
direction.  This does not determine the Smith index of (8B.14) inside
the much larger ideal Johnson/literal target lattice.

Nonzero curvature is necessary to move literal loads, but not sufficient
to reduce collisions.  Let \(\delta_1,\ldots,\delta_k\) be the literal
derivatives of an owner-disjoint circuit at one typed depth, and let
\(d_t\) be its current one-slab collision cost.  Exact expansion gives

\[
 \boxed{
 \Delta{\cal C}
   =\sum_{t=1}^k d_t
      +\sum_{1\le t<u\le k}\langle\delta_t,\delta_u\rangle.}       \tag{8B.15}
\]

At a one-slab local minimum all \(d_t\ge0\).  Hence a compound circuit
breaks the local holonomy exactly when its negative cross-interaction
exceeds the sum of its one-slab costs.  For the minimal labelled digon
this condition is

\[
                         \langle\delta_1,\delta_2\rangle
                             <-d_1-d_2.                            \tag{8B.16}
\]

For a common all-depth objective, (8B.15)--(8B.16) hold with the weighted
inner product

\[
 \langle\delta_t,\delta_u\rangle_w
   =\sum_{\epsilon,q}w_{\epsilon,q}
       \langle\delta_{t,\epsilon,q},
              \delta_{u,\epsilon,q}\rangle.                       \tag{8B.17}
\]

### Proposition 8B.5 (separated digons cannot break a local minimum)

Suppose two owner-disjoint parallel slabs have the same physical active
axis set and are separated by a frozen coordinate which is pinned to
opposite values on the two slabs.  Then every lower and upper trace in
one slab retains that coordinate, so the two slabs' literal target
images are disjoint at every controlled depth.  Consequently

\[
                 \langle\delta_{1,\epsilon,q},
                         \delta_{2,\epsilon,q}\rangle=0
                 \quad\text{for every }\epsilon,q.                \tag{8B.18}
\]

Such a digon has nonzero curvature—each primitive has nonzero direction
marginal and the two derivative supports are disjoint—but at a one-slab local minimum its compound
energy change is \(d_1+d_2\ge0\).  It cannot break the local minimum.

#### Proof

Compiler traces move only along active swap pairs.  The separating
coordinate is inactive and hence survives unchanged in every literal
lower or upper target.  Opposite pins therefore separate the two target
catalogues.  Their derivative supports are disjoint, proving (8B.18).
Equation (8B.15) now has no mixed term. \(\square\)

Thus an energy-useful labelled digon must be *trace-overlapping*: no
frozen coordinate may separate its two target families.  This is a
strictly stronger requirement than equality of the carrier edge and is
not supplied by the slab reachability theorem.

### Proposition 8B.6 (complete four-slab topology)

Measured with multiplicity, every nonzero decorated circulation using at
most four slabs is one of the following:

1. a two-slab labelled digon;
2. a four-slab simple rectangle; or
3. a sum of two labelled digons.

In particular, if no two-slab digon satisfies (8B.16), no three-slab
invariant-respecting correction exists.  The first remaining compound
energy candidates have four slabs and are exactly the last two types.
Both preserve every histogram in Theorem 8B.1 and use
\(2^{R+3}\) owners.

#### Proof

Project a decorated circulation to the simple graph by summing over
parallel decorations.  If the projection is zero, the circulation is a
sum of parallel-edge differences; with total multiplicity at most four,
it is one or two digons.  If the projection is nonzero, a simple
bipartite circulation has even length at least four.  Equality forces a
four-cycle.  The owner count is four times \(2^{R+1}\). \(\square\)

Thus the absence of a useful single digon does not by itself isolate the
rectangle: two individually useless separated digons may still have a
negative cross-interaction with each other.  Formula (8B.15) is the
exact audit for both four-slab topologies.

The two-slab set-system trap from the slab-energy audit can be oriented
as a labelled digon.  With disjoint \(X,Y\), \(|X|=|Y|=K\ge2\), use

\[
 A_1=X+a,\quad B_1=Y+c,qquad
 A_2=Y+b,\quad B_2=X+d.                                            \tag{8B.19}
\]

Against a fixed background containing \(a,b\), both one-slab costs are
\(K-1>0\), while

\[
                         \langle\delta_1,\delta_2\rangle=-2K.      \tag{8B.20}
\]

Thus the two-slab circuit changes collision energy by \(-2\), even
though each constituent move is strictly uphill.  The occurrence
directions may be assigned opposite audited marginals
\(\alpha_q(e_e-e_i)\) and \(-\alpha_q(e_e-e_i)\); all invariants in
Theorem 8B.1 are then respected exactly.  This proves that the residue
ledger does not forbid a minimal holonomy-breaking digon at the abstract
incidence level.  It does **not** prove that (8B.19) is a literal
diverse-compiler pair.  The remaining positive gate is to exhibit a
literal labelled digon satisfying (8B.16), or, if all digons are flat, a
literal rectangle satisfying the four-slab version of (8B.15).

## 9. Audited boundary

Proved:

* the exact minimum Johnson support exchange;
* index-one generation of every fixed-depth support lattice;
* index-one generation of the abstract antipodal literal-face lattice;
* an exact owner-preserving packet implementation by coordinate
  conjugation;
* an exact Hamming-two cross-parent slab primitive and its reduction to
  decorated carrier circulations;
* the two-slab labelled-digon/four-slab rectangle minimality dichotomy;
* an exact cross-parent cycle-image lattice, including the distinction
  between support and literal orientation cokernels;
* the full residue/component/cross-depth/two-sign invariant ledger and
  the equivalence of depth-one and all-depth circuit closure;
* integral generation of compound holonomy by labelled digons and a
  simple-graph cycle basis, with a sharp flatness obstruction;
* index-one integral rectangle generation for the actual local
  compatibility graph when \(d\ge5\);
* an exact energy test for holonomy breaking and an abstract strict
  two-slab example respecting every projected invariant;
* a literal no-go for parallel digons separated by a frozen exterior
  tag: their cooperative collision term is exactly zero;
* a complete classification of invariant-respecting circuits through
  four slabs: digon, rectangle, or two-digon quartet;
* a fixed-depth harmonic span criterion; and
* a simultaneous all-depth harmonic criterion with an explicit stable
  invariant when it fails.

Not proved:

* a physical packet trade whose derivative is one isolated minimal
  support square with independently prescribed orientations;
* surjectivity of \(\Phi_q\), \(\Phi_{\le H}\), or
  \(\widehat\Phi_{\le H}\) for the certified diverse-order labels;
* the Smith index of the actual diverse compiler orbit lattice;
* condition (8.5) or (8A.5) for the current compiler library;
* a positive-density owner-disjoint embedding of the required decorated
  circulations in the rank-twisted macroblock tiling;
* a literal compiler digon, rectangle, or two-digon quartet with negative
  compound energy at every bad local minimum;
* existence and abundance of trace-overlapping, rather than merely
  carrier-parallel, slab copies;
* an owner-disjoint packing of the signed packet trades with \(o(W)\)
  duplicate/interface cost; or
* a common all-depth integral absorber.

The exact next audit is now the decorated-curvature calculation: derive
the literal vectors \({\bf H}_{a;\lambda,\mu}\) for a labelled digon and
\({\bf H}_C\) for a compatible rectangle.  If all are zero, Corollary
8B.3 closes this slab route negatively.  If one is nonzero, test the
energy inequality (8B.16) for digons, rectangles, and two-digon
quartets, then the multiplicity ranks \(U_j^{\rm cp}\) and
the integral Smith index.  Full rational rank still leaves the literal
orientation and owner-packing gates.
