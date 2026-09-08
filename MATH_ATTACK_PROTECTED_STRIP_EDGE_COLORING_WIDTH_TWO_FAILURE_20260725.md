# Protected-strip integral edge coloring: the width-two moment is not a resolution theorem

Date: 2026-07-25

Method: pure mathematics only.

## 0. Verdict

Scale a rational protected-strip fractional point to a path
multihypergraph \(\mathcal H\).  Its vertices consist of tags and protected
targets, and every path-copy is an edge.  Suppose that

\[
 d_{\mathcal H}(U)=D\quad(U\text{ a tag}),
 \qquad
 d_{\mathcal H}(v)\le D+o(D)\quad(v\text{ a target}).
 \tag{0.1}
\]

A proper edge coloring with only

\[
 D\bigl(1+o(1/Q)\bigr)
 \tag{0.2}
\]

colors would finish the integral extraction without a separate
chain-aligned reserve.  The weaker bound \((1+o(1))D\) need not: an
averaged color may miss \(o(T)\), but not \(o(T/Q)\), tags.  The protected
width-two exponential census does **not** imply even the weaker coloring
from the exact degree ledger (0.1).  There is a sharp obstruction in which

* the fractional point is exact at every tag and respects every target
  capacity;
* any two distinct path-edges meet in at most one vertex, so every nonlinear
  width-two intersection moment is identically zero; but
* the chromatic index divided by \(D\) is at least the projective ratio
  \((K^2-K+1)/\mu\), and a matching covers at most the reciprocal fraction
  of the tags.

The obstruction is a projective-plane block.  Thus a proof based only on
tag degrees, target degrees, and the width-two moment is invalid.

The corrected pointwise pruning parameters are

\[
 \delta=m^{-2/3},
 \qquad L=Qm^{2/3}\log m,
 \qquad \mu=m^{11/6-o(1)}.
 \tag{0.3}
\]

Outside \(o(W)\) protected targets and \(o(T/Q)\) tags, the uniform fibre
point has target load at most \(1+3\delta\).  Scaling it by
\((1+3\delta)^{-1}\) gives a genuine fractional matching whose total tag
deficit is

\[
 O(\delta T)+o(T/Q)=o(T/Q),
 \tag{0.4}
\]

because \(Q\delta=o(1)\).  This closes the pointwise fractional-capacity
gate at the coefficient-one accuracy.

It does **not** remove the singleton obstruction numerically.  With
\(K=gQ=m^{1+o(1)}\),

\[
 {K^2\over\mu}=m^{1/6+o(1)}\longrightarrow\infty.
 \tag{0.5}
\]

A parameter-matched projective construction has \(\mu\) distinct choices
per tag, target load at most one, zero nonlinear intersection moment, and
maximum matching covering only \(O(\mu/K^2)=o(1)\) of its tags.  Hence the
actual scale does not itself exclude the projective weighted matching cut.
Specific rotor/gap incidence must do so.

The distinction between \(D\) and \(\mu\) is essential.  The integer scale
\(D\) is a common denominator and may be enlarged by parallel repetition;
the intrinsic condition is

\[
 K^2\max_e x_e=o(1),
 \quad\hbox{or equivalently}\quad
 \rho K^2=o(D),
 \tag{0.6}
\]

where \(\rho\) is the maximum multiplicity of one distinct path after
scaling.  A claim based only on \(K^2=o(D)\) would be invalid.  Under the
pointwise tuning, even this intrinsic sufficient exclusion fails:
\(\max x_e\asymp1/\mu\) and \(K^2/\mu\to\infty\).

## 1. Exact pointwise and coefficient-scale ledger

Let \(\mathcal T_g\) be the good tags and \(V_g\) the nonexceptional
targets supplied by the pointwise pruning.  Then

\[
 |\mathcal T\setminus\mathcal T_g|=o(T/Q),
 \qquad |V\setminus V_g|=o(W),
 \tag{1.1}
\]

