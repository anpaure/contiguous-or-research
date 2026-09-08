# Proportional tight atoms are homogeneous multiradius Pascal bundles

Date: 2026-07-25

This note audits `PROPORTIONAL_TIGHT_ATOM_GAUSSIAN_REDUCTION_20260725.md`
and identifies its matching lemma exactly inside the multiradius buffered-
tower framework.  The result is an equivalence, not a proof of the final
matching assertion.

Put

\[
 n=2m+1,\qquad N_q=\binom{n}{m+q},\qquad
 p=\left\lfloor\frac Wb\right\rfloor,\qquad
 b_q=\left\lfloor\frac{N_q}{p}\right\rfloor.
\]

For large (m), (p>b), and division of (W) by (b) shows in fact

\[
 b_0=b_1=b.
\tag{0.1}
\]

Also binomial symmetry gives

\[
 N_{-d}=N_{d+1},\qquad b_{-d}=b_{d+1}.
\tag{0.2}
\]

## 1. Exact radius differences inside one proportional atom

Define the truncated per-atom radius counts

\[
 a_d=b_{-d}-b_{-(d+1)}\quad(0\le d<H),
 \qquad a_H=b_{-H}.
\tag{1.1}
\]

They are nonnegative because the binomial layers decrease away from the
middle.  If

\[
 \rho(q)=\max\{-q,q-1\},
\tag{1.2}
\]

then telescoping and (0.2) give the exact identity

\[
 \boxed{b_q=\sum_{d=\rho(q)}^H a_d}
 \qquad(-H\le q\le H+1).
\tag{1.3}
\]

Choose a partition

\[
 [0,b-1]=J_0\sqcup\cdots\sqcup J_H,
 \qquad |J_d|=a_d,
\tag{1.4}
\]

and, in the definition of the proportional atom, take

\[
 I_q=\bigcup_{d\ge\rho(q)}J_d.
\tag{1.5}
\]

Then (|I_q|=b_q), exactly as required in the original reduction.

For (i\in J_d), the designated targets belonging to that start are

\[
 A_{i,-d}(x)\subset A_{i,-d+1}(x)\subset\cdots
 \subset A_{i,d+1}(x).
\tag{1.6}
\]

This is a saturated symmetric chain of (B_{2m+1}), from rank (m-d)
to rank (m+d+1=n-(m-d)), hence of radius (d).  Thus one proportional
atom is exactly a bundle containing (a_d) radius-(d) chains for every
(d\le H).

Because (x) is injective, different starts give different intervals of a
fixed length, and different ranks have different cardinalities.  Therefore
all chain vertices inside one atom are distinct.  The atom has the exact
chain count and edge size

\[
 \sum_{d=0}^H a_d=b,
 \qquad
 \sum_{d=0}^H(2d+2)a_d
   =\sum_{q=-H}^{H+1}b_q=\kappa.
\tag{1.7}
\]

## 2. These chains form one tight physical row

Put

\[
 E_j=\{x_j,\ldots,x_{j+m-H-1}\}.
\]

For every designated chain member,

\[
 A_{i,q}=E_i\cup E_{i+1}\cup\cdots\cup E_{i+q+H}.
\tag{2.1}
\]

Hence all the differently truncated chains in (1.6) share one literal
row, of length (b+2H+1).  This is stronger sharing than concatenating a
separate radius-(d) atom for each (d): the initialization is paid once
for the entire radius profile.

There is also a central-walk interpretation.  The (b) rank-(m) windows

\[
 T_i=A_{i,0}=\{x_i,\ldots,x_{i+m-1}\}
\tag{2.2}
\]

form a support-separated Johnson path.  For (i\in J_d), its chain in
(1.6) is precisely the consecutive-intersection/union flag of (T_i),
truncated at radius (d).  Since (b+H<m), the tight-completion lemma
extends this path segment to a cyclic coordinate row; use cyclic indices
for the few windows preceding (T_0).  The exact identities are then