the omitted targets carry \(o(W)\) total fractional incidence, and the
uniform fibre point satisfies

\[
 \sum_{e\ni U}x_e=1\quad(U\in\mathcal T_g),
 \qquad
 \sum_{e\ni v}x_e\le1+3\delta\quad(v\in V_g).
 \tag{1.2}
\]

Choose a common denominator \(D\) and replace a distinct path \(e\) by
exactly

\[
 m_e=Dx_e\in\mathbb Z_{\ge0}
 \tag{1.3}
\]

copies.  There is no floor loss.  Equation (1.2) becomes

\[
 \sum_{e\ni U}m_e=D,
 \qquad
 \sum_{e\ni v}m_e\le D(1+3\delta).
 \tag{1.4}
\]

Enlarging \(D\) only repeats this same rational multihypergraph.  It does
not improve any normalized weighted matching cut or add distinct-support
incidence.  (The purely integral gap above the fractional chromatic number
can decrease under repetition.)  This is why the structural hypotheses
used below are stated invariantly under common scaling.  Alternatively,
replace \(x_e\) by
\(x_e/(1+3\delta)\).  This gives target capacity exactly one and loses tag
mass

\[
 {3\delta\over1+3\delta}|\mathcal T_g|
   +o(T/Q)=o(T/Q).
 \tag{1.5}
\]

Now write \(T_g=|\mathcal T_g|\).  Since each edge contains exactly one
tag, the unscaled tag-saturating multihypergraph has

\[
 |E(\mathcal H)|=T_gD.
 \tag{1.6}
\]

Each color class in a proper edge coloring is a matching simultaneously in
the tag and nonexceptional target coordinates.  If

\[
 C=(1+\varepsilon_m)D,
 \tag{1.7}
\]

let \(r_c\) be the number of good tags missed by color \(c\), and let
\(h_c\) be the total number of incidences of its selected paths with the
exceptional targets.  Put

\[
 I_{\rm exc}
 =\sum_e x_e|C(e)\cap(V\setminus V_g)|=o(W).
 \tag{1.8}
\]

Every tag has one edge in each of \(D\) distinct colors.  Double counting
therefore gives the exact ledgers

\[
 \sum_{c=1}^C r_c=T_g(C-D),
 \qquad
 \sum_{c=1}^C h_c=DI_{\rm exc}=o(DW).
 \tag{1.9}
\]

If

\[
 \boxed{\varepsilon_m=o(1/Q),}
 \tag{1.10}
\]

then the two averages
\(\bar r=C^{-1}\sum_c r_c\) and
\(\bar h=C^{-1}\sum_c h_c\) are \(o(T/Q)\) and \(o(W)\).  If both are
positive, some color has
\(r_c/\bar r+h_c/\bar h\le2\); if either is zero, its corresponding
variable vanishes for every color.  Hence some one color simultaneously
satisfies

\[
 r_c=o(T/Q),
 \qquad h_c=o(W).
 \tag{1.11}
\]

Adding the exceptional tags still gives \(o(T/Q)\) missed tags.  Thus the
no-reserve route requires (1.10), not merely \(\varepsilon_m=o(1)\).
This accuracy is compatible with the target degree in (1.4), because
\(3Q\delta=o(1)\).  If \(r=o(T/Q)\) tags are missed, their total
protected-claim ledger is

\[
 Kr=O(gQ)\,o(T/Q)=o(gT)=o(W).
 \tag{1.12}
\]

With only \(r=o(T)\), the same estimate can be as large as \(o(QW)\).
Such a leave is coefficient-safe only after a separate chain-aligned
reserve theorem.  Coloring all scaled copies is stronger than finding one
integral matching; the strength and the \(1/Q\) accuracy must both be
justified.

## 2. The moment that the strip census controls

For two edge-copies \(e,f\) on different tags, write \(I(e,f)\) for their
common protected targets.  Same-tag copies already lie in one exact clique
of size \(D\); the protected-strip census concerns the additional
cross-tag conflicts.  The nonlinear part of its exponential intersection
census is

\[
 \Phi_w(e,f)
 =w^{|I(e,f)|}-1-(w-1)|I(e,f)|,
 \qquad w\ge1.
 \tag{2.1}
\]

It vanishes when \(|I(e,f)|=0\) or \(1\).  Its quadratic shadow is

\[
 M_2(e)=\sum_{\operatorname{tag}(f)\ne\operatorname{tag}(e)}
              \binom{|I(e,f)|}{2}
       =\sum_{\{x,y\}\subset e}d_{\ne\operatorname{tag}(e)}(x,y),
 \tag{2.2}
\]

where the pair-codegree on the right counts only other tag fibres.  Thus
the width-two hierarchy is strong information
about **repeated** intersections.  It gives no information at all about a
family in which every pair of edges has a different singleton
intersection.  The next theorem realizes exactly that failure while
preserving (0.1).

The multiplicity transfer is exact.  If \(f\) denotes a distinct path
support and \(\widetilde f\) ranges over its \(m_f=Dx_f\) copies, then

\[
 {1\over D}
 \sum_{\substack{\widetilde f:\\
                  \operatorname{tag}(f)\ne\operatorname{tag}(e)}}
 \Phi_w(e,\widetilde f)
 =
 \sum_{\substack{f:\\
                  \operatorname{tag}(f)\ne\operatorname{tag}(e)}}
 x_f\Phi_w(e,f).
 \tag{2.3}
\]

Thus the census needed after scaling is its \(x\)-weighted form.  An
unweighted moment normalized by the raw catalogue degree cannot be
substituted without checking how the fractional point redistributes mass.

## 3. Exact counterexample

### Theorem 3.1 (parameter-matched projective weighted cut)

Let \(q\) be a prime power and put

\[
 k=q+1,
 \qquad N=q^2+q+1=k^2-k+1.
 \tag{3.1}
\]

For every integer \(R\) with \(k\le R\le N\), there is a tag-target
hypergraph with \(N\) tags and exactly \(R\) distinct edges above every
tag such that

\[
 d(U)=R,
 \qquad d(v)=k\le R,
 \tag{3.2}
\]

the uniform fibre weight \(x_e=1/R\) is a genuine fractional matching,
and every two supports on different tags meet in at most one target.
Nevertheless