\[
 \boxed{
 A_{i,-q}=\bigcap_{j=0}^qT_{i-j},\qquad
 A_{i,q}=\bigcup_{j=0}^qT_{i+j}.}
\tag{2.3}
\]

In particular, proportional atoms are genuine tight multiradius Pascal
braids, not abstract rankwise boxes.

## 3. Exact equivalence of the matching statements

Call a **homogeneous proportional Pascal bundle** any injective tight row
equipped with the fixed partition (1.4), and containing the target system
(1.6).

### Theorem 3.1 (matching/bundle equivalence)

For every integer (s\), the following are equivalent.

1. The proportional atom hypergraph has a matching of size (s\).
2. There are (s\) homogeneous proportional Pascal bundles whose Boolean
   chain vertices are pairwise disjoint.

Under this bijection, every bundle contains (a_d) radius-(d) chains,
one literal row costs (b+2H+1), and the number of covered targets in rank
(m+q) is exactly (sb_q).

#### Proof

A hyperedge was defined to be one distinct designated target system (1.3).
Equations (1.5)--(1.7) identify that target system with one homogeneous
Pascal bundle.  Two hyperedges are disjoint exactly when their Boolean chain
vertices are disjoint.  The remaining assertions are the exact counts above.
\(\square\)

Consequently the proportional tight-atom matching lemma is *exactly* the
following homogeneous multiradius rounding statement:

> Select (p-o(p/\sqrt m)) disjoint tight rows, every row carrying the
> same truncated radius profile ((a_0,\ldots,a_H)).

This is a special, more rigid form of the multiradius buffered-tower gate.
The latter permits separate paths and nonidentical radius profiles, whereas
the proportional lemma requires all radii in one row and the same floor-
proportional profile in every row.  Thus the general multiradius gate implies
the proportional lemma only if it additionally supplies this homogeneous
row bundling; there is no converse regrouping for free.

In the forward direction the implication is exact.  If
(s=p-t\), the selected bundles have

\[
 W-sb=(W-pb)+tb<b+tb
\tag{3.1a}
\]

uncovered middle owners, and their shared-row initialization cost is

\[
 O(Hs)=O(HW/b)=o(W).
\tag{3.1b}
\]

Thus (t=o(p/\sqrt m)\) supplies the multiradius gate, with more than the
required reset margin.  What fails in reverse is precisely the demand that
heterogeneous radius paths be rebundled into (p) common injective rows
without creating new Boolean collisions.

## 4. Comparison with the exact global radius counts

Let the truncated global symmetric-chain radius counts be

\[
 C_d=N_{-d}-N_{-(d+1)}\quad(d<H),
 \qquad C_H=N_{-H}.
\tag{4.1}
\]

Writing (R_q=N_q-pb_q\), where (0\le R_q<p), gives

\[
 C_d-pa_d=R_{-d}-R_{-(d+1)}\quad(d<H),
 \qquad C_H-pa_H=R_{-H}.
\tag{4.2}
\]

Hence

\[
 |C_d-pa_d|<p,qquad
 \sum_{d=0}^H|C_d-pa_d|=O(Hp).
\tag{4.3}
\]

This is exactly the floor remainder repaired in Theorem 2.1 of the original
note.  The profile is therefore the truncated radius distribution divided
into (p) almost-equal bundles; no additional quota choice is hidden in
the construction.

## 5. What the local overlap row sum actually proves

The (O(1/m)) term has a completely localized source.  In the notation
of (3.1) of the original reduction,

\[
 \boxed{
 \sum_{Q:\,|P\setminus Q|+|Q\setminus P|\ge2}
 \frac1{\binom r{|P\setminus Q|}
          \binom{n-r}{|Q\setminus P|}}
 =O(m^{-2}).}
\tag{5.0}
\]