\[
 \boxed{\nu(\mathcal P_{q,R})\le R,}
 \qquad
 \boxed{\chi'(\mathcal P_{q,R})\ge N.}
 \tag{3.3}
\]

After scaling by any common denominator \(D\) divisible by \(R\), the
tag degree is \(D\), the target degree is \(Dk/R\le D\), and

\[
 \boxed{
 \chi'(\mathcal P_{q,R}^{(D)})
 \ge {DN\over R},
 \qquad
 {\chi'\over D}\ge {N\over R}.}
 \tag{3.4}
\]

For the all-ones weight vector, the exact weighted matching ratio is also
at least \(DN/R\).

#### Proof

Take \(R\) pairwise disjoint projective planes
\(\Pi_1,\ldots,\Pi_R\) of order \(q\).  Each plane has \(N\) points and
\(N\) lines; every line has \(k\) points, every point lies on \(k\) lines,
and two different lines meet in one point.

Create tags \(U_1,\ldots,U_N\).  In each \(\Pi_i\), choose an arbitrary
bijection \(j\mapsto L_{i,j}\) from the tags to the lines, and put

\[
 e_{i,j}=\{U_j\}\cup L_{i,j}.
 \tag{3.5}
\]

For fixed \(j\), the \(R\) edges \(e_{1,j},\ldots,e_{R,j}\) are exactly
the edges through \(U_j\).  A target point lies on \(k\) lines in its one
plane.  This proves (3.2), and weight \(1/R\) has tag load one and target
load \(k/R\le1\).

Supports over different planes have no common target.  Two supports in
one plane and on different tags meet in their unique projective point.
Hence

\[
 \Phi_w(e,f)=0
 \qquad
 \bigl(\operatorname{tag}(e)\ne\operatorname{tag}(f),\ w\ge1\bigr),
 \tag{3.6}
\]

and the complete nonlinear width-two moment is zero.

A matching uses at most one edge from each plane, because all lines within
one projective plane pairwise meet.  Hence its size is at most \(R\).  For
fixed \(i\), the \(N\) edges \(e_{i,1},\ldots,e_{i,N}\) form a clique, so
\(\chi'\ge N\).  This proves (3.3).

In the \(D\)-scaled multihypergraph each support has multiplicity
\(D/R\).  A fixed plane is now a clique of size \(DN/R\), proving (3.4).
There are \(DN\) edge-copies in total and every matching still has at most
\(R\) copies.  Taking weight one on every copy therefore gives weighted
ratio at least \(DN/R\). \(\square\)

Private targets may pad every support to any common rank \(K\ge k\), and
the construction may be repeated in disjoint blocks to obtain arbitrarily
many tags.  Neither operation changes the matching fraction \(R/N\), the
nonlinear moments, or the normalized coloring lower bound \(N/R\).

At the corrected protected-strip scales, take \(R\asymp\mu\) and a prime
power scale \(k\asymp K\).  Since

\[
 {N\over R}\asymp {K^2\over\mu}=m^{1/6+o(1)},
 \tag{3.7}
\]

the abstract obstruction is compatible with the available number of
distinct choices per tag and is much stronger than the required
\(1+o(1/Q)\) accuracy.  It is not an embedding into the geodesic
catalogue: it isolates the global singleton-intersection property that a
rotor proof must exclude.

## 4. Why this is the sharp singleton-intersection obstruction

The projective plane is extremal at the natural \(K^2\) scale.

### Lemma 4.1 (linear intersecting-family bound)

Let \(\mathcal F\) be a family of sets of size at most \(K\), any two of
which meet in at most one point.  If \(\mathcal F\) is pairwise intersecting,
then either all its members contain one common point or

\[
 \boxed{|\mathcal F|\le K^2-K+1.}
 \tag{4.1}
\]

#### Proof

If \(|\mathcal F|\le1\), the assertion is immediate.  Otherwise choose
distinct \(A,B\in\mathcal F\).  Pairwise intersection and linearity give
\(A\cap B=\{x\}\).  Because the whole family is not a star, choose
\(F\in\mathcal F\) with \(x\notin F\).

Every member containing \(x\) must meet \(F\).  Two such members cannot
meet \(F\) in the same point, since they would then share that point and
\(x\).  Hence at most \(|F|\le K\) members contain \(x\).

Every member \(E\) not containing \(x\) meets \(A\) and \(B\) in unique
points \(a_E\) and \(b_E\), and determines the ordered pair

\[
 (a_E,b_E)\in(A\setminus\{x\})
              \times(B\setminus\{x\}).
 \tag{4.2}
\]

The map is injective: two members with the same ordered pair would share
two points.  There are at most \((K-1)^2\) such pairs.  Adding the two
classes gives

\[
 |\mathcal F|\le K+(K-1)^2=K^2-K+1.
\]

\(\square\)

The lines of a projective plane of order \(K-1\) attain equality.  For the
corrected pointwise-pruned catalogue,

\[
 {K^2\over \mu}
 ={m^{2+o(1)}\over m^{11/6-o(1)}}
 =m^{1/6+o(1)}.
 \tag{4.3}
\]

For the point constructed by uniformizing each good retained fibre,
\(x_e=1/A'_U\le((1-\delta)\mu)^{-1}\).  If \(m_e=Dx_e\) is
integral and
\(\rho=\max_e m_e\), then

\[
 \rho\le {D\over(1-\delta)\mu},
 \qquad
 \rho(K^2-K+1)\le
 {D(K^2-K+1)\over(1-\delta)\mu}.
 \tag{4.4}
\]

The right side is \(D m^{1/6+o(1)}\), not \(o(D)\).  Theorem 3.1 realizes
this order with \(R\asymp\mu\).  Thus the extremal linear-family lemma now
confirms, rather than excludes, the projective obstruction at the protected
parameter scale.  The calculation is invariant under enlarging the common
denominator \(D\).

The protected pruning only says that a common-target poset has width at
most two; it does not prevent different edge pairs from meeting at
different singleton targets.  The exponential moment makes multiple
intersections sparse in an averaged sense, but it is exactly zero on this
projective geometry.  A successful rotor census needs an additional
global dispersal statement stronger than Lemma 4.1.

## 5. The exact cut missed by vertex capacities

Let \(e\) now index distinct path supports and let \(m_e=Dx_e\) be their
integer multiplicities.  Let \(\mathfrak M\) be the family of matchings of
distinct supports in the tag and nonexceptional-target coordinates.  The
exact fractional edge-chromatic number of this demand vector is

\[
 \chi_f'(\mathcal H,m)
 =\min\left\{
   \sum_{M\in\mathfrak M}\lambda_M:
   \sum_{M\ni e}\lambda_M\ge m_e,
   \ \lambda_M\ge0
 \right\}.
 \tag{5.1}
\]

Linear-programming duality gives

\[
 \boxed{
 \chi_f'(\mathcal H,m)
 =\max_{y_e\ge0}
 {\sum_e m_ey_e\over
  \max_{M\in\mathfrak M}\sum_{e\in M}y_e}.}
 \tag{5.2}
\]

Thus the exact no-reserve weighted cut is

\[
 \boxed{
 \sum_e m_ey_e
 \le D\bigl(1+\eta_m\bigr)
 \max_{M\in\mathfrak M}\sum_{e\in M}y_e
 \quad(y_e\ge0),
 \qquad \eta_m=o(1/Q).}
 \tag{EC_Q}
\]

Since \(m_e=Dx_e\), its scale-free form is

\[
 \boxed{
 \sum_e x_ey_e
 \le \bigl(1+o(1/Q)\bigr)
 \max_{M\in\mathfrak M}\sum_{e\in M}y_e.}
 \tag{5.3}
\]

The pointwise vertex inequalities (1.2) test only tag and target stars.
They do not test (5.3) for a general \(y\).

### Lemma 5.1 (the weighted cut has exact integral rounding)

Condition \((EC_Q)\) is necessary for a proper coloring with
\(D(1+o(1/Q))\) colors.  Conversely, if \((EC_Q)\) holds, then some common
integer blow-up of the demand vector has a proper coloring with the same
normalized number of colors.

#### Proof

Every integral coloring is feasible in (5.1), proving necessity via
(5.2).  Conversely, take a rational optimum \((\lambda_M)\) in (5.1) and
clear its denominators by an integer \(b\).  Use \(b\lambda_M\) copies of
matching \(M\) as colors.  If a support is covered more than \(bm_e\)
times, delete it from surplus matching copies.  This properly colors the
\(b\)-fold demand using

\[
 b\chi_f'(\mathcal H,m)
 \le bD(1+\eta_m)
 \tag{5.4}
\]

colors.  The extra factor \(b\) may be folded into the initial common
denominator \(D\), so the final object is integral. \(\square\)

Taking \(y_e\equiv1\) in \((EC_Q)\) gives the necessary direct matching
bound

\[
 \nu(\mathcal H)
 \ge {T_g\over1+\eta_m}
 =T_g-o(T/Q).
 \tag{5.5}
\]

Theorem 3.1 violates this all-ones instance already.  In its \(D\)-scaled
form,

\[
 \sum_e m_e=DN,
 \qquad
 \max_M|M|\le R,
 \qquad
 {\sum_e m_e\over D\max_M|M|}
 \ge {N\over R}\asymp {K^2\over\mu}.
 \tag{5.6}
\]

Thus the singleton/projective obstruction is exactly a weighted matching
cut, not an integral-rounding error.

## 6. The two exact coefficient-one routes

### 6.1 No chain-aligned reserve

It is enough, and weaker than a full coloring, to prove directly that the
actual protected rotor hypergraph has a matching satisfying the two
ledgers

\[
 \boxed{|M|=T_g-o(T/Q),}
 \qquad
 \boxed{
  \sum_{e\in M}|C(e)\cap(V\setminus V_g)|=o(W).}
 \tag{6.1}
\]

Equation (1.12) and the second part of (6.1) then give total physical cost
\(o(W)\).  Any coloring-by-averaging proof of (6.1) must have palette
excess \(o(D/Q)\), equivalently relative excess \(o(1/Q)\).

A sufficient stronger theorem is the weighted rotor cut \((EC_Q)\).
By Lemma 5.1 it yields an integral proper coloring after one common
rational blow-up, and the two-ledger averaging in (1.9)--(1.11) supplies a
color satisfying (6.1).  No
fixed-uniformity coloring black box is involved in this final rounding.

### 6.2 With a chain-aligned reserve

One may weaken (6.1) only by proving separately that the omitted tags and
their correlated protected-row claims can be completed for \(o(W)\)
literal cost.  Tag count \(o(T)\) alone is not such a theorem: the crude
leave is \(K\,o(T)=o(QW)\).

In either route the missing catalogue-specific input is a global
singleton-intersection dispersal statement.  It must rule out the weighted
projective cut (5.6), preferably in the hereditary form needed after any
partial palette exposure.  The width-two moment supplies no part of this
for singleton intersections, since every nonlinear summand is zero in
Theorem 3.1.

## 7. Audited conclusion

The sharper isolated pruning does close the fractional capacity gate at
the right coefficient-one accuracy: outside \(o(W)\) targets and
\(o(T/Q)\) tags, loads are at most \(1+3m^{-2/3}\), and rescaling loses
only \(o(T/Q)\) tag mass.

It does not close the integral selection gate.  A color must miss
\(o(T/Q)\), not merely \(o(T)\), tags unless a chain-aligned reserve is
proved.  Accordingly the coloring accuracy is \(1+o(1/Q)\).

At the corrected support degree \(\mu=m^{11/6-o(1)}\), the relation is
\(K^2/\mu=m^{1/6+o(1)}\), so the singleton projective obstruction is
compatible with the raw parameters.  The parameter-matched construction
has target loads at most one and zero width-two nonlinear moment,
yet violates even the all-ones matching cut by this factor.

The sharp remaining theorem is therefore (6.1), or the stronger weighted
cut \((EC_Q)\), proved from the deterministic rotor/gap structure.  Once
\((EC_Q)\) is available, Lemma 5.1 performs the integral rounding exactly.

## 8. Audit of the eight-template Latin absorber

The two-update transport in
`MATH_ATTACK_PSTUBE8_LATIN_TRANSPORT_AND_PROTECTED_STRIP_ABSORBER_20260725.md`
gives a genuine terminal correction reservoir of
\((1/16-o(1))W\) rank-isolated rectangles.  It does not remove the matching
cut above.  A missed chunk tag carries \(K=\Theta(gQ)\) protected claims,
while one rectangle repairs at most two positive units.  Hence even the
entire Latin reservoir can absorb only

\[
 r\le {W\over8K}+o(W/K)=O(T/Q)
\]

missed tags, and the rectangle lattice additionally preserves every
coordinate marginal in each rank.  Thus the absorber can finish a
marginal-balanced \(1-O(1/Q)\) transversal, but it cannot manufacture that
transversal from the fractional multicover or defeat the parameter-matched
projective cut.