Indeed, on either axis the first retained term is
(O(1/\binom r2)=O(m^{-2})), and when both differences are positive the
first term is (O(1/(r(n-r)))=O(m^{-2})); the same binomial-series bound
as in the original proof sums the tails.  Hence the entire first-order
(O(1/m)) overlap comes from (a+c=1), namely from two interval slots
which are adjacent by one Boolean cover relation.  After deleting these
vertical nearest-neighbor pairs, the normalized row sum is (O(m^{-2})).

This does not permit simply deleting the cover pairs: they are the links
which make each start a saturated chain.  It does show exactly what a
successful structured coloring must contract or absorb.  All nonvertical
multiple overlaps are already below the (m^{-1/2}) target by a full extra
power of (m).

Numerically, this is precisely the missing square-root gain.  A matching
argument which handled the cover-adjacent grid integrally and exposed only
the residual (O(m^{-2})) codegree would have the nominal parameter

\[
 B\asymp\sqrt{D/D_2}\asymp m,
\]

rather than (B\asymp\sqrt m).  Its natural leave scale would be
(p/m=o(p/\sqrt m)).  Thus no further polynomial saving is needed after
an exact vertical contraction; the whole quantitative gap sits in retaining
the tight-row bundling during that contraction.

Let (F) be a uniformly random labelled atom, and fix an atom (e).  The
row-sum estimate (3.3) of the original note implies the useful second-order
bound

\[
 \boxed{
 \mathbb E\binom{|F\cap e|}{2}
 =O\left(\frac{\kappa}{mp}\right).}
\tag{5.1}
\]

Indeed, a fixed target has atom degree ((1+o(1))E/p); sum the normalized
codegrees first over the other targets in (e), using (3.3), and then over
the (kappa) possible first targets.  Since

\[
 \mathbb E|F\cap e|=(1+o(1))\frac{\kappa}{p},
\tag{5.2}
\]

only an (O(1/m)) fraction of the local conflict mass comes from atoms
meeting (e) in two or more targets.  Equivalently, the line-graph
neighborhood of an atom is a union of (kappa) target cliques whose total
multiple-overlap mass is (O(1/m)).

This is substantially stronger than a maximum-codegree statement.  It is
the correct input for a near-(D) edge-coloring or structured-resolution
theorem: if the atom multihypergraph admitted an edge coloring with

\[
 \chi'\le(1+o(m^{-1/2}))D,
 \qquad D=(1+o(1))E/p,
\tag{5.3}
\]

then the largest color class would be a matching of size

\[
 \frac E{\chi'}=p-o(p/\sqrt m),
\]

proving the desired lemma.

However, (5.1) alone does not justify applying a fixed-rank nibble.  In a
vertex-independent residual of density (delta=m^{-1/2}), a fixed atom is
retained with probability exactly (delta^kappa), while

\[
 \kappa=\Theta(m^{5/4}),
 \qquad \log E=O(m\log m).
\]

Thus (E\delta^kappa=o(1)).  Markov's inequality says that with probability
(1-o(1)) such a residual contains no complete atom at all.  An ordinary
nibble whose leave becomes vertexwise independent therefore necessarily
stalls far before the required scale.
The row-sum estimate says conflicts are almost always single-column; it
does not remove the need to keep the final leave vertically structured.

## 6. Exact remaining theorem

The proportional matching lemma is exactly equivalent to the homogeneous
proportional Pascal-bundle packing of Theorem 3.1.  A near-(D) atom edge
coloring satisfying (5.3) is a stronger sufficient statement, not a reverse
equivalence.

The bundle formulation exposes the relationship with the multiradius
buffered-tower gate; the edge-coloring formulation isolates one way the
(O(1/m)) overlap row sum could be exploited.  A conventional random-
residual nibble proves neither.  The needed new input is a structured
resolution or absorber which preserves the common tight row while reducing
the atom leave to (o(p/\sqrt m)).
